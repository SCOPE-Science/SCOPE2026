#!/usr/bin/env python3
"""Independent finite checks for three-nonmatching complexes of square bouquets.
Only topology/graph definitions are included, with exhaustive checks at small widths.
"""
from itertools import combinations, product
from collections import defaultdict
from math import comb


def graph_edges(m):
    result=[]
    for i in range(m):
        a,b,c=3*i+1,3*i+2,3*i+3
        result.extend(((0,a),(a,b),(b,c),(c,0)))
    return result

def direct_faces(m):
    edges=graph_edges(m)
    forbidden=[]
    for triple in combinations(range(4*m),3):
        endpoints=[v for index in triple for v in edges[index]]
        if len(set(endpoints))==6:
            forbidden.append(sum(1<<j for j in triple))
    return {s for s in range(1<<(4*m)) if not any(s&x==x for x in forbidden)},len(forbidden)

def expected_parts(m):
    spokes=sum((1<<(4*i))+(1<<(4*i+3)) for i in range(m))
    spoke_indices=[i for i in range(4*m) if i%4 in (0,3)]
    a=set()
    for bits in range(1<<(2*m)):
        sm=sum(1<<spoke_indices[k] for k in range(2*m) if (bits>>k)&1)
        a.add(sm)
        for i in range(m):
            for r in (1,2,3):
                other=((r&1)<< (4*i+1))|(((r>>1)&1)<<(4*i+2))
                a.add(sm|other)
    paths={}
    for i in range(m):
        v=[4*i+j for j in range(4)]
        loc=[0]+[1<<j for j in v]+[(1<<v[k])|(1<<v[k+1]) for k in range(3)]
        paths[i]=loc
    balls={}
    for i,j in combinations(range(m),2):
        balls[i,j]={x|y for x,y in product(paths[i],paths[j])}
    union=set(a)
    for faces in balls.values(): union.update(faces)
    return union,a,balls

def betti_mod2(faces):
    by_dim=defaultdict(list)
    for face in faces:
        if face:by_dim[face.bit_count()-1].append(face)
    ranks={}
    for d in range(1,max(by_dim)+1):
        index={s:i for i,s in enumerate(by_dim[d-1])}
        pivots={}
        for s in by_dim[d]:
            v=0
            for j in range(s.bit_length()):
                if s & (1<<j):v^=1<<index[s^(1<<j)]
            while v:
                p=v.bit_length()-1
                if p in pivots:v^=pivots[p]
                else:pivots[p]=v;break
        ranks[d]=len(pivots)
    out={d:len(faces_d)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
         for d,faces_d in by_dim.items()}
    return {d:v for d,v in out.items() if v}

def parity_to_sort(seq):
    inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inversions%2 else 1

def fundamental_3_chain(i,j):
    assert i<j
    out=defaultdict(int)
    for p,q in product(range(3),range(3)):
        ordered=[4*i+p,4*i+p+1,4*j+q,4*j+q+1]
        assert ordered==sorted(ordered)
        out[tuple(ordered)]+=1
    return {k:v for k,v in out.items() if v}

def transform_chain(chain,perm):
    out=defaultdict(int)
    for simplex,coeff in chain.items():
        v=tuple(perm[x] for x in simplex)
        out[tuple(sorted(v))]+=coeff*parity_to_sort(v)
    return {k:v for k,v in out.items() if v}

def boundary(chain):
    out=defaultdict(int)
    for simplex,coeff in chain.items():
        for k in range(len(simplex)):
            out[simplex[:k]+simplex[k+1:]]+=coeff*(-1 if k%2 else 1)
    return {k:v for k,v in out.items() if v}

def pair_permutations(m):
    for k in range(m):
        p=list(range(4*m))
        p[4*k:4*k+4]=[4*k+3,4*k+2,4*k+1,4*k]
        yield p, list(range(m)), {k:-1}
    for k in range(m-1):
        p=list(range(4*m))
        for t in range(4):
            p[4*k+t]=4*(k+1)+t
            p[4*(k+1)+t]=4*k+t
        sigma=list(range(m));sigma[k],sigma[k+1]=sigma[k+1],sigma[k]
        yield p,sigma,{}

def check(m):
    direct, triples=direct_faces(m)
    union,a,balls=expected_parts(m)
    assert direct==union, (m, len(direct^union))
    for ij,ball in balls.items():
        # Local join is a subdivided 3-ball whose boundary lies entirely in A.
        i,j=ij
        bd={s for s in ball if (s&(3<<(4*i+1))==0) or (s&(3<<(4*j+1))==0)}
        assert ball&a==bd
        assert len(ball)==64 and len(bd)>0
        for kl,ball2 in balls.items():
            if ij!=kl: assert ball&ball2<=a
        f=fundamental_3_chain(i,j)
        assert all(sum(1<<v for v in simplex) in ball for simplex in f)
        assert all(sum(1<<v for v in simplex) in a for simplex in boundary(f))
    if m>=2:
        for perm,sigma,signs in pair_permutations(m):
            for (i,j) in balls:
                ii,jj=sorted((sigma[i],sigma[j]))
                sign=signs.get(i,1)*signs.get(j,1)
                actual=transform_chain(fundamental_3_chain(i,j),perm)
                expect={x:sign*v for x,v in fundamental_3_chain(ii,jj).items()}
                assert actual==expect,(m,i,j,signs)
    if m<=4:
        bet=betti_mod2(direct)
        assert bet==({3:comb(m,2)} if m>=2 else {}),(m,bet)
    print('PASS m=%s edges=%s forbidden_3matchings=%s faces=%s 3ball_pairs=%s mod2_H3=%s symmetries=PASS' %
          (m,4*m,triples,len(direct),len(balls),comb(m,2)))

if __name__=='__main__':
    for m in range(1,5):check(m)
    print('ALL_VERIFY_OK')
