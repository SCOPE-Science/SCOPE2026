"""Independent small-instance checks for optimal triangle transversals of K_{a,b,c}.
Requires only Python 3 standard library. No precomputed tables.
"""
from itertools import combinations
from math import comb


def edges_and_triangles(a,b,c):
    A=range(a); B=range(a,a+b); C=range(a+b,a+b+c)
    edges=sorted([(x,y) for x in A for y in B]+[(x,z) for x in A for z in C]+[(y,z) for y in B for z in C])
    index={e:k for k,e in enumerate(edges)}
    triples=[(index[(x,y)],index[(x,z)],index[(y,z)]) for x in A for y in B for z in C]
    return edges,triples


def predicted_count(a,b,c):
    assert 2<=a<=b<=c
    if b<c:return 1
    if a<b:return 2**a
    return 3*(2**a)-3


def exhaustive_small():
    total_tests=0
    for a,b,c in [(2,2,2),(2,2,3),(2,2,4),(2,3,3),(2,3,4)]:
        edges,triangles=edges_and_triangles(a,b,c)
        tri_bits=[sum(1<<e for e in tri) for tri in triangles]
        m=len(edges); k=a*b
        found=[]
        # Every deletion subset below the claimed optimum is checked.
        for size in range(k+1):
            for inds in combinations(range(m),size):
                total_tests+=1
                deletion_mask=sum(1<<i for i in inds)
                if all(deletion_mask & tb for tb in tri_bits):
                    assert size==k,(a,b,c,'unexpected smaller cover',inds)
                    found.append(deletion_mask)
        assert len(found)==predicted_count(a,b,c),(a,b,c,len(found))
        # Confirm every extremal cover's triangle set and its batch geometry.
        for x,y in combinations(found,2):
            assert (x^y).bit_count()>=2*b if b==c and a<b else (x^y).bit_count()>=2*a
        print('EXHAUSTIVE',a,b,c,'tested',sum(comb(m,s) for s in range(k+1)),
              'optima',len(found),'minimum_deletions',k)
    print('TOTAL_SMALL_SUBSETS_TESTED',total_tests)


def balanced_eq_assignments(n):
    """Enumerate ALL 0/1 AB matrices and solve the triangle exact-one system.
    Every optimal transversal has exactly one deleted edge in each triangle.
    For each fixed C vertex the AC/BC deletion vectors solve X_ab+u_a+v_b=1.
    """
    solutions=0
    for bitmask in range(1<<(n*n)):
        X=[[bool(bitmask>>(i*n+j)&1) for j in range(n)] for i in range(n)]
        t=0
        for u0 in (0,1):
            v=[1-int(X[0][j])-u0 for j in range(n)]
            if any(w not in (0,1) for w in v):continue
            u=[1-int(X[i][0])-v[0] for i in range(n)]
            if any(w not in (0,1) for w in u):continue
            if all(int(X[i][j])+u[i]+v[j]==1 for i in range(n) for j in range(n)):
                t+=1
        solutions+=t**n
    assert solutions==3*2**n-3,(n,solutions)
    print('COMPLETE_BALANCED_EQUALITY',n,'optima',solutions,'AB_matrices',2**(n*n))


def reconfiguration_tests():
    from collections import deque
    for n in range(2,8):
        A=range(n); B=range(n,2*n); C=range(2*n,3*n)
        edges,_=edges_and_triangles(n,n,n)
        ei={e:k for k,e in enumerate(edges)}
        opt=set()
        for X,Y,Z in ((A,B,C),(B,A,C),(C,A,B)):
            for choice in range(1<<n):
                mask=0
                for i,x in enumerate(X):
                    for y in (Y if choice>>i&1 else Z):
                        mask |=1<<ei[tuple(sorted((x,y)))]
                opt.add(mask)
        opt=list(opt)
        adj=[[] for _ in opt]
        single_swap_count=0
        for i,j in combinations(range(len(opt)),2):
            changes=(opt[i]^opt[j]).bit_count()
            if changes==2:single_swap_count+=1
            if changes==2*n:
                adj[i].append(j);adj[j].append(i)
            assert changes>=2*n
        assert single_swap_count==0
        assert len(opt)==3*2**n-3
        assert sum(map(len,adj))//2==3*n*2**(n-1)
        diam=0
        for start in range(len(opt)):
            dist={start:0};queue=deque([start])
            while queue:
                u=queue.popleft()
                for v in adj[u]:
                    if v not in dist:
                        dist[v]=dist[u]+1;queue.append(v)
            assert len(dist)==len(opt)
            diam=max(diam,max(dist.values()))
        assert diam==3*n//2,(n,diam)
        print('BALANCED_EXCHANGE',n,'vertices',len(opt),'edges',sum(map(len,adj))//2,'diameter',diam)
    for a,b in [(2,3),(3,4),(3,5),(4,5)]:
        # For K_{a,b,b}, one free choice for each vertex in the smaller part.
        covers=[]
        A=range(a); B=range(a,a+b); C=range(a+b,a+2*b)
        edges,_=edges_and_triangles(a,b,b);ei={e:k for k,e in enumerate(edges)}
        for choice in range(1<<a):
            cover=set()
            for i,x in enumerate(A):
                for y in (B if choice>>i&1 else C):
                    cover.add(ei[tuple(sorted((x,y)))])
            covers.append(cover)
        deg=[sum(len(x-y)==b for y in covers if x is not y) for x in covers]
        assert len(covers)==2**a and all(d==a for d in deg)
        assert min(len(x-y) for x,y in combinations(covers,2))==b
        print('TIED_LARGEST_EXCHANGE',a,b,b,'vertices',len(covers),'degree',a,'diameter',a)


if __name__=='__main__':
    exhaustive_small()
    for n in (2,3,4):balanced_eq_assignments(n)
    reconfiguration_tests()
    print('VERIFY_OK')
