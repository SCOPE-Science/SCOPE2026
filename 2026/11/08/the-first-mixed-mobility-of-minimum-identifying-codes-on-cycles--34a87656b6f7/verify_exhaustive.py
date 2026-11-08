"""Complete direct state-space verification for radius-one identifying codes on cycles."""
from itertools import combinations
from collections import Counter,deque
import json

def optimum(n):
    balls=[]
    for i in range(n):
        balls.append(set(((i-1)%n,i,(i+1)%n)))
    for size in range(n+1):
        opt=[]
        for subset in combinations(range(n),size):
            subset=set(subset)
            traces=[frozenset(b & subset) for b in balls]
            if all(traces) and len(set(traces))==n:
                opt.append(frozenset(subset))
        if opt:return size,opt
    return None,[]

def graph(n,states,slide):
    labels={s:i for i,s in enumerate(states)}
    adj=[set() for s in states]
    for i,s in enumerate(states):
        for v in s:
            for w in range(n):
                if w in s or (slide and (w-v)%n not in (1,n-1)):
                    continue
                new=(s-{v})|{w}
                j=labels.get(frozenset(new))
                if j is not None:adj[i].add(j)
    assert all(i in adj[j] for i,li in enumerate(adj) for j in li)
    unseen=set(range(len(states)));parts=[]
    while unseen:
        v=next(iter(unseen));unseen.remove(v);seen={v};queue=[v]
        for w in queue:
            for u in adj[w]:
                if u in unseen:
                    unseen.remove(u);seen.add(u);queue.append(u)
        parts.append(tuple(sorted(seen)))
    return adj,parts

def ecc(adj,component):
    res=[]
    for src in component:
        dist={src:0};queue=deque([src]);
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;queue.append(w)
        assert len(dist)==len(component)
        res.append(max(dist.values()))
    return min(res),max(res)

report={}
for n in range(4,12):
    size,states=optimum(n)
    assert size is not None
    slide,sparts=graph(n,states,True)
    jump,jparts=graph(n,states,False)
    data={
      'minimum_size':size,
      'optimum_count':len(states),
      'slide_edges':sum(map(len,slide))//2,
      'slide_degrees':dict(sorted(Counter(map(len,slide)).items())),
      'slide_components':dict(sorted(Counter(map(len,sparts)).items())),
      'jump_edges':sum(map(len,jump))//2,
      'jump_components':dict(sorted(Counter(map(len,jparts)).items())),
      'jump_degrees':dict(sorted(Counter(map(len,jump)).items()))
    }
    if n==11:
        assert len(sparts)==12
        nontriv=[c for c in sparts if len(c)>1]
        assert len(nontriv)==1
        data['mobile_radius_diameter']=ecc(slide,nontriv[0])
        data['jump_radius_diameter']=ecc(jump,jparts[0])
        data['mobile_component_is_cycle']=all(len(slide[v])==2 for v in nontriv[0])
    report[str(n)]=data
assert report['11']=={
 'minimum_size':7,'optimum_count':33,'slide_edges':22,
 'slide_degrees':{0:11,2:22},'slide_components':{1:11,22:1},
 'jump_edges':66,'jump_components':{33:1},'jump_degrees':{4:33},
 'mobile_radius_diameter':(11,11),'jump_radius_diameter':(4,5),
 'mobile_component_is_cycle':True
}
assert all(len([k for k in d['slide_degrees'] if k==0])==0 or len(d['slide_degrees'])==1 for n,d in report.items() if int(n)<11)
print(json.dumps(report,sort_keys=True,indent=2))
