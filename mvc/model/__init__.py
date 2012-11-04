import config
import json
import mysql.connector
from abc import abstractmethod

class Gateway(object):
    
    def __init__(self, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.connection = None
    
    def openConnection(self):
        try:
            cnx = mysql.connector.connect(**config.DB_CONFIG)
            self.connection = cnx
        except:
            return None
    
    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()              
            self.connection = None

    def query(self, query):        
        result = None
        try:
            self.openConnection()
            cursor = self.connection.cursor()            
            cursor.execute(query)
            result = cursor.fetchall()            
        finally:
            self.closeConnection()
        return result
                
    def getSingle(self,query):
        queryResult = self.query(query);
        return queryResult[0][0]
    
    def getVector(self,query):
        queryResult = self.query(query);
        return queryResult[0]
    
    def getMatrix(self,query):
        return self.query(query)
    
class MySQLJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (mysql.connector.datetime.date,mysql.connector.datetime.datetime)):
            return obj.isoformat()       
        elif isinstance(obj, Item):
            return obj.__dict__    
        elif isinstance(obj, Gateway):
            return None  

        return json.JSONEncoder.default(self, obj)
    
    
class Item(object):
    
    def __init__(self, identifier,user_id,name,itemType,inventory,serial,transferred,receipt_date,
                 transfer_date,transfer_where,who_took,who_on_account,notes):
        object.__init__(self)
        self.identifier = identifier
        self.user_id = user_id
        self.name = name
        self.type = itemType
        self.inventory = inventory
        self.serial = serial
        self.transferred = transferred
        self.receipt_date = receipt_date
        self.transfer_date = transfer_date
        self.transfer_where = transfer_where
        self.who_took = who_took
        self.who_on_account = who_on_account
        self.notes = notes    
      
        
    def fromList(lst):
        return Item(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],
                lst[9],lst[10],lst[11],lst[12])  
    fromList = staticmethod(fromList)
        
    def find(identifier):
        gateway = Gateway()
        return Item.fromList(gateway.getVector("select * from items where id='"+str(identifier)+"'"))
    find = staticmethod(find)
        
    def getAll():
        gateway = Gateway()
        matrix =  gateway.getMatrix("select * from items")
        result = []
        for row in matrix:
            result.append(Item.fromList(row))
        return result
    getAll = staticmethod(getAll)
    
    def getDistinct(fieldName):
        gateway = Gateway()
        matrix =  gateway.getMatrix("select min(id) as id, "+fieldName+" from items group by "+fieldName)
        result = []
        for row in matrix:
            result.append((row[0],row[1]))
        return result   
    getDistinct = staticmethod(getDistinct)
    
    def getDistinctNames():        
        return Item.getDistinct('name')   
    getDistinctNames = staticmethod(getDistinctNames)
    
    def getDistinctTypes():        
        return Item.getDistinct('type')   
    getDistinctTypes = staticmethod(getDistinctTypes)
    
    def getDistinctTransferWhere():        
        return Item.getDistinct('transfer_where')   
    getDistinctTransferWhere = staticmethod(getDistinctTransferWhere)
    
    def getDistinctWhoTook():        
        return Item.getDistinct('who_took')   
    getDistinctWhoTook = staticmethod(getDistinctWhoTook)
    
    def getDistinctWhoOnAccount():        
        return Item.getDistinct('who_on_account')   
    getDistinctWhoOnAccount = staticmethod(getDistinctWhoOnAccount)
    
    def toJSON(self):
        return json.dumps(self,cls=MySQLJSONEncoder)
    
    def itemsToJSON(items):
        return json.dumps(items,cls=MySQLJSONEncoder)
    itemsToJSON = staticmethod(itemsToJSON)

