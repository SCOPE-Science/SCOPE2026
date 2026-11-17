#!/usr/bin/env python3
"""Exact checks for affine-denominator cubic-numerator generalized barycentric coordinates on trapezoids.
Scientific verification: polynomial identities, boundary reconstruction, and rational-grid inequalities.
"""
import sympy as S
from fractions import Fraction
x,y,a,b,A,B = S.symbols('x y a b A B', real=True)
k=a-b
L=a-k*y
q=S.expand((A+k*B)*L+b*B*x)
p1=S.expand((1-y)*(L-x)*(A+k*B+b*B*x/a))
p2=S.expand(x*(1-y)*(a*(A+k*B)+b*B*(x+k*y))/a)
p3=S.expand(x*y*(A+B*(x+k*y)))
p4=S.expand(y*(L-x)*(A+k*B+B*x))
assert S.simplify(sum((p1,p2,p3,p4))-q)==0
assert S.simplify(a*p2+b*p3-x*q)==0
assert S.simplify(p3+p4-y*q)==0
print('Exact symbolic normalization, x/y precision: PASS')
# Algebraic reconstruction from generic p3=xy(A+Bx+Cy), generic affine q=d0+d1*x+d2*y
C,d0,d1,d2=S.symbols('C d0 d1 d2')
qg=d0+d1*x+d2*y
p3g=x*y*(A+B*x+C*y)
# v3 on top edge y=1: p3=x q/b; on right edge x=L: p3=y q
bounds=[S.expand(b*p3g.subs(y,1)-x*qg.subs(y,1)),S.expand(p3g.subs(x,L)-y*qg.subs(x,L))]
eqs=[]
for expr in bounds:
    eqs+=S.Poly(expr,x,y).coeffs()
sol=S.solve(eqs,[d0,d1,d2,C],dict=True)
assert len(sol)==1,sol
assert S.simplify((d0+d1*x+d2*y).subs(sol[0])-q)==0,sol
assert S.simplify(sol[0][C]-k*B)==0
print('Generic 4-variable interpolation system -> unique two-parameter cone: PASS')
# Under rational parameters A>=0,A+(a+k)B>=0, all bracket factors have nonnegative minima
for aa,bb in ((2,1),(7,3),(13,9),(15,14)):
    kk=aa-bb
    ps=[S.factor(v.subs({a:aa,b:bb})) for v in (p1,p2,p3,p4)]
    qq=S.factor(q.subs({a:aa,b:bb}))
    choices=[(0,1),(1,0),(1,1),(aa+kk,-1),(aa+kk+1,-1),(0,3),(10,-1)]
    for u,v in choices:
        if u<0 or u+(aa+kk)*v<0 or (u==0 and v==0):
            continue
        for iy in range(17):
            yy=S.Rational(iy,16)
            maxx=S.Rational(aa)-(aa-bb)*yy
            for ix in range(17):
                xx=maxx*ix/16
                nums=[z.subs({A:u,B:v,x:xx,y:yy}) for z in ps]
                den=qq.subs({A:u,B:v,x:xx,y:yy})
                assert den>0,(aa,bb,u,v,ix,iy,'denominator')
                assert min(nums)>=0,(aa,bb,u,v,ix,iy,'numerator')
                assert S.simplify(sum(nums)-den)==0
    print('Rational-grid nonnegativity PASS:',aa,bb)
# Match published Example A.3 (a=2,b=1,A=0,B=2).
exps=[(2-x-y)*(1-y)*(2+x),x*(1-y)*(2+x+y),2*x*y*(x+y),2*y*(2-x-y)*(1+x)]
for got,expect in zip((p1,p2,p3,p4),exps):
    assert S.simplify(got.subs({a:2,b:1,A:0,B:2})-expect)==0
assert S.simplify(q.subs({a:2,b:1,A:0,B:2})-2*(2+x-y))==0
print('Published non-Wachspress source example exactly recovered: PASS')
# Distinct parameter rays are distinct rational coordinates on the polygon interior.
C,D=S.symbols('C D',real=True)
second_q=q.subs({A:C,B:D},simultaneous=True)
left=A+B*(x+k*y);right=C+D*(x+k*y)
assert S.simplify(left*second_q-right*q-k*(1-y)*(L-x)*(A*D-B*C))==0
print('Projective injectivity identity: PASS')
# Every admissible q is positive at all 4 polygon vertices. Its two decisive
# positive factors A+kB and A+aB follow from the cone inequalities.
assert S.simplify(q.subs({x:0,y:0})-a*(A+k*B))==0
assert S.simplify(q.subs({x:a,y:0})-a*(A+a*B))==0
assert S.simplify(q.subs({x:0,y:1})-b*(A+k*B))==0
assert S.simplify(q.subs({x:b,y:1})-b*(A+a*B))==0
print('Exact denominator vertex factors: PASS')
print('ALL EXACT CHECKS PASSED')
