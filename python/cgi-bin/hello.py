# -*- coding: UTF-8 -*-

import cgi, cgitb
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')

print ("Content-type:text/html\n\n")
print (name)
