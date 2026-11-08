"""Independent finite-state max-plus energy-and-multiplicity checks.

Run: python3 verify_transfer.py
Includes an alternate exact transfer recursion for all cyclic original-spin words.
"""
from collections import defaultdict

def evaluate(n):
    # Fix hub to +1; 4-bit state records previous two original spins.
    # Transition (a,b)->(b,c) has gain |b-c| + a*c.
    # For cyclic x, sum of |x_i-x_{i+1}| + x_{i-1}x_{i+1}
    # equals the optimized energy gain B+T.
    best = -1
    total = 0
    for first in range(4):
        a0, b0 = (first >> 1) & 1, first & 1
        # Each word of length n is uniquely specified by start pair and n-2 successors.
        dp = {(a0,b0):(0,1)}
        for _ in range(n-2):
            nd = {}
            for (a,b),(value,count) in dp.items():
                for c in (0,1):
                    cand = value + (a!=b) + (a and c)
                    key=(b,c)
                    # This naive state best-collapsing would discard words that are
                    # suboptimal mid-path; it is legitimate for max-plus counts.
                    if key not in nd or cand>nd[key][0]: nd[key]=(cand,count)
                    elif cand==nd[key][0]: nd[key]=(cand,nd[key][1]+count)
            dp=nd
        for (a,b),(val,count) in dp.items():
            # The n-2 transitions score positions 0 through n-3.
            # The remaining two cyclic positions are scored explicitly.
            # Last two bits of original word are (a,b).
            v1=val+(a!=b)+(a and a0)
            v2=v1+(b!=a0)+(b and b0)
            # But the gain formula f(x_i,x_{i+1},x_{i+2})
            # is (x_i != x_{i+1}) + x_i*x_{i+2}.
            # First correction = f(x[n-2],x[n-1],x[0]); second=f(x[n-1],x[0],x[1]).
            if v2>best:best=v2;total=count
            elif v2==best: total+=count
    return best, 2*total

for n in range(4,202):
    e, g=evaluate(n)
    expect=(3*n//2 if n%2==0 else 3*(n-1)//2,4 if n%2==0 else 2*n)
    assert (e,g)==expect,(n,e,g,expect)
print('PASS cyclic transfer all lengths 4..201: exact energy and degeneracy')
