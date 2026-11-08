#!/usr/bin/env python3
"""Reproduce the exact Baum--Sweet nearest-one gap law, independently of the proof."""
from collections import Counter

def val(n):
    if n == 0: return 1
    return int(all(len(part) % 2 == 0 for part in bin(n)[2:].split('1')))

def fibs(u):
    a=[0,1]
    while len(a)<=u:a.append(a[-1]+a[-2])
    return a

def legal_blocks(m):
    if m == 0: return ['']
    out=[]
    if m >= 1: out.extend('1'+s for s in legal_blocks(m-1))
    if m >= 2: out.extend('00'+s for s in legal_blocks(m-2))
    return sorted(out)

def delta(t):
    return (1<<t)+(2 if t%2==0 else 1)

def run(max_length=20):
    fib=fibs(max_length+1)
    prev_max=0
    all_seen=set()
    for L in range(1,max_length+1):
        words=legal_blocks(L-1)
        vals=sorted(int('1'+s,2) for s in words)
        assert len(vals)==fib[L], ('count',L)
        assert all(val(a)==1 for a in vals), ('language',L)
        if L <= 16:
            direct_layer=[a for a in range(1 << (L-1),1 << L) if val(a)]
            assert vals==direct_layer, ('completeness',L)
        actual=Counter(b-a for a,b in zip(vals,vals[1:]))
        predicted=Counter()
        for t in range(max(0,L-2)):
            predicted[delta(t)]+=fib[L-t-2]
        assert actual==predicted, ('gaps',L,actual,predicted)
        if L > 1:
            assert vals[0]-prev_max == (1 if (L-1)%2==0 else 2), ('cross',L)
        prev_max=vals[-1]
        all_seen.update(actual)
    all_seen.update([1,2])
    claimed={1,2}
    for t in range(max_length-2):claimed.add(delta(t))
    assert all_seen==claimed, ('finite spectrum',sorted(all_seen),sorted(claimed))
    limit=1<<18
    direct=[n for n in range(limit) if val(n)]
    assert direct[0:5]==[0,1,3,4,7]
    diffs=set(v-u for u,v in zip(direct,direct[1:]))
    assert diffs==({1,2}|{delta(t) for t in range(16)}), ('direct',sorted(diffs))
    assert all(1 if v-u in claimed else 0 for u,v in zip(direct,direct[1:]))
    assert len(direct)==fib[20] if max_length==20 else True  # F_20 one-indices below 2^18
    print('VERIFY_OK: all binary-length layers 1..%d, %d indices <2^18, %d distinct return gaps' %(max_length,len(direct),len(diffs)))

if __name__=='__main__':run()
