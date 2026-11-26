#!/usr/bin/env python3
"""Independent finite checks for independence complexes of bouquet hexagons.
Requires Python 3.9+ standard library only. The all-parameter proof is textual.
"""
from itertools import combinations, permutations, product
from math import factorial


def graph(m):
    n = 5*m + 1
    edges = set()
    for j in range(m):
        vertices = [0]+[1+5*j+k for k in range(5)]
        for a,b in zip(vertices, vertices[1:] + vertices[:1]):
            edges.add(tuple(sorted((a,b))))
    return n, edges


def independence_faces(m):
    n, edges = graph(m)
    adj = [0]*n
    for a,b in edges:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    faces = [()]
    for x in range(n):
        faces += [face+(x,) for face in faces if all((adj[x]>>y)&1 == 0 for y in face)]
    return faces


def permutation_sign(seq):
    inversions = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inversions%2 else 1


def action(m,pi,mask):
    vmap=[0]
    for i in range(m):
        for k in range(5):
            vmap.append(1+5*pi[i] + (4-k if (mask>>i)&1 else k))
    return vmap


def lefschetz(faces, vmap):
    s=-1  # augmented empty face, degree -1
    for face in faces[1:]:
        image=[vmap[v] for v in face]
        if set(image)==set(face):
            s += (-1 if len(face)%2==0 else 1)*permutation_sign(image)
    return s


def mod_rank(columns):
    piv={}
    for x in columns:
        while x:
            h=x.bit_length()-1
            if h in piv: x ^= piv[h]
            else: piv[h]=x;break
    return len(piv)


def betti_mod2(faces):
    bydim={}
    for face in faces: bydim.setdefault(len(face)-1,[]).append(face)
    ranks={}
    for d in range(0,max(bydim)+1):
        lower={x:i for i,x in enumerate(bydim[d-1])}
        cols=[]
        for t in bydim[d]:
            bits=0
            for i in range(len(t)):
                bits ^= 1<<lower[t[:i]+t[i+1:]]
            cols.append(bits)
        ranks[d]=mod_rank(cols)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,fs in bydim.items() if d>=0 and len(fs)-ranks.get(d,0)-ranks.get(d+1,0)}


def check(m, full):
    faces=independence_faces(m)
    expected={m:1,2*m-1:1}
    if m in (2,3):
        got=betti_mod2(faces)
        assert got==expected, (m,got,expected)
    group=list(permutations(range(m)))
    masks=range(1<<m) if full else [0,1,(1<<m)-1]
    checks=0
    for pi in group:
        pi_sign=permutation_sign(pi)
        for mask in masks:
            predicted=(-1)**m*pi_sign-(-1 if mask.bit_count()%2 else 1)
            result=lefschetz(faces,action(m,pi,mask))
            assert result==predicted,(m,pi,mask,result,predicted)
            checks+=1
    print(f'm={m}: {len(faces)} independent faces including empty; '
          f'{checks} signed Lefschetz actions agree with two-character formula; '
          f'mod-2 full-rank calculation={"checked" if m in (2,3) else "not run"}')


def main():
    for m in (2,3):check(m,True)
    # Additional parameter with sampled local flips and all petal permutations.
    check(4,False)
    print('VERIFY_OK')

if __name__=='__main__': main()
