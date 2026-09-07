import numpy as np, json
from collections import deque

D=json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/G1.json"))
E1=[tuple(e) for e in D["E1"]]
N1=20
# spanning tree BFS
adj=[[] for _ in range(N1)]
for idx,(u,v) in enumerate(E1):
    adj[u].append((v,idx)); adj[v].append((u,idx))
vis=[False]*N1; tree=set()
dq=deque([0]); vis[0]=True
while dq:
    u=dq.popleft()
    for w,ei in adj[u]:
        if not vis[w]: vis[w]=True; tree.add(ei); dq.append(w)
print("tree size",len(tree))
non_tree=[i for i in range(30) if i not in tree]
print("nontree",non_tree)

def rho_of(mask):
    S=np.zeros((N1,N1))
    for idx,(u,v) in enumerate(E1):
        if idx in tree: s=1.0
        else:
            j=non_tree.index(idx)
            s=1.0 if ((mask>>j)&1) else -1.0
        S[u,v]+=s; S[v,u]+=s
    ev=np.linalg.eigvalsh(S)
    return float(abs(ev).max()), ev

best=(1e9,None)
rows=[]
for mask in range(2**11):
    r,ev=rho_of(mask)
    rows.append(r)
    if r<best[0]-1e-12: best=(r,mask)
print("MIN over 2048 classes:",best[0],"mask",best[1])
rows=np.array(rows)
print("quantiles:",np.round(np.quantile(rows,[0,.01,.05,.25,.5,.75,1]),4))
print("num <=2.828:",int((rows<=2.828+1e-9).sum())," num<=2.60:",int((rows<=2.60+1e-9).sum()))
order=np.argsort(rows)
for m in order[:10]:
    r,ev=rho_of(int(m))
    print(f"mask={int(m)} rho={r:.6f} ev={np.round(ev,3)}")
json.dump({"best_mask":int(best[1]),"best_rho":float(best[0]),"nontree":non_tree,"tree":sorted(tree)},
 open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-76/output/artifacts/s2_search.json","w"))
