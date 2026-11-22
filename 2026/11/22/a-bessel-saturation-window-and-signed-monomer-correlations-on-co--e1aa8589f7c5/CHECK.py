"""Reproduce finite exact counts and critical-window monomer correlations."""
import math
from fractions import Fraction
from itertools import combinations

CHECKS = 0

def verify(assertion, message):
    global CHECKS
    if not assertion:
        raise AssertionError(message)
    CHECKS += 1

def falling(n, j):
    v = 1
    for i in range(j): v *= (n-i)
    return v

def normalized(n, k, c):
    c = Fraction(c)
    a = [Fraction(falling(n,j), math.factorial(j)*math.factorial(k+j)) * (c/n)**j for j in range(n+1)]
    z = sum(a)
    return [v/z for v in a]

def matching_count(n, k, j):
    return math.comb(n,j)*math.comb(n+k,k+j)*math.factorial(n-j)

def enumerated_counts(n,k):
    # Distinct labeled matchings, independently built by recursing over left vertices.
    counts=[0]*(n+1)
    def rec(i,used,edges):
        if i==n:
            counts[n-edges]+=1
            return
        rec(i+1,used,edges)
        for r in range(n+k):
            if not ((used>>r)&1):rec(i+1,used|(1<<r),edges+1)
    rec(0,0,0)
    return counts

def limit(k,c,terms=160):
    c=float(c)
    a=[]
    v=1.0/math.factorial(k)
    for j in range(terms):
        a.append(v)
        v*=c/((j+1)*(j+k+1))
    z=sum(a)
    return [v/z for v in a]

for n in range(1,7):
    for k in range(4):
        for c in (Fraction(1,2), Fraction(1), Fraction(5,2), Fraction(6)):
            p=normalized(n,k,c)
            lam=Fraction(n,1)/c
            raw=[Fraction(matching_count(n,k,j))*lam**(n-j) for j in range(n+1)]
            zr=sum(raw)
            verify(all(p[j]==raw[j]/zr for j in range(n+1)), f'count {n,k,c}')
            mu=sum(Fraction(j)*p[j] for j in range(n+1))
            var=sum((j-mu)**2*p[j] for j in range(n+1))
            verify(var>0, f'var {n,k,c}')
            if n>=2:
                left=sum(Fraction(j*(j-1),n*(n-1))*p[j] for j in range(n+1))-(mu/n)**2
                verify(left<0, f'left {n,k,c}: {left}')
            if n+k>=2:
                right=sum(Fraction((j+k)*(j+k-1),(n+k)*(n+k-1))*p[j] for j in range(n+1))-((mu+k)/(n+k))**2
                verify(right<0, f'right {n,k,c}: {right}')
            cross=var/Fraction(n*(n+k))
            verify(cross>0, f'cross {n,k,c}')
            # Exact joint probabilities from two uniformly selected monomer subsets.
            verify(sum(Fraction(j*(j+k),n*(n+k))*p[j] for j in range(n+1)) - mu/Fraction(n) * (mu+k)/Fraction(n+k) == cross, 'cross exact')

for n in range(1,5):
    for k in range(3):
        verify(enumerated_counts(n,k)==[matching_count(n,k,j) for j in range(n+1)], f'direct matching enumeration {n,k}')

for n in (2,3,5,10,20,60,150):
    for k in range(4):
        for c in (0.3,1.0,3.5,8.0):
            p=[float(x) for x in normalized(n,k,Fraction(str(c)))]
            q=limit(k,c)
            tv=sum(abs((p[j] if j<=n else 0)-q[j]) for j in range(len(q)))/2
            factorial2=sum(j*(j-1)*q[j] for j in range(len(q)))
            bound=factorial2/(2*n)
            verify(tv<=bound+1e-13, f'TV: {n,k,c}, {tv} > {bound}')
            if n>=20:
                mu=sum(j*q[j] for j in range(len(q)))
                neg=sum(j*(j-1)*q[j] for j in range(len(q)))-mu**2
                verify(neg<0, 'asymptotic negative same-shore coefficient')

print('MONOMER_DIMER_EXACT_CHECKS_PASSED', CHECKS)
