#!/usr/bin/env python3
"""Independent combinatorial enumeration for minimum cube zero forcing (d=2,3,4)."""
from itertools import combinations
from collections import Counter


def zero_forces(d, chosen):
    n=1<<d
    colored=set(chosen)
    steps=0
    while len(colored)<n:
        to_add=set()
        for u in colored:
            waiting=[u^(1<<j) for j in range(d) if (u^(1<<j)) not in colored]
            if len(waiting)==1:to_add.add(waiting[0])
        if not to_add:return None
        colored.update(to_add)
        steps+=1
    return steps


def main():
    expected={2:(4,{1:4}),3:(30,{1:6,2:24}),4:(2360,{1:8,2:816,3:1152,4:384})}
    for d in (2,3,4):
        n=1<<d;k=n//2
        assert all(zero_forces(d,c) is None for c in combinations(range(n),k-1))
        sets={frozenset(c):zero_forces(d,c) for c in combinations(range(n),k)}
        winners={s:r for s,r in sets.items() if r is not None}
        assert len(winners)==expected[d][0]
        assert dict(Counter(winners.values()))==expected[d][1]
        for s in winners:
            assert sum(x.bit_count()%2==0 for x in s)==n//4
            for x in s:
                for j in range(d):
                    y=x^(1<<j)
                    if y not in s:
                        assert (s-{x})|{y} not in winners
        print(f'd={d}: optimal={len(winners)}; propagation={dict(sorted(Counter(winners.values()).items()))}; slides=0')
    print('ENUMERATION_CERTIFICATE_PASS')

if __name__=='__main__':main()
