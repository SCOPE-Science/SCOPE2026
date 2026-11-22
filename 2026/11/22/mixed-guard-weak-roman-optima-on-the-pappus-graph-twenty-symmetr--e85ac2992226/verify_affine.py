"""Independent affine-geometry verifier for weak Roman defense on Pappus graph.
Run: python3 verify_affine.py
Uses only Python standard-library modules.
"""
from itertools import combinations, permutations
from collections import Counter, deque
N = 18
G = [set() for _ in range(N)]
def add_edge(i,j):
    G[i].add(j); G[j].add(i)
# Point vertices: 3*x+y for x,y in F_3. Line vertices: 9+c: x=c;
# 12+c: y=c; 15+c: y-x=c. All coordinates computed mod 3.
for x in range(3):
    for y in range(3):
        p=3*x+y
        add_edge(p,9+x)
        add_edge(p,12+y)
        add_edge(p,15+(y-x)%3)
assert sum(map(len,G))//2==27 and all(len(ns)==3 for ns in G)
ADJ = [sum(1<<j for j in G[i]) for i in range(N)]
ALL=(1<<N)-1
# Independently compute all dominating supports from closed neighborhoods.
closed=[(1<<i)|ADJ[i] for i in range(N)]
dominated=bytearray(1<<N)
dominated[0]=0
coverage=[0]*(1<<N)
for s in range(1,1<<N):
    bit=s&-s;i=bit.bit_length()-1
    coverage[s]=coverage[s^bit]|closed[i]
    dominated[s]=(coverage[s]==ALL)

def is_wrd(s,t):
    # Support s; vertices carrying two guards t, a subset of s.
    if not dominated[s]:return False
    missing=ALL^s
    while missing:
        b=missing&-missing; missing^=b;v=b.bit_length()-1
        donors=ADJ[v]&s
        if donors&t:continue
        possible=False
        while donors:
            donor=donors&-donors;donors^=donor
            if dominated[(s^donor)|b]:possible=True;break
        if not possible:return False
    return True

opt={}
counts=Counter()
# Independent support/two-set enumeration, unlike ternary-code scan.
for weight in range(9):
    for n2 in range(weight//2+1):
        n1=weight-2*n2
        for t_items in combinations(range(N),n2):
            t=sum(1<<i for i in t_items)
            remaining=[i for i in range(N) if not (t>>i&1)]
            for singles in combinations(remaining,n1):
                s=t|sum(1<<i for i in singles)
                if is_wrd(s,t):
                    counts[(weight,n2)]+=1
                    if weight==8:opt[(s,t)]=True
assert sum(counts.values())==2691
assert counts=={(8,0):1755,(8,1):882,(8,2):54},counts
print('PASS affine independent enumeration: weight 8, 2691 = 1755 + 882 + 54')

# Every automorphism is found from independent affine incidence representation.
# Generate all 108 shore-preserving affine collineations of the three-class
# affine 3-net, and compose with one explicitly verified point-line duality.
lines=[frozenset(G[i]) for i in range(9,18)]
line_index={line:i+9 for i,line in enumerate(lines)}
perms=[]
for a in range(3):
 for b in range(3):
  for c in range(3):
   for d in range(3):
    if (a*d-b*c)%3 == 0:continue
    for tx in range(3):
     for ty in range(3):
      pointmap=[]
      for x in range(3):
       for y in range(3):
        pointmap.append(3*((a*x+b*y+tx)%3)+((c*x+d*y+ty)%3))
      if not all(frozenset(pointmap[p] for p in line) in line_index for line in lines):
       continue
      linemap=[line_index[frozenset(pointmap[p] for p in line)] for line in lines]
      perms.append(tuple(pointmap+linemap))
assert len(perms)==108 and len(set(perms))==108
DUAL=(9,12,15,13,17,11,16,10,14,0,7,5,1,3,8,2,6,4)
perms += [tuple(DUAL[v] for v in p) for p in perms]
assert len(perms)==216 and len(set(perms))==216
# Exhaustively exclude unlisted shore-preserving automorphisms:
# each induces one of the 9! point permutations preserving all nine line triples.
all_line_triples=set(lines)
shore_preserving=sum(all(frozenset(q[x] for x in line) in all_line_triples
                          for line in lines) for q in permutations(range(9)))
assert shore_preserving==108
assert all(all({p[v] for v in G[u]}==G[p[u]] for u in range(N)) for p in perms)
orbit_hist=Counter();rem=set(opt)
while rem:
    s,t=next(iter(rem));orbit=set()
    for perm in perms:
        a=b=0
        for i,j in enumerate(perm):
            if s>>i&1:a|=1<<j
            if t>>i&1:b|=1<<j
        orbit.add((a,b))
    assert orbit<=set(opt)
    rem.difference_update(orbit)
    orbit_hist[(t.bit_count(),len(orbit))]+=1
assert orbit_hist=={(0,27):1,(0,108):8,(0,216):4,(1,18):1,(1,108):2,(1,216):3,(2,54):1},orbit_hist
print('PASS exactly 20 symmetry orbits (13 binary, 6 one-double, 1 two-double)')

# Build one-guard transfer graphs: jump to any vertex, slide along an edge.
J={f:set() for f in opt};L={f:set() for f in opt}
for s,t in opt:
    for u in range(N):
        if not(s>>u&1):continue
        for v in range(N):
            if v==u or t>>v&1:continue
            ss=s;tt=t
            ub=1<<u;vb=1<<v
            if t&ub:tt^=ub # u: 2->1
            else:ss^=ub # u: 1->0
            if s&vb:tt|=vb # v: 1->2
            else:ss|=vb  # v: 0->1
            f=(ss,tt)
            if f in opt:
                J[(s,t)].add(f)
                if ADJ[u]&vb:L[(s,t)].add(f)

def connected_diameter(A):
    assert all(v in A and u in A[v] for u,vs in A.items() for v in vs)
    vertices=list(A)
    hist=Counter();radius=N*2;diam=0
    for source in vertices:
        d={source:0};todo=deque([source])
        while todo:
            u=todo.popleft()
            for v in A[u]:
                if v not in d:d[v]=d[u]+1;todo.append(v)
        assert len(d)==len(vertices),'disconnected'
        e=max(d.values());hist[e]+=1
        diam=max(diam,e);radius=min(radius,e)
    return sum(map(len,A.values()))//2,radius,diam,hist
E1,r1,d1,h1=connected_diameter(J)
E2,r2,d2,h2=connected_diameter(L)
assert (E1,r1,d1)==(18846,8,9),(E1,r1,d1)
assert (E2,r2,d2)==(6372,9,12),(E2,r2,d2)
assert h1=={8:1323,9:1368},h1
assert h2=={9:567,10:1422,11:486,12:216},h2
print('PASS optimal jump graph: 2691 vertices, 18846 edges, radius 8 diameter 9')
print('PASS optimal slide graph: 2691 vertices, 6372 edges, radius 9 diameter 12')
print('PASS eccentricity histograms of both graphs')
