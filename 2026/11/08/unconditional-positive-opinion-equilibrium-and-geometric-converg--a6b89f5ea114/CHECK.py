"""Standalone exact and numerical checks for positive-opinion leadership equilibria.
Run with Python 3.10+: python CHECK.py
Numerical checks supplement, rather than establish, the general theorem.
"""
from fractions import Fraction as F
from math import log, exp
from random import Random


def residual(x, anchor, W, rho):
    return [rho * (x[i]-anchor[i]) + (x[i]-sum(W[i][j]*x[j] for j in range(len(x))))**3/x[i]**2 for i in range(len(x))]


def scalar_root(m, u, rho, lo, hi):
    # Unique positive zero of rho*(z-u)+(z-m)**3/z**2.
    def f(z): return rho*(z-u)+(z-m)**3/z**2
    assert f(lo) <= 1.e-12 and f(hi) >= -1.e-12
    for _ in range(66):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def mapping(x, anchor, W, rho):
    lo,hi=min(anchor),max(anchor)
    return [scalar_root(sum(W[i][j]*x[j] for j in range(len(x))), anchor[i], rho, lo,hi) for i in range(len(x))]


def vector_field(x, anchor, W, rho):
    n=len(x); out=[]
    for i in range(n):
        d=x[i]-sum(W[i][j]*x[j] for j in range(n))
        out.append(-(d**3+rho*x[i]**2*(x[i]-anchor[i]))/(rho*x[i]**2+d**2))
    return out


def rk4(x, anchor, W, rho, h):
    def add(z,k,r): return [v+r*t for v,t in zip(z,k)]
    a=vector_field(x,anchor,W,rho)
    b=vector_field(add(x,a,h/2),anchor,W,rho)
    c=vector_field(add(x,b,h/2),anchor,W,rho)
    d=vector_field(add(x,c,h),anchor,W,rho)
    return [v+h*(u+2*w+2*z+t)/6 for v,u,w,z,t in zip(x,a,b,c,d)]


def main():
    # Exact witness, parameters: rho=16, W swaps two agents.
    rho=F(16); W=[[F(0),F(1)],[F(1),F(0)]]
    anchor=[F(55,72),F(1,8)]
    equilibrium=[F(3,4),F(1,4)]
    assert residual(equilibrium,anchor,W,rho)==[0,0]
    d=[equilibrium[0]-equilibrium[1],equilibrium[1]-equilibrium[0]]
    y=[rho*equilibrium[i]**2/(rho*equilibrium[i]**2+d[i]**2) for i in range(2)]
    assert y==[F(36,37),F(4,5)]
    assert all(-(1-y[i])*d[i]-y[i]*(equilibrium[i]-anchor[i])==0 for i in range(2))
    assert all(rho*(1-y[i])*equilibrium[i]**2-y[i]*d[i]**2==0 for i in range(2))
    a,b=min(anchor),max(anchor)
    q=1-rho*a**3/(rho*b**3+3*b*(b-a)**2)
    c=rho*a**3/(b*(rho*b**2+(b-a)**2))
    assert 0<q<1 and c>0
    # Source sufficient-contraction expression at the largest possible epsilon=1/4.
    epsilon=F(1,4)
    source_ratio=3*(b-a)**2/(rho*epsilon**2)*(2*b/epsilon+1)
    assert source_ratio > 1
    print('Exact equilibrium:',tuple(map(str,equilibrium)))
    print('Exact leadership:',tuple(map(str,y)))
    print('Source contraction bound at epsilon=1/4:',float(source_ratio))
    print('Explicit log-iteration factor q:',float(q))
    print('Explicit reduced-flow rate c:',float(c))
    A=[float(v) for v in anchor]; M=[[float(v) for v in r] for r in W]; r=float(rho)
    low=[float(a)]*2; high=[float(b)]*2
    for k in range(1,501):
        low,high=mapping(low,A,M,r),mapping(high,A,M,r)
        assert all(low[j]<=float(equilibrium[j])+1.e-11 and float(equilibrium[j])<=high[j]+1.e-11 for j in range(2))
        assert all(low[j]<=high[j]+1.e-12 for j in range(2))
        assert all(high[j]-low[j]<=float(b)*float(q)**k*log(float(b/a))+1.e-10 for j in range(2))
    assert max(high[j]-low[j] for j in range(2))<1.e-10
    print('Witness lower/upper bracket after 500 iterations:',tuple(round(v,14) for v in low),tuple(round(v,14) for v in high))
    # RK4 compares the explicit analytic logarithmic-flow rate with the reduced dynamics.
    x=[float(a),float(b)]; e0=max(abs(log(x[j]/float(equilibrium[j]))) for j in range(2))
    for k in range(1,501):
        x=rk4(x,A,M,r,.01)
        err=max(abs(log(x[j]/float(equilibrium[j]))) for j in range(2))
        assert err <= e0*exp(-float(c)*k*.01)+1.e-8
    print('Reduced dynamics final state t=5:',tuple(round(v,12) for v in x))
    # Random strongly varying positive anchors and row-stochastic networks.
    rng=Random(3021)
    tests=0
    for n in [2,3,5]:
      for _ in range(35):
        anchor=[rng.uniform(.04,.99) for j in range(n)]
        a,b=min(anchor),max(anchor)
        W=[]
        for i in range(n):
          weights=[rng.expovariate(1) for j in range(n)]
          W.append([v/sum(weights) for v in weights])
        rho=10**rng.uniform(-2,2)
        q=1-rho*a**3/(rho*b**3+3*b*(b-a)**2)
        lo=[a]*n; hi=[b]*n
        for j in range(300):
          lo=mapping(lo,anchor,W,rho); hi=mapping(hi,anchor,W,rho)
          assert all(lo[i]<=hi[i]+2e-11 for i in range(n))
          assert all(hi[i]-lo[i]<=b*q**(j+1)*log(b/a)+1e-10 for i in range(n))
        x=lo
        assert max(abs(v) for v in residual(x,anchor,W,rho))<2e-3 or max(hi[i]-lo[i] for i in range(n))>1.e-3
        tests+=1
    print('Random bracket and bound tests passed:',tests)

if __name__=='__main__':main()
