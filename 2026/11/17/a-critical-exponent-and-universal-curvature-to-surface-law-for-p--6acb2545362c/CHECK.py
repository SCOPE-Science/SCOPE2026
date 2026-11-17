#!/usr/bin/env python3
"""Stdlib-only exact ridge-volume and asymptotic checks for lecture-hall simplices."""
from fractions import Fraction as Q
import math
import random


def det(a):
    n = len(a)
    if n == 0: return Q(1)
    b = [[Q(x) for x in row] for row in a]
    ans = Q(1)
    for k in range(n):
        i = next((i for i in range(k,n) if b[i][k]),None)
        if i is None: return Q(0)
        if i != k: b[k],b[i] = b[i],b[k]; ans = -ans
        pivot = b[k][k]; ans *= pivot
        for i in range(k+1,n):
            t = b[i][k]/pivot
            for j in range(k+1,n): b[i][j] -= t*b[k][j]
            b[i][k] = Q(0)
    return ans


def inverse(a):
    n=len(a)
    b=[[Q(a[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        m=next(i for i in range(k,n) if b[i][k])
        b[m],b[k]=b[k],b[m]
        v=b[k][k]
        b[k]=[x/v for x in b[k]]
        for i in range(n):
            if i==k:continue
            v=b[i][k]
            b[i]=[b[i][j]-v*b[k][j] for j in range(2*n)]
    return [row[n:] for row in b]


def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))


def curvature_bracket(s):
    a=[1.0/x for x in s]
    q=[a[0]]+[math.hypot(a[i-1],a[i]) for i in range(1,len(a))]+[a[-1]]
    total=math.pi/4*(sum(q)**2-sum(x*x for x in q))
    for i,ai in enumerate(a):
        qprod=q[i]*q[i+1]
        rho=min(1.,(ai*ai)/qprod)
        total += qprod*(math.sqrt(max(0.,1-rho*rho))*(math.pi/2+math.asin(rho))-math.pi/2)
    return total


def normalized_curvature(s):
    n=len(s)
    return n*(n-1)/(2*math.pi)*curvature_bracket(s)


def exact_checks():
    rng=random.Random(1251)
    profiles=0; ridges=0
    for n in range(2,7):
        for rep in range(12):
            s=[rng.randint(1,8) for i in range(n)]
            v=[[0]*n]+[[0]*(k-1)+s[k-1:] for k in range(1,n+1)]
            B=[[v[j+1][i] for j in range(n)] for i in range(n)]
            delta=det(B)
            assert delta==math.prod(s)
            inv=inverse(B)
            u=[[-sum((inv[k][j] for k in range(n)),Q(0)) for j in range(n)]]
            u += [row[:] for row in inv]
            # Chain order facets: z1, z2-z1,...,zn-z(n-1),1-zn.
            chain=u[1:]+u[:1]
            for i in range(n+1):
                for j in range(i+1,n+1):
                    expected=-Q(1,s[i]**2) if j==i+1 else Q(0)
                    assert dot(chain[i],chain[j])==expected
            for i in range(n+1):
                for j in range(i+1,n+1):
                    wedge2=dot(u[i],u[i])*dot(u[j],u[j])-dot(u[i],u[j])**2
                    remaining=[k for k in range(n+1) if k not in (i,j)]
                    E=[[v[k][t]-v[remaining[0]][t] for t in range(n)] for k in remaining[1:]]
                    gram=[[dot(a,b) for b in E] for a in E]
                    face2=det(gram)/math.factorial(n-2)**2
                    predicted=delta**2*wedge2/math.factorial(n-2)**2
                    assert face2==predicted,(n,s,i,j)
                    ridges+=1
            profiles+=1
    # independent known unit-leg orthoscheme intrinsic V_1 in R3 (Gao--Vitale).
    known=1+1/math.sqrt(2)+1/math.sqrt(3)
    assert abs(normalized_curvature([1,1,1])/6-known)<1e-12
    assert abs(normalized_curvature([1,1])/2-1.0)<1e-12
    print('EXACT_RIDGE_GRAM_PASS',f'profiles={profiles}',f'ridges={ridges}', 'known_orthoscheme_V1=PASS')


def asymptotic_checks():
    for p in (0,.5,1,2):
        out=[]
        for n in (100,1000,10000):
            s=[i**p for i in range(1,n+1)]
            C=normalized_curvature(s)
            surface=n*(1/s[0]+sum(math.hypot(1/s[i-1],1/s[i]) for i in range(1,n))+1/s[-1])
            if p<1: scale=n**(4-2*p)/(4*(1-p)**2)
            elif p==1: scale=n*n*math.log(n)**2/4
            else: scale=n*n
            out.append(f'{C/scale:.6f}/{C/surface**2:.6f}')
        print(f'POWER p={p}: at n=100,1000,10000 (scaled curvature / curvature-to-surface-squared)', ', '.join(out))

if __name__=='__main__':
    exact_checks()
    asymptotic_checks()
