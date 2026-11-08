"""Independent finite checks of the square-completion splitting of closed neighborhoods.

Uses exhaustive face sets, exact elementary free-face checks, and GF(2) boundary
ranks. Standard library only. Run: python3 verify.py
"""
from itertools import combinations
from collections import defaultdict
import random

def normalized(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        assert a!=b
        adj[a].add(b);adj[b].add(a)
    return adj

def graph_data(adj):
    n=len(adj)
    for a in range(n):
        for b in adj[a]:
            assert not (adj[a] & adj[b]), 'triangle'
    commons={}
    for a,b in combinations(range(n),2):
        x=adj[a]&adj[b]
        assert len(x)<=2, 'codegree exceeds two'
        if x: commons[a,b]=tuple(sorted(x))
    squares=set()
    for (a,b),cs in commons.items():
        if len(cs)==2:
            v,w=cs
            # a,b are necessarily nonadjacent; v,w are nonadjacent.
            assert b not in adj[a] and w not in adj[v]
            squares.add(frozenset((a,b,v,w)))
    assert all(len(x)==4 for x in squares)
    edge_set={frozenset((a,b)) for a in range(n) for b in adj[a] if a<b}
    assert len(edge_set)==sum(len(z) for z in adj)//2
    return commons,squares,edge_set

def faces_of_closed_neighborhood(adj):
    faces={frozenset()}
    for v,nb in enumerate(adj):
        base=sorted(nb|{v})
        for k in range(1,len(base)+1):
            for x in combinations(base,k):faces.add(frozenset(x))
    return faces

def faces_of_target(n,squares,edges):
    out={frozenset()}
    out|={frozenset([v]) for v in range(n)}
    out|=edges
    for s in squares:
        for k in (2,3):
            for x in combinations(sorted(s),k):out.add(frozenset(x))
    return out

def collapse(faces, low, high):
    assert low in faces and high in faces and len(high)==len(low)+1 and low<high
    assert sum(1 for z in faces if low<z)==1,(low,high,'not free')
    faces.remove(low);faces.remove(high)

def ranks_mod2(faces):
    fs=defaultdict(list)
    for s in faces:
        if s:fs[len(s)-1].append(tuple(sorted(s)))
    for k in fs: fs[k].sort()
    ranks={}
    for k in sorted(fs):
        if k==0: ranks[0]=0;continue
        im={v:i for i,v in enumerate(fs[k-1])}
        piv={}
        for face in fs[k]:
            col=0
            for j in range(len(face)):
                col^=1<<im[face[:j]+face[j+1:]]
            while col:
                key=col.bit_length()-1
                if key not in piv:
                    piv[key]=col;break
                col^=piv[key]
        ranks[k]=len(piv)
    betti={k:len(fs[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in fs}
    betti[0]-=1
    return {k:b for k,b in sorted(betti.items()) if b}

def check(n, edges, label, compute_betti=True):
    adj=normalized(n,edges)
    commons,squares,orig_edges=graph_data(adj)
    faces=faces_of_closed_neighborhood(adj)
    start_size=len(faces)
    for v,nb in enumerate(adj):
        nb=sorted(nb)
        for k in range(len(nb),2,-1):
            for combo in combinations(nb,k):
                low=frozenset(combo)
                collapse(faces,low,low|{v})
    for (a,b),cs in sorted(commons.items()):
        if len(cs)==1:
            v=cs[0]
            collapse(faces,frozenset([a,b]),frozenset([a,b,v]))
    exp=faces_of_target(n,squares,orig_edges)
    assert faces==exp,(label,'missing',len(exp-faces),'extra',len(faces-exp))
    # The square cylinders are genuine discs with unique diagonals, which
    # never occur in the graph or another square.
    diagonal_owners=defaultdict(set)
    for s in squares:
        for a,b in combinations(sorted(s),2):
            if b not in adj[a]: diagonal_owners[a,b].add(tuple(sorted(s)))
    assert all(len(x)==1 for x in diagonal_owners.values())
    assert len(diagonal_owners)==2*len(squares)
    betti=ranks_mod2(faces) if compute_betti else None
    if not label.startswith('random_'): print(f'{label}: n={n} edges={len(orig_edges)} squares={len(squares)} starting_faces={start_size} remaining_faces={len(faces)} betti={betti}')
    return (len(squares),betti)

def cycle(m):
    return m,{(i,(i+1)%m) for i in range(m)}

def cube(d):
    return 1<<d,{(i,i^(1<<b)) for i in range(1<<d) for b in range(d) if i < (i^(1<<b))}

def torus(m,n):
    def x(a,b):return a*n+b
    e=set()
    for a in range(m):
        for b in range(n):
            e.add(tuple(sorted((x(a,b),x((a+1)%m,b)))))
            e.add(tuple(sorted((x(a,b),x(a,(b+1)%n)))))
    return m*n,e

def klein(m,n):
    def x(a,b):return a*n+b
    e=set()
    for a in range(m):
        for b in range(n):
            e.add(tuple(sorted((x(a,b),x((a+1)%m,b)))))
            if b<n-1:
                e.add(tuple(sorted((x(a,b),x(a,b+1)))))
            else:
                e.add(tuple(sorted((x(a,b),x((-a)%m,0)))))
    return m*n,e

def grotzsch():
    # Mycielskian of a 5-cycle: original vertices 0..4,
    # shadows 5..9, universal shadow apex 10.
    edges=set()
    for i in range(5):
        j=(i+1)%5
        edges.add(tuple(sorted((i,j))))
        edges.add(tuple(sorted((i,5+j))))
        edges.add(tuple(sorted((j,5+i))))
        edges.add((5+i,10))
    return 11,edges

def run():
    cases=[('C5',cycle(5)),('C6',cycle(6)),('C8',cycle(8)),
           ('Q3',cube(3)),('Q4',cube(4)),('Q5',cube(5)),('Grotzsch',grotzsch()),
           ('torus_5_5',torus(5,5)),('torus_5_6',torus(5,6)),('klein_5_5',klein(5,5)),('klein_6_5',klein(6,5))]
    for label,(n,edges) in cases:
        q,b=check(n,edges,label)
        if label.startswith('Q'):
            d=int(label[1:]);expected=2**(d-2)*(d*d-3*d+4)-1
            assert b=={2:expected},(label,b,expected)
        if label.startswith('torus_') or label.startswith('klein_'):
            assert b=={1:2,2:q+1},(label,b,q)
    rng=random.Random(261105)
    passed=0;skipped=0
    for n in range(3,8):
        for trial in range(300 if n==7 else 160):
            es={(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<0.33}
            adj=normalized(n,es)
            try:graph_data(adj)
            except AssertionError:skipped+=1;continue
            check(n,es,f'random_{n}_{trial}',compute_betti=False)
            passed+=1
    print('RANDOM_PASSED',passed,'EXCLUDED_BY_HYPOTHESES',skipped)
    print('ALL_VERIFY_OK')
if __name__=='__main__':run()
