"""Exact, reproducible rank and spectral certificate for labelled STS(9) sampling."""
from itertools import combinations
from collections import Counter
from math import comb
from fractions import Fraction

N=9
triples=list(combinations(range(N),3))
triidx={v:i for i,v in enumerate(triples)}
pairs=list(combinations(range(N),2))
pari={v:i for i,v in enumerate(pairs)}
cover=[sum(1<<pari[p] for p in combinations(t,2)) for t in triples]
by_pair=[[j for j,c in enumerate(cover) if (c>>i)&1] for i in range(len(pairs))]
allmask=(1<<len(pairs))-1
systems=[]
def rec(done,blocks):
 if done==allmask:
  systems.append(sum(1<<i for i in blocks));return
 remaining=allmask^done
 choices=None
 while remaining:
  b=remaining&-remaining
  remaining-=b
  options=[j for j in by_pair[b.bit_length()-1] if not (cover[j]&done)]
  if not options:return
  if choices is None or len(options)<len(choices):choices=options
  if len(choices)==1:break
 for j in choices:
  rec(done|cover[j],blocks+[j])
rec(0,[])
assert len(systems)==len(set(systems))==840
systems.sort()
R=len(systems)
base=systems[0]
print('Independent exact-cover enumeration:',R,'systems')

# A feature column is the product of up to d distinct line-incidence bits.
# Pairwise Gram uses shared line count h; entries are sum C(h,j).
levels={
 0:([0,840],[839,1]),
 1:([0,180,2280],[791,48,1]),
 2:([0,60,102,120,570,3720],[371,216,120,84,48,1]),
 3:([63,120,128,168,275,422,440,1133,4920],[56,84,189,42,216,120,84,48,1]),
}

def gram(d):
 return [[sum(comb((a&b).bit_count(),k) for k in range(d+1)) for b in systems] for a in systems]

def multiply(M,v):
 return [sum(x*y for x,y in zip(row,v)) for row in M]

def check_spectrum(M,ev,mults):
 # Only the first column of P(M) must vanish: every column is a relabelled copy.
 v=[int(j==0) for j in range(R)]
 first=[v]
 for root in ev:
  v=[a-root*b for a,b in zip(multiply(M,v),v)]
 assert all(x==0 for x in v),('minimal polynomial failure',ev)
 # Exact power traces are recovered from one diagonal entry using transitivity.
 v=[int(j==0) for j in range(R)]
 measured=[]
 for k in range(len(ev)):
  measured.append(R*v[0])
  v=multiply(M,v)
 expected=[sum(m*e**k for m,e in zip(mults,ev)) for k in range(len(ev))]
 assert measured==expected, (measured,expected)
 assert sum(mults)==R
 assert all(m>0 for m in mults)
 print('all spectral levels:',list(zip(ev,mults)))
 print('rank:',sum(m for e,m in zip(ev,mults) if e),'trace=',measured[1])
 print('polynomial and trace certificate PASS')

for d,(ev,mults) in levels.items():
 print('d=',d)
 M=gram(d)
 assert all(M[i][j]==M[j][i] for i in range(R) for j in range(R))
 assert all(sum(row)==ev[-1] for row in M)
 check_spectrum(M,ev,mults)
 print('first row overlaps', Counter((base&x).bit_count() for x in systems) if d==0 else '')
print('ALL EXACT CHECKS PASSED')
