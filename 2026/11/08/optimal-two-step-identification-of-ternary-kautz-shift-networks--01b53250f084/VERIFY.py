#!/usr/bin/env python3
"""Standalone finite verification of optimal two-step Kautz identification."""
from itertools import product
from collections import defaultdict

def words(n):
    return [''.join(w) for w in product('012', repeat=n)
            if all(w[i]!=w[i+1] for i in range(n-1))]

def positive_step(a,b):
    assert a != b
    return (int(b)-int(a))%3 == 1

def in_code(w):
    n=len(w)
    p = 0 if n%2 else 1
    return positive_step(w[p], w[p+1]) == positive_step(w[-2],w[-1])

def inball(v):
    t=v[:-2]
    P1={a+v[:-1] for a in '012' if a!=v[0]}
    P2={b+a+t for a in '012' if a!=v[0] for b in '012' if b!=a}
    return {v}|P1|P2

def decode(sig,n):
    assert len(sig)>=2
    groups=defaultdict(list)
    if n%2:
        for w in sig: groups[w[-(n-2):]].append(w)
        heavy=[x for x in groups if len(groups[x])==2]
        assert len(heavy)==1, (n, sig,groups)
        t=heavy[0]
        first=[w for w in sig if w[1:-1]==t]
        assert len(first)==1,(n,sig,first,t)
        pref=first[0][1:]
    else:
        for w in sig: groups[w[1:]].append(w)
        pairs=[s for s,c in groups.items() if len(c)==2]
        assert len(pairs) in (1,2),(n,sig,groups)
        if len(pairs)==2:
            ordered=[(a,b) for a in pairs for b in pairs if a!=b and a[1:]==b[:-1]]
            assert len(ordered)==1,(n,sig,pairs)
            pref=ordered[0][1]
        else:
            t=pairs[0][1:]
            last=[b for b in '012' if b!=t[-1] and
                  positive_step(t[-1],b)!=positive_step(t[0],t[1])]
            assert len(last)==1,(n,sig,t)
            pref=t+last[0]
    candidates=[pref+a for a in '012' if a!=pref[-1]]
    chosen=[v for v in candidates if in_code(v)]
    assert len(chosen)==1, (n,sig,candidates)
    return chosen[0] if chosen[0] in sig else [v for v in candidates if v!=chosen[0]][0]

def run():
    for n in range(3,12):
        vs=words(n)
        assert len(vs)==3*2**(n-1)
        C={v for v in vs if in_code(v)}
        assert len(C)==len(vs)//2
        signatures={v:frozenset(inball(v)&C) for v in vs}
        assert all(signatures.values())
        assert len(set(signatures.values()))==len(vs)
        assert all(decode(signatures[v],n)==v for v in vs)
        assert all(not in_code(v) for v in vs if all(v[i]==v[i+2] for i in range(n-2)))
        if n<=7:
            for p in set(v[:-1] for v in vs):
                a,b=[v for v in vs if v[:-1]==p]
                # Every identifying code must use a member of each disjoint sibling pair.
                assert inball(a)^inball(b) <= {a,b}
        print(f'n={n}: vertices={len(vs)} sensors={len(C)}, distinct nonempty signatures and decoded vertices OK')
    # Radius two fails to identify the six vertices of K(2,2) even with all sensors.
    vs=words(2)
    balls={v:{w for w in vs if w==v or w[1:]==v[:-1] or any(y[1:]==v[:-1] and w[1:]==y[:-1] for y in vs)} for v in vs}
    assert len(set(map(frozenset,balls.values())))<len(vs)
    print('n=2: two-step identification impossible (twin balls)')
    print('VERIFY_OK')

if __name__=='__main__':run()
