#!/usr/bin/env python3
"""Finite cross-checks for incidence-metric Rips complexes of symplectic GQ(3,q), q=2,3.
No external modules are required. The uniform homotopy proof is mathematical, not inferred from these cases.
"""
from itertools import product, combinations
from collections import deque, defaultdict
from math import comb

def canonical(v,q):
    for a in v:
        if a%q: return tuple((x*pow(a,-1,q))%q for x in v)
    raise ValueError('zero')

def bilinear(a,b,q):
    return (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%q

def geometry(q):
    P=sorted({canonical(v,q) for v in product(range(q),repeat=4) if any(v)})
    ix={p:i for i,p in enumerate(P)}; L=set()
    for a,b in combinations(P,2):
        if bilinear(a,b,q):continue
        line=frozenset(ix[canonical(tuple((s*x+t*y)%q for x,y in zip(a,b)),q)]
                       for s in range(q) for t in range(q) if s or t)
        assert len(line)==q+1
        L.add(line)
    L=sorted(L,key=lambda x:sorted(x)); n=len(P);m=len(L)
    E={(i,n+j) for j,line in enumerate(L) for i in line}
    assert n==m==(q+1)*(q*q+1)
    assert len(E)==n*(q+1)
    return P,L,E

def distances(n,E):
    N=[set() for _ in range(n)]
    for i,j in E:N[i].add(j);N[j].add(i)
    out=[]
    for i in range(n):
        d=[-1]*n;d[i]=0;Q=deque([i])
        while Q:
            u=Q.popleft()
            for v in N[u]:
                if d[v]<0:d[v]=d[u]+1;Q.append(v)
        assert all(x>=0 for x in d)
        out.append(d)
    return N,out

def all_cliques(adj):
    # Iteratively extend faces by higher vertex labels.
    faces={frozenset()}
    level=[frozenset([i]) for i in range(len(adj))]
    while level:
        faces.update(level)
        nxt=[]
        for s in level:
            for j in range(max(s)+1,len(adj)):
                if all(j in adj[i] for i in s):nxt.append(s|{j})
        level=nxt
    return faces-{frozenset()}

def morse_test(faces,pairs):
    face_set=set(faces)
    matched=set()
    for a,b in pairs:
        assert a in face_set and b in face_set and len(b)==len(a)+1 and a<b
        assert a not in matched and b not in matched
        matched.add(a); matched.add(b)
    # Hasse arrows: matched up, all others down.
    indeg={s:0 for s in face_set}
    out=defaultdict(list); incidences=0
    pset=set(pairs)
    for s in face_set:
        if len(s)==1:continue
        for v in s:
            t=s-{v}
            assert t in face_set
            a,b=(t,s) if (t,s) in pset else (s,t)
            out[a].append(b);indeg[b]+=1;incidences+=1
    Q=deque(s for s in face_set if indeg[s]==0)
    count=0
    while Q:
        x=Q.popleft();count+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:Q.append(y)
    assert count==len(face_set),(count,len(face_set))
    return incidences,len(face_set)-len(matched)

def rank2(cols):
    p={}
    for z in cols:
        while z:
            i=z.bit_length()-1
            if i in p:z^=p[i]
            else:p[i]=z;break
    return len(p)

def homology(faces):
    bydim=defaultdict(list)
    for s in faces:bydim[len(s)-1].append(s)
    rk={}
    for d in sorted(bydim,reverse=True):
        if d==0:continue
        index={s:i for i,s in enumerate(bydim[d-1])}
        rk[d]=rank2([sum(1<<index[s-{v}] for v in s) for s in bydim[d]])
    return {d:len(fs)-rk.get(d,0)-rk.get(d+1,0)-int(d==0) for d,fs in bydim.items()}

def exercise(q):
    P,L,E=geometry(q);n=len(P); N,D=distances(2*n,E)
    assert max(max(x) for x in D)==4
    assert all(D[i][j]==(1 if (min(i,j),max(i,j)) in E else 3)
               for i in range(n) for j in range(n,2*n))
    # Check diameter 4 and the two-colour subgraph threshold tests.
    for offset,blocks in [(0,L),(n,[frozenset(j for j,li in enumerate(L) if i in li) for i in range(n)])]:
        adj=[{j for j in range(n) if j!=i and D[i+offset][j+offset]<=3} for i in range(n)]
        fs=all_cliques(adj)
        maxima={s for s in fs if not any(s<t for t in fs)}
        wanted={frozenset(offset*0+i for i in B) for B in blocks}
        assert maxima==wanted,(q,offset,maxima^wanted)
        pairs=[]
        for B in blocks:
            root=min(B); leaves=sorted(B-{root})
            for k in range(2,len(leaves)+1):
                for S in combinations(leaves,k):
                    a=frozenset(S);pairs.append((a,a|{root}))
        hasse,crit=morse_test(fs,pairs)
        beta=homology(fs)
        assert beta.get(1)==(q**4) and all(v==0 for d,v in beta.items() if d!=1),beta
        print('q',q,'side',('points' if offset==0 else 'lines'),'faces',len(fs),'hasse',hasse,'matching_pairs',len(pairs),'critical',crit,'beta1',beta[1])
    # Verify both colour factors form a join at threshold 3.
    assert all(D[i][j]<=3 for i in range(n) for j in range(n,2*n))
    assert all(D[i][j] in (2,4) for i in range(n) for j in range(i+1,n))
    adj2=[{j for j in range(2*n) if j!=i and D[i][j]<=2} for i in range(2*n)]
    fs2=all_cliques(adj2)
    pairs=[]
    for v in range(2*n):
        leaves=sorted(N[v])
        for k in range(2,len(leaves)+1):
            for S in combinations(leaves,k):
                a=frozenset(S);pairs.append((a,a|{v}))
    hasse,crit=morse_test(fs2,pairs)
    assert crit==2*n+len(E)
    beta=homology(fs2)
    assert beta.get(1)==q**4 and all(v==0 for d,v in beta.items() if d!=1)
    print('q',q,'VR2 faces',len(fs2),'hasse',hasse,'matching_pairs',len(pairs),'critical',crit,'beta1',beta[1])
    print('q',q,'VR3 predicted Betti3',q**8,'VR4 simplex',2*n,'vertices')

if __name__=='__main__':
    exercise(2)
    exercise(3)
    print('GENERALIZED_QUADRANGLE_RIPS_FINITE_CHECK_PASS')
