#!/usr/bin/env python3
"""Standalone exact checks for the three-by-five cyclic chessboard quotient.

The proof in RESULT.md supplies the topological interpretation; this script
checks simplex-orbit enumeration, oriented attaching words, and every free-group
Tietze elimination without external packages.
"""
from itertools import combinations
from collections import Counter

N = 5
CELLS = tuple((r,c) for r in range(3) for c in range(N))

def good(s):
    return len({r for r,c in s}) == len(s) and len({c for r,c in s}) == len(s)

def rotate(s,k):
    return tuple(sorted((r,(c+k)%N) for r,c in s))

def canon(s):
    return min(rotate(s,k) for k in range(N))

simplices = [tuple(s for s in combinations(CELLS,d) if good(s)) for d in (1,2,3)]
orbits = [{canon(s) for s in ss} for ss in simplices]
assert [len(s) for s in simplices] == [15,60,60]
assert [len(o) for o in orbits] == [3,12,12]
for ss in simplices:
    for s in ss:
        assert len({rotate(s,k) for k in range(N)}) == 5
print('source simplex counts:', [len(x) for x in simplices])
print('quotient cell counts:', [len(x) for x in orbits])

def edge_label(s):
    a,b = sorted(s)
    r,c = a; rr,cc = b
    if (r,rr)==(0,1):return ('a',(cc-c)%N)
    if (r,rr)==(0,2):return ('b',(cc-c)%N)
    if (r,rr)==(1,2):return ('c',(cc-c)%N)
    raise AssertionError((a,b))

assert {edge_label(s) for s in orbits[1]} == {
    (z,k) for z in 'abc' for k in range(1,N)}

# Every triangle has a representative ((0,0),(1,i),(2,j)) with 1<=i,j<=4,
# i != j; its row-oriented boundary is a_i c_{j-i} b_j^{-1}.
triangles = {((0,0),(1,i),(2,j)) for i in range(1,5)
                                      for j in range(1,5) if i!=j}
assert {canon(t) for t in triangles} == orbits[2]
for ((r0,c0),(r1,i),(r2,j)) in triangles:
    assert (r0,r1,r2)==(0,1,2)
    assert edge_label(((0,0),(1,i)))==('a',i)
    assert edge_label(((1,i),(2,j)))==('c',(j-i)%5)
    assert edge_label(((0,0),(2,j)))==('b',j)

# Free group words: tuple of signed letters, each (letter,index,sign).
def word(*letters):return tuple(letters)
def inv(w):return tuple((a,i,-e) for a,i,e in reversed(w))
def red(w):
    stack=[]
    for a,i,e in w:
        assert e in (-1,1)
        if stack and stack[-1][:2]==(a,i) and stack[-1][2]==-e:stack.pop()
        else:stack.append((a,i,e))
    return tuple(stack)
def sub(w,key,replacement):
    out=[]
    for a,i,e in w:
        v=replacement if e==1 else inv(replacement)
        out.extend(v if (a,i)==key else ((a,i,e),))
    return red(out)
def signed(a,i,e=1):return ((a,i,e),)

def rel(i,j):
    return red((() if i==1 else signed('a',i))
        + signed('c',(j-i)%5)
        + (() if j==1 else signed('b',j,-1)))

R={(i,j):rel(i,j) for i in range(1,5) for j in range(1,5) if i!=j}
assert len(R)==12
# Chosen elimination order; solve U x^e V=1 by x=(U^-1 V^-1)^e.
steps=[((2,1),('a',2)),((3,1),('a',3)),((4,1),('a',4)),
       ((1,2),('b',2)),((1,3),('b',3)),((1,4),('b',4)),
       ((4,3),('c',4)),((2,4),('c',3)),((3,4),('c',1))]
for key,gen in steps:
    w=R.pop(key)
    positions=[k for k,z in enumerate(w) if z[:2]==gen]
    assert len(positions)==1,(key,gen,w)
    pos=positions[0]
    U,V=w[:pos],w[pos+1:]
    value=red(inv(U)+inv(V))
    if w[pos][2]==-1:value=inv(value)
    assert gen not in [z[:2] for z in value]
    assert sub(w,gen,value)==()
    R={k:sub(v,gen,value) for k,v in R.items()}
    print('eliminate',gen,'with',key,'->',value)
assert set(R)=={(2,3),(3,2),(4,2)},R
assert R[(2,3)]==signed('c',2,-1)*5,R
assert R[(3,2)]==signed('c',2,+1)*5,R
assert R[(4,2)]==(),R
print('remaining relators:',R)
print('homotopy result: M(Z/5,1) wedge S2 wedge S2')
print('pi1: Z/5; H1: Z/5; H2: Z^2')
print('universal cover: wedge of 14 two-spheres')
print('integral deck module H2: augmentation ideal Z[C5] plus Z[C5]^2')
print('PASS')
