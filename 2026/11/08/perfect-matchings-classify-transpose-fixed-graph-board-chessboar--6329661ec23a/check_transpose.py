"""Exact finite checks for transpose-fixed square chessboard complexes.
No third-party packages are required.  Run: python3 check_transpose.py
"""
from itertools import permutations, combinations
from collections import defaultdict
from math import factorial


def orbit_vertices(n):
    return tuple((i,j) for i in range(n) for j in range(i,n))

def generate_fixed_faces(n):
    """Independent orbit-face generation by recursive support partition."""
    orbs=orbit_vertices(n)
    ind={e:z for z,e in enumerate(orbs)}
    out=set()
    def walk(remaining,selected):
        if not remaining:
            out.add(tuple(sorted(selected)));return
        x=min(remaining);tail=remaining-{x}
        walk(tail,selected)
        walk(tail,selected+(ind[x,x],))
        for y in tail:walk(tail-{y},selected+(ind[x,y],))
    walk(set(range(n)),())
    return orbs,out

def direct_original_invariant(n):
    """Independently enumerate ordinary nonattacking rook placements and test transpose stability."""
    orbs=orbit_vertices(n)
    idx={ij:i for i,ij in enumerate(orbs)}
    got=set()
    def rec(i,cols,squares):
        if i==n:
            S=set(squares)
            if {(j,k) for k,j in S}==S:
                got.add(tuple(sorted({idx[min(i,j),max(i,j)] for i,j in S})))
            return
        rec(i+1,cols,squares)
        for j in range(n):
            if j not in cols:rec(i+1,cols|{j},squares+((i,j),))
    rec(0,set(),())
    return got

def mod2_homology(n,faces):
    dims=defaultdict(list)
    for face in faces:
        if face:dims[len(face)-1].append(face)
    ranks={}
    for d in range(1,max(dims)+1):
        lower={f:i for i,f in enumerate(dims[d-1])}
        pivots={}
        for face in dims[d]:
            v=0
            for i in range(len(face)):
                v^=1<<lower[face[:i]+face[i+1:]]
            while v:
                p=v.bit_length()-1
                if p not in pivots:pivots[p]=v;break
                v^=pivots[p]
        ranks[d]=len(pivots)
    ranks[0]=0
    return [len(dims[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(max(dims)+1)], [len(dims[d]) for d in range(max(dims)+1)]

def odddouble(n):
    ans=1
    for v in range(1,n,2):ans*=v
    return ans

def verify_sign_rep(n,orbs,faces):
    """Check induced orientation signs and functorial group action on relative facets."""
    k=n//2
    full=[f for f in faces if len(f)==k and all(orbs[i][0]!=orbs[i][1] for i in f)]
    assert len(full)==odddouble(n)
    fullset=set(full)
    lookup={x:z for z,x in enumerate(orbs)}
    def act(prm,facet):
        target=[]
        for ix in facet:
            a,b=orbs[ix]
            target.append(lookup[tuple(sorted((prm[a],prm[b])))] )
        inversions=sum(target[i]>target[j] for i in range(k) for j in range(i+1,k))
        to=tuple(sorted(target))
        assert to in fullset
        return to, (-1 if inversions%2 else 1)
    allperms=list(permutations(range(n)))
    for prm in allperms:
        assert sorted(prm)==list(range(n))
        for facet in full:
            image,sgn=act(prm,facet)
            assert sgn in (-1,1)
    # Exhaustive composition for S_4 and sampled, deterministic group pairs in S_6.
    sample=allperms if n<=4 else allperms[::17]
    for p in sample:
        for q in sample:
            pq=tuple(p[q[i]] for i in range(n))
            for facet in full:
                intermediate,sgn_q=act(q,facet)
                out,sgn_p=act(p,intermediate)
                out_direct,sgn_pq=act(pq,facet)
                assert out==out_direct and sgn_pq==sgn_p*sgn_q
    # The stabilizer of the standard perfect matching acts via the sign of
    # permutation of its k blocks, but all flips internal to blocks act trivially.
    std=tuple(lookup[(i,i+1)] for i in range(0,n,2))
    for i in range(k):
        p=list(range(n));p[2*i],p[2*i+1]=p[2*i+1],p[2*i]
        assert act(p,std)==(std,1)
    if k>=2:
        p=list(range(n))
        p[0],p[1],p[2],p[3]=2,3,0,1
        assert act(p,std)==(std,-1)


def check_arbitrary_graphs(n,orbs,all_faces):
    # Exhaust every labelled simple graph on at most five vertices, and an
    # explicitly specified systematic sample on six vertices.
    possible=list(combinations(range(n),2))
    total=1<<len(possible)
    samples=range(total) if n<=5 else range(0,total,137)
    checked=0
    for code in samples:
        E={possible[b] for b in range(len(possible)) if (code>>b)&1}
        restricted={f for f in all_faces if all(orbs[ix][0]==orbs[ix][1] or orbs[ix] in E for ix in f)}
        matchings=sum(1 for f in restricted if len(f)==n//2 and len(f)>0
                       and all(orbs[ix][0]!=orbs[ix][1] for ix in f)) if n%2==0 else 0
        betti,_=mod2_homology(n,restricted)
        predicted={n//2-1:matchings} if n%2==0 else {}
        assert all(v==predicted.get(d,0) for d,v in enumerate(betti)),(n,code,betti,predicted)
        checked+=1
    print('general_graph_n=%d graph_patterns_checked=%d' % (n,checked))


def run():
    for n in range(1,9):
        orbs,faces=generate_fixed_faces(n)
        if n<=7:
            direct=direct_original_invariant(n)
            assert direct==faces,(n,len(direct),len(faces))
        betti,fv=mod2_homology(n,faces)
        k=n//2
        predicted={}
        if n%2==0:predicted[k-1]=odddouble(n)
        for d,v in enumerate(betti):assert v==predicted.get(d,0),(n,d,v,predicted)
        print('n=%d orbits=%d nonempty_faces=%d f=%s reduced_betti_F2=%s' % (n,len(orbs),len(faces)-1,fv,betti))
        if n in (2,4,6):verify_sign_rep(n,orbs,faces)
        if n<=6:check_arbitrary_graphs(n,orbs,faces)
    print('TRANSPOSE_FIXED_GRAPH_BOARD_HOMOLOGY_AND_SYMMETRY_CHECKS_OK')
if __name__=='__main__':run()
