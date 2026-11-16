"""Exact-rational checks for pure quartic Hopf-torus trace spectra.
The global optimization proof is analytic; bounded checks are regressions.
"""
from fractions import Fraction as F
from math import factorial, comb


def add(p,q):
    out = [F(0)]*max(len(p),len(q))
    for k,c in enumerate(p): out[k] += c
    for k,c in enumerate(q): out[k] += c
    return out

def mul(p,q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j] += a*b
    return out

def powpoly(p,n):
    v=[F(1)]
    for _ in range(n): v=mul(v,p)
    return v

def jac(a,b,j):
    # P_j^(b,a)(2t-1), from Jacobi binomial expansion.
    out=[F(0)]
    for k in range(j+1):
        term=mulpow=mul(powpoly([F(0),F(1)],j-k),powpoly([F(1),F(-1)],k))
        out=add(out,[F((-1)**k*comb(j+b,j-k)*comb(j+a,k))*c for c in term])
    return out

def beta_integral(p,a,b):
    w=mul(mul(p,powpoly([F(0),F(1)],a)),powpoly([F(1),F(-1)],b))
    return sum(c*F(factorial(i),factorial(i+1)) for i,c in enumerate(w))

def orthonormal(a,b,j):
    c2=F(5*factorial(j)*factorial(j+a+b),factorial(j+a)*factorial(j+b))
    P=jac(a,b,j)
    assert c2*beta_integral(mul(P,P),a,b)==1,(a,b,j)
    for h in range(j):
        assert beta_integral(mul(P,jac(a,b,h)),a,b)==0,(a,b,j,h)
    return c2

levels=[]
for s in [0,2,4]:
    for a in range(s+1):
        b=s-a;j=(4-s)//2
        levels.append((a,b,j,orthonormal(a,b,j)))
assert sum((1 if a==0 else 2)*(1 if b==0 else 2) for a,b,j,c in levels)==25
assert len(levels)==9

def lam(a,b,j,t):
    c2=F(5*factorial(j)*factorial(j+a+b),factorial(j+a)*factorial(j+b))
    val=sum(coeff*t**i for i,coeff in enumerate(jac(a,b,j)))
    return c2*t**a*(1-t)**b*val**2

def f(t):return 25*t**3-48*t*t+30*t-6
lo=F(42,100);hi=F(43,100)
assert f(lo)<0<f(hi)
for _ in range(90):
    m=(lo+hi)/2
    if f(m)<0:lo=m
    else:hi=m
root=(lo+hi)/2
assert hi-lo<F(1,10**26)
A=5*root**4
B=30*root*(1-root)*(2*root-1)**2
assert abs(A-B)<F(1,10**23)
for a,b,j,c in levels:
    v=lam(a,b,j,root)
    if (a,b,j) not in [(4,0,0),(1,1,1)]:
        assert v>A,(a,b,j)
# Strict rational, interval-wide bounds on each potentially competing block.
assert 5*F(43,100)**4<F(171,1000)
assert 5*F(42,100)**2*(3-4*F(43,100))**2>F(171,1000)
assert 5*F(57,100)**2*(4*F(42,100)-1)**2>F(171,1000)
assert F(5,4)*(1-3*F(16,100)**2)**2>F(171,1000)
# Closed-form sector polynomials checked against Jacobi basis at independent rationals.
for t in [F(1,7),F(2,7),F(5,13),F(7,11)]:
    assert lam(4,0,0,t)==5*t**4
    assert lam(1,1,1,t)==30*t*(1-t)*(2*t-1)**2
    assert lam(2,0,1,t)==5*t*t*(4*t-3)**2
    assert lam(0,2,1,t)==5*(1-t)**2*(4*t-1)**2
    assert lam(0,0,2,t)==F(5,4)*(3*(2*t-1)**2-1)**2
    assert 5*t**4-30*t*(1-t)*(2*t-1)**2==F(5)*t*f(t)
assert abs(float(root)-0.425313431933887)<1e-12
assert abs(float(A)-0.163608701688)<2e-11
print('HOPF_QUARTIC_CHECK_OK', '9_sectors', '25_fourier_modes', '90_exact_bisections', 't=',float(root),'sharp_lower=',float(A))
