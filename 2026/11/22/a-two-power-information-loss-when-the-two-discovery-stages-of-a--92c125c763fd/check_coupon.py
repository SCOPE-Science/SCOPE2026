"""Exact arithmetic diagnostics for two-stage coupon waiting-time inference.

Uses only Python standard library. Finite checks supplement, never replace, the
analytic proof of the all-parameter and asymptotic assertions.
"""
from fractions import Fraction as F
from math import comb, factorial

def mean_variance(m,h):
    z=F(1,2*m-1)
    p=1/(h*(1-z));q=1/(h*(1+z))
    mean=(1-p)/p+(1-q)/q
    var=(1-p)/p**2+(1-q)/q**2
    return mean,var,p,q,z

def coeffs(h,z,nt):
    eta=z*z
    a0=h*h*(1-eta)
    a1=-2*h*(h-1)+2*h*h*eta
    a2=(h-1)**2-h*h*eta
    C=[1/a0]
    C.append(-a1*C[0]/a0)
    for t in range(2,nt):
        C.append(-(a1*C[t-1]+a2*C[t-2])/a0)
    return C

def geometric_convolution(p,q,t):
    a,b=1-p,1-q
    return p*q*sum((a**j*b**(t-j) for j in range(t+1)),F(0))

def moment_of_poly(eval_poly,degree,h):
    """NB(2,1/h) polynomial expectation via Newton finite differences."""
    aa=h-1 # a/(1-a) = h-1
    vals=[eval_poly(i) for i in range(degree+1)]
    return sum((sum(((-1)**(j-i)*comb(j,i)*vals[i] for i in range(j+1)),F(0))*(j+1)*aa**j for j in range(degree+1)),F(0))

def score_total(h,t):
    mu=2*h-2
    return ((t-mu)**2-(2*h-1)*(t-mu)-2*h*(h-1))/(6*(h-1)**2)

def score_poly_coeff(h,t):
    a=(h-1)/h
    return ((t+3)*(t+2)-2*t*(t+2)/a+t*(t-1)/a**2)/6

def derivative_prob(h,t):
    a=(h-1)/h
    def term(j):
        u=t-j
        return F(0) if u<0 else (-1)**j*comb(2,j)*comb(u+3,3)*a**u/h**2
    return sum((term(j) for j in range(3)),F(0))

checks=0
for h in [F(8,5),F(2),F(5,2),F(3),F(9,2)]:
    aa=(h-1)/h
    for m in range(2,36):
        mu,var,p,q,z=mean_variance(m,h)
        eta=z*z
        assert 0<p<1 and 0<q<1 and q<p; checks+=1
        assert mu==2*h-2 and var==2*h*h*(1+eta)-2*h;checks+=1
        R=(var+mu+2)/(mu+2)**2
        assert R==F(1,2)+F(1,2*(2*m-1)**2);checks+=1
        recovered=(1+F(1,1)/z)/2
        assert recovered==m; checks+=1
        C=coeffs(h,z,27)
        for t in range(27):
            assert C[t]==geometric_convolution(p,q,t);checks+=1
    for t in range(40):
        assert score_total(h,t)==score_poly_coeff(h,t);checks+=1
        base=(t+1)*(1/h)**2*aa**t
        assert derivative_prob(h,t)==base*score_total(h,t);checks+=1
    E=lambda f,deg:moment_of_poly(f,deg,h)
    s=lambda t:score_total(h,t)
    assert E(s,2)==0;checks+=1
    assert E(lambda t:t*s(t),3)==0;checks+=1
    assert E(lambda t:s(t)**2,4)==1/(3*aa**2);checks+=1
    mu=2*h-2;V=2*h*(h-1)
    psi=lambda t:((t-mu)**2-(2*h-1)*(t-mu)-V)/(4*h*h)
    assert E(psi,2)==0;checks+=1
    assert E(lambda t:psi(t)**2,4)==3*aa**2/4;checks+=1
    for t in range(8):
        assert psi(t)==F(3,2)*aa**2*s(t);checks+=1
for m in range(2,100):
    z=F(1,2*m-1);zp=F(1,2*m+1)
    assert z-zp==F(2,(2*m-1)*(2*m+1));checks+=1
    assert z*z-zp*zp==F(8*m,(2*m-1)**2*(2*m+1)**2);checks+=1
    assert (z*z-zp*zp)/2==F(4*m,(4*m*m-1)**2);checks+=1
assert F(2,3)>0
print(f'PASS: {checks} exact-rational identities (finite diagnostics only)')
