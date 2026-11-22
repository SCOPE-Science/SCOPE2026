from collections import defaultdict

def witness(n):
    s=set(range(2,n-1,3)) if n%3==1 else set(range(1,n,3))
    # swaps positions 1-based; adjacent swaps all simultaneous, centers spaced by three
    p=list(range(n))
    q=p.copy()
    for k in sorted(s): q[k-1],q[k]=q[k],q[k-1]
    edges=set()
    for order in (p,q):
        for i in range(n-1):
            a,b=order[i:i+2]
            if (i%2==0)==(order is p):
                edges.add((a,b))
            else:
                edges.add((b,a))
    deg={i:0 for i in range(n)}; neigh=defaultdict(list)
    for a,b in edges: deg[b]+=1;neigh[a].append(b)
    avail=[u for u in deg if deg[u]==0]; topo=[]
    while avail:
        a=avail.pop();topo.append(a)
        for b in neigh[a]:
            deg[b]-=1
            if deg[b]==0:avail.append(b)
    assert len(topo)==n,(n,s,edges)
    rank={u:i for i,u in enumerate(topo)}
    a=[rank[u] for u in p];b=[rank[u] for u in q]
    assert all((a[i]<a[i+1]) == (i%2==0) for i in range(n-1))
    assert all((b[i]<b[i+1]) == (i%2!=0) for i in range(n-1))
    assert len(s)==(n+1)//3
    return n,sorted(s),a,b
for n in range(2,101):
    witness(n)
for n in (2,3,4,5,6,7,8,9,20,100):print(witness(n)[0:2])
print('WITNESS_OK')
