"""Independent exhaustive finite-state check for a diagonally linked rook network.
Uses direct updates and orbit tracing, not matrix ranks or linear-algebra software.
"""
from collections import Counter

def check(m,n,q):
    cells=m*n
    edges=[[] for _ in range(cells)]
    for i in range(cells):
        for j in range(cells):
            if i!=j and (i//n==j//n or i%n==j%n or {i,j}=={0,n+1}):
                edges[i].append(j)
    N=q**cells
    def update(state):
        vals=[]
        temp=state
        for _ in range(cells):
            vals.append(temp%q);temp//=q
        nxt=0;stride=1
        for nb in edges:
            z=0
            for j in nb:z^=vals[j]
            nxt+=z*stride;stride*=q
        return nxt
    next_state=[update(s) for s in range(N)]
    result=[None]*N
    for x in range(N):
        if result[x] is not None:continue
        path=[];seen={};y=x
        while y not in seen and result[y] is None:
            seen[y]=len(path);path.append(y);y=next_state[y]
        if result[y] is not None:
            t,p=result[y]
            for z in reversed(path):
                t+=1;result[z]=(t,p)
        else:
            k=seen[y];p=len(path)-k
            for z in path[k:]:result[z]=(0,p)
            for j in range(k-1,-1,-1):result[path[j]]=(k-j,p)
    obs=Counter(result)
    if m%2==0 and n%2==0:
        r=2
        divisor_dimensions={1:1,2:2}
        ranks=[cells,m+n,4,2] if cells!=4 else [4,2,2,2]
    elif m%2 and n%2:
        r=m+n
        divisor_dimensions={1:r-4,2:r-2,4:r}
        ranks=[cells,r,r,r]
    else:
        e=m if m%2==0 else n;o=n if m%2==0 else m
        r=e+4
        a=0 if e==2 else e-3
        b=0 if e==2 else e-2
        c=3 if e==2 else e
        divisor_dimensions={1:a,2:b,7:c,14:r}
        ranks=[cells,e+o+1,e+4,e+4]
    counts={}
    for p,d in divisor_dimensions.items():
        counts[p]=q**d-sum(v for j,v in counts.items() if p%j==0)
    expected=Counter()
    for t in range(4):
        if t==0:h=1
        else:
            h=q**(cells-ranks[t])-q**(cells-ranks[t-1])
        if h:
            for p,v in counts.items():
                if v:expected[t,p]=h*v
    assert obs==expected,(m,n,q,obs,expected)
    assert sum(obs.values())==N
    print('state_census',m,n,'q',q,'initial_states',N,'classes',dict(sorted(obs.items())),'OK')

for m,n,q in [(2,2,2),(2,3,2),(2,3,4),(2,4,2),(3,3,2),(3,4,2),(4,4,2)]:
    check(m,n,q)
print('all independent full-state comparisons OK')
