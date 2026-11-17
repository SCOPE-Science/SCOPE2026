"""Reproducible finite tests for triangle-avoidance on two-matching-deficient tripartite graphs.
Only Python 3 standard library. The all-parameter theorem uses an independent topological proof.
"""
from itertools import combinations
from collections import defaultdict

def make_instance(a,b,c,p,q):
    assert min(a,b,c,p,q)>=1 and a>=p and b>=p+q and c>=q
    A=set(range(a)); B=set(range(a,a+b)); C=set(range(a+b,a+b+c))
    aa=sorted(A);bb=sorted(B);cc=sorted(C)
    missing={frozenset((aa[i],bb[i])) for i in range(p)}
    missing|={frozenset((bb[p+j],cc[j])) for j in range(q)}
    edges={frozenset((v,w)) for v,w in combinations(range(a+b+c),2)
           if ((v in A and w in B) or (v in A and w in C) or (v in B and w in C))
           and frozenset((v,w)) not in missing}
    triangles={frozenset(t) for t in combinations(range(a+b+c),3)
               if all(frozenset(e) in edges for e in combinations(t,2))}
    base=[A|B,A|C,B|C]
    side1=[{aa[i],bb[i]}|C for i in range(p)]
    side2=[A|{bb[p+j],cc[j]} for j in range(q)]
    bridge=[{aa[i],bb[i],bb[p+j],cc[j]} for i in range(p) for j in range(q)]
    cover=base+side1+side2+bridge
    return edges,triangles,cover

def faces_by_size(facets):
    f=defaultdict(set)
    f[0].add(())
    for facet in facets:
        sv=sorted(facet)
        for r in range(1,len(sv)+1):
            f[r].update(combinations(sv,r))
    return f

def reduced_betti_mod2(f):
    # f[r] consists of r-vertex simplices, so the returned key is dimension r-1.
    rows={r:sorted(x) for r,x in f.items()}
    rank={}
    for r in range(1,max(rows)+1):
        prev={face:i for i,face in enumerate(rows[r-1])}
        pivots={}
        for face in rows[r]:
            v=0
            for j in range(r):
                v ^= 1<<prev[face[:j]+face[j+1:]]
            while v:
                lead=v.bit_length()-1
                if lead in pivots:
                    v ^= pivots[lead]
                else:
                    pivots[lead]=v
                    break
        rank[r]=len(pivots)
    bettis={r-1:len(rows[r])-rank.get(r,0)-rank.get(r+1,0)
            for r in range(1,max(rows)+1)}
    # The augmented boundary r=1 already computes reduced degree-zero homology.
    return {d:k for d,k in bettis.items() if k}

def brute_faces(n,triangles):
    f=defaultdict(set);f[0].add(())
    for r in range(1,n+1):
        for verts in combinations(range(n),r):
            if all(not t.issubset(verts) for t in triangles):
                f[r].add(verts)
    return f

def test(a,b,c,p,q):
    edges,triangles,cover=make_instance(a,b,c,p,q)
    structural=faces_by_size(cover)
    actual=brute_faces(a+b+c,triangles)
    assert actual==structural,(a,b,c,p,q, 'face classification fails')
    bb=reduced_betti_mod2(actual)
    predicted={} if (p-1)*(q-1)==0 else {3:(p-1)*(q-1)}
    assert bb==predicted,(a,b,c,p,q,bb,predicted)
    return len(triangles),sum(len(s) for s in actual.values())-1,bb

def det_bareiss(matrix):
    a=[list(row) for row in matrix]
    n=len(a)
    if n==0:return 1
    sign=1;old=1
    for k in range(n-1):
        if a[k][k]==0:
            for j in range(k+1,n):
                if a[j][k]:
                    a[k],a[j]=a[j],a[k];sign=-sign;break
            else:return 0
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%old==0
                a[i][j]=num//old
        for i in range(k+1,n):a[i][k]=0
        old=pivot
    return sign*a[-1][-1]

def primitive_incidence_test(p,q):
    # Columns are the differences e_i-f_j in Z^(p+q).
    # Select p+q-1 tree edges of the complete bipartite graph.
    tree=[(i,0) for i in range(p)]+[(0,j) for j in range(1,q)]
    n=p+q
    minor=[[0]*(n-1) for _ in range(n-1)]
    for col,(i,j) in enumerate(tree):
        if i<n-1:minor[i][col]=1
        if p+j<n-1:minor[p+j][col]=-1
    d=det_bareiss(minor)
    assert abs(d)==1,(p,q,d)
    return d

if __name__=='__main__':
    cases=[(1,2,1,1,1),(2,2,2,1,1),(2,3,3,1,2),
           (3,3,2,2,1),(2,4,2,2,2),(3,4,3,2,2),
           (2,5,3,2,3),(4,6,3,3,2),(3,6,3,3,3)]
    total=0
    for a,b,c,p,q in cases:
        t,n,h=test(a,b,c,p,q)
        total+=n
        d=primitive_incidence_test(p,q)
        print('case',a,b,c,p,q,'triangles',t,'faces',n,'betti',h,'tree_minor',d)
    print('TWO_MATCHING_TRIANGLE_AVOIDANCE_PASS',len(cases),'cases',total,'faces')
