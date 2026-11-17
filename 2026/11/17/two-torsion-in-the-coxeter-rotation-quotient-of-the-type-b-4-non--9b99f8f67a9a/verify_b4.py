#!/usr/bin/env python3
"""Exact integral cellular computation for the Coxeter-rotation quotient of NC(B4)."""
from collections import Counter, deque
from itertools import combinations
from math import comb
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 4
ONE = (1,2,3,4)
COX = (2,3,4,-1)

def evaluate(w, i):
    return (1 if i > 0 else -1) * w[abs(i)-1]
def compose(a,b):
    return tuple(evaluate(a,j) for j in b)
def inverse(w):
    v=[0]*N
    for i,j in enumerate(w,1):v[abs(j)-1]=(1 if j>0 else -1)*i
    return tuple(v)
def power(w,k):
    x=ONE
    for _ in range(k):x=compose(w,x)
    return x

# Exactly the N^2 signed-coordinate reflections of Weyl group B_N.
reflections=[]
for i in range(1,N+1):
    a=list(ONE);a[i-1]=-i;reflections.append(tuple(a))
for i,j in combinations(range(1,N+1),2):
    for sign in (1,-1):
        a=list(ONE);a[i-1]=sign*j;a[j-1]=sign*i;reflections.append(tuple(a))
assert len(reflections)==16 and all(compose(t,t)==ONE for t in reflections)

# Breadth-first shortest reflection lengths on all signed permutations.
length={ONE:0}; todo=deque([ONE])
while todo:
    x=todo.popleft()
    for r in reflections:
        y=compose(x,r)
        if y not in length:
            length[y]=length[x]+1;todo.append(y)
assert len(length)==384
assert Counter(length.values())=={0:1,1:16,2:86,3:176,4:105}
assert power(COX,8)==ONE and all(power(COX,k)!=ONE for k in range(1,8))

def is_below(x,y):
    return length[x]+length[compose(inverse(x),y)]==length[y]
noncrossing={x for x in length if is_below(x,COX)}
assert len(noncrossing)==comb(8,4)==70
assert Counter(length[x] for x in noncrossing)=={0:1,1:16,2:36,3:16,4:1}

def rotate(x):
    return compose(COX,compose(x,inverse(COX)))
assert all(rotate(x) in noncrossing and length[rotate(x)]==length[x] for x in noncrossing)

def orbit_min(chain):
    images=[]
    current=chain
    for _ in range(8):
        images.append(current)
        current=tuple(rotate(x) for x in current)
    assert current==chain
    return min(images)

ranks={k:[w for w in noncrossing if length[w]==k] for k in (1,2,3)}
# All strict chains of the proper part, ordered by reflection length.
chains={0:[(x,) for x in ranks[1]+ranks[2]+ranks[3]],1:[],2:[]}
for a in ranks[1]:
    for b in ranks[2]:
        if is_below(a,b):chains[1].append((a,b))
    for c in ranks[3]:
        if is_below(a,c):chains[1].append((a,c))
for b in ranks[2]:
    for c in ranks[3]:
        if is_below(b,c):chains[1].append((b,c))
for a in ranks[1]:
    for b in ranks[2]:
        if is_below(a,b):
            for c in ranks[3]:
                if is_below(b,c):chains[2].append((a,b,c))
assert tuple(len(chains[d]) for d in range(3))==(68,288,256)
cell={d:sorted({orbit_min(ch) for ch in chains[d]}) for d in range(3)}
assert tuple(len(cell[d]) for d in range(3))==(18,72,64)
index={d:{ch:i for i,ch in enumerate(cell[d])} for d in range(3)}
boundary={}
for d in (1,2):
    matrix=zeros(len(cell[d-1]),len(cell[d]))
    for col,ch in enumerate(cell[d]):
        for i in range(d+1):
            face=ch[:i]+ch[i+1:]
            matrix[index[d-1][orbit_min(face)],col]+=(-1)**i
    boundary[d]=matrix
assert boundary[1]*boundary[2]==zeros(len(cell[0]),len(cell[2]))

# Exact Smith reductions, over ZZ (not rational ranks or a modular heuristic).
def smith_data(matrix):
    D=smith_normal_form(matrix,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(matrix.shape)) if D[i,i]!=0]
d1=smith_data(boundary[1]);d2=smith_data(boundary[2])
assert Counter(d1)=={1:17}
assert Counter(d2)=={1:54,2:1}
# Connected H0, torsion H1 = Z/2, free H2 of rank 64-55=9.
print('B4_CYCLIC_NC_QUOTIENT_EXACT_PASS group=384 interval=70 cells=18,72,64')
print('d1_smith: '+str(Counter(d1)))
print('d2_smith: '+str(Counter(d2)))
print('H0=Z H1=Z/2 H2=Z^9')
