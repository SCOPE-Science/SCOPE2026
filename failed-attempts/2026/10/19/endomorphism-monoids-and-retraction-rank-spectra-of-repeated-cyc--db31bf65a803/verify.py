"""Exhaustive finite-field verification of evolution-cycle algebra homomorphism and retraction counts.
Representation: each generator basis element is one vertex of a directed disjoint union of cycles;
products of distinct generators are zero and each generator squares to its next vertex.
"""
from itertools import product
from math import comb, gcd

def add(a,b,q):return (a^b) if q==4 else (a+b)%q
def neg(a,q):return a if q==4 else (-a)%q
def mul(a,b,q):
 if q!=4:return a*b%q
 res=0
 for i in (0,1):
  if (b>>i)&1:res^=a<<i
 if res&8:res^=0b1100 # x^3=x^2+x (mod x^2+x+1)
 if res&4:res^=0b111  # x^2=x+1
 return res

def matrix_mult(A,B,q):
 n=len(A);R=[[0]*n for _ in range(n)]
 for i in range(n):
  for h in range(n):
   if A[i][h]:
    for j in range(n):R[i][j]=add(R[i][j],mul(A[i][h],B[h][j],q),q)
 return R

def inverse(x,q):
 for y in range(1,q):
  if mul(x,y,q)==1:return y
 raise AssertionError

def rank(A,q):
 C=[row[:] for row in A];n=len(C);r=0
 for j in range(n):
  piv=next((i for i in range(r,n) if C[i][j]),None)
  if piv is None:continue
  C[r],C[piv]=C[piv],C[r]; z=inverse(C[r][j],q)
  C[r]=[mul(z,x,q) for x in C[r]]
  for i in range(n):
   if i!=r and C[i][j]:
    z=C[i][j]
    C[i]=[add(x,neg(mul(z,y,q),q),q) for x,y in zip(C[i],C[r])]
  r+=1
 return r

def count(cycles,ell,q):
 n=cycles*ell
 nx=lambda j: (j//ell)*ell+(j+1)%ell
 hist=[0]*(cycles+1);hom=0
 # Independent search over all matrices with <=1 nonzero in each row.
 options=[(-1,0)]+[(j,t) for j in range(n) for t in range(1,q)]
 for rows in product(options,repeat=n):
  A=[[0]*n for _ in range(n)]
  for i,(j,t) in enumerate(rows):
   if j>=0:A[i][j]=t
  compatible=True
  for i in range(n):
   for t in range(n):
    if mul(A[t][i],A[t][i],q)!=A[nx(t)][nx(i)]:
     compatible=False;break
   if not compatible:break
  if not compatible:continue
  hom+=1
  if matrix_mult(A,A,q)==A:
   r=rank(A,q)
   assert r%ell==0
   hist[r//ell]+=1
 g=gcd(q-1,2**ell-1);h=ell*g
 expected_hom=(1+cycles*h)**cycles
 expected=[comb(cycles,k)*(1+k*h)**(cycles-k) for k in range(cycles+1)]
 assert (hom,hist)==(expected_hom,expected),(ell,cycles,q,hom,hist,expected_hom,expected)
 print(f'ell={ell} cycles={cycles} q={q} total_endomorphisms={hom}, idempotent_ranks={hist}, PASS')


def all_matrices_crosscheck(cycles,ell,q):
 n=cycles*ell
 nx=lambda j:(j//ell)*ell+(j+1)%ell
 hom=0;hist=[0]*(cycles+1)
 for flat in product(range(q),repeat=n*n):
  A=[list(flat[i*n:(i+1)*n]) for i in range(n)]
  if any(mul(A[t][i],A[t][j],q) for t in range(n) for i in range(n) for j in range(i+1,n)):
   continue
  if any(mul(A[t][i],A[t][i],q)!=A[nx(t)][nx(i)] for t in range(n) for i in range(n)):
   continue
  hom+=1
  if matrix_mult(A,A,q)==A:
   rk=rank(A,q)
   assert rk%ell==0
   hist[rk//ell]+=1
  # Full-matrix enumeration has no one-entry-per-row assumption.
 h=ell*gcd(q-1,2**ell-1)
 assert hom==(1+cycles*h)**cycles
 assert hist==[comb(cycles,k)*(1+k*h)**(cycles-k) for k in range(cycles+1)]
 print(f'FULL_MATRIX_EXHAUSTIVE ell={ell} cycles={cycles} q={q}, all={q**(n*n)}, hom={hom}, idempotent_ranks={hist}, PASS')

if __name__=='__main__':
 for r,l,q in [(1,1,2),(2,1,3),(2,2,2),(2,2,3),(2,2,4),(2,3,2),(3,2,2)]:count(r,l,q)
 all_matrices_crosscheck(2,2,2)
 print('ALL_EXACT_CHECKS_PASSED')
