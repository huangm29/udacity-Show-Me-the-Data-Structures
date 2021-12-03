## Union and Intersection of Two Linked Lists

Linked list has been used in this case. I only implemented a sorting 

For the union of the two linked lists, the code goes through each list and append their elements in a set which avoids any redundant element.

Time complexity: O(N + M), where N and M are the size of two lists.
Space complexity: O(N + M), where N and M are the size of two lists.

For the intersection of the two linked lists, the code needs to go through each list in a nested way to check if one element belongs to the other. Again, a python set is used to avoid any redundant element.

Time complexity: O(N * M), where N and M are the size of two lists.
Space complexity: O(max(N,M)), where N and M are the size of two lists.
