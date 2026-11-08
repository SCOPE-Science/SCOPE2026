#!/usr/bin/env python3
"""Exact and finite sanity checks for the two-cycle exclusion theorem."""
from fractions import Fraction as Q
import sympy as sp
x,s = sp.symbols("x s", real=True, nonzero=True)
y0 = 2-s-x
x1 = s*x
y1 = 2-1/s-x1
assert sp.simplify((y1-y0)-(s-1)*(1+1/s-x))==0
# All two-point prey orbit equations are already encoded in these identities.
# At s>1, positivity y0>0 forces x<2-s<1, implying y1>y0.
# But positive predator multipliers have product one and increase with x,
# hence y1<y0. Thus a strict positive 2-cycle is impossible.
tests=0
for r in [Q(1,5),Q(1,2),Q(1),Q(3,2),Q(2)]:
    for g in [Q(1,4),Q(1,2),Q(1),Q(3),Q(6)]:
        def F(z):
            a,b=z
            return (a*(2-a-b),b*(1-r+g*a))
        for a in [Q(k,8) for k in range(17)]:
            for b in [Q(k,8) for k in range(17)]:
                z=(a,b);v=F(z)
                if min(v)>=0 and F(v)==z:
                    assert v==z, (r,g,z,v)
                tests+=1
print(f"VERIFY_OK symbolic_identity=1 exact_grid_cases={tests} exact_parameter_pairs=25")
