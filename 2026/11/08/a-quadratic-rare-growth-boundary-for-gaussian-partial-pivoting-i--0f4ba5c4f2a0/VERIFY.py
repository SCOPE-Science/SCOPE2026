"""Reproducibility checks for the 2x2 Gaussian partial-pivoting growth tail.

Only standard-library modules are needed. Finite numerical checks do not replace
proofs of the limiting probability and density-universal exponent.
"""
import math
import random
from fractions import Fraction


def growth(A):
    """Direct one-step, row-pivoted elimination in real arithmetic."""
    a,b,c,d=A
    original=max(map(abs,A))
    if abs(c)>abs(a):
        a,b,c,d=c,d,a,b
    if a==0 or original==0:
        raise ValueError('degenerate test')
    schur=d-(c/a)*b
    return max(original,abs(a),abs(b),abs(schur))/original


def growth_fraction(A):
    a,b,c,d=map(Fraction,A)
    original=max(map(abs,(a,b,c,d)))
    if abs(c)>abs(a):
        a,b,c,d=c,d,a,b
    return max(original,abs(a),abs(b),abs(d-c*b/a))/original


def gaussian_tail_integral(t,ntheta=360,nq=360):
    """Midpoint quadrature of the derived exact 2D Gaussian tail law."""
    v=0.0
    for i in range(ntheta):
        theta=(i+0.5)*math.pi/(2*ntheta)
        si,co=math.sin(theta),math.cos(theta)
        q_min=max(0.0, (t*max(si,co)-si)/co)
        if q_min>=1:
            continue
        hq=(1-q_min)/nq
        for j in range(nq):
            q=q_min+(j+0.5)*hq
            h=si+q*co
            v += (4/math.pi**2)*h*h/(t*t+(1+q*q)*h*h)*hq*math.pi/(2*ntheta)
    return v


def run():
    for A in [(1,1,-1,1),(-2,7,1,-3),(5,-7,3,-2), (1,50,0.5,100)]:
        assert abs(growth(tuple(map(float,A)))-float(growth_fraction(A)))<1e-13
    assert growth_fraction((1,1,-1,1))==2
    assert growth_fraction((1,50,Fraction(1,2),100))==1
    rng=random.Random(314159265)
    for k in range(1200):
        A=[rng.randint(-99,99) or 1 for _ in range(4)]
        assert abs(growth(tuple(map(float,A)))-float(growth_fraction(A)))<1e-12
    expected={1.5:0.02194037589310731, 1.9:0.00056084486590013}
    for t,v in expected.items():
        z=gaussian_tail_integral(t)
        print('quadrature',t,z)
        assert abs(z-v)<3e-7
    N=450000
    counts={t:0 for t in expected}
    for _ in range(N):
        A=tuple(rng.gauss(0.,1.) for i in range(4))
        rho=growth(A)
        for t in counts:
            counts[t]+=(rho>t)
    for t,cnt in counts.items():
        rate=cnt/N
        print('simulation',t,rate,'theory',expected[t])
        assert abs(rate-expected[t])<6.5*math.sqrt(expected[t]*(1-expected[t])/N)+5e-5
    # Exact coefficient evaluations from elementary exponential integrals:
    coeff_gauss=1/(2*math.pi**2)
    coeff_laplace=Fraction(1,32)
    assert abs(coeff_gauss-0.05066059182116889)<1e-14
    assert coeff_laplace==Fraction(1,32)
    print('endpoint coefficient Gaussian',coeff_gauss,'Laplace',str(coeff_laplace))
    print('VERIFY_OK')

if __name__=='__main__':
    run()
