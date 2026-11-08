#!/usr/bin/env python3
"""Exhaustive arithmetic certificate for power domination in Q_5."""
from itertools import combinations, permutations
from collections import Counter,deque
from hashlib import sha256

def nbrs(n):
    return [sum(1 << (v ^ (1 << j)) for j in range(n)) for v in range(1 << n)]

def powers(n, t, ng):
    N = 1 << n
    mask = 0
    for v in t:
        mask |= 1 << v | ng[v]
    while True:
        nxt = mask
        for v in range(N):
            if mask >> v & 1:
                missing = ng[v] & ~mask
                if missing and missing & (missing-1) == 0:
                    nxt |= missing
        if nxt == mask:
            return mask == (1 << N) - 1
        mask = nxt

def permute_vertex(v,pi):
    return sum((1 << pi[i]) for i in range(5) if v >> i & 1)

def orbit(S):
    O=set()
    for pi in permutations(range(5)):
        perm=[permute_vertex(v,pi) for v in S]
        for t in range(32):
            O.add(tuple(sorted(v ^ t for v in perm)))
    return O

def main():
    ng=nbrs(5)
    assert all(not powers(5,s,ng) for k in (1,2,3) for s in combinations(range(32),k))
    states=[t for t in combinations(range(32),4) if powers(5,t,ng)]
    st=set(states)
    assert len(states)==3600
    rest=st.copy(); os=[]
    while rest:
        rep=min(rest)
        orb=orbit(rep)
        assert orb <= st
        rest -= orb
        os.append((rep,orb))
    assert len(os)==6
    links={s:set() for s in states}
    slides=0
    for s in states:
        for u in s:
            for v in range(32):
                if v in s:continue
                t=tuple(sorted((set(s)-{u})|{v}))
                if t in st:
                    links[s].add(t)
                    if (v ^ u).bit_count()==1:slides+=1
    assert slides==0
    assert sum(map(len,links.values()))==70400
    assert all(len(links[s])==len({t for t in links[s]}) for s in states)
    print('Q5 minimum size 4; state count',len(states), 'TJ edges',sum(map(len,links.values()))//2,'TS edges',slides//2)
    print('ordered orbit reps size TJ-degree TJ-ecc distance-multiset')
    freqs=Counter(); degree_hist=Counter(); eccentricities=[]; observed_rows=[]
    for s,O in os:
        ds={s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for v in links[u]:
                if v not in ds:
                    ds[v]=ds[u]+1;q.append(v)
        assert len(ds)==3600
        ecc=max(ds.values())
        ecc_entries=(len(O),ecc)
        eccentricities.append(ecc_entries)
        degrees={len(links[u]) for u in O}
        assert len(degrees)==1
        degree=degrees.pop()
        degree_hist[degree]+=len(O);freqs[ecc]+=len(O)
        dists=sorted((a^b).bit_count() for a,b in combinations(s,2))
        print(s,len(O),degree,ecc,dists)
        observed_rows.append((s,len(O),degree,ecc))
    assert observed_rows == [
        ((0,1,14,15),160,16,5),
        ((0,1,14,23),960,22,5),
        ((0,1,14,30),320,14,5),
        ((0,3,13,14),240,16,6),
        ((0,3,13,22),960,22,6),
        ((0,3,13,28),960,18,6)]
    assert sorted([len(O) for s,O in os])==[160,240,320,960,960,960]
    assert freqs == {5:1440,6:2160}
    assert degree_hist == {14:320,16:400,18:960,22:1920}
    print('TJ degree histogram',sorted(degree_hist.items()))
    print('TJ eccentricity histogram',sorted(freqs.items()))
    print('TJ radius',min(freqs),'diameter',max(freqs))
    n4=nbrs(4)
    a4=[t for t in combinations(range(16),2) if powers(4,t,n4)]
    assert len(a4)==32
    assert all((x^y).bit_count()==3 for x,y in a4)
    n3=nbrs(3)
    a3=[t for t in combinations(range(8),2) if powers(3,t,n3)]
    assert len(a3)==28
    print('Q4 states 32, all distance-3 pairs and TS-frozen; Q3 states 28')
    print('complete')
if __name__=='__main__':main()
