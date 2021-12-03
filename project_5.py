import hashlib
import json
import time
    
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
    
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = json.dumps(self.__dict__, sort_keys=True).encode('utf-8') #use self.__dict__ as hash_str
      sha.update(hash_str)
      return sha.hexdigest()

    def __str__(self):
        return f"Timestamp: {self.timestamp} \n" + f"Data: {self.data} \n" + f"Hash: {self.hash} \n"

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if self.head == None:
            self.head = Block(time.time(), data, None)
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Block(time.time(), data,  current.hash)
    
    def print_bc(self):
        if not self.head:
            print( "Empty Blockchain！\n")

        else:
            current = self.head
            index = 0
            while current:
                print(f"Block {index}")
                print(current)
                current = current.next
                index += 1

#Test 1 Normal case
print("\n Test 1")
bc = Blockchain()
bc.add_block("data 1")
bc.add_block("data 2")
time.sleep(1)
bc.add_block("data 3")
bc.print_bc()

#Test 1 output

#Block 0
#Timestamp: 1638503897.0707026
#Data: data 1
#Hash: dbd810b5cc496504c8ec603dfc1c110fbaa6b8a34ec83ea2a8b8b231483bdac3

#Block 1
#Timestamp: 1638503897.0707026
#Data: data 2
#Hash: 7fca40985e404b0ca101984a06fb3dda92984372ea4e47663c1321c51be1d8ed

#Block 2
#Timestamp: 1638503898.0842783
#Data: data 3
#Hash: 7e0fa1248a58bf19e1c90f4c3cfa30f4e4e805f00a441cb25c08e554b766d430

#Test 2 Empty BlockChain
print("\n Test 2")
bc = Blockchain()
bc.print_bc()
#Test 2 output

#Empty Blockchain！

#Test 2 #Adding two blockchain with the exact same content
print("\n Test 2")
bc = Blockchain()
bc.add_block("data 1")
bc.add_block("data 1")
bc.print_bc()
#Test 3 output

#Block 0
#Timestamp: 1638503949.6751313
#Data: data 1
#Hash: 49bfa54d6bbcf0f173eef6c415513e70ce3ace84866e8d5bdcb5d90f069f3fdc

#Block 1
#Timestamp: 1638503949.6751313
#Data: data 1
#Hash: 13a154cac4d26033e1038b967f03f617265d35ca6c3b7894f10b147f7c365d4d



