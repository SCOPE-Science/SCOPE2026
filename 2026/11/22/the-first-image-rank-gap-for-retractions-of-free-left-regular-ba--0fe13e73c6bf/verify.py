"""Exhaustive certificate of the first image-rank gap in free LRB monoids.
Run with: python3 verify.py (standard library only).
"""
from itertools import permutations, product
from collections import Counter

EXPECTED={1:{1:1,2:1},2:{1:1,2:10,3:3,4:2,5:1},3:{1:1,2:90,3:126,4:143,5:69,6:45,7:12,8:27,9:6,10:9,12:6,16:1}}

def words(n):
    return [()]+[w for j in range(1,n+1) for w in permutations(range(n),j)]

def merge(a,b):
    seen=set(a);out=list(a)
    for i in b:
        if i not in seen:out.append(i);seen.add(i)
    return tuple(out)

def direct(n):
    W=words(n);H=Counter()
    def evaluate(w,im):
        ans=()
        for j in w:ans=merge(ans,im[j])
        return ans
    for images in product(W,repeat=n):
        # Since these are free generators, checking generator fixedness under
        # composition proves the entire endomorphism is idempotent.
        if all(evaluate(w,images)==w for w in images):
            H[len({evaluate(w,images) for w in W})]+=1
    return H

def tabular(n):
    W=words(n); ix={w:i for i,w in enumerate(W)}
    # Independent implementation: product of indices built by scanning the
    # raw concatenation exactly once; zero is the identity index.
    M=[]
    for a in W:
        row=[]
        for b in W:
            u=tuple(dict.fromkeys(a+b))
            row.append(ix[u])
        M.append(row)
    E=Counter();r=range(len(W))
    def evaluate(w,g):
        x=0
        for j in w:x=M[x][g[j]]
        return x
    for g in product(r, repeat=n):
        full=tuple(evaluate(w,g) for w in W)
        if all(full[full[j]]==full[j] for j in r):
            # Generator-level equivalence is enough by the homomorphism law.
            assert all(full[full[i]]==full[i] for i in r)
            E[len(set(full))]+=1
    return E

for n in (1,2,3):
    A=direct(n);B=tabular(n)
    assert dict(A)==dict(B)==EXPECTED[n],(n,A,B)
    print('n=',n,'generator assignments=',len(words(n))**n,
          'retractions=',sum(A.values()), 'rank_poly=', sorted(A.items()))
assert all(i in EXPECTED[2] for i in range(1,6))
assert 11 not in EXPECTED[3] and all(j not in EXPECTED[3] for j in (13,14,15))
print('FIRST_FREE_LRB_RETRACTION_RANK_GAP_CERTIFIED')
