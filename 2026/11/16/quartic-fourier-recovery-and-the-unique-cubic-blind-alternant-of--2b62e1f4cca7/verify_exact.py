"""Exact finite certificate for positional-marginal sampling of 3x3 standard tableaux.
Run: python3 verify_exact.py. Python 3 standard library only.
"""
from collections import defaultdict
from itertools import combinations, permutations

N = 9
CELLS = tuple(range(9))       # row-major, zero-based

def enumerate_orders():
    pred = []
    for p in CELLS:
        i,j = divmod(p,3)
        b = 0
        if i: b |= 1 << (p-3)
        if j: b |= 1 << (p-1)
        pred.append(b)
    allmask = (1<<N)-1
    def rec(mask,word):
        if mask==allmask:
            yield word
            return
        for p in CELLS:
            if not(mask>>p&1) and pred[p]&mask == pred[p]:
                yield from rec(mask | (1<<p),word+(p,))
    return list(rec(0,()))

def event_vectors(orders,d):
    # Each key fixes d entries to specific cells (equiv. d coordinate observations).
    features = [defaultdict(int) for _ in range(d+1)]
    for index, order in enumerate(orders):
        bit = 1 << index
        for k in range(d+1):
            for positions in combinations(range(N),k):
                key = tuple((pos,order[pos]) for pos in positions)
                features[k][key] |= bit
    # One mask per distinct column; equality of columns does not affect ranks.
    return [list(set(x.values())) for x in features]

def integer_gram(masks,n):
    g=[[0]*n for _ in range(n)]
    for mask in masks:
        inds=[i for i in range(n) if mask>>i&1]
        for i in inds:
            for j in inds:
                g[i][j]+=1
    return g

def exact_rank(a):
    # Full pivoting fraction-free Gaussian elimination (Bareiss).
    a=[row[:] for row in a]
    m=len(a); n=len(a[0])
    k=0;den=1
    while k < min(m,n):
        piv=next(((r,c) for r in range(k,m) for c in range(k,n) if a[r][c]),None)
        if piv is None:break
        r,c=piv
        a[k],a[r]=a[r],a[k]
        if c!=k:
            for row in a:row[k],row[c]=row[c],row[k]
        z=a[k][k]
        for i in range(k+1,m):
            v=a[i][k]
            for j in range(k+1,n):
                num=z*a[i][j]-v*a[k][j]
                assert num%den==0,(k,i,j)
                a[i][j]=num//den
            a[i][k]=0
        den=z;k+=1
    return k

def signature(word):
    blocks = (word[1:3],word[3:6],word[6:8])
    targets = ((1,3),(2,4,6),(5,7))
    if word[0] != 0 or word[-1] != 8 or any(set(block)!=set(tar) for block,tar in zip(blocks,targets)):
        return 0
    s=1
    for block in blocks:
        s*=(-1)**sum(block[i]>block[j] for i in range(len(block)) for j in range(i+1,len(block)))
    return s

def main():
    orders = enumerate_orders()
    assert len(orders)==42 and len(set(orders))==42
    basis=event_vectors(orders,4)
    target=(1,11,31,41,42)
    cumulative=[]
    signs=[signature(w) for w in orders]
    assert signs.count(1)==12 and signs.count(-1)==12 and signs.count(0)==18
    for d,v in enumerate(basis):
        cumulative.extend(v)
        rank=exact_rank(integer_gram(cumulative,42))
        assert rank==target[d],(d,rank)
        if d<=3:
            for mask in v:
                assert sum(signs[i] for i in range(42) if mask>>i&1)==0
        print('degree',d,'new_unique_events',len(v),'cumulative_rank',rank)
    witness=((1,1),(3,2),(4,4),(6,5))  # label is position+1, cell zero-based
    w=sum(signs[i] for i,word in enumerate(orders) if all(word[pos]==cell for pos,cell in witness))
    assert abs(w)==1,w
    print('signed_witness',w, 'marginal_gap',str(abs(w))+'/12')
    print('VERIFY_EXACT_OK')
if __name__=='__main__':main()
