"""Exact check of a four-leaf rooted-tree conservation witness.

Run with Python 3.8+: python check.py
Only standard-library arithmetic is used.
"""
from fractions import Fraction as Q
from itertools import combinations

# Root topology: (a,(b,(c,d))), with no stem above the root.
# Each pair is (descendant-leaf mask, positive edge length).
EDGES = ((1,3),(2,5),(4,2),(8,9),(12,7),(14,8))
BASE_EXT = (Q(1,2),)*4
AFTER_EXT = (Q(1,5),Q(1,10),Q(1,10),Q(3,10))

def expected_pd(extinction):
    total=Q(0)
    for mask,length in EDGES:
        p_all_extinct=Q(1)
        for i in range(4):
            if mask & (1<<i):
                p_all_extinct*=extinction[i]
        total+=length*(1-p_all_extinct)
    return total

def gain(protected):
    ex=list(BASE_EXT)
    for i in protected:
        ex[i]=AFTER_EXT[i]
    return expected_pd(ex)-expected_pd(BASE_EXT)

def expected_pd_by_enumeration(extinction):
    answer=Q(0)
    for subset in range(16):
        prob=Q(1)
        for i in range(4):
            prob*=1-extinction[i] if subset & (1<<i) else extinction[i]
        surviving_length=sum(length for mask,length in EDGES if mask & subset)
        answer+=prob*surviving_length
    return answer

for subset in range(16):
    p=list(BASE_EXT)
    for i in range(4):
        if subset & (1<<i): p[i]=AFTER_EXT[i]
    assert expected_pd(p)==expected_pd_by_enumeration(p)

singles={k:gain((k,)) for k in range(4)}
pairs={p:gain(p) for p in combinations(range(4),2)}
assert singles == {0:Q(9,10), 1:Q(14,5), 2:Q(3), 3:Q(29,10)}, singles
assert pairs == {
 (0,1):Q(37,10), (0,2):Q(39,10), (0,3):Q(19,5),
 (1,2):Q(129,25), (1,3):Q(269,50), (2,3):Q(251,50)
},pairs
first=max(range(4),key=lambda x:singles[x])
second=max((i for i in range(4) if i!=first),
           key=lambda x:gain((first,x)))
assert (first,second)==(2,1)
assert pairs[(1,3)]-pairs[(1,2)]==Q(11,50)
assert pairs[(1,3)]>max(v for pair,v in pairs.items() if pair!=(1,3))
print('PASS: all exact singleton and pair gains; unique greedy sequence (c,b); unique optimum (b,d); gap 11/50')
