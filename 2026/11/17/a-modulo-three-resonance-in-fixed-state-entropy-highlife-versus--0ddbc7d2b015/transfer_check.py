#!/usr/bin/env python3
"""Exact integer certificate for fixed configurations on 3-row Life and HighLife tori.
Run: python3 transfer_check.py (standard library only).
"""
from collections import Counter


def make_edges(births):
    edges = [[] for _ in range(64)]
    for a in range(8):
        for b in range(8):
            for c in range(8):
                total = a.bit_count() + b.bit_count() + c.bit_count()
                if all((total - ((b >> r) & 1) in ({2, 3} if (b >> r) & 1 else births)) == bool((b >> r) & 1)
                       for r in range(3)):
                    edges[8 * a + b].append(8 * b + c)
    return edges


def components(edges):
    # Kosaraju's algorithm, with independent transposed traversal.
    rev = [[] for _ in edges]
    for v, adj in enumerate(edges):
        for w in adj:
            rev[w].append(v)
    seen = set()
    finish = []
    def visit(v):
        seen.add(v)
        for w in edges[v]:
            if w not in seen:
                visit(w)
        finish.append(v)
    for v in range(len(edges)):
        if v not in seen:
            visit(v)
    seen.clear()
    result = []
    def explore(v, comp):
        seen.add(v)
        comp.append(v)
        for w in rev[v]:
            if w not in seen:
                explore(w, comp)
    for v in reversed(finish):
        if v not in seen:
            comp = []
            explore(v, comp)
            if len(comp) > 1 or v in edges[v]:
                result.append(sorted(comp))
    return sorted(result, key=lambda t: (-len(t), t))


def characteristic(edges, comp):
    # Newton identities on exact traces; no floating point or CAS.
    ix = {v:i for i,v in enumerate(comp)}
    aa = [[ix[w] for w in edges[v] if w in ix] for v in comp]
    k = len(comp)
    traces = [0] * (k+1)
    for seed in range(k):
        vec = [0] * k
        vec[seed] = 1
        for n in range(1,k+1):
            nxt = [0] * k
            for u in range(k):
                if vec[u]:
                    for w in aa[u]:
                        nxt[w] += vec[u]
            vec = nxt
            traces[n] += vec[seed]
    coeff = [1]
    for n in range(1,k+1):
        sm = sum(coeff[n-j]*traces[j] for j in range(1,n+1))
        assert sm % n == 0
        coeff.append(-sm // n)
    return aa, coeff, traces


def pf_bracket(aa, lo, hi):
    v = [1] * len(aa)
    for _ in range(50):
        w = [0] * len(aa)
        for i, adj in enumerate(aa):
            for j in adj:
                w[i] += v[j]
        v = w
    w = [sum(v[j] for j in row) for row in aa]
    assert all(z > 0 for z in v)
    assert all(lo*z < 100000*t < hi*z for z,t in zip(v,w))
    return True


def main():
    h, l = make_edges({3,6}), make_edges({3})
    ch,cl=components(h),components(l)
    assert ch==cl and [len(x) for x in ch] == [30,27]
    assert [sum(len(x) for x in e) for e in [h,l]] == [155,156]
    assert [(i,j) for i in range(64) for j in l[i] if j not in h[i]] == [(56,7)]
    assert 0 in ch[0] and 0 in h[0] and 0 in l[0]  # a self-loop makes the size-30 class primitive
    assert {((u//8).bit_count(), (u%8).bit_count()) for u in ch[1]} == {(1,1),(1,2),(2,1)}
    expected={
        'HighLife':[1,-1,0,-15,6,-9,72,-63,0,-162,162],
        'Life':[1,-1,-1,-14,6,0,63,-63,0,-81,243],
    }
    for name,edges,lo,hi in [('HighLife',h,265923,265924),('Life',l,270363,270364)]:
        a,p,tr=characteristic(edges,ch[0])
        assert p == expected[name]+[0]*20, (name,p)
        b,q,tr2=characteristic(edges,ch[1])
        assert q==[1,0,0,-27]+[0]*24
        assert tr2[1:16] == [3*3**n if n%3==0 else 0 for n in range(1,16)]
        assert pf_bracket(a,lo,hi)
        counts=[tr[n]+tr2[n] for n in range(3,16)]
        print(name,'S(3..15)=',counts)
        print(name,'recurrent_edges=',[sum(sum(w in set(c) for w in edges[u]) for u in c) for c in ch], 'PF*100000 interval=',(lo,hi))
    print('PASS: same recurrent vertices [30,27]; exact characteristic polynomials; 1-edge difference; rational PF bounds')

if __name__=='__main__':main()
