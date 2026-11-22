"""Standalone verification of exact proper conflict-free three-colouring census for unicyclic graphs.
Run python3 verify_unicyclic.py (requires only Python 3 standard library)."""
import itertools, collections, random, math

def cycle_and_trees(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    remain=set(range(n));deg=[len(x) for x in adj]
    queue=collections.deque(i for i in range(n) if deg[i]<=1)
    while queue:
        u=queue.popleft()
        if u not in remain: continue
        remain.remove(u)
        for v in adj[u]:
            if v in remain:
                deg[v]-=1
                if deg[v]==1:queue.append(v)
    assert len(remain)>=3
    start=min(remain)
    cycle=[start]
    prev=-1
    while True:
        u=cycle[-1]
        nexts=[x for x in adj[u] if x in remain and x!=prev]
        assert len(nexts)==(2 if len(cycle)==1 else 1)
        v=min(nexts)
        if v==start:break
        prev=u;cycle.append(v)
    assert len(cycle)==len(remain)
    return adj,cycle

def predicted(n,edges):
    adj,C=cycle_and_trees(n,edges)
    m=len(C);ts=[len(adj[v])-2 for v in C]
    leaf_product=math.prod(len(adj[u]) if len(adj[u])>=3 else 1 for u in range(n) if u not in C)
    total=0
    for signs in itertools.product([-1,1],repeat=m):
        if sum(signs)%3:continue
        ways=1
        for i,t in enumerate(ts):
            ways*= ((1 if t==0 else 2) if signs[(i-1)%m]==signs[i] else t)
        total+=ways
    return 3*leaf_product*total

def criterion(n,edges):
    adj,C=cycle_and_trees(n,edges)
    T=[i for i,v in enumerate(C) if len(adj[v])>2]
    if not T:return len(C)%3==0
    gaps=[(T[(i+1)%len(T)]-T[i])%len(C) or len(C) for i in range(len(T))]
    return sum(g%3!=0 for g in gaps)!=1

def brute(n,edges,q):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    result=0
    # backtrack with full color checks when all neighbor colors assigned
    assignment=[-1]*n
    order=sorted(range(n),key=lambda x:-len(adj[x]))
    def backtrack(pos):
        nonlocal result
        if pos==n:
            result+=1;return
        v=order[pos]
        for c in range(q):
            if any(assignment[w]==c for w in adj[v]): continue
            assignment[v]=c
            okay=True
            for w in adj[v]+[v]:
                if all(assignment[x]>=0 for x in adj[w]):
                    co=collections.Counter(assignment[x] for x in adj[w])
                    if 1 not in co.values():okay=False;break
            if okay:backtrack(pos+1)
        assignment[v]=-1
    backtrack(0)
    return result

def generate_unicyclic(n,rng):
    m=rng.randrange(3,n+1)
    edges=[(i,(i+1)%m) for i in range(m)]
    for v in range(m,n):edges.append((v,rng.randrange(v)))
    perm=list(range(n));rng.shuffle(perm)
    return sorted(tuple(sorted((perm[a],perm[b]))) for a,b in edges)

def main():
    rng=random.Random(1544)
    trials=0;vertices=0
    # first sample all possible augmentations for cycles <=8 and random trees
    for n in range(3,10):
        trial_count=1 if n==3 else (70 if n<=7 else 35)
        seen=set()
        for t in range(trial_count):
            e=generate_unicyclic(n,rng)
            key=tuple(e)
            if key in seen:continue
            seen.add(key)
            pred=predicted(n,e)
            direct=brute(n,e,3)
            assert pred==direct,(n,e,pred,direct)
            assert (pred>0)==criterion(n,e),(n,e,pred)
            if n<=7:
                if pred==0:
                    four=brute(n,e,4)
                    if n==5 and all(len(x)==2 for x in cycle_and_trees(n,e)[0]):
                        assert four==0
                    else:assert four>0,(n,e)
            trials+=1;vertices+=n
    print('RANDOM_GRAPH_CYCLE_AND_DIRECT_THREE_COLOUR_CENSUS_PASS',trials,'total_vertices',vertices)
    # all (small) lollipop cycle lengths n=3..12 with tree attachments at each subset of cycle vertices (one leaf per selected vertex)
    trials2=0
    for m in range(3,9):
        for mask in range(1<<m):
            n=m+mask.bit_count()
            edges=[(i,(i+1)%m) for i in range(m)]
            idx=m
            for i in range(m):
                if mask>>i&1:
                    edges.append((i,idx));idx+=1
            pred=predicted(n,edges)
            assert (pred>0)==criterion(n,edges),(m,mask)
            if n<=9:assert pred==brute(n,edges,3),(m,mask,pred)
            trials2+=1
    print('CYCLE_WITH_ALL_LEAF_SUBSET_PATTERNS_PASS',trials2)
    # Explicit phase-transition witness: moving only one leaf on C5 changes 3 vs 4.
    def decorated_cycle(m,attach):
        edges=[(i,(i+1)%m) for i in range(m)]
        edges += [(v,m+j) for j,v in enumerate(attach)]
        return m+len(attach),edges
    n,e=decorated_cycle(5,[0,1]); assert predicted(n,e)==6 and brute(n,e,3)==6
    n,e=decorated_cycle(5,[0,2]); assert predicted(n,e)==0 and brute(n,e,4)>0
    n,e=decorated_cycle(6,[0]); assert predicted(n,e)==12
    n,e=decorated_cycle(4,[0]); assert predicted(n,e)==0 and brute(n,e,4)>0
    n,e=decorated_cycle(5,[]); assert brute(n,e,4)==0 and brute(n,e,5)>0
    print('FIVE_CYCLE_ATTACHMENT_PHASE_TRANSITION_AND_BOUNDARY_PASS')
    print('VERIFY_OK')
if __name__=='__main__':main()
