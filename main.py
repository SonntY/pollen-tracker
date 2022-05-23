import requests
import json
import smtplib
import os

#We are checking the tree pollen levels for Haifa for today.

url = "https://air-quality.p.rapidapi.com/current/airquality"
headers = {"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
           "X-RapidAPI-Key": "f19e0ebaf6msh90c9d85d5908c3ap187ae6jsn371e951a2d95",
           'Content-Type': 'application/json;charset=UTF-8'}

params = {
    "lat": "32.794044",
    "lon": "34.989571",
    "hours": 24
}

response = requests.get(url, headers=headers, params=params)

info = response.text
data_dict = json.loads(info)

tree_pollen = int(data_dict["data"][0]["pollen_level_tree"])

#if the tree pollen level is high or very high (3 or 4),
# the person who is allergic will get an email with a warning:

email = "pythonsonn@gmail.com"
password = os.environ.get("my_password")

if tree_pollen > 2:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="tova259@gmail.com",
                     msg="Careful! High tree pollen levels today!"
                         "\nStay at home or wear your protective glasses!")