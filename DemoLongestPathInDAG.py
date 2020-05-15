import random


def parse_data(dataset): ##! read in the graph into some python object
  nodes = set()
  adj_list = {}
  rev_adj_list = {}
  for line in dataset: ##! just some data preprocesing
    line = line.strip().split("->")
    node1 = int(line[0])
    node2, weight = map(int, line[1].split(":"))
    nodes.add(node1)
    nodes.add(node2)
    adj_list.setdefault(node1, []).append((node2, weight))
    # store reverse edges to easily find previous nodes
    rev_adj_list.setdefault(node2, []).append((node1, weight))
  return sorted(nodes), adj_list, rev_adj_list


def solve(dataset):
  dataset = dataset.splitlines()
  start, end = map(int, dataset[:2])
  dataset = dataset[2:]
  ##! just read in graph. build nodes, and edges
  nodes, adj_list, _ = parse_data(dataset) 
  print('nodes')
  print (nodes)
  print('adj_list')
  print(adj_list)
  #
  dp = {n:-float("inf") for n in nodes}
  dp[start] = 0 ##! set 0 at the start
  prev = {}
  #
  ##! looks like greedy algorithm
  for node in nodes:
    for neigh, weight in adj_list.get(node, []): ##! go over each neighbor
      if dp[neigh] < dp[node] + weight: ##! if we gain "weight" then we keep the node
        dp[neigh] = dp[node] + weight
        prev[neigh] = node
  #
  prev_node = end
  path = []
  while prev_node is not None:
    path.append(prev_node)
    prev_node = prev.get(prev_node)
  #
  solution = "{}\n{}".format(dp[end], "->".join(map(str, path[::-1])))
  return solution


#### run testing

testcase = "0\n4\n0->1:7\n0->2:4\n2->3:2\n1->4:1\n3->4:3"

solve(testcase)

