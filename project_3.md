##Huffman Coding

As suggested, I used the priority queue combined with the binary tree to build the Huffman Tree. I did not sort the priority queue, therefore it is not necessary to use a min-heap.

Time complexity:  O(Nlog(N)), where N is number of character in the data. It takes logN to search the character with the minimum frequency
Space complexity: O(N), where N is number of character in the data.

