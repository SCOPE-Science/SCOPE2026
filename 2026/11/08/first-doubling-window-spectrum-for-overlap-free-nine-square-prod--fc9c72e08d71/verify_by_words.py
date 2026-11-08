#!/usr/bin/env python3
"""Exhaustive prefix-DP enumeration for binary overlap-free nine-square words.
No third-party modules. Run: python3 verify_by_words.py
"""
from pathlib import Path

def allowed_extension(w):
    n = len(w)
    for p in range(1, (n-1)//2 + 1):
        if w[n-2*p-1:n-p] == w[n-p-1:n]:
            return False
    return True

def square_suffix(w, h):
    return w[-2*h:-h] == w[-h:]

def decompositions(w, target=9):
    n=len(w)
    solutions=[]
    def visit(i, seq):
        if i==n:
            if len(seq)==target: solutions.append(tuple(seq))
            return
        if len(seq)>=target or i+2*(target-len(seq))>n: return
        for h in range(1,(n-i)//2+1):
            if w[i:i+h]==w[i+h:i+2*h]: visit(i+2*h,seq+[h])
    visit(0,[])
    return solutions

def main():
    records={}
    for line in Path(__file__).with_name('census_96.tsv').read_text().splitlines()[1:]:
        n,s,hs=line.split('\t'); records[s]=tuple(map(int,hs.split(',')))
        assert int(n)==len(s)
    current=[('',(0,))]
    found={}
    checkpoints={}
    for n in range(1,97):
        nxt=[]
        for w,dp in current:
            for a in '01':
                t=w+a
                if not allowed_extension(t): continue
                val=-1000
                if n%2==0:
                    for h in range(1,n//2+1):
                        old=dp[n-2*h]
                        if old>=0 and square_suffix(t,h):val=max(val,old+1)
                z=dp+(val,)
                nxt.append((t,z))
                if val>=9:
                    found[t]=n
        current=nxt
        if n in (24,48,76,86,92,96):
            checkpoints[n]=(len(current),sum(1 for w,d in current if d[-1]>=9))
    assert set(found)==set(records)
    assert len(found)==12
    assert {n:sum(v==n for v in found.values()) for n in set(found.values())}=={48:2,76:2,86:4,92:2,96:2}
    assert checkpoints=={24:(164,0),48:(416,2),76:(722,2),86:(856,4),92:(960,2),96:(1016,2)},checkpoints
    for w,hs in records.items():
        paths=decompositions(w)
        assert paths==[hs],(w,paths,hs)
    print('BY_WORDS_PASS words=12 lengths=48,76,86,92,96 bounds=96',checkpoints)
if __name__=='__main__':main()
