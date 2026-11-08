from itertools import permutations,product
from math import factorial,comb
from fractions import Fraction

def falling(n,k):
 v=1
 for j in range(k):v*=n-j
 return v

def exact(n,r,k):
 def avoidance(j):
  s=sum(((-1)**h*comb(j,h)*Fraction(1,falling(n,h)) for h in range(min(j,k-1)+1)),Fraction(0))
  return s
 return Fraction(falling(n,k),k)*sum(((-1)**j*comb(k,j)*avoidance(j)**r for j in range(k+1)),Fraction(0))

def countcycles(succ,n,k):
 result=0
 for cyc in permutations(range(n),k):
  if cyc[0]!=min(cyc):continue
  if all(cyc[(j+1)%k] in succ[cyc[j]] for j in range(k)):result+=1
 return result

for n,r in [(2,1),(3,2),(4,2),(4,3)]:
 orders=list(permutations(range(n)))
 counts=[0]*(n+1); sz=len(orders)**r
 for ps in product(orders,repeat=r):
  succ=[set() for _ in range(n)]
  for p in ps:
   for a,b in zip(p,p[1:]):succ[a].add(b)
  for k in range(2,n+1):counts[k]+=countcycles(succ,n,k)
 for k in range(2,n+1):
  emp=Fraction(counts[k],sz); exp=exact(n,r,k)
  print('n,r,k',n,r,k,'bruteforce',emp,'exact',exp)
  assert emp==exp
print('ALL_EXACT_CYCLE_CHECKS_PASS')
