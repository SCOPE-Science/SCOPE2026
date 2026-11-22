"""Exact finite chain verification for the icosahedral ordinary cut complexes.

Python >=3.10, standard library only. All integral arithmetic is exact.
The labeled graph and face test are specified in this file.
"""
from itertools import combinations
from collections import Counter
import json

N = 12
V = (1 << N) - 1
EDGES = [
 (0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
 (2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
 (4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),
 (7,10),(7,11),(8,9),(9,10),(10,11)
]
ADJ = [0] * N
for a, b in EDGES:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert len(EDGES) == 30 and all(x.bit_count() == 5 for x in ADJ)
TRIANGLES = [t for t in combinations(range(N), 3)
             if all(ADJ[a] & (1 << b) for a,b in combinations(t,2))]
assert len(TRIANGLES) == 20
assert all(sum(set((a,b)) <= set(t) for t in TRIANGLES) == 2 for a,b in EDGES)
# The link of each vertex in the triangulated polyhedral sphere is a 5-cycle.
assert all(sum(bool(ADJ[a] & (1 << b)) for b in range(N) if ADJ[v] & (1 << b)) == 2
           for v in range(N) for a in range(N) if ADJ[v] & (1 << a))

def connected(s):
    if not s: return False
    seen = 0
    stack = s & -s
    while stack:
        bit = stack & -stack
        stack -= bit
        if seen & bit: continue
        seen |= bit
        stack |= ADJ[bit.bit_length() - 1] & s & ~seen
    return seen == s

def subfaces(top):
    s = top
    while True:
        yield s
        if s == 0: break
        s = (s - 1) & top

def complex_faces(k):
    disconnected = [sum(1 << i for i in a) for a in combinations(range(N), k)
                    if not connected(sum(1 << i for i in a))]
    facets = [V ^ s for s in disconnected]
    faces = set()
    for f in facets:
        faces.update(subfaces(f))
    # Independent exhaustive membership test from the defining predicate.
    for s in range(1 << N):
        belong = any((bad & s) == 0 for bad in disconnected)
        assert (s in faces) == belong
    return faces, facets

def boundary(s):
    vertices = [i for i in range(N) if s & (1 << i)]
    return {s ^ (1 << i): (-1) ** j for j, i in enumerate(vertices)}

def exact_unit_reduce(faces):
    columns = {s: boundary(s) if s else {} for s in faces}
    active = set(faces)
    original = Counter(s.bit_count()-1 for s in faces)
    cancelled = Counter()
    for d in range(0, N):
        while True:
            cols = [s for s in active if s.bit_count() == d+1]
            row_degree = Counter(r for s in cols for r in columns[s])
            best = None
            for s in cols:
                for r, coefficient in columns[s].items():
                    if abs(coefficient) != 1: continue
                    key = ((len(columns[s])-1)*(row_degree[r]-1),
                           len(columns[s])+row_degree[r], r, s)
                    if best is None or key < best[0]: best = (key,r,s)
            if best is None: break
            _,row,col = best
            pivot = columns[col][row]
            assert abs(pivot) == 1 and row.bit_count() + 1 == col.bit_count()
            for other in cols:
                if other == col: continue
                a = columns[other].get(row, 0)
                if not a: continue
                m = a // pivot
                for r,b in columns[col].items():
                    value = columns[other].get(r,0) - m*b
                    if value: columns[other][r] = value
                    else: columns[other].pop(r,None)
            # Corresponding transformed basis of the adjacent chain group.
            for higher in active:
                if higher.bit_count() == d+2:
                    columns[higher].pop(col,None)
            active.remove(row);active.remove(col)
            columns.pop(row);columns.pop(col)
            cancelled[d] += 1
    critical = Counter(s.bit_count()-1 for s in active)
    nonzero = [(s,r,v) for s,c in columns.items() for r,v in c.items()]
    # Verify all remaining boundaries square to zero, with signed coefficients.
    for s,c in columns.items():
        dd = {}
        for r, a in c.items():
            for t,b in columns[r].items(): dd[t] = dd.get(t,0)+a*b
        assert not any(dd.values())
    return {
       'f_vector': [original[d] for d in range(-1,N)],
       'unit_pivots':sum(cancelled.values()),
       'pivots_by_upper_dimension': {str(d):cancelled[d] for d in range(N) if cancelled[d]},
       'critical': {str(d):critical[d] for d in range(-1,N) if critical[d]},
       'residual_entries':[(r.bit_count()-1,s.bit_count()-1,v) for s,r,v in nonzero],
    }

def xor_basis(vectors):
    basis = {}
    for v in vectors:
        while v:
            j = v.bit_length()-1
            if j in basis: v ^= basis[j]
            else:
                basis[j] = v;break
    return basis

def remainder(v,basis):
    while v:
        j=v.bit_length()-1
        if j not in basis: return v
        v ^= basis[j]
    return 0

def mod2_boundary(s,index):
    return sum(1 << index[s ^ (1<<v)] for v in range(N) if s & (1<<v))

def verify_map(five,six):
    level = lambda faces,d: sorted(s for s in faces if s.bit_count()==d+1)
    assert six <= five
    five4, five5 = level(five,4),level(five,5)
    six3, six4 = level(six,3),level(six,4)
    i54={s:i for i,s in enumerate(five4)}
    b5 = xor_basis(mod2_boundary(s,i54) for s in five5)
    assert len(b5) == 461
    i63={s:i for i,s in enumerate(six3)}
    piv = {}
    cycles=[]
    for i,s in enumerate(six4):
        v=mod2_boundary(s,i63)
        chain=1<<i
        while v:
            j=v.bit_length()-1
            if j not in piv:
                piv[j] = (v,chain);break
            w,c=piv[j];v^=w;chain^=c
        if v==0: cycles.append(chain)
    assert len(piv)==294 and len(cycles)==138
    images=[]
    for z in cycles:
        out=0;support=[]
        while z:
            bit=z & -z;z-=bit
            face=six4[bit.bit_length()-1]
            support.append(face)
            out ^= 1<<i54[face]
        if remainder(out,b5): images.append(support)
    assert images
    witness = min(images,key=lambda support:(len(support),support))
    return {
      'boundary_rank_five_degree_five_mod2':len(b5),
      'six_degree_four_cycle_space_dim_mod2':len(cycles),
      'six_degree_four_boundary_rank_mod2':len(piv),
      'nonzero_source_cycle_images_found':len(images),
      'image_rank_on_H4_mod2':1,
      'witness_support_size':len(witness),
      'witness_four_simplices':[[i for i in range(N) if face&(1<<i)] for face in witness]
    }

def main():
    f5, fac5 = complex_faces(5)
    f6, fac6 = complex_faces(6)
    a=exact_unit_reduce(f5)
    b=exact_unit_reduce(f6)
    assert len(fac5)==300 and len(fac6)==112
    assert a['critical']=={'4':1,'5':1,'6':30}
    assert len(a['residual_entries'])==1
    assert a['residual_entries'][0][:2] == (4,5)
    assert abs(a['residual_entries'][0][2])==2
    assert b['critical']=={'3':6,'4':26}
    assert b['residual_entries']==[]
    map_result=verify_map(f5,f6)
    out={'graph':'explicit icosahedral edge list','vertex_count':N,'edge_count':len(EDGES),
         'cut5':a,'cut6':b,'inclusion':map_result,
         'homology_cut6':{'3':'Z^6','4':'Z^26'},
         'homology_cut5':{'4':'Z/2','6':'Z^30'},
         'integral_H4_map':'surjective onto Z/2 by mod-2 naturality and the universal coefficient theorem',
         'status':'PASS'}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
