#!/usr/bin/env python3
"""Exact Cartier computation over GF(2), using only the standard library."""
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  a<<=1;b>>=1
 return r
def power(a,n):
 r=1
 for _ in range(n):r=mul(r,a)
 return r
def der(a):
 return sum(1<<(j-1) for j in range(1,a.bit_length(),2) if (a>>j)&1)
def root_square(a):
 assert all(not ((a>>j)&1) for j in range(1,a.bit_length(),2))
 return sum(1<<(j//2) for j in range(0,a.bit_length(),2) if (a>>j)&1)
H=0b111;F=mul(0b11, mul(0b10,power(H,3)))
assert F==mul(0b110,power(H,3))
B=[(2,0),(4,0),(5,0),(5,1),(6,0),(7,0),(7,1),(8,0),(8,1),(8,2)]
expected=[None,(2,0),(7,0),(7,1),None,(8,0),(8,2),None,(4,0),None]
assert len(B)==10
M=[0]*10
for col,(i,a) in enumerate(B):
 f=i//3;s=i//2 if i%2==0 else (i+9)//2
 G=mul(1<<a,power(H,f))
 if i%2:G=mul(G,F)
 num=root_square(der(G))
 if not num:
  got=None
 else:
  assert s in [j for j,_ in B]
  fs=s//3;den=power(H,fs)
  assert num.bit_length()>=den.bit_length()
  # Divide polynomials exactly in GF(2).
  rem=num;quo=0
  while rem and rem.bit_length()>=den.bit_length():
   t=rem.bit_length()-den.bit_length();quo^=1<<t;rem^=den<<t
  assert rem==0 and quo.bit_count()==1
  got=(s,quo.bit_length()-1)
 assert got==expected[col],(col,got,expected[col])
 if got is not None:M[col]=1<<B.index(got)
def apply(v):
 r=0
 for i in range(10):
  if (v>>i)&1:r^=M[i]
 return r
basis=[1<<i for i in range(10)]
for degree,rank in [(0,10),(1,6),(2,3),(3,0)]:
 # These images are distinct coordinate vectors or zero; count nonzero distinct images.
 assert len(set(v for v in basis if v))==rank,(degree,basis)
 print('CARTIER_POWER_RANK',degree,rank)
 basis=[apply(v) for v in basis]
assert all(v==0 for v in basis)
print('ALL_TEN_CARTIER_IDENTITIES_OK')
print('CERTIFICATE_OK')
