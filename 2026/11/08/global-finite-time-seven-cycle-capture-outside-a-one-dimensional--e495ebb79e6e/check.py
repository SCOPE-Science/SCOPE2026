"""Exact affine-symbolic checks for the planar seven-cycle basin theorem.

Represent u+v*b by (u,v) with rational u,v. No floating-point
operations are used. The proof of global capture uses cited theorems;
this script checks the explicit orbit and arithmetic formulas only.
"""
from fractions import Fraction as Q

def z(c=0,d=0):
    return (Q(c),Q(d))
def plus(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def minus(u,v): return plus(u,neg(v))
B=z(0,1); ONE=z(1); NEGONE=z(-1)

def sign_at_minusb2(u):
    """Classify expressions known to have fixed sign throughout b<=-2."""
    at=u[0]-2*u[1]
    if u[1]<=0 and at>=0: return 1
    if u[1]>=0 and at<=0: return -1
    raise AssertionError('symbolic sign needs more justification '+str(u))

def step(point):
    x,y=point
    sx=sign_at_minusb2(x)
    sy=sign_at_minusb2(y)
    return (minus((x if sx>=0 else neg(x)),plus(y,ONE)),
            minus(plus(x,B),(y if sy>=0 else neg(y))))

P=[(plus(neg(B),z(-2)),NEGONE),
   (plus(neg(B),z(-2)),z(-3)),
   (neg(B),z(-5)),
   (plus(neg(B),z(4)),z(-5)),
   (plus(neg(B),z(8)),z(-1)),
   (plus(neg(B),z(8)),z(7)),
   (neg(B),z(1))]
Qorb=[(plus(neg(B),z(Q(-16,15))),z(Q(-1,15))),
    (plus(neg(B),z(-2)),z(Q(-17,15))),
    (plus(neg(B),z(Q(-28,15))),z(Q(-47,15))),
    (plus(neg(B),z(Q(4,15))),z(-5)),
    (plus(neg(B),z(Q(64,15))),z(Q(-71,15))),
    (plus(neg(B),z(8)),z(Q(-7,15))),
    (plus(neg(B),z(Q(112,15))),z(Q(113,15)))]
for name,orbit in [('attracting',P),('exceptional',Qorb)]:
    assert len(set(orbit))==7
    for i,x in enumerate(orbit):
        assert step(x)==orbit[(i+1)%7], (name,i,step(x),orbit[(i+1)%7])
# Explicit line inside x,y>0 maps to Qorb[0].
# x=t-b-1/15, y=t, with t>0 and b<=-2.
T=z(10)
assert step((minus(minus(T,B),z(Q(1,15))),T))==Qorb[0]
# The fixed point p=(-b,-1) is fixed.
p=(neg(B),NEGONE)
assert step(p)==p
# Each of the seven Q-orbit entries fails to belong to Z+bZ in both
# coordinates simultaneously, for irrational b and rational b=p/q
# whose denominator q is not divisible by 15.
for x,y in Qorb:
    assert any(coord[0].denominator==15 for coord in (x,y))
    assert any(coord[0].denominator==15 and coord[1] in (Q(-1),Q(0)) for coord in (x,y))
# Exploratory exact rational orbit sampling: verifies representative
# nonexceptional points enter the seven-cycle; not a universal proof.
def f_numeric(pt,b):
    x,y=pt
    return abs(x)-y-1, x-abs(y)+b
for b in [Q(-2),Q(-5,2),Q(-3),Q(-7,2),Q(-4)]:
    target={(x[0]+x[1]*b,y[0]+y[1]*b) for x,y in P}
    exceptional={(x[0]+x[1]*b,y[0]+y[1]*b) for x,y in Qorb}
    exceptional.add((-b,Q(-1)))
    hit=0
    for i in range(-8,9):
      for j in range(-8,9):
        x,y=Q(i,3),Q(j,5)
        for n in range(300):
            if (x,y) in target:
                hit+=1;break
            if (x,y) in exceptional:
                break
            x,y=f_numeric((x,y),b)
        else:
            # Exceptional fixed points and repellers can occupy this grid.
            raise AssertionError((b,i,j,x,y))
    assert hit>=270,(b,hit)
print('SYMBOLIC_SEVEN_CYCLE_AND_ARITHMETIC_CHECK_OK')
