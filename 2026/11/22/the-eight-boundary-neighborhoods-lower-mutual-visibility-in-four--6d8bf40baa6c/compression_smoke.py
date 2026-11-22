"""Cross-check order-gap truncation for cylinder mutual visibility (finite tests only)."""
import random
from collections import deque

def graph(n):
    a=[[] for _ in range(4*n)]
    for r in range(4):
        for c in range(n):
            u=r*n+c
            a[u]=[((r+1)%4)*n+c,((r-1)%4)*n+c]
            if c:a[u].append(u-1)
            if c+1<n:a[u].append(u+1)
    return a

def visible(u,v,chosen,n,g):
    dr=abs(u//n-v//n)
    original=min(dr,4-dr)+abs(u%n-v%n)
    blocked=chosen-{u,v}
    q=deque([(u,0)])
    seen={u}
    while q:
        x,depth=q.popleft()
        if x==v:return depth==original
        if depth>=original:continue
        for y in g[x]:
            if y not in seen and y not in blocked:
                seen.add(y)
                q.append((y,depth+1))
    return False

def valid(chosen,n,g):
    return all(visible(u,v,chosen,n,g) for i,u in enumerate(sorted(chosen)) for v in sorted(chosen)[i+1:])

def maximal(chosen,n,g):
    if not valid(chosen,n,g):return False
    return all(not valid(chosen|{x},n,g) for x in range(4*n) if x not in chosen)

def compress(chosen,n):
    cols=sorted({u%n for u in chosen})
    mp={cols[0]:min(cols[0],2)}
    for a,b in zip(cols,cols[1:]):mp[b]=mp[a]+min(b-a,4)
    m=mp[cols[-1]]+min(n-1-cols[-1],2)+1
    return {u//n*m+mp[u%n] for u in chosen},m

def run():
    rng=random.Random(291105)
    tests=0; feasible_cases=0; maximal_cases=0
    for n in (2,3,4,5,6,7,8,10,12,17,20,30,48):
        g=graph(n)
        for i in range(110):
            if i%2:
                s=set()
                for v in rng.sample(range(4*n),4*n):
                    if len(s)==4:break
                    if valid(s|{v},n,g):s.add(v)
                if len(s)<3:continue
            else:
                s=set(rng.sample(range(4*n),rng.choice((3,4))))
            t,m=compress(s,n)
            h=graph(m)
            a=valid(s,n,g); b=valid(t,m,h)
            assert a==b,("feasibility",n,s,m,t)
            x=maximal(s,n,g);y=maximal(t,m,h)
            assert x==y,("maximality",n,s,m,t)
            tests+=1;feasible_cases+=int(a);maximal_cases+=int(x)
    print("COMPRESSION_TEST_OK",tests,feasible_cases,maximal_cases)

if __name__=='__main__':run()
