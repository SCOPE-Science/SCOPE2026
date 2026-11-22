"""Exact finite checks for periodic-window projected firing; not a substitute for proof."""
from fractions import Fraction as F
from math import floor, gcd
from decimal import Decimal, getcontext

def frac(x):
    return x - (x.numerator // x.denominator)

def phase(x, beta, eta):
    z = frac(x+beta)
    return z if z <= eta else F(0)

def project(x, tau, eta):
    z=x+tau
    k=z.numerator//z.denominator
    return z if z-k <= eta else F(k+1)

def first_hit(beta,eta,q):
    for r in range(1,q):
        if frac(r*beta)>eta:
            return r
    return None

def safe_set(x,beta,eta,q):
    return all(frac(x+j*beta)<=eta for j in range(q))

cases=checks=0
for q in range(2,13):
  for p in range(1,q):
    if gcd(p,q)!=1:continue
    beta=F(p,q); critical=F(q-1,q)
    widths={F(1,25),F(1,3),F(2,3),F(9,10),critical}
    for i in range(q):
        widths.add((F(i,q)+F(i+1,q))/2)
    for eta in sorted(x for x in widths if 0<x<1):
      r=first_hit(beta,eta,q)
      assert (r is None)==(eta>=critical)
      orb={frac(j*beta) for j in range(r)} if r else None
      for m in range(4):
        tau=F(m)+beta
        if r is not None:
          P= m*r - (-r*beta.numerator//beta.denominator)
          assert P==m*r+(r*beta.numerator+beta.denominator-1)//beta.denominator
          t=F(0)
          for j in range(r):
              t=project(t,tau,eta)
          assert t==P
        period=r if r else q
        duration=P if r else m*q+p
        for a in range(0,9):
          x=eta*F(a,8)
          t=x
          for j in range(q):
             old=t;t=project(t,tau,eta)
             checks+=1
             assert frac(t)==phase(frac(old),beta,eta)
          y=frac(t)
          if r:
             assert y in orb
          else:
             assert safe_set(y,beta,eta,q)
          t2=t
          for j in range(period):t2=project(t2,tau,eta)
          assert t2-t==duration
          checks+=1
        cases+=1
    # finite grid area test for rational-survivor phase measure
    for eta in [critical, (critical+1)/2]:
        count=0; total=600
        for i in range(total):
            x=F(2*i+1,2*total)
            if safe_set(x,beta,eta,q):count+=1
        theory=max(F(0), q*eta-(q-1))
        assert abs(F(count,total)-theory)<=F(q,total)
        checks+=1

# Irrational checks are high precision finite stress-tests, not infinite proofs.
getcontext().prec=85
beta=(Decimal(5).sqrt()-1)/2
for eta_s in ['0.05','0.3','0.6','0.8','0.95','0.99']:
    eta=Decimal(eta_s)
    x=Decimal(0);r=0
    while True:
        r+=1
        x=(Decimal(r)*beta)%1
        if x>eta:break
        assert r<100000
    for j in range(r):
        assert (Decimal(j)*beta)%1<=eta
    for a in range(21):
        x=eta*Decimal(a)/20
        for it in range(15000):
            z=(x+beta)%1
            x=z if z<=eta else Decimal(0)
            if x==0:break
        assert it<14999
        checks+=1

print('PASS rational parameter cases',cases,'exact and high-precision checks',checks)
