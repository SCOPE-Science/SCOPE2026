"""Finite corroboration for the sign-reversal correction (not an infinite proof)."""
from math import sqrt, exp, prod

# Exact input: F(u)=-1+(171/50)u-(36/25)u^2, with odd extension.
def fpos(u):
    return -1.0 + (171.0/50.0)*u - (36.0/25.0)*u*u

def deriv(u):
    return (171.0/50.0)-(72.0/25.0)*u

def f(x):
    if x == 0: raise ValueError('cut')
    return fpos(x) if x > 0 else -fpos(-x)

def iterate(x,n):
    for _ in range(n):
        x=f(x)
    return x

def bisect(fun,left,right,steps=65):
    a,b=left,right
    fa=fun(a)
    for _ in range(steps):
        c=(a+b)/2
        fc=fun(c)
        if fa*fc<=0: b=c
        else: a=c;fa=fc
    return (a+b)/2

def roots(fun,n=160000):
    # Positive half; return roots away from boundary and cut.
    pts=[]
    a=1e-8; fa=fun(a)
    for i in range(1,n+1):
        b=(1-1e-8)*i/n
        fb=fun(b)
        if fa*fb<0:
            r=bisect(fun,a,b)
            if not pts or abs(r-pts[-1])>1e-6: pts.append(r)
        a=b;fa=fb
    return pts

# Exact algebraic fixed-point roots and exact derivative values.
rminus=(121-sqrt(241))/144
rplus=(121+sqrt(241))/144
assert 0<rminus<rplus<1
assert abs(fpos(rminus)-rminus)<1e-13
assert abs(fpos(rplus)-rplus)<1e-13
assert deriv(1)>0 and 0<fpos(1)<1
assert abs(deriv(rminus)-(1+sqrt(241)/50))<1e-12
assert abs(deriv(rplus)-(1-sqrt(241)/50))<1e-12

# Continuous quotient avoids artificial sign changes across discontinuous cut preimages.
def q(u):
    return abs(fpos(u)) if u>0 else 1.0

def qiter(u,n):
    for _ in range(n):u=q(u)
    return u

def qderivative(u,n):
    d=1.0
    for _ in range(n):
        y=fpos(u)
        d*=deriv(u)*(1 if y>0 else -1)
        u=abs(y)
    return d

for n in (1,3,5):
    pts=roots(lambda u:qiter(u,n)-u)
    decreasing=sum(qderivative(u,n)<0 for u in pts)
    attracting=sum(0<=qderivative(u,n)<1 for u in pts)
    repelling=sum(qderivative(u,n)>1 for u in pts)
    assert decreasing+attracting-repelling==1, (n,decreasing,attracting,repelling)
    aF=2*(attracting+repelling)
    aG=2*decreasing
    AF=2*attracting
    assert aG-aF==2-2*AF
    print('n =',n,'quotient fixed points:',len(pts),'F/G/A counts:',aF,aG,AF)

# Independent family: numerical monotonicity witnesses and fixed-root derivative alternation.
for k in (1,2,3):
    r=[j/(2*k+1) for j in range(1,2*k+1)]
    K=25.0
    def P(u):return prod((u-t)/t for t in r)
    def Pd(u):
        return sum(prod((u-r[j])/r[j] for j in range(2*k) if j!=i)/r[i] for i in range(2*k))
    def derivative(u):return 1+exp(-K*u)*(K*P(u)-Pd(u))
    assert min(derivative(i/3000.0) for i in range(3001))>0
    assert 0<exp(-K)*P(1)<1
    for j,t in enumerate(r):
        d=derivative(t)
        assert d>1 if j%2==0 else 0<d<1
    print('analytic family sample k =', k, 'positive F fixed roots:', len(r))
print('Finite checks passed; all-period proof is separate.')
