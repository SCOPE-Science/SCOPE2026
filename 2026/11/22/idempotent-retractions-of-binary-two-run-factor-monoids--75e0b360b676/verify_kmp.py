#!/usr/bin/env python3
"""Direct KMP transition-monoid closure and idempotent census.

Python >=3.8, no external dependencies. All assertions are exhaustive finite tests,
not a substitute for the all-order proof in RESULT.md.
"""
from collections import deque


def prefix_machine(pattern):
    n = len(pattern)
    rows = []
    for symbol in '01':
        row = []
        for k in range(n + 1):
            if k == n:
                row.append(n)
                continue
            tail = pattern[:k] + symbol
            if pattern in tail:
                row.append(n)
            else:
                row.append(max(j for j in range(n) if tail.endswith(pattern[:j])))
        rows.append(tuple(row))
    return tuple(rows)


def enumerate_monoid(transitions):
    n = len(transitions[0]); identity = tuple(range(n))
    seen = {identity}; frontier = deque([identity])
    while frontier:
        t = frontier.popleft()
        for a in transitions:
            u = tuple(a[t[x]] for x in range(n))
            if u not in seen:
                seen.add(u)
                frontier.append(u)
    return seen


def predicted(r,s):
    if min(r,s) == 1:
        return (r+s)*(r+s-1)//2+3
    return r*(r-1)//2 + s*(s-1)//2 + 2*r*s+3


def run():
    tests = 0
    for r in range(1,11):
        for s in range(1,11):
            transitions = prefix_machine('0'*r+'1'*s)
            elements = enumerate_monoid(transitions)
            size = r+s+1
            identity = tuple(range(size))
            zero = (size-1,)*size
            idem = {t for t in elements if all(t[t[i]] == t[i] for i in range(size))}
            assert len(idem) == predicted(r,s), (r,s,len(idem),predicted(r,s))
            assert identity in idem and zero in idem
            assert all(len(set(t)) <= 2 for t in idem-{identity}), (r,s)
            cardinality = (r+s)**2+r*s+1 if min(r,s)>1 else (r+s)**2+1
            assert len(elements) == cardinality, (r,s,len(elements),cardinality)
            tests += 1
    print('PASS: 100 exhaustive monoids (1<=r,s<=10); exact idempotent census, ranks, established total sizes')

if __name__ == '__main__':
    run()
