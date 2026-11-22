"""Standalone finite verification of cyclic clique strong-metric-basis exchange classification.
Python 3 standard library; no external data required.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

def host(n,m):
    N=n*m
    adj=[set() for _ in range(N)]
    for i in range(n):
        for a in range(m):
            u=i*m+a
            for j in ((i+1)%n,(i-1)%n):adj[u].add(j*m+a)
            for b in range(m):
                if b!=a:adj[u].add(i*m+b)
    return adj

def sr_direct(n,m):
    adj=host(n,m);N=n*m
    d=[]
    for u in range(N):
        du=[-1]*N;du[u]=0;q=deque([u])
        while q:
            a=q.popleft()
            for b in adj[a]:
                if du[b]<0:du[b]=du[a]+1;q.append(b)
        d.append(du)
    ed=[]
    for u in range(N):
        for v in range(u+1,N):
            if all(d[w][v]<=d[u][v] for w in adj[u]) and all(d[w][u]<=d[u][v] for w in adj[v]):ed.append((u,v))
    return ed,d

def sr_formula(n,m):
    h=n//2
    return {(i*m+a,j*m+b) for i in range(n) for j in range(i+1,n) for a in range(m) for b in range(m)
            if a!=b and (min(j-i,n-(j-i))==h)}

def indep_enum(N,edges):
    nb=[0]*N
    for u,v in edges:
        nb[u]|=1<<v;nb[v]|=1<<u
    count=Counter(); maxsets=[]; best=0
    def visit(i,chosen,mask,k):
        nonlocal best,maxsets
        if i==N:
            count[k]+=1
            if k>best:best=k;maxsets=[chosen]
            elif k==best:maxsets.append(chosen)
            return
        visit(i+1,chosen,mask,k)
        if not (mask>>i&1): visit(i+1,chosen|(1<<i),mask|nb[i],k+1)
    visit(0,0,0,0)
    return count, maxsets

def polynomial_formula(n,m):
    # elementary coefficient-polynomial matrices, no sympy
    def add(a,b):
        c=[0]*max(len(a),len(b))
        for i,x in enumerate(a):c[i]+=x
        for i,x in enumerate(b):c[i]+=x
        return c
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    def matmul(A,B):
        z=[[[0] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):z[i][j]=add(z[i][j],mul(A[i][k],B[k][j]))
        return z
    if n%2==0:
        single=[0]*(2*m+1)
        for k in range(m+1):single[k]+=2*comb(m,k)
        single[0]-=1;single[2]+=m
        p=[1]
        for _ in range(n//2):p=mul(p,single)
        return p
    W=[0]*(m+1)
    for j in range(2,m+1):W[j]=comb(m,j)
    T=[[[1],[0,m],W],[[1],[0,1],[0]],[[1],[0],[0]]]
    R=[[[int(i==j)] for j in range(3)] for i in range(3)]
    for _ in range(n):R=matmul(R,T)
    p=[0]
    for i in range(3):p=add(p,R[i][i])
    if len(p)<=n:p += [0]*(n+1-len(p))
    p[n]+=m-1
    return p

def expected_optima(n,m):
    # Return independent-set masks, with proven complete formulas
    if n%2==0:
        k=n//2
        if m==2:
            # each diametral column-pair has two disjoint K2 components
            parts=[]
            for i in range(k):
                j=i+k
                parts.extend([((i,0),(j,1)),((i,1),(j,0))])
            arr=[0]
            for pair in parts:
                arr=[t|(1<<(x[0]*m+x[1])) for t in arr for x in pair]
            return set(arr)
        arr=[0]
        for i in range(k):
            arr=[t|sum(1<<((i+o*k)*m+a) for a in range(m)) for t in arr for o in (0,1)]
        return set(arr)
    if m==2:
        return {sum(1<<(i*m+a) for i in range(n)) for a in range(2)}
    out={sum(1<<(((t+j)%n)*m+a) for j in range((n-1)//2) for a in range(m)) for t in range(n)}
    if n==3 and m==3:
        out|={sum(1<<(i*m+a) for i in range(n)) for a in range(m)}
    return out

def verify():
    cases=[(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4),(6,2),(6,3),(7,2),(7,3),(8,2)]
    for n,m in cases:
        N=n*m
        edges,d=sr_direct(n,m)
        assert set(edges)==sr_formula(n,m),(n,m,'MMD graph')
        counts,bests=indep_enum(N,edges)
        p=polynomial_formula(n,m)
        assert all(counts[k]==(p[k] if k<len(p) else 0) for k in range(N+1)),(n,m,'polynomial')
        assert set(bests)==expected_optima(n,m),(n,m,'optima',len(bests),len(expected_optima(n,m)))
        # independently compute edge-exchange graph on all optimum solutions
        opt=sorted(bests); L=len(opt);dist={}
        for a,b in combinations(range(L),2):
            moves=(opt[a]^opt[b]).bit_count()//2
            dist[(a,b)]=moves
        if n%2==0 and m==2: assert L==2**n and min(dist.values())==1
        elif n%2==0:assert L==2**(n//2) and min(dist.values())==m
        elif m==2:assert L==2 and list(dist.values())==[n]
        elif n==3 and m==3:assert L==6 and sorted(set(dist.values()))==[2,3]
        else:assert L==n and min(dist.values())==m
        # Check exact batch-exchange distance formulas, not merely connectivity.
        if n%2==0 and m==2:
            pairs=[]
            for i in range(n//2):
                j=i+n//2
                pairs.extend([((i,0),(j,1)),((i,1),(j,0))])
            def code(I):
                return tuple(0 if I>>(pair[0][0]*m+pair[0][1])&1 else 1 for pair in pairs)
            def predicted(I,J):
                return sum(x!=y for x,y in zip(code(I),code(J)))
        elif n%2==0:
            def code(I):
                return tuple(0 if all(I>>(i*m+a)&1 for a in range(m)) else 1 for i in range(n//2))
            def predicted(I,J):
                return m*sum(x!=y for x,y in zip(code(I),code(J)))
        elif m==2:
            def predicted(I,J):return 0 if I==J else n
        elif n==3 and m==3:
            def ctype(I):
                for i in range(n):
                    if all(I>>(i*m+a)&1 for a in range(m)):return ('row',i)
                for a in range(m):
                    if all(I>>(i*m+a)&1 for i in range(n)):return ('column',a)
                raise AssertionError('unknown base')
            def predicted(I,J):
                return 0 if I==J else (2 if ctype(I)[0]!=ctype(J)[0] else 3)
        else:
            k=(n-1)//2
            Jsets=[sum(1<<(((t+j)%n)*m+a) for j in range(k) for a in range(m)) for t in range(n)]
            mapping={I:t for t,I in enumerate(Jsets)}
            def predicted(I,J):
                delta=abs(mapping[I]-mapping[J]);return m*min(delta,n-delta)
        for (a,b),actual in dist.items():
            assert actual==predicted(opt[a],opt[b]),(n,m,a,b,actual,predicted(opt[a],opt[b]))
            # One-vertex host slides never preserve optimal strong resolution.
            if actual==1:
                lost=((opt[a]^opt[b]) & opt[a]).bit_length()-1
                gained=((opt[a]^opt[b]) & opt[b]).bit_length()-1
                assert gained not in host(n,m)[lost],(n,m,'unexpected slide')
        # Test strong resolving criterion without calling MMD theorem: strong geodesic equality.
        if N<=12:
            for sm in range(1<<N):
                strong=all(any((sm>>w&1) and (d[w][u]==d[w][v]+d[u][v] or d[w][v]==d[w][u]+d[u][v]) for w in range(N)) for u in range(N) for v in range(u+1,N))
                cover=all((sm>>u&1) or (sm>>v&1) for u,v in edges)
                assert strong==cover,(n,m,sm,'strong equivalence')
        print('case',n,m,'independent',sum(counts.values()),'maximum',N-min(b.bit_count() for b in [((1<<N)-1)^t for t in bests]),'basis_count',L,'PASS')
    print('VERIFY_OK')
if __name__=='__main__':verify()
