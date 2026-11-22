#!/usr/bin/env python3
"""Independent finite signed Lefschetz and boundary-rank checks for pentagonal windmill matching complexes."""
from itertools import permutations, product
from math import factorial

def graph(n):
    # vertices: center -1 and (blade, position 1..4)
    edges=[]
    for i in range(n):
        for j in range(5):
            a=(-1 if j==0 else (i,j))
            k=(j+1)%5
            b=(-1 if k==0 else (i,k))
            edges.append(frozenset((a,b)))
    return edges

def faces(edges):
    out=[()]
    for j,e in enumerate(edges):
        out += [face+(j,) for face in list(out) if all(e.isdisjoint(edges[z]) for z in face)]
    return out

def edge_permutation(edges,pi,flips):
    lookup={e:i for i,e in enumerate(edges)}
    def g(x):
        if x==-1:return -1
        i,j=x
        return (pi[i],5-j if flips[i] else j)
    return tuple(lookup[frozenset(g(x) for x in e)] for e in edges)

def sign_of_perm(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def direct_char(faces,edge_map,n):
    total=0
    for f in faces:
        mapped=tuple(edge_map[e] for e in f)
        if set(mapped)!=set(f):continue
        # Trace in augmented chain group is (-1)^orbits.
        orbits=0
        todo=set(f)
        while todo:
            orbits+=1
            a=next(iter(todo))
            while a in todo:
                todo.remove(a)
                a=edge_map[a]
        total+=(-1)**orbits
    return (-1)**(n+1)*total

def predicted(pi,flips):
    f0=sum(pi[i]==i and not flips[i] for i in range(len(pi)))
    return sign_of_perm(pi)*(2*f0-1)

def gf2_betti(allfaces):
    bydeg={}
    for f in allfaces:
        bydeg.setdefault(len(f)-1,[]).append(f)
    ranks={}
    for d,faces_d in bydeg.items():
        if d<0: continue
        prev={f:i for i,f in enumerate(bydeg.get(d-1,[]))}
        if d==0: continue
        basis={}
        for face in faces_d:
            col=0
            for j in range(len(face)):
                col ^=1<<prev[face[:j]+face[j+1:]]
            while col:
                pivot=col.bit_length()
                if pivot in basis:col^=basis[pivot]
                else: basis[pivot]=col;break
        ranks[d]=len(basis)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0) - (1 if d==0 else 0) for d,fs in bydeg.items() if d>=0}

checks=0
for n in range(2,5):
    es=graph(n)
    fs=faces(es)
    assert len(es)==5*n
    print('size n',n,'faces',len(fs),'maxdim',max(map(len,fs))-1)
    for pi in permutations(range(n)):
        for bits in product((0,1),repeat=n):
            edge_map=edge_permutation(es,pi,bits)
            calc=direct_char(fs,edge_map,n)
            expected=predicted(pi,bits)
            assert calc==expected,(n,pi,bits,calc,expected)
            checks+=1
    betti=gf2_betti(fs)
    assert betti.get(n,0)==2*n-1 and all(v==0 for k,v in betti.items() if k!=n),(n,betti)
    print('homology n',n,betti)
print('checked group elements',checks)
# n=5 independent sample including nontrivial flips and permutations
n=5
es=graph(n);fs=faces(es)
for pi in [tuple(range(n)),(1,2,3,4,0),(1,0,2,3,4),(1,0,3,2,4),(4,3,2,1,0)]:
    for bits in [(0,)*n,(1,)*n,(1,0,0,0,0),(1,0,1,0,1)]:
        x=direct_char(fs,edge_permutation(es,pi,bits),n)
        assert x==predicted(pi,bits),(n,pi,bits,x,predicted(pi,bits))
        checks+=1
print('n5 sample checked',20,'faces',len(fs))
print('VERIFY_OK')
