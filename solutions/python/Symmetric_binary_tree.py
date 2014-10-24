

class BTnode:
    def __init__(self,v, l, r):
	self.key = v 
	self.left = l 
	self.right = r  

    def is_mirror(self):
	return self._mirror_equals(self.left, self.right)

    def _mirror_equals( self, l, r):
	if l is None or r is None:
	    return l is None and r is None

	return ( l.key == r.key 
		and self._mirror_equals(l.left, r.right) 
		and self._mirror_equals(l.right, r.left)
		)


#Test case 1

r1 = BTnode( 1, BTnode(2, None, None), BTnode(2,None,None) )

print r1.is_mirror() 



#Test case 2

r2 = BTnode( 1, BTnode(3, None, None), BTnode(2,None,None) )

print r2.is_mirror() 



#Test case 3

r3 = BTnode( 1, BTnode(3, r1, r1), BTnode(3, r1 , r1) )

print r3.is_mirror() 

#Test case 4

r3 = BTnode( 1, BTnode(3, r3, r3), BTnode(3, r3 , r1) )

print r3.is_mirror() 









