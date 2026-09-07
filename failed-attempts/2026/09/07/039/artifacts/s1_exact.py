import sympy as sp
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
# spanning tree (BFS from 0), same as s1_search
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
print("nontree",non_tree)
# optimal mask 25 = 011001 over non_tree order [2,7,8,11,12,14]
mask=25
bits=[1]*15
for j,ei in enumerate(non_tree):
    bits[ei]=(mask>>j)&1
print("s1 bits (edge order 0..14, +1/-1 as 1/0):",bits)
print("edge list:",E)
svals=[1 if b==1 else -1 for b in bits]
print("s1 signs:",svals)

M=sp.zeros(10)
for (u,v),s in zip(E,svals):
    M[u,v]=s; M[v,u]=s
x=sp.Symbol('x')
cp=M.charpoly(x)
print("charpoly:",cp.as_expr())
print("factored:",sp.factor(cp.as_expr()))
# expected x^4*(x^2-5)^3
expected=x**4*(x**2-5)**3
print("matches expected:",sp.expand(cp.as_expr()-expected)==0)
