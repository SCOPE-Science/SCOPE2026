"""Numerical checks for exact alternating-grid Fourier-frame identities.

Run with Python 3 standard library: python CHECK.py.
All-integer statements are proved in RESULT.md; finite tests are supplementary.
"""
import cmath
import math
import random

checks = 0

def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def gram(n,delta,weights):
    angles=[2*math.pi*j/n+((1 if j%2==0 else -1)*delta) for j in range(n)]
    moments=[sum(weights[j]*cmath.exp(1j*d*angles[j]) for j in range(n)) for d in range(-n+1,n)]
    return [[moments[k-l+n-1] for l in range(n)] for k in range(n)]

def fnormerror(G):
    return sum(abs(G[i][j]-(1 if i==j else 0))**2 for i in range(len(G)) for j in range(len(G)))

def det(M):
    a=[row[:] for row in M]; n=len(a); z=1.+0j
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(a[i][k]))
        if abs(a[p][k])<1e-13:
            return 0j
        if p!=k:
            a[k],a[p]=a[p],a[k]; z=-z
        d=a[k][k]; z*=d
        for i in range(k+1,n):
            mul=a[i][k]/d
            for j in range(k+1,n):a[i][j]-=mul*a[k][j]
            a[i][k]=0j
    return z

rng=random.Random(20261115)
for n in range(2,34,2):
    for frac in [-.99,-.79,-.4,-.12,0,.2,.57,.89,.99]:
        delta=frac*math.pi/n
        s=abs(math.sin(n*delta/2)); c=math.cos(n*delta/2)
        G=gram(n,delta,[1/n]*n)
        check(abs(fnormerror(G)-n*s*s)<2e-10,('F',n,frac))
        # The exact minimal polynomial has both frame eigenvalues as its roots.
        check(max(abs(sum(G[i][k]*G[k][j] for k in range(n))
            -2*G[i][j]+(1-s*s)*(1 if i==j else 0))
            for i in range(n) for j in range(n))<2e-10,('poly',n,frac))
        if n<=12:
            check(abs(det(G)-c**n)<1e-8,('det',n,frac))
        t=1/(1+s*s)
        Gt=gram(n,delta,[t/n]*n)
        check(abs(fnormerror(Gt)-n*s*s/(1+s*s))<2e-10,('shrink',n,frac))
        if n<=20:
            for trial in range(4):
                raw=[.01+rng.random() for _ in range(n)]; T=sum(raw)
                W=[x/T for x in raw]
                Gw=gram(n,delta,W)
                check(fnormerror(Gw)+1e-9>=n*s*s,('global',n,frac,trial))
print('PASS: %d supplementary checks' % checks)
