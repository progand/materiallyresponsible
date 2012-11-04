#!/usr/bin/python


import sys
import os 
#sys.path.append(os.environ["DOCUMENT_ROOT"])
from mvc import *
from mvc.commands import *
import cgi
request = cgi.FieldStorage()

#fc = FrontController()
#fc.dispatch()
command = APICommand()
command.printNames()
