"""Exact verification of the bipartite-switching public-goods/opinion result.

Run: python CHECK.py. Uses only SymPy and the Python standard library.
"""
from fractions import Fraction as F
import random
import sympy as S

alpha, r, n, beta, lam, z, m, x = S.symbols('alpha r n beta lam z m x', positive=True)
h = alpha * (1-r/n)
k = beta*lam/(beta+lam)

def val(act):
    yy = (beta*m+lam*act)/(beta+lam)
    return -h*act-S.Rational(1,2)*beta*(yy-m)**2-S.Rational(1,2)*lam*(act-yy)**2
assert S.simplify(val(S.Integer(1))-val(S.Integer(0)) + h-k*(m-S.Rational(1,2))) == 0

# The two-block linear period-two equations and the strict switching test.
c, p, q = S.symbols('c p q', positive=True)
d=1-c
D = d/(d+2*c*p)
lo=(1-D)/2
hi=(1+D)/2
mH=S.factor(p*lo+(1-p)*hi)
mL=S.factor(p*hi+(1-p)*lo)
assert S.simplify(hi-(c*mH+d))==0
assert S.simplify(lo-c*mL)==0
pc=S.factor(d*(1-q)/(2*(d+c*q)))
assert S.factor(((1-2*p)*D-q)*(d+2*c*p))==S.factor(2*(d+c*q)*(pc-p))

# Illustrative 4-player exact witness.
c0=F(1,2); p0=F(1,4); q0=F(2,9); t0=(1+q0)/2
assert pc.subs({c:S.Rational(1,2),q:S.Rational(2,9)})==S.Rational(7,22)
w=[[F(0),p0,(1-p0)/2,(1-p0)/2],
   [p0,F(0),(1-p0)/2,(1-p0)/2],
   [(1-p0)/2,(1-p0)/2,F(0),p0],
   [(1-p0)/2,(1-p0)/2,p0,F(0)]]

A=(F(1,6),F(1,6),F(5,6),F(5,6))
B=tuple(1-a for a in A)
xA=(0,0,1,1); xB=(1,1,0,0)
def step(y):
    means=[sum(w[i][j]*y[j] for j in range(4)) for i in range(4)]
    actions=tuple(int(z>t0) for z in means)
    return tuple(c0*means[i]+(1-c0)*actions[i] for i in range(4)),actions,means
Y,act,M=step(A)
assert Y==B and act==xB and M==[F(2,3),F(2,3),F(1,3),F(1,3)]
Y2,act2,M2=step(Y)
assert Y2==A and act2==xA
assert t0==F(11,18) and min(M[0]-t0,t0-M[2])==F(1,18)
W=S.Matrix([[S.Rational(a.numerator,a.denominator) for a in row] for row in w])
assert sorted(W.eigenvals().keys()) == [S.Rational(-1,2),S.Rational(-1,4),S.Integer(1)]
assert W.eigenvals()[S.Rational(-1,4)]==2
assert set((S.Rational(1,4)*W**2).eigenvals().keys())=={S.Rational(1,4),S.Rational(1,16),S.Rational(1,64)}

# Random exact rational interior tests against the exact switching threshold.
rng=random.Random(412)
for _ in range(360):
    c1=F(rng.randint(1,11),12)
    q1=F(rng.randint(1,11),12)
    p1=F(rng.randint(1,11),12)
    d1=1-c1
    cutoff=d1*(1-q1)/(2*(d1+c1*q1))
    gap=(1-2*p1)*d1/(d1+2*c1*p1)-q1
    assert (gap>0)==(p1<cutoff)
    dh=d1/(d1+2*c1*p1)
    yl=(1-dh)/2; yh=(1+dh)/2
    H=p1*yl+(1-p1)*yh
    L=p1*yh+(1-p1)*yl
    assert yh==c1*H+d1 and yl==c1*L
    if p1<cutoff:
        assert H>(1+q1)/2>L
        assert 0<=yl<yh<=1

print('PASS: symbolic payoff discriminant, exact branch equations, sharp cutoff,')
print('       rational 4-agent cycle/stability and 360 rational parameter comparisons.')
