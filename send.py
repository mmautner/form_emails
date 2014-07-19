#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from secret import USERNAME
from secret import PASSWORD

url = 'http://example.com/stage2'
me = USERNAME
you  = [
    #'joeblow@gmail.com'
    USERNAME
]

msg = MIMEMultipart('alternative')
msg['Subject'] = "Get insurance quotes in seconds!"
msg['From'] = me
msg['To'] = ','.join(you)

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\ncheck us out here: %s" % url
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       We received your inquiry about cheap auto insurance prices--fill out the form 
       and we'll give you your quote instantly!
    </p>
    <form action="%s" method="get">
        <p><label>Interest: <select name="interest">
                          <option value="1">Currently insured, need savings</option>
                          <option value="2">Currently insured, just curious</option>
                          <option value="3">Uninsured, need coverage</option>
                          <option value="4">Uninsured, just curious</option>
                        </select></label></p>
        
        <p><label>Zipcode: <input type="text" name="zipcode" value="02139"></label></p>
        <p><input type="submit" value="Go!"></p>
    </form>
    <p>Yes! Forms-in-emails really works! Give it a try.</p>
    <hr>
    <footer>Car Coverage Gurus &copy; 2014</footer>
  </body>
</html>
""" % url

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(USERNAME, PASSWORD)
server.sendmail(me, you, msg.as_string())
server.quit()
