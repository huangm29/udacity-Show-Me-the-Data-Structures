class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    node1 = llist_1.head
    node2 = llist_2.head
    union_set = set()
    while node1:
        union_set.add(node1.value)
        node1 = node1.next
    while node2:
        union_set.add(node2.value)
        node2 = node2.next
    unionLL = LinkedList()
    for i in union_set:
        unionLL.append(i)
    return unionLL

def intersection(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    intersection_set = set()
    while node1:
        if node1.value not in intersection_set:
            node2 = llist_2.head
            while node2:
                if node1.value == node2.value:
                    intersection_set.add (node1.value)
                    break
                node2 = node2.next
        node1 = node1.next
    intersectionLL = LinkedList()
    for i in intersection_set:
        intersectionLL.append(i)
    return intersectionLL


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))