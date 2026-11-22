"""Finite independent checks for standard-example pair-type asymptotics.
No external dependencies: python3 check.py.
"""
from itertools import product

def brute_types(n):
    # a_i have positions i, b_i positions n+i; a_i<b_j iff i!=j.
    edges=[(i,n+j) for i in range(n) for j in range(n) if i!=j]
    out=[]
    for v in product(range(3),repeat=2*n):
        # 0=incomparable,1=below new vertex,2=above new vertex.
        if any((v[i]==2 and v[j]==1) or (v[j]==1 and v[i]!=1) or (v[i]==2 and v[j]!=2)
               for i,j in edges):
            continue
        L=sum(1<<i for i,s in enumerate(v) if s==1)
        if any(((L>>i)&1) and v[j]==2 and (i,j) not in edges for i in range(2*n) for j in range(2*n)):
            continue
        U=sum(1<<i for i,s in enumerate(v) if s==2)
        out.append((L,U))
    return out

def analytic(n):
    q=(1<<n)+n-1
    t=3**n+2*q
    a=3*6**n+4*n*3**(n-1)+(n-2)*2**n+2*n+q*q
    f=5**n-3**n+2*n*3**(n-1)
    inc=9**n+4*f+2*q*q+2*n
    return t,a,inc

def independent_extend_test(n,types,l,u,rel):
    # Transitive closure of augmented oriented diagram from pair of single types.
    size=2*n+2
    x,y=2*n,2*n+1
    edges={(i,n+j) for i in range(n) for j in range(n) if i!=j}
    for z,(L,U) in ((x,l),(y,u)):
        for i in range(2*n):
            if L>>i&1:edges.add((i,z))
            if U>>i&1:edges.add((z,i))
    if rel==1:edges.add((x,y))
    if rel==-1:edges.add((y,x))
    reach=[sum(1<<j for i,j in edges if i==k) for k in range(size)]
    for k in range(size):
        for i in range(size):
            if reach[i]>>k&1:reach[i]|=reach[k]
    if any(reach[i]>>i&1 for i in range(size)): return False
    if any(((reach[i]>>j)&1)!=((i,j) in edges) for i in range(2*n) for j in range(2*n)):return False
    for z,(L,U) in ((x,l),(y,u)):
        for i in range(2*n):
            if ((reach[i]>>z)&1)!=((L>>i)&1):return False
            if ((reach[z]>>i)&1)!=((U>>i)&1):return False
    if rel==0 and (reach[x]>>y&1 or reach[y]>>x&1):return False
    return True

for n in range(2,6):
    ts=brute_types(n)
    T=len(ts)
    A=sum((L1 & ~L2)==0 and (U2 & ~U1)==0 for L1,U1 in ts for L2,U2 in ts)
    N=sum((U1 & L2)==0 and (U2 & L1)==0 for L1,U1 in ts for L2,U2 in ts)
    t,a,inc=analytic(n)
    assert T==t,(n,T,t)
    assert A==a,(n,A,a)
    assert N==inc,(n,N,inc)
    assert N>=9**n and N<=(T*T)
    print(f'n={n}: types={T}, oriented comparable={A}, incomparable={N}, exact-two-types={2*A+N}, p_comparable={2*A/(2*A+N):.7f}')
    if n<=3:
        for l in ts:
            for u in ts:
                for rel,criterion in [ (1,((l[0]&~u[0])==0 and (u[1]&~l[1])==0)),(0,((l[1]&u[0])==0 and (u[1]&l[0])==0)) ]:
                    assert independent_extend_test(n,ts,l,u,rel)==criterion,(n,l,u,rel)
        print(f'n={n}: independent closure replay passed')
print('ALL CHECKS PASS')
