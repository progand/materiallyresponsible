#!/usr/bin/python


import sys
import os 
#sys.path.append(os.environ["DOCUMENT_ROOT"])
from mvc import *
from mvc.commands import *
from mvc.model import *
import cgi
request = cgi.FieldStorage()

#fc = FrontController()
#fc.dispatch()
print Item.getDistinctTypes()