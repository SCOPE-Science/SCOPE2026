"""Independent small-field tests of a finite quandle endomorphism rank census.
No network access or third-party packages required. Python 3.10+.
"""
from collections import Counter
from itertools import product
from math import prod, comb, factorial

def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))
def neg(a,p): return tuple(-x%p for x in a)
def mm(M,x,p): return tuple(sum(a*b for a,b in zip(row,x))%p for row in M)
def rank(M,p):
    A=[list(row) for row in M]; d=len(A); i=0
    for j in range(d):
        k=next((h for h in range(i,d) if A[h][j]%p),None)
        if k is None: continue
        A[i],A[k]=A[k],A[i]; v=pow(A[i][j],-1,p)
        A[i]=[(v*a)%p for a in A[i]]
        for h in range(d):
            if h!=i:
                b=A[h][j]; A[h]=[(a-b*c)%p for a,c in zip(A[h],A[i])]
        i+=1
    return i

def stirling(n,k):
    T=[[0]*(n+1) for _ in range(n+1)];T[0][0]=1
    for i in range(1,n+1):
        for j in range(1,i+1): T[i][j]=T[i-1][j-1]+j*T[i-1][j]
    return T[n][k]

def gaussian(d,r,p):
    top=prod(p**d-p**i for i in range(r));bot=prod(p**r-p**i for i in range(r))
    return top//bot

def nrank(d,r,p):
    return gaussian(d,r,p)*prod(p**d-p**i for i in range(r))

def mulpoly(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():c[i+j]+=x*y
    return c

def theory(p,d):
    Q=p**d; P=Counter()
    for r in range(d+1):
        s=p**r; M=p**(d-r)
        A={s*j:s**M*prod(M-i for i in range(j))*stirling(M,j) for j in range(1,M+1)}
        B={0:1}
        for _ in range(s):B=mulpoly(B,A)
        for rank,size in B.items():P[rank]+=Q*nrank(d,r,p)*size
    return P

def test(p,d):
    V=list(product(range(p),repeat=d)); Q=len(V); zero=(0,)*d
    elems=list(product(V,V)); idx={x:i for i,x in enumerate(elems)}
    op=[[idx[(add(a,add(b,neg(v,p),p),p),b)] for c,v in elems] for a,b in elems]
    mats=list(product(range(p),repeat=d*d))
    seen=Counter(); params=0
    for vals in mats:
        M=[vals[i*d:(i+1)*d] for i in range(d)]
        for shift in V:
            for ts in product(V,repeat=Q):
                t=dict(zip(V,ts)); table=[idx[(add(mm(M,a,p),t[b],p),add(mm(M,b,p),shift,p))] for a,b in elems]
                for u in range(Q*Q):
                    for v in range(Q*Q):
                        assert table[op[u][v]]==op[table[u]][table[v]]
                seen[len(set(table))]+=1;params+=1
    assert seen==theory(p,d),(seen,theory(p,d))
    print(f'p={p}, d={d}, underlying quandle size={Q*Q}, param maps={params}, rank histogram={sorted(seen.items())}, formula=PASS, every listed map preserves operation=PASS')
    if p==2 and d==1:
        allh=Counter()
        for F in product(range(4),repeat=4):
            if all(F[op[u][v]]==op[F[u]][F[v]] for u in range(4) for v in range(4)):
                allh[len(set(F))]+=1
        assert allh==seen
        print('Brute forced ALL 4^4 set maps: exact agreement.')
    return seen

if __name__=='__main__':
    test(2,1);test(3,1);test(2,2)
    for p,d in [(2,1),(3,1),(2,2),(3,2),(2,3)]:
        Z=theory(p,d);Q=p**d;total=p**(d*d+d+d*Q)
        assert sum(Z.values())==total
        assert Z[Q*Q]==Q*nrank(d,d,p)*Q**Q
        assert max(k for k,v in Z.items() if k<Q*Q)==Q*Q//p
        print(f'formula checksum p={p} d={d} total={total} proper_max={Q*Q//p} support_length={len(Z)} PASS')
