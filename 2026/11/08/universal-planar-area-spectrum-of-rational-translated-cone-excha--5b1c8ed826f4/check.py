"""Exact-rational checks for the periodic spectrum of a translated-cone-exchange slice.
The analytical proof is in RESULT.md; finite checks do not imply its full scope.
"""
from fractions import Fraction as F
from math import gcd

def H(x, lam, u, v):
    eta=1-lam
    if x < -v: return x+lam
    if x < u: return x-eta
    return x-1

def return_R(x, lam, u, v):
    L=1+lam
    left=u-1
    right=lam-v
    def r(z):
        z+=lam
        if z>=lam: z-=L
        return z
    z=r(x)
    if left<=z<right:return z,1
    z=r(z)
    assert left<=z<right
    return z,2

def minimum_period(x,lam,u,v):
    y=x
    n=0
    while True:
        y=H(y,lam,u,v)
        n+=1
        if y==x:return n
        assert n<100

def test():
    nchecks=0
    for q in range(2,9):
      for p in range(1,q):
        if gcd(p,q)!=1:continue
        lam=F(p,q)
        N=p+q
        for s in range(1,5):
          c=lam*F(s,5)
          u=c*F(2,5);v=c-u
          # Test induced map on many generic rational points.
          lo=u-1; hi=lam-v
          for k in range(1,13):
            x=lo+(hi-lo)*F(k,13)
            if x in (-v,u):continue
            out,r=return_R(x,lam,u,v)
            assert H(x,lam,u,v)==out,(p,q,c,x,'induced')
            nchecks+=1
            n=minimum_period(x,lam,u,v)
            z=q*c
            floor=z.numerator//z.denominator
            assert n in (N-floor,N-floor-1),(p,q,c,x,n)
            nchecks+=1
          z=q*c; j=z.numerator//z.denominator; th=z-j
          # A layer consists of regular circle orbits parametrized
          # by the lattice offset; exactly the expected two periods.
          for k in range(1,13):
            # offset t ∈ (0,1/q); then orbit is t+v/q for v=0..N-1,
            # reduced modulo circumference L.
            t=F(k,13*q)
            orbit=[t+F(i,q)-1 for i in range(N)]
            kept=[x for x in orbit if lo<=x<hi]
            assert len(kept) in (N-j,N-j-1)
            for x in kept:
                n=minimum_period(x,lam,u,v)
                assert n==len(kept)
                nchecks+=1
          # Theoretical area law sums to one for each parameter.
          # Independently assemble slice-area contributions from adjacent
          # bands (the altitude prefactor cancels in normalized areas).
          raw={m:F(0) for m in range(q,N+1)}
          for band in range(p):
              raw[N-band]+=F(N-band,2*q*q)
              raw[N-band-1]+=F(N-band-1,2*q*q)
          total=sum(raw.values())
          assert total==lam*(1+lam/F(2))
          probabilities=[raw[N-i]/total for i in range(p+1)]
          target=[F((N-i)*(1 if i in (0,p) else 2),p*(2*q+p)) for i in range(p+1)]
          assert probabilities==target
          assert sum(probabilities)==1
          nchecks+=p+2
    print('PASS',nchecks,'exact-rational assertions')
if __name__=='__main__':test()
