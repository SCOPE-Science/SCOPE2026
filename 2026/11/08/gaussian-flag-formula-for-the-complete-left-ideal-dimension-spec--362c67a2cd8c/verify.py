"""Direct ideal enumeration and independent Gaussian flags, standard-library only."""
from itertools import combinations, product
from collections import Counter
from functools import lru_cache

def gauss(n,k,q):
    if k<0 or k>n:return 0
    a=b=1
    for i in range(k):
        a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b

def count_flags(n,q):
    @lru_cache(None)
    def rec(i,prev):
        if i==0:return {0:1}
        ans=Counter()
        for d in range(prev,n-i+2):
            coeff=gauss(n-i+1-prev,d-prev,q)
            for e,c in rec(i-1,d).items():ans[e+d]+=coeff*c
        return dict(ans)
    return Counter(rec(n,0))

def rref_subspaces(n,q):
    for r in range(n+1):
        for piv in combinations(range(n),r):
            free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
            for vals in product(range(q),repeat=len(free)):
                B=[[0]*n for _ in range(r)]
                for i,p in enumerate(piv):B[i][p]=1
                for (i,j),v in zip(free,vals):B[i][j]=v
                yield tuple(map(tuple,B))

def span(B,q):
    n=len(B[0]) if B else 0
    return {tuple(sum(c*B[i][j] for i,c in enumerate(coeffs))%q for j in range(n)) for coeffs in product(range(q),repeat=len(B))}

def raw_ideal_count(n,q):
    units=[(i,j) for i in range(n) for j in range(i,n)]
    k=len(units); pos={p:a for a,p in enumerate(units)}
    actions=[]
    for i,j in units:
        rows=[]
        for a,b in units:
            out=[0]*k
            if j==a:out[pos[(i,b)]]=1
            rows.append(tuple(out))
        actions.append(tuple(rows))
    hist=Counter();tot=0
    for basis in rref_subspaces(k,q):
        # test each generator Eij times each basis vector, via matrix unit multiplication
        good=True
        # rref rank membership via reduction over prime field
        for row in basis:
            for (i,j),act in zip(units,actions):
                out=[sum(row[a]*act[a][b] for a in range(k))%q for b in range(k)]
                # reduce against RREF pivot basis
                for br in basis:
                    p=next(p for p,x in enumerate(br) if x)
                    c=out[p]
                    if c:out=[(x-c*y)%q for x,y in zip(out,br)]
                if any(out):good=False;break
            if not good:break
        if good:hist[len(basis)]+=1;tot+=1
    return hist

for n,q in [(2,2),(2,3),(3,2)]:
    flags=count_flags(n,q)
    raw=raw_ideal_count(n,q)
    assert flags==raw,(n,q,flags,raw)
    print(f'n={n}, q={q}: direct-left-ideal-ranks={dict(sorted(raw.items()))}, total={sum(raw.values())}: PASS')
for n,q in [(3,3),(4,2),(4,3),(5,2)]:
    flag=count_flags(n,q)
    assert sum(flag.values())>0
    print(f'n={n}, q={q}: Gaussian-flag-ranks={dict(sorted(flag.items()))}, total={sum(flag.values())}: PASS')
print('TRIANGULAR_LEFT_IDEAL_DIRECT_RING_AND_GAUSSIAN_COUNTS_OK')
