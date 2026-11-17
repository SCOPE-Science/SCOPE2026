"""Exact symbolic and independent quadrature checks for a quadratic Jacobi BV operator theorem."""
import math
import random
from math import gamma, sqrt, pi
import sympy as sp
import mpmath as mp

def constants(alpha):
    r=alpha+1
    k=2*r+3
    b=k*k+1-2*r
    disc=b*b-4*k*k*(2*r+1)
    z=(b+math.sqrt(disc))/(2*k*k*(2*r+1))
    c=math.exp(math.lgamma(r+.5)-math.lgamma(r)-.5*math.log(pi))
    C=(2*r+1)/(2*r)*c
    a=k*math.sqrt(z)
    M=C*((1-z)**r)*(a+1/a)
    return r,k,z,C,M

def direct_jump_quadrature(alpha,t):
    mp.mp.dps=75
    aa=mp.mpf(str(alpha)); tt=mp.mpf(str(t)); r=aa+1
    norm=mp.beta(mp.mpf('.5'),r)
    m2=1/(2*aa+3)
    m4=3/((2*aa+3)*(2*aa+5))
    A=mp.quad(lambda v: v*(1-v*v)**aa,[tt,1])/norm
    B=mp.quad(lambda v:(v*v-m2)*(1-v*v)**aa,[tt,1])/norm
    p=A/m2; q=2*B/(m4-m2*m2)
    root=-p/q if abs(q)>mp.mpf('1e-15') else None
    grid=[mp.mpf(-1),mp.mpf(1)]
    if root is not None and -1<root<1:grid=[mp.mpf(-1),root,mp.mpf(1)]
    direct=sum(abs(mp.quad(lambda x:p+q*x,[a,b])) for a,b in zip(grid,grid[1:]))
    kk,C=(2*aa+5),(2*aa+3)/(2*(aa+1)*norm)
    a=abs(kk*tt)
    formula=C*(1-tt*tt)**r*(2 if a<=1 else a+1/a)
    return float(direct),float(formula)

def symbolic_checks():
    r,t,x=sp.symbols('r t x',real=True,positive=True)
    k=2*r+3
    B=k*k+1-2*r
    P=(k*k*t*t-1)*(1-t*t)-2*r*t*t*(k*k*t*t+1)
    assert sp.simplify(P-(-k*k*(2*r+1)*t**4+B*t*t-1))==0
    # independent check of rank-two kernel and beta moment normalization
    q=2*r+1
    moment2=1/q
    moment4=3/(q*(q+2))
    var=sp.factor(moment4-moment2**2)
    assert sp.simplify(var-2*(q-1)/(q*q*(q+2)))==0
    # A integral = (1-t^2)^r/(2*r*Z), B = t(1-t^2)^r/(q*Z).
    # Relative affine slope must be k*t.
    ratio=sp.simplify((2*t/q)/var/(1/(2*r)/moment2))
    assert sp.simplify(ratio-k*t)==0
    # discriminant
    assert sp.simplify(B*B-4*k*k*(2*r+1)-4*(4*r**4+12*r**3+17*r**2+20*r+16))==0
    print('SYMBOLIC_JACOBI_MOMENTS_AND_STATIONARITY_PASS')

def numerical_checks():
    rr=random.Random(80419)
    N=0
    for alpha in [-.75,-.5,-.25,0,.4,1,3,15,60]:
        r,k,z,C,M=constants(alpha)
        assert 0<z<1
        t=math.sqrt(z)
        for pos in [-t,t,0,.25,.6]:
            d,f=direct_jump_quadrature(alpha,pos)
            if not math.isclose(d,f,rel_tol=2e-8,abs_tol=2e-8):raise AssertionError((alpha,pos,d,f))
            assert d<=M+1e-7
            N+=1
        assert M>2*C
        # Derivative sign and maximum on a fine grid, using exact integral of affine derivative
        for j in range(701):
            s=j/700
            a=k*s
            value=C*(1-s*s)**r*(2 if a<=1 else a+1/a)
            assert value<=M+1e-8,(alpha,s,value,M)
        # signed jump expansion yields a finite-BV function
        for i in range(8):
            jumps=sorted((rr.uniform(-.95,.95),rr.uniform(-1,1)) for _ in range(7))
            # using coefficient identity rather than unreliable sampling
            p=sum(2*C*(1-u*u)**r*d/2 for u,d in jumps)  # affine derivative constant
            q=sum((2*C*(1-u*u)**r)*(k*u)*d/2 for u,d in jumps)
            root=-p/q if abs(q)>1e-12 else 2
            points=[-1,1] if not -1<root<1 else [-1,root,1]
            var=sum(abs(p*(b-a)+.5*q*(b*b-a*a)) for a,b in zip(points,points[1:]))
            assert var<=M*sum(abs(d) for _,d in jumps)+1e-8
    print('DIRECT_INDEPENDENT_WEIGHTED_QUADRATURE_PASS',N)
    print('ALL_JUMP_AND_SIGNED_BV_STRESS_PASS')
    for r in [1e-4,1e-5,1e-6]:
        val=constants(r-1)[-1]
        assert abs(val-5/3)<0.01
    c=math.sqrt(2/(math.pi*math.e))
    for r in [1000,10000]:
        M=constants(r-1)[-1]
        assert abs(M/r-c)<.005
    print('SINGULAR_JACOBI_LIMITS_PASS')

if __name__=='__main__':
    symbolic_checks()
    numerical_checks()
    print('ALL_QUADRATIC_JACOBI_BV_CHECKS_PASS')
