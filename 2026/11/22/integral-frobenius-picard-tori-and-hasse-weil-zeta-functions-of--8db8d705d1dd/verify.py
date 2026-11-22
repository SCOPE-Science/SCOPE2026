#!/usr/bin/env python3
"""Exact Eisenstein-incidence and arithmetic checks for the Hesse 12-line divisor.
Python 3 standard library only. All geometric operations are over Z[omega].
"""
from collections import Counter, deque
from itertools import combinations

Z = (0, 0)
O = (1, 0)
W = (0, 1)
POWERS = [O, W, (-1, -1)]

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)

def conjugate(x):
    return (x[0]-x[1], -x[1])

def norm(x):
    a,b=x
    return a*a-a*b+b*b

def cross(u, v):
    return [sub(mul(u[(i+1)%3], v[(i+2)%3]),
                mul(u[(i+2)%3], v[(i+1)%3])) for i in range(3)]

def dot(u, v):
    return add(add(mul(u[0],v[0]), mul(u[1],v[1])), mul(u[2],v[2]))

def projectively_equal(u, v):
    return all(t == Z for t in cross(u, v))

LINES = [[O,Z,Z],[Z,O,Z],[Z,Z,O]] + [
    [O,POWERS[i],POWERS[j]] for i in range(3) for j in range(3)
]
assert len(LINES) == 12

# All triple determinants: supports a proof of stable concurrence away from 3.
histogram = Counter(norm(dot(LINES[i],cross(LINES[j],LINES[k])))
                    for i,j,k in combinations(range(12),3))
assert histogram == {0:36,1:28,3:81,9:72,27:3},histogram

# Exact projective intersections and incidence edges over the Eisenstein integers.
points = []
for i,j in combinations(range(12),2):
    pt=cross(LINES[i],LINES[j])
    assert any(x!=Z for x in pt)
    if not any(projectively_equal(pt,p) for p in points):
        points.append(pt)
assert len(points)==21
edges=[(i,12+j) for i,l in enumerate(LINES)
                  for j,p in enumerate(points) if dot(l,p)==Z]
assert len(edges)==60
multiplicity = Counter(sum(y==12+j for x,y in edges) for j in range(21))
assert multiplicity == {2:12,4:9}

# Quadratic conjugation is the Frobenius action for q == 2 mod 3.
line_g=[next(j for j,l in enumerate(LINES)
             if projectively_equal([conjugate(x) for x in w],l))
             for w in LINES]
point_g=[next(j for j,p in enumerate(points)
             if projectively_equal([conjugate(x) for x in w],p))
             for w in points]
assert all(line_g[line_g[i]]==i for i in range(12))
assert all(point_g[point_g[i]]==i for i in range(21))
fixed_l=sum(line_g[i]==i for i in range(12))
fixed_p=sum(point_g[i]==i for i in range(21))
fixed_e=sum(line_g[a]==a and point_g[b-12]==b-12 for a,b in edges)
assert (fixed_l,fixed_p,fixed_e)==(4,7,12)
fixed_singular_types = Counter(sum(b==12+j for a,b in edges)
             for j in range(21) if point_g[j]==j)
assert fixed_singular_types=={2:4,4:3}
fixed_branch_counts = sorted(sum(line_g[i]==i for i,k in edges if k==12+j)
                              for j in range(21) if point_g[j]==j)
assert fixed_branch_counts == [0,2,2,2,2,2,2]

# Integral H_1 of the incidence graph, using the fundamental-cycle basis.
adj=[[] for _ in range(33)]
for idx,(a,b) in enumerate(edges):
    adj[a].append((b,idx))
    adj[b].append((a,idx))
parent=[None]*33
parent_edge=[None]*33
parent[0]=-1
queue=deque([0])
while queue:
    a=queue.popleft()
    for b,idx in adj[a]:
        if parent[b] is None:
            parent[b]=a
            parent_edge[b]=idx
            queue.append(b)
assert all(x is not None for x in parent)
tree=set(x for x in parent_edge if x is not None)
chords=[idx for idx in range(60) if idx not in tree]
assert len(chords)==28

def tree_path(start,stop):
    # Retrieve the unique tree path; 33 vertices, so BFS is harmless.
    visited={start:None}
    dq=deque([start])
    while dq:
        a=dq.popleft()
        if a==stop:break
        for b,i in adj[a]:
            if i in tree and b not in visited:
                visited[b]=a
                dq.append(b)
    assert stop in visited
    chain=[stop]
    while chain[-1]!=start:
        chain.append(visited[chain[-1]])
    return list(reversed(chain))

edge_index={edge:idx for idx,edge in enumerate(edges)}
cycles=[]
for chord in chords:
    line,point=edges[chord]
    vec=[0]*60
    vec[chord]=1
    for u,v in zip(tree_path(point,line),tree_path(point,line)[1:]):
        if u<12:
            vec[edge_index[(u,v)]] += 1
        else:
            vec[edge_index[(v,u)]] -= 1
    # Integral boundary zero at every vertex.
    assert all(sum(vec[i] for i,(a,b) in enumerate(edges) if a==v)
                -sum(vec[i] for i,(a,b) in enumerate(edges) if b==v)==0
                for v in range(33))
    cycles.append(vec)

permuted_edge=[edge_index[(line_g[a],12+point_g[b-12])] for a,b in edges]
chord_positions={idx:i for i,idx in enumerate(chords)}
A=[[0]*28 for _ in range(28)]
for col,cyc in enumerate(cycles):
    for eid,coeff in enumerate(cyc):
        mapped=permuted_edge[eid]
        if mapped in chord_positions:
            A[chord_positions[mapped]][col] += coeff
# Involution and trace.
assert all(sum(A[i][k]*A[k][j] for k in range(28))==(i==j)
           for i in range(28) for j in range(28))
trace=sum(A[i][i] for i in range(28))
assert trace == fixed_e-fixed_l-fixed_p+1 == 2

# Rank over F_2 of (A-I). Each regular Z[C_2] summand contributes rank 1.
rows=[]
for i in range(28):
    rows.append(sum((((A[i][j]-(i==j))&1)<<j) for j in range(28)))
pivots={}
for row in rows:
    while row:
        k=row.bit_length()-1
        if k not in pivots:
            pivots[k]=row
            break
        row ^= pivots[k]
c=len(pivots)
a=(28-2*c+trace)//2
b=(28-2*c-trace)//2
assert (a,b,c)==(3,1,12)

# Independent ground-field projective enumerations of the equation.
def count_direct(p):
    projective=[(1,x,y) for x in range(p) for y in range(p)]
    projective += [(0,1,y) for y in range(p)] + [(0,0,1)]
    result=0
    for x,y,z in projective:
        t=x**3+y**3+z**3
        if (x*y*z*(t**3-27*(x*y*z)**3))%p==0:
            result+=1
    return result
for p in (2,3,5,7,11,13,17,19,23,31):
    predicted=(4*p-2 if p==3 else (12*p-27 if p%3==1 else 4*p-1))
    assert count_direct(p)==predicted,(p,count_direct(p),predicted)

print('HESSE_ARITHMETIC_PICARD_TORUS_OK')
print('triple_det_norm_histogram',dict(sorted(histogram.items())))
print('incidence',len(LINES),len(points),len(edges),dict(multiplicity))
print('Galois_fixed',fixed_l,fixed_p,fixed_e,'trace',trace)
print('Z[C2]_summands: trivial',a,'sign',b,'regular',c)
