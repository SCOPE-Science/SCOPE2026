import numpy as np
from collections import deque

def petersen_edges():
    E=[]
    for i in range(5):
        E.append((i,(i+1)%5))
    for i in range(5):
        E.append((i,5+i))
    for i in range(5):
        E.append((5+i,5+((i+2)%5)))
    return E
E=petersen_edges()
n=10
def signed_mat(bits):
    A=np.zeros((n,n))
    for (u,v),b in zip(E,bits):
        s = 1.0 if b==1 else -1.0
        A[u,v]+=s; A[v,u]+=s
    return A

adj=[[] for _ in range(n)]
for idx,(u,v) in enumerate(E):
    adj[u].append((v,idx)); adj[v].append((u,idx))
vis=[False]*n; tree=set()
dq=deque([0]); vis[0]=True
while dq:
    u=dq.popleft()
    for v,ei in adj[u]:
        if not vis[v]:
            vis[v]=True; tree.add(ei); dq.append(v)
non_tree=[i for i in range(15) if i not in tree]
print("tree",sorted(tree),"nontree",non_tree)

best=(1e9,None,None)
rows=[]
for mask in range(2**6):
    bits=[1]*15
    for j,ei in enumerate(non_tree):
        bits[ei]= (mask>>j)&1
    A=signed_mat(bits)
    ev=np.linalg.eigvalsh(A)
    rho=float(abs(ev).max())
    rows.append((rho,mask,ev))
    if rho<best[0]-1e-12:
        best=(rho,mask,ev.copy())
print("MIN rho over 64 switching classes:",best[0],"mask",best[1])
print("ev:",np.round(best[2],6))
# count how many achieve min
c=sum(1 for r,_,_ in rows if abs(r-best[0])<1e-9)
print("num optimal classes:",c)
for r,m,ev in sorted(rows,key=lambda t:t[0])[:8]:
    print(f"mask={m:02d} bits={m:06b} rho={r:.6f} ev={np.round(ev,3)}")
print("sqrt5=",5**0.5)
# also full 2^15 min check quickly
gmin=min(r for r,_,_ in rows)
print("switching-class min =",gmin)
