import sys
from collections import Counter


class Node: #The Node in the Huffman Tree
    def __init__(self, character, frequency):
        self.character = character;
        self.frequency = frequency;
        self.left = None;
        self.right = None;

class HuffmanTree: #Huffman Tree
    def __init__(self, root_node):
        self.root_node = root_node

def encode_huffman_tree(node): 
    encode_dict = {} 
    if (node.left is None and node.right is None): #When leaf node is reached
            encode_dict[node.character] = ""
    else:
        if node.left is not None: # search along the tree
            return_dict = encode_huffman_tree(node.left)
            for keys in return_dict :
                encode_dict[keys] = '0' + return_dict[keys]
        if node.right is not None:
            return_dict =  encode_huffman_tree(node.right)
            for keys in return_dict :
                encode_dict[keys] = '1' + return_dict[keys]
    return encode_dict


def huffman_encoding(data):

    priority_list = list()
    freq_map = Counter(data).most_common() # Sort the word with its frequency, when two words have equal frequency, it does not matter which one comes first
    for item in freq_map:
        priority_list.append(Node(item[0],item[1])) #Append the node with string and key

    if len(priority_list) < 2: 
        print("Warning: The huffman coding does not work for sentences consistent of less than 2 characters!")        
        if len(priority_list) == 0:
            root_node = Node("", 0)
        else:
            priority_list.append(priority_list[0]) #A trick for single character case
    
    while(len(priority_list) > 1):
        first_node = priority_list.pop()
        second_node = priority_list.pop() #pop-out two nodes
        sum_freq = first_node.frequency + second_node.frequency
        sum_string = first_node.character + second_node.character # This is not required, but the name of string is also summed in this case
        root_node = Node(sum_string , sum_freq) # create a new node
        root_node.left = first_node
        root_node.right = second_node
        
        index = 0 # If there are only two letters in the code
        for index in range(len(priority_list)): 
            if priority_list[index].frequency < sum_freq: 
                break

        if index + 1 == len(priority_list) and priority_list[index].frequency > sum_freq:
            priority_list.append(root_node)
        else:
            priority_list.insert(index, root_node)

   #Create the Huffman node when there is a single element in the priority tree
    HT = HuffmanTree(root_node)
        
    encoded_dict = encode_huffman_tree(HT.root_node)
    encoded_string = ""
    for char in data:
            encoded_string += encoded_dict[char]
    return encoded_string, HT #return both the encoded string and the Huffman Tree 


def huffman_decoding(data,tree):
    decoded_string = ""
    index = 0
    while index < len(data): #decode by seraching through the tree
        node = tree.root_node
        while (node.left is not None and node.right is not None):
            decoded_char = data[index]
            if decoded_char == '0':
                node = node.left    
            elif decoded_char == '1':
                node = node.right
            index = index+1
        decoded_string += node.character
    return decoded_string

    
    pass


print("\n Test 1")
# Test 1
a_great_sentence = "The bird is the word"
print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}".format(a_great_sentence))
encoded_data, tree = huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}".format(decoded_data))
# output
#The size of the data is: 69
#The content of the data is: The bird is the word
#The size of the encoded data is: 36
#The content of the encoded data is: 1111101101010111100010001101100011110110111000110101011001110000001101
#The size of the decoded data is: 69
#The content of the encoded data is: The bird is the word


print("\n Test 2")
# Test 2 : Empty case
empty_sentence = ""
print ("The size of the data is: {}".format(sys.getsizeof(empty_sentence)))
print ("The content of the data is: {}".format(empty_sentence))
encoded_data, tree = huffman_encoding(empty_sentence)
print ("The content of the encoded data is: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print ("The content of the encoded data is: {}".format(decoded_data))
# output 
#The size of the data is: 49
#The content of the data is:
#Warning: The huffman coding does not work for sentences consistent of less than 2 characters!
#The size of the encoded data is: 49
#The content of the encoded data is:

print("\n Test 3")
# Test 3 : A sentence made of two character
a_sentence = "AAAAA"
print ("The size of the data is: {}".format(sys.getsizeof(a_sentence)))
print ("The content of the data is: {}".format(a_sentence))
encoded_data, tree = huffman_encoding(a_sentence)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}".format(decoded_data))

#The size of the data is: 54
#The content of the data is: AAAAA
#Warning: The huffman coding does not work for sentences consistent of less than 2 characters!
#The size of the encoded data is: 28
#The content of the encoded data is: 11111
#The size of the decoded data is: 54
#The content of the encoded data is: AAAAA