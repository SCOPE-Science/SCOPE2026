"""Finite checks for the Gaussian Mehler-mixture variation-error identities.

Run with Python 3; uses only the standard library. These numerical tests
corroborate, but cannot replace, the analytic proofs in RESULT.md.
"""
from fractions import Fraction
from math import acos, asin, erf, exp, pi, sqrt


def phi(x):
    return exp(-x*x/2)/sqrt(2*pi)


def Phi(x):
    return (1+erf(x/sqrt(2)))/2


def q(r,s,N=16000):
    """P(X>s,Y>s), via conditional one-dimensional quadrature."""
    p=Phi(-s)
    if r==1.0: return p
    if r==0.0: return p*p
    high=12.0
    dx=(high-s)/N
    den=sqrt(1-r*r)
    def v(x): return phi(x)*Phi((r*x-s)/den)
    return dx/3*(v(s)+v(high)+4*sum(v(s+(2*j-1)*dx) for j in range(1,N//2+1))
                 +2*sum(v(s+2*j*dx) for j in range(1,N//2)))


def exact_median(mix):
    a=sum(w*asin(r) for r,w in mix)
    b=sum(w*v*asin(r*s) for r,w in mix for s,v in mix)
    return 0.25+(b-2*a)/(2*pi)


def residual(s,mix,N=16000):
    return (Phi(-s)-2*sum(w*q(r,s,N) for r,w in mix)
            +sum(w*v*q(r*u,s,N) for r,w in mix for u,v in mix))


def derivative_over_phi(s,mix):
    u=lambda r: sqrt((1-r)/(1+r))
    return (-2*sum(w*erf(u(r)*s/sqrt(2)) for r,w in mix)
            +sum(w*v*erf(u(r*u0)*s/sqrt(2)) for r,w in mix for u0,v in mix))


def check():
    n=0
    # Exact algebraic identity for the correlation-product parameter.
    for a in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(7,8),Fraction(1)]:
        for b in [Fraction(0),Fraction(1,5),Fraction(2,3),Fraction(9,10),Fraction(1)]:
            u2=(1-a)/(1+a)
            v2=(1-b)/(1+b)
            w2=(1-a*b)/(1+a*b)
            assert w2 == (u2+v2)/(1+u2*v2)
            assert w2 <= u2+v2
            n+=2
    mixtures=[[(1.0,0.2),(0.35,0.3),(0.0,0.5)],[(0.7,1.0)],[(0.0,1.0)],[(1.0,0.97),(0.1,0.03)]]
    for mix in mixtures:
        assert abs(sum(w for r,w in mix)-1)<1e-14
        c2=exact_median(mix)
        assert 0<c2<=.25
        n+=2
        nums=[residual(s,mix) for s in [0,0.15,0.5,1,2]]
        assert abs(nums[0]-c2)<2e-7,(mix,nums[0],c2)
        for j in range(1,len(nums)):
            assert nums[j]<nums[j-1],(mix,nums)
            assert derivative_over_phi([0,.15,.5,1,2][j],mix)<0
            n+=2
        n+=1
    # Pure Gaussian semigroup: small-time leading coefficient and end behavior.
    for t in [.0001,.00002,.000004]:
        rho=exp(-t)
        c2=exact_median([(rho,1.0)])
        limit=(sqrt(2)-1)/pi
        assert abs(c2/sqrt(t)-limit)<.005
        n+=1
    for t in [1,3,5,10]:
        c2=exact_median([(exp(-t),1.0)])
        assert c2<.25 and c2>0
        n+=1
    print(f"PASS: {n} checks (exact fraction identities, independent integral quadrature, monotonicity, and asymptotics)")

if __name__=='__main__': check()
