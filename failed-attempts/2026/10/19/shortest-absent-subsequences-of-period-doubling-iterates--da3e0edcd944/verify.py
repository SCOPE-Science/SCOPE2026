#!/usr/bin/env python3
"""Reproduce exact shortest absent subsequences for period-doubling iterates.
Pure standard-library finite checks; proof of all lengths is in RESULT.md.
"""
from itertools import product

def subsequence(s, w):
    pos = iter(w)
    return all(any(c == b for c in pos) for b in s)

def pd(m):
    w='0'
    for _ in range(m):
        w=''.join('01' if c=='0' else '00' for c in w)
    return w

def sas_direct(w, length):
    return [''.join(t) for t in product('01',repeat=length)
            if not subsequence(t,w)]

def missing_binary_count(w, length):
    # A deterministic subsequence automaton state is the next unread index;
    # a transition to len(w)+1 is the absent sink. Count all words.
    n=len(w)
    nxt=[[n+1,n+1] for _ in range(n+2)]
    for i in range(n-1,-1,-1):
        nxt[i]=nxt[i+1].copy()
        nxt[i][int(w[i])]=i+1
    dp={0:1}; count_absent=0
    for _ in range(length):
        np={}
        for state, mult in dp.items():
            for bit in (0,1):
                target=nxt[state][bit]
                np[target]=np.get(target,0)+mult
        dp=np
    return dp.get(n+1,0)

def main():
    for m in range(2,14):
        w=pd(m); k=w.count('1'); wanted=(2**m-(-1)**m)//3
        assert k==wanted
        assert not '11' in w
        assert (w.endswith('00') if m%2==0 else w.endswith('1000101'))
        sas_count=missing_binary_count(w,k+1)
        expect=['1'*(k+1)] if m%2==0 else ['1'*(k-1)+'00','1'*k+'0','1'*(k+1)]
        assert sas_count==len(expect),(m,sas_count,len(expect))
        assert missing_binary_count(w,k)==0
        assert all(not subsequence(s,w) for s in expect)
        if m<=5:
            assert sorted(sas_direct(w,k+1))==sorted(expect)
        print('m=%d length=%d K=%d shortest_absent_length=%d count=%d' % (m,len(w),k,k+1,sas_count))
    print('VERIFY_OK')

if __name__=='__main__': main()
