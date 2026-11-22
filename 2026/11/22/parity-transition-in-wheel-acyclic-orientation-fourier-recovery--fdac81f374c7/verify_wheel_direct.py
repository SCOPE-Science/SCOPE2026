"""Independent edge-orientation enumeration and Walsh transform for wheel graphs."""

def acyclic(n, x):
    # Edges: spoke i, followed by rim edge from i to i+1, both with bit zero
    indeg=[0]*(n+1)
    outgoing=[[] for _ in range(n+1)]
    for i in range(n):
        u,v=(i+1,0) if (x>>i)&1 else (0,i+1)
        indeg[v]+=1;outgoing[u].append(v)
        u,v=(1+(i+1)%n,i+1) if (x>>(n+i))&1 else (i+1,1+(i+1)%n)
        indeg[v]+=1;outgoing[u].append(v)
    queue=[i for i in range(n+1) if not indeg[i]]
    head=0
    while head<len(queue):
        u=queue[head];head+=1
        for v in outgoing[u]:
            indeg[v]-=1
            if not indeg[v]:queue.append(v)
    return len(queue)==n+1

def walsh(a):
    x=a[:];shift=1
    while shift<len(x):
        for q in range(0,len(x),2*shift):
            for j in range(q,q+shift):
                x[j],x[j+shift]=x[j]+x[j+shift],x[j]-x[j+shift]
        shift*=2
    return x

def check(n):
    a=[int(acyclic(n,x)) for x in range(1<<(2*n))]
    w=walsh(a)
    N=3**n-3
    assert sum(a)==N
    assert w[0]==N
    assert sum(v*v for v in w)==4**n*N
    assert all((v==0 if i.bit_count()%2 else True) for i,v in enumerate(w))
    if n%2==0:
        assert all(v%4==2 for i,v in enumerate(w) if i.bit_count()%2==0)
        assert sum(v!=0 for v in w)==2**(2*n-1)
        assert min(abs(v) for v in w if v)==2
        assert max(abs(v) for v in w)==N
    else:
        rim=(1<<n)-1
        for a in range(1<<n):
            if a.bit_count()%2:
                assert w[a+(rim<<n)]==0
        assert sum(v==0 and i.bit_count()%2==0 for i,v in enumerate(w))>=2**(n-1)
    return n,N,sum(v!=0 for v in w)

if __name__=='__main__':
    for n in range(3,9):
        print('DIRECT_WHEEL',*check(n))
    print('DIRECT_WHEEL_OK')
