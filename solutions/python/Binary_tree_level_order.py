
class BTnode(object):
    def __init__(self, v, l, r):
	self.key = v
	self.left = l
	self.right = r

    def traverse(root):
	curl = [root] 
	while curl :
	    nextl = list()  
	    for node in curl:
		print node.key,
		if node.left: nextl.append(node.left)
		if node.right: nextl.append(node.right)
	    print 
	    curl = nextl
	print




#Test case 1

r1 = BTnode( 1, BTnode(2, None, None), BTnode(2, None,None) )
r1.traverse() 

r2 = BTnode( 1, BTnode(3, None, None), BTnode(2, r1,None) )
r2.traverse()

r3 = BTnode( 1, BTnode(3, r1, r1), BTnode(3, r1 , r1) )
r3.traverse()

r3 = BTnode( 1, BTnode(3, r3, r3), BTnode(3, r3 , r1) )

r3.traverse() 




