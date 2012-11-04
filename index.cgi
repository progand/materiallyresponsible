#!/usr/bin/python


import sys
import os 
sys.path.append(os.environ["DOCUMENT_ROOT"])
from mvc import FrontController

fc = FrontController()
fc.dispatch()