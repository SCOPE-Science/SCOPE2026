"""Independent all-reflection binary-vertex graph boundary component count.

One sign bit per polygon coordinate; no floating-point computations.
"""
from collections import defaultdict

def boundary_count(n):
    rotations=[tuple((i+k)%n for i in range(n)) for k in range(n)]
    reflections=[tuple((k-i)%n for i in range(n)) for k in range(n)]
    def act(mask,p):
        return sum(1<<p[i] for i in range(n) if mask & (1<<i))
    up={}
    def find(x):
        if x not in up:up[x]=x
        if up[x]!=x:up[x]=find(up[x])
        return up[x]
    def union(x,y):
        a,b=find(x),find(y)
        if a!=b:up[b]=a
    for p in reflections:
        indices=set(range(n));orbits=[]
        while indices:
            i=min(indices);j=p[i]
            indices-={i,j}
            orbits.append((i,) if i==j else (i,j))
        special=[o for o in orbits if len(o)==1 or ((o[0]-o[1])%n in (1,n-1))]
        regular=[o for o in orbits if o not in special]
        assert len(special)==2
        flip=[sum(1<<i for i in o) for o in special]
        for a in range(1<<len(regular)):
            base=sum(sum(1<<i for i in o) for t,o in enumerate(regular) if a&(1<<t))
            for b in range(4):
                union(base,base ^ (flip[0] if b&1 else 0) ^ (flip[1] if b&2 else 0))
    for u in list(up):
        for p in rotations+reflections:
            union(u,act(u,p))
    return len({find(u) for u in up})

if __name__=='__main__':
    expected={4:1,6:2,8:4,10:10,12:20}
    for n, want in expected.items():
        got=boundary_count(n)
        assert got==want
        print(f'n={n}: {got} boundary circles')
    print('EVEN_MIRROR_COMPONENT_CHECK_PASS')
