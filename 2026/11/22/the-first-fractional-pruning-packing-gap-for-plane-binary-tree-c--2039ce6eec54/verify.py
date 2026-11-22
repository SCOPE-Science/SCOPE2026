#!/usr/bin/env python3
"""Exact verifier for leaf-pruning codes of ordered full binary tree shapes.
Only Python's standard library is needed. All source tree and deletion
incidences are regenerated independently from prefix encodings.
"""
import json
from fractions import Fraction
from pathlib import Path

def parse_bracket(w):
    i = 0
    def rec():
        nonlocal i
        if w[i] == '.':
            i += 1
            return 'L'
        assert w[i] == '('
        i += 1
        a = rec()
        assert w[i] == ','
        i += 1
        b = rec()
        assert w[i] == ')'
        i += 1
        return 'F' + a + b
    p = rec()
    assert i == len(w)
    return p

def all_prefix_full_trees(n):
    result = set()
    def extend(word, slots, forks):
        if slots == 0:
            if forks == n:
                result.add(word)
            return
        if forks < n:
            extend(word+'F', slots+1, forks+1)
        if len(word)-forks < n+1:
            extend(word+'L', slots-1, forks)
    extend('', 1, 0)
    return result

def pruning_prefixes(w):
    # Return all one-terminal reductions by locating every direct leaf child
    # of every fork in a preorder serialization and promoting the sibling.
    reductions = set()
    def subtree(i):
        if w[i]=='L':
            return i+1
        j = subtree(i+1)
        k = subtree(j)
        if w[i+1]=='L':
            reductions.add(w[:i]+w[j:k]+w[k:])
        if w[j]=='L':
            reductions.add(w[:i]+w[i+1:j]+w[k:])
        return k
    assert subtree(0) == len(w)
    return reductions

def rational(s):
    return Fraction(s)

def main():
    data = json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))['lengths']
    table = []
    for n in range(1, 7):
        d=data[str(n)]
        src=[parse_bracket(s) for s in d['source_words']]
        outputs=[parse_bracket(s) for s in d['output_words']]
        assert len(set(src))==len(src)
        assert len(set(outputs))==len(outputs)
        assert set(src)==all_prefix_full_trees(n)
        assert set(outputs)==all_prefix_full_trees(n-1)
        oi={o:i for i,o in enumerate(outputs)}
        incidence=[]
        for t in src:
            ds=pruning_prefixes(t)
            assert ds
            incidence.append(sorted(oi[x] for x in ds))
        assert incidence==d['deletion_incidence']
        N=len(src); K=len(outputs)
        p=[Fraction(0) for _ in src]
        q=[Fraction(0) for _ in outputs]
        for j,v in d['fractional_primal']:
            assert p[j]==0 and Fraction(v)>0
            p[j]=rational(v)
        for i,v in d['fractional_dual']:
            assert q[i]==0 and Fraction(v)>0
            q[i]=rational(v)
        for o in range(K):
            assert sum(p[j] for j in range(N) if o in incidence[j])<=1
        for j in range(N):
            assert sum(q[o] for o in incidence[j])>=1
        assert sum(p)==sum(q)==rational(d['fractional_optimum'])
        code=d['codeword_indices']
        assert len(set(code))==len(code)==d['integer_optimum']
        assert all(0<=j<N for j in code)
        assert len(set.union(*(set(incidence[j]) for j in code)))==sum(len(incidence[j]) for j in code)
        assert len(code)<=sum(q)<len(code)+1
        table.append((n, N, K, len(code), str(sum(q))))
    assert [x[3] for x in table]==[1,1,2,3,7,15]
    assert [x[4] for x in table]==['1','1','2','3','7','205/13']
    for line in table:
        print('n=%s sources=%s outputs=%s integer=%s fractional=%s'%line)
    print('VERIFY_OK')
if __name__=='__main__':main()
