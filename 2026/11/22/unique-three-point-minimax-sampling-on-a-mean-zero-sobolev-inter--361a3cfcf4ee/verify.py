#!/usr/bin/env python3
"""Exact algebraic and rational spot-checks for a three-point Neumann Sobolev trace design.

Requires Python 3 and SymPy. Finite checks corroborate, but do not replace,
the all-node proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import sqrt
import sympy as s

a,L,M,d=s.symbols('a L M d',real=True)
x=[s.Rational(1,2)+M-L/2,s.Rational(1,2)+M+d,s.Rational(1,2)+M+L/2]
G=s.Matrix([[s.Rational(1,3)+(x[i]**2+x[j]**2)/2-x[max(i,j)] for j in range(3)] for i in range(3)])
u=s.Matrix([1/s.sqrt(2),0,1/s.sqrt(2)])
v=s.Matrix([0,1,0])
z=s.Matrix([1/s.sqrt(2),0,-1/s.sqrt(2)])
A=(u.T*G*u)[0]; B=(u.T*G*v)[0]; D=(v.T*G*v)[0]
A0=L**2/2-L/2+s.Rational(1,6)
B0=(L**2/4-L/2+s.Rational(1,6))/s.sqrt(2)
assert s.simplify(A-A0-2*M**2)==0
assert s.simplify(B-B0-(M**2+(M+d)**2)/s.sqrt(2))==0
assert s.simplify(D-s.Rational(1,12)-(M+d)**2)==0
assert s.simplify((z.T*G*z)[0]-L/2)==0
H=s.Matrix([[A0.subs(L,2*a), B0.subs(L,2*a)],[B0.subs(L,2*a),s.Rational(1,12)]])
p=3*a**3+6*a**2-9*a+1
assert s.factor((H-a*s.eye(2)).det()+a*p/6)==0
assert p.subs(a,s.Rational(1,9))>0 and p.subs(a,s.Rational(1,8))<0
assert s.diff(p,a).subs(a,0)<0 and s.diff(p,a).subs(a,s.Rational(1,6))<0

def green(xx,yy):
    return Q(1,3)+(xx**2+yy**2)/2-max(xx,yy)
def integral_kernel(xx,yy):
    cuts=sorted(set([Q(0),xx,yy,Q(1)]))
    result=Q(0)
    for l,r in zip(cuts,cuts[1:]):
        m=(l+r)/2
        sx=int(m>=xx);sy=int(m>=yy)
        result+=(r**3-l**3)/3 - (sx+sy)*(r**2-l**2)/2 + sx*sy*(r-l)
    return result

count=0
points=[Q(i,24) for i in range(25)]
for xx in points:
    for yy in points:
        assert integral_kernel(xx,yy)==green(xx,yy)
        count+=1

for x1,x2,x3 in combinations_with_replacement([Q(i,12) for i in range(13)],3):
    L0=x3-x1; M0=(x1+x3-Q(1))/2; d0=x2-(x1+x3)/2
    g=[[green(xx,yy) for yy in (x1,x2,x3)] for xx in (x1,x2,x3)]
    # Derive three independent quadratic compression identities from the kernel.
    Au=(g[0][0]+2*g[0][2]+g[2][2])/2
    assert Au == L0*L0/2-L0/2+Q(1,6)+2*M0*M0
    Dv=g[1][1]
    assert Dv == Q(1,12)+(M0+d0)**2
    assert g[0][0]+g[2][2]-2*g[0][2] == L0
    count+=3

lo,hi=1/9,1/8
for _ in range(80):
    mid=(lo+hi)/2
    if 3*mid**3+6*mid**2-9*mid+1>0:lo=mid
    else:hi=mid
r=(lo+hi)/2
assert abs(3*r**3+6*r**2-9*r+1)<1e-14
minor=2*r*r-2*r+1/4
assert 0<minor<r
print('exact rational/algebraic checks:',count+9)
print('unique positive design parameter a ~ %.15f'%r)
print('squared evaluation norm ~ %.15f'%r)
print('evaluation norm ~ %.15f'%sqrt(r))
print('Gram spectrum ~',minor,r,r)
