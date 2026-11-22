"""Exact and numerical checks for classical RK4 on a three-state directed cycle.
Requires Python 3 and SymPy.  These finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp


def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def direct(a,b,c,h):
    q=[[-a,a,F(0)], [F(0),-b,b], [c,F(0),-c]]
    p=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    t=[[F(int(i==j)) for j in range(3)] for i in range(3)]
    for j in range(1,5):
        t=mm(t,q)
        t=[[x*h/j for x in row] for row in t]
        p=[[p[i][k]+t[i][k] for k in range(3)] for i in range(3)]
    return p


def reduced(a,b,c,h):
    S=a+b+c;T=a*b+b*c+c*a
    f=h-T*h**3/6+S*T*h**4/24
    g=h*h/2-S*h**3/6+(S*S-T)*h**4/24
    M,u,v=sorted((a,b,c),reverse=True)
    edge=f-(M+u)*g
    diag=1-M*f+M*M*g
    return f,g,edge,diag


def test_rationals():
    vals=[F(1,5), F(1,2), F(1), F(3,2), F(2), F(3)]
    steps=[F(0), F(1,10), F(1,2), F(1),F(7,5),F(2),F(13,5),F(4)]
    count=0
    for a,b,c in product(vals,repeat=3):
        for h in steps:
            d=direct(a,b,c,h)
            f,g,edge,diag=reduced(a,b,c,h)
            q=[[-a,a,F(0)],[F(0),-b,b],[c,F(0),-c]]
            q2=mm(q,q)
            approx=[[F(int(i==j))+f*q[i][j]+g*q2[i][j] for j in range(3)] for i in range(3)]
            assert d==approx, (a,b,c,h)
            assert all(sum(row)==1 for row in d)
            assert all(x>=0 for row in d for x in row)==(edge>=0 and diag>=0)
            if h>0:
                assert g>0
                assert d[0][2]>0 and d[1][0]>0 and d[2][1]>0
            count+=1
    return count


def test_symbolic():
    h,r=sp.symbols('h r',real=True)
    S=2+r;T=1+2*r
    f=h-T*h**3/6+S*T*h**4/24
    g=h**2/2-S*h**3/6+(S*S-T)*h**4/24
    E=sp.expand(24*(f-2*g)/h)
    D=sp.expand(24*(1-f+g))
    assert sp.simplify(E-(24-24*h+12*h*h-(4-r)*h**3))==0
    assert sp.simplify(D-(24-24*h+12*h*h+4*(r-1)*h**3+(1-3*r-r*r)*h**4))==0
    P=8*r**6+48*r**5+93*r**4-24*r**3-84*r**2+48*r-8
    assert sp.simplify(sp.resultant(E,D,h)+41472*P)==0
    z=sp.symbols('z',real=True)
    def bernstein(poly,n):
        f=sp.Poly(sp.expand(poly),z)
        a=[f.nth(j) for j in range(n+1)]
        return [sp.factor(sum(a[j]*sp.binomial(i,j)/sp.binomial(n,j) for j in range(i+1))) for i in range(n+1)]
    assert bernstein(P.subs(r,z/2),6)==[-8,-4,-sp.Rational(7,5),-sp.Rational(7,20),-sp.Rational(49,80),-sp.Rational(21,16),-sp.Rational(9,16)]
    assert bernstein(sp.diff(P,r).subs(r,(1+z)/2),5)==[9,sp.Rational(132,5),sp.Rational(1329,20),sp.Rational(1413,10),sp.Rational(1338,5),468]
    return E,D,P


def test_frontier(E,D,P):
    r,h=sp.symbols('r h',real=True)
    rp=sp.nroots(P,maxsteps=200)
    rr=[sp.re(z) for z in rp if abs(float(sp.im(z)))<1e-10 and 0<float(sp.re(z))<1]
    assert len(rr)==1
    star=float(rr[0])
    assert .54243757<star<.54243759
    cases=[F(1,20),F(1,4),F(2,5),F(1,2),F(3,4),F(1)]
    count=0
    for rv in cases:
        a,b,c=F(1),F(1),rv
        for hq in (F(1),F(3,2),F(7,4),F(2),F(5,2)):
            mat=direct(a,b,c,hq)
            ee=sp.Rational(1,24)*E.subs({r:sp.Rational(rv.numerator,rv.denominator),h:sp.Rational(hq.numerator,hq.denominator)})
            dd=sp.Rational(1,24)*D.subs({r:sp.Rational(rv.numerator,rv.denominator),h:sp.Rational(hq.numerator,hq.denominator)})
            assert (all(x>=0 for row in mat for x in row))==(ee>=0 and dd>=0)
            count+=1
    return star,count

if __name__=='__main__':
    count=test_rationals()
    E,D,P=test_symbolic()
    star,additional=test_frontier(E,D,P)
    print('ALL_CHECKS_PASSED',count,additional,'symbolic_resultant_and_rate_crossover')
    print('transition_rate',format(star,'.12f'))
