"""Two finite checking methods for cyclic-run subsequence-universality formulas.

Run with: python3 verify.py
Requires only Python 3 standard library.
"""
from itertools import product
from collections import Counter

def scan_arches(w, q):
    seen = set()
    count = 0
    for letter in w:
        seen.add(letter)
        if len(seen) == q:
            count += 1
            seen.clear()
    return count

def occurs_subsequence(pattern, w):
    j=0
    for a in w:
        if j < len(pattern) and a == pattern[j]:
            j+=1
    return j == len(pattern)

def brute_index(w, q):
    level=0
    while all(occurs_subsequence(v, w) for v in product(range(q), repeat=level+1)):
        level+=1
    return level

def formula(lengths, k, off):
    q=len(lengths)
    if 1 in lengths:
        return k
    return k+(k-1)//(q-1) + (1 if off>0 and k%(q-1)==0 else 0)

def test():
    cases=0
    phase_comparisons=0
    brute_checks=0
    for q, mx, max_k in ((3,4,9),(4,4,8),(5,3,8),(6,3,7)):
        for lengths in product(range(1,mx+1), repeat=q):
            period=tuple(i for i,a in enumerate(lengths) for _ in range(a))
            p=len(period)
            for k in range(1,max_k+1):
                vals=[]
                for pos in range(p):
                    word=(period[pos:]+period[:pos])*k
                    off=pos-sum(lengths[:period[pos]])
                    actual=scan_arches(word,q)
                    predicted=formula(lengths,k,off)
                    assert actual==predicted, (lengths,k,pos,off,actual,predicted)
                    vals.append(actual)
                    phase_comparisons+=1
                expected_best=k if 1 in lengths else k+k//(q-1)
                assert max(vals)==expected_best, (lengths,k,vals,expected_best)
                if 1 not in lengths and k%(q-1)==0:
                    assert vals.count(expected_best)==p-q
                    assert vals.count(expected_best-1)==q
                else:
                    assert all(v==expected_best for v in vals)
                cases+=1
    for q, mx, kmax in ((3,3,3),(4,2,2)):
        for lengths in product(range(1,mx+1), repeat=q):
            period=tuple(i for i,a in enumerate(lengths) for _ in range(a))
            for k in range(1,kmax+1):
                for pos in range(len(period)):
                    word=(period[pos:]+period[:pos])*k
                    got=brute_index(word,q)
                    assert got==scan_arches(word,q), (lengths,k,pos,got)
                    brute_checks+=1
    print(f'PASS {cases} parameter/repetition cases; {phase_comparisons} phase-index comparisons; {brute_checks} direct full-spectrum cross-checks')

if __name__=='__main__': test()
