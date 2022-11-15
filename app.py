from flask import Flask,render_template,request,redirect
import smtplib

app=Flask(__name__)

#route() decorators
@app.route('/')
def home():
    return "okay"

if __name__=='__main__':
    app.run(debug=True)
