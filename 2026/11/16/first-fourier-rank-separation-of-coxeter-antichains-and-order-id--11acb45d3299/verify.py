#!/usr/bin/env python3
"""Exact finite Fourier comparison for positive-root poset antichains and ideals.

Run with Python 3.9+, standard library only. Writes spectrum.csv on request.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
import csv
import sys

EXPECTED = {
    "A1": (1, 2, (1, 1), (1, 1)),
    "A2": (3, 5, (0, 0), (1, 1)),
    "A3": (6, 14, (18, 18), (Fraction(51,16), Fraction(51,16))),
    "A4": (10, 42, (213, 214), (Fraction(3819,512), Fraction(1901,256))),
    "D4": (12, 50, (802, 824), (Fraction(10053,1024), Fraction(1981,256))),
}

def positive_roots(label):
    if label.startswith('A'):
        rank=int(label[1:])
        return sorted({tuple(int(i <= k < j) for k in range(rank))
                       for i in range(rank) for j in range(i+1, rank+1)})
    if label=='D4':
        roots=[]
        for i,j in combinations(range(4),2):
            for sign in (-1,1):
                vector=[0]*4
                vector[i],vector[j]=1,sign
                v1,v2,v3,v4=vector
                nums=(2*v1, 2*(v1+v2), v1+v2+v3-v4, v1+v2+v3+v4)
                assert all(z%2==0 for z in nums)
                cs=tuple(z//2 for z in nums)
                assert all(z>=0 for z in cs)
                # Verify reconstruction in simple-root basis.
                a,b,c,d=cs
                assert (a,-a+b,-b+c+d,-c+d)==tuple(vector)
                roots.append(cs)
        return sorted(roots)
    raise ValueError(label)

def below(a,b):
    return all(x<=y for x,y in zip(a,b))

def support_families(roots):
    k=len(roots)
    low=[]; compare=[]
    for i,a in enumerate(roots):
        low.append(sum(1<<j for j,b in enumerate(roots) if below(b,a)))
        compare.append(sum(1<<j for j,b in enumerate(roots)
                           if i!=j and (below(a,b) or below(b,a))))
    # Independent antichain backtracking and direct validity checks.
    antichains=[0]
    for i in range(k):
        antichains += [s|(1<<i) for s in antichains if (s&compare[i])==0]
    assert len(set(antichains))==len(antichains)
    # Maximal-element-to-ideal bijection.
    ideals=[0]*len(antichains)
    for idx,s in enumerate(antichains):
        t=0
        for i in range(k):
            if s>>i&1:t|=low[i]
        ideals[idx]=t
    assert len(set(ideals))==len(antichains)
    # Independently verify both families by checking all Boolean masks.
    candidate_anti=[s for s in range(1<<k) if all(not(s&compare[i])
                      for i in range(k) if s>>i&1)]
    candidate_ideal=[s for s in range(1<<k) if all((s&low[i])==low[i]
                      for i in range(k) if s>>i&1)]
    assert set(antichains)==set(candidate_anti)
    assert set(ideals)==set(candidate_ideal)
    return set(antichains),set(ideals)

def hadamard(a):
    a=list(a);n=len(a);h=1
    while h<n:
        for st in range(0,n,2*h):
            for j in range(st,st+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def direct_fourier(support, n):
    return [sum(1 if ((x&frequency).bit_count()%2)==0 else -1
                for x in support) for frequency in range(n)]

def analyze(label, roots, support):
    N=1<<len(roots)
    f=hadamard(int(i in support) for i in range(N))
    # A different algorithm evaluates all character sums directly.
    assert f==direct_fourier(support,N)
    assert f[0]==len(support)
    assert sum(z*z for z in f)==N*len(support)
    spec=Counter(f)
    E={i for i,w in enumerate(f) if w!=0}
    H=hadamard(int(i in E) for i in range(N))
    assert H[0]==len(E)
    assert sum(z*z for z in H)==N*len(E)
    norm=Fraction(sum(abs(z) for z in H),N)
    return dict(label=label, spec=spec, zeros=spec[0], rank=len(E), norm=norm, freqs=f)

def triality_orbits(roots, freqs):
    find={v:i for i,v in enumerate(roots)}
    perms=[]
    for p in permutations((0,2,3)):
        m={0:p[0],1:1,2:p[1],3:p[2]}
        # New coefficient at position m[i] equals old coefficient at position i.
        q=[]
        for c in roots:
            c2=[0]*4
            for old,new in m.items():c2[new]=c[old]
            q.append(find[tuple(c2)])
        assert sorted(q)==list(range(12))
        perms.append(q)
    def act(mask, p):
        return sum(1<<p[i] for i in range(12) if mask>>i&1)
    assert all(freqs[act(s,p)]==freqs[s] for s in range(4096) for p in perms)
    zeros={s for s in range(4096) if freqs[s]==0}
    sizes=Counter()
    while zeros:
        s=min(zeros)
        orbit={act(s,p) for p in perms}
        assert orbit <= zeros
        sizes[len(orbit)]+=1
        zeros-=orbit
    return sizes

def main():
    entries=[]
    for label, expected in EXPECTED.items():
        roots=positive_roots(label)
        ant,ide=support_families(roots)
        assert (len(roots),len(ant))==expected[:2]
        left=analyze(label,roots,ant)
        right=analyze(label,roots,ide)
        assert (left['zeros'],right['zeros'])==expected[2]
        assert (left['norm'],right['norm'])==expected[3]
        assert left['rank']==(1<<len(roots))-left['zeros']
        assert right['rank']==(1<<len(roots))-right['zeros']
        if label=='D4':
            assert triality_orbits(roots,left['freqs'])==Counter({1:10,3:64,6:100})
            assert triality_orbits(roots,right['freqs'])==Counter({1:8,3:76,6:98})
        for family,r in [('antichains',left),('ideals',right)]:
            for multiplier,count in sorted(r['spec'].items()):
                entries.append((label,family,multiplier,count))
        print(label, 'antichains/ideals',len(ant), 'zeros',left['zeros'],right['zeros'],
              'rank',left['rank'],right['rank'], 'endpoint norms',left['norm'],right['norm'])
    if '--csv' in sys.argv:
        with open('spectrum.csv','w',newline='',encoding='utf-8') as f:
            w=csv.writer(f,lineterminator='\n')
            w.writerow(['root_system','family','walsh_multiplier','multiplicity'])
            w.writerows(entries)
    print('ROOT_POSET_FOURIER_RANK4_PASS type_count=5 spectral_rows='+str(len(entries)))

if __name__=='__main__':main()
