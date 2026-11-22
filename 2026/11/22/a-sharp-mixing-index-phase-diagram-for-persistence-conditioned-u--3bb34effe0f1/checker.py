"""Exact finite-state checks of the upper-tail and support lemmas.

These discretizations verify identities; they are not evidence for an infinite theorem.
"""
from fractions import Fraction as F
from itertools import combinations

checks=0

def test(c,a,green):
    global checks
    m=min(a,F(1,c))
    L=-m
    if green:
        grid=[F(-7,16),F(-3,8),F(-1,4),F(-1,8),F(0),F(1,8),F(1,4),F(3,8),F(1,2),F(3,4),F(1)]
    else:
        grid=[-a,F(-1,8),F(0),F(1,8),F(1,4),F(1,2),F(3,4),F(1)]
    grid=[z for z in grid if z>L or (not green and z==L)]
    b=m/c
    # A positive density-like weight rising to its prescribed constant plateau.
    wt=[F(0) if z==L else F(1) if z>=b else F(1,4)+F(3,4)*(z-L)/(b-L) for z in grid]
    H=sum(wt)
    mu=[v/H for v in wt]
    rows=[]
    for x in grid:
        allowed=[j for j,z in enumerate(grid) if z>-c*x]
        assert allowed
        normal=sum(mu[j] for j in allowed)
        rows.append([mu[j]/normal if j in allowed else F(0) for j in range(len(grid))])
    for i,j in combinations(range(len(grid)),2):
        tv=sum(abs(u-v) for u,v in zip(rows[i],rows[j]))/2
        # Two truncated nested tails have exactly this ratio.
        upper=max(-c*grid[i],-c*grid[j])
        lower=min(-c*grid[i],-c*grid[j])
        p_hi=sum(mu[z] for z,y in enumerate(grid) if y>upper)
        p_lo=sum(mu[z] for z,y in enumerate(grid) if y>lower)
        assert tv==1-p_hi/p_lo
        checks+=1
    if not green:
        q=sum(mu[j] for j,y in enumerate(grid) if y>c*a)
        actual=max(sum(abs(u-v) for u,v in zip(rows[i],rows[j]))/2 for i,j in combinations(range(len(grid)),2))
        assert actual==1-q
        checks+=1
    q2=sum(mu[j] for j,y in enumerate(grid) if y>=b)
    for i,x in enumerate(grid):
        qb=sum(rows[i][j] for j,y in enumerate(grid) if y>=b)
        assert qb>=q2
        checks+=1
        for j,y in enumerate(grid):
            if y>=b:
                assert rows[j]==mu
                checks+=1
        for z in range(len(grid)):
            step2=sum(rows[i][j]*rows[j][z] for j in range(len(grid)))
            assert step2>=q2*mu[z]
            checks+=1
    return len(grid)

# Exact rational grids with both sides of the sharp endpoint.
for c,a,green in [(F(2),F(1,4),False),(F(2),F(1,2),True),(F(3),F(1,3),True)]:
    test(c,a,green)

# Support propagation for the positive-coupling chain: if each jump is legal,
# the terminal state exceeds the iterated multiplicative lower bound.
for theta in [F(3,2),F(2),F(3)]:
    states=[F(-1),F(-3,4),F(-1,2),F(-1,4),F(-1,8),F(-1,16)]
    for x in states:
        frontier={x}
        for k in range(1,5):
            frontier={y for z in frontier for y in states if y>theta*z}
            assert all(y>theta**k*x for y in frontier)
            checks+=1
print(f"PASS: {checks} exact rational assertions")
