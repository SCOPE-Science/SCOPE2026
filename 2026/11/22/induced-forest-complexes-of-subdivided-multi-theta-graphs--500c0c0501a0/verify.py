"""Finite exhaustive checks for induced-vertex-forest complexes of multi-theta graphs.
Pure Python 3; no external dependencies. Mathematical proof in RESULT.md covers all parameters.
"""
from itertools import combinations
from math import comb

def make_graph(sizes):
    # sizes are positive numbers of internal vertices on each s--t arm
    blocks=[]; nxt=2; edges=set()
    for a in sizes:
        block=tuple(range(nxt,nxt+a)); nxt+=a; blocks.append(block)
        seq=(0,)+block+(1,)
        for x,y in zip(seq,seq[1:]): edges.add(tuple(sorted((x,y))))
    return nxt,blocks,edges

def acyclic(subset,edges):
    parent={v:v for v in subset}
    def root(v):
        while parent[v]!=v: v=parent[v]
        return v
    for a,b in edges:
        if a in parent and b in parent:
            ra,rb=root(a),root(b)
            if ra==rb:return False
            parent[ra]=rb
    return True

def gf2_rank(columns):
    basis={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p in basis:c^=basis[p]
            else:
                basis[p]=c
                break
    return len(basis)

def betti(faces,n):
    by_size={k:[] for k in range(n+1)}
    for f in faces:by_size[f.bit_count()].append(f)
    ranks={0:0}
    for k in range(1,n+1):
        lo={x:i for i,x in enumerate(by_size[k-1])}
        cols=[]
        for f in by_size[k]:
            col=0
            for bit in range(n):
                if f & (1<<bit):col^=1<<lo[f^(1<<bit)]
            cols.append(col)
        ranks[k]=gf2_rank(cols)
    return {k-1:len(by_size[k])-ranks[k]-ranks.get(k+1,0) for k in range(1,n+1) if len(by_size[k])-ranks[k]-ranks.get(k+1,0)}

def run(sizes):
    n,blocks,edges=make_graph(sizes)
    full=(1<<n)-1
    faces={f for f in range(1<<n) if acyclic({i for i in range(n) if f>>i&1},edges)}
    dual={f for f in range(1<<n) if (full^f) not in faces}
    # Independent reconstruction of Alexander dual from pairs of full arms.
    expected_dual=set()
    for i,j in combinations(range(len(blocks)),2):
        allowed=set(v for k,block in enumerate(blocks) if k not in (i,j) for v in block)
        for f in range(1<<n):
            if all(not (f>>v&1) for v in range(n) if v not in allowed):expected_dual.add(f)
    assert dual==expected_dual,(sizes,'dual disagreement')
    m=len(sizes); d=n-m
    expected_betti={d:m-1}
    got=betti(faces,n)
    assert got==expected_betti,(sizes,got,expected_betti)
    # Detect full 2-skeleton.
    assert all(sum(f>>v&1 for v in range(n))>3 or f in faces for f in range(1<<n))
    # Check face-collapse domination in each non-singleton arm via maximal faces.
    facets=[f for f in dual if not any(f!=g and (f&g)==f for g in dual)]
    for block in blocks:
        for w in block[1:]:
            assert all(not(f>>w&1) or f>>block[0]&1 for f in facets)
    # Check the Euler characteristic also independently via all faces.
    red_euler=sum((-1)**(f.bit_count()-1) for f in faces)
    assert red_euler==(-1)**d*(m-1),(sizes,red_euler)
    return n,len(faces),len(dual),got

if __name__=='__main__':
    cases=[(1,1,1),(1,1,2),(1,2,2),(2,2,2),(1,1,1,1),(1,1,1,2),
           (1,1,2,2),(1,1,1,1,1),(2,1,1,1,1),(1,2,1,2,1)]
    for case in cases:
        result=run(case)
        print('PASS sizes=%s N=%d forest_faces=%d dual_faces=%d mod2_reduced_betti=%s'%((case,)+result))
    print('PASS all %d exhaustive cases (enumeration is finite only)'%len(cases))
