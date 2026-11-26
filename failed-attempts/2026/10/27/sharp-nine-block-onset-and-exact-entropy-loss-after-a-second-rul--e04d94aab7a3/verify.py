#!/usr/bin/env python3
"""Exact, self-contained certification for the Rule 54 first/second image comparison.

Run with Python 3: python verify.py
Uses only Python standard library; no external data or packages.
"""
from collections import deque
from fractions import Fraction
from math import gcd
from pathlib import Path

RULE = 54


def local_output(block, steps):
    """Apply the elementary rule to a consecutive (2*steps+1)-bit block."""
    row = list(block)
    assert len(row) == 2 * steps + 1
    for _ in range(steps):
        row = [((RULE >> (4*row[j] + 2*row[j+1] + row[j+2])) & 1)
               for j in range(len(row)-2)]
    return row[0]


def graph(steps):
    """Complete deterministic follower automaton, empty set included."""
    r = 2 * steps
    num = 1 << r
    local = [[0, 0] for _ in range(num)]
    for state in range(num):
        for bit in (0, 1):
            block_int = (state << 1) | bit
            block = tuple((block_int >> (r-i)) & 1 for i in range(r+1))
            label = local_output(block, steps)
            target = block_int & (num-1)
            local[state][label] |= 1 << target
    start = (1 << num) - 1
    masks = [start]
    index = {start: 0}
    edges = []
    j = 0
    while j < len(masks):
        mask = masks[j]
        nxt = []
        for letter in (0, 1):
            sub = mask
            dest = 0
            while sub:
                low = sub & -sub
                sub ^= low
                dest |= local[low.bit_length()-1][letter]
            if dest not in index:
                index[dest] = len(index)
                masks.append(dest)
            nxt.append(index[dest])
        edges.append(nxt)
        j += 1
    assert len(index) == len(masks) == len(edges)
    return masks, edges


def minimized(masks, edges):
    """Moore minimization: distinct right languages of all nonempty subsets."""
    cls = [int(x == 0) for x in masks]
    while True:
        signatures = [(int(masks[j] == 0),
                       cls[edges[j][0]], cls[edges[j][1]])
                      for j in range(len(masks))]
        d = {p: i for i, p in enumerate(dict.fromkeys(signatures))}
        new = [d[p] for p in signatures]
        if new == cls:
            break
        cls = new
    m = max(cls)+1
    rows = [None]*m
    for j in range(len(masks)):
        r = [cls[edges[j][0]], cls[edges[j][1]]]
        if rows[cls[j]] is not None:
            assert rows[cls[j]] == r
        rows[cls[j]] = r
    assert all(z is not None for z in rows)
    return rows, cls[0], cls[masks.index(0)]


def components(rows, dead):
    """Tarjan strongly-connected components of nondead labeled graph."""
    active = set(range(len(rows))) - {dead}
    clock = 0
    stack = []
    indices, lowlink, onstack = {}, {}, set()
    comps = []
    def visit(v):
        nonlocal clock
        indices[v] = clock
        lowlink[v] = clock
        clock += 1
        stack.append(v)
        onstack.add(v)
        for w in rows[v]:
            if w not in active:
                continue
            if w not in indices:
                visit(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in onstack:
                lowlink[v] = min(lowlink[v], indices[w])
        if lowlink[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))
    for v in sorted(active):
        if v not in indices:
            visit(v)
    return comps


def adjacency(rows, comp):
    pos = {v:i for i,v in enumerate(comp)}
    A = [[0 for _ in comp] for _ in comp]
    for v in comp:
        for w in rows[v]:
            if w in pos:
                A[pos[v]][pos[w]] += 1
    return A


def matmul(a, b):
    d = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d)) for j in range(d)]
            for i in range(d)]


def charpoly_coeffs(A):
    """Faddeev–LeVerrier identities over exact integers."""
    n = len(A)
    B = [[int(i==j) for j in range(n)] for i in range(n)]
    c = [1]
    for k in range(1, n+1):
        C = matmul(A, B)
        negtrace = -sum(C[i][i] for i in range(n))
        assert negtrace % k == 0
        ck = negtrace // k
        c.append(ck)
        for i in range(n):
            C[i][i] += ck
        B = C
    assert all(v == 0 for row in B for v in row)   # Cayley–Hamilton
    return c


def mulpoly(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def pf_bounds(A, iterations=110):
    """Certified rational Collatz–Wielandt interval, no numerical roots."""
    v = [1]*len(A)
    for _ in range(iterations):
        v = [sum(x*y for x,y in zip(row,v)) for row in A]
        common = gcd(*v)
        v = [x//common for x in v]
        assert min(v)>0
    Av = [sum(x*y for x,y in zip(row,v)) for row in A]
    quot = [Fraction(x,y) for x,y in zip(Av,v)]
    return min(quot), max(quot)


def dfa_words(edges, start, dead, n):
    states = {'':start}
    for _ in range(n):
        update={}
        for w,u in states.items():
            for letter in (0,1):
                dest=edges[u][letter]
                if dest!=dead:
                    update[w+str(letter)]=dest
        states=update
    return set(states)


def direct_words(steps, n):
    """Independent exhaustive local-preimage enumeration, no graph used."""
    length = n + 2*steps
    words = set()
    for x in range(1 << length):
        row = [(x >> (length-1-i)) & 1 for i in range(length)]
        for _ in range(steps):
            row = [((RULE >> (4*row[j]+2*row[j+1]+row[j+2])) & 1)
                   for j in range(len(row)-2)]
        words.add(''.join(map(str,row)))
    return words


def verify():
    expected = {
        1: {
            'reachable':11,'minimal':10,'core':8,
            'char':mulpoly(mulpoly([1,0,0],[1,0,1]),[1,-2,0,1,-1]),
            'counts':[2,4,8,16,29,53,100,187,348,649],
            'lo':Fraction(186675,100000), 'hi':Fraction(186677,100000),
        },
        2: {
            'reachable':39,'minimal':18,'core':16,
            'char': [1,-4,6,-5,2,2,-5,6,-2,-4,8,-4,-2,5,-4,1,0],
            'counts':[2,4,8,16,29,53,100,187,344,635],
            'lo':Fraction(182767,100000), 'hi':Fraction(182770,100000),
        }
    }
    W={}
    rows_csv=["steps,state,next0,next1,is_dead,in_entropy_core"]
    for t in (1,2):
        masks, edges = graph(t)
        data = expected[t]
        assert len(masks)==data['reachable'] and 0 in masks
        # Subset and minimized automata accept precisely the same right language.
        mins,start,dead = minimized(masks,edges)
        assert len(mins)==data['minimal']
        assert start == 0 and mins[dead] == [dead,dead]
        cores = components(mins,dead)
        nontriv = [x for x in cores if len(x)>1]
        assert len(nontriv)==1 and len(nontriv[0]) == data['core']
        assert len(cores)==2
        for c in cores:
            if len(c)==1:
                u=c[0]
                assert u not in mins[u]
        for j, (u,v) in enumerate(mins):
            rows_csv.append(f"{t},{j},{u},{v},{int(j==dead)},{int(j in nontriv[0])}")
        A=adjacency(mins,nontriv[0])
        assert charpoly_coeffs(A)==data['char']
        lo,hi=pf_bounds(A)
        assert data['lo'] < lo <= hi < data['hi'],(t,lo,hi)
        row=[]
        for n in range(1,11):
            ws=dfa_words(mins,start,dead,n)
            ds=direct_words(t,n)
            assert ws==ds,(t,n,sorted(ws ^ ds)[:5])
            row.append(len(ws))
            W[t,n] = ws
        assert row==data['counts'],(t,row)
    assert all(W[2,n]<=W[1,n] for n in range(1,11))
    assert all(W[1,n]==W[2,n] for n in range(1,9))
    assert W[1,9]-W[2,9] == {'011001110','011100101','011100110','101001110'}
    assert len(W[1,9]-W[2,9])==4
    # Rational Perron bounds disjoint; entropy drop is therefore strictly proved.
    assert expected[2]['hi'] < expected[1]['lo']
    table=Path(__file__).with_name("automata.csv")
    assert table.is_file()
    assert table.read_bytes() == ("\n".join(rows_csv)+"\n").encode("ascii")
    print('VERIFY_OK: independent finite-preimage languages through length 10; '
          'first/second-time minimal deterministic automata 10/18 states; '
          'principal SCCs 8/16 states; exact characteristic polynomials; '
          'rational Perron bounds (1.86675,1.86677) and (1.82767,1.82770); '
          'sharp length-nine first divergence: four specified words')

if __name__ == '__main__':
    verify()
