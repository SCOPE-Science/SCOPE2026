#!/usr/bin/env python3
"""Exact determinant and equality-support enumeration for the square-pentagon free sum.
Only Python standard library; no floating-point steps are used.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from collections import Counter

# An exact real algebraic number a+b*sqrt(5) is represented by (a,b).
def sign(a,b):
    a,b=Fraction(a),Fraction(b)
    if not b: return (a>0)-(a<0)
    if not a: return (b>0)-(b<0)
    if (a>0)==(b>0): return (a>0)-(a<0)
    # Compare |a| with sqrt(5)*|b| exactly.
    d=a*a-5*b*b
    if not d: return 0
    return (1 if a>0 else -1)*(1 if d>0 else -1)

def cmp_coeff(x,y):
    # x=(u,v) means (u*sin(72)+v*sin(36)).
    du,dv=x[0]-y[0],x[1]-y[1]
    return sign(Fraction(du)-Fraction(dv,2), Fraction(dv,2))

def abs_coeff(x):
    return x if cmp_coeff(x,(0,0))>=0 else (-x[0],-x[1])

def add(*xs):
    return (sum(x[0] for x in xs),sum(x[1] for x in xs))

def negate(x): return (-x[0],-x[1])

def sine(q): return ((0,0),(1,0),(0,1),(0,-1),(-1,0))[q%5]

def det_b(i,j,k):
    return add(sine(k-j),negate(sine(k-i)),sine(j-i))

A=((1,0),(0,1),(-1,0),(0,-1))
def detA(i,j): return A[i][0]*A[j][1]-A[i][1]*A[j][0]
def double_tri_A(i,j,k):
    return detA(j,k)-detA(i,k)+detA(i,j)

def det5(sel):
    aa=[i for i in sel if i<4]
    bb=[i-4 for i in sel if i>=4]
    if len(aa)==2 and len(bb)==3:
        t=detA(*aa)
        u,v=det_b(*bb)
        return (t*u,t*v)
    if len(aa)==3 and len(bb)==2:
        t=double_tri_A(*aa)
        return tuple(t*v for v in sine(bb[1]-bb[0]))
    return (0,0)

# These are determinant magnitudes, not volumes (divide by 24).
expected={(0,0):46,(0,2):20,(2,-1):20,(2,0):20,(1,2):20}
spectrum=Counter()
max_vertex=[]
for sel in combinations(range(9),5):
    t=abs_coeff(det5(sel))
    spectrum[t]+=1
    if t==(1,2):max_vertex.append(sel)
assert spectrum==expected,(spectrum,expected)
assert len(max_vertex)==20
assert all(sum(i<4 for i in c)==2 and (c[1]-c[0] in (1,3) or (c[0],c[1])==(0,3)) for c in max_vertex)
assert cmp_coeff((1,2),(2,0))>0
assert cmp_coeff((2,0),(2,-1))>0
assert cmp_coeff((2,-1),(0,2))>0

# Positive-order maximizing pentagon triples. Correct orientation matters:
# convex-combination determinant equality demands the SAME signed extremum.
max_triples={tr for tr in permutations(range(5),3) if det_b(*tr)==(1,2)}
assert len(max_triples)==15
unordered_triples={frozenset(t) for t in max_triples}
assert unordered_triples=={frozenset(((i)%5,(i+1)%5,(i+3)%5)) for i in range(5)}

# All independently allowed vertex-support sets for ordered triples in
# the regular pentagon. If a point has a nontrivial convex support, it
# permits ALL Cartesian-product tuples: this is a necessary and sufficient
# condition by determinant multilinearity.
subsets=[tuple(i for i in range(5) if mask>>i&1) for mask in range(1,32)]
supports=[]
for triple in product(subsets,repeat=3):
    if all(v in max_triples for v in product(*triple)):
        supports.append(triple)
assert len(supports)==30
singleton=[s for s in supports if sum(len(a)-1 for a in s)==0]
moving=[s for s in supports if sum(len(a)-1 for a in s)==1]
assert len(singleton)==15 and len(moving)==15
assert all(sorted(len(a) for a in s)==[1,1,2] for s in moving)
assert all((s[j][1]-s[j][0])%5 in (1,4) for s in moving for j in range(3) if len(s[j])==2)

# Equality graph of unordered vertex triples: an edge represents the
# motion of one apex along a polygon edge with two other vertices fixed.
triangles=list(unordered_triples)
graph={t:set() for t in triangles}
for s in moving:
    pair={frozenset(x) for x in product(*s)}
    assert len(pair)==2
    u,v=tuple(pair)
    graph[u].add(v);graph[v].add(u)
assert len(graph)==5 and all(len(v)==2 for v in graph.values())
seen={next(iter(graph))}
frontier=list(seen)
while frontier:
    for nxt in graph[frontier.pop()]:
        if nxt not in seen:seen.add(nxt);frontier.append(nxt)
assert len(seen)==5

# The four square-pair choices are isolated, so the full moduli consist
# of 4 separate pentagonal loops with 20 vertices and 20 open edges.
assert len({tuple(i for i in c if i<4) for c in max_vertex})==4
print('PASS exact spectrum:',dict(sorted(spectrum.items())))
print('PASS top ordered maximal triangles:',len(max_triples))
print('PASS equality support systems:',len(singleton),'isolated vertex orderings +',len(moving),'one-vertex slide orderings')
print('PASS full maximal-simplex moduli: 4 disjoint pentagonal cycles, 20 vertex simplices and 20 moving segments')
