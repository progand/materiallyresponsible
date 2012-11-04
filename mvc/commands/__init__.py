from mvc.model import *
import cgi
import cgitb


class FrontCommand(object):    
    def process(self):
        return
        
class BaseCommand(FrontCommand):
    def __init__(self):
        self.request = cgi.FieldStorage()
        return
    def process(self):
        return   
    
class APICommand(BaseCommand):          
       
    def process(self):
        print "Content-Type: text/javascript"
        print  
        if self.request.has_key('get'):
            if self.request['get'].value=='names':
                self.printNames()
            elif self.request['get'].value=='types':
                print Item.itemsToJSON(Item.getDistinctTypes()) 
            elif self.request['get'].value=='transfer_where':
                print Item.itemsToJSON(Item.getDistinctTransferWhere()) 
            elif self.request['get'].value=='who_took':
                print Item.itemsToJSON(Item.getDistinctWhoTook())  
            elif self.request['get'].value=='who_on_account':
                print Item.itemsToJSON(Item.getDistinctWhoOnAccount())  
                
    def printNames(self):
        print Item.itemsToJSON(Item.getDistinctNames()) 
        
class MyItemsCommand(BaseCommand):
    def process(self):  
            
        if self.request.has_key('get'):
            if self.request['get'].value=='all_items':
                self.allItemsJSON()                  
            elif self.request['get'].value=='names':
                self.printNames()
            elif self.request['get'].value=='types':
                self.printTypes()
            elif self.request['get'].value=='transfer_where':
                self.printTransferWhere() 
            elif self.request['get'].value=='who_took':
                self.printWhoTook()  
            elif self.request['get'].value=='who_on_account':
                self.printWhoOnAccount() 
        else:      
            html = open(config.DOCUMENT_ROOT+"html/my_items.html")  
            print "Content-Type: text/html"
            print
            print html.read()            
    def allItemsJSON(self):
        print "Content-Type: text/javascript"
        print        
        print Item.itemsToJSON(Item.getAll()) 
        
    def printNames(self):
        term = None
        if self.request.has_key('term'):
            term = self.request['term'].value
        print "Content-Type: text/javascript"
        print 
        print Item.itemsToJSON(Item.getDistinctNames(term))  
        
    def printTypes(self):
        term = None
        if self.request.has_key('term'):
            term = self.request['term'].value
        print "Content-Type: text/javascript"
        print 
        print Item.itemsToJSON(Item.getDistinctTypes(term))  
        
    def printTransferWhere(self):
        term = None
        if self.request.has_key('term'):
            term = self.request['term'].value
        print "Content-Type: text/javascript"
        print 
        print Item.itemsToJSON(Item.getDistinctTransferWhere(term))  
        
    def printWhoTook(self):
        term = None
        if self.request.has_key('term'):
            term = self.request['term'].value
        print "Content-Type: text/javascript"
        print 
        print Item.itemsToJSON(Item.getDistinctWhoTook(term))  
        
    def printWhoOnAccount(self):
        term = None
        if self.request.has_key('term'):
            term = self.request['term'].value
        print "Content-Type: text/javascript"
        print 
        print Item.itemsToJSON(Item.getDistinctWhoOnAccount(term))  
        
    