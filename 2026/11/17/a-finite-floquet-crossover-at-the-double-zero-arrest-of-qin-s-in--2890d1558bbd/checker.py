"""Standalone algebraic and numerical diagnostics for a quadratic invariant-circle flow."""
import sympy as s
import mpmath as mp
x,y,a,b,c=s.symbols('x y a b c',real=True)
F=x*x+y*y-1
S=a*x+b*y+c
P=-y*S-F
Q=x*S
assert s.expand(2*x*P+2*y*Q+2*x*F)==0
assert s.expand(x*Q-y*P-(x*x+y*y)*S-y*F)==0
J=s.Matrix([P,Q]).jacobian([x,y]); corner=s.simplify(J.subs({x:0,y:-1,a:0,c:b}))
assert corner==s.Matrix([[0,b+2],[0,0]])
mp.mp.dps=50
B=mp.mpf('2');K=mp.mpf('1.5')
periodlimit=2*mp.pi/mp.sqrt(2*B)
multlimit=4*mp.pi*K/(B*mp.sqrt(2*B))
for e in ['1e-3','1e-5','1e-7']:
    eps=mp.mpf(e);A=K*mp.sqrt(eps)
    R=mp.sqrt(B*B+A*A);C=R+eps;D=mp.sqrt(C*C-R*R)
    T=2*mp.pi/D;logmu=2*A*T/(C+D)
    assert abs(mp.sqrt(eps)*T-periodlimit)<3*mp.sqrt(eps)
    assert abs(logmu-multlimit)<10*mp.sqrt(eps)
    import math
    # Check angular quadratures versus closed forms at a noncritical parameter.
C=mp.mpf('3');A=mp.mpf('0.7');B=mp.mpf('1.2');R=mp.sqrt(A*A+B*B);D=mp.sqrt(C*C-R*R)
f=lambda t:1/(C+A*mp.cos(t)+B*mp.sin(t))
numT=mp.quad(f,[0,mp.pi,2*mp.pi]);numlog=-2*mp.quad(lambda t:mp.cos(t)*f(t),[0,mp.pi,2*mp.pi])
assert abs(numT-2*mp.pi/D)<mp.mpf('1e-40')
assert abs(numlog-4*mp.pi*A/(D*(C+D)))<mp.mpf('1e-40')
print('QIN_DOUBLE_ZERO_CROSSOVER_CHECK_OK')
