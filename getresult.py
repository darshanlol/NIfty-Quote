import smtplib
from bs4 import BeautifulSoup
import requests
import re
from mechanize import Browser
import mechanize
from bs4 import BeautifulSoup
import pandas as pd
import subprocess

toaddrs  = 'darshanjadav97@gmail.com'
fromaddr = 'uwu.jpeg@gmail.com'
username = 'uwu.jpeg@gmail.com'
password = 'X'

br = mechanize.Browser()
br.open("http://result.saurashtrauniversity.edu/Default1.aspx")
print br.geturl()

br.select_form(nr=0)
control = br.form.find_control("ctl00$ContentPlaceHolder1$ddstr")

for item in control.items:
    if item.name == "BSc_3":
        item.selected = True
        print "BSc_3"       

control1 = br.form.find_control("ctl00$ContentPlaceHolder1$ddyr")
for item1 in control1.items:
    if item1.name == "2016":
        item1.selected = True
        print "2016"

control2 = br.form.find_control("ctl00$ContentPlaceHolder1$ddmon")
for item2 in control2.items:
    if item2.name == "Oct":
        item2.selected = True
        print "Oct"
        
response = br.submit(name="ctl00$ContentPlaceHolder1$ImageButton8")

redir = response.read()

br.select_form(nr=0)
br.form['ctl00$ContentPlaceHolder1$txtseat'] = "036448"

resultresp = br.submit(name="ctl00$ContentPlaceHolder1$imgsearch")



soup = BeautifulSoup(resultresp, "html.parser")


student = soup.find(attrs={'id': "ctl00_ContentPlaceHolder1_lblnm"})
studentname = student.text
print studentname
    





for allmarks in soup.findAll(attrs={'style': "background-color:gray;color:white"}):
    msg = allmarks.text
    print msg
   

for allgrades in soup.findAll(attrs={'style': "background-color:orange;color:White"}):
    msg1 = allgrades.text
    print msg1


