import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC35286ab14ae8ad3e5315b271b846f786'
        auth_token = 'bce26ce3d137b5f1b23abfa9ae71b998'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('IS9f027b3ebbbdd9e8cd9bff177f905143') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
         return render_template('otp_error.html')

# Write the code here
@app.route('/', methods=['POST'])
def download_text():
    text_from_notepad = request.form['text']
    with open('workfile.txt', 'w') as f:
        f.write(text_from_notepad)

    path_to_store_txt = "workfile.txt"

    return send_file(path_to_store_txt, as_attachment=True)
    
    if verification_check.status == "pending":
    	return render_template('otp_error.html')
    else:
    	return redirect("https://project-c272.onrender.com/")

    

    


if __name__ == "__main__":
    app.run(host='localhost', port='5001', debug=True)
