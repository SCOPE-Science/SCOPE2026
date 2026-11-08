#!/usr/bin/env python3
from itertools import product

def rank(M,q):
 M=[list(map(lambda x:x%q,row)) for row in M]
 h=len(M); w=len(M[0]) if h else 0; k=0
 for j in range(w):
  l=next((i for i in range(k,h) if M[i][j]),None)
  if l is None:continue
  M[k],M[l]=M[l],M[k]
  a=pow(M[k][j],-1,q);M[k]=[a*x%q for x in M[k]]
  for i in range(h):
   if i!=k and M[i][j]:
    a=M[i][j];M[i]=[(b-a*c)%q for b,c in zip(M[i],M[k])]
  k+=1
  if k==h:break
 return k

def omega(u,v,q,n):
 return (sum(u[i]*v[i+n] - u[i+n]*v[i] for i in range(n)))%q

def mult(A,B,q):
 m=len(A);return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(m))%q for j in range(m)) for i in range(m))

def commuting(A,B,q):
 return mult(A,B,q)==mult(B,A,q)

def operators(q,n):
 out=[(tuple(tuple(0 for _ in range(2*n)) for _ in range(2*n)),None)]
 for v in product(range(q),repeat=2*n):
  if not any(v):continue
  i=next(i for i,x in enumerate(v) if x)
  if v[i]!=1:continue
  w=tuple([-v[j+n]%q if j<n else v[j-n] for j in range(2*n)])
  # w_j = -Jv_j so X_{ij}=v_i w_j ; scalar as all nonzero coefficient
  for a in range(1,q):
   X=tuple(tuple(a*v[i]*w[j]%q for j in range(2*n)) for i in range(2*n))
   out.append((X,v))
 assert len(out)==q**(2*n),(q,n,len(out))
 return out

def isotropic_subspaces(q,n,s):
 # direct enumeration via canonical row spaces of tuples, only small test cases
 from itertools import combinations
 if s==0:return 1
 seen=set()
 for rows in product(list(product(range(q),repeat=2*n)),repeat=s):
  if rank(rows,q)!=s:continue
  if any(omega(rows[i],rows[j],q,n) for i in range(s) for j in range(i+1,s)):continue
  M=[list(x) for x in rows]
  piv=0
  for col in range(2*n):
   ri=next((i for i in range(piv,s) if M[i][col]%q),None)
   if ri is None:continue
   M[piv],M[ri]=M[ri],M[piv]
   h=pow(M[piv][col],-1,q);M[piv]=[h*x%q for x in M[piv]]
   for i in range(s):
    if i!=piv and M[i][col]:
     h=M[i][col];M[i]=[(x-h*y)%q for x,y in zip(M[i],M[piv])]
   piv+=1
   if piv==s:break
  seen.add(tuple(map(tuple,M)))
 return len(seen)

def I(q,n,s):
 from fractions import Fraction
 x=Fraction(1,1)
 for j in range(s):x*=Fraction(q**(2*(n-j))-1,q**(s-j)-1)
 assert x.denominator==1
 return int(x)

def C(q,n,r):
 return sum(I(q,n,s)*__import__('math').prod(q**r-q**i for i in range(s)) for s in range(min(n,r)+1))

def run(q,n,r):
 ops=operators(q,n);M=len(ops)
 assert len({A for A,v in ops})==M
 for A,v in ops:
  if v is None:continue
  assert mult(A,A,q)==ops[0][0]
 # actual commutator check against symplectic orthogonality
 good=[[commuting(ops[i][0],ops[j][0],q) for j in range(M)] for i in range(M)]
 for i in range(M):
  for j in range(M):
   va,vb=ops[i][1],ops[j][1]
   assert good[i][j]==(va is None or vb is None or omega(va,vb,q,n)==0)
 hist=[0]*(min(n,r)+1);active=0
 if r==2:
  for i in range(M):
   for j in range(M):
    if good[i][j]:
     rows=[v for v in [ops[i][1],ops[j][1]] if v is not None]
     hist[rank(rows,q)]+=1
 else:
  assert r==3
  for i in range(M):
   for j in range(M):
    if not good[i][j]:continue
    for k in range(M):
     if good[i][k] and good[j][k]:
      rows=[v for v in (ops[i][1],ops[j][1],ops[k][1]) if v is not None]
      hist[rank(rows,q)]+=1
 expected=[I(q,n,s)*__import__('math').prod(q**r-q**i for i in range(s)) for s in range(min(n,r)+1)]
 assert hist==expected,(hist,expected)
 print('PASS',f'q={q}, n={n}, r={r}, total={sum(hist)}, by_support_rank={hist}, expected={expected}, all_actual_matrix_commutators_tested')

if __name__=='__main__':
 for p,n,r in [(3,1,2),(3,1,3),(5,1,3),(3,2,2),(3,2,3),(5,2,2)]:
  run(p,n,r)
 print('ALL_SP_RANK_ONE_COUNTS_PASS')
