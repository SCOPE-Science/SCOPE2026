#!/usr/bin/env python3
"""Exact algebraic verification for the degree-four circle L4 point-evaluation invariant.
Requires Python 3 and SymPy. Run: python3 checker.py
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
coeff = [x, y, 1-2*x-2*y, y, x]
conv = [sum(coeff[j]*coeff[k-j] for j in range(5) if 0 <= k-j <= 4) for k in range(9)]
Q = sp.expand(sum(v*v for v in conv))
Q_expected = (70*x**4+160*x**3*y-80*x**3+168*x*x*y*y-144*x*x*y
              +36*x*x+112*x*y**3-120*x*y*y+48*x*y-8*x
              +70*y**4-80*y**3+36*y*y-8*y+1)
assert sp.expand(Q-Q_expected)==0
f=35*x**3+60*x*x*y-30*x*x+42*x*y*y-36*x*y+9*x+14*y**3-15*y*y+6*y-1
g=20*x**3+42*x*x*y-18*x*x+42*x*y*y-30*x*y+6*x+35*y**3-30*y*y+9*y-1
assert sp.expand(sp.diff(Q,x)-8*f)==0
assert sp.expand(sp.diff(Q,y)-8*g)==0
R=(1486485*x**9-2058210*x**8+1342737*x**7-545445*x**6
   +152559*x**5-30600*x**4+4435*x**3-453*x*x+30*x-1)
assert sp.expand(sp.resultant(f,g,y)+189*R)==0
sub=sp.subresultants(f,g,y)
A=12474*x**4-6405*x**3+1242*x*x-91*x+2
B=13860*x**5-13146*x**4+4770*x**3-868*x*x+78*x-3
assert sp.expand(sub[-2]-63*(A*y+B))==0
assert sp.Poly(R,x).count_roots(-sp.oo,sp.oo)==1
lo,hi=sp.Rational(271251647973,10**12),sp.Rational(271251647974,10**12)
assert R.subs(x,lo)<0<R.subs(x,hi)
assert sp.Poly(R,x).count_roots(lo,hi)==1
assert sp.Poly(A,x).count_roots(lo,hi)==0
assert A.subs(x,lo)>0
# Exact resultant and subresultant identities also guarantee that the
# real R-root and its rationally recovered y solve BOTH stationarity equations.
for h in [f,g]:
    degree=sp.degree(h,y)
    numerator=sp.Poly(sp.cancel(A**degree*h.subs(y,-B/A)),x)
    assert sp.rem(numerator,sp.Poly(R,x)).is_zero
# Three supporting hyperplanes form a rational convexity certificate:
pts=[(sp.Rational(27,100),sp.Rational(16,100)),
     (sp.Rational(28,100),sp.Rational(16,100)),
     (sp.Rational(27,100),sp.Rational(15,100))]
weights=[sp.Rational(t,1497299) for t in (1004160,148115,345024)]
assert sum(weights)==1 and all(w>0 for w in weights)
grads=[(sp.diff(Q,x).subs({x:a,y:b}),sp.diff(Q,y).subs({x:a,y:b})) for a,b in pts]
assert sum(w*grad[0] for w,grad in zip(weights,grads))==0
assert sum(w*grad[1] for w,grad in zip(weights,grads))==0
intercepts=[Q.subs({x:a,y:b})-a*gx-b*gy for (a,b),(gx,gy) in zip(pts,grads)]
cert=sum(w*t for w,t in zip(weights,intercepts))
assert cert==sp.Rational(14888369619,116976484375)
assert cert>sp.Rational(1,8)
# The positive-definiteness of the Hessian follows from strict convexity of
# the L4 integral; the polynomial code does not replace that analytic proof.
r=sp.nroots(R,maxsteps=200)[0]
if abs(sp.im(r))>1e-12:
    r=[t for t in sp.nroots(R,maxsteps=200) if abs(sp.im(t))<1e-12][0]
rr=sp.re(r)
yy=-B.subs(x,rr)/A.subs(x,rr)
q=Q.subs({x:rr,y:yy})
assert abs(float(q)-.12737488298053188)<1e-10
assert abs(1/float(q)-7.850841363699946)<1e-8
print('PASS: exact norm identity, stationarity, degree-nine elimination, real-root isolation, rational global bound')
print('C_4,4 ≈',sp.N(1/q,16))
