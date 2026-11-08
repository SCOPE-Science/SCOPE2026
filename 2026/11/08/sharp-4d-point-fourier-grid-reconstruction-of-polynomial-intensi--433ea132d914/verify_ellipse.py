#!/usr/bin/env python3
"""Exact arithmetic and finite Fourier checks of polynomial intensity sampling on ellipses.
Run with Python 3; no external packages required. These checks supplement the proof.
"""
from fractions import Fraction as F
import cmath, math, random

def mul(z,w):
    a,b=z;c,d=w;return (a*c-b*d,a*d+b*c)
def conj(z):return (z[0],-z[1])
def powers(z,n):
    arr=[(F(1),F(0))]
    for _ in range(n):arr.append(mul(arr[-1],z))
    return arr

def row(d,z):
    v=powers(z,d);r=[]
    for j in range(d+1):r.append(mul(v[j],conj(v[j]))[0])
    for j in range(d+1):
        for k in range(j+1,d+1):
            re,im=mul(v[j],conj(v[k]));r.extend((2*re,2*im))
    assert len(r)==(d+1)**2
    return r

def rational_rank(a):
    a=[r[:] for r in a];m=len(a);n=len(a[0]);i=0
    for j in range(n):
        pivot=next((k for k in range(i,m) if a[k][j]),None)
        if pivot is None:continue
        a[i],a[pivot]=a[pivot],a[i]
        v=a[i][j]
        a[i]=[t/v for t in a[i]]
        for k in range(i+1,m):
            if a[k][j]:
                v=a[k][j];a[k]=[a[k][h]-v*a[i][h] for h in range(n)]
        i+=1
        if i==m:break
    return i

def point(a,b,t):return (a*(1-t*t)/(1+t*t),2*b*t/(1+t*t))

def exact_tests():
    count=0
    for d in range(1,7):
        for a,b in ((F(2),F(1)),(F(3),F(2)),(F(1),F(1))):
            target=4*d if a!=b else 2*d+1
            ts=[F(k,2*d+3) for k in range(-2*d,2*d+1)]
            rank=rational_rank([row(d,point(a,b,t)) for t in ts])
            assert rank==target,(d,a,b,rank,target)
            count+=1
    for k in range(-15,16):
        x,y=point(F(2),F(1),F(k,17))
        assert x*x/F(4)+y*y==1
        count+=1
    return count

def numerical_rank(a,eps=1.e-7):
    a=[r[:] for r in a]; rows=len(a);cols=len(a[0]);i=0
    for j in range(cols):
        p=max(range(i,rows),key=lambda k:abs(a[k][j]),default=None)
        if p is None or abs(a[p][j])<eps: continue
        a[i],a[p]=a[p],a[i];v=a[i][j]
        a[i]=[z/v for z in a[i]]
        for k in range(i+1,rows):
            v=a[k][j]
            a[k]=[a[k][h]-v*a[i][h] for h in range(cols)]
        i+=1
        if i==rows:break
    return i

def fft_tests():
    rng=random.Random(2019)
    count=0
    for d in range(1,7):
        n=4*d;a,b=2.0,1.0
        coeff=[complex(rng.random()-.5,rng.random()-.5) for _ in range(d+1)]
        def signal(theta):
            z=complex(a*math.cos(theta),b*math.sin(theta))
            p=sum(c*z**j for j,c in enumerate(coeff))
            return abs(p)**2
        for offset in (0., .071/d,math.pi/(4*d)):
            thetas=[offset+2*math.pi*j/n for j in range(n)]
            sampled=[signal(t) for t in thetas]
            # The real profile space has no sine(2d theta) term.
            recovered={k:sum(sampled[j]*cmath.exp(-1j*k*thetas[j]) for j in range(n))/n for k in range(-2*d+1,2*d)}
            gamma=sum((-1)**j*sampled[j] for j in range(n))/n
            if abs(math.cos(2*d*offset))>1.e-8:
                gamma/=math.cos(2*d*offset)
                for x in (.137, .513, 1.313, 2.971):
                    val=sum(c*cmath.exp(1j*k*x) for k,c in recovered.items()).real+gamma*math.cos(2*d*x)
                    assert abs(val-signal(x))<1.e-7,(d,offset,x,val,signal(x))
                    count+=1
            # For deliberately singular shift the top cosine column vanishes.
            basis=[]
            for t in thetas:
                basis.append([1.]+[v for k in range(1,2*d) for v in (math.cos(k*t),math.sin(k*t))]+[math.cos(2*d*t)])
            expected=n-1 if abs(math.cos(2*d*offset))<1.e-8 else n
            r=numerical_rank(basis)
            assert r==expected,(d,offset,r,expected)
            count+=1
    return count
if __name__=='__main__':
    a=exact_tests();b=fft_tests()
    print('ELLIPSE_PHASE_INTENSITY_CHECK_PASS', 'exact_cases='+str(a), 'fourier_cases='+str(b))
