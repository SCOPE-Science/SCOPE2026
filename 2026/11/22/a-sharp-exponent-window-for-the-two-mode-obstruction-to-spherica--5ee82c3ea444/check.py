"""Finite reproducibility checks for the spherical two-mode fourth-order threshold.

Requires Python 3, scipy, sympy. This verifies identities and sampled cases;
the proof of universal signs and asymptotics is analytic in RESULT.md.
"""
import math
from fractions import Fraction
from scipy.optimize import brentq
from scipy.special import roots_jacobi
import sympy as sp

def coeffs(d, q):
    M = d+1
    t = q-1
    R = math.sqrt(2*M/(M-1))
    b = t**(-R/2)
    h = 1-t*b*b
    w = 2*(M-1)/(M*M*(M+2))
    A = -q*w*h/2
    B = q*(q-2)*b*w/2
    C = -q*(q-2)*(M+q-1)/(4*t*M*M*(M+2))
    c = -B/(2*A)
    D = C-B*B/(4*A)
    return R,b,c,A,B,C,D

def moment(M,j):
    out=sp.Integer(1)
    for k in range(1,j+1):
        out *= sp.Rational(2*k-1,M+2*k-2)
    return out

def symbolic_case(d,q):
    M=d+1; eps,c,a,b=sp.symbols('eps c a b',real=True)
    x=sp.symbols('x',real=True)
    y=x*x-sp.Rational(1,M)
    E=lambda expr: sum(coef*moment(M,int(mon[0])//2) if mon[0]%2==0 else sp.Integer(0) for mon,coef in sp.Poly(sp.expand(expr),x).terms())
    z=1+a*eps*x+b*c*eps**2*y
    lhs=E(sp.expand(z**q))
    fnorm=1+eps**2*sp.Rational(1,M)+c*c*eps**4*E(y*y)
    # Expand the right norm in eps, then force the first harmonic Nelson multiplier.
    rhs=sp.series(fnorm**sp.Rational(q,2),eps,0,5).removeO()
    quart=sp.Poly(sp.expand(lhs-rhs),eps).coeff_monomial(eps**4).subs(a*a,sp.Rational(1,q-1))
    quart=sp.factor(quart)
    # Terms in epsilon^4 depend on a^4 and a^2 only.
    quart=quart.subs(a**4,sp.Rational(1,(q-1)**2)).subs(a*a,sp.Rational(1,q-1))
    w=sp.Rational(2*(M-1),M*M*(M+2))
    A=-sp.Rational(q,2)*w*(1-(q-1)*b*b)
    B=sp.Rational(q*(q-2),2)*b*w
    C=-sp.Rational(q*(q-2)*(M+q-1),4*(q-1)*M*M*(M+2))
    assert sp.simplify(quart-(A*c*c+B*c+C))==0
    return True

def critical(d):
    M=d+1;R=math.sqrt(2*M/(M-1))
    F=lambda t: (1-R)*math.log(t)+math.log(M*t+1)-math.log(M+t)
    return 1+brentq(F,1.00001,M**4)

if __name__=='__main__':
    tests=0
    for d in [4,5,7,10]:
        for q in [4,6,8]:
            assert symbolic_case(d,q);tests+=1
    expected={4:6.8035120211789,5:14.8695791364333,6:26.5361716749417,10:120.234312662278}
    for d,target in expected.items():
        assert abs(critical(d)-target)<1e-7;tests+=1
        assert coeffs(d, (critical(d)+2)/2)[-1]>0;tests+=1
        assert coeffs(d, critical(d)+1)[-1]<0;tests+=1
    for d in [4,5,6]:
        M=d+1
        x,w=roots_jacobi(120,(M-3)/2,(M-3)/2)
        w/=w.sum()
        for q in [3.,4.,6.]:
            R,b,c,A,B,C,D=coeffs(d,q)
            assert D>0
            for eps in [0.02,0.05]:
                f=1+eps*x+c*eps**2*(x*x-1/M)
                pf=1+eps*(q-1)**(-.5)*x+c*eps**2*b*(x*x-1/M)
                assert min(f)>0 and min(pf)>0
                delta=sum(w*pf**q)-sum(w*f*f)**(q/2)
                assert delta>0 and abs(delta/eps**4-D)<0.025*D
                tests+=1
    print(f'PASS: {tests} finite symbolic, transition and quadrature diagnostics')
