#!/usr/bin/env python3
"""Exact finite proof for binary guarded (2,infinity)-RLL one-deletion code threshold.
Run: python3 verify.py
Only Python's standard library is used.
"""
import json
from pathlib import Path


def admissible(n):
    # Every 1 is isolated; every zero gap, including the two boundary gaps,
    # has at least two zeros.  The all-zero word is admitted.
    ans=[]
    for value in range(1 << n):
        w=format(value, '0%db'%n)
        if all(len(gap) >= 2 for gap in w.split('1')):
            ans.append(w)
    return ans


def deletion_shadow(word):
    return frozenset(word[:j]+word[j+1:] for j in range(len(word)))


def check_code(words, n):
    assert len(words)==len(set(words)) and words
    allowed=set(admissible(n))
    assert all(len(w)==n and w in allowed for w in words)
    seen=set()
    for word in words:
        s=deletion_shadow(word)
        assert not seen.intersection(s),('collision',word)
        seen.update(s)


def bound_maximum_16():
    W=admissible(16)
    shadows=[deletion_shadow(w) for w in W]
    N=len(W)
    # Edge = compatible pair; optimal deletion-correcting codes are cliques.
    edges=[]
    for i in range(N):
        mask=0
        for j in range(N):
            if i!=j and shadows[i].isdisjoint(shadows[j]):
                mask |= 1 << j
        edges.append(mask)
    assert N==129
    assert all((edges[i]>>j)&1 == (edges[j]>>i)&1 for i in range(N) for j in range(N))

    known=json.loads(Path(__file__).with_name('witnesses.json').read_text())['n16']
    check_code(known,16)
    best=len(known)
    visits=0

    def greedily_color(P):
        # Each color class is an independent set in compatibility graph.
        # Therefore no clique contains two vertices of the same color.
        order=[]; bounds=[]; color=0
        while P:
            color += 1
            independent_candidates=P
            while independent_candidates:
                vbit=independent_candidates & -independent_candidates
                v=vbit.bit_length()-1
                order.append(v);bounds.append(color)
                P &= ~vbit
                independent_candidates &= ~vbit
                independent_candidates &= ~edges[v]
        return order,bounds

    def search(depth,P):
        nonlocal visits,best
        visits += 1
        order,bounds=greedily_color(P)
        for k in range(len(order)-1,-1,-1):
            if depth + bounds[k] <= best:
                return
            v=order[k]
            remaining=P & edges[v]
            if remaining:
                search(depth+1,remaining)
            else:
                best=max(best,depth+1)
            P &= ~(1<<v)
    search(0,(1<<N)-1)
    assert best==14, ('unexpected optimum',best)
    return {'admissible_words':N,'search_nodes':visits,'maximum':best}


def main():
    data=json.loads(Path(__file__).with_name('witnesses.json').read_text())
    check_code(data['n16'],16)
    check_code(data['n17'],17)
    stats=bound_maximum_16()
    assert len(data['n16'])==14 and len(data['n17'])==16
    # Exact prefix-embedding argument proves all n<16 impossible for 16
    # messages by appending zeros to a hypothesized code and then using the
    # length-16 maximum.  Nonempty shorter lengths with guarded runs are okay.
    print('EXACT_PROOF_OK n16_max=14 n17_code=16',stats)

if __name__=='__main__':main()
