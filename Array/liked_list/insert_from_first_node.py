class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(5)
node2=Node(15)
node3=Node(25)

node1.next=node2
node2.next=node3

head=node1
current=head

new_node=Node(35)
new_node.next=head
head=new_node
current=head

while current:
    print(current.data)
    current=current.next