"""Reproducible finite acyclic-matching certificates for a 20-vertex graph-metric Rips filtration.
Python >=3.9, standard library only. Run: python verify.py.
"""
from itertools import combinations
from collections import Counter, deque

def build_graph():
    parts = list(combinations(range(5), 2)) + list(combinations(range(5), 3))
    assert len(parts) == 20
    adj = [0]*20
    for a in range(10):
        for b in range(10, 20):
            if set(parts[a]).issubset(parts[b]):
                adj[a] |= (1 << b)
                adj[b] |= (1 << a)
    assert all(x.bit_count() == 3 for x in adj)
    return parts, adj

def graph_distances(adj):
    out = []
    for v in range(len(adj)):
        dist = [-1]*len(adj); dist[v]=0
        todo = deque([v])
        while todo:
            a=todo.popleft()
            avail = adj[a]
            while avail:
                b = (avail & -avail).bit_length()-1; avail &= avail-1
                if dist[b] == -1:
                    dist[b]=dist[a]+1;todo.append(b)
        assert -1 not in dist
        out.append(dist)
    assert all(out[i][j]==out[j][i] for i in range(20) for j in range(20))
    return out

def graph_power_edges(dist, r):
    return [sum(1<<j for j in range(20) if j != i and dist[i][j] <= r) for i in range(20)]

def faces_recursive(links):
    """Enumerate all nonempty cliques, extending only with larger vertices."""
    result=[]
    def visit(face, may):
        while may:
            bit=may&-may; may^=bit
            v=bit.bit_length()-1
            new=face|bit;result.append(new)
            visit(new,may&links[v])
    visit(0,(1<<20)-1)
    assert len(result)==len(set(result))
    return set(result)

def maximal_cliques(links):
    """Independent maximal-clique enumeration via Bron--Kerbosch pivoting."""
    result=[]
    def visit(R,P,X):
        if not P and not X:
            result.append(R);return
        candidates=P
        if P|X:
            # Deterministically pivot, reducing branching.
            u=((P|X)&-(P|X)).bit_length()-1
            candidates=P & ~links[u]
        while candidates:
            bit=candidates&-candidates;candidates^=bit
            v=bit.bit_length()-1
            visit(R|bit,P&links[v],X&links[v])
            P^=bit;X|=bit
    visit(0,(1<<20)-1,0)
    return result

def faces_from_maximal(max_cliques):
    # All subfaces of each maximal clique, by subset iteration.
    result=set()
    for m in max_cliques:
        s=m
        while s:
            result.add(s)
            s=(s-1)&m
    return result

def toggle_matching(faces):
    # Deterministic multi-stage vertex-toggling matching.
    # A face is paired at its first possible stage, and never reused.
    taken=set();pairs=[]
    order=sorted(faces,key=lambda m:(m.bit_count(),m))
    for v in range(20):
        bit=1<<v
        for lo in order:
            if lo in taken or lo&bit:continue
            hi=lo|bit
            if hi in faces and hi not in taken:
                taken.add(lo);taken.add(hi);pairs.append((lo,hi))
    return pairs,faces-taken

def acyclic_hasse_certificate(faces,pairs):
    # Ordinary cover u -> v when v has one more vertex; matched cover reversed v -> u.
    # The directed graph must admit a full topological sorting (acyclicity).
    matched={hi:lo for lo,hi in pairs}
    indeg={x:0 for x in faces}
    # For each high face and facet, orientation into high unless matched, then out of high.
    for hi in faces:
        t=hi
        while t:
            bit=t&-t; t^=bit
            lo=hi^bit
            if not lo:continue
            if matched.get(hi)==lo: indeg[lo]+=1
            else: indeg[hi]+=1
    q=deque(sorted(x for x in faces if indeg[x]==0))
    seen=0;cover_count=0
    while q:
        x=q.popleft();seen+=1
        # Outgoing unmatched covers from x to its cofaces; using bit adjacency tests;
        # for each candidate vertex in 20, check if coface exists.
        absent=(1<<20)-1-x
        while absent:
            b=absent&-absent;absent^=b
            h=x|b
            if h in faces and matched.get(h)!=x:
                indeg[h]-=1;cover_count+=1
                if indeg[h]==0:q.append(h)
        # Matched edge h -> x, when current x is the higher endpoint.
        if x in matched:
            lo=matched[x];indeg[lo]-=1;cover_count+=1
            if indeg[lo]==0:q.append(lo)
    assert seen == len(faces),('cycle!',seen,len(faces))
    assert all(v==0 for v in indeg.values())
    return cover_count

def main():
    parts,adj=build_graph();dist=graph_distances(adj)
    assert len(set(parts))==20
    assert max(max(row) for row in dist)==5
    assert [sum(d==5 for d in row) for row in dist]==[1]*20
    expected={1:([20,30],11),2:([20,90,120,30],19),3:([20,150,540,1000,960,450,80],1),4:([20,180,960,3360,8064,13440,15360,11520,5120,1024],1)}
    for r in range(1,5):
        links=graph_power_edges(dist,r)
        f1=faces_recursive(links)
        maximals=maximal_cliques(links)
        f2=faces_from_maximal(maximals)
        assert f1==f2,(r,len(f1),len(f2))
        vector=[Counter(m.bit_count() for m in f1)[k] for k in range(1,max(m.bit_count() for m in f1)+1)]
        assert vector==expected[r][0],(r,vector)
        pairs,critical=toggle_matching(f1)
        assert len(f1)==2*len(pairs)+len(critical)
        crit_dims=sorted(Counter(m.bit_count()-1 for m in critical).items())
        aim=[(0,1),(r if r<3 else (3 if r==3 else 9),expected[r][1])]
        assert crit_dims==aim, (r,crit_dims,aim)
        covers=acyclic_hasse_certificate(f1,pairs)
        expected_covers=sum(m.bit_count() for m in f1 if m.bit_count()>1)
        assert covers == expected_covers,(r,covers,expected_covers)
        euler=sum((-1)**(i-1)*vector[i-1] for i in range(1,len(vector)+1))
        assert euler==1+expected[r][1]*(-1)**(aim[1][0])
        print(f'r={r} faces={len(f1)} maximal_facets={len(maximals)} f_vector={vector} pairs={len(pairs)} critical={crit_dims} covers={covers} euler={euler}',flush=True)
    print('r=0: twenty isolated vertices, reduced H_0 rank 19')
    print('r>=5: full 19-simplex, contractible')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
