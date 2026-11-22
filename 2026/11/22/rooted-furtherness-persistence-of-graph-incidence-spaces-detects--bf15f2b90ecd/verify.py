"""Independent persistence verification for incidence-poset furtherness barcodes.
Public-domain style research reproduction: finite graph filtration, no external dependencies.
"""
from collections import Counter
from itertools import combinations
import random


def is_connected(n, edges):
    seen = {0}
    changed = True
    while changed:
        changed = False
        for u,v in edges:
            if (u in seen) ^ (v in seen):
                seen.update((u,v)); changed = True
    return len(seen) == n


def from_graph(n, edges, root):
    """Compute persistence via filtered order-complex edges and DSU, not formulas.

    root is ('v', index) or ('e', index); data are exact integers.
    """
    edges = sorted(tuple(sorted(e)) for e in edges)
    verts = [('v',i) for i in range(n)] + [('e',j) for j in range(len(edges))]
    opens = {('v',i):{('v',i)} for i in range(n)}
    opens.update({('e',j): {('e',j),('v',u),('v',v)} for j,(u,v) in enumerate(edges)})
    origin = opens[root]
    weight = {v:len(opens[v]-origin) for v in verts}
    # Discrete simplex order: all vertices before edges at a shared filtration time.
    events=[]
    for v in verts:
        events.append((weight[v],0,v,None))
    for j,(u,v) in enumerate(edges):
        for z in (u,v):
            a,b=('e',j),('v',z)
            events.append((max(weight[a],weight[b]),1,a,b))
    events.sort(key=lambda e:(e[0],e[1],str(e[2]),str(e[3])))
    par={};birth={}
    def find(v):
        while par[v]!=v:
            par[v]=par[par[v]];v=par[v]
        return v
    out={0:Counter(),1:Counter()}
    for t,dim,a,b in events:
        if dim==0:
            par[a]=a; birth[a]=t
        else:
            x,y=find(a),find(b)
            if x==y:
                out[1][(t,None)]+=1
            else:
                if (birth[x],str(x)) > (birth[y],str(y)):
                    x,y=y,x
                if birth[y]<t:out[0][(birth[y],t)]+=1
                par[y]=x
    for x in par:
        if find(x)==x: out[0][(birth[x],None)]+=1
    return out


def prediction(n, edges, root):
    m=len(edges); deg=[0]*n;adj=[set() for _ in range(n)]
    for u,v in edges:
        deg[u]+=1;deg[v]+=1;adj[u].add(v);adj[v].add(u)
    beta=m-n+1
    if root[0]=='v':
        d=deg[root[1]]
        q0={(0,None):1,(1,2):d,(1,3):n-1-d}
        q1={(3,None):beta}
    else:
        u,v=edges[root[1]];c=len(adj[u]&adj[v]);k=deg[u]+deg[v]-2-c
        q0={(0,None):1,(1,2):k,(1,3):n-2-k}
        q1={(2,None):c,(3,None):beta-c}
    return {0:Counter({k:v for k,v in q0.items() if v}),1:Counter({k:v for k,v in q1.items() if v})}


def run():
    count=0;root_count=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            ed=[pairs[i] for i in range(len(pairs)) if mask>>i&1]
            if not is_connected(n,ed):continue
            count+=1
            for root in [('v',i) for i in range(n)]+[('e',i) for i in range(len(ed))]:
                x=from_graph(n,ed,root);y=prediction(n,ed,root)
                assert x==y, (n,ed,root,x,y)
                root_count+=1
    rng=random.Random(7719)
    for n in (6,7,8,9):
        pairs=list(combinations(range(n),2))
        for repeat in range(90):
            ed=[p for p in pairs if rng.random()<rng.choice([0.21,0.4,0.65,0.8])]
            if not is_connected(n,ed):continue
            count+=1
            for root in [('v',i) for i in range(n)]+[('e',i) for i in range(len(ed))]:
                x=from_graph(n,ed,root);y=prediction(n,ed,root)
                assert x==y,(n,ed,root,x,y)
                root_count+=1
    # Petersen and pentagonal prism: ten vertices, cubic, triangle-free, nonisomorphic.
    # Petersen: outer 5-cycle, 5 spokes, inner pentagram.
    petersen=sorted({tuple(sorted(e)) for i in range(5) for e in ((i,(i+1)%5),(i,i+5),(i+5,5+(i+2)%5))})
    prism=sorted({tuple(sorted(e)) for i in range(5) for e in ((i,(i+1)%5),(i+5,5+(i+1)%5),(i,i+5))})
    assert len(petersen)==len(prism)==15
    for ed in (petersen,prism):
        for root in [('v',i) for i in range(10)]+[('e',i) for i in range(len(ed))]:
            assert from_graph(10,ed,root)==prediction(10,ed,root)
    def dist_profile(ed):
        return Counter(tuple(sorted((d,tuple(sorted(c.items()))) for d,c in from_graph(10,ed,r).items())) for r in [('v',i) for i in range(10)]+[('e',i) for i in range(len(ed))])
    assert dist_profile(petersen)==dist_profile(prism)
    # 5-cycle is present in Petersen but prism contains a 4-cycle.
    def four_cycles(ed):
        E=set(ed); N=range(10)
        for s in combinations(N,4):
            a,b,c,d=s
            for x,y,z,w in ((a,b,c,d),(a,b,d,c),(a,c,b,d)):
                if all(tuple(sorted(e)) in E for e in ((x,y),(y,z),(z,w),(w,x))):return True
        return False
    assert not four_cycles(petersen) and four_cycles(prism)
    print('VERIFY_OK')
    print('connected_test_graphs',count,'root_test_cases',root_count,'plus_two_cubic_examples',50)
    print('petersen_prism_profile_equal',True,'petersen_has_4cycle',False,'prism_has_4cycle',True)

if __name__=='__main__':run()
