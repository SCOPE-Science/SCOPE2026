"""Self-contained exact census of minimum two-neighbor percolating sets in GP(12,5)."""
from itertools import combinations
from collections import Counter
N=24
V=range(N)
# Construct the graph via the three edge families, then use a direct
# synchronous infection simulation (no forest/cycle predicate).
E=set()
for i in range(12):
    for a,b in ((i,(i+1)%12),(i,i+12),(i+12,12+(i+5)%12)):
        E.add(tuple(sorted((a,b))))
assert len(E)==36
neighbors=[0]*N
for a,b in E:
    neighbors[a]|=1<<b
    neighbors[b]|=1<<a
assert all(x.bit_count()==3 for x in neighbors)
full=(1<<N)-1
def forest_shape(initial_mask):
    remaining=set(v for v in V if not initial_mask >> v & 1)
    shape=[]
    while remaining:
        start=next(iter(remaining)); component={start}; queue=[start]
        for x in queue:
            for y in V:
                if y in remaining and neighbors[x] >> y & 1 and y not in component:
                    component.add(y); queue.append(y)
        remaining.difference_update(component)
        diameter=0
        for root in component:
            d={root:0}; q=[root]
            for x in q:
                for y in component:
                    if neighbors[x] >> y & 1 and y not in d:
                        d[y]=d[x]+1;q.append(y)
            diameter=max(diameter,max(d.values()))
        shape.append((len(component),diameter))
    return tuple(sorted(shape))
hist=Counter(); parts=Counter(); shapes=Counter(); smallest=0; fast=[]; slow=[]; examined=0
for c in combinations(V,7):
    examined+=1
    bits=sum(1<<v for v in c)
    # Cubic forest equality forces induced seed edges <=1 at k=7.
    internal=sum((neighbors[v]&bits).bit_count() for v in c)//2
    if internal>1:continue
    active=bits;rounds=0
    while active!=full:
        next_active=active
        for v in V:
            if not active&(1<<v) and (neighbors[v]&active).bit_count()>=2:
                next_active|=1<<v
        if next_active==active:break
        active=next_active;rounds+=1
    if active!=full:continue
    # The forest has c=2-e internal components, by 36-3k+e=17-c.
    components=2-internal
    assert components in (1,2)
    hist[rounds]+=1; parts[rounds,components]+=1
    if rounds in (4,8):shapes[rounds,forest_shape(bits)]+=1
    if rounds==4:fast.append(bits)
    if rounds==8:slow.append(bits)
assert examined==346104
assert dict(hist)=={4:120,5:3288,6:6456,7:1584,8:936}
assert dict(parts)=={(4,2):120,(5,1):1872,(5,2):1416,(6,1):4968,(6,2):1488,(7,1):1224,(7,2):360,(8,1):864,(8,2):72}
assert len(fast)==120 and len(slow)==936
assert dict(shapes)=={
 (4,((3,2),(14,6))):72,(4,((4,2),(13,6))):48,
 (8,((17,14),)):576,(8,((17,15),)):288,
 (8,((1,0),(16,14))):72}
print('PASS: 346104 seven-seed subsets, 12384 optima; time histogram',sorted(hist.items()))
print('PASS: forest component/time table',sorted(parts.items()))
print('PASS: all 120 fastest sets have two-component residual forests')
print('PASS: extremal residual-forest shapes',sorted(shapes.items()))
