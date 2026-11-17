#!/usr/bin/env python3
"""Finite exact-rational sanity checks; the almost-sure theorem is proved in RESULT.md."""
from fractions import Fraction as Q
from itertools import product

def opportunity_count(path, m):
    """Predictable opportunities: active iff previous draws of edge zero are even.

    Decision at time t depends only on draws at times below t.
    """
    earlier_hits = 0
    seen = 0
    chosen_on_opportunities = []
    for j in path:
        active = (earlier_hits % 2 == 0)
        if active:
            seen += 1
            chosen_on_opportunities.append(j == 0)
        earlier_hits += (j == 0)
    return tuple(chosen_on_opportunities)

def check_probability_bound():
    # For the event of >=k opportunities with no successful draw at any of them,
    # exhaustive exact probability never exceeds (1-1/m)**k.
    for m in (1, 2, 3):
        for horizon in range(1, 7):
            counts = [opportunity_count(path, m)
                      for path in product(range(m), repeat=horizon)]
            for k in range(1, horizon + 1):
                bad = sum(1 for statuses in counts
                          if len(statuses) >= k and not any(statuses[:k]))
                prob = Q(bad, m ** horizon)
                assert prob <= (Q(m-1, m) ** k), (m, horizon, k, prob)

def check_confidence_jumps():
    for c_num in range(0, 12):
        c = Q(c_num, 11)
        for g_num in range(1, 12):
            gamma = Q(g_num, 11)
            new = c + gamma * (1-c)
            assert new >= gamma and 0 <= new <= 1

def check_two_node_paths():
    # The two-node edge is always selected; if receptive initially, opinion
    # separation decreases and confidence increases, so receptiveness persists.
    for x in (Q(0), Q(1,4), Q(1,2)):
        for y in (Q(1,2), Q(3,4), Q(1)):
            for mu in (Q(1,10),Q(1,2)):
                for gamma in (Q(1,10),Q(1)):
                    for c0 in (Q(1,4),Q(1,2),Q(3,4)):
                        a,b,c=x,y,c0
                        was_receptive = abs(a-b)<c
                        for _ in range(20):
                            if abs(a-b)<c:
                                a,b = (1-mu)*a+mu*b,mu*a+(1-mu)*b
                                c=c+gamma*(1-c)
                            else:
                                c=Q(1,2)*c
                            if was_receptive:
                                assert abs(a-b)<c

def main():
    check_probability_bound()
    check_confidence_jumps()
    check_two_node_paths()
    print('PASS: rational opportunity bounds, confidence jumps and finite two-node dynamics')

if __name__ == '__main__': main()
