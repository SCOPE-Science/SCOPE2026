"""Exact census and reconfiguration certificate for two-colour line splittings of AG(2,4)."""
from collections import Counter, deque

# The field has elements 0,1,z,z+1 represented by 0,1,2,3,
# with z^2=z+1. Coordinates of each point are (x,y).
def times(a,b):
    out=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): out ^= 1<<(i+j)
    if out&4: out ^= 7
    return out

lines=[]
for x in range(4):
    lines.append(sum(1<<(4*x+y) for y in range(4)))
for m in range(4):
    for b in range(4):
        lines.append(sum(1<<(4*x+(times(m,x)^b)) for x in range(4)))
assert len(lines)==len(set(lines))==20
assert all(l.bit_count()==4 for l in lines)
assert all(sum((l>>i)&1 for l in lines)==5 for i in range(16))
assert all(sum(((l>>i)&1) and ((l>>j)&1) for l in lines)==1
           for i in range(16) for j in range(i+1,16))

states=[b for b in range(1<<16) if all(b&l not in (0,l) for l in lines)]
assert len(states)==120
assert Counter(b.bit_count() for b in states)=={8:120}
S=set(states)
constructed=set()
for direction in range(5):
    for ell in (1,2,3):
        for affine in range(8):
            bits=0
            for x in range(4):
                for y in range(4):
                    if direction==0: s,t=x,y
                    else: s,t=y^times(direction-1,x),x
                    val=((s&1) & ((s>>1)&1))
                    val ^= ((ell&t).bit_count()&1)
                    val ^= (affine&1) ^ (((affine>>1)&1)*(s&1)) ^ (((affine>>2)&1)*((s>>1)&1))
                    if val: bits|=1<<(4*x+y)
            assert bits in S
            constructed.add(bits)
assert constructed==S
# Verify directly the ten nondegenerate polar forms used in the proof.
def quadratic(direction, v):
    x,y=divmod(v,4)
    s=x if direction==0 else y^times(direction-1,x)
    return (s&1)&((s>>1)&1)
def binary_rank(rows):
    rank=0
    for bit in range(4):
        pivot=next((k for k in range(rank,4) if rows[k]>>bit&1),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        for k in range(4):
            if k!=rank and (rows[k]>>bit&1):rows[k]^=rows[rank]
        rank+=1
    return rank
basis=(1,2,4,8)
for d in range(5):
    for e in range(d+1,5):
        q=lambda v: quadratic(d,v)^quadratic(e,v)
        form=[sum((q(basis[i]^basis[j])^q(basis[i])^q(basis[j])^q(0))<<j
                  for j in range(4)) for i in range(4)]
        assert binary_rank(form)==4
class_of={}
for b in states:
    full=[d for d in range(5) if all((b&l).bit_count()==2
                                     for l in lines[4*d:4*d+4])]
    assert len(full)==1
    class_of[b]=full[0]
assert Counter(class_of.values())=={d:24 for d in range(5)}

pairs=Counter()
for i,a in enumerate(states):
    for b in states[i+1:]:
        pairs[(class_of[a]==class_of[b],(a^b).bit_count())]+=1
assert pairs=={(True,8):1320,(True,16):60,(False,6):2880,(False,10):2880},pairs

adj={a:[b for b in states if (a^b).bit_count()==6] for a in states}
assert all(len(adj[a])==48 for a in states)
assert all(Counter(class_of[b] for b in adj[a]) ==
           {d:12 for d in range(5) if d!=class_of[a]} for a in states)
distance_class=Counter(); common=Counter()
for a in states:
    dist={a:0};todo=deque([a])
    while todo:
        v=todo.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w]=dist[v]+1;todo.append(w)
    assert len(dist)==120
    assert Counter(dist.values())=={0:1,1:48,2:70,3:1}
    assert {b for b,d in dist.items() if d==3}=={a^0xffff}
    for b in states:
        distance_class[((a^b).bit_count(),dist[b])]+=1
        if a!=b:
            common[((a^b).bit_count(),len(set(adj[a])&set(adj[b])))] +=1
assert distance_class=={(0,0):120,(6,1):5760,(8,2):2640,(10,2):5760,(16,3):120},distance_class
assert common=={(6,22):5760,(8,24):2640,(10,14):5760,(16,0):120},common

# Under exactly eight simultaneous recolourings, each of the five balanced
# directions is a cocktail-party graph on 24 vertices.
for d in range(5):
    group=[a for a in states if class_of[a]==d]
    for a in group:
        nbr={b for b in group if (a^b).bit_count()==8}
        assert nbr==set(group)-{a,a^0xffff}
assert all((a^b).bit_count()!=8 for a in states for b in states
           if class_of[a]!=class_of[b])
print('SUCCESS: 120 splittings, five balanced-direction classes of 24, 6-flip:')
print('2880 edges, degree 48, spheres (1,48,70,1), diameter 3,')
print('unique complement antipode; 8-flip: five K24-minus-matching components.')
print('Common 6-flip neighbour counts by Hamming separation:',
      {6:22,8:24,10:14,16:0})
