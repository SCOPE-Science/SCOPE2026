#!/usr/bin/env python3
"""Independent wheel shattering support enumerator and recurrence verifier."""
from collections import Counter


def data(n, mask):
    p = list(range(n + 1))
    cycles = False
    def root(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for i in range(n):
        for j, a, b in ((i, i, (i + 1) % n), (n + i, i, n)):
            if (mask >> j) & 1:
                a, b = root(a), root(b)
                if a == b:
                    cycles = True
                else:
                    p[a] = b
    connected = all(root(i) == root(n) for i in range(n))
    return not cycles, connected


def brute(n):
    full = (1 << (2 * n)) - 1
    counts = [0] * (n + 1)
    for mask in range(1 << (2 * n)):
        if mask.bit_count() <= n and data(n, mask)[0] and data(n, full ^ mask)[1]:
            counts[mask.bit_count()] += 1
    return counts


def pol_add(a, b):
    m = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(m)]


def mul(a, b):
    ret = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ret[i+j] += x*y
    return ret


def transfer(n):
    states = [(r,s,c,d) for r in (0,1) for s in (0,1) for c in (0,1) for d in (0,1)]
    edges = []
    for i, (r, s, c, d) in enumerate(states):
        for j, (R, S, C, D) in enumerate(states):
            if C == (c + S if r else S) <= 1 and D == (d + R if S else R) <= 1:
                edges.append((i, j, R+S))
    # enumerate closed walks length n by dynamic programming
    out = [0] * (n+1)
    for start in range(16):
        curr = {(start, 0): 1}
        for _ in range(n):
            nxt = {}
            for (i, degree), coeff in curr.items():
                for a,b,weight in edges:
                    if a != i: continue
                    key = (b, degree+weight)
                    nxt[key] = nxt.get(key,0)+coeff
            curr=nxt
        for (i, degree), coeff in curr.items():
            if i == start: out[degree] += coeff
    out[n] -= 4
    return out


def recurrence(n):
    # q(lambda) = lambda^3 - (1+4z)lambda^2 + (2z+4z^2)lambda - z^2
    q0=[3]
    q1=[1,4]
    q2=pol_add(mul(q1,q1),[-0,-4,-8])  # -2*(2z+4z^2)
    traces=[q0,q1,q2]
    for k in range(3,n+1):
        term=pol_add(mul([1,4],traces[k-1]),[-x for x in mul([0,2,4],traces[k-2])])
        term=pol_add(term,mul([0,0,1],traces[k-3]))
        traces.append(term)
    val=traces[n] + [0]*(n+1-len(traces[n]))
    val[n]-=4
    return val

if __name__ == '__main__':
    for n in range(3,9):
        a=brute(n)
        b=transfer(n)
        c=recurrence(n)
        assert a == b == c, (n,a,b,c)
        print('n=',n,'coefficients=',a)
    for n in range(9,13):
        assert transfer(n)==recurrence(n)
        print('n=',n,'recurrence-automaton agreement')
    n=5
    full=(1<<(2*n))-1
    supports={m for m in range(1<<(2*n)) if data(n,m)[0] and data(n,full^m)[1]}
    facets=[m for m in supports if all((m|(1<<j)) not in supports for j in range(2*n) if not (m>>j)&1)]
    facet_sizes=Counter(m.bit_count() for m in facets)
    assert facet_sizes == Counter({4:5,5:60}), facet_sizes
    example=(1<<2)|(1<<4)|(1<<5)|(1<<7)
    assert example in facets
    print('five-rim facets:',dict(facet_sizes),'witness:',example)
    print('WHEEL_SHATTERING_CHECKS_PASS')
