#!/usr/bin/env python3
"""Deterministic finite checks for a priced wheel spectral-gap allocation theorem.

Uses Python standard library only. The universal proof is in RESULT.md;
these checks do not certify its universal quantifiers or novelty.
"""
import math
import random


def eigensymmetric(A, tol=1.e-12):
    n=len(A)
    a=[row[:] for row in A]
    for it in range(50*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda t:abs(a[t[0]][t[1]]))
        if abs(a[p][q]) < tol:
            break
        tau=(a[q][q]-a[p][p])/(2*a[p][q]); t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau)); cs=1/math.sqrt(1+t*t); sn=t*cs
        app,aqq,apq=a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq; a[q][q]=aqq+t*apq; a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k==p or k==q:continue
            akp,akq=a[k][p],a[k][q]
            a[k][p]=a[p][k]=cs*akp-sn*akq
            a[k][q]=a[q][k]=sn*akp+cs*akq
    else:
        raise AssertionError('Jacobi solver did not converge')
    return sorted(a[k][k] for k in range(n))


def laplacian(spokes,rim):
    m=len(spokes)
    A=[[0.]*(m+1) for _ in range(m+1)]
    for i in range(m):
        for u,v,w in [(0,i+1,spokes[i]),(i+1,1+(i+1)%m,rim[i])]:
            A[u][u]+=w; A[v][v]+=w; A[u][v]-=w; A[v][u]-=w
    return A


def opt(m,c,B):
    k=4*math.sin(math.pi/m)**2
    if c<k:
        a=B*k/(m*(k+m*c)); b=B/(k+m*c)
    else:
        a=B/m; b=0.
    return [a]*m,[b]*m


def run():
    rng=random.Random(681699)
    checks=0
    for m in range(3,14):
        k=4*math.sin(math.pi/m)**2
        for cscale in (.08,.3,.9,1.,1.1,1.7,8.):
            c=k*cscale
            for B in (.5,1.,7.25):
                s,r=opt(m,c,B)
                assert abs(sum(s)+c*sum(r)-B)<1.e-10*max(1,B)
                ev=eigensymmetric(laplacian(s,r))
                expected=(m+1)*B*k/(m*(k+m*c)) if c<k else B/m
                assert abs(ev[0])<1.e-8
                assert abs(ev[1]-expected)<3.e-8*max(1,expected), (m,c,B,ev[1],expected)
                checks+=1
        # The complete segment at c=k is optimal; nonuniform rim/spokes are not assumed.
        B=3.14
        for frac in (0.,.17,.53,.95,1.):
            b=frac*B/(k*(m+1))
            a=B/m-k*b
            ev=eigensymmetric(laplacian([a]*m,[b]*m))
            assert abs(ev[1]-B/m)<1.e-8
            checks+=1
        # Test exact Rayleigh upper bounds independently on heterogeneous designs.
        for case in range(60):
            c=k*(.1+3*rng.random()); B=.1+4*rng.random()
            sw=[.1+rng.random() for i in range(m)]
            rw=[.1+rng.random() for i in range(m)]
            factor=B/(sum(sw)+c*sum(rw)); sw=[x*factor for x in sw];rw=[x*factor for x in rw]
            gap=eigensymmetric(laplacian(sw,rw))[1]
            S=sum(sw);R=sum(rw)
            assert gap <= (m+1)*S/m+3.e-9
            assert gap <= (S+k*R)/m+3.e-9
            checks+=1
        # Pointwise uniqueness forcing by first harmonic: if cos/sin eigenvectors,
        # the edge weights must be uniform. Perturbed designs have nonzero residual.
        for _ in range(30):
            a=[.5+rng.random() for i in range(m)];b=[.5+rng.random() for i in range(m)]
            z=[complex(math.cos(2*math.pi*j/m),math.sin(2*math.pi*j/m)) for j in range(m)]
            kcos=4*math.sin(math.pi/m)**2
            D=[a[j]+b[j]*(1-complex(math.cos(2*math.pi/m),math.sin(2*math.pi/m)))+b[j-1]*(1-complex(math.cos(2*math.pi/m),-math.sin(2*math.pi/m))) for j in range(m)]
            assert max(abs(d.imag) for d in D)>1.e-8
            checks+=1
    # exact special trigonometric values for short cycles
    for m,k in [(3,3),(4,2),(6,1)]:
        assert abs(4*math.sin(math.pi/m)**2-k)<2.e-14
        checks+=1
    print('VERIFY_OK', checks)

if __name__=='__main__':run()
