#!/usr/bin/env python3
"""Independent weighted matching-enumerator checks and spectral-gap sampling."""
from functools import lru_cache
from math import cos,pi,sin,sqrt
import sympy as s
x=s.symbols('x')

def poly_enumerate(m,a,b):
    n=2*m; N=2*n
    edges=[]
    for j in range(n):
        edges.append((j,(j+1)%n,s.Rational(1)))
        edges.append((j,n+j,s.Rational(a if j%2==0 else b)))
    adj=[[] for _ in range(N)]
    for u,v,w in edges:
        adj[u].append((v,w));adj[v].append((u,w))
    @lru_cache(None)
    def go(mask):
        if mask==0:return s.Integer(1)
        bit=mask & -mask;v=bit.bit_length()-1
        rest=mask^bit
        ans=x*go(rest)
        for w,z in adj[v]:
            if rest>>w&1:ans-=z*go(rest^(1<<w))
        return s.expand(ans)
    return s.Poly(go((1<<N)-1),x)

def poly_transfer(m,a,b):
    a=s.Rational(a);b=s.Rational(b)
    y=x*x-(a+b+2)+a*b/x**2
    return s.Poly(s.cancel(2*x**(2*m)*s.chebyshevt(m,y/2)),x)

def near_gap(m,a,b):
    th=pi/(2*m)
    A=a+b+2*(1-cos(th))
    lo=(A-sqrt(A*A-4*a*b))/2;hi=(A+sqrt(A*A-4*a*b))/2
    g=sqrt(hi)-sqrt(lo)
    rhs=sqrt((sqrt(a)-sqrt(b))**2+4*sin(pi/(4*m))**2)
    assert abs(g-rhs)<1e-10,(m,a,b,g,rhs)
    return g

def main():
    checks=0
    for m in range(2,5):
        for a,b in [(1,1),(1,4),(2,3),(s.Rational(1,2),s.Rational(5,3))]:
            p=poly_enumerate(m,a,b)
            q=poly_transfer(m,a,b)
            assert p==q,(m,a,b,p.as_expr()-q.as_expr())
            assert p.degree()==4*m
            checks+=1
            near_gap(m,float(a),float(b));checks+=1
    for m in [2,3]:
        n=2*m;N=2*n
        H=s.zeros(N)
        for j in range(n):
            k=(j+1)%n
            if j==n-1:
                H[j,k]=s.I;H[k,j]=-s.I
            else:
                H[j,k]=H[k,j]=1
            H[j,n+j]=H[n+j,j]=1 if j%2==0 else 2
        mag=s.Poly(s.expand((x*s.eye(N)-H).det()),x)
        assert mag==poly_enumerate(m,1,4)
        checks+=1
    print('PASS weighted matching, transfer and magnetic determinant:',checks,'checks')
    for m in [2,3,5,10,25,50]:
        print('m=',m,'a=b=1, gap=',near_gap(m,1,1),'a=1,b=4 gap=',near_gap(m,1,4))
if __name__=='__main__':main()
