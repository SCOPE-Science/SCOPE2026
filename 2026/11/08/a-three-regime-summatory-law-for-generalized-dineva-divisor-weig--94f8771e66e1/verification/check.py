"""Standalone finite arithmetic checks for the mean-value phase transition.
Only finite checks; analytic theorems are proved in RESULT.md.
"""
from fractions import Fraction
from math import log

def prime_divisors(n):
    ds=[]; x=n; p=2
    while p*p<=x:
        if x%p==0:
            ds.append(p)
            while x%p==0:x//=p
        p+=1
    if x>1:ds.append(x)
    return ds

def phi(n):
    v=n
    for p in prime_divisors(n):v=v//p*(p-1)
    return v

def is_squarefree(n):
    return all(n%(p*p)!=0 for p in prime_divisors(n))

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def a(n,t):
    if not is_squarefree(n):return Fraction(0)
    return Fraction(n**t,phi(n))

def weighted_sum(n,t):
    return sum((a(d,t) for d in divisors(n)),Fraction(0))

def product_form(n,t):
    out=Fraction(1)
    for p in prime_divisors(n):out *= 1+Fraction(p**t,p-1)
    return out

def h(n):
    # h at p^e: 1, 1/(p-1), -p/(p-1), and zero at e>=3.
    z=Fraction(1);x=n;p=2
    while p*p<=x:
        if x%p==0:
            e=0
            while x%p==0:x//=p;e+=1
            if e>=3:return Fraction(0)
            z*= Fraction(1,p-1) if e==1 else Fraction(-p,p-1)
        p+=1
    if x>1:z*=Fraction(1,x-1)
    return z

for t in [0,1,2]:
    for n in range(1,121):
        left=weighted_sum(n,t)
        assert left==product_form(n,t),(n,t,'Euler product')
        if t==1:
            v=sum((h(d) for d in divisors(n)),Fraction())
            assert a(n,1)==v,(n,'convolution')
    print(f'EXACT_DIVISOR_EULER_IDENTITIES_OK t={t} n=1..120')
print('CRITICAL_CONVOLUTION_IDENTITY_OK n=1..120')

# Efficient arithmetic sieve, evaluating the full finite double divisor sum.
N=60000
phi_values=list(range(N+1)); sqfree=[True]*(N+1)
for p in range(2,N+1):
    if phi_values[p]==p:
        for n in range(p,N+1,p):phi_values[n]-=phi_values[n]//p
        if p*p<=N:
            for n in range(p*p,N+1,p*p):sqfree[n]=False

def S(x,t):
    arr=[1.0]*(x+1)
    for d in range(2,x+1):
        if sqfree[d]:
            weight=(d**t)/phi_values[d]
            for n in range(d,x+1,d):arr[n]+=weight
    return sum(arr[1:])

for t in [0.0,0.5,1.0,1.5,2.0]:
    samples=[]
    for x in [2000,10000,60000]:
        v=S(x,t)
        den=x if t<1 else x*log(x) if t==1 else x**t
        samples.append(f'{v/den:.6f}')
    print(f'SUMMATORY_SCALED t={t:.1f}: '+', '.join(samples)+' at x=2000,10000,60000')
print('FINITE_CHECKS_ONLY_TRUE; INFINITE_PROOF_SEPARATE_TRUE; INDEPENDENT_AUDIT_FALSE')
