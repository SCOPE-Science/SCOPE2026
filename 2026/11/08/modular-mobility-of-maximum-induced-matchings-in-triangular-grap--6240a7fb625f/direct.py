"""Independent direct construction of induced matchings in T_n, with exhaustive checks."""
import itertools,collections,math

def run(n):
    V=list(itertools.combinations(range(n),2))
    E=[(i,j) for i in range(len(V)) for j in range(i+1,len(V)) if len(set(V[i])&set(V[j]))==1]
    adj=[set() for _ in V]
    for i,j in E:adj[i].add(j);adj[j].add(i)
    k=n//3
    selected=[]
    for inds in itertools.combinations(range(len(E)),k):
        if any((set(E[inds[p]]) & set(E[inds[q]])) or
               any(v in adj[u] for u in E[inds[p]] for v in E[inds[q]])
               for p in range(k) for q in range(p+1,k)):
            continue
        selected.append(tuple(inds))
    S=set(selected)
    jump={s:set() for s in S};slide={s:set() for s in S}
    for s in S:
        for old in s:
            remaining=set(s)-{old}
            for new in range(len(E)):
                if new in s: continue
                t=tuple(sorted(remaining|{new}))
                if t in S:
                    jump[s].add(t)
                    if bool(set(E[old])&set(E[new])): slide[s].add(t)
    def comps(graph):
        seen=set(); sizes=[]
        for v in graph:
            if v in seen:continue
            q=[v];seen.add(v)
            for a in q:
                for b in graph[a]:
                    if b not in seen:seen.add(b);q.append(b)
            sizes.append(len(q))
        return sorted(collections.Counter(sizes).items())
    r=n%3; cnt=math.factorial(n)//(math.factorial(r)*2**k*math.factorial(k))
    assert len(S)==cnt,(n,len(S),cnt)
    assert all(len(v)==k*({0:2,1:11,2:29}[r]) for v in jump.values()),n
    assert all(len(v)==k*({0:2,1:6,2:10}[r]) for v in slide.values()),n
    ecomp=[(3**k,math.factorial(n)//(6**k*math.factorial(k)))] if r==0 else [(cnt,1)]
    assert comps(jump)==ecomp,(n,'TJ',comps(jump),ecomp)
    assert comps(slide)==ecomp,(n,'TS',comps(slide),ecomp)
    print('PASS direct',n,'Tedges',len(E),'optima',cnt,'TJ_degree',next(iter(jump.values())).__len__(),'TS_degree',next(iter(slide.values())).__len__(),'components',ecomp,flush=True)
for n in range(3,9):run(n)
