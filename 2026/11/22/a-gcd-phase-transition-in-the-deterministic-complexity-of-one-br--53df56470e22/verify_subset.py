#!/usr/bin/env python3
"""Independent NFA subset traversal and DFA Moore minimization for modular markers."""
from collections import deque, Counter
from math import gcd
from itertools import product

def machine(r,s):
    # Concrete NFA bitsets: C_i are bits [0,r), D_j are [r,r+s).
    full=(1<<(r+s))-1
    def step(mask,c):
        out=0
        for state in range(r+s):
            if not ((mask>>state)&1): continue
            if state<r:
                if c=='a': out |= 1<<((state+1)%r)
                else:
                    out |= 1<<state
                    if state==0: out |= 1<<r
            else:
                j=state-r
                nxt=r+(j+1)%s if c=='a' else state
                out |= 1<<nxt
        return out
    found={1:0}; states=[1]; trans=[]
    for mask in states:
        edges=[]
        for c in 'ab':
            v=step(mask,c)
            if v not in found:
                found[v]=len(states);states.append(v)
            edges.append(found[v])
        trans.append(edges)
    return states, trans, step

def minimize(states, edges, r):
    colors=[bool(m&(1<<r)) for m in states]
    rounds=0
    while True:
        key={}; new=[]
        for i in range(len(states)):
            sig=(colors[i],colors[edges[i][0]],colors[edges[i][1]])
            if sig not in key: key[sig]=len(key)
            new.append(key[sig])
        rounds+=1
        if len(set(new))==len(set(colors)):
            # Stability of number of classes with refinement suffices;
            # each old class is split, no old classes merge.
            return len(set(new)),Counter(Counter(new).values()),rounds
        colors=new

def direct(w,r,s):
    for k,c in enumerate(w):
        if c=='b' and w[:k].count('a')%r==0 and w[k+1:].count('a')%s==0:
            return True
    return False

def main():
    tested=0; words=0; max_reach=0
    for r in range(1,8):
        for s in range(1,8):
            states,edges,step=machine(r,s)
            g=gcd(r,s)
            R=r*(2**(s//g)); M=r*(2**(s//g)-1)+g
            got,blocks,rounds=minimize(states,edges,r)
            assert len(states)==R,(r,s,'reachable',len(states),R)
            assert got==M,(r,s,'minimal',got,M)
            expected_blocks=Counter()
            expected_blocks[1]+=M-g
            expected_blocks[r//g]+=g
            assert blocks == expected_blocks, (r,s,'blocks',blocks,expected_blocks)
            assert all((m&((1<<r)-1)).bit_count()==1 for m in states)
            if r<=4 and s<=4:
                for n in range(0,9):
                    for seq in product('ab', repeat=n):
                        w=''.join(seq); mask=1
                        for c in w: mask=step(mask,c)
                        assert bool(mask&(1<<r))==direct(w,r,s),(r,s,w)
                        words+=1
            tested+=1; max_reach=max(max_reach,len(states))
    print('PASS independent explicit-NFA subset BFS and partition refinement')
    print('parameter pairs:',tested,'r,s in [1,7]')
    print('largest reachable subset DFA:',max_reach)
    print('direct word checks:',words)
    print('all reachable sizes, minimized sizes and quotient block multiplicities agree with formula')

if __name__=='__main__': main()
