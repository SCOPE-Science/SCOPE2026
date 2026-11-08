#!/usr/bin/env python3
"""Direct finite comparison of the monotone-gap Lyndon subsequence formula."""
from itertools import combinations_with_replacement

def word(gs):
    return '1' + ''.join('0'*g+'1' for g in gs)

def prediction(gs):
    S = sum(gs)
    prefix = 0
    t = len(gs)
    for j,g in enumerate(gs,1):
        prefix += g
        if prefix > gs[-1]:
            t = j
            break
    witness = '0'*sum(gs[:t]) + '1' + ''.join('0'*g+'1' for g in gs[t:])
    return S+len(gs)+1-t,witness,t

def all_subseq(s):
    a={''}
    for c in s:
        a |= {x+c for x in a}
    return a

def lyndon(s):
    return bool(s) and all(s < s[j:] for j in range(1,len(s)))

def test():
    counts = {}
    witness_count=0
    for k in range(1,6):
        n=0
        for gs in combinations_with_replacement(range(1,8),k):
            w=word(gs)
            if len(w)>18:
                continue
            expected,witness,t=prediction(gs)
            assert lyndon(witness),(gs,witness)
            assert len(witness)==expected
            assert witness in all_subseq(w)
            actual=max(map(len,filter(lyndon,all_subseq(w))))
            assert actual==expected,(gs,actual,expected)
            n+=1
            witness_count+=1
        counts[k]=n
    print('PASS direct brute-force Lyndon subsequences:',sum(counts.values()),'words; by number of gaps:',counts)
    print('PASS direct suffix Lyndon witness and exact length:',witness_count,'cases')
    # Further exact parametric examples that do not need brute enumeration.
    for k in range(2,33):
        gs=list(range(1,k+1))
        n,w,t=prediction(gs)
        assert t==next(j for j in range(1,k+1) if j*(j+1)//2>k)
        assert len(w)==n and lyndon(w)
        const=[3]*k
        n,w,t=prediction(const)
        assert t==2 and len(w)==n and lyndon(w)
        if k <= 11:
            geom=[2**j for j in range(k)]
            n,w,t=prediction(geom)
            assert t==k and len(w)==n and lyndon(w)
    print('PASS triangular, constant and geometric leading block formula:',31*2+10,'families')

if __name__=='__main__':
    test()
