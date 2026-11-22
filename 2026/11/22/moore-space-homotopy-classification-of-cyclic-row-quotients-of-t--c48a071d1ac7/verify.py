#!/usr/bin/env python3
"""Reconstruct cyclic row-orbit cells and verify the explicit collapse of rook complexes.
Run: python3 verify.py (standard library only).
"""
from itertools import combinations, permutations
from math import comb

def inv(word):
    return tuple(-t for t in reversed(word))

def reduce_word(word):
    a=[]
    for t in word:
        if a and a[-1]==-t:a.pop()
        else:a.append(t)
    return tuple(a)

def substitute(word,variable,replacement):
    out=[]
    for t in word:
        if t==variable:out.extend(replacement)
        elif t==-variable:out.extend(inv(replacement))
        else:out.append(t)
    return reduce_word(out)

def qcells(n):
    # C3 action on row coordinates: faces are injections from columns to Z/3.
    faces=[]
    for size in (1,2,3):
        for cols in combinations(range(n),size):
            for rows in permutations(range(3),size):
                orbit=tuple(sorted(tuple((r+a)%3 for r in rows) for a in range(3)))
                if (cols,orbit) not in faces:faces.append((cols,orbit))
    bysz={k:[z for z in faces if len(z[0])==k] for k in (1,2,3)}
    assert len(bysz[1])==n and len(bysz[2])==2*comb(n,2) and len(bysz[3])==2*comb(n,3)
    return bysz

def check(n):
    bysz=qcells(n)
    # Quotient edge (i,j,d), d = row(j)-row(i) mod 3. Edge orientation i to j.
    edges=[(i,j,d) for i,j in combinations(range(n),2) for d in (1,2)]
    faces=[(i,j,k,p) for i,j,k in combinations(range(n),3) for p in (1,2)]
    boundary={e:{e[0]:-1,e[1]:1} for e in edges}
    for i,j,k,p in faces:
        tri=[((i,j,p),1),((j,k,p),1),((i,k,3-p),-1)]
        # Each triangle must be the C3-orbit of three nonattacking rooks.
        dd={v:0 for v in range(n)}
        for e,c in tri:
            for v,b in boundary[e].items():dd[v]+=c*b
        assert not any(dd.values()), (n,i,j,k,p)
    # Contract the tree edges (0,j,1), and eliminate (i,j,d) (i,j >=1).
    remaining={j:(j,) for j in range(1,n)}
    words=[]
    for i,j,k,p in faces:
        if i==0:continue
        if p==1:word=(j,k,i)
        else:word=(-i,-j,-k)
        words.append(((i,j,k,p),word))
    if n==3:
        assert not words
        return 'wedge of 2 circles',0
    if n==4:
        assert len(words)==2
        # The relator x2 x3 x1 kills x1. Remaining is conjugate to a commutator.
        rem=substitute(words[1][1],1,(-3,-2))
        assert rem== (2,3,-2,-3),rem
        return 'torus',0
    # Kill x1 by triangle 123, x4 by triangle 124, x2 by triangle 134;
    # then kill x5,...,x_{n-1} by triangle 12i.
    chosen=[(1,2,3,1),(1,2,4,1),(1,3,4,1)]+[(1,2,i,1) for i in range(5,n)]
    current=dict(words)
    substitutions=[(1,(-3,-2)),(4,(3,)),(2,(3,))]+[(i,(3,)) for i in range(5,n)]
    for label,(var,rep) in zip(chosen,substitutions):
        assert label in current
        # For an elementary elimination, its boundary word contains var just once.
        assert sum(abs(x)==var for x in current[label])==1,(n,label,current[label],var)
        assert reduce_word(substitute(current[label],var,rep))==(),(n,label,current[label],var,rep)
        del current[label]
        current={k:substitute(w,var,rep) for k,w in current.items()}
    assert all(set(abs(x) for x in w)<= {3} for w in current.values())
    assert any(len(w)==3 for w in current.values())
    assert all(len(w) in (0,3) for w in current.values())
    r=len(current)-1
    expected=n*(n-2)*(n-4)//3 - 1
    assert r==expected
    # Check the stable Euler characteristic using all quotient faces.
    euler=n-2*comb(n,2)+2*comb(n,3)
    assert euler==r+1
    # Confirm at least one nontrivial relator (order 3), and all others are null
    # after its 2-cell is attached, giving Moore space plus r spheres.
    return f'M(Z/3,1) wedge {r} two-spheres',r

if __name__=='__main__':
    for n in range(3,12):
        result,r=check(n)
        print(f'n={n}: {result}')
    print('VERIFY_OK')
