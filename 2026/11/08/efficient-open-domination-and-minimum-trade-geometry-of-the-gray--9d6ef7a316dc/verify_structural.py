#!/usr/bin/env python3
"""Independent affine-Latin-square and cube-gluing verification for Gray incidence codes.

This program does not use exact-cover enumeration or any external package.
Run: python3 verify_structural.py
"""
from collections import Counter, deque
from itertools import combinations, product

points=list(product(range(3),repeat=3))
lines=[]
for direction in range(3):
    for fixed in product(range(3),repeat=2):
        triples=[]
        for t in range(3):
            v=list(fixed);v.insert(direction,t);triples.append(tuple(v))
        lines.append(frozenset(triples))
line_ids={line:i for i,line in enumerate(lines)}

def axial_layer(direction,layer_axis,level):
    return frozenset(line_ids[L] for L in lines
        if len({p[layer_axis] for p in L})==1
        and next(iter(L))[layer_axis]==level
        and len({p[direction] for p in L})==3)

point_codes=[]
for alpha,beta,constant in product((1,2),(1,2),range(3)):
    point_codes.append(frozenset((x,y,(alpha*x+beta*y+constant)%3)
        for x in range(3) for y in range(3)))
assert len(set(point_codes))==12

line_codes={}
pure={}
for d in range(3):
    pure[d]=frozenset(i for i,L in enumerate(lines)
        if len({p[d] for p in L})==3)
    assert len(pure[d])==9
    line_codes[pure[d]]=set()

for a,b in combinations(range(3),2):
    c=next(z for z in range(3) if z not in (a,b))
    cube={}
    for bits in product((0,1),repeat=3):
        s=frozenset().union(*(axial_layer(a if bits[h] else b,c,h) for h in range(3)))
        assert len(s)==9
        cube[bits]=s
        line_codes.setdefault(s,set()).add((a,b))
    # One coordinate flip replaces three rods in a single 3x3 slice.
    for u in cube:
        for v in cube:
            if sum(i!=j for i,j in zip(u,v))==1:
                assert len(cube[u]-cube[v])==3
    assert len(cube)==8
assert len(line_codes)==21

# Test efficient open domination directly from the incidence relation.
for point_code in point_codes:
    for line_code in line_codes:
        for q in points:
            assert sum(q in lines[i] for i in line_code)==1
        for L in lines:
            assert sum(q in L for q in point_code)==1

# Distinct slope pairs give a six-cell Latin trade; equal slopes give nine changes.
pcounts=Counter(len(A-B) for A,B in combinations(point_codes,2))
assert pcounts=={6:54,9:12},pcounts
P=[set() for _ in point_codes]
for i,j in combinations(range(12),2):
    if len(point_codes[i]-point_codes[j])==6:
        P[i].add(j);P[j].add(i)
assert all(len(n)==9 for n in P)
assert [sorted(len(n) for n in P)][:1]==[[9]*12]

# Three Q3 graphs, one per unordered pair of directions, share exactly the
# all-parallel endpoints. The resulting 21-vertex graph has 36 edges.
order=list(line_codes)
position={s:i for i,s in enumerate(order)}
T=[set() for _ in order]
for a,b in combinations(range(3),2):
    c=next(z for z in range(3) if z not in (a,b))
    def tiling(bits):
        return frozenset().union(*(axial_layer(a if bits[h] else b,c,h) for h in range(3)))
    for bits in product((0,1),repeat=3):
        for h in range(3):
            other=tuple(1-v if k==h else v for k,v in enumerate(bits))
            x,y=position[tiling(bits)],position[tiling(other)]
            T[x].add(y);T[y].add(x)
assert sum(map(len,T))//2==36
assert Counter(map(len,T))=={6:3,3:18}

def distance_profile(graph):
    hist=Counter();ecc=[]
    for start in range(len(graph)):
        dis={start:0};work=deque([start])
        while work:
            u=work.popleft()
            for v in graph[u]:
                if v not in dis:
                    dis[v]=dis[u]+1;work.append(v)
        assert len(dis)==len(graph)
        ecc.append(max(dis.values()))
        for end in range(start+1,len(graph)):
            hist[dis[end]]+=1
    return hist,ecc
ph,pe=distance_profile(P)
th,te=distance_profile(T)
assert ph=={1:54,2:12} and set(pe)=={2}
assert th=={1:36,2:63,3:66,4:45} and set(te)=={4}

# Distances in a Cartesian product add. Count ordered pairs by convolution.
po={0:len(P),**{i:2*v for i,v in ph.items()}}
to={0:len(T),**{i:2*v for i,v in th.items()}}
combined=Counter()
for i,a in po.items():
    for j,b in to.items():combined[i+j]+=a*b
hist={d:combined[d]//2 for d in range(1,7)}
assert hist=={1:1566,2:4896,3:8460,4:9180,5:6444,6:1080}
assert sum(hist.values())==252*251//2
print('AFFINE_LATIN_CLASSIFICATION_4_FAMILIES_OF_3_PASS')
print('TWENTY_ONE_LINE_TILINGS_THREE_Q3_GLUE_GRAPH_PASS')
print('FACTOR_GRAPHS_K_3_3_3_3_AND_21_VERTEX_DIAMETER4_PASS')
print('PRODUCT_252_CODES_1566_EDGES_RADIUS6_DIAMETER6_PASS')
print('PRODUCT_ALL_PAIR_DISTANCE_HISTOGRAM_PASS')
