"""Finite exhaustive checks for rooted-tree conjunctive Horn closures.

No finite check establishes the infinite-size classification; the proof is in RESULT.md.
"""
from itertools import product
from collections import deque

def rooted_parents_from_code(n, code):
    if n == 1: return [None]
    # Prüfer code for labelled undirected trees; root at vertex zero.
    deg = [1] * n
    for x in code: deg[x] += 1
    edges=[]
    for x in code:
        y=next(v for v in range(n) if deg[v]==1)
        edges.append((y,x)); deg[y]-=1; deg[x]-=1
    u,v=[k for k in range(n) if deg[k]==1]
    edges.append((u,v))
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    par=[None]*n
    q=deque([0]); seen={0}
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w);par[w]=v;q.append(w)
    return par

def predicted_masks(par):
    n=len(par)
    ch=[[] for _ in range(n)]
    for v,p in enumerate(par):
        if p is not None:ch[p].append(v)
    good=set()
    for leaf in range(n):
        if ch[leaf]:continue
        mask=0;cur=leaf
        while cur is not None:
            mask|=1<<cur
            good.add(((1<<n)-1)^mask)
            cur=par[cur]
    return good

def observed_masks(par):
    n=len(par);ch=[[] for _ in range(n)]
    for v,p in enumerate(par):
        if p is not None:ch[p].append(v)
    allmask=(1<<n)-1
    closed=[]
    for X in range(1<<n):
        if all(not ch[v] or (any(not ((X>>w)&1) for w in ch[v])) or ((X>>v)&1) for v in range(n)):
            closed.append(X)
    result=set()
    for X in closed:
        if X==allmask:continue
        upper=[Y for Y in closed if Y!=X and X&Y==X]
        mins=[Y for Y in upper if not any(Z != Y and X&Z==X and Z&Y==Z for Z in upper)]
        if len(mins)==1:result.add(X)
    return result

def run():
    cases=0; ground_total=0; maximizers=0
    for n in range(1,8):
        codes=product(range(n),repeat=max(n-2,0)) if n>1 else [()]
        for code in codes:
            par=rooted_parents_from_code(n,code)
            a=predicted_masks(par);b=observed_masks(par)
            if a!=b:
                raise AssertionError((n,code,a,b))
            if not (n<=len(a)<=((n+1)**2//4)):
                raise AssertionError(('bounds',n,code,len(a)))
            cases+=1;ground_total+=2**n
            maximizers+=len(a)==((n+1)**2//4)
        print('n',n,'tested labelled rooted trees so far',cases)
    print('VERIFY_OK', 'tree_instances='+str(cases), 'subset_tests='+str(ground_total), 'maximizers='+str(maximizers))

if __name__=='__main__':run()
