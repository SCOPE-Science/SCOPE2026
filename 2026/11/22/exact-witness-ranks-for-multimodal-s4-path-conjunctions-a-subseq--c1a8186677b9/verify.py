#!/usr/bin/env python3
"""Exact finite checks for modal path-conjunction support ranks.

This script builds finite reflexive/transitive frames, checks reachability,
and verifies sharp leaf independence. It uses only Python's standard library.
"""
from itertools import product
from random import Random


def reduce_runs(w):
    return ''.join(ch for i,ch in enumerate(w) if i == 0 or ch != w[i-1])


def embeds(u, v):
    it = iter(v)
    return all(any(ch == a for ch in it) for a in u)


def minimals(words):
    normalized = sorted(set(map(reduce_runs,words)), key=lambda w: (len(w),w))
    return tuple(w for w in normalized if not any(v != w and embeds(v,w) for v in normalized))


def reduced_words(q,depth):
    a = 'abcdefghijklmnopqrstuvwxyz'[:q]
    out = ['']
    for d in range(1, depth+1):
        out += [''.join(w) for w in product(a,repeat=d)
                if all(w[i]!=w[i+1] for i in range(d-1))]
    return tuple(out)


def frame(words, q):
    # Nodes are words in a prefix trie; one reflexive/transitive R_a per letter.
    P = {''}
    for w in words:
        P.update(w[:i] for i in range(1,len(w)+1))
    nodes = tuple(sorted(P, key=lambda w:(len(w),w)))
    ix = {w:i for i,w in enumerate(nodes)}
    N = len(nodes)
    relations = {a:[1<<i for i in range(N)] for a in 'abcdefghijklmnopqrstuvwxyz'[:q]}
    for w in nodes:
        for a in relations:
            if w+a in ix:
                relations[a][ix[w]] |= 1 << ix[w+a]
    # Compute reachability closure, verify reflexivity and transitivity.
    for a,R in relations.items():
        for k in range(N):
            for i in range(N):
                if (R[i]>>k)&1: R[i] |= R[k]
        assert all((R[i]>>i)&1 for i in range(N))
        assert all((R[i] & (1<<j)) == 0 or (R[j] & ~R[i]) == 0
                   for i in range(N) for j in range(N))
    return nodes,relations


def reach(word, nodes, rel):
    state = 1<<nodes.index('')
    for a in word:
        nxt = 0
        for j in range(len(nodes)):
            if (state>>j)&1: nxt |= rel[a][j]
        state = nxt
    return state


def verify_set(words,q):
    M = minimals(words)
    nodes,rel = frame(M,q)
    marks = sum(1<<nodes.index(w) for w in M)
    # All conjuncts are witnessed by marks.
    assert all(reach(w,nodes,rel)&marks for w in words)
    # For every essential word, deleting its own mark falsifies the formula.
    for w in M:
        mask = marks & ~(1<<nodes.index(w))
        assert not (reach(w,nodes,rel)&mask)
    # Exact embedding/reachability equivalence for all marked end nodes.
    for v in reduced_words(q,max((len(w) for w in M),default=0)):
        reached=reach(v,nodes,rel)
        for w in M:
            assert bool(reached&(1<<nodes.index(w))) == embeds(w,v)
    return len(M),len(nodes)


def run():
    cases=0
    for q,d in [(1,4),(2,3),(3,2)]:
        U=reduced_words(q,d)
        assert len(U)<=10
        for mask in range(1,1<<len(U)):
            words=[u for i,u in enumerate(U) if (mask>>i)&1]
            rank,n=verify_set(words,q)
            assert 1<=rank<=(q*(q-1)**(d-1) if q>=2 else 1)
            cases+=1
    rng=Random(21280)
    U=reduced_words(3,3)
    for _ in range(300):
        words=[u for u in U if rng.randrange(2)]
        if words:
            verify_set(words,3)
            cases+=1
    for q in range(1,5):
        for d in range(1,5):
            U=tuple(w for w in reduced_words(q,d) if len(w)==(1 if q==1 else d))
            rank,n=verify_set(U,q)
            expected=1 if q==1 else q*(q-1)**(d-1)
            assert rank==expected
            if q==3 and d==3: assert (rank,n)==(12,22)
            if q==2 and d==4: assert (rank,n)==(2,9)
            cases+=1
    assert reduce_runs('aaabbbaaccc')=='abac'
    assert embeds('aba','abbaba') and not embeds('aba','ab')
    print('VERIFY_OK cases=%d max_q2=2 q3_d3=12 trie_worlds=22' % cases)

if __name__=='__main__':
    run()
