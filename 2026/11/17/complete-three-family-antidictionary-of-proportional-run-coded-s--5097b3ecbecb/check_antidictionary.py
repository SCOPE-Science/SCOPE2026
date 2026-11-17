"""Finite exact language/antidictionary comparisons for the block-coded binary family.
All values and languages are computed from the generator definitions; no third-party dependencies.
Finite comparisons corroborate but do not prove the arbitrary-length theorem.
"""
from functools import lru_cache
@lru_cache(None)
def tails(k,n):
 if n==0:return {''}
 s=set()
 for m in range(1,n+1):
  g='0'*m+'1'*(k*m)
  if len(g)>=n:s.add(g[:n])
  else:
   for t in tails(k,n-len(g)):s.add(g+t)
 return s
@lru_cache(None)
def lang(k,n):
 s=set()
 for m in range(1,n+1):
  g='0'*m+'1'*(k*m)
  for i in range(len(g)):
   t=g[i:]
   if len(t)>=n:s.add(t[:n])
   else:
    for u in tails(k,n-len(t)):s.add(t+u)
 return s
for k in range(1,6):
 for n in range(3,17):
  L=lang(k,n); P=lang(k,n-1)
  bad={f'{i:0{n}b}' for i in range(2**n) if f'{i:0{n}b}' not in L and f'{i:0{n}b}'[:-1] in P and f'{i:0{n}b}'[1:] in P}
  expected=set()
  for r in range(1,n):
   w='0'+'1'*r+'0'
   if len(w)==n and r%k:expected.add(w)
  for m in range(1,n):
   for w in ('0'*(m+1)+'1'*(k*m)+'0','1'+'0'*m+'1'*(k*m+1)):
    if len(w)==n:expected.add(w)
  if bad!=expected:
   print('MISMATCH',k,n,'bad',bad,'expected',expected)
   raise SystemExit(1)
 print('passed k=',k,'lastn=16','L=',len(lang(k,16)))
print('VERIFY_OK block_coded_parameters=5 word_lengths=3..16 exact_comparisons=70')
