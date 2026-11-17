"""Reconstruct simplicial three-tupling from six-vertex facets and compare with the component formula.
Only Python standard library; run: python verify.py
"""
from itertools import combinations, product
from collections import deque


def factor_cycle(n):
    return n, {tuple(sorted((i,(i+1)%n))) for i in range(n)}


def factor_cycle_leaf():
    n,e=factor_cycle(5)
    return 6, e|{(0,5)}


def factor_cycle_two_leaves():
    n,e=factor_cycle(4)
    return 6,e|{(0,4),(0,5)}


def factor_path(n):
    return n,{(i,i+1) for i in range(n-1)}


def factor_star(n):
    return n,{(0,i) for i in range(1,n)}


def graph_components(vertices,edges):
    adj={v:set() for v in vertices}
    for a,b in edges:
        assert a!=b
        adj[a].add(b);adj[b].add(a)
    unseen=set(vertices);ans=[]
    while unseen:
        v=next(iter(unseen));unseen.remove(v);todo=[v];num_edges=0;comp=set([v])
        while todo:
            q=todo.pop();num_edges+=len(adj[q])
            for w in adj[q]:
                if w in unseen:
                    unseen.remove(w);todo.append(w);comp.add(w)
        ans.append((len(comp),num_edges//2,num_edges//2-len(comp)+1))
    return sorted(ans)


def bipart_colors(n,edges):
    g=[set() for i in range(n)]
    for a,b in edges:g[a].add(b);g[b].add(a)
    color={0:0};queue=deque([0]);ok=True
    while queue:
        a=queue.popleft()
        for b in g[a]:
            if b not in color:
                color[b]=1-color[a];queue.append(b)
            elif color[b]==color[a]:ok=False
    assert len(color)==n
    return (sum(v==0 for v in color.values()),sum(v==1 for v in color.values())) if ok else None


def predicted(factors):
    v=[n for n,_ in factors];e=[len(ed) for _,ed in factors]
    colors=[bipart_colors(*factor) for factor in factors]
    indices=[i for i,c in enumerate(colors) if c is not None];b=len(indices)
    t=2**max(0,b-1);P=e[0]*e[1]*e[2]
    comps=[]
    if b==0:
        comps.append((v[0]*v[1]*v[2],4*P))
    else:
        for eta in product((0,1),repeat=b-1):
            bits=(0,)+eta
            size=1
            for i in range(3):
                if i not in indices:size*=v[i]
            p=1;q=1
            for j,i in enumerate(indices):
                p*=colors[i][bits[j]];q*=colors[i][1-bits[j]]
            comps.append((size*(p+q),4*P//t))
    for i in range(3):
        j,k=[a for a in range(3) if a!=i]
        if colors[i] is None:
            comps.append((v[i]*(e[j]+e[k]),2*P))
        else:
            a,c=colors[i]
            comps.extend([(a*e[j]+c*e[k],P),(a*e[k]+c*e[j],P)])
    return sorted((V,E,E-V+1) for V,E in comps)


def direct_three_tuple(factors):
    # Build the three-complex simplex vertex labels from three disjoint original factors.
    offset=0;blocks=[];real_edges=[]
    for n,edges in factors:
        blocks.append(list(range(offset,offset+n)))
        real_edges.append({tuple(sorted((a+offset,b+offset))) for a,b in edges})
        offset+=n
    triangles=set()
    for x,y,z in product(*blocks):triangles.add(tuple(sorted((x,y,z))))
    for i in range(3):
        for j in range(3):
            if i==j:continue
            for a,b in real_edges[i]:
                for z in blocks[j]:triangles.add(tuple(sorted((a,b,z))))
    adjacent=set()
    for aa,bb,cc in product(*real_edges):
        six=set(aa+bb+cc)
        assert len(six)==6
        for a in combinations(sorted(six),3):
            if a not in triangles:continue
            b=tuple(sorted(six-set(a)))
            if b in triangles:
                adjacent.add(tuple(sorted((a,b))))
    result=graph_components(triangles,adjacent)
    # direct total simplex count depends only on vertex/edge counts
    v=[n for n,_ in factors];e=[len(ed) for _,ed in factors]
    assert len(triangles)==v[0]*v[1]*v[2]+sum(e[i]*(v[j]+v[k]) for i,(j,k) in enumerate(((1,2),(0,2),(0,1))))
    assert len(adjacent)==10*e[0]*e[1]*e[2]
    return result,len(triangles),len(adjacent)


def run(name,factors):
    got,V,E=direct_three_tuple(factors);want=predicted(factors)
    assert got==want,(name,got,want)
    print(name,'f0',V,'f1',E,'components',len(got),'circle_ranks',sorted(c[2] for c in got))
    return sorted(c[2] for c in got)

if __name__=='__main__':
    r0=run('cycle6_cycle6_cycle3',[factor_cycle(6),factor_cycle(6),factor_cycle(3)])
    r1=run('cycle5plusleaf_cycle6_cycle3',[factor_cycle_leaf(),factor_cycle(6),factor_cycle(3)])
    r2=run('cycle5plusleaf_twice_cycle3',[factor_cycle_leaf(),factor_cycle_leaf(),factor_cycle(3)])
    assert [len(r0),len(r1),len(r2)]==[7,5,4]
    assert sum(r0)==sum(r1)+2==sum(r2)+3
    assert r0!=r1!=r2
    run('P6_P6_C3',[factor_path(6),factor_path(6),factor_cycle(3)])
    run('K15_K15_C3',[factor_star(6),factor_star(6),factor_cycle(3)])
    run('cycle4_cycle5_cycle6',[factor_cycle(4),factor_cycle(5),factor_cycle(6)])
    run('K2_P3_C3',[factor_path(2),factor_path(3),factor_cycle(3)])
    run('cycle4_cycle4_cycle4',[factor_cycle(4)]*3)
    run('cycle4plus2leaves_twice_cycle3',[factor_cycle_two_leaves(),factor_cycle_two_leaves(),factor_cycle(3)])
    print('THREE_GRAPH_JOIN_TRIPLING_PASS')
