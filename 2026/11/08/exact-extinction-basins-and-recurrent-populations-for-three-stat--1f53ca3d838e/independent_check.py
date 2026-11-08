"""Independent trajectory and rainbow-triangle verification for finite cases."""
from collections import Counter

def check(r):
    n=2*r
    N=3**n
    powers=[3**v for v in range(n)]
    nbrs=[tuple(w for w in range(n) if w != v and w//2 != v//2) for v in range(n)]
    def decode(z):
        return tuple((z//p)%3 for p in powers)
    def update(z):
        x=decode(z)
        y=[((a+1)%3 if a else int(any(x[w]==1 for w in nbrs[v]))) for v,a in enumerate(x)]
        return sum(p*c for p,c in zip(powers,y))
    # A forward-trace resolver, without an indegree peel.
    fate=[None]*N
    depth=[None]*N
    transitions={}
    cycles=Counter()
    for start in range(N):
        if fate[start] is not None:
            continue
        path=[]; seen={}; v=start
        while fate[v] is None and v not in seen:
            seen[v]=len(path);path.append(v)
            if v not in transitions:transitions[v]=update(v)
            v=transitions[v]
        if fate[v] is None:
            j=seen[v]
            length=len(path)-j
            cycles[length]+=1
            for w in path[j:]:fate[w]=length;depth[w]=0
            path=path[:j]
        for w in reversed(path):
            b=transitions[w]
            fate[w]=fate[b]
            depth[w]=depth[b]+1
    basins=Counter(fate)
    periodic=sum(x==0 for x in depth)
    # Independently detect a rainbow triangle from pair-color support.
    rain=0
    for z in range(N):
        x=decode(z)
        if any(x[2*a+i]==0 and x[2*b+j]==1 and x[2*c+k]==2
               for a in range(r) for b in range(r) for c in range(r)
               if a!=b and a!=c and b!=c
               for i in range(2) for j in range(2) for k in range(2)):
            rain+=1
    fixed=3*(2**n)-3+6*r
    c3=(3**n-3*2**n+3-3*n*(2**(n-2)-1))//3
    assert basins==Counter({1:fixed,3:N-fixed})
    assert cycles==Counter({1:1,3:c3})
    assert periodic==1+3*c3
    assert rain==N-fixed
    print(f"r={r} states={N} cycles={dict(sorted(cycles.items()))} basin={dict(sorted(basins.items()))} rainbow={rain} periodic={periodic} max_entry={max(depth)}")

if __name__=='__main__':
    for r in range(3,6):check(r)
    print('INDEPENDENT_CHECKS_OK')
