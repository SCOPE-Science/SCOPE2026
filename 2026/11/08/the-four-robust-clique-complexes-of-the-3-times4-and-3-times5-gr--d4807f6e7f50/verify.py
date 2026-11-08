"""Exact discrete-Morse certificates for two four-robust rectangular grid complexes.
Run: python verify.py
Uses only the Python standard library.
"""
from itertools import combinations
from collections import Counter, deque

ORDERS = {
    4: (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6),
    5: (7, 8, 9, 6, 5, 14, 13, 12, 11, 10, 4, 3, 2, 1, 0),
}
EXPECTED = {
    4: (1416, (1,12,66,220,434,466,217), 20),
    5: (3642, (1,15,105,455,1089,1323,654), 56),
}

def test_grid(n):
    size=3*n
    edges=set()
    for a in range(size):
        for b in range(a+1,size):
            if abs(a//n-b//n)+abs(a%n-b%n)==1:
                edges.add((a,b))
    independent4=[]
    for t in combinations(range(size),4):
        if all((a,b) not in edges for a,b in combinations(t,2)):
            independent4.append(sum(1<<a for a in t))
    faces={s for s in range(1<<size)
           if not any((s&b)==b for b in independent4)}
    fvector=tuple(sum(s.bit_count()==j for s in faces)
                  for j in range(7))
    assert (len(faces),fvector)==EXPECTED[n][:2]
    # In a bipartite graph, seven vertices contain four in the same bipartition.
    assert all(s.bit_count()<=6 for s in faces)
    unmatched=set(faces)
    pairs=[]
    for v in ORDERS[n]:
        bit=1<<v
        stage=[s for s in unmatched
               if s&bit==0 and (s|bit) in unmatched]
        for lo in stage:
            hi=lo|bit
            unmatched.remove(lo)
            unmatched.remove(hi)
            pairs.append((lo,hi))
    assert len(unmatched)==EXPECTED[n][2]
    assert all(s.bit_count()==6 for s in unmatched)
    assert len(pairs)*2+len(unmatched)==len(faces)
    # The empty simplex is matched against one vertex. Remove this augmented
    # matching pair, producing one critical 0-cell in the ordinary face poset.
    empty_pair=[(a,b) for a,b in pairs if a==0]
    assert len(empty_pair)==1
    vertex=empty_pair[0][1]
    pairs=[(a,b) for a,b in pairs if a!=0]
    matched=set(pairs)
    ordinary=faces-{0}
    indeg={s:0 for s in ordinary}
    arcs={s:[] for s in ordinary}
    incidences=0
    for hi in ordinary:
        for v in range(size):
            bit=1<<v
            if not hi&bit: continue
            lo=hi^bit
            if lo==0: continue
            a,b=(lo,hi) if (lo,hi) in matched else (hi,lo)
            arcs[a].append(b)
            indeg[b]+=1
            incidences+=1
    queue=deque(s for s in ordinary if indeg[s]==0)
    seen=0
    while queue:
        u=queue.popleft(); seen+=1
        for v in arcs[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert seen==len(ordinary),('cyclic matching',n,seen)
    crit=unmatched|{vertex}
    assert Counter(s.bit_count()-1 for s in crit)==Counter({0:1,5:EXPECTED[n][2]})
    return fvector,len(pairs),len(ordinary),incidences,vertex

if __name__=='__main__':
    for n in sorted(ORDERS):
        f,p,c,h,v=test_grid(n)
        print(f'grid=3x{n} f_vector={f} ordinary_faces={c} pairs={p} '
              f'hasse_incidences={h} critical=(one_vertex,{EXPECTED[n][2]}_five_cells) '
              f'critical_vertex={v.bit_length()-1} acyclic=PASS')
    print('ALL_VERIFY_OK')
