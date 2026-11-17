#!/usr/bin/env python3
"""Exact symbolic replay for a one-cost-defect continuous-time mixing cycle."""
from fractions import Fraction as F
import sympy as S

checks = 0

def check(expr):
    global checks
    assert bool(expr)
    checks += 1

def Lmat(n, w, z):
    M = S.zeros(n)
    for i, a in enumerate(w):
        M[i,i] += a; M[i+1,i+1] += a
        M[i,i+1] -= a; M[i+1,i] -= a
    M[0,0] += z; M[-1,-1] += z
    M[0,-1] -= z; M[-1,0] -= z
    return M

lam,z=S.symbols('lam z', real=True)
x=S.symbols('x')
for n in range(5,11):
    weights=[lam*S.Rational(i*(n-i),2)-(n-1)*z for i in range(1,n)]
    L=Lmat(n,weights,z)
    v=S.Matrix([S.Rational(n+1,2)-i for i in range(1,n+1)])
    check(L*S.ones(n,1) == S.zeros(n,1))
    check(S.simplify(L*v-lam*v) == S.zeros(n,1))
    check(S.simplify(sum(weights)+(n-1)**2*z - lam*S.Rational(n*(n*n-1),12)) == 0)
    M=Lmat(n,[S.Rational(i*(n-i),2) for i in range(1,n)],0)
    expected=[S.Rational(k*(k+1),2) for k in range(n)]
    check(sorted(M.eigenvals(),key=lambda t: float(t)) == expected)
    # Path optimizer is the first positive eigenvalue exactly.
    check(M*v == v)

L=Lmat(5,[2*lam-4*z,3*lam-4*z,3*lam-4*z,2*lam-4*z],z)
formula=x*(x-lam)*(x-6*lam+10*z)*(x*x+(-13*lam+20*z)*x+30*lam*lam-100*lam*z+80*z*z)
check(S.expand(L.charpoly(x).as_expr()-formula)==0)
zcrit=lam*(10-S.sqrt(10))/20
q=x*x+(-13*lam+20*z)*x+30*lam*lam-100*lam*z+80*z*z
check(S.simplify(q.subs({x:lam,z:zcrit}))==0)
check(S.simplify(zcrit/lam)>0)
check(S.simplify(S.Rational(1,2)-zcrit/lam)>0)

for n in range(5,10):
    for b in [F(1),F(7,3)]:
        for a in [F(0),F(1,8),F(1,4)]:
            lam0=F(12)*b/F(n*(n*n-1))
            zz=lam0*a
            W=[lam0*F(i*(n-i),2)-(n-1)*zz for i in range(1,n)]
            LL=Lmat(n,[S.Rational(w.numerator,w.denominator) for w in W],S.Rational(zz.numerator,zz.denominator))
            check(sum(W)+F((n-1)**2)*zz == b)
            check(min(W)>0)
            ev=LL.eigenvals() if n<=7 else {}
            if n<=7: check(S.Rational(lam0.numerator,lam0.denominator) in ev)
            v=S.Matrix([S.Rational(n+1,2)-i for i in range(1,n+1)])
            check(LL*v == S.Rational(lam0.numerator,lam0.denominator)*v)
            if a==0 and n<=7:
                check(min([float(k) for k in ev if k!=0])==float(lam0))
            if a == F(1,8):
                # Lowering the closing-edge price by one makes the same positive-gap design cheaper.
                cheaper=b-zz
                check(cheaper > 0 and cheaper < b)
                check(sum(W)+(F((n-1)**2)-1)*zz == cheaper)
                check(b/cheaper > 1)
print('VERIFY_OK', checks)
