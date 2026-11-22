"""Finite numerical consistency checks; the universal argument is in RESULT.md.
No finite test is an infinite-dimensional proof.
"""
from itertools import product
from math import sqrt, factorial
from fractions import Fraction
import random

def det(a):
    # exact Gaussian elimination for rational input
    m=[list(map(Fraction,row)) for row in a]; d=len(m);sgn=1;prod=Fraction(1)
    for k in range(d):
        i=next((i for i in range(k,d) if m[i][k]),None)
        if i is None:return Fraction(0)
        if i!=k:m[k],m[i]=m[i],m[k];sgn=-sgn
        piv=m[k][k];prod*=piv
        for i in range(k+1,d):
            r=m[i][k]/piv
            for j in range(k,d):m[i][j]-=r*m[k][j]
    return sgn*prod

def norm_facets(vertices):
    n=len(vertices)-1; areas=[]
    for omit in range(n+1):
        face=[vertices[j] for j in range(n+1) if j!=omit]
        edges=[[face[j][k]-face[0][k] for k in range(n)] for j in range(1,n)]
        gram=[[sum(a*b for a,b in zip(edges[i],edges[j])) for j in range(n-1)] for i in range(n-1)]
        areas.append(sqrt(float(det(gram)))/factorial(n-1))
    return [v/sum(areas) for v in areas]

def trial(vertices):
    n=len(vertices)-1; a=1/(n+1);w=norm_facets(vertices)
    tv=sum(max(0,x-a) for x in w)/n
    extr=max(abs(sum((a-w[i])*t[i] for i in range(n+1)))/n for t in product([0,1],repeat=n+1))
    assert abs(tv-extr)<1e-11
    assert max(w)<.5+1e-11
    assert tv<(n-1)/(n*(n+1))+1e-10
    intcent=[sum(v[j] for v in vertices)/(n+1) for j in range(n)]
    bdcent=[sum(w[i]*sum(vertices[k][j] for k in range(n+1) if k!=i)/n for i in range(n+1)) for j in range(n)]
    assert max(abs(bdcent[j]-intcent[j]-sum((a-w[i])*vertices[i][j] for i in range(n+1))/n) for j in range(n))<1e-11
    return tv

rng=random.Random(20261116);count=0
for n in range(2,7):
    for k in range(12):
        while True:
            verts=[[rng.randrange(-3,4) for _ in range(n)] for _ in range(n+1)]
            mat=[[verts[j][i]-verts[0][i] for i in range(n)] for j in range(1,n+1)]
            if det(mat)!=0: break
        trial(verts);count+=1
for n in range(2,12):
    for eps in (.1,.01,.001):
        verts=[[0]*n]+[[int(i==j) for i in range(n)] for j in range(n-1)]+[[0]*(n-1)+[eps]]
        w=norm_facets(verts)
        W=sqrt(1+(n-1)*eps*eps)+1+(n-1)*eps
        expected=[sqrt(1+(n-1)*eps*eps)/W]+[eps/W]*(n-1)+[1/W]
        assert max(abs(x-y) for x,y in zip(w,expected))<1e-11
        gap=sum((1/(n+1)-w[j]) for j in range(1,n))/n
        assert 0<gap<(n-1)/(n*(n+1))
        count+=1
print('PASS:',count,'finite consistency cases; universal theorem relies on proof')
