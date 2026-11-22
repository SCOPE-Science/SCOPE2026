"""Finite independent checks of optimal edge-geodesic packings on Q_2,Q_3."""
from itertools import permutations, combinations


def cube_data(d):
    edges=[]
    for u in range(1<<d):
        for i in range(d):
            v=u^(1<<i)
            if u<v:
                edges.append((u,v,i))
    index={(u,v):j for j,(u,v,_) in enumerate(edges)}
    geodesics=set()
    for a in range(1<<d):
        for b in range(a+1,1<<d):
            directions=[i for i in range(d) if ((a^b)>>i)&1]
            for order in permutations(directions):
                u=a;mask=0
                for i in order:
                    v=u^(1<<i)
                    mask |= 1<<index[min(u,v),max(u,v)]
                    u=v
                assert u==b
                geodesics.add(mask)
    return edges, geodesics


def test(d):
    edges,paths=cube_data(d)
    paths_by_t={t:tuple(p for p in paths if p.bit_count()>t) for t in range(2,d+1)}
    direction_masks=[]
    for i in range(d):
        direction_masks.append(sum(1<<j for j,e in enumerate(edges) if e[2]==i))
    for t in range(2,d+1):
        target=t*(1<<(d-1)); found=[]
        for subset in range(1<<len(edges)):
            if subset.bit_count()!=target:continue
            if all((subset&p).bit_count()<=t for p in paths_by_t[t]):found.append(subset)
        expected={sum(direction_masks[i] for i in choice) for choice in combinations(range(d),t)}
        assert set(found)==expected,(d,t,len(found),len(expected))
        print('Q%d t=%d optimum_size=%d exhaustive_optima=%d expected=%d: PASS' % (d,t,target,len(found),len(expected)))

for d in (2,3):test(d)
