#!/usr/bin/env python3
"""Direct set-enumeration cross-check, independent of interval arithmetic."""
G = set(range(1,60)) | {74,112,113,119}
assert len(G)==63 and max(G)==119
# The complement is a numerical semigroup: every positive nongap
# is at least 60, and every integer at least 120 is a nongap.
assert all((i+j) not in G for i in range(60,120) if i not in G
           for j in range(60,120) if j not in G)
assert all((i+j) not in G for i in range(120,241)
           for j in range(120,241))
EXPECTED = [0,1,0,0,1,1,0,-6,-12,-18,-24,-30,-36]
acc = {0}
for n in range(1,15):
    acc = {x+y for x in acc for y in G}
    if n >= 2:
        beta=len(acc)-(2*n-1)*62
        assert beta == EXPECTED[n-2], (n,beta)
        if n>=8:
            assert len(acc) == 118*n-14
        print(f'n={n} count={len(acc)} beta={beta}')
print('DIRECT_ENUMERATION_OK')
