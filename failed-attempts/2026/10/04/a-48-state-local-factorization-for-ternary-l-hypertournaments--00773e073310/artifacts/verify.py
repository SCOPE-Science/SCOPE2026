#!/usr/bin/env python3
import itertools
from math import comb

perms=list(itertools.permutations(range(3)))
idx={p:i for i,p in enumerate(perms)}
sigmas=perms[:]

def reorder(t,s):
    return tuple(t[s[i]] for i in range(3))

def rot(t):
    return (t[1],t[2],t[0])

def direct_valid(mask):
    def R(t):
        return bool(mask & (1 << idx[t]))
    # Clause 1: each injective ordered tuple can be permuted to a true one.
    for t in perms:
        if not any(R(reorder(t,s)) for s in sigmas):
            return False
    # Clause 2: no sigma admits a full cyclic triple.
    for s in sigmas:
        for t in perms:
            cyc=[t]
            cyc.append(rot(cyc[-1]))
            cyc.append(rot(cyc[-1]))
            if all(R(reorder(u,s)) for u in cyc):
                return False
    return True

def parity(p):
    inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    return inv & 1

even_mask=sum(1<<i for i,p in enumerate(perms) if parity(p)==0)
odd_mask=sum(1<<i for i,p in enumerate(perms) if parity(p)==1)

def coset_valid(mask):
    return mask != 0 and (mask & even_mask) != even_mask and (mask & odd_mask) != odd_mask

valid=[]
dist={}
for mask in range(1<<6):
    dv=direct_valid(mask)
    cv=coset_valid(mask)
    assert dv==cv, (mask,dv,cv)
    if dv:
        valid.append(mask)
        dist[mask.bit_count()]=dist.get(mask.bit_count(),0)+1

assert len(valid)==48
assert dist=={1:6,2:15,3:18,4:9}, dist
# Coefficients of (1+3z+3z^2)^2 - 1, computed independently.
a=[1,3,3]
coef=[0]*5
for i,x in enumerate(a):
    for j,y in enumerate(a):
        coef[i+j]+=x*y
coef[0]-=1
assert coef==[0,6,15,18,9]

# Restricted-growth strings enumerate equality partitions directly.
def rgs(n):
    if n==0:
        yield ()
        return
    def rec(prefix):
        if len(prefix)==n:
            yield tuple(prefix); return
        hi=max(prefix)+1
        for x in range(hi+1):
            prefix.append(x); yield from rec(prefix); prefix.pop()
    yield from rec([0])

def stirling(n,k):
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

vals=[]
for n in range(6):
    block_counts={}
    for s in rgs(n):
        k=0 if not s else max(s)+1
        block_counts[k]=block_counts.get(k,0)+1
    for k,c in block_counts.items():
        assert c==stirling(n,k)
    b=sum(stirling(n,k)*(48**comb(k,3)) for k in range(n+1))
    vals.append(b)

assert vals==[1,1,2,52,5308712,64925062161630400], vals
print('local_states',len(valid))
print('size_distribution',dist)
print('all_tuple_orbits_n0_to_5',vals)
print('VERIFY_OK')
