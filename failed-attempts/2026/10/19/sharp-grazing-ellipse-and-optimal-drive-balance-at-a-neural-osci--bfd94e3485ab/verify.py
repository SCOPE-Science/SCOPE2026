"""Exact algebraic checks for an active-cell Matsuoka center and its grazing ellipse.

Run with Python 3 and SymPy: python verify.py
The analytical proof supplies the all-parameter and all-time quantifiers.
"""
import sympy as sp

T, S, b, sig, drive, r = sp.symbols('T S b sig drive r', positive=True)
c = 1 + T / S
alpha12 = c / sig
alpha21 = c * sig
Delta = (1 + b)**2 - c**2
p = drive * (1 + b - alpha12 * r) / Delta
q = drive * ((1 + b) * r - alpha21) / Delta
u, v = sp.symbols('u v', real=True)

# Full affine four-neuron residuals on the candidate center plane.
x1, y1, x2, y2 = p + u, p + v, q - sig * u, q - sig * v
vx1 = sp.factor((-x1-b*y1-alpha12*x2+drive)/T)
vy1 = sp.factor((-y1+x1)/S)
vx2 = sp.factor((-x2-b*y2-alpha21*x1+r*drive)/T)
vy2 = sp.factor((-y2+x2)/S)
assert sp.simplify(vx1-(u/S-b*v/T)) == 0
assert sp.simplify(vy1-(u-v)/S) == 0
assert sp.simplify(vx2+sig*vx1) == 0
assert sp.simplify(vy2+sig*vy1) == 0

omega2 = (b-T/S)/(T*S)
K2 = 1+S*S*omega2
assert sp.simplify(K2-b*S/T) == 0
assert sp.simplify((1+b)*p+alpha12*q-drive) == 0
assert sp.simplify(alpha21*p+(1+b)*q-r*drive) == 0
assert sp.simplify((q/sig-p).subs(r, sig)) == 0
assert sp.simplify(p.subs(r, sig)-drive/(1+b+c)) == 0
assert sp.simplify(q.subs(r, sig)-sig*drive/(1+b+c)) == 0

# Exact rational example: the frequency, amplitudes and two grazing extrema.
values = {T:sp.Integer(1), S:sp.Integer(4), b:sp.Rational(1,2),
          sig:sp.Rational(5,4),drive:sp.Integer(1), r:sp.Rational(5,4)}
P=sp.factor(p.subs(values))
Q=sp.factor(q.subs(values))
w=sp.sqrt(omega2.subs(values))
K=sp.sqrt(K2.subs(values))
R=sp.simplify(P/K)
area=sp.simplify(sp.pi*w*values[S]*R**2)
embedded_area=sp.simplify(area*(1+values[sig]**2))
assert (P,Q,w,K,R)==(sp.Rational(4,11),sp.Rational(5,11),
                       sp.Rational(1,4),sp.sqrt(2),sp.Rational(2,11)*sp.sqrt(2))
assert area==8*sp.pi/121
assert embedded_area==41*sp.pi/242
assert sp.simplify(Q/values[sig]-P)==0
assert sp.simplify(P-K*R)==0
assert sp.simplify(Q-values[sig]*K*R)==0

# Nonoptimal asymmetric tonic input: only neuron 2 grazes.
other = dict(values)
other[r] = sp.Rational(6,5)
p_other = sp.simplify(p.subs(other))
q_other = sp.simplify(q.subs(other))
assert p_other == sp.Rational(24,55)
assert q_other == sp.Rational(19,55)
R_other = sp.simplify((q_other / other[sig])/K)
assert sp.simplify(R_other-R) < 0
assert sp.simplify(q_other-other[sig]*K*R_other)==0
assert sp.simplify(p_other-K*R_other)>0

# Exact trigonometric state on the maximal orbit: every ODE residual vanishes.
t = sp.symbols('t',real=True)
vt=R*sp.cos(w*t)
ut=sp.simplify(vt+values[S]*sp.diff(vt,t))
xt1=P+ut; yt1=P+vt
xt2=Q-values[sig]*ut; yt2=Q-values[sig]*vt
f1=sp.simplify((-xt1-values[b]*yt1-sp.Integer(1)*xt2+1)/values[T])
g1=sp.simplify((-yt1+xt1)/values[S])
f2=sp.simplify((-xt2-values[b]*yt2-sp.Rational(25,16)*xt1+values[r])/values[T])
g2=sp.simplify((-yt2+xt2)/values[S])
for residual in [sp.diff(xt1,t)-f1,sp.diff(yt1,t)-g1,
                 sp.diff(xt2,t)-f2,sp.diff(yt2,t)-g2]:
    assert sp.trigsimp(sp.simplify(residual))==0
assert sp.simplify(sp.sqrt(2)*R-P)==0
print('SYMBOLIC_CENTER_AND_ELLIPSE_OK')
print('EXAMPLE:p=',P,'q=',Q,'omega=',w,'R=',R,'area=',area)
