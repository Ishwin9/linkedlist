class Node:
     def __init__(self,value,next_node = None):
                self.value = value
                self.next_node = next_node

class LinkedList:
     def __init__(self,value,next_node=None):
              self.first_node = Node(value)
    
     def addnode(self,value):
              if self.first_node.next_node == None:
                       self.first_node.next_node = Node(value)
                       return
              temp = self.first_node.next_node
              while True:
                      if temp.next_node == None:
                            break
                      temp = temp.next_node
                      
              temp.next_node = Node(value)
           
      
     def __str__(self):
             if self.first_node.next_node == None:
                      return f"{self.first_node.value}"
             result = f"{self.first_node.value} "
             temp = self.first_node.next_node
             while True:
                      if temp.next_node == None:
                          result+= f" --> {temp.value}"
                          break
                      result+= f" --> {temp.value}"
                      temp = temp.next_node
             return result

ll = LinkedList(10)
ll.addnode(20)
ll.addnode(30)
ll.addnode(40)
ll.addnode(50)
ll.addnode(60)
ll.addnode(70)
print(ll)