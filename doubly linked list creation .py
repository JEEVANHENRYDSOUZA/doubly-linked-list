class Node:
	def __init__(self,value):
		self.value=value
		self.prev=None
		self.next=None
		
class DoublyLinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		
	def setHead(self,node):
		if self.head==None:
			self.head=node
			self.tail=node
			return
		self.insertBefore(self.head,node)
			
			
	def setTail(self,node):
		if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail,node)
			
	def insertBefore(self,node,nodeToInsert):
		if nodeToInsert==self.head and nodeToInsert==self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev=node.prev
		nodeToInsert.next=node
		if node.prev is None:
			self.head=nodeToInsert
		else:
			node.prev.next=nodeToInsert
		node.prev=nodeToInsert
			
			
			
	def insertAfter(self,node,nodeToInsert):
		if nodeToInsert==self.head and nodeToInsert==self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev=node
		nodeToInsert.next=node.next
		if node.next is None:
			self.tail=nodeToInsert
		else:
			node.next.prev=nodeToInsert
		node.next=nodeToInsert

	def insertAtPosition(self,position,nodeToInsert):
		if position ==1:
			self.setHead(nodeToInsert)
			return
		node=self.head
		currentPosition=1
		while node is not None and currentPosition !=position:
			node=node.next
			currentPosition+=1
		if node is not None:
			self.insertBefore(node,nodeToInsert)
		else:
			self.setTail(nodeToInsert)
			
		
		
		
		
		
		
		
		
		
		
	def removeNodesWithValue(self,value):
		current=self.head
		while current is not None:
			Temp=current
			current=current.next
			if Temp.value==value:
				self.remove(Temp)
		
		
		
		
		
	def remove(self,node):
		if(node==self.head):
			self.head=self.head.next
		if(node==self.tail):
			self.tail=self.tail.prev
		self.removeNodeBindings(node)#will work on the current instance of the node which is being used
		
	def containsNodeWithValue(self,value):
		current=self.head
		while current is not None and current.value!=value:
			current=current.next
				
		return current is not None
		
	def removeNodeBindings(self,node):
		if node.prev is not None:
			node.prev.next=node.next
		if node.next is not None:
			node.next.prev=node.prev
		node.prev=None
		node.next=None
