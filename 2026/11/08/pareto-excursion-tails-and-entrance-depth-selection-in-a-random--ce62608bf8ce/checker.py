"""Standalone arithmetic checks for a Pareto-controlled random interval map.
Scientific object: T_b(x)=2x on [0,1/2], (x-1/2)**b on (1/2,1].
No external files or network needed.
"""
from fractions import Fraction
from math import log2, log, comb, factorial, exp

COUNT = 0

def checked(condition, info):
    global COUNT
    if not condition:
        raise AssertionError(info)
    COUNT += 1

def T(x, b):
    return 2*x if x <= Fraction(1,2) else (x-Fraction(1,2))**b

def first_return(y,b):
    x = y
    for k in range(1,100):
        x = T(x,b)
        if x > Fraction(1,2):
            return k
    raise ValueError('finite test outside horizon')

for b in range(1,7):
    for j in range(1,64):
        y=Fraction(1,2)+Fraction(j,128)
        W=Fraction(j,128)**b
        k=0
        while 2**k*W <= Fraction(1,2):
            k+=1
        observed=first_return(y,b)
        checked(observed==k+1,(b,j,observed,k+1))
        z=-log2(float(y-Fraction(1,2)))
        if abs(b*z-round(b*z))>1.e-9:
            checked(observed==1+int(b*z),(b,j,'log formula'))

# Under normalized Lebesgue measure on Y, Z=1+Exp(rate log 2).
a=log(2.)
def C(k):
    return sum(comb(k,j)*factorial(j)/a**j for j in range(k+1))
def analytic_tail(k,n):
    # E[Z^k * 1_{Z<n}] / n^k + Pr(Z>=n).
    # Equivalently n^-k(C_k - k int_n^infty z^(k-1) 2^(1-z) dz).
    J=exp(-a*n)*sum(factorial(k-1)//factorial(k-1-j)*n**(k-1-j)/a**(j+1) for j in range(k))
    return (C(k)-2*k*J)/n**k
for k in [1,2,3,4]:
    for n in [1,2,3,5,8,10,20,35]:
        p=analytic_tail(k,n)
        checked(0<p<=1+1e-12,(k,n,p))
        checked(p<=C(k)/n**k+1e-12,(k,n,'upper'))
        # Exact quadrature for Pareto mixing over the exponential logarithmic depth.
        N=40000
        integral=sum(min(1., ((1-log2((i+.5)/N))/n)**k) for i in range(N))/N
        checked(abs(p-integral)<0.00012,(k,n,p,integral))
        if n>=10:
            checked(abs(n**k*p-C(k))< 2*k*exp(-a*n)*sum(factorial(k-1)//factorial(k-1-j)*n**(k-1-j)/a**(j+1) for j in range(k))+1e-9,(k,n,'exp error'))

# Conditioning on a long excursion tilts logarithmic depth by Z^k.
for k in [1,2,3]:
    for n in [8,12,20,30]:
        # The direct quadrature checks the size-bias convergence without relying on numerator closed form.
        N=50000
        weights=[]
        vals=[]
        for i in range(N):
            z=1-log2((i+.5)/N)
            w=min(1.,(z/n)**k)
            weights.append(w)
            vals.append(w*z)
        mean=sum(vals)/sum(weights)
        if n>=20:
            checked(abs(mean-C(k+1)/C(k))<0.02,(k,n,mean,C(k+1)/C(k)))
print('PASS',COUNT,'standalone finite supporting checks')
