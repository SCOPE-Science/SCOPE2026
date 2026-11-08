#!/usr/bin/env python3
"""Exact finite extremal census for two binary scattered-subsequence patterns."""
from itertools import combinations, product
from math import comb

patterns = ('00101','01101')
expected = {
 '00101': [(1,1),(3,1),(6,5),(15,1)],
 '01101': [(1,1),(3,1),(6,4),(12,7)],
}
wins7={
 '00101': {'0000101','0001001','0001011','0001101','0010101'},
 '01101': {'0011101','0111001','0111011','0111101'},
}
wins8={
 '00101': {'00010101'},
 '01101': {'00111001','00111011','00111101','01110011','01110101','01111001','01111011'},
}
def embedding_dp(word,pattern):
 d=[1]+[0]*len(pattern)
 for c in word:
  for j in range(len(pattern)-1,-1,-1):
   if c==pattern[j]: d[j+1]+=d[j]
 return d[-1]
def embedding_choose(word,pattern):
 return sum(''.join(word[j] for j in idx)==pattern
            for idx in combinations(range(len(word)),len(pattern)))
def runs(word):
 return (len(word)>0)+sum(word[i]!=word[i-1] for i in range(1,len(word)))
def orbit(word):
 comp=lambda s: ''.join('0' if c=='1' else '1' for c in s)
 return {word,word[::-1],comp(word),comp(word)[::-1]}
allpatterns={''.join(x) for x in product('01',repeat=5) if runs(''.join(x))==4}
assert len(allpatterns)==8
assert orbit('00101').isdisjoint(orbit('01101'))
assert orbit('00101') | orbit('01101')==allpatterns
seen=0
for p in patterns:
 for n in range(5,9):
  best=-1;opt=set()
  for x in product('01',repeat=n):
   w=''.join(x)
   got=embedding_dp(w,p)
   assert got==embedding_choose(w,p), (p,w,got)
   if got>best:
    best=got; opt={w}
   elif got==best: opt.add(w)
   seen+=1
  assert (best,len(opt))==expected[p][n-5],(p,n,best,len(opt))
  if n==7: assert opt==wins7[p],(p,n,opt)
  if n==8: assert opt==wins8[p],(p,n,opt)
# Four-run host upper bound follows independently from a run-composition census.
values=[(comb(a,2)*b*c*d,(a,b,c,d)) for a in range(2,9)
 for b in range(1,9) for c in range(1,9)
 for d in range(1,9) if a+b+c+d==8]
assert max(z[0] for z in values)==12
assert embedding_dp('00010101','00101')==15
assert runs('00010101')==6
assert embedding_dp('00111001','01101')==12
assert runs('00111001')==4
assert 6*6<3*15
print('VERIFY_OK; inspected',seen,'binary words, two patterns; independent combinations matched')
