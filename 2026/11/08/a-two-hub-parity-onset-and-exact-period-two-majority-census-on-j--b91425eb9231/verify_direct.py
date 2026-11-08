"""Independent graph-neighborhood majority simulator, all labelled inputs."""

def update(state,n,neighbors):
    out=0
    for v,neis in enumerate(neighbors):
        ones=sum((state>>u)&1 for u in neis)
        bit= (1 if 2*ones>len(neis) else
              0 if 2*ones<len(neis) else (state>>v)&1)
        out |= bit<<v
    return out

def graph(n):
    a=[set() for _ in range(n+2)]
    def edge(u,v):a[u].add(v);a[v].add(u)
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,n);edge(i,n+1)
    edge(n,n+1)
    assert all(len(a[i])==4 for i in range(n))
    assert len(a[n])==len(a[n+1])==n+1
    return [sorted(x) for x in a]

def C(n,k):
    from math import comb
    return comb(n,k) if 0<=k<=n else 0

def S(n):
    a=0
    for k in range(1,n):
        for r in range(1,min(k//3,n-k)+1):
            if 2*k>n+1 and 2*(k-2*r)<n-1:
                a+=n*C(k-2*r-1,r-1)*C(n-k-1,r-1)//r
    return a

def B(n):
    if n%2:return 0
    m=n//2
    return sum(n*C(m-r-1,r-1)**2//r for r in range(1,m//2+1))

for n in range(3,17):
    g=graph(n)
    fixed=primitive=0
    phases={}
    for x in range(1<<(n+2)):
        y=update(x,n,g)
        if y==x:fixed+=1
        elif update(y,n,g)==x:
            primitive+=1
            h=((x>>n)&3,(y>>n)&3)
            phases[h]=phases.get(h,0)+1
    assert fixed==2,(n,fixed)
    expected=2*S(n)+(2*(B(n)+2) if n%2==0 else 0)
    assert primitive==expected,(n,primitive,expected)
    assert set(phases).issubset({(0,3),(3,0),(1,2),(2,1)})
    assert phases.get((0,3),0)==S(n)
    assert phases.get((3,0),0)==S(n)
    z=B(n)+2 if n%2==0 else 0
    assert phases.get((1,2),0)==z
    assert phases.get((2,1),0)==z
    print(n,fixed,primitive,phases,flush=True)
print('INDEPENDENT_EXHAUSTIVE_DYNAMICS_PASS')
