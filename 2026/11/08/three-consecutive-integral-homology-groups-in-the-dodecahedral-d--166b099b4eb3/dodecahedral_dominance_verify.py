#!/usr/bin/env python3
"""Exact integral homology certificate for the dodecahedral dominance complex.

Standard-library-only; enumerate every subset, verify two face tests, check
acyclicity of two Morse matchings on the full face Hasse digraph, and calculate
signed Morse boundaries by exact elementary chain cancellation.
"""
from array import array
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

EDGES = ((0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),
         (3,19),(4,5),(4,17),(5,6),(5,15),(6,7),(7,8),(7,14),
         (8,9),(9,10),(9,13),(10,11),(11,12),(11,18),(12,13),
         (12,16),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19))
N = 20
LIMIT = 1 << N
FULL = LIMIT-1
adj = [0]*N
for a,b in EDGES:
    assert 0 <= a < b < N
    adj[a] |= 1 << b
    adj[b] |= 1 << a
assert len(set(EDGES)) == 30 and all(a.bit_count()==3 for a in adj)
# Explicit graph isomorphism to the standard generalized Petersen GP(10,2).
TO_GP=(0,1,2,12,14,4,3,13,11,19,9,8,7,17,15,5,6,16,18,10)
GP_EDGES=set()
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        GP_EDGES.add(tuple(sorted((a,b))))
assert set(TO_GP)==set(range(20))
assert {tuple(sorted((TO_GP[a],TO_GP[b]))) for a,b in EDGES}==GP_EDGES
closed = [adj[i] | (1<<i) for i in range(N)]

# The two criteria are logically equivalent, but implemented separately.
face_bits = bytearray(LIMIT)
faces = []
for s in range(1,LIMIT):
    isface = not any((s & neighborhood)==neighborhood for neighborhood in closed)
    if isface:
        face_bits[s]=1
        faces.append(s)
assert len(faces)==425028
for s in range(1,LIMIT):
    if face_bits[s]:
        comp=FULL ^ s
        dominated=comp
        b=comp
        while b:
            u=b & -b
            dominated |= adj[u.bit_length()-1]
            b ^= u
        assert dominated==FULL
    else:
        comp=FULL ^ s
        # A vertex is undominated iff its closed neighborhood is entirely in s.
        assert any((closed[v] & comp)==0 for v in range(N))
fvec=dict(sorted(Counter(s.bit_count()-1 for s in faces).items()))
assert fvec=={0:20,1:190,2:1140,3:4825,4:15184,5:36390,6:66800,
              7:93060,8:95900,9:69644,10:32680,11:8405,12:780,13:10}
print('faces',len(faces),'f_vector',fvec)

def make_matching(order):
    match={}
    for pivot in order:
        b=1<<pivot
        for s in faces:
            if s & b or s in match: continue
            t=s|b
            if face_bits[t] and t not in match:
                match[s]=t
                match[t]=s
    critical=sorted(s for s in faces if s not in match)
    assert len(match)%2==0
    return match,critical

def check_acyclic(match):
    indeg=array('i',[0])*LIMIT
    cover_edges=0
    for t in faces:
        bits=t
        while bits:
            lb=bits & -bits
            s=t^lb
            bits^=lb
            if s==0: continue
            cover_edges+=1
            if match.get(s)==t:
                indeg[t]+=1 # reverse matched edge s -> t
            else:
                indeg[s]+=1 # ordinary Hasse edge t -> s
    q=deque(s for s in faces if indeg[s]==0)
    visited=0
    while q:
        t=q.popleft()
        visited+=1
        bits=t
        while bits:
            lb=bits & -bits
            s=t^lb
            bits^=lb
            if s and match.get(s)!=t:
                indeg[s]-=1
                if indeg[s]==0:q.append(s)
        upper=match.get(t)
        if upper is not None and upper.bit_count()==t.bit_count()+1:
            indeg[upper]-=1
            if indeg[upper]==0:q.append(upper)
    assert visited==len(faces), (visited,len(faces))
    assert all(indeg[s]==0 for s in faces)
    return cover_edges

def signed_differentials(match,critical):
    dim=defaultdict(list)
    for s in critical: dim[s.bit_count()-1].append(s)
    @lru_cache(maxsize=None)
    def reduced(s):
        t=match.get(s)
        if t is None:return {s:1}
        if t.bit_count()<s.bit_count():return {}
        bit=(s^t).bit_length()-1
        pos=(s & ((1<<bit)-1)).bit_count()
        a = -1 if pos%2 else 1 # oriented incidence of s in t
        ans=defaultdict(int)
        for j in range(N):
            lb=1<<j
            if not (t & lb) or j==bit:continue
            u=t^lb
            p=(t & (lb-1)).bit_count()
            c=-a*(-1 if p%2 else 1)
            for f,val in reduced(u).items():ans[f]+=c*val
        return {f:val for f,val in ans.items() if val}
    def boundary(d):
        lower=dim[d-1]
        upper=dim[d]
        cols=[]
        for t in upper:
            row=defaultdict(int)
            bits=t
            while bits:
                lb=bits & -bits
                j=lb.bit_length()-1
                bits ^= lb
                u=t^lb
                sign=-1 if (t & (lb-1)).bit_count()%2 else 1
                for f,val in reduced(u).items():row[f]+=sign*val
            cols.append([row[s] for s in lower])
            assert not any(f not in lower for f in row if row[f])
        return cols
    return dim,boundary(10),boundary(11),reduced.cache_info()

def rank_exact(columns):
    if not columns:return 0
    a=[[Fraction(x) for x in col] for col in columns]
    m=len(a);n=len(a[0]);pivot=0
    for j in range(n):
        if pivot==m:break
        ix=next((i for i in range(pivot,m) if a[i][j]),None)
        if ix is None:continue
        a[pivot],a[ix]=a[ix],a[pivot]
        c=a[pivot][j]
        a[pivot]=[x/c for x in a[pivot]]
        for k in range(m):
            if k==pivot or a[k][j]==0:continue
            v=a[k][j]
            a[k]=[x-v*y for x,y in zip(a[k],a[pivot])]
        pivot+=1
    return pivot

def det(matrix):
    n=len(matrix)
    if n==1:return matrix[0][0]
    if n==2:return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    return sum(((-1)**j)*x*det([row[:j]+row[j+1:] for row in matrix[1:]]) for j,x in enumerate(matrix[0]))

def primitive_unit_minor(cols,rank):
    rows=len(cols[0]) if cols else 0
    for selected_columns in combinations(range(len(cols)),rank):
        for selected_rows in combinations(range(rows),rank):
            a=[[cols[i][j] for i in selected_columns] for j in selected_rows]
            v=det(a)
            if abs(v)==1:return selected_columns,selected_rows,v
    raise AssertionError('No unit maximal minor')

def verify(order,expected_counts,expected_ranks):
    match,crit=make_matching(order)
    counts=dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))
    assert counts==expected_counts,(counts,expected_counts)
    covers=check_acyclic(match)
    dims,d10,d11,cache=signed_differentials(match,crit)
    r10,r11=rank_exact(d10),rank_exact(d11)
    assert (r10,r11)==expected_ranks,((r10,r11),expected_ranks)
    # d11 is 11 -> 10; d10 is 10 -> 9, columns transposed convention.
    for col11 in d11:
        for row9 in range(len(d10[0])):
            assert sum(col11[j]*d10[j][row9] for j in range(len(col11)))==0
    witness10=primitive_unit_minor(d10,r10)
    witness11=primitive_unit_minor(d11,r11) if r11 else None
    b9=len(dims[9])-r10
    b10=len(dims[10])-r10-r11
    b11=len(dims[11])-r11
    assert (b9,b10,b11)==(12,1,10)
    print('matching',list(order),'critical',counts,'pairs',len(match)//2,
          'Hasse_covers',covers,'Morse_ranks',(r10,r11))
    print('unimodular_minors',witness10,witness11,'Morse_cache',cache)
    return d10,d11,covers

reverse10,reverse11,covers=verify(range(19,-1,-1),{0:1,9:14,10:3,11:10},(2,0))
assert all(not any(col) for col in reverse11)
assert all(a==b-c for a,b,c in zip(*reverse10))
print('reverse_Morse_boundary_10_columns',reverse10)
assert [col[5] for col in reverse10]==[-1,-1,0]
assert [col[9] for col in reverse10]==[-1,0,1]
forward10,forward11,covers2=verify(range(20),{0:1,9:15,10:6,11:12},(3,2))
assert covers==covers2
print('reduced_integral_homology',{9:'Z^12',10:'Z',11:'Z^10'},
      'connectivity',8)
print('DODECAHEDRAL_DOMINANCE_INTEGRAL_HOMOLOGY_PASS')
