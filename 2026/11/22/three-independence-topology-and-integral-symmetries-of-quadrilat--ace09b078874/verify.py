#!/usr/bin/env python3
"""Independent finite checks for quadrilateral-book three-independence topology.
Requires only the Python standard library. The uniform proof is mathematical,
not dependent on finite exhaustive enumeration.
"""
from itertools import permutations
from collections import defaultdict

def graph(m):
    nv=2+2*m
    edges=[0]*nv
    def edge(a,b):
        edges[a] |= 1<<b
        edges[b] |= 1<<a
    edge(0,1)
    for i in range(m):
        edge(0,2+2*i); edge(2+2*i,3+2*i); edge(3+2*i,1)
    return edges

def valid(mask, edges, cutoff=3):
    todo=mask
    while todo:
        front=todo&-todo; todo^=front; size=0
        while front:
            v=front&-front; front^=v; size+=1
            if size>cutoff:return False
            w=v.bit_length()-1
            discovered=edges[w]&todo
            front|=discovered;todo^=discovered
    return True

def all_faces(m):
    edges=graph(m)
    return {s for s in range(1<<(2+2*m)) if valid(s,edges)}

def make_sets(m):
    n=2+2*m
    W=sum(1<<j for j in range(2,n))
    W0={0}|{1<<j for j in range(2,n)}
    K=all_faces(m)
    A={s for s in K if not (s&3)}
    U={s for s in K if not (s&2)}
    V={s for s in K if not (s&1)}
    Y=A|U|V
    J={t|s for t in (0,1,2,3) for s in W0}
    D={t|s for t in (0,1,2) for s in W0}
    assert Y|J==K and Y&J==D
    assert all((s&W)==s for s in A)
    assert len(D-{0})==2+2*m+4*m
    return K,Y,J,D

def ranks_mod2(K,n):
    faces=defaultdict(list)
    for mask in K:
        if mask:faces[mask.bit_count()-1].append(mask)
    ranks={}
    for d in range(1,max(faces)+1):
        prev={v:i for i,v in enumerate(faces[d-1])}
        pivots={}
        for face in faces.get(d,[]):
            x=0
            for v in range(n):
                if (face>>v)&1:x^=1<<prev[face^(1<<v)]
            while x:
                top=x.bit_length()-1
                if top in pivots:x^=pivots[top]
                else:pivots[top]=x;break
        ranks[d]=len(pivots)
    bettis={d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d,fs in faces.items()}
    return {d:b for d,b in bettis.items() if b},len(K)-1

def perm_map(m,p,flip):
    mp=list(range(2+2*m))
    if flip:mp[0],mp[1]=1,0
    for i in range(m):
        j=p[i]
        mp[2+2*i]=2+2*j+(1 if flip else 0)
        mp[3+2*i]=2+2*j+(0 if flip else 1)
    assert sorted(mp)==list(range(2+2*m))
    return mp

def trace_via_lefschetz(K,mp):
    # reduced Lefschetz trace from integer-oriented, nonempty simplices.
    z=-1
    for face in K:
        if face==0:continue
        verts=[i for i in range(len(mp)) if face>>i&1]
        mapped=[mp[i] for i in verts]
        if {i for i in mapped}!={i for i in verts}:continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        z+=(-1)**(len(mapped)-1+inversions)
    return z

def test_flap_collapse(m):
    # L_u has no other hubs. Remove the free-face/coface pairs
    # containing each pair a_i,a_j, using a b_k where k differs.
    K=all_faces(m)
    L={s for s in K if not (s&3) and (s|1) in K}
    for i in range(m):
        for j in range(i+1,m):
            c=next(t for t in range(m) if t not in (i,j))
            base=(1<<(2+2*i))|(1<<(2+2*j))
            B=[3+2*t for t in range(m) if t not in (i,j,c)]
            subsets=sorted((sum(1<<v for v in z) for k in range(len(B)+1)
                             for z in __import__('itertools').combinations(B,k)),
                           key=lambda x:-x.bit_count())
            for s in subsets:
                f=base|s;coface=f|(1<<(3+2*c))
                assert f in L and coface in L
                # Confirm the only strict coface of f remaining is coface.
                assert [g for g in L if g!=f and (g&f)==f]==[coface]
                L.remove(f);L.remove(coface)
    # Remaining L is the join of the discrete a_i's and full b-simplex.
    for s in L:
        assert sum(bool(s&(1<<(2+2*i))) for i in range(m))<=1
    return len(L)

def main():
    for m in (3,4,5):
        K,Y,J,D=make_sets(m)
        b,nfaces=ranks_mod2(K,2+2*m)
        assert b=={2:2*m-1},(m,b)
        reduced_faces=test_flap_collapse(m)
        tests=0
        for p in permutations(range(m)):
            f=sum(i==p[i] for i in range(m))
            for flip in (0,1):
                mp=perm_map(m,p,flip)
                observed=trace_via_lefschetz(K,mp)
                predicted=(2*f-1) if not flip else 1
                assert observed==predicted,(m,p,flip,observed,predicted)
                tests+=1
        print(f'm={m}: faces={nfaces}, D_edges={4*m}, L_u_survivor_faces={reduced_faces}, '
              f'reduced_F2_betti={b}, signed_character_tests={tests}: PASS')
    print('All tested identities and signed Lefschetz character checks PASS.')

if __name__=='__main__':main()
