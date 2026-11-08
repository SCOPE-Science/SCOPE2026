#!/usr/bin/env python3
"""Finite algebraic and illustrative checks for delayed rational activation/inhibition."""
from fractions import Fraction as F
from math import exp, log

def h(s, mode, a=F(2), k=F(1)):
    return a*s/(k+s) if mode=='act' else a*k/(k+s)
def dh(s, mode, a=F(2), k=F(1)):
    out=a*k/(k+s)**2
    return out if mode=='act' else -out

count=0
for mode in ('act','inh'):
    for s in (F(1,5),F(1,2),F(1),F(2),F(7)):
        H=h(s,mode)
        assert s*abs(dh(s,mode))==H-H**2/F(2)
        count+=1
# Three nodes: 2->1 activation, 1->2 inhibition, 1->3 activation.
links={0:[(1,'act')],1:[(0,'inh')],2:[(0,'act')]}
for i in range(3):
    assert F(2)==F(1)+sum(h(F(1),m) for j,m in links[i])
# For all z in [1/2,2]^3: h(z)>=2/3, z |h'|<=1/2.
for mode in ('act','inh'):
    assert min(h(F(1,2),mode),h(F(2),mode))==F(2,3)
    for z in (F(1,2),F(1),F(2)):
        assert z*abs(dh(z,mode))<=F(1,2)
delta=F(11,18); B=F(1); delay=7; eta=0.01
assert eta+B*(exp(eta*delay)-1)<float(delta)
# Forward Euler method-of-steps with lags that are integer multiples of dt.
dt=0.01; T=150; lag={0:300,1:500,2:700} # delays to inputs: 3, 5, 7
hist=[1.45,0.65,1.7]
y=[hist[:] for _ in range(701)]
for step in range(int(T/dt)):
    curr=y[-1]
    feed=[F(0)]*3
    feed[0]=float(h(F(str(y[-1-lag[0]][1])),'act'))
    feed[1]=float(h(F(str(y[-1-lag[1]][0])),'inh'))
    feed[2]=float(h(F(str(y[-1-lag[2]][0])),'act'))
    nextx=[curr[i]+dt*(-2*curr[i]+1+feed[i]) for i in range(3)]
    assert all(0.5<=u<=2 for u in nextx)
    y.append(nextx)
last=max(abs(log(u)) for u in y[-1]); assert last<1e-4
print('VERIFY_OK rational_identities=%d reducible_equilibrium=3 delta_lower=%s beta_upper=%s admissible_eta=%.3f delays=3 numerical_final_log_error=%.6g' % (count,delta,B,eta,last))
