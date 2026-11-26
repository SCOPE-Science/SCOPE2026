#!/usr/bin/env python3
"""Direct square-zero and centralizer enumeration for 4 by 4 matrices over prime fields."""
from itertools import product

def mul(a,b,p,n=4):
 return tuple(sum(a[n*i+k]*b[n*k+j] for k in range(n))%p for i in range(n) for j in range(n))

def rank(a,p,n=4):
 b=[list(a[n*i:n*i+n]) for i in range(n)]; h=0
 for j in range(n):
  t=next((i for i in range(h,n) if b[i][j]),None)
  if t is None:continue
  b[t],b[h]=b[h],b[t]; inv=pow(b[h][j],-1,p); b[h]=[(z*inv)%p for z in b[h]]
  for i in range(n):
   if i!=h and b[i][j]:
    c=b[i][j];b[i]=[(v-c*w)%p for v,w in zip(b[i],b[h])]
  h+=1
  if h==n:break
 return h

def fixed_rank1_b(p):
 # A=E01.  B=[[a,b,u0,u1],[0,a,0,0],[0,v0,C00,C01],[0,v1,C10,C11]].
 A=(0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
 zero=(0,)*16; cnt=0; prod_nonzero=0
 for a,b,u0,u1,v0,v1,c00,c01,c10,c11 in product(range(p),repeat=10):
  B=(a,b,u0,u1,0,a,0,0,0,v0,c00,c01,0,v1,c10,c11)
  if mul(B,B,p)!=zero:continue
  assert mul(A,B,p)==mul(B,A,p)
  cnt+=1
  if mul(A,B,p)!=zero:prod_nonzero+=1
 assert cnt==p**5+p**4-p**2,(p,cnt)
 assert prod_nonzero==0
 return cnt

def fixed_rank2_b(p):
 # A maps e2 to e0 and e3 to e1.  B=[[P,Q],[0,P]] with 2x2 blocks.
 A=(0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0)
 zero=(0,)*16;cnt=0;nonzero=0
 for vals in product(range(p),repeat=8):
  a,b,c,d,e,f,g,h=vals
  B=(a,b,e,f,c,d,g,h,0,0,a,b,0,0,c,d)
  if mul(B,B,p)!=zero:continue
  assert mul(A,B,p)==mul(B,A,p)
  cnt+=1
  if mul(A,B,p)!=zero:nonzero+=1
 assert cnt==2*p**4-p**2,(p,cnt)
 assert nonzero==p**4-p**2,(p,nonzero)
 return cnt,nonzero

def formula(p):
 n1=(p**4-1)*(p**3-1)//(p-1)
 n2=(p*p+1)*(p*p+p+1)*((p*p-1)*(p*p-p))
 c=1+n1+n2+n1*(p**5+p**4-p*p)+n2*(2*p**4-p*p)
 nz=n2*(p**4-p*p)
 fiber=p**3*(p-1)*(p*p-1)
 assert nz==n1*fiber
 return n1,n2,c,nz,fiber

def run(p):
 a=fixed_rank1_b(p); b=fixed_rank2_b(p)
 n1,n2,total,nz,fiber=formula(p)
 print(f'q={p}: ranks 0/1/2: 1/{n1}/{n2}; B centralizers {a}/{b[0]}; total pairs {total}, nonzero products {nz}, each nonzero rank-one fiber {fiber}')
 if p==2:
  zero=(0,)*16
  mats=[a for a in product(range(p),repeat=16) if mul(a,a,p)==zero]
  assert len(mats)==1+n1+n2
  counts={};total2=0
  for A in mats:
   for B in mats:
    AB=mul(A,B,p)
    if AB==mul(B,A,p):
     total2+=1; counts[AB]=counts.get(AB,0)+1
  assert total2==total
  assert len(counts)==1+n1
  assert counts[zero]==total-nz
  assert all(v==fiber for k,v in counts.items() if k!=zero)
  assert all(rank(k,p)==1 for k in counts if k!=zero)
  print(f'q=2 full 4x4 independent multiplication fibers: {len(counts)} targets, zero={counts[zero]}, each nonzero={fiber}')

if __name__=='__main__':
 for p in (2,3):run(p)
 print('COMMUTING_SQUAREZERO4_MULTIPLICATION_FIBERS_OK')
