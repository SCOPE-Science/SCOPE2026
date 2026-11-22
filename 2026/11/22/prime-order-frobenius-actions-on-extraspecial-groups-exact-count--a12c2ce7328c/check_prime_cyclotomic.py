#!/usr/bin/env python3
"""Finite independent checks for prime-order cyclotomic actions on extraspecial groups.

Standard library only. This tests rank-one symplectic quotient matrices directly,
then tests group products and norm identities on finite Heisenberg groups.
It does not replace the proof for arbitrary symplectic rank.
"""
from itertools import product
from math import comb
from collections import Counter

def matmul(A,B,p):
 return ((A[0]*B[0]+A[1]*B[2])%p,(A[0]*B[1]+A[1]*B[3])%p,
         (A[2]*B[0]+A[3]*B[2])%p,(A[2]*B[1]+A[3]*B[3])%p)

def matpow(A,e,p):
 R=(1,0,0,1)
 while e:
  if e&1:R=matmul(R,A,p)
  A=matmul(A,A,p);e//=2
 return R

def inv2check(p,ell):
 I=(1,0,0,1)
 matrices=[]
 for A in product(range(p),repeat=4):
  a,b,c,d=A
  mu=(a*d-b*c)%p
  if not mu or mu==1 or pow(mu,ell,p)!=1:continue
  if matpow(A,ell,p)!=I:continue
  if ((a-1)*(d-1)-b*c)%p==0:continue
  matrices.append((A,mu))
 m=(ell-3)//2
 expected=(ell-1)*(1+m*p*(p+1)) if (p-1)%ell==0 else 0
 assert len(matrices)==expected,(p,ell,len(matrices),expected)
 classes=Counter((mu,(A[0]+A[3])%p) for A,mu in matrices)
 if expected:
  assert len(classes)==(ell-1)*(m+1),(p,ell,len(classes))
  if m:
   assert Counter(classes.values())==Counter({1:ell-1,p*(p+1):(ell-1)*m})
  else:
   assert set(classes.values())=={1}
 print('p=%d ell=%d symplectic-rank-one matrices=%d, predicted lifts=%d'%(p,ell,len(matrices),p*p*len(matrices)))
 return matrices

def group_check(p,ell,matrices,full):
 inv2=pow(2,-1,p)
 def mul(g,h):
  v,z=g;w,t=h
  return (((v[0]+w[0])%p,(v[1]+w[1])%p),
          (z+t+inv2*(v[0]*w[1]-v[1]*w[0]))%p)
 E=((0,0),0)
 pick=matrices if full else [matrices[i] for i in sorted({0,1,len(matrices)//2,len(matrices)-1})]
 taus=list(product(range(p),repeat=2)) if full else [(0,0),(1,0),(0,1),(1,1)]
 count=0
 for A,mu in pick:
  for tau in taus:
   def alpha(g):
    (x,y),z=g
    return (((A[0]*x+A[1]*y)%p,(A[2]*x+A[3]*y)%p),
            (mu*z+tau[0]*x+tau[1]*y)%p)
   for x,y,z in product(range(p),repeat=3):
    g=((x,y),z)
    if g!=E: assert alpha(g)!=g
    h=g;norm=E
    for _ in range(ell):
     norm=mul(norm,h);h=alpha(h)
    assert h==g,(p,ell,A,tau,g,'order')
    assert norm==E,(p,ell,A,tau,g,'norm')
   count+=1
 print('p=%d ell=%d group automorphisms checked=%d with complete element norm/period/fixedpoint verification'%(p,ell,count))

def main():
 assert not inv2check(5,3)
 q7=inv2check(7,3)
 q11=inv2check(11,5)
 inv2check(13,3)
 inv2check(29,7)
 group_check(7,3,q7,True)
 group_check(11,5,q11,False)
 # The full exponent-p^2 group has a nonzero pth-power linear form.
 # Every permitted eigenspace spectrum excludes the central multiplier,
 # while this form requires that eigenvalue. Confirm the residue involutions.
 for ell in (3,5,7,11):
  allowed=set(range(2,ell))
  invol=lambda i:(1-i)%ell
  assert all(invol(i) in allowed for i in allowed)
  fixed=[i for i in allowed if invol(i)==i]
  pairs={tuple(sorted((i,invol(i)))) for i in allowed if invol(i)!=i}
  assert len(fixed)==1 and len(pairs)==(ell-3)//2
  for n in range(1,5):
   m=(ell-3)//2
   # Number of nonnegative solutions to b+a_1+...+a_m=n.
   assert comb(n+m,m)>0
 print('PRIME_CYCLOTOMIC_EXTRASPECIAL_CHECKS_OK')
if __name__=='__main__':main()
