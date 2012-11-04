from mvc.commands import *
import cgi

class FrontController(object):
    def dispatch(self):   
        req = cgi.FieldStorage()
        if req.length<1:
            command = MyItemsCommand()            
        else:
            if req['action'].value=='api':
                command = APICommand()
            else:
                command = MyItemsCommand()
        command.process()