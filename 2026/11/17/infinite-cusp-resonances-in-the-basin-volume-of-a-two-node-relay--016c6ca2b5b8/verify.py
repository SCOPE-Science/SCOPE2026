#!/usr/bin/env python3
"""Finite exact-rational checks for the two-node relay basin theorem."""
from fractions import Fraction as Q

def bins(a):
    assert Q(0) < a < Q(1)
    k = 1
    while a**k > Q(1, 2):
        k += 1
    widths = [(1-a)/(2*a**j) for j in range(1, k)]
    widths.append(1-Q(1)/(2*a**(k-1)))
    assert all(w >= 0 for w in widths)
    assert sum(widths) == Q(1, 2)
    area = 2*sum((w*w for w in widths), Q(0))
    closed = (1-a)/(2*(1+a))*(a**(-2*(k-1))-1) + 2*(1-a**(-(k-1))/2)**2
    assert area == closed
    return k, area

def crossing(a, low, high):
    u, v = 1-low, high
    j = 1
    while a**j*u >= Q(1, 2): j += 1
    h = 1
    while a**h*v >= Q(1, 2): h += 1
    return j, h

def iterate(a, x, y):
    return a*x+(1-a)*int(y>Q(1,2)), a*y+(1-a)*int(x>Q(1,2))

assert bins(Q(1,2)) == (1,Q(1,2))
assert bins(Q(2,3)) == (2,Q(1,4))
assert bins(Q(3,4)) == (3,Q(29,162))
checks = 0
for a in [Q(2,5), Q(1,2), Q(2,3), Q(3,4), Q(4,5), Q(9,10)]:
    k, area = bins(a)
    for xi in range(1,30):
        for yi in range(1,30):
            x,y=Q(xi,30),Q(yi,30)
            if x==Q(1,2) or y==Q(1,2):continue
            is_mixed=(x-Q(1,2))*(y-Q(1,2))<0
            t1,t2=crossing(a,min(x,y),max(x,y)) if is_mixed else (0,0)
            expected_cycle=is_mixed and t1==t2
            steps=max(2, t1,t2)+3
            boundary=False
            for _ in range(steps):
                if x==Q(1,2) or y==Q(1,2):
                    boundary=True
                    break
                x,y=iterate(a,x,y)
            if boundary: continue  # explicitly outside the a.e. theorem
            got_cycle=(x-Q(1,2))*(y-Q(1,2))<0
            assert got_cycle == expected_cycle, (a,xi,yi,t1,t2,x,y)
            checks+=1
print(f'RELAY_BASIN_CHECK_OK exact_parameter_cases=6 exact_initial_trajectories={checks}')
