#!/usr/bin/env python3
"""Standalone algebraic identity and finite trajectory diagnostics for the displayed theorem.
Finite runs are *not* a proof of the uniform asymptotic statement.
"""
import math
import sympy as s

A,y=s.symbols('A y',positive=True)
p=1/(A-1)
q=A*(A+1)/(2*(A-1)**3)
H=p*y+q*y*y
Y=s.series((1+A*H)*(1-s.exp(-y)),y,0,4).removeO().expand()
a=(1+A)/(2*(1-A))
b=(1-6*A*A-A**3)/(6*(1-A)**3)
B=(1+3*A+9*A*A-A**3)/(6*(1-A)**2*(1+A))
assert s.simplify(Y.coeff(y,1)-1)==0
assert s.simplify(Y.coeff(y,2)+a)==0
assert s.simplify(Y.coeff(y,3)-b)==0
assert s.simplify((a*a-b)/a-B)==0
inv=s.series(H.subs(y,Y)-(A*H-Y),y,0,3).removeO().expand()
assert all(s.simplify(inv.coeff(y,i))==0 for i in range(3))
print('Exact symbolic slow-jet and invariance identities: PASS')

def trial(alpha, lam, N, x0, y0):
    beta=(1-alpha)/alpha+lam/N
    x,y=x0,y0
    for _ in range(N):
        transfer=-math.expm1(-y)
        x,y=alpha*x*(1-transfer)+beta,alpha*x*transfer
    c=alpha/(1-alpha);a=(1+alpha)/(2*(1-alpha))
    B=(1+3*alpha+9*alpha*alpha-alpha**3)/(6*(1-alpha)**2*(1+alpha))
    U=a*(-math.expm1(-c*lam))/(c*lam) if lam else a
    return 1/y-N*U-B*math.exp(-c*lam)*math.log(N)

for alpha,lam,x0,y0 in [(.5,-.8,2,.6),(.5,0,2,.6),(.5,.8,2,.6),(.25,.8,1.6,.2),(.7,-.8,4,.8)]:
    vals=[trial(alpha,lam,N,x0,y0) for N in (2000,8000,32000)]
    assert all(math.isfinite(v) and abs(v)<1000 for v in vals),(alpha,lam,vals)
    assert abs(vals[-1]-vals[-2])<5,(alpha,lam,vals)
    print('trajectory check',alpha,lam,['%.8f'%v for v in vals],'PASS')
print('Finite trajectory diagnostics: PASS (not an infinite proof)')
