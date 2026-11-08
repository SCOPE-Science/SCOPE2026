"""Exact finite-step checks for a three-agent neighborhood-confidence phase diagram.

All comparisons and states use rational arithmetic. This file checks identities
and finite trajectories; infinite-time assertions require the accompanying proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

E=F(1,5)
R=F(1,2)
C0=F(1,2)

def update(s, z, c, eps=E, rho=R):
    """One selected edge of the three-node path with endpoint opinions 0,1."""
    leaf0, hub, leaf1 = c
    if z not in (0,1): raise ValueError(z)
    if z==0:
        # hub looks at leaf0's only neighbor (the hub itself)
        hscore=s*abs(hub-leaf0)+(1-s)*abs(hub-hub)
        # leaf0 looks at the mean of the hub's two neighbors
        lscore=s*abs(leaf0-hub)+(1-s)*abs(leaf0-(leaf0+leaf1)/2)
        new_hub = hub+rho*(leaf0-hub) if hscore<eps else hub
        new_leaf0 = leaf0+rho*(hub-leaf0) if lscore<eps else leaf0
        return (new_leaf0,new_hub,leaf1)
    hscore=s*abs(hub-leaf1)+(1-s)*abs(hub-hub)
    lscore=s*abs(leaf1-hub)+(1-s)*abs(leaf1-(leaf0+leaf1)/2)
    new_hub = hub+rho*(leaf1-hub) if hscore<eps else hub
    new_leaf1 = leaf1+rho*(hub-leaf1) if lscore<eps else leaf1
    return (leaf0,new_hub,new_leaf1)

# Verify the complete finite-depth stochastic tree on each side of both
# phase boundaries. 2**12 paths times 5 settings, exact arithmetic.
for s in [F(0),F(1,10),F(1,5),F(3,10),F(2,5),F(3,5),F(1)]:
    paths=[((F(0),C0,F(1)),F(1))]
    for t in range(9):
        nxt=[]
        for state,prob in paths:
            for z in (0,1):
                nxt.append((update(s,z,state),prob/2))
        paths=nxt
        assert sum(p for _,p in paths)==1
        assert all(a==0 and b==1 and F(0)<=c<=1 for (a,c,b),_ in paths)
        if s>=F(2,5):
            assert all(state==(0,C0,1) for state,_ in paths)
    if s<=F(1,5):
        # all paths: center exactly dyadic midpoints with equal weights
        xs=sorted({state[1] for state,_ in paths})
        assert len(xs)==2**9
        assert xs==[F(2*k+1,2**10) for k in range(2**9)]
        m=sum(state[1]*p for state,p in paths)
        v=sum((state[1]-m)**2*p for state,p in paths)
        assert m==F(1,2) and v==(1-F(1,4**9))/12
    if s==F(3,10):
        # first edge locks in an absorbing left/right influence sector
        assert update(s,0,(0,C0,1))==(0,F(1,4),1)
        assert update(s,1,(0,C0,1))==(0,F(3,4),1)
        assert update(s,1,(0,F(1,4),1))==(0,F(1,4),1)
        assert update(s,0,(0,F(3,4),1))==(0,F(3,4),1)
        t=9
        m=sum(state[1]*p for state,p in paths)
        v=sum((state[1]-m)**2*p for state,p in paths)
        expected=F(1,4)-F(1,4)*F(3,4)**(t-1)+F(1,16)*F(5,8)**(t-1)
        assert m==F(1,2) and v==expected

# Threshold equality is strict: at s=2 eps the center is unreceptive,
# while at s=eps it is receptive at every finite time from c in (0,1).
for sigma in [F(1,5),F(2,5)]:
    for z in (0,1):
        first=update(sigma,z,(0,C0,1))[1]
        assert (first != C0)==(sigma==F(1,5))

# For mixed dyadic weight, frozen leaves hold uniformly if s <=1-2eps.
for s in [F(0),F(1,5),F(3,10),F(2,5),F(3,5)]:
    assert E <= (1-s)/2
    for h in [F(k,64) for k in range(65)]:
        for z in (0,1):
            a,c,b=update(s,z,(F(0),h,F(1)))
            assert (a,b)==(0,1)
print('VERIFY_OK: exact boundary, leaf, recursion, dyadic law and finite-time variance tests')
