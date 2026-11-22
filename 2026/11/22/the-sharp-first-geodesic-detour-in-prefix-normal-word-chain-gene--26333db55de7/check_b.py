#!/usr/bin/env python3
"""Independent bitmask-DP construction and all-pair distance cross-check."""
from collections import Counter

def normal_mask(mask,n):
    for length in range(1,n+1):
        # integer mask: bit (n-i) is position i (one-based)
        prefix=(mask>>(n-length)).bit_count()
        for start in range(n-length+1):
            factor=((mask>>(n-(start+length))) & ((1<<length)-1)).bit_count()
            if factor>prefix:
                return False
    return True

def build(n):
    full=(1<<n)-1
    legal=[normal_mask(x,n) for x in range(1<<n)]
    dp={full:[()]}
    for depth in range(n):
        future={}
        for mask,paths in dp.items():
            for pos in range(1,n+1):
                flag=1<<(n-pos)
                if mask&flag and legal[mask^flag]:
                    target=mask^flag
                    future.setdefault(target,[]).extend(
                        path+(pos,) for path in paths)
        dp=future
    return dp.get(0,[])

def dist_bfs(vertices,n):
    idx={p:i for i,p in enumerate(vertices)}
    adj=[]
    for p in vertices:
        v=[]
        for j in range(n-1):
            s=list(p)
            s[j],s[j+1]=s[j+1],s[j]
            if tuple(s) in idx:
                v.append(idx[tuple(s)])
        adj.append(v)
    discrep=Counter()
    for i,p in enumerate(vertices):
        d={i:0};front=[i]
        for length in range(n*(n-1)//2+1):
            if not front:break
            next_front=[]
            for v in front:
                for y in adj[v]:
                    if y not in d:
                        d[y]=length+1;next_front.append(y)
            front=next_front
        assert len(d)==len(vertices)
        for j in range(i+1,len(vertices)):
            q=vertices[j]
            positions={letter:k for k,letter in enumerate(q)}
            reference=sum(positions[p[a]]>positions[p[b]]
                          for a in range(n) for b in range(a+1,n))
            if d[j]!=reference:discrep[(reference,d[j])]+=1
    return discrep

for n in range(1,8):
    vertices=sorted(build(n));discordant=dist_bfs(vertices,n)
    print('n=%d states=%d exceptional=%d profile=%s'%(n,len(vertices),sum(discordant.values()),dict(sorted(discordant.items()))))
    assert (not discordant) if n<7 else discordant=={(4,6):4,(5,7):6,(6,8):4,(7,9):3,(8,10):2,(9,11):1}
print('INDEPENDENT ENUMERATION PASS')
