#!/usr/bin/env python3
"""Independently compare an exact rotor-entry formula to the full finite state map.
Usage: python3 verify.py
The pointer is an index into each vertex's fixed neighbour ordering;
at an update it advances by one modulo degree before the walker moves.
"""
from itertools import product
from collections import Counter

def graph(k,L):
    adj=[[1+i*L for i in range(k)]]
    for i in range(k):
        for d in range(1,L+1):
            v=1+i*L+(d-1)
            adj.append([0 if d==1 else v-1]+([v+1] if d<L else []))
    return adj

def cycle_entry(k,L,hub,mask):
    adj=graph(k,L)
    pointer=[hub]+list(mask)
    # First vertex on every arm's base-to-tip path is internal, and leaf rotors are fixed.
    at=0
    visited={}
    steps=0
    while (at,tuple(pointer)) not in visited:
        visited[at,tuple(pointer)]=steps
        pointer[at]=(pointer[at]+1)%len(adj[at])
        at=adj[at][pointer[at]]
        steps+=1
    entrance=visited[at,tuple(pointer)]
    period=steps-entrance
    return entrance,period

def direct_formula(k,L,hub,mask):
    bad=[]
    for i in range(k):
        bad.append([d for d in range(1,L) if mask[i*L+d-1]==1])
    B=max(map(len,bad))
    if B==0:return 0
    order=[(hub+j+1)%k for j in range(k)]
    last=max(j for j,i in enumerate(order) if len(bad[i])==B)
    t=0
    for j,i in enumerate(order):
        if j==last:
            t+=2*sum(bad[i][:B-1])+bad[i][B-1]
        else:
            count=B if j<last else B-1
            t+=2*(sum(bad[i][:min(len(bad[i]),count)])
                  +L*max(0,count-len(bad[i])))
    return t

def run():
    tested=0
    for k,L in [(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3)]:
        stats=Counter()
        for hub in range(k):
            for choices in product((0,1),repeat=k*(L-1)):
                # Insert deterministic pointers for leaves; they have degree one.
                mask=[]
                for i in range(k):
                    mask.extend(choices[i*(L-1):(i+1)*(L-1)])
                    mask.append(0)
                actual,period=cycle_entry(k,L,hub,mask)
                predicted=direct_formula(k,L,hub,mask)
                assert actual==predicted,(k,L,hub,choices,actual,predicted)
                assert period==2*k*L,(k,L,hub,choices,period)
                stats[actual]+=1;tested+=1
        maximum=(L-1)*((2*k-1)*L-1)
        assert max(stats)==maximum,(k,L,max(stats),maximum)
        assert stats[maximum]==k,(k,L,stats[maximum],k)
        assert sum(stats.values())==k*(1<< (k*(L-1)))
        print('PASS k=%d L=%d states=%d max=%d extremizers=%d period=%d' % (
            k,L,sum(stats.values()),maximum,stats[maximum],2*k*L))
    print('PASS TOTAL STATES:',tested)
if __name__=='__main__':run()
