#!/usr/bin/env python3
"""Exhaustive local-weight certificates for Seeds B2/S on a 3-row torus."""
from collections import Counter
from itertools import product

def update_middle(word):
    return tuple(3-word[i] if word[i-1]+word[i]+word[i+1]==2 else 0
                 for i in range(1,len(word)-1))

def cyclic_update(word):
    n=len(word)
    return tuple(3-word[i] if word[(i-1)%n]+word[i]+word[(i+1)%n]==2 else 0
                 for i in range(n))

# Two updates at a single site use five initial consecutive column counts.
C=Counter()
for a in product(range(4), repeat=5):
    b=update_middle(update_middle(a))[0]
    C[b]+=1
assert C==Counter({0:963,1:18,3:43})
print('two_step_center',dict(sorted(C.items())))

# Adjacent two-step sites depend on six input column counts.
adjacent_ones=0
for a in product(range(4),repeat=6):
    b=update_middle(update_middle(a))
    adjacent_ones+=(b==(1,1))
assert adjacent_ones==0
print('adjacent_two_step_ones',adjacent_ones,'out_of',4**6)

# Independent direct third-step local outcome check (seven input columns).
C3=Counter()
for a in product(range(4),repeat=7):
    b=update_middle(update_middle(update_middle(a)))[0]
    C3[b]+=1
assert C3==Counter({0:16375,3:9})
print('three_step_center',dict(sorted(C3.items())))

# Complete all-state weight census at the two shortest ring lengths.
for n,want in [(3,2),(4,3)]:
    sharp=0
    for a in product(range(4),repeat=n):
        b=a
        for t in range(1,5):
            b=cyclic_update(b)
            if any(b): sharp=max(sharp,t+1)
        assert b==(0,)*n
    assert sharp==want
    print('short_ring_nilpotency_index',n,want)

# A single live cell in each of three successive columns gives a sharp clock.
for n in range(5,20):
    a=(1,1,1)+(0,)*(n-3)
    for t in range(1,4):a=cyclic_update(a)
    assert any(a)
    assert cyclic_update(a)==(0,)*n
print('three_consecutive_singletons_sharp_for_n', '5..19')
print('WEIGHT_CONES_PASS')
