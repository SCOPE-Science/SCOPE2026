"""Checks exact cyclic homopolymer-2 spin correlations against enumeration."""
import math, cmath
from fractions import Fraction

def fib(n):
    if n == -1: return 1
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def luc(n): return fib(n-1)+fib(n+1)

def term(r,k):
    if r==0:return luc(k)
    if r==1:return -fib(k+1)
    return -fib(k-1)

def predicted(n,d):
    z=luc(n)+(2 if n%3==0 else -1)
    return Fraction(term(d%3,n-d)+term((n-d)%3,d),z)

def allowed(n):
    for b in range(1<<n):
        if all(not (((b>>i)&1)==((b>>((i+1)%n))&1)==((b>>((i+2)%n))&1)) for i in range(n)):
            yield b

def lam(n,k):
    return sum(float(predicted(n,d))*math.cos(2*math.pi*k*d/n) for d in range(n))

count=0
for n in range(3,18):
    words=list(allowed(n));z=luc(n)+(2 if n%3==0 else -1)
    assert len(words)==z,(n,len(words),z);count+=1
    for d in range(n):
        numer=sum((1 if (b&1) else -1)*(1 if (b>>d)&1 else -1) for b in words)
        assert Fraction(numer,z)==predicted(n,d), (n,d,numer,z,predicted(n,d));count+=1
    assert min(lam(n,k) for k in range(n)) > 1e-8 if n!=4 else abs(lam(n,0))<1e-8
    count+=1
for n in [20,40,80,150,250]:
    v=[lam(n,k) for k in range(n)]
    assert min(v)>0
    approx=[(2/math.sqrt(5))/(1+math.sqrt(5)*math.cos(2*math.pi*k/n)+2*math.cos(2*math.pi*k/n)**2) for k in range(n)]
    assert max(abs(x-y) for x,y in zip(v,approx)) < (2 if n==20 else (0.015 if n==40 else 2e-6)),(n,max(abs(x-y) for x,y in zip(v,approx)))
    count+=1
print('PASS',count,'assertions; n=4 nonconstant eigenvalues', [lam(4,k) for k in range(4)])
print('n=250 empirical kappa',max(v)/min(v),'exact limiting kappa',8+8*math.sqrt(5)/3)
