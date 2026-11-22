#!/usr/bin/env python3
"""Exact rational and exhaustive checks for Motzkin one-deletion coding."""
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

EXPECTED_SOURCES = [1, 2, 4, 9, 21, 51, 127]
EXPECTED_SIZES = [1, 2, 2, 4, 6, 14, 25]
EXPECTED_FRACTIONAL = [Fraction(x) for x in ['1','2','2','4','6','14','382/15']]
EXPECTED_OPTIMA = [1, 1, 3, 8, 75, 28, 142560]
EXPECTED_LAYER_COUNTS = {
  1: [1], 2: [1,1], 3: [1,3], 4: [1,4,2],
  5: [1,5,15], 6: [1,7,2,2], 7: [1,9,11,1440]
}

def words(n):
    def rec(prefix, height):
        if len(prefix) == n:
            if height == 0:
                yield prefix
            return
        yield from rec(prefix+'F',height)
        yield from rec(prefix+'U',height+1)
        if height:
            yield from rec(prefix+'D',height-1)
    return sorted(rec('',0))

def shadow(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def exhaustive_optima(group):
    # Every independent set is a clique in the compatibility graph.
    n=len(group)
    incompatible=[0]*n
    shared=defaultdict(list)
    for i,w in enumerate(group):
        for y in shadow(w):shared[y].append(i)
    for index_list in shared.values():
        for i in index_list:
            for j in index_list:
                if j!=i:incompatible[i]|=1<<j
    full=(1<<n)-1
    compatible=[(full ^ (1<<i)) & ~incompatible[i] for i in range(n)]
    best=0
    count=0
    def bron_kerbosch(size,P,X):
        nonlocal best,count
        if not (P|X):
            if size>best:
                best,count=size,1
            elif size==best:
                count+=1
            return
        if size+P.bit_count()<best:
            return
        U=P|X
        pivot=-1
        pivot_score=-1
        while U:
            b=U & -U
            i=b.bit_length()-1
            U^=b
            score=(P & compatible[i]).bit_count()
            if score>pivot_score:pivot,pivot_score=i,score
        candidates=P & ~compatible[pivot]
        while candidates:
            b=candidates & -candidates
            i=b.bit_length()-1
            candidates^=b
            bron_kerbosch(size+1,P & compatible[i],X & compatible[i])
            P^=b
            X|=b
            if size+P.bit_count()<best:break
    bron_kerbosch(0,full,0)
    return best,count

def main():
    path=Path(__file__).with_name('certificates.json')
    evidence=json.loads(path.read_text(encoding='utf-8'))
    assert set(evidence)==set(map(str,range(1,8)))
    for n in range(1,8):
        W=words(n)
        assert len(W)==EXPECTED_SOURCES[n-1]
        groups=defaultdict(list)
        for w in W:groups[w.count('U')].append(w)
        assert set(map(int,evidence[str(n)]))==set(groups)
        total_integer=0
        total_frac=Fraction(0)
        total_codes=1
        for t in sorted(groups):
            E=evidence[str(n)][str(t)]
            G=groups[t]
            outs=set().union(*(shadow(w) for w in G))
            assert E['source_count']==len(G)
            assert E['output_count']==len(outs)
            S=E['witness']
            assert len(S)==E['integer']==len(set(S))
            assert set(S)<=set(G)
            used=set()
            for w in S:
                assert used.isdisjoint(shadow(w))
                used.update(shadow(w))
            x={w:Fraction(f) for w,f in E['primal'].items()}
            y={v:Fraction(f) for v,f in E['dual'].items()}
            assert set(x)<=set(G) and set(y)<=outs
            assert all(v>=0 for v in x.values()) and all(v>=0 for v in y.values())
            for out in outs:
                assert sum((x.get(w,0) for w in G if out in shadow(w)),Fraction(0))<=1
            for w in G:
                assert sum((y.get(out,0) for out in shadow(w)),Fraction(0))>=1
            P=sum(x.values(),Fraction(0))
            assert P==sum(y.values(),Fraction(0))==Fraction(E['fractional'])
            assert E['integer']<=P<E['integer']+1
            best,number=exhaustive_optima(G)
            assert (best,number)==(E['integer'],EXPECTED_LAYER_COUNTS[n][t]),(n,t,best,number)
            total_integer+=best
            total_frac+=P
            total_codes*=number
        assert (total_integer,total_frac,total_codes)==(
            EXPECTED_SIZES[n-1],EXPECTED_FRACTIONAL[n-1],EXPECTED_OPTIMA[n-1])
    print('VERIFY_OK')

if __name__=='__main__':main()
