"""Self-contained exact checker for alternating-permutation Kendall codes.
Run: python3 verify.py (Python >=3.9, standard library only).
"""
from itertools import permutations, combinations
from collections import defaultdict, Counter
from pathlib import Path

def orientation(p):
    if len(p)<2: return 1
    signs=tuple(p[i]<p[i+1] for i in range(len(p)-1))
    if all(signs[i] != signs[i+1] for i in range(len(signs)-1)):
        return 1 if signs[0] else -1
    return 0

def zigzags(n):
    return [p for p in permutations(range(1,n+1)) if orientation(p)]

def adjacent_ball(p):
    yield p
    for i in range(len(p)-1):
        x=list(p); x[i],x[i+1]=x[i+1],x[i]
        yield tuple(x)

def conflicts(v):
    # A pair conflicts exactly when radius-one output balls overlap.
    source_index={p:i for i,p in enumerate(v)}
    buckets=defaultdict(list)
    for i,p in enumerate(v):
        for q in adjacent_ball(p): buckets[q].append(i)
    E=set()
    for idx in buckets.values():
        for a,b in combinations(idx,2): E.add((a,b))
    return sorted(E)

def graph_components(v,edges):
    adj=[set() for _ in v]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    unseen=set(range(len(v))); comps=[]
    while unseen:
        start=unseen.pop(); stack=[start]; c=[start]
        while stack:
            i=stack.pop()
            for j in adj[i]&unseen:
                unseen.remove(j);stack.append(j);c.append(j)
        comps.append((c,adj))
    return comps,adj

def independence_enumerator(indices,adj):
    # exact independent subset enumeration for components of <= 10 vertices
    best=-1;num=0
    for mask in range(1<<len(indices)):
        size=mask.bit_count()
        if size<best: continue
        chosen=[indices[i] for i in range(len(indices)) if mask>>i&1]
        if all(not (adj[i]&set(chosen)) for i in chosen):
            if size>best:best=size;num=1
            else:num+=1
    return best,num

EULER=[0,1,1,2,5,16,61,272,1385]
RESULTS={1:(1,1),2:(1,2),3:(2,2),4:(5,4),5:(16,9216),
         6:(80,2**42),7:(502,2**42),8:(2770,1)}
EDGES_EXPECTED={2:1,3:4,4:10,5:22,6:42,7:42,8:0}
for n in range(1,9):
    v=zigzags(n)
    assert len(v)==(1 if n==1 else 2*EULER[n])
    edges=conflicts(v)
    if n>=2: assert len(edges)==EDGES_EXPECTED[n]
    comps,adj=graph_components(v,edges)
    if n==3:
        assert len(comps)==1 and len(comps[0][0])==4
        assert all(len(adj[i])==2 for i in range(4))
    if n==4:
        assert len(comps)==1 and len(comps[0][0])==10 and len(edges)==10
    if n==5:
        expected_paths=Counter({(2,1):6,(4,3):2,(6,5):2})
        got_paths=Counter()
        for comp,_ in comps:
            deg=Counter(len(adj[i]) for i in comp)
            edge_count=sum(len(adj[i]) for i in comp)//2
            if len(comp)>2:
                assert deg[1]==2 and deg[2]==len(comp)-2 and len(deg)==2
            got_paths[(len(comp),edge_count)]+=1
        assert got_paths==expected_paths
    if n<=5:
        opt=0; num=1
        for comp,_ in comps:
            a,b=independence_enumerator(comp,adj)
            opt+=a;num*=b
    else:
        assert max(map(len,adj))<=1, (n,'not a matching')
        opt=len(v)-len(edges)
        num=2**len(edges)
    assert (opt,num)==RESULTS[n],(n,opt,num)
    if n in (6,7):
        path=Path(__file__).with_name('optimal_%d.txt'%n)
        code=[tuple(map(int,line.strip())) for line in path.read_text().splitlines() if line.strip()]
        assert len(code)==opt and len(set(code))==opt
        code_idx={v.index(p) for p in code}
        assert all(a not in code_idx or b not in code_idx for a,b in edges)
        assert all(p in v for p in code)
        profiles=Counter()
        for a,b in edges:
            p,q=v[a],v[b]
            assert orientation(p)*orientation(q)==-1
            centers=[]
            for i,j in combinations(range(1,n),2):
                if j==i+1:continue
                s=list(p);s[i-1],s[i]=s[i],s[i-1]
                s[j-1],s[j]=s[j],s[j-1]
                if tuple(s)==q:centers.append((i,j))
            assert len(centers)==1,(n,p,q,centers)
            profiles[centers[0]]+=1
        expected=({(1,4):12,(2,4):18,(2,5):12} if n==6
                  else {(2,5):42})
        assert dict(profiles)==expected,(n,profiles)
    print('n',n,'source',len(v),'conflicts',len(edges),'max_code',opt,'opt_codebooks',num)
print('VERIFY_OK')
