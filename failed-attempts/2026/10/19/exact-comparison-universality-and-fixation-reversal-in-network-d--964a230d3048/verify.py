"""Exact reproducibility checks for neighbor-payoff comparison under death--birth updating.

Only Python's standard library is required. All graph and fixation calculations use rational arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations


def connected(n, edges):
    seen = {0}
    while True:
        other = seen | {b for a,b in edges if a in seen} | {a for a,b in edges if b in seen}
        if other == seen:
            return len(seen) == n
        seen = other


def rank(rows, n):
    a = [list(row) for row in rows if any(row)]
    k = 0
    for col in range(n):
        pivot = next((j for j in range(k,len(a)) if a[j][col]), None)
        if pivot is None: continue
        a[k], a[pivot] = a[pivot], a[k]
        b = a[k][col]
        a[k] = [v/b for v in a[k]]
        for j in range(k+1,len(a)):
            t=a[j][col]
            if t: a[j]=[p-t*q for p,q in zip(a[j],a[k])]
        k+=1
        if k==len(a):break
    return k


def dim_silent(n, edges):
    adj = [set() for _ in range(n)]
    for i,j in edges: adj[i].add(j); adj[j].add(i)
    deg = list(map(len,adj))
    rows = []
    for nbr in adj:
        for i,k in combinations(sorted(nbr),2):
            for v in range(n):
                row = [F(0)]*n
                row[i] = F(int(v in adj[i]), deg[i])
                row[k] -= F(int(v in adj[k]),deg[k])
                rows.append(row)
    return n-rank(rows,n)


def complete_bipartite(n, edges):
    adj = [set() for _ in range(n)]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    side={0:0};todo=[0]
    for i in todo:
        for j in adj[i]:
            if j not in side:side[j]=1-side[i];todo.append(j)
            elif side[j]==side[i]:return False
    return len(side)==n and len(edges)==sum(x==0 for x in side.values())*sum(x==1 for x in side.values())


def atlas():
    totals=[]
    for n in range(2,6):
        pairs=list(combinations(range(n),2)); count=0
        for mask in range(1<<len(pairs)):
            edges=[p for i,p in enumerate(pairs) if mask & (1<<i)]
            if not connected(n,edges):continue
            dim=dim_silent(n,edges)
            expected=2 if complete_bipartite(n,edges) else 0
            assert dim==expected,(n,edges,dim,expected)
            count+=1
        totals.append((n,count))
    return totals


def fixation(N,R):
    assert N>=3 and R>0
    ratios=[]
    for k in range(1,N):
        qplus=F(N-k,N)*F(k*R,k*R+N-k-1)
        qminus=F(k,N)*F(N-k,(k-1)*R+N-k)
        ratios.append(qminus/qplus)
    s=F(1); q=F(1)
    for v in ratios:q*=v;s+=q
    direct=1/s
    formula=1/sum((F(N-1)+j*(R-1))/(F(N-1)*R**j) for j in range(N))
    assert direct==formula,(N,R,direct,formula)
    return direct


def main():
    print('Graph classification tests:',atlas())
    cases=0
    for n in range(3,12):
        for r in (F(1,5),F(1,2),F(1),F(2),F(3),F(7,3)):
            rho=fixation(n,r)
            if r==1:assert rho==F(1,n)
            elif r>1:assert rho>F(1,n)
            else:assert rho<F(1,n)
            cases+=1
    print('Exact fixation identities and signs:',cases,'cases passed')
    # Compare competing neighbors on K_{2,3}, with partitionwise-varying sensitivities.
    n=5; edges=[(i,j) for i in (0,1) for j in (2,3,4)]
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    lam=[F(7),F(7),F(-3,2),F(-3,2),F(-3,2)]
    tests=0
    for bits in range(1<<n):
        x=[F((bits>>i)&1) for i in range(n)]
        u=[-x[i]+3*sum(x[z] for z in adj[i])/len(adj[i]) for i in range(n)]
        obs=[lam[i]*sum(u[z] for z in adj[i])/len(adj[i]) for i in range(n)]
        for ns in adj:
            assert len({obs[i] for i in ns})==1
            tests+=1
    print('Partitionwise comparison cancellation:',tests,'replacement neighborhoods passed')
    # P4: removing one edge from C4 makes comparison observable for a donation-game state.
    edges=[(0,1),(1,2),(2,3)]
    adj=[set() for _ in range(4)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    x=[F(1),F(0),F(0),F(0)]
    u=[-x[i]+2*sum(x[z] for z in adj[i])/len(adj[i]) for i in range(4)]
    t=[sum(u[z] for z in adj[i])/len(adj[i]) for i in range(4)]
    assert u==[F(-1),F(1),F(0),F(0)] and t[0]-t[2]==F(1,2)
    print('P4 edge-deletion example: competitor log-fitness contrast shifts by',t[0]-t[2],'at positive comparison')

if __name__=='__main__':main()
