"""Exhaustive exact certificate for edge-deletion forests of the cube line graph."""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256

cube_edges = [(a,b) for a in range(8) for b in range(a+1,8) if (a^b).bit_count()==1]
assert len(cube_edges)==12
# The cuboctahedral graph is the line graph of Q3.
line_edges = [(a,b) for a in range(12) for b in range(a+1,12) if set(cube_edges[a]) & set(cube_edges[b])]
assert len(line_edges)==24

def is_acyclic(mask):
    parent = list(range(12))
    def find(i):
        while i!=parent[i]:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for a,b in line_edges:
        if ((mask>>a)&1) and ((mask>>b)&1):
            ra,rb=find(a),find(b)
            if ra==rb:
                return False
            parent[ra]=rb
    return True

# A deleted set of five vertices gives the complement of an induced forest.
opt=[]
for s in combinations(range(12),5):
    deleted = sum(1<<j for j in s)
    kept = ((1<<12)-1)^deleted
    if is_acyclic(kept): opt.append(kept)
assert len(opt)==72
assert all(not is_acyclic(sum(1<<i for i in s)) for s in combinations(range(12),8))
index={s:i for i,s in enumerate(opt)}
slide=[set() for _ in opt]; jump=[set() for _ in opt]
for i,mask in enumerate(opt):
    inside=[a for a in range(12) if mask>>a&1]
    outside=[b for b in range(12) if not (mask>>b&1)]
    for a in inside:
        for b in outside:
            alt=mask^(1<<a)^(1<<b)
            j=index.get(alt)
            if j is not None:
                jump[i].add(j)
                if (a,b) in line_edges or (b,a) in line_edges:
                    slide[i].add(j)

def summarize(adj):
    degree=Counter(map(len,adj))
    pair=Counter();ecc=Counter();shells={}
    for i in range(len(opt)):
        d={i:0}; queue=deque([i])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if w not in d:
                    d[w]=d[v]+1;queue.append(w)
        ecc[len(d),max(d.values())]+=1
        for j in range(i+1,len(opt)): pair[d[j]]+=1
        shells[i]=tuple(Counter(d.values())[k] for k in range(max(d.values())+1))
    return degree,pair,ecc,shells
sdeg,spair,secc,sshell=summarize(slide)
jdeg,jpair,jecc,jshell=summarize(jump)
assert sdeg=={4:72} and spair=={1:144,2:408,3:624,4:732,5:504,6:144}
assert secc=={(72,6):72}
assert jdeg=={9:48,4:24} and jpair=={1:264,2:408,3:576,4:684,5:480,6:144}
assert jecc=={(72,6):72}
assert all(slide[i].issubset(jump[i]) for i in range(72))
print('line-graph vertices=12 edges=24; optimal deletion size=5 count=72')
print('slide edges=144 degrees=',dict(sdeg),'eccentricities=',dict(secc))
print('slide unordered pair histogram=',dict(sorted(spair.items())))
print('jump edges=264 degrees=',dict(jdeg),'eccentricities=',dict(jecc))
print('jump unordered pair histogram=',dict(sorted(jpair.items())))
print('slide shell distribution=',dict(Counter(sshell.values())))
print('jump shell distribution=',dict(Counter(jshell.values())))
print('pass')
