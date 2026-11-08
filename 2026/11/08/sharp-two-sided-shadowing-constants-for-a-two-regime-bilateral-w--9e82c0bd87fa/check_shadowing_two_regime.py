#!/usr/bin/env python3
"""Finite diagnostic checks for the two-regime bilateral shift shadowing formulas.
All universal claims require the analytical argument in RESULT.md.
"""
import math
import random

def formula(a, b, p):
    if a == 1.0 or b == 1.0 or (a < 1 < b):
        return math.inf
    if a < 1 and b < 1:
        return 1.0/(1.0-max(a,b))
    if a > 1 and b > 1:
        return 1.0/(min(a,b)-1.0)
    x, y = 1.0/(a-1.0), 1.0/(1.0-b)
    return max(x,y) if math.isinf(p) else (x**p+y**p)**(1.0/p)

def correction(k,n,a,b,e):
    if n == 0: return 0.0
    if n > 0:
        return sum(b**j*e.get((k-1-j,n-j),0) for j in range(n))
    return -sum(a**(-j)*e.get((k+j-1,n+j),0) for j in range(1,-n+1))

def norm(z,p):
    if math.isinf(p): return max((abs(v) for v in z), default=0.0)
    return sum(abs(v)**p for v in z)**(1.0/p)

def main():
    rng=random.Random(10931)
    checks=0
    # The coordinatewise solution is checked against the full time-space recurrence.
    for a,b in [(1.2,.6),(2.5,.3),(4.1,.85)]:
        for run in range(10):
            e={(k,n):rng.uniform(-1,1) for k in range(-4,5) for n in range(-4,5)}
            for k in range(-6,7):
                for n in range(-7,8):
                    w=a if n<=0 else b
                    r=correction(k+1,n,a,b,e)-w*correction(k,n-1,a,b,e)-e.get((k,n),0)
                    assert abs(r)<4e-13,(a,b,k,n,r)
                    checks+=1
    # A discrete forcing realizing the two independent boundary loads.
    for a,b in [(1.5,.2),(2.3,.4),(4.0,.75)]:
        for m in [3,6,12,25,50]:
            e={(-1-j,m+1-j):1.0 for j in range(m)}
            e.update({(j-1,-m-1+j):-1.0 for j in range(1,m+1)})
            assert all(sum(abs(v) for (t,n),v in e.items() if t==time)<=1 for time in range(-m,m))
            pos=correction(0,m+1,a,b,e)
            neg=correction(0,-m-1,a,b,e)
            assert abs(pos-(1-b**m)/(1-b))<2e-12
            assert abs(neg-sum(a**(-j) for j in range(1,m+1)))<2e-12
            checks+=3
            for p in [1.0,2.0,3.0,math.inf]:
                assert norm([pos,neg],p)<=formula(a,b,p)+1e-10
                checks+=1
        for p in [1.0,2.0,3.0,math.inf]:
            e={(-1-j,200+1-j):1.0 for j in range(200)}
            e.update({(j-1,-201+j):-1.0 for j in range(1,201)})
            z=[correction(0,201,a,b,e),correction(0,-201,a,b,e)]
            assert abs(norm(z,p)-formula(a,b,p)) < 1e-9
            checks+=1
    # Boundary and orientation classification; these are diagnostic checks of the formula only.
    assert formula(.4,.5,2)==2.0;checks+=1
    assert formula(2,3,2)==1.0;checks+=1
    assert formula(.4,2,2)==math.inf;checks+=1
    assert formula(1,2,2)==math.inf;checks+=1
    assert formula(.5,1,2)==math.inf;checks+=1
    print('PASS:',checks,'finite diagnostic assertions; all infinite claims require proof')
if __name__=='__main__':main()
