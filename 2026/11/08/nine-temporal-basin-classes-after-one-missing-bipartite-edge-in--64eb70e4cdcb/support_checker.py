"""Exact finite-state verification for ternary successor contact on K_(m,n)-e.

Run: python3 support_checker.py
Only the Python standard library is required.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb

EXPECTED = {
 (0,1): {(1,1):3},
 (0,3): {(3,3):9,(3,2):6,(2,3):6,(2,2):3},
 (0,4): {(2,2):24,(2,1):12,(1,2):12},
 (1,1): {(2,2):12,(2,1):15,(1,2):15,(1,1):24},
 (1,3): {(3,2):3,(2,3):3},
 (1,4): {(3,2):18,(3,1):12,(2,3):18,(1,3):12,(2,2):30,(2,1):12,(1,2):12},
 (2,1): {(3,1):9,(1,3):9,(2,1):24,(1,2):24,(1,1):24},
 (2,4): {(3,1):6,(1,3):6,(2,2):12,(2,1):12,(1,2):12},
 (3,1): {(2,1):6,(1,2):6,(1,1):30},
}
# Coefficient keys are the cardinalities of the nonempty color-support sets.
# A singleton support contributes the multiplicative unit.

def advance(state):
    singled_a, singled_b, regular_a, regular_b = state
    sa, sb = set(regular_a), set(regular_b)
    ta, tb = sa | {singled_a}, sb | {singled_b}
    def go(color, neighbors):
        succ = (color + 1) % 3
        return succ if succ in neighbors else color
    return (go(singled_a, sb), go(singled_b, sa),
            tuple(go(c, tb) for c in regular_a),
            tuple(go(c, ta) for c in regular_b))

def signature(sa, sb, a0, b0):
    state = (a0, b0,
             tuple(c for c in range(3) if sa & (1 << c)),
             tuple(c for c in range(3) if sb & (1 << c)))
    seen = {}
    while state not in seen:
        assert len(seen) < 20
        seen[state] = len(seen)
        state = advance(state)
    return seen[state], len(seen)-seen[state]

def support_formula(r, support_size):
    if support_size==1: return 1
    if support_size==2: return 2**r-2
    if support_size==3: return 3**r-3*2**r+3
    raise AssertionError

def check():
    results = defaultdict(Counter)
    raw_counts = Counter()
    for sa, sb, a0, b0 in product(range(1,8), range(1,8), range(3), range(3)):
        t,p=signature(sa,sb,a0,b0)
        key=(sa.bit_count(), sb.bit_count())
        results[t,p][key]+=1
        raw_counts[t,p]+=1
    assert sum(raw_counts.values()) == 7*7*9 == 441
    assert dict(results)=={k:Counter(v) for k,v in EXPECTED.items()}
    assert raw_counts==Counter({(0,1):3,(0,3):24,(0,4):48,
         (1,1):66,(1,3):6,(1,4):114,(2,1):90,(2,4):48,(3,1):42})
    for m,n in product(range(2,12), repeat=2):
        r,s=m-1,n-1
        census={}
        for tp,coeff in results.items():
            census[tp]=sum(v*support_formula(r,a)*support_formula(s,b)
                            for (a,b),v in coeff.items())
        assert sum(census.values()) == 3**(m+n)
        assert all(t<=3 and p in (1,3,4) for t,p in census)
        assert census[3,1] == 30+6*(2**r-2)+6*(2**s-2)
    # A concrete sharp witness on the four-vertex path.
    assert signature(1,1,0,1) == (3,1)
    print('SUPPORT_CHECK_OK 441 abstract states; 9 classes; exact coefficient table; sizes 2..11.')
    for k in sorted(raw_counts):
        print('class',k,'abstract_count',raw_counts[k], 'coefficients', dict(sorted(results[k].items())))

if __name__ == '__main__': check()
