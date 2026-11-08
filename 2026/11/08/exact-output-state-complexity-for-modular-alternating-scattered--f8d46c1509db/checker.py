#!/usr/bin/env python3
"""Reproducibility checks for modular scattered-pattern 010 output automata."""
from collections import deque
from itertools import product
from math import gcd

def step(s,ch,m):
    a,b,c=s
    if ch=='0':return ((a+1)%m,b,(c+b)%m)
    return (a,(b+a)%m,c)

def run(s,w,m):
    for ch in w:s=step(s,ch,m)
    return s

def naive_010(w):
    ans=0
    for i,x in enumerate(w):
        if x!='0':continue
        for j in range(i+1,len(w)):
            if w[j]!='1':continue
            for k in range(j+1,len(w)):
                if w[k]=='0':ans+=1
    return ans

def reachable(m):
    q=deque([(0,0,0)]); seen={(0,0,0)}
    while q:
        s=q.popleft()
        for ch in '01':
            t=step(s,ch,m)
            if t not in seen:seen.add(t);q.append(t)
    return seen

def main():
    word_tests=0;reach_tests=0;dist_tests=0;witness_tests=0;minimization_cases=0
    for n in range(14):
        for tup in product('01',repeat=n):
            w=''.join(tup)
            exact=naive_010(w)
            for m in range(2,11):
                a,b,c=run((0,0,0),w,m)
                assert a==w.count('0')%m
                assert c==exact % m
                assert b==sum(w[i]=='0' and w[j]=='1' for i in range(n) for j in range(i+1,n))%m
                word_tests+=1
    for m in range(2,24):
        S=reachable(m)
        assert len(S)==m**3//gcd(m,2)
        assert all((c-(a-1)*b)%gcd(m,2)==0 for a,b,c in S)
        # Outputs after empty, '0', and '10' distinguish distinct triples.
        sigs={(s[2],run(s,'0',m)[2],run(s,'10',m)[2]) for s in S}
        assert len(sigs)==len(S)
        dist_tests+=len(S)
        reach_tests+=1
    # Independent fixed-point refinement of Moore-output equivalence.
    for m in range(2,11):
        S=reachable(m)
        blocks={s:s[2] for s in S}
        while True:
            signatures={s:(blocks[s],blocks[step(s,'0',m)],blocks[step(s,'1',m)]) for s in S}
            colors={v:i for i,v in enumerate(sorted(set(signatures.values())))}
            updated={s:colors[signatures[s]] for s in S}
            if len(set(updated.values()))==len(set(blocks.values())):
                assert len(set(updated.values()))==len(S)
                break
            blocks=updated
        minimization_cases+=1
    # Positive-word representatives of inverse generators; check C,D on all states.
    for m in range(2,9):
        C='01'+'0'*(m-1)+'1'*(m-1)
        D=C+'0'+C*(m-1)+'0'*(m-1)
        for s in reachable(m):
            a,b,c=s
            assert run(s,C,m)==(a,(b+1)%m,(c-a-1)%m)
            assert run(s,D,m)==(a,b,(c+2)%m)
            witness_tests+=2
        for a in range(m):
            for b in range(m):
                for t in range(m//gcd(m,2)):
                    word='0'*a + C*b + D*t
                    expected=(a,b,(-b*(a+1)+2*t)%m)
                    assert run((0,0,0),word,m)==expected
                    witness_tests+=1
    print('PASS',{'word_count_checks':word_tests,'reachable_moduli':reach_tests,
                  'distinguishable_state_checks':dist_tests,
                  'generator_and_witness_checks':witness_tests,
                  'independent_moore_minimizations':minimization_cases})
if __name__=='__main__':main()
