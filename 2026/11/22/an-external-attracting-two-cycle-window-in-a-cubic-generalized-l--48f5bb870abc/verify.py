#!/usr/bin/env python3
"""Exact algebraic consistency checks for cubic generalized-logistic two-cycles.
Requires SymPy (see requirements.txt). Outputs PASS only after exact identities hold.
No computer search is used to assert mathematical novelty or infinite completeness.
"""
import sympy as S

q,t,d,u,v=S.symbols('q t d u v', real=True)
f=q*t*(1-t)**2
P=S.expand(f.subs(t,f)-t)
Q=t*(q*(t-1)**2-1)*(q*t*t-q*t+1)*(
    q*q*t**4-3*q*q*t**3+3*q*q*t*t-q*q*t-q*t+q+1)
assert S.expand(P-Q)==0, 'second-iterate factorization'
M=q*q*(1-u+v)*(1-3*u+9*v)
assert S.cancel(M.subs({u:1,v:1/q})-(9-2*q))==0
# Cross-side case: sum u, product u(u-1)/2, parameter 2/[(u-1)(2-u)].
Mx=S.factor(M.subs(v,u*(u-1)/2).subs(q,2/((u-1)*(2-u))))
qd=8/(1-d*d)
for sign in (+1,-1):
    us=(3+sign*d)/2
    expected=9-qd*(1+3*sign*d)   # sqrt(q(q-8))=qd*d for d>0
    assert S.cancel(Mx.subs(u,us)-expected)==0
star=(S.Integer(13)+3*S.sqrt(41))/4
assert star>8 and star<10
assert S.simplify((10-star)**2-9*star*(star-8))==0
assert S.simplify(2*star*star-13*star-25)==0
# Check both formulas return a swapped pair as a symbolic identity.
z=S.symbols('z', positive=True)
innerx=(1+z)/2; innery=(1-z)/2
qi=4/(1-z*z)
assert S.simplify(qi*innerx*(1-innerx)**2-innery)==0
assert S.simplify(qi*innery*(1-innery)**2-innerx)==0
for sign in (+1,-1):
    ss=(3+sign*d)/2
    rr=S.sqrt(ss*(2-ss))
    xx=(ss+rr)/2; yy=(ss-rr)/2
    for expr in [qd*xx*(1-xx)**2-yy, qd*yy*(1-yy)**2-xx]:
        assert S.simplify(S.powdenest(S.expand(expr),force=True))==0
print('PASS: complete symbolic factorization, both two-cycle constructions,')
print('      inner/external multipliers, exact fold and flip thresholds.')
