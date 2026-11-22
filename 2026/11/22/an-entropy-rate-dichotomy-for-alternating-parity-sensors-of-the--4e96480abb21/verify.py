"""Finite GF(2) checks for the entropy classification of alternating parity sensors."""
from itertools import product

def mul(a,b):
    c=0
    while b:
        if b&1:c ^= a
        a <<= 1;b >>= 1
    return c

def gf_rank(vectors):
    basis={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i not in basis:
                basis[i]=v
                break
            v ^= basis[i]
    return len(basis)

def determinant(p,q):
    pe=sum(((p>>(2*k))&1)<<k for k in range((p.bit_length()+1)//2))
    po=sum(((p>>(2*k+1))&1)<<k for k in range(p.bit_length()//2))
    qe=sum(((q>>(2*k))&1)<<k for k in range((q.bit_length()+1)//2))
    qo=sum(((q>>(2*k+1))&1)<<k for k in range(q.bit_length()//2))
    return mul(pe,qe) ^ (mul(po,qo)<<1)

def method1(p,q,N):
    return [((p if n%2==0 else q)<<n) for n in range(2*N)]

def method2(p,q,N):
    return [((p if n%2==0 else q)<<(n//2)) for n in range(2*N)]

pairs=0; deficient=0; full=0
for p in range(1,32):
 for q in range(1,32):
    pairs+=1
    d=determinant(p,q)
    product=mul(p,q)
    assert (d==0)==all(not ((product>>k)&1) for k in range(0,product.bit_length(),2))
    for N in (3,6,12):
     r=gf_rank(method1(p,q,N))
     assert r==2*N if d else N<=r<=N+8,(p,q,N,r)
     m2=gf_rank(method2(p,q,N))
     assert N<=m2<=N+8,(p,q,N,m2)
    deficient+= (d==0)
    full+= (d!=0)
# Method 1: all two-point coordinates are independent but a three-bit XOR relation survives.
p=0b11;q=0b11110
assert determinant(p,q)==0
for N in range(2,20):
  rows=method1(p,q,N)
  assert gf_rank(rows)==N+2,(N,gf_rank(rows))
  assert all(rows[i]!=rows[j] for i in range(2*N) for j in range(i+1,2*N))
  assert (rows[1]^rows[2]^rows[4])==0 if N>=3 else True
# Method 2: p=1+s, q=1+s^2.
p=0b11;q=0b101
for N in range(1,20):
  rows=method2(p,q,N)
  assert gf_rank(rows)==N+1
  assert all(rows[i]!=rows[j] for i in range(2*N) for j in range(i+1,2*N))
  if N>=2:
   assert rows[1]^rows[0]^rows[2]==0
print('PASS:',pairs,'nonzero pairs checked at three block lengths; full=',full,'half=',deficient,
      '; exact example blocks N=1..19')
