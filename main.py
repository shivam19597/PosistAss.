import hashlib, binascii
import random
import DateTime
#python program 

'''
This is the data class used to create the data objects
which will be part of node.
'''
owner_id = []
node_number = 0
class Data:
  HASH_VALUE = ''
  
  def set_owner_id(self, id);
    self.owner_id = id
  
  def set_value(self, value):
    self.valuelue
    
  def set_owner_name(self,name):
    self.name = name
   
  def get_id(self):
    return self.id
    
  def get_value(self):
    return self.value
  
  def get_owner_name(self):
    return self.name
  
  
    
class Node:

  child_ref = []
  
  HASH_VALUE = ''
  
  def set_time_stamp(self, timestamp):
    self.timestamp = timestamp
    
  def set_data(self,obj):
    self.data = obj
    
  def set_node_number(self, number):
    self.node_number = number
    
  def set_node_id(self, id):
    self.node_id = id
  
  def set_reference_node_id(self, id):
    self.ref_node_id = id
    
  def set_child_ref_node_id(self,id):
    self.child_ref.append(id)
    
  def set_genesis_ref_node_id(self, id):
    self.genesis_id = id
  
class Util:
  def hash(self, *args, **kwargs):
    pass = b''
    r = b''
    for x in range(10):
      r = r + str(random.randint(1,101))
    for i in args:
      pass = pass + str(i)
    
    dk = hashlib.pbkdf2_hmac('sha256', pass, r, 100000)
    return binascii.hexlify(dk)
    
    
if __name__ == __main__:
  option = input('''select from the following options\n
  1.) create Data\n
  2.) exit
 ''')
 
 if (option == 1):
  name = input("Enter your name")
  value = input("Enter Data value")
  submit = input("1.Create\n2.Exit")
  
  if submit == 1:
    data = Data()
    data.set_value = value
    data.set_name = name
    data.owner_id = owner_id
    owner_id += 1
    data.HASH_VALUE = Util().hash(data.get_value(), data.get_owner_id(), data.get_owner_name())
    
    print ('''
          please store these information safely
          1.) key-----------------> data.HASH_VALUE
          2.) owner_id ----------------> data.owner_id
          
          creating Node...
          ''')
          
          node = Node()
          node.set_timeStamp(DateTime.date())
          node.set_data(data)
          node.set_node_number(node_number+=1)
          node.set_node_id(''.join(str(data)+str(random.rand(1,100))))
          node.HASH_VALUE = Util().hash(node.get_timestamp, node.get_data, node.get_node_number)
    
    
  elif submit == 2:
    exit()
  else :
    print "Wrong input"
    exit()
   
 elif option == 2:
  exit()
  
 else:
  print("wrong input")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
