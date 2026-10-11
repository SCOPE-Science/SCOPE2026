from itertools import combinations
from collections import deque

def partitions(n, r, lo=1):
    if r == 0:
        if n == 0:
            yield ()
        return
    for x in range(lo, n + 1):
        if n - x < x * (r - 1):
            break
        for rest in partitions(n-x, r-1, x):
            yield (x,) + rest

def labels(parts):
    out=[]
    for i,a in enumerate(parts):
        out += [i]*a
    return out

def is_zero_forcing(parts, mask):
    lab=labels(parts)
    n=len(lab)
    blue=mask
    while True:
        moved=False
        for u in range(n):
            if not ((blue>>u)&1):
                continue
            whites=[v for v in range(n) if not ((blue>>v)&1) and lab[v] != lab[u]]
            if len(whites)==1:
                blue |= 1<<whites[0]
                moved=True
                break
        if not moved:
            break
    return blue == (1<<n)-1

def minimum_sets(parts):
    n=sum(parts)
    all_masks=[]
    for k in range(n+1):
        for S in combinations(range(n),k):
            mask=sum(1<<v for v in S)
            if is_zero_forcing(parts,mask):
                all_masks.append(mask)
        if all_masks:
            return k,sorted(all_masks)
    raise AssertionError

def admissible_edges(parts):
    lab=labels(parts)
    n=len(lab)
    singleton={i for i,a in enumerate(parts) if a==1}
    out=[]
    for x,y in combinations(range(n),2):
        if lab[x] == lab[y]:
            continue
        if lab[x] in singleton and lab[y] in singleton:
            continue
        out.append((x,y))
    return out

def predicted_sets(parts):
    n=sum(parts)
    full=(1<<n)-1
    if all(a==1 for a in parts):
        return n-1, sorted(full ^ (1<<v) for v in range(n))
    ed=admissible_edges(parts)
    return n-2, sorted(full ^ ((1<<x)|(1<<y)) for x,y in ed)

def zgraph_adj(masks):
    m=len(masks)
    A=[[False]*m for _ in range(m)]
    for i in range(m):
        for j in range(i+1,m):
            if (masks[i]^masks[j]).bit_count()==2:
                A[i][j]=A[j][i]=True
    return A

def line_adj(edges):
    m=len(edges)
    A=[[False]*m for _ in range(m)]
    for i in range(m):
        ei=set(edges[i])
        for j in range(i+1,m):
            if len(ei.intersection(edges[j]))==1:
                A[i][j]=A[j][i]=True
    return A

def diameter(A):
    n=len(A)
    if n<=1:
        return 0
    diam=0
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v,a in enumerate(A[u]):
                if a and d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        assert all(x>=0 for x in d)
        diam=max(diam,max(d))
    return diam

types=subsets=minsets=edges_checked=0
for N in range(2,11):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            z,actual=minimum_sets(parts)
            pz,pred=predicted_sets(parts)
            assert z==pz,(parts,z,pz)
            assert actual==pred,(parts,actual,pred)
            subsets += sum(__import__('math').comb(N,k) for k in range(z+1))
            minsets += len(actual)

            A=zgraph_adj(actual)
            if all(a==1 for a in parts):
                # Every pair of complements of singletons differs by one exchange.
                assert all(A[i][j] for i in range(len(A)) for j in range(len(A)) if i!=j)
                assert diameter(A)==1 if len(A)>1 else 0
            else:
                ed=admissible_edges(parts)
                full=(1<<N)-1
                index={full ^ ((1<<x)|(1<<y)): t for t,(x,y) in enumerate(ed)}
                # reorder line graph adjacency into actual-mask order
                L=line_adj(ed)
                for i,m1 in enumerate(actual):
                    e1_idx=index[m1]
                    for j,m2 in enumerate(actual):
                        e2_idx=index[m2]
                        assert A[i][j]==L[e1_idx][e2_idx],(parts,i,j)
                edges_checked += len(ed)
                q=sum(a==1 for a in parts)
                order_formula=sum(parts[i]*parts[j] for i in range(r) for j in range(i+1,r)) - q*(q-1)//2
                assert len(actual)==order_formula,(parts,len(actual),order_formula)
                d=diameter(A)
                is_star=(r==2 and 1 in parts)
                assert d==(1 if is_star else 2),(parts,d,is_star)
            types+=1

print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('candidate_subsets_checked_through_minimum_layer =',subsets)
print('minimum_zero_forcing_sets_checked =',minsets)
print('admissible_pair_vertices_checked =',edges_checked)
print('orders = 2..10')
print('all minimum-set classifications matched')
print('all zero-forcing-graph adjacencies matched the claimed line graph')
print('all order and diameter corollaries matched')
