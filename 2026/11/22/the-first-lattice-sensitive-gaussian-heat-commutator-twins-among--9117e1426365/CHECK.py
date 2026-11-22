#!/usr/bin/env python3
"""Exact integer certificates and finite checks of toral heat-commutator assertions."""
from collections import defaultdict
from fractions import Fraction
from math import pi, exp

A1=(-4,-1,1,0)
A2=(-2,-3,-1,-2)

def info(A):
    a,b,c,d=A
    assert a*d-b*c==1
    T=a*a+b*b+c*c+d*d
    tr=a+d
    # Q=I+A^T A
    u=1+a*a+c*c; v=a*b+c*d; w=1+b*b+d*d
    det=u*w-v*v
    assert det==T+2
    return tr,T,(u,v,w),det

def dual_quad(q,n):
    u,v,w=q
    x,y=n
    return w*x*x-2*v*x*y+u*y*y

def minimal_dual(q,det):
    # The vector (1,0) or (0,1) yields <=1/2 of shortest dual scale.
    # For Q with lambda_max <= trace(Q)=det, Q^-1 >= I/det.
    # Therefore minimizer n has |n|²<=det/2<=10 if det<=20.
    assert det<=20
    best=min(dual_quad(q,(1,0)),dual_quad(q,(0,1)))
    assert best<=det//2
    M=4  # |n|² <=10 => |n_i|<=3.
    minima=[]
    for x in range(-M,M+1):
      for y in range(-M,M+1):
        if x==y==0: continue
        val=dual_quad(q,(x,y))
        if val<best:
          best=val; minima=[(x,y)]
        elif val==best:
          minima.append((x,y))
    # no minimizer can lie outside the radius-4 box:
    assert best<=det//2<=10
    assert all(x*x+y*y<=10 for x,y in minima)
    return Fraction(best,det), len(minima), minima

h=defaultdict(list)
for a in range(-4,5):
 for b in range(-4,5):
  for c in range(-4,5):
   for d in range(-4,5):
    if a*d-b*c!=1: continue
    tr,T,q,det=info((a,b,c,d))
    if T<=18 and abs(tr)>2:
        mu,r,mins=minimal_dual(q,det)
        h[(tr,T)].append(((a,b,c,d),mu,r))
assert h

def unimodular_witness(Q,R):
    # Return a signed unimodular integer change of basis taking Q to R.
    u,v,w=Q; X,Y,Z=R
    for a in range(-5,6):
      for b in range(-5,6):
        for c in range(-5,6):
          for d in range(-5,6):
            if abs(a*d-b*c)!=1:continue
            if u*a*a+2*v*a*c+w*c*c!=X:continue
            if u*a*b+v*(a*d+b*c)+w*c*d!=Y:continue
            if u*b*b+2*v*b*d+w*d*d==Z:
                return (a,b,c,d)
    return None

# Every lower-complexity pair with the same dynamical trace and Euclidean
# Frobenius cost has GL(2,Z)-equivalent Gaussian quadratic forms.
for key,entries in h.items():
    tr,T=key
    if T>=18: continue
    Q0=info(entries[0][0])[2]
    for A,mu,r in entries:
        assert unimodular_witness(Q0,info(A)[2]) is not None
print('all T<18 forms have a common theta series within each trace: PASSED')
print('hyperbolic (trace, T) groups:',len(h))
for key,entries in sorted(h.items()):
 mus=sorted(set(v[1] for v in entries))
 print(key, 'count',len(entries),'dual minima',mus)
 assert key[1]==18 or len(mus)==1
assert sorted(set(m[1] for m in h[(-4,18)]))==[Fraction(1,10),Fraction(1,5)]
assert info(A1)==(-4,18,(18,4,2),20)
assert info(A2)==(-4,18,(6,8,14),20)
assert minimal_dual(info(A1)[2],20)[:2]==(Fraction(1,10),2)
assert minimal_dual(info(A2)[2],20)[:2]==(Fraction(1,5),2)
print('minimality & dual shortest-vector exact checks: PASSED')

def theta_energy(A,t,cut=40):
    a,b,c,d=A
    s=0.
    for x in range(-cut,cut+1):
      for y in range(-cut,cut+1):
        s+=(exp(-t*2*(x*x+y*y))-exp(-t*((x*x+y*y)+(a*x+b*y)**2+(c*x+d*y)**2)))
    return 2*s

def theta_poisson_energy(A,t,cut=40):
    tr,T,q,det=info(A)
    u,v,w=q
    val=pi/t*(1-2/det**.5)
    for x in range(-cut,cut+1):
      for y in range(-cut,cut+1):
        if x==y==0: continue
        val+=pi/t*exp(-pi*pi*(x*x+y*y)/(2*t))
        val-=2*pi/(t*det**.5)*exp(-pi*pi*dual_quad(q,(x,y))/(det*t))
    return val
for A in (A1,A2):
 for t in (0.4,0.75,1.,2.,4.):
    lhs=theta_energy(A,t); rhs=theta_poisson_energy(A,t)
    assert abs(lhs-rhs)<4e-10, (A,t,lhs,rhs)
print('finite direct/Poisson theta diagnostics: PASSED')
# Precise secondary length check all n in boxes
for A,mu,nextval in ((A1,Fraction(1,10),Fraction(2,5)),(A2,Fraction(1,5),Fraction(3,10))):
 q=info(A)[2]; det=20
 positive=sorted(set(Fraction(dual_quad(q,(x,y)),det) for x in range(-5,6) for y in range(-5,6) if x or y))
 assert positive[:2]==[mu,nextval],(A,positive[:5])
print('second dual length exact checks: PASSED')
