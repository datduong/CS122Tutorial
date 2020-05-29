import itertools

MATCH = 1
MISMATCH = 0
GAP = 0


def solve(dataset):
  #
  def go():
    ## @k is going to be len of DNA... this function is not very well coded. whatever...
    ## notice below, we keep -1, so we can walk backward (backtracking)
    g = itertools.product([0, -1], repeat=k) ## all combinations of (0,-1) of the length k, suppose k=2 we will have 4 choices total.
    next(g) ## return all 0
    return g
  #
  dna = dataset.splitlines()
  k = len(dna) #! in the example, we have 3 sequences, so k=3
  score = {}
  dir = {}
  cells = itertools.product(*[range(len(d) + 1) for d in dna])
  # print (*[range(len(d) + 1) for d in dna]) #! special syntax here, it creates a tuple of "range(x,y)", we will look at the 3 input sequences, and then we create the x,y,z coordinates for the 3D walk
  start = next(cells)
  score[start] = 0
  dir[start] = None #! is used to backtrack
  for c in cells:
    # print (c) #! this is the 3D coordinate
    score[c] = -10 ** 6
    dir[c] = None
    for d in go(): #! at cell @c, we do we go next?
      prev = tuple(map(lambda x, y: x + y, c, d)) # where we were in previous step
      if any(x < 0 for x in prev): continue
      if d.count(0): # at least one '-'
        penalty = GAP
      elif any(dna[i][prev[i]] != dna[0][prev[0]] for i in range(k)): # unequal column
        penalty = MISMATCH
      else: # all are equal in column
        penalty = MATCH
      #
      ##! tracking "best" score.
      if score[c] < score[prev] + penalty:
        score[c] = score[prev] + penalty
        dir[c] = d #! tracking "best" score.
  #
  #
  c = tuple(len(d) for d in dna)
  final_score = score[c]
  alignment = ['' for _ in dna]
  d = dir[c]
  #### now we are finding final alignment, notice, we now use @dir to backtrack
  while d:
    c = tuple(map(lambda x, y: x + y, c, d))
    for i, g in enumerate(d):
      if not g:
        alignment[i] += '-'
      else:
        alignment[i] += dna[i][c[i]]
    d = dir[c]
  return '%d\n%s' % (final_score, '\n'.join(x[::-1] for x in alignment))



input_string = "ATATCCG\nTCCGA\nATGTACTG"
output = solve(input_string)
print (output)
