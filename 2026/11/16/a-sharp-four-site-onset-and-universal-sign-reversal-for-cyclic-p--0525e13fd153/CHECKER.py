#!/usr/bin/env python3
"""Independent finite checks for periodic Poisson covariance identities.

Analytic proofs in RESULT.md cover arbitrary sample counts and all parameters.
Uses only Python standard library.
"""
import math

checks = 0

def eq(a, b, tol=2e-8):
    global checks
    checks += 1
    if not abs(a-b) <= tol * max(1.0, abs(a), abs(b)):
        raise AssertionError((a,b))

def kernel(n, r, d):
    th = 2 * math.pi * (d % n) / n
    return (1-r*r) / (1 - 2*r*math.cos(th) + r*r)

def eig(n,r,j):
    return n*(r**j + r**(n-j))/(1-r**n)

def qf(n,r,d):
    return sum(math.cos(2*math.pi*j*d/n)/eig(n,r,j) for j in range(n))/n

def inverse(a):
    n=len(a)
    z=[list(map(float,a[i])) + [float(i==j) for j in range(n)] for i in range(n)]
    for i in range(n):
        k=max(range(i,n),key=lambda k:abs(z[k][i]))
        z[i],z[k]=z[k],z[i]
        pivot=z[i][i]
        assert abs(pivot)>1e-13
        z[i]=[x/pivot for x in z[i]]
        for j in range(n):
            if j==i: continue
            f=z[j][i]
            z[j]=[z[j][p]-f*z[i][p] for p in range(2*n)]
    return [x[n:] for x in z]

def root4():
    u=1+math.sqrt(5)
    return (u-math.sqrt(u*u-4))/2

def root5():
    a=3+math.sqrt(5)
    u=(a+math.sqrt(a*a+16))/4
    return (u-math.sqrt(u*u-4))/2

for n in range(2,13):
    for r in [0.19,0.43,0.77,0.91]:
        cov=[[kernel(n,r,i-j) for j in range(n)] for i in range(n)]
        mat=inverse(cov)
        for d in range(n):
            eq(qf(n,r,d),mat[0][d])
        for j in range(n):
            for k in range(n):
                eq(sum(cov[j][l]*mat[l][k] for l in range(n)),float(j==k))

# Completely separate exact expressions for the quadrilateral.
for r in [0.09,0.28,root4(),0.50,0.84]:
    q1=(r-1)**3*(1+r)**3*(1+r*r)/(32*r*r*(1+r**4))
    q2=(1-r)**3*(1+r)*(r**4-2*r**3-2*r*r-2*r+1)/(32*r*r*(1+r**4))
    eq(qf(4,r,1),q1)
    eq(qf(4,r,2),q2)
    checks+=1
    assert q1<0
    checks+=1
    if abs(r-root4())<1e-12: assert abs(q2)<1e-10
    else: assert (q2>0)==(r<root4())

# Fifth-root-of-unity factorization, independently of direct inverse.
s5=math.sqrt(5)
for r in [0.09,0.26,root5(),0.51,0.8]:
    A=(1+r**5)*(r+r**4)*(r*r+r**3)
    h1=r**4 - (3-s5)/2*r**3 + r*r - (3-s5)/2*r + 1
    h2=r**4 - (3+s5)/2*r**3 + r*r - (3+s5)/2*r + 1
    v1=(1-r**5)/25/A*(-1-s5)/2 *r*(r-1)**2*(r+1)**2*h1
    v2=(1-r**5)/25/A*(-1+s5)/2 *r*(r-1)**2*(r+1)**2*h2
    eq(qf(5,r,1),v1)
    eq(qf(5,r,2),v2)
    checks+=1
    assert v1<0
    checks+=1
    if abs(r-root5())<1e-12: assert abs(v2)<1e-10
    else: assert (v2>0)==(r<root5())

# Boundary profiles of every cyclic distance, including the parity effect.
for n in range(4,18):
    h=n//2
    r=0.1
    for d in range(1,h+1):
        v=qf(n,r,d)
        expected=(((-1)**d)/(2*n*n) if n%2==0 else 2*((-1)**d)*math.cos(math.pi*d/n)/(n*n))*r**(-h)
        # In finite r, lower aliases contribute corrections, tending to zero.
        eq(v/expected,1,0.6)
    r=0.999
    for d in range(1,h+1):
        v=qf(n,r,d)
        lead=-(1-r)**3/(4*(1-math.cos(2*math.pi*d/n)))
        eq(v/lead,1,0.10)

print('PASS:',checks,'finite independently reconstructed checks; analytic generality in RESULT.md')
