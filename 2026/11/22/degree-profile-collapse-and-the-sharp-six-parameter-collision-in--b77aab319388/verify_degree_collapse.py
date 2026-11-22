"""Independent verification of clique-free one-point type polynomial and sharp C4 boundary.
Only Python standard library. Run: python3 verify_degree_collapse.py
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import comb


def poly_add(*polys):
    ans=[0]*max(map(len,polys))
    for p in polys:
        for k,v in enumerate(p): ans[k]+=v
    return tuple(ans)

def poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return tuple(r)

def one_plus(n):return tuple(comb(n,k) for k in range(n+1))

def poly(F,a,b,c):
    """Directly enumerate all finite graph neighborhoods (not the theorem formula)."""
    N=a+b+c
    removed=set(F)
    edges=set()
    for i in range(a):
        for j in range(b):
            if (i,j) not in removed: edges.add(frozenset((i,a+j)))
    for x in range(a+b):
        for y in range(a+b,N):edges.add(frozenset((x,y)))
    triangles=[]
    for triple in combinations(range(N),3):
        if all(frozenset(pair) in edges for pair in combinations(triple,2)):
            triangles.append(sum(1<<v for v in triple))
    p=[0]*(N+1)
    for bits in range(1<<N):
        if not any((bits&t)==t for t in triangles):p[bits.bit_count()]+=1
    while p and not p[-1]:p.pop()
    return tuple(p)

def deg_formula(F,a,b,c):
    degrees=[0]*(a+b)
    for i,j in F:
        degrees[i]+=1
        degrees[a+j]+=1
    q=list(poly_add(one_plus(a),one_plus(b)))
    q[0]-=1
    while len(q)<4:q.append(0)
    for d in degrees:
        for k in range(1,d+1):
            while len(q)<=k+1:q.append(0)
            q[k+1]+=comb(d,k)
    q[2]-=len(F)
    # (1+z)^(a+b) + [(1+z)^c-1]Q(z)
    factor=list(one_plus(c));factor[0]-=1
    r=list(poly_add(one_plus(a+b),poly_mul(factor,q)))
    while r and not r[-1]:r.pop()
    return tuple(r)

def count_4cycles(F,a,b):
    return sum(1 for i,k in combinations(range(a),2)
                 for j,l in combinations(range(b),2)
                 if all((x,y) in F for x in (i,k) for y in (j,l)))

def canonical(F,a,b):
    """Exact part-preserving isomorphism, also allowing whole-shore swap if a=b."""
    possibilities=[]
    for pa in permutations(range(a)):
        for pb in permutations(range(b)):
            possibilities.append(tuple(sorted((pa[i],pb[j]) for i,j in F)))
    if a==b:
        for pa in permutations(range(b)):
            for pb in permutations(range(a)):
                possibilities.append(tuple(sorted((pa[j],pb[i]) for i,j in F)))
    return min(possibilities)

checked=0; sharp_checks=0; five_fibres=[]
for n in range(2,6):
    for a in range(1,n):
        b=n-a
        if a>b:continue
        fingerprints=defaultdict(set)
        for bits in range(1<<(a*b)):
            F={(i,j) for i in range(a) for j in range(b) if bits>>(i*b+j)&1}
            c4=count_4cycles(F,a,b)
            for c in (1,2):
                direct=poly(F,a,b,c)
                predicted=deg_formula(F,a,b,c)
                if c4==0:
                    assert direct==predicted,(a,b,c,F,direct,predicted)
                    if c==1:
                        fingerprints[direct].add(canonical(F,a,b))
                else:
                    # First missing coefficient is c times the number of four-cycles.
                    diff=[(direct[k] if k<len(direct) else 0)-(predicted[k] if k<len(predicted) else 0)
                          for k in range(max(len(direct),len(predicted)))]
                    assert all(x==0 for x in diff[:5]) and diff[5]==c*c4
                    sharp_checks+=1
                checked+=1
        if n<=4:
            assert all(len(s)==1 for s in fingerprints.values()),(a,b,fingerprints)
        if n==5:
            five_fibres += [(a,b,poly,len(s)) for poly,s in fingerprints.items() if len(s)>1]

assert five_fibres==[(2,3,(1,6,15,16,7,1),2)],five_fibres

# Witnesses: two deleted-edge forests, equal spectra but different old degree lists.
a,b=2,3
Fa={(0,0),(0,1)}
Fb={(0,0),(1,0)}
assert canonical(Fa,a,b)!=canonical(Fb,a,b)
for c in range(1,8):
    # Vertex degrees in the two full graphs have a constant cubic-moment gap.
    degA=[c+1]*3+[c+2,c+3]+[5]*c
    degB=[c]+[c+2]*4+[5]*c
    assert sum(x**3 for x in degA)-sum(x**3 for x in degB)==6
    p=poly(Fa,a,b,c)
    assert p==poly(Fb,a,b,c)==deg_formula(Fa,a,b,c)
    assert sum(p)==18+14*(2**c)
assert poly(Fa,2,3,1)==(1,6,15,16,7,1)
assert count_4cycles(Fa,2,3)==count_4cycles(Fb,2,3)==0

# C4 produces an exact extra term z^4 in the bipartite rectangle polynomial,
# hence c z^5 at the type-polynomial level.
assert count_4cycles({(0,0),(0,1),(1,0),(1,1)},2,2)==1
print('VERIFY_OK', 'graph_instances',checked,'positive_C4_instances',sharp_checks,
      'first_collision_defect_vertices',5,'witness_types',46)
