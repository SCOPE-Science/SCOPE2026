"""Exact symbolic checks for fourth-order Runge--Kutta diffusion on paths and cycles.

Only scientific arithmetic is performed here. The all-size proof uses the
four-step walk-locality argument explained in RESULT.md; finite tests alone
would not establish the unbounded graph-size statements.
"""
from sympy import (Matrix, eye, zeros, symbols, Rational, factorial, Poly,
                   factor, simplify, discriminant, diff)

h=symbols('h')

def laplacian(kind,n):
    L=zeros(n)
    edges = [(i,i+1) for i in range(n-1)] if kind=='P' else [(i,(i+1)%n) for i in range(n)]
    for i,j in edges:
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    return L

def step(L):
    return sum(((-h)**k*L**k/factorial(k) for k in range(5)),zeros(L.rows))

# Exact endpoint transition factors, with transition = h*g(h).
qe = (6-9*h+9*h**2-7*h**3)/6
qn = (24-48*h+60*h**2-55*h**3)/24
qi = (6-12*h+15*h**2-14*h**3)/6
qp2 = (3-3*h+2*h**2-h**3)/3
qp3 = (8-12*h+12*h**2-9*h**3)/8
qp4 = (4-8*h+10*h**2-9*h**3)/4
qc4 = (3-6*h+8*h**2-8*h**3)/3

# All these cubics are strictly decreasing on the entire positive ray:
# derivatives have negative leading coefficient and negative discriminant.
for p in (qe,qn,qi,qp2,qp3,qp4,qc4):
    d=diff(p,h)
    assert Poly(d,h).LC()<0 and discriminant(d,h)<0, (p,d)
    assert p.subs(h,0)==1

# Every second-distance quadratic is positive on the real line.
q2s = [(13*h**2-16*h+12)/24,
       (5*h**2-5*h+3)/6,
       (7*h**2-6*h+3)/6,
       (7*h**2-6*h+3)/3,
       (29*h**2-24*h+12)/24]
for q in q2s:
    assert Poly(q,h).LC()>0 and discriminant(q,h)<0

p_factors={
    2:{1:{qp2}},
    3:{1:{qp3},2:{q2s[0]}},
    4:{1:{qe,qp4},2:{q2s[1]},3:{(4-6*h)/24}},
    5:{1:{qe,qn},2:{q2s[1],q2s[2]},3:{(4-7*h)/24},4:{Rational(1,24)}},
}
for n in range(6,13):
    p_factors[n]={1:{qe,qn,qi},2:{q2s[1],q2s[2]},
                  3:{(4-7*h)/24,(4-8*h)/24},4:{Rational(1,24)}}

c_factors={
    3:{1:{qp3}},
    4:{1:{qc4},2:{q2s[3]}},
    5:{1:{qn},2:{q2s[1]}},
    6:{1:{qi},2:{q2s[4]},3:{(4-8*h)/12}},
    7:{1:{qi},2:{q2s[2]},3:{(4-7*h)/24}},
    8:{1:{qi},2:{q2s[2]},3:{(4-8*h)/24},4:{Rational(1,12)}},
}
for n in range(9,15):
    c_factors[n]={1:{qi},2:{q2s[2]},3:{(4-8*h)/24},4:{Rational(1,24)}}

entries=0
for kind,families in [('P',p_factors),('C',c_factors)]:
    for n,classes in families.items():
        L=laplacian(kind,n);T=step(L)
        assert L==L.T
        assert T*Matrix([1]*n)==Matrix([1]*n)
        for i in range(n):
            for j in range(i+1,n):
                d=abs(i-j) if kind=='P' else min(abs(i-j),n-abs(i-j))
                v=simplify(T[i,j]/h**d)
                if d<=4:
                    assert any(simplify(v-z)==0 for z in classes[d]), (kind,n,i,j,d,v)
                else:
                    assert v==0
                entries+=1

# Correct lower-envelope thresholds and exact noncritical sign values.
assert [factor(p.subs(h,Rational(2,3))) for p in (qe,qp4)]==[Rational(26,81),Rational(1,9)]
assert [factor(p.subs(h,Rational(4,7))) for p in (qe,qn)]==[Rational(61,147),Rational(253,1029)]
assert [factor(p.subs(h,Rational(1,2))) for p in (qe,qn,qi)]==[Rational(23,48),Rational(65,192),Rational(1,3)]
assert qi.subs(h,Rational(4,7))==Rational(5,21)

# The four controlling cubic roots have exact rational isolating intervals.
root_polynomials={
    'P2': (qp2,Rational(1392646,10**6),Rational(1392647,10**6)),
    'P3/C3': (qp3,Rational(928431,10**6),Rational(928432,10**6)),
    'C4': (qc4,Rational(696323,10**6),Rational(696324,10**6)),
    'C5': (qn,Rational(720325,10**6),Rational(720326,10**6))
}
for name,(p,low,high) in root_polynomials.items():
    assert p.subs(h,low)>0 and p.subs(h,high)<0, (name,p.subs(h,low),p.subs(h,high))

# Any diagonal entry is strictly positive for h>0 because R_4(-x)>0
# for every real x>=0; exact sum-of-squares identity.
x=symbols('x')
R=sum((-x)**k/factorial(k) for k in range(5))
assert simplify(24*R-(x**2-2*x+2)**2-4*((x-2)**2+1))==0

# The general distance-three contribution on any simple path with degrees d_j
# is h^3*(4-h*sum_j d_j)/24, because a 4-walk differs from the sole
# geodesic by one diagonal stay; C7 adds a wrap-around length-4 route.
for n in range(4,12):
    L=laplacian('P',n);T=step(L)
    for i in range(n-3):
        degsum=sum(L[j,j] for j in range(i,i+4))
        assert simplify(T[i,i+3]-h**3*(4-h*degsum)/24)==0

print('VERIFY_OK',entries,'symbolic pair entries; all quadratic/derivative sign certificates; exact root intervals; all path distance-3 degree identities')
