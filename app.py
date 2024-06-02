from flask import Flask,render_template,request
import sqlite3


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/contact',methods = ["get","POST"])
def contactus():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        state = request.form.get("state")
        country = request.form.get("country")
        message = request.form.get("message")
        print(name,email,state,country,message)
        conn = sqlite3.connect('contactus.db')
        cur = conn.cursor()
        cur.execute(f'''
        INSERT INTO CONTACT VALUES(
                    "{name}","{email}","{state}",
                    "{country}","{message}"
        )
        ''')
        conn.commit()
        return render_template("message.html")
    else:
        return render_template("contactus.html")

if __name__ == "__main__":
    app.run()
