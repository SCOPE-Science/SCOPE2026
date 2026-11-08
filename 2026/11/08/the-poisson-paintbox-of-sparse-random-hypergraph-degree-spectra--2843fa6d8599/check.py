#!/usr/bin/env python3
"""Finite independent checks for a hypergraph degree-spectrum limit.
Standard-library only. These are checks, not an infinite proof.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, log
from itertools import combinations

checks=0

def eq(a,b,msg):
    global checks
    assert a==b, (msg,a,b)
    checks+=1

def falling(n,k):
    z=1
    for j in range(k): z*=n-j
    return z

# Exact finite hyperedge incidence partition identities.
for n in range(4,18):
 for m in range(1,min(n,6)+1):
  for r in range(2,n+1):
   for s in range(1,min(m,r)+1):
    lhs=Q(comb(n-m,r-s) if 0 <= r-s <= n-m else 0,comb(n-1,r-1))
    rhs=Q(falling(r-1,s-1)*falling(n-r,m-s),falling(n-1,m-1)) if n-r>=m-s else Q(0)
    eq(lhs,rhs,'incidence ratio')

# Joint subset-pattern means sum exactly to m times single-vertex mean.
for n in range(4,15):
 for m in range(1,min(n,5)+1):
  for r in range(2,n+1):
   value=sum(s*comb(m,s)*comb(n-m,r-s) for s in range(1,m+1) if 0<=r-s<=n-m)
   eq(value,m*comb(n-1,r-1),'sum over nonempty tagged patterns')

# Finite Bernoulli hypergraph n=4, ranks 2 and 3: complete 1024-outcome enumeration.
n=4
edges=list(combinations(range(n),2))+list(combinations(range(n),3))
p=[Q(1,5) if len(e)==2 else Q(1,11) for e in edges]
target_iso_mean=Q(1)
target_pair_iso=Q(1)
for e,prob in zip(edges,p):
 if 0 in e: target_iso_mean*=1-prob
 if 0 in e or 1 in e: target_pair_iso*=1-prob
iso_mean=Q(0); pair_iso=Q(0); means=[Q(0) for _ in range(n)]
for mask in range(1<<len(edges)):
 prob=Q(1); degrees=[0]*n
 for j,e in enumerate(edges):
  included=(mask>>j)&1
  prob*=p[j] if included else (1-p[j])
  if included:
   for v in e: degrees[v]+=1
 iso_mean+=prob*(degrees[0]==0)
 pair_iso+=prob*(degrees[0]==0 and degrees[1]==0)
 for v in range(n):means[v]+=prob*degrees[v]
eq(iso_mean,target_iso_mean,'exact isolated mean')
eq(pair_iso,target_pair_iso,'exact pair isolated mean')
for v in range(n):eq(means[v],sum(comb(n-1,r-1)*Q(1,5 if r==2 else 11) for r in (2,3)),'exact degree means')

# Algebraic Poisson shock check: sums of all cell means incident to a tag equal lambda.
# For atom with mass lambda at alpha, intensity = lambda/alpha. With alpha=0 use only singleton shocks.
for den in range(2,12):
 for numerator in range(1,den):
  alpha=Q(numerator,den); lam=Q(5,3)
  for m in range(1,8):
   # mean of all nonempty patterns containing vertex 0
   total=sum(comb(m-1,s-1)*lam*alpha**(s-1)*(1-alpha)**(m-s) for s in range(1,m+1))
   eq(total,lam,'Poisson shadow vertex mean')
   # shared between vertices 0 and 1
   if m>=2:
    shared=sum(comb(m-2,s-2)*lam*alpha**(s-1)*(1-alpha)**(m-s) for s in range(2,m+1))
    eq(shared,lam*alpha,'Poisson shadow pair shared mean')

# Invert isolation-moment identities: log E(P_0^k)= sum_j (-1)^j C(k,j) M_{j-1}.
# Here arithmetic is exact for rational moment coefficients.
nu_atoms=[(Q(0),Q(1,4)),(Q(1,3),Q(7,8)),(Q(3,4),Q(2,5)),(Q(1),Q(1,9))]
M=[sum(weight*x**j for x,weight in nu_atoms) for j in range(9)]
L=[]
for k in range(1,10):
 value=sum((-1)**j*comb(k,j)*M[j-1] for j in range(1,k+1))
 L.append(value)
M_recovered=[]
for k in range(1,10):
 previous=sum((-1)**j*comb(k,j)*M_recovered[j-1] for j in range(1,k))
 new=(-1)**k*(L[k-1]-previous)
 M_recovered.append(new)
 eq(new,M[k-1],'isolates identify moment')

# Exact second-moment formula Var(P0)=exp(-2lambda)*(exp(M1)-1) is nonnegative;
# strict if and only if there is positive mass away from zero.
for atoms in [[(Q(0),Q(2))],[(Q(1,2),Q(2))],[(Q(0),Q(1)),(Q(3,4),Q(1))]]:
 mass=sum(w for x,w in atoms); m1=sum(x*w for x,w in atoms)
 lhs=exp(-2*float(mass))*(exp(float(m1))-1)
 eq(lhs>1e-14,m1>0,'isolate variance positivity')

print('PASS', checks, 'exact combinatorial/algebraic and distributional checks')
