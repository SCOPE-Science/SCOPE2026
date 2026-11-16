"""Independent finite consistency checks for the two-channel rational-window Zak energy.
The infinite-dimensional claims are proved analytically in RESULT.md.
Requires only the Python standard library.
"""
import math
from fractions import Fraction
from itertools import product

pi = math.pi
count = 0

def check(p, context):
    global count
    count += 1
    if not p:
        raise AssertionError(context)

def coefficients(beta):
    x = pi * beta
    inv_sinh2 = lambda y: 4 * math.exp(-2 * y) / (1 - math.exp(-2 * y))**2
    inv_cosh2 = lambda y: 4 * math.exp(-2 * y) / (1 + math.exp(-2 * y))**2
    a0 = pi*pi*beta/3 * (inv_sinh2(x)-inv_sinh2(2*x))
    a1 = pi*pi*beta/3 * (inv_cosh2(2*x)-inv_cosh2(x))
    b0 = 2*pi*pi*beta*beta/3 * math.tanh(x)
    b1 = 2*pi*pi*beta*beta/3 * (2*math.tanh(2*x)-math.tanh(x))
    return a0,a1,b0,b1

def analytic_ratio(beta):
    u = math.tanh(pi*beta)**2
    P = 17*u**4 + 4*u**3 + 6*u*u +4*u+1
    H = 2*u**3*(5-2*u+u*u)*(1+u)**2/((1-u)**2*(3+u)**2*P)
    return 64*beta*beta*H

def g(t,b):
    y=t/b
    return y/((y*y+1)*(y*y+4))

def direct_derivatives(beta,N):
    # Spatial derivative: absolutely convergent derivative of Zak sums.
    def dg(t):
        y=t/beta; y2=y*y
        return (4-5*y2-3*y2*y2)/(beta*(y2+1)**2*(y2+4)**2)
    a0=sum(dg(-m) for m in range(-N,N+1))
    a1=sum(dg(.5-m) for m in range(-N,N+1))
    # Frequency derivative: -i times b, and sum m*g is absolutely convergent.
    b0=-2*pi*sum(m*g(-m,beta) for m in range(-N,N+1))
    b1=-2*pi*sum(m*g(.5-m,beta) for m in range(-N,N+1))
    return a0,a1,b0,b1

# Validate exact derivative identity in rational arithmetic by polynomial evaluation.
def polys(u):
    P = 17*u**9 -51*u**8 +284*u**7 +348*u**6 +886*u**5 -50*u**4 +188*u**3+220*u*u+161*u+45
    Q = 17*u**4 + 4*u**3 +6*u*u +4*u + 1
    return P,Q

def Hfrac(u):
    _,q=polys(u)
    return 2*u**3*(u+1)**2*(u*u-2*u+5)/((u-1)**2*(u+3)**2*q)

def H_deriv_rational(u):
    p,q=polys(u)
    return -2*u*u*(u+1)*p/((u-1)**3*(u+3)**3*q*q)

# Rational central difference only checks an identity at sampled points; sign proof is algebraic.
for j in range(1,38):
    u=Fraction(j,40)
    d=Fraction(1,10**6)
    left=(Hfrac(u+d)-Hfrac(u-d))/(2*d)
    right=H_deriv_rational(u)
    check(abs(float(left-right)) < 1e-7*max(1.0,abs(float(right))),('H prime',j))
    check(right>0,('positive H derivative',j))

for beta in (.05,.10,.20,.30,.45,.60,.90,1.3):
    a0,a1,b0,b1=coefficients(beta)
    direct=direct_derivatives(beta,100000)
    for k,(v,w) in enumerate(zip((a0,a1,b0,b1),direct)):
        check(abs(v-w)< 5e-5*max(1,abs(v)),('direct Zak gradient',beta,k,v,w))
    check(a0>0 and a1<0 and b0>0 and b1>0,('gradient signs',beta))
    check(abs(analytic_ratio(beta)-(b0*b0+b1*b1)/(a0*a0+a1*a1))<1e-8*analytic_ratio(beta),('closed ratio',beta))

# Unique transition bracket and monotonicity sampled independently from the analytic proof.
lo,hi=.3003,.3004
check(analytic_ratio(lo)<1 and analytic_ratio(hi)>1,'crossover enclosure')
values=[analytic_ratio(.02+j*.01) for j in range(1,201)]
check(all(a<b for a,b in zip(values,values[1:])), 'ratio monotonic sample')

# Limiting powers, convergence at shrinking/growing b.
for beta in (.002,.003,.005):
    a0,a1,b0,b1=coefficients(beta)
    A=a0*a0+a1*a1; B=b0*b0+b1*b1
    check(abs(16*beta*beta*A-1)<2e-3,('small A',beta))
    check(abs(B/((40*pi**6/9)*beta**6)-1)<3e-3,('small B',beta))
for beta in (1.5,2.,2.5):
    a0,a1,b0,b1=coefficients(beta)
    A=a0*a0+a1*a1; B=b0*b0+b1*b1
    check(abs(A/((32*pi**4/9)*beta**2*math.exp(-4*pi*beta))-1)<.004,('large A',beta))
    check(abs(B/((8*pi**4/9)*beta**4)-1)<.004,('large B',beta))

print(f'PASS: {count} finite consistency checks. Universal assertions require the analytic proof.')
