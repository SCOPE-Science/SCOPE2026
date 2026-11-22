"""Independent finite rational checks of a minorized Markov adjugate inequality.

Run: python3 check_markov_adjugate.py
All arithmetic is exact using fractions.Fraction, not floating-point.
This finite check supplements, but cannot replace, the proof for all orders.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial
from random import Random

def determinant(A):
    n = len(A)
    out = F(0)
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        z = F(-1 if inv%2 else 1)
        for i,j in enumerate(perm): z *= A[i][j]
        out += z
    return out

def adjugate(A):
    n = len(A)
    return [[(-1 if (i+j)%2 else 1)*determinant(
        [[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j]
    ) for j in range(n)] for i in range(n)]

def norm_one(A):
    return max(sum(abs(A[i][j]) for i in range(len(A))) for j in range(len(A)))

def matrix_from_mapping(n,alpha,mapping):
    s=sum(alpha); t=1-s
    return [[alpha[i]+(t if mapping[j]==i else 0) for j in range(n)] for i in range(n)]

def bound(n,alpha):
    s=sum(alpha)
    return 2*(1-min(alpha))*(1-s)**(n-2)

def permute_matrix(n,alpha,rr):
    # make a deterministic map with exactly n-1 different images, omitting rr
    used=[i for i in range(n) if i!=rr]
    mapping=used+[used[0]]
    return matrix_from_mapping(n,alpha,mapping)

checks=0
profiles = {
  2: [[F(0),F(0)],[F(2,9),F(1,3)],[F(3,4),F(1,8)]],
  3: [[F(0)]*3,[F(1,20),F(1,5),F(3,10)],[F(1,4)]*3],
  4: [[F(0)]*4,[F(1,20),F(1,10),F(1,7),F(1,6)]],
}
for n, ps in profiles.items():
  for a in ps:
    b=bound(n,a)
    mx=F(0)
    for indices in product(range(n),repeat=n):
      P=matrix_from_mapping(n,a,indices)
      k=norm_one(adjugate(P)); checks+=1
      assert k<=b,(n,a,indices,k,b)
      mx=max(mx,k)
    assert mx==b,(n,a,mx,b)
    P=permute_matrix(n,a,a.index(min(a)))
    assert norm_one(adjugate(P))==b; checks+=1

rng=Random(20261117)
for n in [2,3,4,5]:
 for it in range(80):
  raw=[rng.randrange(1,20) for _ in range(n)]
  s=F(rng.randrange(0,9),10)
  a=[s*F(k,sum(raw)) for k in raw]
  # rational stochastic residual with columns in (n-1)-simplex
  Q=[[F(0) for _ in range(n)] for _ in range(n)]
  for j in range(n):
   w=[rng.randrange(0,10) for _ in range(n)]
   if sum(w)==0:w[0]=1
   for i in range(n): Q[i][j]=F(w[i],sum(w))
  t=1-s
  P=[[a[i]+t*Q[i][j] for j in range(n)] for i in range(n)]
  val=norm_one(adjugate(P)); b=bound(n,a)
  assert val<=b,(n,a,val,b)
  checks+=1
  Pstar=permute_matrix(n,a,a.index(min(a)))
  assert norm_one(adjugate(Pstar))==b; checks+=1

print('MINORIZED_MARKOV_ADJUGATE_EXACT_CHECK_OK',checks)
