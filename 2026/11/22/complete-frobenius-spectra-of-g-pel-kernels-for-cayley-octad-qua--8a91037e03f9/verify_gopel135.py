"""Exact, dependency-free certificate for rational Gopel kernels of a Cayley octad.
Run with: python3 verify_gopel135.py
"""
from itertools import combinations, permutations
from collections import Counter
from math import prod

N=8

def canon(mask):
    assert mask.bit_count()%2 == 0 and 0 <= mask < 256
    if mask & 128: mask ^= 255
    return mask

def act(mask, sigma):
    result=0
    for i in range(7):
        if mask>>i & 1: result ^= 1<<sigma[i]
    return canon(result)

def subspace(gens):
    result={0}
    for g in gens: result |= {u^g for u in tuple(result)}
    return frozenset(result)

def dot(u,v): return (u & v).bit_count() & 1

# Exhaust all linearly independent, mutually orthogonal triples.
even=[u for u in range(128) if u.bit_count()%2==0]
by_triples=set()
for a,b,c in combinations(even[1:],3):
    if dot(a,b) or dot(a,c) or dot(b,c): continue
    s=subspace((a,b,c))
    if len(s)==8: by_triples.add(s)
assert len(by_triples)==135

def matchings(labels):
    if not labels:
        yield ()
    else:
        p=labels[0]
        for i in range(1,len(labels)):
            for rest in matchings(labels[1:i]+labels[i+1:]):
                yield ((p,labels[i]),)+rest

# Direct perfect matching construction (105).
from_matchings=set()
for m in matchings(tuple(range(8))):
    vs=[canon((1<<a)|(1<<b)) for a,b in m]
    s=subspace(vs)
    assert len(s)==8
    from_matchings.add(s)
assert len(from_matchings)==105

# Direct affine geometry construction (30). Hyperplane masks of F_2^3.
def parity(i): return i.bit_count()&1
base=[canon(sum(1<<i for i in range(8) if parity(i&a)==0)) for a in range(1,8)]
from_affine=set()
for sigma in permutations(range(8)):
    s=subspace(act(u,sigma) for u in base)
    assert len(s)==8
    from_affine.add(s)
assert len(from_affine)==30
assert not (from_affine & from_matchings)
assert by_triples == from_matchings | from_affine

ALL=sorted(by_triples,key=lambda s:tuple(sorted(s)))
lookup={s:i for i,s in enumerate(ALL)}
match_indices={lookup[x] for x in from_matchings}
affine_indices={lookup[x] for x in from_affine}

def partitions(n,maximum=None):
    if n==0:
        yield ()
        return
    for k in range(min(n, n if maximum is None else maximum),0,-1):
        for rest in partitions(n-k,k): yield (k,)+rest

def perm_for_cycle_partition(parts):
    sigma=list(range(8));p=0
    for width in parts:
        for j in range(width): sigma[p+j]=p+(j+1)%width
        p+=width
    assert p==8
    return sigma

def orbit_counts(f):
    unseen=set(range(len(f)));cnt=Counter()
    while unseen:
        start=min(unseen);v=start;k=0
        while v in unseen:
            unseen.remove(v);k+=1;v=f[v]
        assert v==start
        cnt[k]+=1
    return dict(sorted(cnt.items()))

TABLE={}
for parts in partitions(8):
    sigma=perm_for_cycle_partition(parts)
    f=[lookup[frozenset(act(u,sigma) for u in s)] for s in ALL]
    assert sorted(f)==list(range(135))
    c=orbit_counts(f)
    assert sum(k*v for k,v in c.items())==135
    fixedm=sum(f[j]==j for j in match_indices)
    fixeda=sum(f[j]==j for j in affine_indices)
    assert c.get(1,0)==fixedm+fixeda
    fixedbit=sum({sigma[i],sigma[j]}=={i,j} for i in range(8) for j in range(i+1,8))
    TABLE[parts]=(c,fixedm,fixeda,fixedbit)
assert len(TABLE)==22
assert TABLE[(8,)][0]=={1:1,2:5,4:7,8:12}
assert TABLE[(7,1)][0]=={1:2,7:19}
assert TABLE[(4,4)][0]=={1:11,2:14,4:24}
assert TABLE[(5,3)][0]=={15:9}
assert TABLE[(1,)*8][0]=={1:135}
for parts,(c,fm,fa,b) in TABLE.items():
    print(','.join(map(str,parts)), 'cycles=' + ','.join(f'{k}:{v}' for k,v in c.items()),f'rational_matchings={fm}',f'rational_affine={fa}',f'rational_bitangents={b}')
print('GOPEL135_OCTAD_FROBENIUS_EXHAUSTIVE_OK')
