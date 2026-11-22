"""Exact consistency checks for the trace-zero character-divisor normal form.
Uses SymPy, with no network, external data, or approximate arithmetic.
The proof of the universal GIT quotient is in RESULT.md, not inferred from samples.
"""
import sympy as S
I=S.I
t,u,v,w=S.symbols('t u v w',nonzero=False)
A=S.diag(t,1/t)
B=S.diag(I/t,-I*t)
C=S.Matrix([[u,v],[w,-u]])
D=C.det()-1

def mod_relation(expr):
    return S.factor(S.cancel(expr)).subs(v*w,-1-u**2)

assert S.simplify(A.det()-1)==0
assert S.simplify(B.det()-1)==0
assert S.simplify(A*A*B*B+S.eye(2))==S.zeros(2)
assert S.simplify(A*B-S.diag(I,-I))==S.zeros(2)
assert S.factor(C.det()-1)==-(u*u+v*w+1)
assert S.simplify(C*C+S.eye(2))==S.eye(2)*(u*u+v*w+1)
a=S.trace(A);b=S.trace(B);p=S.trace(A*B);c=S.trace(C)
q=S.trace(B*C);r=S.trace(C*A);s=S.trace(A*B*C)
for expr in [p,c,a*a+b*b-4,2*q-a*s,2*r-b*s,s-2*I*u,(a+I*b)/2-t]:
    assert S.simplify(expr)==0,expr
assert S.factor(a*a+b*b-4)==0
print('PASS: universal matrix identities, determinant relation and seven trace equations')

# A family with non-diagonal C and a boundary case v=0.
for tt,uu,vv in [(S.Rational(2), S.Rational(3), S.Rational(5)),(I,S.Integer(0),S.Integer(1)),(S.Rational(1,3),-I,S.Integer(0))]:
    ww=(-(1+uu**2)/vv) if vv!=0 else S.Integer(0)
    Aa=A.subs(t,tt);Bb=B.subs(t,tt);Cc=C.subs({u:uu,v:vv,w:ww})
    assert Cc.det()==1
    assert Aa*Aa*Bb*Bb*Cc*Cc==S.eye(2)
print('PASS: three exact SL2 representation samples, including v=0')

# Algebraic morphism of the punctured conic: parametrization and inverse.
aa,bb=S.symbols('aa bb')
tinv=(aa+I*bb)/2
assert S.factor(tinv*((aa-I*bb)/2)-(aa**2+bb**2)/4)==0
assert S.simplify(tinv + (aa-I*bb)/2 - aa)==0
assert S.simplify(I*((aa-I*bb)/2-tinv)-bb)==0
print('PASS: Laurent inverse t=(a+i*b)/2, t^-1=(a-i*b)/2 on a^2+b^2=4')
