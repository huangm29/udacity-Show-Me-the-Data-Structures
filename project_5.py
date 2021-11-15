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
      hash_str = json.dumps(self.__dict__, sort_keys=True).encode('utf-8')
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
            print( "Empty Blockchain！")

        else:
            current = self.head
            index = 0
            print(f"Block {index}")
            print(current)
            while current:
                print(f"Block {index}")
                print(current)
                current = current.next
                index += 1


bc = Blockchain()
bc.print_bc()
bc.add_block("data 1")
bc.add_block("data 2")
time.sleep(1)
bc.add_block("data 3")
bc.print_bc()






