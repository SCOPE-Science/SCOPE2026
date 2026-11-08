#!/usr/bin/env python3
"""Independent checks for exact shifted binary digit-sum kernel classification.

Requires only the Python standard library.  All words and parameters are finite.
"""
from collections import deque

def popcount(n):
    return n.bit_count()


def extrema(t, e):
    """Minimum weight on [t,2**e), maximum on [0,t)."""
    assert 0 <= t < (1 << e)
    lo = popcount(t)
    hi = -1
    for i in range(e):
        upper = popcount(t >> (i + 1))
        if (t >> i) & 1:
            hi = max(hi, upper + i)
        else:
            lo = min(lo, upper + 1)
    return lo, hi


def formula_pairs(c, m):
    assert c >= 0 and m >= 2
    out = {(0, b) for b in range(m)}
    if c == 0:
        return out
    L = c.bit_length()
    _, h = extrema(c, L)
    out.update((1, b % m) for b in range(h + 1))
    for e in range(L):
        p = 1 << e
        q, t = divmod(c, p)
        lo, hi = extrema(t, e)
        out.update((q, b % m) for b in range(lo, e + 1))
        if t:
            out.update((q + 1, b % m) for b in range(hi + 1))
    return out


def bfs_pairs(c,m):
    start=(c,0)
    queue=deque([start])
    found={start}
    while queue:
        a,b=queue.popleft()
        for digit in (0,1):
            a2,r=divmod(a+digit,2)
            nxt=(a2,(b+r)%m)
            if nxt not in found:
                found.add(nxt)
                queue.append(nxt)
    return found


def minimize_bfs(c,m):
    pairs = sorted(bfs_pairs(c,m))
    index = {p:i for i,p in enumerate(pairs)}
    outs = [(a.bit_count()+b)%m for a,b in pairs]
    arcs = []
    for a,b in pairs:
        arcs.append(tuple(index[((a+d)//2,(b+(a+d)%2)%m)] for d in (0,1)))
    # Repeated refinement without assuming pair-state inequivalence.
    cells = [0]*len(pairs)
    for _ in range(len(pairs)+1):
        keys=[(outs[i],cells[arcs[i][0]],cells[arcs[i][1]]) for i in range(len(pairs))]
        dictionary={k:j for j,k in enumerate(sorted(set(keys)))}
        new=[dictionary[k] for k in keys]
        if new==cells:
            return len(set(new)), len(pairs)
        cells=new
    raise AssertionError('partition refinement failed')


def check():
    cases=0
    for c in range(0,129):
        for m in range(2,9):
            predicted=formula_pairs(c,m)
            actual=bfs_pairs(c,m)
            assert predicted==actual,(c,m,predicted^actual)
            minimized,total=minimize_bfs(c,m)
            assert minimized==total==len(predicted), (c,m,minimized,total,len(predicted))
            cases+=1
    extreme_cases=0
    for e in range(0,11):
        for t in range(1<<e):
            lo,hi=extrema(t,e)
            assert lo==min(popcount(z) for z in range(t,1<<e))
            assert hi==max([popcount(z) for z in range(t)],default=-1)
            extreme_cases+=1
    powers=0
    for m in (2,3,4,6,11,20):
        for k in range(0,16):
            actual = len(formula_pairs(1<<k,m))
            expected = m+sum(min(m,e+1) for e in range(k+1))
            assert actual==expected,(m,k,actual,expected)
            powers+=1
    # Check the evaluated sequence and its kernel directly, independently
    # of numerical state complexity/minimization for many small shifts.
    words=0
    for c in range(0,40):
        for m in (2,3,5):
            Q=bfs_pairs(c,m)
            for e in range(0,8):
                for r in range(1<<e):
                    A,B=divmod(c+r,1<<e)
                    pair=(A,popcount(B)%m)
                    assert pair in Q
                    for n in (0,1,2,3,7,16,31,63,127,250,511):
                        assert (popcount((1<<e)*n+r+c)%m) == ((popcount(n+A)+popcount(B))%m)
                    words+=1
    print('PASS: formula/reachability/independent DFAO minimization:',cases)
    print('PASS: binary interval extremum identities:',extreme_cases)
    print('PASS: power-of-two shift exact formulas:',powers)
    print('PASS: direct residual identities:',words,'(11 n-values each)')

if __name__=='__main__':
    check()
