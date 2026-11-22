"""Supplementary numerical checks for one-node trigonometric quadrature formulas.
Run with Python 3 standard library: python check.py
"""
import cmath
import math


def dirichlet(n, x):
    m = (n - 1)//2
    return sum(cmath.exp(1j*k*x) for k in range(-m,m+1)).real


def weights(n, delta):
    h = 2*math.pi/n
    d0 = dirichlet(n, h*delta)
    w = [1/d0]
    w.extend((1-dirichlet(n,h*(delta-j))/d0)/n for j in range(1,n))
    return w


def spectral(n, delta):
    c = math.sin(math.pi*delta)/(n*math.sin(math.pi*delta/n))
    s = math.sqrt(max(0, 1-c*c))
    return 1-s, 1+s, c


def dot(u,v):
    return sum(a*b.conjugate() for a,b in zip(u,v))


count=0
for n in (3,5,7,9,11,17,31):
    m=(n-1)//2
    for delta in (0.02,0.15,0.3,0.499,0.5,0.501,0.7,0.92,0.99):
        w=weights(n,delta)
        assert abs(sum(w)-1)<1e-8
        count+=1
        for k in range(-m,m+1):
            q=sum(w[j]*cmath.exp(2j*math.pi*k*(delta if j==0 else j)/n) for j in range(n))
            assert abs(q-(1 if k==0 else 0)) < 2e-8
            count+=1
        for j in range(n):
            if delta < 0.5:
                assert w[j] > 0
            elif abs(delta-0.5)<1e-10:
                assert abs(w[1]) < 1e-8 if j==1 else w[j]>0
            elif j==1: assert w[j] < 0
            else: assert w[j] > 0
            count+=1
        lmin,lmax,c=spectral(n,delta)
        F=[[cmath.exp(2j*math.pi*k*(delta if j==0 else j)/n)/math.sqrt(n) for k in range(-m,m+1)] for j in range(n)]
        G=[[dot(F[i],F[j]) for j in range(n)] for i in range(n)]
        assert max(abs(G[i][j]-(1 if i==j else 0)) for i in range(1,n) for j in range(1,n))<2e-13
        u=[G[0][j] for j in range(1,n)]
        su=sum(abs(x)**2 for x in u)
        assert abs(su-(1-c*c))<2e-12
        assert abs(G[0][0]-1)<2e-12
        assert abs(lmin+lmax-2)<2e-12 and abs(lmin*lmax-c*c)<2e-12
        count+=4
        ratio=math.sin(math.pi*delta/n)/math.sin(math.pi*(1-delta)/n)
        amplification=1+2*max(0,ratio-1)/n
        assert abs(amplification-sum(abs(z) for z in w))<2e-8
        count+=1

for t in (0.7,1.3,4.0):
    for n in (51,101,501,1001):
        delta=1-t/n
        amp=sum(abs(a) for a in weights(n,delta))
        _,_,c=spectral(n,delta)
        kap=(1+math.sqrt(1-c*c))/c
        assert abs(amp-(1+2/t)) < 8/n
        assert abs(kap/n-2/t)<5/n
        count+=2
print(f'PASS {count} numerical assertions')
