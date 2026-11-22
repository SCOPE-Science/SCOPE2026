#!/usr/bin/env python3
"""Independent incidence-only census, constructing all lines from pairs of points.

Field multiplication uses polynomial reduction rather than an explicit multiplication table.
Distinct union concepts are classified by whether constituent lines intersect.
"""
from itertools import combinations
from math import comb

def mult(a,b):
 p=0
 for i in range(2):
  for j in range(2):
   if (a>>i&1) and (b>>j&1):p^=1<<(i+j)
 if p&4:p^=7  # t^2=t+1 in GF(4)
 return p

def inv(a):
 assert a
 return next(b for b in range(1,4) if mult(a,b)==1)

points=[(x,y) for x in range(4) for y in range(4)]
line_set=set()
for i,j in combinations(range(16),2):
 x,y=points[i]; u,v=points[j]
 dx=x^u;dy=y^v
 # Zero determinant (x-a, y-b) with the joining direction (dx,dy).
 L=sum(1<<z for z,(a,b) in enumerate(points) if mult(a^x,dy)==mult(b^y,dx))
 assert L.bit_count()==4
 line_set.add(L)
assert len(line_set)==20
lines=sorted(line_set)
parallel=[]; nonparallel=[]
for A,B in combinations(lines,2):
    (parallel if A&B==0 else nonparallel).append(A|B)
assert len(parallel)==30 and len(nonparallel)==160
concepts={'parallel':sorted(set(parallel)),'nonparallel':sorted(set(nonparallel)),
          'all':sorted(set(parallel+nonparallel))}
expected={'parallel':[1,16,120,560,1680,0],
          'nonparallel':[1,16,120,560,1680,2400],
          'all':[1,16,120,560,1800,3840]}
assert {k:len(v) for k,v in concepts.items()}=={'parallel':30,'nonparallel':160,'all':190}

for k in range(6):
 count=dict.fromkeys(concepts,0)
 for subset in combinations(range(16),k):
  for name,cs in concepts.items():
   traces=set()
   for C in cs:
    t=0
    for j,i in enumerate(subset):
     if C & (1<<i): t|=1<<j
    traces.add(t)
    if len(traces)==2**k:break
   if len(traces)==2**k:count[name]+=1
 for name,v in count.items(): assert v==expected[name][k],(k,name,v)
# Six-supports cannot be shattered by any two-line union: a shattered support
# may not have four collinear points, and a six-set covered by two lines would
# require two triples; deleting one point from a triple then becomes impossible.
# Independently check the combinatorial obstruction for all 6-subsets.
for subset in combinations(range(16),6):
 S=sum(1<<x for x in subset)
 if any((S&L).bit_count()>=4 for L in lines):continue
 covers=[(A,B) for A,B in combinations(lines,2) if (A|B)&S==S]
 for A,B in covers:
  # If both lines meet S in three points, remove an A-only point,
  # retaining two other A points and all three B points.
  assert (A&S).bit_count()==3 and (B&S).bit_count()==3
  i=next(i for i in subset if (A>>i&1) and not(B>>i&1))
  wanted=S & ~(1<<i)
  assert all(not(((C|D)&S)==wanted) for C,D in combinations(lines,2))
print('AFFINE_INCIDENCE_INDEPENDENT_PASS')
print('verified coefficient vectors:',expected)
