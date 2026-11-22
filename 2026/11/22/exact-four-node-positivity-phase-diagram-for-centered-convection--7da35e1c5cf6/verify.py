"""Independent algebraic and rational checks for a four-point advection--diffusion theta update.
Run: python verify.py. Scientific proof of all-parameter claims is in RESULT.md.
"""
import random
import sympy as S
r,t,th=S.symbols('r t th', positive=True, real=True)
F=(1+2*r*t)**2+4*t*t
q0=S.Rational(1,4)*(1+1/(1+4*r*t)+2*(1+2*r*t)/F)
q2=S.Rational(1,4)*(1+1/(1+4*r*t)-2*(1+2*r*t)/F)
qgood=S.Rational(1,4)*(1-1/(1+4*r*t)+4*t/F)
qbad=S.Rational(1,4)*(1-1/(1+4*r*t)-4*t/F)
P=S.expand(r*F-(1+4*r*t))
assert S.simplify(qbad-(t*P)/((1+4*r*t)*F))==0
assert S.simplify(q0+q2+qgood+qbad-1)==0
assert S.expand(P-(4*r*(r*r+1)*t*t-4*r*(1-r)*t+r-1))==0
assert S.simplify(S.diff((1+2*r*t)/F,t) + (2*r*(1+2*r*t)**2+8*t+8*r*t*t)/F**2)==0
assert S.factor(S.diff(q0,t)).subs({r:S.Rational(1,3),t:S.Rational(3,5)})<0
# At the bad-neighbor sign boundary, q0 reduces to a simple fraction.
B=(1+r)*(1+2*r*t)/(2*(1+4*r*t))
num=S.together(q0-B)
assert S.rem(S.fraction(num)[0],P,t)==0
# The CN critical parameter and the unique critical timestep are exact.
r0=S.sqrt(2)-1; t0=(2+S.sqrt(2))/4
assert S.simplify(P.subs({r:r0,t:t0}))==0
assert S.simplify(q0.subs({r:r0,t:t0})-S.Rational(1,2))==0
assert S.factor(P.subs(t,1/(2*(1-r))))==(r*r+2*r-1)/(r-1)**2
# Direct exact inversions of theta-scheme matrices against Fourier formula.
I=S.eye(4)
N=S.zeros(4)
for i in range(4):
    N[i,i]=-2*r
    N[i,(i+1)%4]=r+1
    N[i,(i-1)%4]=r-1
rng=random.Random(20261120)
comparisons=0
for k in range(320):
    rr=S.Rational(rng.randrange(1,12),rng.randrange(12,30))
    if rr>=1: continue
    theta=rng.choice([S.Rational(1,3),S.Rational(1,2),S.Rational(2,3),S.Rational(3,4),S.Rational(1,1), S.Rational(4,5)])
    hh=S.Rational(rng.randrange(1,41),rng.randrange(4,15))
    ss=theta*hh
    A=N.subs(r,rr)
    matrix=(I-theta*hh*A).inv()*(I+(1-theta)*hh*A)
    predicted=((P.subs({r:rr,t:ss})>=0) and (q0.subs({r:rr,t:ss})>=1-theta))
    observed=all(v>=0 for v in matrix)
    assert observed==predicted,(rr,theta,hh)
    # Every Fourier entry is checked against the actual inverse.
    row=[q0, qgood, q2, qbad]
    # The sign convention of the cyclic shift determines good/bad order.
    calculated=[S.simplify(q.subs({r:rr,t:ss})/theta - ((1-theta)/theta if j==0 else 0)) for j,q in enumerate(row)]
    assert sorted(calculated)==sorted(list(matrix.row(0)))
    comparisons+=1
# Check the explicit CN bounded interval at r=1/2.
rr=S.Rational(1,2);theta=S.Rational(1,2)
for x,yes in [(S.Rational(1,2),False),(S.Rational(7,10),True),(S.Rational(4,5),True),(S.Rational(9,10),False)]:
    assert bool((P.subs({r:rr,t:x})>=0) and(q0.subs({r:rr,t:x})>=1-theta))==yes
print('PASS: 7 algebraic identities/boundaries,',comparisons,'exact rational matrix inversions and CN interval witnesses')
