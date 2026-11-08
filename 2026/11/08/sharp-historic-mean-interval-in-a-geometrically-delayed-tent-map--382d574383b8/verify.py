#!/usr/bin/env python3
"""Exact rational checks for geometric-stasis tent-map Cesaro asymptotics."""
from fractions import Fraction as Q
from itertools import product

def tent(x):
    return 2*x if 2*x<=1 else 2*(1-x)

def predecessors(x):
    return (x/2, 1-x/2)

def bound(k):
    return Q(2*k,2*k+1)

checks=0
for k in range(2,8):
    for seed in (Q(0),Q(1),Q(1,3),Q(2,3),Q(2,5),Q(1,7),Q(8,13)):
        values=[seed]
        for m in range(1,9):
            values.append(tent(values[-1]))
        for m,y in enumerate(values):
            # Check the defining delayed recurrence only at representative
            # locations, avoiding impractically large full sequences.
            start=(k**m-1)//(k-1)
            end=start+k**m
            for n in {start,max(start,end-2),end-1}:
                if n+1<end:
                    idx=0
                    while (k**(idx+1)-1)//(k-1)<=n+1: idx+=1
                    delayed_idx=0
                    while (k**(delayed_idx+1)-1)//(k-1)<=n//k: delayed_idx+=1
                    assert values[idx]==tent(values[delayed_idx])
                    checks+=1
            avg=sum((k**j * values[j] for j in range(m+1)),Q(0))/end
            if m==0: assert avg==seed
            else:
                prevend=(k**m-1)//(k-1)
                prevavg=sum((k**j * values[j] for j in range(m)),Q(0))/prevend
                assert end*avg==prevend*prevavg+k**m*y
            checks+=1
    # For all inverse-branch histories up to depth eight and grids of terminal
    # points, verify the sharp universal upper barrier algebraically.
    for i in range(17):
        x=Q(i,16)
        for choices in product((0,1), repeat=8):
            hist=[x]
            for bit in choices:
                hist.append(predecessors(hist[-1])[bit])
            numerator=sum((Q(1,k**j)*hist[j] for j in range(9)),Q(0))
            discounted=Q(k-1,k)*numerator
            assert discounted<=bound(k)
            checks+=1
    # The maximizing infinite inverse history is x_0=1 and z_{-j}=H^j(1).
    hist=Q(1)
    partial=Q(0)
    for j in range(48):
        partial += Q(k-1,k**(j+1))*hist
        assert partial<=bound(k)
        hist=Q(1)-hist/2
        checks+=1
    assert bound(k)-partial<Q(1,10**10)
    checks+=1

# The explicit two-cycle source has two distinct endpoint mean limits.
p=Q(2,5); r=Q(4,5)
assert tent(p)==r and tent(r)==p
assert (2*p+r)/3==Q(8,15)
assert (2*r+p)/3==Q(2,3)
checks+=4
print(f'VERIFY_OK exact_checks={checks} k_range=2..7 grid=17 inverse_depth=8')
