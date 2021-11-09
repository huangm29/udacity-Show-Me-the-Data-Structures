import sys
from collections import Counter


class Node:
    def __init__(self, character, frequency):
        self.character = character;
        self.frequency = frequency;
        self.left = None;
        self.right = None;

class HuffmanTree:
    def __init__(self, root_node):
        self.root_node = root_node

def encode_huffman_tree(node):
    encode_dict = {}
    if (node.left is None and node.right is None):
        encode_dict[node.character] = ""
    else:
        if node.left is not None:
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
    freq_map = Counter(data).most_common()
    for item in freq_map:
        priority_list.append(Node(item[0],item[1])) 

    while(len(priority_list)>1):
        first_node = priority_list.pop()
        second_node = priority_list.pop()
        sum_freq = first_node.frequency + second_node.frequency
        sum_string = first_node.character + second_node.character # This is not necessary
        root_node = Node(sum_string , sum_freq)
        root_node.left = first_node
        root_node.right = second_node

        for index in range(len(priority_list)):
            if priority_list[index].frequency < sum_freq:
                break
        if index+1 == len(priority_list) and priority_list[index].frequency > sum_freq:
            priority_list.append(root_node)
        else:
            priority_list.insert(index, root_node)

        if (len(priority_list) == 1):
            HT = HuffmanTree(root_node)
        
    encoded_dict = encode_huffman_tree(HT.root_node)
    encoded_string = ""
    for char in data:
        encoded_string += encoded_dict[char]
    return encoded_string, HT


def huffman_decoding(data,tree):
    decoded_string = ""
    index = 0
    while index < len(data):
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

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))