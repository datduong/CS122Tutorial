
import collections
import itertools

_end = '$'

root = dict() ## empty dict 

words = [ 'ATAGA','ATC','GAT' ] 

for word in words:
		print ('\n\n'+word) ## one word in array 
		current_dict = root ## dict is pass by "reference"
		for letter in word:
				print (letter)
				print ('@current_dict before call setdefault')
				print (current_dict)
				current_dict = current_dict.setdefault(letter, {})
				print ('@current_dict after call setdefault')
				print ('current_dict = return item wrt. @letter or return {}')
				print (current_dict)
				print ('root')
				print ('add @current_dict to @root, notice @current_dict is not same as @root')
				print (root)
		##
		current_dict.setdefault(_end, _end)
		print ('end word')
		print (root)
		

## let's see root
root 


def print_trie(parent, node, result, _end = '$'):
    nodeid = parent
    for key in node:
        if node[key] == _end:
            continue
        nodeid += 1
        result.append(str(parent) + '->' + str(nodeid) + ':' + key)
        nodeid = print_trie(nodeid, node[key], result) ## recursive ... can probably make it easier to read. 
    return nodeid
	
	
result = []
print_trie(0, root, result) 
result




