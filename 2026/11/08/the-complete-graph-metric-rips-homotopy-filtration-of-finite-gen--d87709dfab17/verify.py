"""Finite checks for incidence-graph Rips complexes of symplectic generalized quadrangles.
Only standard-library Python; proof of unrestricted statement is in RESULT.md.
"""
import itertools
from collections import deque, Counter
from math import comb


def symp(u, v, p):
    return (u[0]*v[2]-u[2]*v[0]+u[1]*v[3]-u[3]*v[1]) % p


def normalized(v,p):
    v = tuple(z%p for z in v)
    k = next(i for i,z in enumerate(v) if z)
    inv = pow(v[k], -1, p)
    return tuple(z*inv % p for z in v)


def geometry(p):
    pts = sorted({normalized(x,p) for x in itertools.product(range(p),repeat=4) if any(x)})
    ids={x:i for i,x in enumerate(pts)}
    lines=set()
    for i,x in enumerate(pts):
        for y in pts[i+1:]:
            if symp(x,y,p)!=0:continue
            line=frozenset(ids[normalized(tuple(a*xj+b*yj for xj,yj in zip(x,y)),p)]
                           for a in range(p) for b in range(p) if a or b)
            assert len(line)==p+1
            lines.add(line)
    return pts, sorted(lines,key=lambda x:tuple(sorted(x)))


def faces_of_maximal(maxfaces):
    return {tuple(z) for F in maxfaces for k in range(1,len(F)+1)
            for z in itertools.combinations(sorted(F),k)}


def collapse_pairs(faces, pairs, target):
    active=set(faces)
    for a,b in pairs:
        a=tuple(sorted(a));b=tuple(sorted(b))
        assert len(b)==len(a)+1 and set(a).issubset(b)
        assert a in active and b in active,(a,b)
        cofaces=[F for F in active if len(F)>len(a) and set(a).issubset(F)]
        assert cofaces==[b],(a,b,cofaces)
        active.remove(a);active.remove(b)
    assert active==target,(len(active),len(target),len(active-target),len(target-active))
    return len(pairs)


def homology_mod2(faces):
    levels={k:sorted(F for F in faces if len(F)==k+1) for k in range(max(map(len,faces)))}
    ranks={}
    for k in range(1,max(levels)+1):
        row={F:i for i,F in enumerate(levels[k-1])}
        piv={}
        for F in levels[k]:
            z=0
            for a in F:z ^= 1<<row[tuple(x for x in F if x!=a)]
            while z:
                j=z.bit_length()-1
                if j in piv:z^=piv[j]
                else:piv[j]=z;break
        ranks[k]=len(piv)
    return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in levels.items()}


def run(p):
    P,L=geometry(p)
    Np=len(P);Nl=len(L);n=Np+Nl
    assert Np==Nl==(p+1)*(p*p+1)
    edges={(a,Np+j) for j,line in enumerate(L) for a in line}
    assert len(edges)==(p+1)*Nl
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    assert all(len(A)==p+1 for A in adj)
    distances=[]
    for i in range(n):
        d=[99]*n;d[i]=0;Q=deque([i])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[v]==99:d[v]=d[u]+1;Q.append(v)
        assert max(d)==4
        distances.append(d)
    assert max(max(d) for d in distances)==4
    assert all(distances[i][j] in (1,3) for i in range(Np) for j in range(Np,n))
    assert all(distances[i][j] in (2,4) for i in range(Np) for j in range(i+1,Np))
    assert all(distances[i][j] in (2,4) for i in range(Np,n) for j in range(i+1,n))
    assert all(distances[a][b]==1 for a,b in edges)
    assert all(distances[i][j]==2 for i in range(Np) for j in range(i+1,Np)
               if any(i in Lx and j in Lx for Lx in L))

    # At radius 2, all maximal simplices are closed vertex neighborhoods.
    max2=[tuple(sorted({v}|adj[v])) for v in range(n)]
    faces2=faces_of_maximal(max2)
    assert all(max(distances[a][b] for a,b in itertools.combinations(F,2))<=2
               for F in faces2 if len(F)>=2)
    for i in range(n):
        for j in range(i+1,n):
            if distances[i][j]==2:
                centers=adj[i]&adj[j]
                assert len(centers)==1
    # Converse: any radius-two clique containing a distance-two pair sits in a unique max2.
    # Enumerate maximal cliques independently, via Bron--Kerbosch on the threshold graph.
    nbr2=[{j for j in range(n) if j!=i and distances[i][j]<=2} for i in range(n)]
    max_independent=[]
    def bk(R,Pset,X):
        if not Pset and not X:
            max_independent.append(tuple(sorted(R)));return
        pivot=max(Pset|X,key=lambda v:len(Pset&nbr2[v])) if Pset|X else None
        for v in list(Pset-(nbr2[pivot] if pivot is not None else set())):
            bk(R|{v},Pset&nbr2[v],X&nbr2[v]);Pset.remove(v);X.add(v)
    bk(set(),set(range(n)),set())
    assert set(max_independent)==set(max2),(p,len(max_independent))
    pairs2=[]
    for v in range(n):
        neigh=sorted(adj[v])
        for k in range(len(neigh),1,-1):
            for S in itertools.combinations(neigh,k):
                pairs2.append((S,tuple(sorted(S+(v,)))))
    target2={tuple([v]) for v in range(n)}|{tuple(sorted(e)) for e in edges}
    count2=collapse_pairs(faces2,pairs2,target2)

    # Radius 3: every cross pair is adjacent, both within-part factors are
    # unions of their original GQ line/pencil simplices.
    linef=faces_of_maximal(L)
    pencils=[tuple(sorted(adj[v])) for v in range(Np)]
    pencil_f=faces_of_maximal(pencils)
    assert all(max(distances[a][b] for a,b in itertools.combinations(F,2))<=3
               for F in linef if len(F)>=2)
    assert all(max(distances[a][b] for a,b in itertools.combinations(F,2))<=3
               for F in pencil_f if len(F)>=2)
    # Check independent factor enumeration against maximal clique search.
    for part, expected in [(set(range(Np)),L),(set(range(Np,n)),pencils)]:
        ns=[{j for j in part if i!=j and distances[i][j]<=3} for i in range(n)]
        maximal=[]
        def cl(R,ps,xs):
            if not ps and not xs:maximal.append(frozenset(R));return
            pivot=max(ps|xs,key=lambda v:len(ps&ns[v])) if ps|xs else None
            for v in list(ps-(ns[pivot] if pivot is not None else set())):
                cl(R|{v},ps&ns[v],xs&ns[v]);ps.remove(v);xs.add(v)
        cl(set(),set(part),set())
        assert set(maximal)==set(map(frozenset,expected))

    pairsP=[]
    for line in L:
        center=min(line);N=sorted(line-{center})
        for k in range(len(N),1,-1):
            for S in itertools.combinations(N,k):pairsP.append((S,tuple(sorted(S+(center,)))))
    graphP={F for F in linef if len(F)==1}
    graphP|={tuple(sorted([min(line),v])) for line in L for v in line if v!=min(line)}
    countP=collapse_pairs(linef,pairsP,graphP)
    pairsL=[]
    for line in pencils:
        center=min(line);N=sorted(set(line)-{center})
        for k in range(len(N),1,-1):
            for S in itertools.combinations(N,k):pairsL.append((S,tuple(sorted(S+(center,)))))
    graphL={F for F in pencil_f if len(F)==1}
    graphL|={tuple(sorted([min(line),v])) for line in pencils for v in line if v!=min(line)}
    countL=collapse_pairs(pencil_f,pairsL,graphL)
    beta=(p*p)**2
    assert len(graphP)==Np+(len(L)*p) and len(graphL)==Nl+(len(P)*p)
    assert len(graphP)-2*Np+1==beta
    assert len(graphL)-2*Nl+1==beta
    bp=homology_mod2(linef)
    bl=homology_mod2(pencil_f)
    assert bp[0]==bl[0]==1 and bp[1]==bl[1]==beta and all(v==0 for k,v in bp.items() if k>1) and all(v==0 for k,v in bl.items() if k>1),(bp,bl)
    print(f"W({p}): points={Np}, lines={Nl}, incidence_edges={len(edges)}, "
          f"rips2_faces={len(faces2)}, rips2_relative_collapses={count2}, "
          f"factor_faces=({len(linef)},{len(pencil_f)}), "
          f"factor_collapses=({countP},{countL}), "
          f"factor_betti=({bp},{bl}), radius3_H3_rank={beta**2}")

if __name__=='__main__':
    for p in (2,3):run(p)
    print('GQ_ALL_FINITE_CHECKS_PASS')
