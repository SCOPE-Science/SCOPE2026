from itertools import product
from collections import Counter

def matmul3(a,b,q):
 return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%q for i in range(3) for j in range(3))

def test(q):
 z=(0,)*9
 square_zero=[]
 for A in product(range(q),repeat=9):
  if matmul3(A,A,q)==z: square_zero.append(A)
 out=Counter()
 for A in square_zero:
  for B in square_zero:out[tuple((x+y)%q for x,y in zip(A,B))]+=1
 assert len(square_zero)==q**4+q**3-q
 assert sum(out.values())==len(square_zero)**2
 print('DIRECT',q,'SQUARE_ZERO',len(square_zero),'ORDERED_PAIR_SUMS',sum(out.values()),'NONZERO_FIBERS',len(out),'ZERO_TARGET_COUNT',out[z])
 for A in square_zero:
  if A!=z:assert out[A]==2*q*q-q
 print('DIRECT_CHECK_PASS',q)
for q in (2,3):test(q)
