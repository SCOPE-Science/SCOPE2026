#!/usr/bin/env python3
"""Exhaustive unlabeled triangle-free graphs through eight vertices (stdlib only)."""
from collections import defaultdict, Counter
from time import perf_counter

def canonical_bucket(a):
    d=[v.bit_count() for v in a]
    return (len(a), sum(d)//2, tuple(sorted(d)),
            tuple(sorted((d[v],tuple(sorted(d[w] for w in range(len(a)) if a[v] >> w & 1))) for v in range(len(a)))))

def iso(a,b):
    n=len(a)
    da=[z.bit_count() for z in a]; db=[z.bit_count() for z in b]
    if sorted(da)!=sorted(db):return False
    order=sorted(range(n),key=lambda i:(-da[i],-sum(da[j] for j in range(n) if a[i]>>j&1),i))
    mapping={}; used=0
    def backtrack(k,used):
        if k==n:return True
        v=order[k]
        for w in range(n):
            if (used>>w)&1 or da[v]!=db[w]:continue
            if any(bool(a[v]>>u & 1)!=bool(b[w]>>z & 1) for u,z in mapping.items()):continue
            mapping[v]=w
            if backtrack(k+1,used|(1<<w)):return True
            del mapping[v]
        return False
    return backtrack(0,0)

def induced_independence_sum(a,S=None):
    n=len(a);S=(1<<n)-1 if S is None else S
    cache={0:1}
    def val(mask):
        if mask not in cache:
            v=(mask&-mask).bit_length()-1
            cache[mask]=val(mask^(1<<v))-val(mask & ~(a[v]|(1<<v)))
        return cache[mask]
    return val(S)

def extend(a,neigh):
    n=len(a)
    return tuple(a[i] | (((neigh>>i)&1)<<n) for i in range(n))+(neigh,)

def is_independent(a,S):
    return all(not (a[i]&S) for i in range(len(a)) if S>>i&1)

def generate(old):
    classes=defaultdict(list)
    for a in old:
        for S in range(1<<len(a)):
            if not is_independent(a,S):continue
            b=extend(a,S)
            key=canonical_bucket(b)
            if not any(iso(b,c) for c in classes[key]):classes[key].append(b)
    return [a for group in classes.values() for a in group]

def brute_independence_sum(a, S):
    # Independent second implementation: enumerate every subset of S.
    total = 0
    U = S
    while True:
        if is_independent(a, U):
            total += -1 if U.bit_count() % 2 else 1
        if U == 0: break
        U = (U-1) & S
    return total

def cube_adjacency():
    # Hamming-one adjacency on three-bit strings 0,...,7.
    return tuple(sum(1<<j for j in range(8) if (i^j).bit_count()==1)
                 for i in range(8))

def check_mobius_congruence(a):
    n=len(a); m=1<<n
    coeff=[(-1 if S.bit_count()%2 else 1)*induced_independence_sum(a,S)
           for S in range(m)]
    zeta=coeff[:]
    for i in range(n):
        for S in range(m):
            if S & (1<<i): zeta[S] += zeta[S ^ (1<<i)]
    assert all(zeta[W]==int(is_independent(a,W)) for W in range(m))
    for S in range(m):
        for T in range(m):
            expected=int(is_independent(a,S&T))
            assert zeta[S&T]==expected
    print(f'MATRIX_MOBIUS_IDENTITY_OK {m}x{m} entries={m*m}',flush=True)

def main():
    t=perf_counter();level=[tuple()]
    counts=[]
    for n in range(1,9):
        level=generate(level)
        vals=Counter(induced_independence_sum(a) for a in level)
        counts.append(len(level))
        print(f'n={n} classes={len(level)} min={min(vals)} max={max(vals)} abs_max={max(map(abs,vals))} values={dict(sorted(vals.items()))}',flush=True)
        if n==8:
            ex=[a for a in level if abs(induced_independence_sum(a))>=3]
            assert len(ex)==1 and induced_independence_sum(ex[0])==3
            cube=ex[0]
            assert iso(cube,cube_adjacency())
            for G in level:
                assert induced_independence_sum(G)==brute_independence_sum(G,255)
            for S in range(256):
                assert induced_independence_sum(cube,S)==brute_independence_sum(cube,S)
            check_mobius_congruence(cube)
            print('UNIQUE_ODD_TORSION_FIRST_BASE_EDGES',[(i,j) for i in range(8) for j in range(i+1,8) if cube[i]>>j&1])
            print('Q3 degree sequence:',sorted((v.bit_count() for v in cube)))
            print('Q3 distance profile:', sorted([tuple(sorted(shortest_paths(cube,i))) for i in range(8)]))
            induced=Counter(induced_independence_sum(cube,S) for S in range(256))
            print('Q3 induced independence sums:',dict(sorted(induced.items())))
            h=Counter((-1)**S.bit_count()*induced_independence_sum(cube,S) for S in range(256))
            plus=sum(v for k,v in h.items() if k>0);minus=sum(v for k,v in h.items() if k<0)
            assert induced==Counter({0:138,1:55,-1:50,2:12,3:1})
            assert (plus,minus)==(60,58)
            print('Q3 inertia:',plus,minus,138,'Smith: I_106, 2*I_11, 6, 0_138')
    assert counts==[1,2,3,7,14,38,107,410]
    print('VERIFY_OK',round(perf_counter()-t,3),'sec')

def shortest_paths(a,start):
    n=len(a);d=[-1]*n;d[start]=0;q=[start]
    for u in q:
        for v in range(n):
            if a[u]>>v&1 and d[v]==-1:d[v]=d[u]+1;q.append(v)
    return d

if __name__=='__main__':main()
