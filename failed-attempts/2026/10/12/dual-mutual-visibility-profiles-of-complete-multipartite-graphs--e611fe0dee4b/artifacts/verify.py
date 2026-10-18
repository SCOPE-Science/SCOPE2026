from collections import deque
from math import comb


def profiles_of(total):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2: out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            cur.append(x); rec(rem-x,x,cur); cur.pop()
    rec(total,1,[])
    return out


def graph(profile):
    part=[]
    for i,n in enumerate(profile): part += [i]*n
    N=len(part)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if part[u]!=part[v]: adj[u].add(v); adj[v].add(u)
    return adj


def distance(adj,u,v,blocked):
    q=deque([(u,0)]); seen={u}
    while q:
        x,d=q.popleft()
        if x==v: return d
        for w in adj[x]:
            if w in seen or (w in blocked and w!=v): continue
            seen.add(w); q.append((w,d+1))
    return None


def visible(adj,u,v,X):
    return distance(adj,u,v,set(X)-{u,v}) == distance(adj,u,v,set())


def direct_dual(adj,X):
    N=len(adj); X=set(X); Y=set(range(N))-X
    for u in range(N):
        for v in range(u+1,N):
            if ((u in X and v in X) or (u in Y and v in Y)) and not visible(adj,u,v,X):
                return False
    return True


def structural_dual(profile,X):
    N=sum(profile); X=set(X); Y=set(range(N))-X; start=0
    for n in profile:
        V=set(range(start,start+n)); start+=n
        x=len(X&V); y=len(Y&V)
        if (x>=2 or y>=2) and len(Y-V)==0:
            return False
    return True


def closed_coeffs(profile):
    N=sum(profile); p=sum(n>=2 for n in profile)
    coeff=[comb(N,k) for k in range(N+1)]
    if p==0: return coeff
    for n in profile:
        if n<2: continue
        if n==2:
            coeff[N]-=1
            coeff[N-2]-=1
        else:
            for j in range(n+1):
                coeff[N-n+j]-=comb(n,j)
    coeff[N]+=p-1
    return coeff


def partitions(n):
    blocks=[]
    def rec(v):
        if v==n:
            yield tuple(frozenset(b) for b in blocks); return
        for i in range(len(blocks)):
            blocks[i].add(v); yield from rec(v+1); blocks[i].remove(v)
        blocks.append({v}); yield from rec(v+1); blocks.pop()
    yield from rec(0)


def expected_chi(profile):
    if all(n==1 for n in profile): return 1
    star=(len(profile)==2 and min(profile)==1 and max(profile)>=2)
    if star and max(profile)>=3: return None
    return 2

profiles=0; subset_checks=0; partitions_checked=0
for N in range(2,9):
    for profile in profiles_of(N):
        profiles+=1
        adj=graph(profile)
        cache={}; counts=[0]*(N+1)
        for mask in range(1<<N):
            X=frozenset(v for v in range(N) if mask>>v&1)
            subset_checks+=1
            d=direct_dual(adj,X)
            s=structural_dual(profile,X)
            if d!=s:
                raise AssertionError(('set-characterization',profile,tuple(sorted(X)),d,s))
            cache[X]=d
            if d: counts[len(X)]+=1
        if counts!=closed_coeffs(profile):
            raise AssertionError(('polynomial',profile,counts,closed_coeffs(profile)))
        minimum=None
        for P in partitions(N):
            partitions_checked+=1
            if minimum is None and all(cache[B] for B in P): minimum=len(P)
        exp=expected_chi(profile)
        if minimum!=exp:
            raise AssertionError(('chromatic',profile,minimum,exp))

print(
    'ALL CHECKS PASSED; '
    f'profiles={profiles}; '
    f'subset_checks={subset_checks}; '
    f'partitions_checked={partitions_checked}; '
    'orders=2..8'
)
