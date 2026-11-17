"""Independent exhaustive full-state primitive-four test on complete graphs.

Uses the ordinary loopless threshold degree n-1 and integer chips.
"""
from collections import Counter
from itertools import product
from math import comb


def update(state):
    n=len(state)
    firing=[int(v>=n-1) for v in state]
    r=sum(firing)
    return tuple(v+r-n*f for v,f in zip(state,firing))


def direct(n):
    counts=Counter()
    for x in product(range(2*n-2),repeat=n):
        y=update(x)
        z=update(y)
        w=update(z)
        if update(w)==x and z!=x and y!=x:
            counts[sum(x)]+=1
    return counts


def predicted_support(n):
    low=n*(n-1)-(3*n*n//8)
    upper=(n-1)*(n-2)
    ref=n*(2*n-3)
    return set(range(low,upper+1))|set(range(ref-upper,ref-low+1))

for n in range(3,7):
    actual=direct(n)
    assert set(actual)==(predicted_support(n) if n>=4 else set())
    if n>=4:
        top=(n-1)*(n-2)
        expectation=4*n*(n-1)*(2**(n-2)-n)+(24 if n==4 else 0)
        assert actual[top]==expectation,(n,actual[top],expectation)
        assert all(actual[k]==actual[n*(2*n-3)-k] for k in actual)
    assert sum(actual.values())%4==0
    print('n',n,'primitive_4_states',sum(actual.values()),'orbits',sum(actual.values())//4,'low_band',min(actual,default=None),'high_band',max(actual,default=None),'upper_low_edge_count',actual.get((n-1)*(n-2),0))
print('EXHAUSTIVE PASS')
