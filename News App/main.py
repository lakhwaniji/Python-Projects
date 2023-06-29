import requests
import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465
username = "indramohan755@gmail.com"
password = os.getenv("PASSWORD")
reciever = "indramohan755@gmail.com"
url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a3fe02bc6a3a4e309bb54650cd0a2b60&language=en"
request = requests.get(url)
content = request.json()
articles = content["articles"]
body = "Subject: Todays News" \
       + "\n"
for article in articles[:5]:
    body = body + article["title"] + "\n" \
           + article["description"] \
           + "\n" + article["url"] + 2 * "\n"
context = ssl.create_default_context()
body=body.encode("utf-8")
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, body)
