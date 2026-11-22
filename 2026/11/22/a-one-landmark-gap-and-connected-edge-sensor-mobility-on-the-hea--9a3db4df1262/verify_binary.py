#!/usr/bin/env python3
"""Independent bit-certificate using the binary projective plane and incidence formulas."""
from itertools import combinations
from collections import deque, Counter

# Nonzero triples of F_2^3 (codes 1,...,7). Line j has dot(x,j) = 0.
lines = [frozenset(i for i in range(7) if ((i+1)&(j+1)).bit_count() % 2 == 0) for j in range(7)]
E = sorted((i, 7+j) for j in range(7) for i in lines[j])
assert len(set(lines)) == 7 and len(E) == 21
edge_set = set(E)

# Exact algebraic distance-to-edge formula valid for every Fano incidence edge.
P=[]
for v in range(14):
    row=[]
    for x,y in E:
        if v<7:
            row.append(0 if v==x else 1 if v in lines[y-7] else 2)
        else:
            row.append(0 if v==y else 1 if x in lines[v-7] else 2)
    P.append(row)

# Separate every unordered pair of the 21 edges; no graph-library distances.
pairs=list(combinations(range(21),2))
sep = [sum(1<<idx for idx,(a,b) in enumerate(pairs) if row[a] != row[b]) for row in P]
all_pairs=(1<<len(pairs))-1
ve = [sum(1<<idx for idx, z in enumerate(row) if z<=1) for row in P]
all_edges=(1<<21)-1

def predicate(S):
    u=v=0
    for i in S:
        u|=sep[i]
        v|=ve[i]
    return u==all_pairs, v==all_edges

counts={}
valid=[]
bases5=[]
for k in range(7):
    c=Counter()
    for S in combinations(range(14),k):
        er, dom=predicate(S)
        if er:
            c['edge_metric']+=1
            if k==5:bases5.append(S)
            if dom:
                c['both']+=1
                if k==6:valid.append(sum(1<<v for v in S))
    counts[k]=(c['edge_metric'],c['both'])
assert counts == {0:(0,0),1:(0,0),2:(0,0),3:(0,0),4:(0,0),5:(168,0),6:(1890,1386)}
assert len(valid)==1386
five_masks = {sum(1 << v for v in S) for S in bases5}
contain = Counter(sum((state ^ (1 << v)) in five_masks for v in range(14) if state >> v & 1) for state in valid)
assert contain == {0: 574, 1: 672, 2: 84, 3: 56}
assert all((all_edges ^ __import__('functools').reduce(int.__or__,(ve[i] for i in S),0)).bit_count()==1 for S in bases5)

# State graph edges are detected by exactly two toggled bits; edge-constrained
# replacements require the toggled locations to be incident in the Fano plane.
all_valid=set(valid)
A={x:[] for x in valid}
B={x:[] for x in valid}
for x in valid:
    occupied=[i for i in range(14) if x>>i & 1]
    free=[i for i in range(14) if not (x>>i & 1)]
    for i in occupied:
        for j in free:
            y=x ^ (1<<i) ^ (1<<j)
            if y not in all_valid:continue
            A[x].append(y)
            if (min(i,j), max(i,j)) in edge_set:B[x].append(y)

# Independent BFS routine and all-pair distribution; also validates symmetry.
def summary(graph):
    assert all(x in graph[y] for x in graph for y in graph[x])
    hist=Counter();ecc=Counter()
    for root in valid:
        q=deque([root]); distance={root:0}
        while q:
            v=q.popleft()
            for w in graph[v]:
                if w not in distance:
                    distance[w]=distance[v]+1
                    q.append(w)
        assert len(distance)==len(valid)
        hist.update(distance.values())
        ecc[max(distance.values())]+=1
    hist[0]=len(valid)
    return sum(map(len,graph.values()))//2, Counter(map(len,graph.values())),ecc,tuple(sorted((k,v if k==0 else v//2) for k,v in hist.items()))

j=summary(A);s=summary(B)
assert j[0]==17514 and j[1]==Counter({12:28,21:336,24:168,26:504,30:350})
assert j[2]==Counter({6:1386})
assert j[3]==tuple({0:1386,1:17514,2:133308,3:356608,4:332066,5:109620,6:10689}.items())
assert s[0]==5040 and s[1]==Counter({4:168,6:532,7:168,9:224,10:252,12:42})
assert s[2]==Counter({7:210,8:812,9:364})
assert s[3]==tuple({0:1386,1:5040,2:23940,3:81256,4:194460,5:296464,6:247891,7:97104,8:13314,9:336}.items())

print('model=Fano nonzero binary vectors, dot-product incidence')
print('edge_resolving_by_size', [counts[i][0] for i in range(7)])
print('joint_qualifying_by_size', [counts[i][1] for i in range(7)])
print('all_168_five_edge_metric_bases_miss_one_ve_edge=TRUE')
print('five_basis_containment', sorted(contain.items()))
print('TJ edges',j[0],'degree_histogram',dict(sorted(j[1].items())),'ecc_histogram',dict(sorted(j[2].items())))
print('TS edges',s[0],'degree_histogram',dict(sorted(s[1].items())),'ecc_histogram',dict(sorted(s[2].items())))
print('TJ unordered distance histogram',dict(j[3]))
print('TS unordered distance histogram',dict(s[3]))
print('PASS')
