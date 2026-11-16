#!/usr/bin/env python3
"""Finite consistency checks for a circular Fock interpolation theorem.

Uses only Python standard library; no finite check proves asymptotics.
"""
import cmath
import math

NTEST = 0

def near(a, b, atol=1e-8, rtol=1e-8):
    global NTEST
    NTEST += 1
    assert abs(a - b) <= atol + rtol * max(abs(a), abs(b)), (a, b)

def logweights(n, rho, kmax=30):
    return [k*n * math.log(rho*n) - math.lgamma(k*n+1) if k else 0.0
            for k in range(kmax + 1)]

def probabilities(n, rho, kmax=30):
    logs = logweights(n, rho, kmax)
    pivot = max(logs)
    weights = [math.exp(x-pivot) for x in logs]
    total = math.fsum(weights)
    return [x/total for x in weights]

def critical(k):
    return math.exp(-1+k*math.log(k)-(k-1)*math.log(k-1)) if k>1 else math.exp(-1)

# Exact product equality at each finite switching radius; monotonicity.
for n in (2, 3, 4, 8, 17, 35):
    thresholds=[]
    for k in range(1, 9):
        logtau=(math.lgamma(k*n+1)-math.lgamma((k-1)*n+1))/n-math.log(n)
        thresholds.append(math.exp(logtau))
        logs=logweights(n, math.exp(logtau), kmax=k+3)
        near(logs[k], logs[k-1], 1e-11)
        assert logs[k] >= max(logs[:k+2])-1e-10
        NTEST += 1
    assert all(a<b for a,b in zip(thresholds, thresholds[1:]))
    NTEST += 1

# Direct finite polynomial representation satisfies the N interpolation equations.
for n in (2, 3, 4, 5, 7):
    for rho in (0.12, 0.50, 1.17, 2.80):
        r=math.sqrt(rho*n)
        vals=[(rho*n)**(k*n)/math.factorial(k*n) for k in range(0, 17)]
        S=math.fsum(vals)
        for j in range(n):
            z=r*cmath.exp(2j*math.pi*j/n)
            numer=sum((r*z)**(k*n)/math.factorial(k*n) for k in range(17))
            near(numer/S, 1, 1e-9)
        norm=math.fsum((r**(k*n)/math.factorial(k*n)/S)**2*math.factorial(k*n) for k in range(17))
        near(norm,1/S,1e-9)

# Dominating indices away from thresholds.
for rho,k in ((0.2,0),(0.5,1),(1.8,2),(2.9,3),(4.8,5)):
    for n in (70,160,480):
        p=probabilities(n,rho)
        assert p.index(max(p))==k
        NTEST += 1

# Higher critical window, exact predicted logistic ratio: convergence for each fixed k and x.
for k in (2,3,4,6):
    t=critical(k)
    for x in (-1.3,0.0,0.7):
        a=math.exp((k-1)*x)/math.sqrt(k-1)
        b=math.exp(k*x)/math.sqrt(k)
        goal=b/(a+b)
        for n in (100,400,1200):
            p=probabilities(n,t*math.exp(x/n))
            near(p[k]/(p[k]+p[k-1]), goal, atol=0.015/n, rtol=0.3/n)
            assert p[k]+p[k-1]>0.98
            NTEST += 1

# The first crossover has a logarithmic rather than constant/N center.
for x in (-1.2,0.0,1.2):
    q=math.exp(x)/(1+math.exp(x))
    for n in (100,400,1200):
        rho=math.exp(-1+(math.log(2*math.pi*n)/2+x)/n)
        p=probabilities(n,rho)
        near(p[1],q,0.002,0.001)
        assert p[0]+p[1]>0.999
        NTEST += 1

print('PASS',NTEST,'finite checks')
