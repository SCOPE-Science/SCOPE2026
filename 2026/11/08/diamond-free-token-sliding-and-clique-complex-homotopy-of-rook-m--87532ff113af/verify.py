#!/usr/bin/env python3
"""Independent checks for matchings / token-sliding on rook graphs."""
import itertools, math, collections

def all_matchings(m,n,k):
    for rows in itertools.combinations(range(m),k):
        for cols in itertools.permutations(range(n),k):
            yield tuple(sorted(zip(rows,cols)))

def state_graph(m,n,k):
    states=list(all_matchings(m,n,k)); ix={s:i for i,s in enumerate(states)}
    adj=[set() for _ in states]
    for i,S in enumerate(states):
        R={u for u,v in S}; C={v for u,v in S}
        for u,v in S:
            base=set(S)-{(u,v)}
            for x in range(m):
                if x not in R:
                    j=ix[tuple(sorted(base|{(x,v)}))];adj[i].add(j)
            for y in range(n):
                if y not in C:
                    j=ix[tuple(sorted(base|{(u,y)}))];adj[i].add(j)
    return states,adj

def polynomial(m,n,k):
    a=m-k+1; b=n-k+1
    N=math.comb(m,k)*math.comb(n,k)*math.factorial(k)
    P=math.comb(m,k-1)*math.comb(n,k-1)*math.factorial(k-1)
    res={0:1,1:N}
    for t in range(2,max(a,b)+1):
        res[t]=P*(a*(math.comb(b,t) if t<=b else 0)+b*(math.comb(a,t) if t<=a else 0))
    return res

def get_cliques(adj):
    count=collections.Counter({0:1});vertices=list(range(len(adj)))
    def extend(clique,candidates):
        for h,v in enumerate(candidates):
            c=clique+[v];count[len(c)]+=1
            extend(c,[w for w in candidates[h+1:] if w in adj[v]])
    extend([],vertices)
    return dict(count)

def shortest_reach(adj):
    dist=[-1]*len(adj);dist[0]=0; q=collections.deque([0])
    while q:
        i=q.popleft()
        for j in adj[i]:
            if dist[j]<0: dist[j]=dist[i]+1;q.append(j)
    return sum(d>=0 for d in dist),max(dist)

def four_cycles(adj):
    # Every 4-cycle counted at each of 4 vertices and both orientations.
    count=0
    for u in range(len(adj)):
        common=collections.Counter()
        for v in adj[u]:
            for w in adj[v]:
                if w!=u:common[w]+=1
        count+=sum(c*(c-1)//2 for c in common.values())
    assert count%4==0
    return count//4

cases=0;verts=0;cliques=0
for m in range(1,7):
    for n in range(m,7):
        for k in range(1,m+1):
            N=math.comb(m,k)*math.comb(n,k)*math.factorial(k)
            if N>180:continue
            sts,adj=state_graph(m,n,k)
            assert len(sts)==N
            for i,neis in enumerate(adj):
                assert len(neis)==k*(m+n-2*k)
                for v in neis:assert i in adj[v]
            got=get_cliques(adj);expected=polynomial(m,n,k)
            assert got=={a:b for a,b in expected.items() if b},(m,n,k,got,expected)
            reached,diam=shortest_reach(adj)
            assert reached==(1 if m==n==k else N),(m,n,k,reached)
            if m==k and n==k+1:
                assert diam==k+k//2,(m,n,k,diam)
            if m==n==k+1:
                assert four_cycles(adj)==N*k*k//4,(m,n,k)
            cases+=1;verts+=N;cliques+=sum(got.values())-1
# Independently check the general common-core identity and diamond transfer
# on every labeled simple input graph on at most five vertices.
generic_instances=0
for order in range(1,6):
    edgelist=list(itertools.combinations(range(order),2))
    for mask in range(1<<len(edgelist)):
        gadj=[set() for _ in range(order)]
        for i,(a,b) in enumerate(edgelist):
            if mask>>i&1:
                gadj[a].add(b); gadj[b].add(a)
        diamond_input=False
        for four in itertools.combinations(range(order),4):
            if sum(v in gadj[u] for u,v in itertools.combinations(four,2))==5:
                diamond_input=True;break
        for kk in range(1,order+1):
            states=[frozenset(c) for c in itertools.combinations(range(order),kk)
                    if all(v not in gadj[u] for u,v in itertools.combinations(c,2))]
            idx={st:i for i,st in enumerate(states)}
            adj=[set() for _ in states]
            for a,st in enumerate(states):
                for u in st:
                    for v in gadj[u]:
                        if v not in st:
                            targ=(st-{u})|{v}
                            if targ in idx: adj[a].add(idx[targ])
            got=get_cliques(adj)
            for t in range(2, max(got,default=1)+1):
                RHS=0
                for Iraw in itertools.combinations(range(order),kk-1):
                    I=set(Iraw)
                    if any(v in gadj[u] for u,v in itertools.combinations(I,2)):continue
                    avail=set(range(order))-I
                    for u in I:avail.difference_update(gadj[u])
                    RHS+=sum(all(v in gadj[u] for u,v in itertools.combinations(c,2))
                             for c in itertools.combinations(avail,t))
                assert got.get(t,0)==RHS,(order,mask,kk,t,got,RHS)
            if not diamond_input:
                for four in itertools.combinations(range(len(states)),4):
                    assert sum(v in adj[u] for u,v in itertools.combinations(four,2))!=5,(order,mask,kk)
            generic_instances+=1
print('VERIFY_OK', 'cases='+str(cases), 'states='+str(verts),'nonempty_cliques='+str(cliques), 'clique_coefficients=PASS', 'degrees=PASS','connectivity=PASS','one_spare_diameters=PASS','two_spare_four_cycles=PASS', 'general_graph_instances='+str(generic_instances), 'core_identity=PASS', 'diamond_transfer=PASS')
