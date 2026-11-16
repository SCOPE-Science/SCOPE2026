"""Independent integer state-table certificate for complete binary-tree Walsh cancellation.

Run: python3 tree_state_certificate.py
"""
from collections import Counter
from math import gcd

# The two coordinates are (whole signed sum, sum with root excluded).
states = Counter({(2, 1): 1, (0, 1): 1})
state_tables = {0:states}
for height in range(1,4):
    new = Counter()
    for (a, b), u in states.items():
        for (c, d), v in states.items():
            new[(a*c+b*d,a*c)] += u*v
            new[(a*c-b*d,a*c)] += u*v
    states = new
    state_tables[height] = states

assert sum(state_tables[2].values()) == 128
assert len(state_tables[2]) == 12
assert sum(m for (a,b),m in state_tables[2].items() if a==b) == 120
# All height-three vanishing signs occur only at a negative root.
by_sign = {sign:sum(u*v for (a,b),u in state_tables[2].items()
                        for (c,d),v in state_tables[2].items()
                        if a*c+sign*b*d == 0) for sign in (-1,1)}
assert by_sign == {-1:14402,1:0}
assert by_sign[-1] == 120*120+2
assert sum(v for (a,b),v in state_tables[3].items() if a==0) == 14402
assert sum(state_tables[3].values()) == 32768
assert gcd(*(a for (a,b) in state_tables[3])) == 2
assert max(a for (a,b) in state_tables[3]) == 2306
assert sum(v*a*a for (a,b),v in state_tables[3].items()) == 32768*2306
print('height-two state table:')
for pair,m in sorted(state_tables[2].items()):print(pair,m)
print('height-three zero counts by root sign:',by_sign)
print('BINARY_TREE_STATE_CERTIFICATE_PASS')
