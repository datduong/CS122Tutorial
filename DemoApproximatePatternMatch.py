
import random
from itertools import product


def divide(dna, d):
  """ Divide a string into small pieces so that at least one fragment is free of errors. d is the number of errors"""
  length = len(dna)
  l = length // (d+1) 
  k = length % (d+1) ## higher d will split patterns into shorter length
  result = []
  i = 0
  while i < length: ## not very important just doing some splitting
    if k > 0:
      result.append((dna[i:i+l+1], i))
      k -= 1
      i += l+1
    else:
      result.append((dna[i:i+l], i))
      i += l
  return result


def HammingDistance(s1, s2):
  if len(s1) != len(s2): return float('inf')
  return sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1)))


def APM(pattern, d, Text, B):
  """ Approximate Pattern Matching """
  result = set()
  l = len(pattern)
  fragments = divide(pattern, d)
  for f in fragments: ## each fragment of each pattern
    s, i = f
    rest = pattern[:i] + pattern[i+len(s):] ## get the rest of pattern (note fragment came from pattern)... may be we can speed this up...
    for p in B.lookup(s): ##! use BWT to look where this small fragment of pattern match. note that B.lookup is just doing FM indexing, change it into your own function
      ##! note: @p should be an interger saying where the match is found, can match at many places
      target = Text[p-i:p] + Text[p+len(s):p-i+l] ## get the text that match.
      if HammingDistance(rest, target) <= d: ## keep results if we have only "a few" errors.
        result.add(p-i)
  return result


def solve(input): ##! assume some input: long-string, patterns-to-match, some-error-rate
  result = []
  dna, patterns, d = input.split('\n')
  d = int(d)
  patterns = patterns.split(' ')
  B = BWT(dna) ##! you need to implement the BWT or take it from https://nbviewer.jupyter.org/github/BenLangmead/comp-genomics-class/blob/master/notebooks/CG_FmIndex.ipynb
  for p in patterns:
    for i in APM(p, d, dna, B):
      result.append(i)
  return ' '.join(sorted(map(str, result)))

