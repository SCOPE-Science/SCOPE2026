"""Exact checks for mixed-update fixation on double-star trees.
Requires Python 3 and SymPy; no network or source files.
"""
from fractions import Fraction
from itertools import product
from math import isclose
import sympy as S
x,m,t=S.symbols('x m t', real=True)

def graph(a,b):
    # centers 0 and 1; pendant vertices 2..a+1 to 0; remaining to 1
    n=a+b+2
    edges=[(0,1)]+[(0,i) for i in range(2,2+a)]+[(1,i) for i in range(2+a,n)]
    return n,edges

def weights(a,b,x):
    p=S.sympify(a+1); q=S.sympify(b+1)
    r=lambda k: ((1-x)+x*k)/(k*(1-x)+x)
    h=((1-x)*p+x*q)/((1-x)*q+x*p)
    z=[S.Integer(1),r(p),S.cancel(r(p)*h),S.cancel(r(p)*h/r(q))]
    Z=S.cancel(a*z[0]+z[1]+z[2]+b*z[3]);return [S.cancel(c/Z) for c in z]

def dual_check(a,b,value):
    n,edges=graph(a,b); D=[0]*n
    for i,j in edges:D[i]+=1;D[j]+=1
    w=weights(a,b,value)
    p=[w[1],w[2]]+[w[0]]*a+[w[3]]*b
    assert S.simplify(sum(p)-1)==0
    neighbors={i:[] for i in range(n)}
    for i,j in edges:neighbors[i].append(j);neighbors[j].append(i)
    # Independently construct linear equations for the dual genealogy.
    for v in range(n):
        lhs=S.S(0)
        for u in neighbors[v]:
            quv=((1-value)/D[u]+value/D[v])/n
            qvu=((1-value)/D[v]+value/D[u])/n
            lhs+=p[v]*quv-p[u]*qvu
        assert S.simplify(lhs)==0,(a,b,value,v,lhs)
    # Martingale drift for every nonabsorbed type configuration.
    for mask in range(1,(1<<n)-1):
        drift=S.S(0)
        for u in range(n):
            for v in neighbors[u]:
                if ((mask>>u)&1)!=((mask>>v)&1):
                    drift+=(p[v] if ((mask>>u)&1) else -p[v])*(((1-value)/D[u]+value/D[v])/n)
        assert S.simplify(drift)==0,(a,b,value,mask,drift)
    return (1<<n)-2+n

def main():
    checks=0
    for a,b in [(1,2),(1,3),(1,4),(2,3)]:
        for value in (S.S(0),S.Rational(1,30),S.Rational(1,2),S.S(1)):
            checks+=dual_check(a,b,value)
    # Tiny-tree minimality: all 5-vertex types other than the fork are bidegreed.
    # The fork is the double-star (1,2); check four complete derivative signs.
    signs=[-1,1,1,-1]
    expected=[[-336,-1188,-1327,-478,-31],
              [192,792,1048,520,88],
              [1008,2388,2017,730,97],
              [-432,-996,-869,-386,-77]]
    for i,prob in enumerate(weights(1,2,x)):
        N=S.fraction(S.factor(S.diff(prob,x)))[0]
        P=S.Poly(S.cancel(N.subs(x,t/(1+t))*(1+t)**4),t)
        assert P.all_coeffs()==expected[i]
        assert all(signs[i]*int(c)>0 for c in P.all_coeffs())
        checks+=6
    # Six-vertex witness identity, unique cubic root, derivative endpoints.
    p6=S.factor(weights(1,3,x)[0]);
    expected_p=(2-x)**2*(3*x+1)/(19+35*x-8*x*x-6*x**3)
    assert S.simplify(p6-expected_p)==0;checks+=1
    d6=S.factor(S.diff(p6,x));f=15*x**3-21*x**2-29*x+1
    assert S.simplify(d6-6*(2-x)*f/(19+35*x-8*x*x-6*x**3)**2)==0;checks+=1
    assert S.simplify(S.diff(f,x)-(45*x*x-42*x-29))==0; checks+=1
    assert f.subs(x,0)>0 and f.subs(x,1)<0; checks+=2
    root=float([S.re(r) for r in S.nroots(f) if abs(float(S.im(r)))<1e-10 and 0<float(S.re(r))<1][0]);
    assert abs(root-0.0336810499232197)<1e-12; checks+=1
    assert abs(float(p6.subs(x,root))-0.2110651074585313)<1e-11;checks+=1
    # Infinite witness family for every m>=3.
    m=S.symbols('m',positive=True)
    p=weights(1,m,x)[0]
    assert S.simplify(S.diff(p,x).subs(x,0)-(2*m**4-7*m**2-16*m-3)/(2*m**2+5*m+5)**2)==0;checks+=1
    assert S.simplify(S.diff(p,x).subs(x,1)+(7*m*m+11*m+6)/(8*(m+1)*(m+2)**2))==0;checks+=1
    assert S.simplify(p.subs(x,0)-2*(m+1)/(2*m*m+5*m+5))==0;checks+=1
    assert S.simplify(p.subs(x,1)-1/(2*(m+2)))==0;checks+=1
    y=S.symbols('y',positive=True)
    expr=S.cancel((m*p).subs({x:1/y,m:y*y},simultaneous=True))
    assert S.limit(expr,y,S.oo)==2; checks+=1
    assert S.limit((m*p).subs(x,0),m,S.oo)==1;checks+=1
    assert S.limit((m*p).subs(x,1),m,S.oo)==S.Rational(1,2);checks+=1
    print('PASS',checks,'exact one-step identities and symbolic checks')
if __name__=='__main__':main()
