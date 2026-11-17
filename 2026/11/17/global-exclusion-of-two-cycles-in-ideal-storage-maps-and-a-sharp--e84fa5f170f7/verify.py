#!/usr/bin/env python3
"""Reproduce exact finite identities and illustrative algebraic inequalities."""
from fractions import Fraction as Q
from math import log, exp, isclose

c=Q(1,2)
z0=(Q(4,5),Q(3,8))
z1=(Q(1,1),Q(7,10))
a=z0[0]*z0[1]
b=z1[0]*z1[1]
assert a==Q(3,10) and b==Q(7,10) and a+b==2*c
assert z0[0]*(1-z0[1])+c==z1[0]
assert z1[0]*(1-z1[1])+c==z0[0]
alpha=2.5*log(35/9)
beta=.3*alpha+log(7/3)
def h_down(u): return 1/(1+exp(alpha*u-beta))
assert alpha>0
assert isclose(h_down(float(a)),float(z1[1]),abs_tol=1e-14)
assert isclose(h_down(float(b)),float(z0[1]),abs_tol=1e-14)

def step(s,r,c,h): return (s*(1-r)+c, h(s*r))
w=step(float(z0[0]),float(z0[1]),float(c),h_down)
v=step(*w,float(c),h_down)
assert all(isclose(x,y,abs_tol=1e-13) for x,y in zip(w,map(float,z1)))
assert all(isclose(x,y,abs_tol=1e-13) for x,y in zip(v,map(float,z0)))

# For any putative two-cycle, a+b=2c and its stock displacement
# would equal (b-a)/2. Monotonicity forces a larger displacement.
checks=0
for k in [0.1,0.7,5.0,20.0]:
  for shift in [-4,-1,0,1,4]:
    def hm(t): return 1/(1+exp(-k*t+shift))
    for i in range(1,60):
      aa=i/45
      bb=aa+i/57
      displacement=bb/hm(aa)-aa/hm(bb)
      assert displacement>bb-aa>(bb-aa)/2
      checks+=1
    cc=0.73
    ss=cc/hm(cc)
    s_next,r_next=step(ss,hm(cc),cc,hm)
    assert isclose(s_next,ss,abs_tol=1e-12)
    assert isclose(r_next,hm(cc),abs_tol=1e-12)
print('passed:',checks,'monotonicity comparisons, 20 fixed points, exact rational witness and two logistic endpoint checks')
