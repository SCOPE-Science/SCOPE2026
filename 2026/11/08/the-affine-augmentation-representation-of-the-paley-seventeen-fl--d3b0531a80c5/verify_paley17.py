#!/usr/bin/env python3
"""Independent finite certificates for the 17-vertex Paley flag complex.

Run: python3 verify_paley17.py
All arithmetic is over the prime field with seventeen elements.
"""
from collections import defaultdict, deque
from itertools import combinations

P = 17
Q = {a*a % P for a in range(1, P)}
assert len(Q) == 8 and -1 % P in Q and 2 in Q


def incident(x, y):
    return x != y and ((x-y) % P in Q)


faces = {k: [tuple(t) for t in combinations(range(P), k)
             if all(incident(x,y) for x,y in combinations(t,2))]
         for k in (1,2,3,4)}
assert [len(faces[k]) for k in (1,2,3,4)] == [17,68,68,0]
assert all(sum({x,y} <= set(t) for t in faces[3]) == 3
           for x,y in faces[2])
assert all(not any(a in t for t in faces[4]) for a in range(P))
E = faces[2]
T = faces[3]
Eset = set(E)
Tset = set(T)

# This breadth-first spanning tree has sixteen edges. Every remaining edge
# follows from triangle relations once two of a triangle's edges are known.
TREE = [(0,1),(0,2),(0,4),(0,8),(0,9),(0,13),(0,15),(0,16),
        (1,3),(1,5),(1,10),(1,14),(2,6),(2,11),(4,12),(7,8)]
assert len(TREE)==16 and len(set(TREE))==16 and all(e in Eset for e in TREE)
seen = {0}
while True:
    nxt=seen | {v for u,v in TREE if u in seen} | {u for u,v in TREE if v in seen}
    if nxt==seen:break
    seen=nxt
assert len(seen)==17

known=set(TREE)
certificate=[]
round_counts=[]
while len(known)<len(Eset):
    newly=[]
    for a,b,c in T:
        tri=((a,b),(a,c),(b,c))
        absent=[e for e in tri if e not in known]
        if len(absent)==1:
            e=absent[0]
            known.add(e)
            newly.append((e,(a,b,c)))
    if not newly:
        raise AssertionError('stalled edge-path null-homotopy certificate')
    certificate.extend(newly)
    round_counts.append(len(newly))
assert known==Eset and len(certificate)==52
assert len({e for e,_ in certificate})==52

# Boundary rank is computed independently over four prime fields.
def boundary_rank_mod(prime):
    cols=[]
    row_index={e:i for i,e in enumerate(E)}
    for a,b,c in T:
        d={row_index[(b,c)]:1, row_index[(a,c)]:-1, row_index[(a,b)]:1}
        cols.append(d)
    pivots={}
    for d in cols:
        d={i:x%prime for i,x in d.items() if x%prime}
        while d:
            row=min(d)
            if row not in pivots:
                inv=pow(d[row],-1,prime)
                pivots[row]={i:(x*inv)%prime for i,x in d.items() if x%prime}
                break
            pivot=pivots[row]
            scalar=d[row]
            for i,x in pivot.items():
                val=(d.get(i,0)-scalar*x)%prime
                if val:d[i]=val
                else:d.pop(i,None)
    return len(pivots)

ranks={p:boundary_rank_mod(p) for p in (2,3,5,17)}
assert ranks=={2:52,3:52,5:52,17:52}

# Signed Lefschetz traces for all 17*8 affine graph automorphisms.
def sign_of_reordering(seq):
    return -1 if sum(seq[i]>seq[j] for i in range(len(seq))
                     for j in range(i+1,len(seq)))%2 else 1

def trace_on_kfaces(mapping, k):
    total=0
    for face in faces[k]:
        mapped=tuple(mapping[x] for x in face)
        if tuple(sorted(mapped))!=face:continue
        total+=sign_of_reordering(mapped)
    return total

trace_hist=defaultdict(int)
trace_classes=defaultdict(set)
for a in sorted(Q):
    for b in range(P):
        mapping=[(a*x+b)%P for x in range(P)]
        assert all(incident(mapping[x],mapping[y]) for x,y in E)
        tr=[trace_on_kfaces(mapping,k) for k in (1,2,3)]
        L=tr[0]-tr[1]+tr[2]
        h2=L-1
        expected=sum(mapping[x]==x for x in range(P))-1
        assert h2==expected,(a,b,tr,h2,expected)
        category=('identity' if a==1 and b==0 else
                  'translation' if a==1 else
                  'other_affine')
        trace_classes[category].add(h2)
        trace_hist[(category,h2)]+=1
assert dict(trace_hist)=={
 ('identity',16):1,('translation',-1):16,('other_affine',0):119}

# Detailed involution calculation (the multipliers -1 with arbitrary b).
for b in range(P):
    mapping=[(-x+b)%P for x in range(P)]
    assert [trace_on_kfaces(mapping,k) for k in (1,2,3)] == [1,-4,-4]

print('quadratic_residues',','.join(map(str,sorted(Q))))
print('f_vector',tuple(len(faces[k]) for k in (1,2,3,4)))
print('triangles_per_edge',3)
print('spanning_tree_edges',len(TREE))
print('triangle_closure_new_edges',len(certificate))
print('triangle_closure_rounds',round_counts)
print('boundary_ranks',','.join(f'{p}:{ranks[p]}' for p in sorted(ranks)))
print('affine_actions',len(Q)*P)
print('H2_trace_histogram',sorted((f'{name}:{v}',count) for (name,v),count in trace_hist.items()))
print('involution_chain_traces', (1,-4,-4))
print('all_checks_passed', True)
