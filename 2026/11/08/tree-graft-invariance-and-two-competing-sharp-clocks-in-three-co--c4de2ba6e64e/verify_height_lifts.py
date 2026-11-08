"""Independent randomized checks of a max-neighbor integer lift for ternary cyclic dynamics."""
import random

def neighbor_graph(c, parents):
    n=len(parents)
    edges=[(u,v) for u in range(c) for v in range(u+1,c)]
    edges +=[(v,parents[v]) for v in range(c,n)]
    nbr=[[] for _ in range(n)]
    for u,v in edges:
        nbr[u].append(v);nbr[v].append(u)
    return nbr

def direct_step(x,nbr):
    return [(a+1)%3 if any(x[j]==(a+1)%3 for j in nbr[i]) else a for i,a in enumerate(x)]

def lift_delta(a,b):
    return ((b-a+1)%3)-1

def trial(c,parents,x):
    n=len(x);nr=neighbor_graph(c,parents)
    d=[0]*n;roots=list(range(c))
    for v in range(c,n):
        d[v]=d[parents[v]]+1
        roots.append(roots[parents[v]])
    H=max(d)
    initial=x[:] 
    has_three=len(set(x[:c]))==3
    if has_three:
        lift=[int(x[i]) for i in range(c)]+[0]*(n-c)
        for v in range(c,n):lift[v]=lift[parents[v]]+lift_delta(x[parents[v]],x[v])
    else:
        col0=x[0]
        uniq=list(set(x[:c]))
        if len(uniq)==1:level={col0:col0}
        else:
            a,b=uniq
            if (a+1)%3==b:level={a:a,b:a+1}
            else:level={b:b,a:b+1}
        lift=[level[x[i]] for i in range(c)]+[0]*(n-c)
        for v in range(c,n):lift[v]=lift[parents[v]]+lift_delta(x[parents[v]],x[v])
    tbound=2*H+n
    for t in range(tbound+1):
        if [v%3 for v in lift]!=x:raise AssertionError(('color mismatch',t,c,parents,x,lift))
        if has_three and t>=2*H:
            if any(lift[v]!=int(initial[roots[v]])+t-d[v] for v in range(c,n)):
                raise AssertionError(('wave late',t,c,parents,x,lift))
        if not has_three and t>=n-1:
            if len(set(x))!=1:raise AssertionError(('no consensus',t,c,parents,x))
        if t==tbound:break
        newx=direct_step(x,nr)
        newlift=lift[:]
        for v in range(n):
            newlift[v]=(lift[v]+1) if v<c and has_three else max([lift[v]]+[lift[u] for u in nr[v]])
        for u in range(n):
            for v in nr[u]:
                if (has_three and u<c and v<c):continue
                if abs(newlift[u]-newlift[v])>1:raise AssertionError(('lost Lipschitz',t,u,v))
        x=newx;lift=newlift

rng=random.Random(195201)
for iteration in range(7000):
    c=rng.randint(3,6)
    n=c+rng.randint(1,14)
    p=[-1]*c
    for v in range(c,n):p.append(rng.randrange(v))
    x0=[rng.randrange(3) for _ in range(n)]
    x=x0[:]
    trial(c,p,x)
print('INDEPENDENT_HEIGHT_CHECK_OK: 7000 seeded random clique-of-trees networks with direct color steps and lifted max process')
