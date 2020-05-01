import random
import collections

def inDegree(adj, v):
	return sum(1 if v == u else 0 for value in list(adj.values()) for u in value)
	
def outDegree(adj, v):
	return len(adj[v])

def nonBranchNode(adj, v):
	return (inDegree(adj, v) == 1) and (outDegree(adj, v) == 1)

# input 
input = 'ATG\nATG\nTGT\nTGG\nCAT\nGGA\nGAT\nAGA'

# construct graph
kmers = input.splitlines()
adj = collections.defaultdict(list) ## construct this data structure @https://docs.python.org/2/library/collections.html
for kmer in kmers:
	adj[kmer[:-1]].append(kmer[1:])

# what is @adj
adj

# now... we assemble kmers into contigs
result = []

# find starts of contigs
# start at a place that is "branch-able" 
starts = [v for v in adj if not nonBranchNode(adj, v)]

for start in starts:
	print ('-'*50)
	print ('\n\nstart a "head" node {}'.format(start))
	for v in adj[start]:
		nextV = v
		path = [start, nextV] ## take any path 
		print ('\npath to take {}'.format(path))
		print ('is this non-branching path {}'.format(nonBranchNode(adj, nextV)))
		while nonBranchNode(adj, nextV):
			# continue to go onto the next node (node that connects to @nextV) 
			# until you see a banch-path, then you exit. 
			print ('path is direct, so we continue to walk until we are able to branch')
			nextV = adj[nextV][0]
			path.append(nextV)
			print (path)
		## 
		print ('what is path after "while" {}'.format(path)) 
		r = path[0]
		r += ''.join(p[-1] for p in path[1:]) ## add string together.
		result.append(r)
	
#
' '.join(sorted(result)) ## final output

