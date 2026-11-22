from itertools import product, combinations
from collections import Counter
from math import comb, factorial

def dominate(board,n):
    for i in range(n):
        for j in range(n):
            if not any(a==i or b==j for a,b in board):return False
    return True

def fast_sets(n):
    cells=[(i,j) for i in range(n) for j in range(n)]
    def msk(t):return sum(1<<(i*n+j) for i,j in t)
    rr=[msk([(i,col[i]) for i in range(n)]) for col in product(range(n),repeat=n)]
    cc=[msk([(row[j],j) for j in range(n)]) for row in product(range(n),repeat=n)]
    return set(rr+cc)

def run(n):
    allsets=fast_sets(n)
    if n<=3:
        direct=[sum(1<<(i*n+j) for i,j in t) for t in combinations([(i,j) for i in range(n) for j in range(n)],n) if dominate(t,n)]
        assert set(direct)==allsets
    arr=list(allsets); hist=Counter()
    for k in range(n+1):
        for idx in combinations(range(n*n),k):
            sm=sum(1<<i for i in idx)
            seen=set()
            for d in arr:
                seen.add(d&sm)
                if len(seen)==2**k:break
            got=len(seen)==2**k
            rows=[i//n for i in idx];cols=[i%n for i in idx]
            pred=len(set(rows))==k or len(set(cols))==k
            assert got==pred,(n,idx,got,pred)
            hist[k]+=got
        assert hist[k]==2*comb(n,k)*n**k-comb(n,k)**2*factorial(k), (n,k,hist[k])
    print(n,len(allsets),dict(hist))
for n in range(2,5):run(n)
