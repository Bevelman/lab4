#!/usr/bin/python37all

# Note that this file must be executed using the Python
# file we created with modified permissions.

# This script requires that the file 'led-slider-multiple.txt' already exists in
# the cgi directory, and has permissions set appropriately (so that the
# Python code can write to the file).

# If needed, create a blank file with the following command:
#   sudo touch /usr/lib/cgi-bin/led-slider-multiple.txt
# and change permissions via:
#   sudo chmod 666 /usr/lib/cgi-bin/led-slider-multiple.txt

import cgi, json

data = cgi.FieldStorage()         # get POST data from led-pwm.html

# set up new data from POST:
led_num = data.getvalue('led')
slider_val = data.getvalue('slider')

# form new dictionary with user data:
fileData = {'led':led_num, 'slider':slider_val}

# write all data to the file:
with open('led-pwm-multiple.txt', 'w') as f:
  json.dump(fileData,f)

# As a bonus, let's display the HTML with the same LED selection
# and slider values from the last user entry (see HTML code below
# to see how these variables are being used in the form):
checked = ['','','']
checked[int(led_num)-1] = 'checked'

# generate new web page:
print("Content-type: text/html\n\n")
print('<html>')
print('<body>')
print('<form action="/cgi-bin/led-pwm-multiple.py" method="POST">')
print('<input type="radio" name="led" value="1" %s> LED 1 <br>' % checked[0])
print('<input type="radio" name="led" value="2" %s> LED 2 <br>' % checked[1])
print('<input type="radio" name="led" value="3" %s> LED 3 <br>' % checked[2])
print('<input type="range" name="slider" min ="0" max="100" value ="%s"><br>' % slider_val)
print('<input type="submit" value="Submit">')
print('</form>')
print('</body>')
print('</html>')