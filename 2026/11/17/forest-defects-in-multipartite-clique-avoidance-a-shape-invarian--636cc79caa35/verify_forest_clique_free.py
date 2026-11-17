"""Finite checks of clique-avoidance complexes of multipartite forest defects.
No external packages. Run with Python 3.10 or newer.
Finite tests corroborate but do not replace the universal homotopy proof.
"""
from itertools import combinations, product

def forest_components(a, b, edges):
    parent = list(range(a+b))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for x,y in edges:
        u,v = root(x),root(a+y)
        if u == v:
            return None
        parent[u] = v
    return len({root(x) for x,y in edges} | {root(a+y) for x,y in edges})

def check_folds(a, b, missing):
    aa,bb = set(range(a)),set(range(b))
    missing=set(missing)
    reductions=0
    while True:
        candidates=[]
        for side, vertices, other in [(0, aa,bb),(1,bb,aa)]:
            for v in sorted(vertices):
                for u in sorted(vertices):
                    if u==v: continue
                    def neigh(x):
                        return {z for z in other if ((x,z) if side==0 else (z,x)) not in missing}
                    if neigh(u) <= neigh(v):
                        candidates.append((side,v))
                        break
        if not candidates:break
        side,v=candidates[0]
        (aa if side==0 else bb).remove(v)
        reductions+=1
    edges={(x,y) for x,y in missing if x in aa and y in bb}
    assert len(edges)==len({x for x,y in edges})==len({y for x,y in edges})
    return reductions,len(edges)

def all_faces(sizes, missing):
    parts=[]; idx=0
    for size in sizes:
        parts.append(list(range(idx,idx+size)));idx+=size
    n=idx; r=len(parts)
    a,b=sizes[:2]
    M={(x,a+y) for x,y in missing}
    all_cliques=[]
    for pts in product(*parts):
        if (pts[0],pts[1]) not in M:
            all_cliques.append(sum(1<<x for x in pts))
    faces=[]
    for f in range(1<<n):
        direct = all((f & c)!=c for c in all_cliques)
        meets=[any(f&(1<<v) for v in P) for P in parts]
        formula = (not all(meets)) or all((x,y) in M for x in parts[0] if f&(1<<x) for y in parts[1] if f&(1<<y))
        assert direct==formula, (sizes,missing,f)
        if direct:faces.append(f)
    return faces

def homology_mod2(faces):
    by={}
    for f in faces:
        if f:by.setdefault(f.bit_count()-1,[]).append(f)
    rank={}
    for k in range(1,max(by)+1):
        low={m:i for i,m in enumerate(by.get(k-1,[]))}
        piv={}
        for face in by.get(k,[]):
            x=face; v=0
            while x:
                bit=x & -x
                v ^= (1<<low[face^bit]);x-=bit
            while v:
                p=v.bit_length()-1
                if p in piv:v ^= piv[p]
                else:piv[p]=v;break
        rank[k]=len(piv)
    return [(k,len(fs)-rank.get(k,0)-rank.get(k+1,0)-(k==0)) for k,fs in sorted(by.items()) if len(fs)-rank.get(k,0)-rank.get(k+1,0)-(k==0)]

def predicted(r,c):
    return [(r-2,1)] if c==0 else ([(r-1,c-1)] if c>=2 else [])

forest_cases=0; folddel=0
for mask in range(1<<9):
    edges={(i//3,i%3) for i in range(9) if mask&(1<<i)}
    c=forest_components(3,3,edges)
    if c is None:continue
    fold,remaining=check_folds(3,3,edges)
    assert remaining==c,(edges,c,remaining)
    folddel+=fold
    faces=all_faces([3,3,1],edges)
    assert homology_mod2(faces)==predicted(3,c),(edges,c)
    forest_cases+=1
assert forest_cases==328
print('ALL_3x3_BIPARTITE_FORESTS_PASS',forest_cases,'fold_deletions',folddel)

patterns=[set(),{(0,0)},{(0,0),(1,1)},{(0,0),(1,1),(2,2)},
          {(0,0),(0,1),(0,2)}, {(0,0),(1,0),(1,1)},
          {(0,0),(1,0),(1,1),(2,2)}]
extra=0
for sizes in ([3,3,2,1],[3,3,2,1,1],[3,3,1,1,1]):
    for F in patterns:
        c=forest_components(3,3,F)
        assert c is not None
        assert homology_mod2(all_faces(sizes,F))==predicted(len(sizes),c),(sizes,F,c)
        extra+=1
print('HIGHER_PARTITE_CASES_PASS',extra)
# Six-cycle deletion is the first displayed cyclic boundary example.
six_cycle={(0,0),(0,2),(1,0),(1,1),(2,1),(2,2)}
assert forest_components(3,3,six_cycle) is None
for r in (3,4,5):
    sizes=[3,3]+[1]*(r-2)
    assert homology_mod2(all_faces(sizes,six_cycle))==[(r,1)]
print('SIX_CYCLE_BOUNDARY_PASS',3)
# In a matching deletion filtration the explicit folded base is two simplices
# joined by t disjoint cross edges. Adding the t-th bridge adds a new 1-cycle
# exactly at t=2,3,...; suspending shifts this to dimension r-1.
for t in range(4):
    F={(i,i) for i in range(t)}
    assert homology_mod2(all_faces([3,3,1],F))==predicted(3,t)
print('MATCHING_FILTRATION_STAGE_RANKS_PASS',4)
print('FOREST_DEFECT_CLIQUE_FREE_CHECK_PASS')
