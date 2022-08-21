#Creating a Node with a value and a pointer
class Node:
  def __init__(self,val = None):
    self.val = val
    self.next = None

class sLL:
  def __init__(self):
    self.headVal = None #header pointer initialized to none

#traversing the node
  def travNode(self, headVal):
    trav = headVal
    while trav is not None:
      print(trav.val)
      trav = trav.next
    print("###################")

#insert at beginning
  def insBegin(self,newVal):
    begNode = Node(newVal)
    begNode.next = a.headVal
    a.headVal = begNode

#insert at end
  def insEnd(self,lstVal):
    lstNode = Node(lstVal)
    tmp = a.headVal
    while tmp.next is not None:
      tmp = tmp.next
      #print("end trav ",tmp.val)
    else:
      tmp.next = lstNode

#count no of nodes
  def cntNode(self, headVal):
    trav = headVal
    cnt = 0
    while trav is not None:
      cnt+=1
      trav = trav.next
    print("the number of nodes is ",cnt)
     

#creating object
a = sLL()
a.headVal = Node("abc")
e1 = Node("def")
a.headVal.next = e1
e2 = Node("ghi")
e1.next = e2

a.travNode(a.headVal)
a.insBegin("ABC")
a.travNode(a.headVal)
a.insEnd("XYZ")
a.travNode(a.headVal)
a.cntNode(a.headVal)