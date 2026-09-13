import sys; sys.path.insert(0,'.'); import json as J, time
sys.setrecursionlimit(100000)
from itertools import combinations
from pipeline2 import expand, pasches_limit, switch, maybe_iso, sig
from collections import Counter
asg='000111222'
Fof=[int(c) for c in asg]
recs=J.load(open('minsys.json'))
for idx,rec in enumerate(recs[:3]):
    mix=[tuple(t) for t in rec['mix']]; p3=[tuple(t) for t in rec['p3']]
    B=expand(Fof,mix,p3)
    P=pasches_limit(B,100)
    print('=== system',idx,'npasch=',len(P))
    for (s6,inside) in P:
        inv = set(sig(x) for x in s6)==set(s6)
        opp=switch(B,s6,inside)
        B2=(B-set(inside))|set(opp)
        n2=len(pasches_limit(B2,100))
        print('  6-set',s6,'sigINV=',inv,'mate_pasch=',n2)
    # twin test on every Pasch: full twin = switch at that Pasch gives iso system
    for (s6,inside) in P[:12]:
        opp=switch(B,s6,inside)
        B2=(B-set(inside))|set(opp)
        if len(pasches_limit(B2,3))!=len(P):
            continue
        m=maybe_iso(B,B2)
        print('  twin-candidate 6-set',s6,'iso=',bool(m))
