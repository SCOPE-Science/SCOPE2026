"""Independent finite experiments for directed height-two parent-edge structures.

Use: python check_pebble_refinement.py
Each structure has f(root)=root, f(middle)=root, f(leaf)=middle;
only the binary relation E(x,y) iff f(x)=y is available to logic.
This script computes stable counting-free k-pebble colors on all partial
k-tuples jointly across a finite sample; it does not prove the infinite claim.
"""
import itertools
import json
from collections import Counter


def structure(degrees):
    f = [0]
    mids = []
    for _ in degrees:
        mids.append(len(f)); f.append(0)
    for parent, d in zip(mids, degrees):
        f.extend([parent] * d)
    return tuple(f)


def atomic(f, t):
    return tuple((i, j, t[i] == t[j], f[t[i]] == t[j], f[t[j]] == t[i])
                 for i in range(len(t)) if t[i] >= 0
                 for j in range(i, len(t)) if t[j] >= 0)


def stable_empty_colors(structures, k):
    tables = [list(itertools.product(range(-1,len(f)), repeat=k)) for f in structures]
    indices = [{t:i for i,t in enumerate(tab)} for tab in tables]
    dictionary = {}
    old = []
    for f, table in zip(structures, tables):
        row = []
        for t in table:
            atom = atomic(f,t)
            row.append(dictionary.setdefault(atom,len(dictionary)))
        old.append(row)
    for rounds in range(1, 100):
        signatures = {}; new = []
        for f, table, lookup, colors in zip(structures, tables, indices, old):
            row = []
            for i,t in enumerate(table):
                continuation = tuple(frozenset(colors[lookup[t[:p]+(v,)+t[p+1:]]]
                                                for v in range(len(f))) for p in range(k))
                key = (colors[i], continuation)
                row.append(signatures.setdefault(key,len(signatures)))
            new.append(row)
        if new == old:
            return [r[0] for r in new], rounds, len(signatures)
        old = new
    raise AssertionError('refinement did not stabilize')


def predicted(degrees,k):
    if k==1:return (int(bool(degrees)),)
    if k==2:
        n0=sum(x==0 for x in degrees)
        npos=sum(x>0 for x in degrees)
        return (min(n0,2),min(npos,2),min(sum(degrees),2))
    c=Counter(min(x,k) for x in degrees)
    return tuple(min(c[j],k) for j in range(k+1))


def main():
    all_degree_lists=[()] + [t for n in range(1,5)
        for t in itertools.combinations_with_replacement(range(5),n)
        if 1+n+sum(t)<=11]
    results=[]
    for k,cutoff in [(1,11),(2,11),(3,8),(4,7)]:
        choices=[d for d in all_degree_lists if len(structure(d))<=cutoff]
        colors, rounds, count=stable_empty_colors([structure(d) for d in choices],k)
        signatures=[predicted(d,k) for d in choices]
        pair_count=0
        for i in range(len(choices)):
            for j in range(i):
                pair_count+=1
                assert (colors[i]==colors[j]) == (signatures[i]==signatures[j]), (
                    k,choices[i],choices[j],colors[i],colors[j],signatures[i],signatures[j])
        results.append(dict(k=k, structures=len(choices), comparisons=pair_count,
                            refinement_rounds=rounds, stable_state_colors=count,
                            distinct_sentence_theories=len(set(colors)), mismatches=0))
    print(json.dumps({'method':'joint stable set-based k-pebble refinement',
                      'results':results},indent=2))

if __name__=='__main__':main()
