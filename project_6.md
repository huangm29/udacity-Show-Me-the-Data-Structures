## Union and Intersection of Two Linked Lists

Linked list has been used in this case. 

For the union of the two linked lists, the code goes through each list and append their elements in a set which avoids the redundant element

Time complexity: O(N + M), where N and M are the size of two lists.
Space complexity: O(N + M), where N and M are the size of two lists.

For the intersection of the two linked lists, the code needs to go through each list in a nested way to check if one element belongs to the other.

Time complexity: O(N * M), where N and M are the size of two lists.
Space complexity: O(max(N,M)), where N and M are the size of two lists.