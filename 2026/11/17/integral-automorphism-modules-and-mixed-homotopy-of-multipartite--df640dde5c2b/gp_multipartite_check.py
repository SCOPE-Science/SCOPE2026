"""Direct finite checks for geodesic-general-position complexes of complete multipartite graphs.

Usage: python gp_multipartite_check.py
No external packages. Finite checks do not substitute for the general proof.
"""
from itertools import combinations, permutations
import random


def test_case(sizes, seed=97):
    r = len(sizes)
    n = sum(sizes)
    groups=[]
    q=0
    for a in sizes:
        groups.append(tuple(range(q,q+a)))
        q+=a
    part=[0]*n
    for i,g in enumerate(groups):
        for v in g: part[v]=i
    # Actual graph distances computed from graph edges by breadth-first search.
    adj=[set(j for j in range(n) if part[i]!=part[j]) for i in range(n)]
    dist=[]
    for i in range(n):
        d=[n+1]*n;d[i]=0;queue=[i]
        for v in queue:
            for w in adj[v]:
                if d[w]>d[v]+1: d[w]=d[v]+1;queue.append(w)
        dist.append(d)
    faces=[];bydim={}
    for k in range(1,n+1):
        for comb in combinations(range(n),k):
            good=True
            for x,y,z in combinations(comb,3):
                if any(dist[u][v]+dist[v][w]==dist[u][w] for u,v,w in ((x,y,z),(y,x,z),(x,z,y))):
                    good=False;break
            if good:
                face=tuple(comb);faces.append(face)
                bydim.setdefault(k-1,[]).append(face)
    # Fully independent classification check from the claimed two face families.
    for face in faces:
        assert len({part[v] for v in face})==1 or len({part[v] for v in face})==len(face)
    assert sum(1 for comb in (c for k in range(n+1) for c in combinations(range(n),k)) if len({part[v] for v in comb})==1 or len({part[v] for v in comb})==len(comb)) == len(faces)+1
    def gf2_rank(cols):
        basis={}
        for col in cols:
            while col:
                t=col.bit_length()-1
                if t in basis: col^=basis[t]
                else:
                    basis[t]=col;break
        return len(basis)
    ranks={}
    for dim in range(1,max(bydim,default=-1)+1):
        lower={f:i for i,f in enumerate(bydim.get(dim-1,[]))}
        cols=[]
        for face in bydim.get(dim,[]):
            mask=0
            for j in range(len(face)):
                mask^=1<<lower[face[:j]+face[j+1:]]
            cols.append(mask)
        ranks[dim]=gf2_rank(cols)
    beta={}
    for dim,fs in bydim.items():
        bd=ranks.get(dim,0) if dim else 0
        nextbd=ranks.get(dim+1,0)
        beta[dim]=len(fs)-bd-nextbd
    beta[0]-=1
    expected={1:sum(a-1 for a in sizes)}
    if r>=3: expected[r-1]=__import__('math').prod(a-1 for a in sizes)
    else: expected[1]+=__import__('math').prod(a-1 for a in sizes)
    expected={k:v for k,v in expected.items() if v}
    assert {k:v for k,v in beta.items() if v}==expected,(sizes,beta,expected)

    rng=random.Random(seed+sum((i+1)*a for i,a in enumerate(sizes)))
    actions=0
    for _ in range(32):
        # A legal part permutation preserves sizes.
        order=list(range(r))
        for size in set(sizes):
            indices=[i for i,a in enumerate(sizes) if a==size]
            targets=indices[:];rng.shuffle(targets)
            for i,j in zip(indices,targets):order[i]=j
        g=[0]*n
        for i,partvertices in enumerate(groups):
            tgt=list(groups[order[i]])
            rng.shuffle(tgt)
            for v,w in zip(partvertices,tgt):g[v]=w
        assert sorted(g)==list(range(n))
        def sign(p):
            return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
        # Signed trace on augmented chain groups, computed only from faces fixed setwise.
        alt=-1
        for dim,fs in bydim.items():
            tr=0
            for face in fs:
                image=[g[v] for v in face]
                if sorted(image)==list(face):
                    tr+=sign(image)
            alt+=((-1)**dim)*tr
        # The integral representation predicted by the structural theorem.
        if r==2:
            a,b=groups
            fixed_edges=sum(set((g[u],g[v]))=={u,v} for u in a for v in b)
            trH1=sign(order)*(fixed_edges-1)
            prediction=-trH1
        else:
            trH1=sum(sum(g[v]==v for v in groups[i])-1 for i in range(r) if order[i]==i)
            seen=set();trtop=sign(order)
            for i in range(r):
                if i in seen: continue
                C=[];j=i
                while j not in seen:
                    C.append(j);seen.add(j);j=order[j]
                fixed=0
                for v in groups[i]:
                    w=v
                    for t in range(len(C)):w=g[w]
                    if w==v:fixed+=1
                trtop*=fixed-1
            prediction=-trH1+((-1)**(r-1))*trtop
        assert alt==prediction,(sizes,order,alt,prediction)
        actions+=1
    return len(faces),sum(len(v) for v in bydim.values()),actions,expected


def main():
    cases=[(2,2),(3,2),(4,3),(1,2),(1,1),(1,1,1),
           (2,2,2),(3,2,2),(2,3,3),(3,3,3),(1,3,2,2),
           (2,2,2,2),(1,2,2,2),(1,1,2,2),(2,2,2,1,1)]
    count=0;faces=0;acts=0
    for sizes in cases:
        a,b,c,expected=test_case(sizes)
        print('PASS',sizes,'faces',a,'nonzero_reduced_betti',expected,'group_actions',c)
        count+=1;faces+=a;acts+=c
    print('GP_MULTIPARTITE_INTEGRAL_MODEL_CHECK_PASS cases=%d faces=%d actions=%d'%(count,faces,acts))
if __name__=='__main__':main()
