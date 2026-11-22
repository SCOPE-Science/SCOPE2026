"""Independent projective-incidence verification of the near-maximum classes and swaps for PG(2,3)."""
from itertools import product, combinations
from collections import Counter, defaultdict

def normalized(a,p):
    s=next(x for x in a if x)
    return tuple(x * pow(s,-1,p)%p for x in a)

p=3
vectors=sorted({normalized(a,p) for a in product(range(p),repeat=3) if any(a)})
v=len(vectors)
assert v==13
neighbors=[sum(1<<j for j,l in enumerate(vectors) if sum(x*y for x,y in zip(t,l))%p==0) for t in vectors]
assert all(x.bit_count()==4 for x in neighbors)
# Enumerate all subsets of points of one shore, then all near-maximum independent sets
# by deriving exactly which opposite-shore choices avoid the selected shore.
full=(1<<v)-1
large=set()
for P in range(1<<v):
    forbidden=0
    for i in range(v):
        if P>>i&1:forbidden |= neighbors[i]
    allowed=full ^ forbidden
    # It suffices to consider lines of the largest admissible sizes;
    # smaller choices are included whenever their total size reaches v-1.
    for target in (v-1,v):
        needed=target-P.bit_count()
        if 0<=needed<=allowed.bit_count():
            avail=[j for j in range(v) if allowed>>j&1]
            for J in combinations(avail,needed):
                L=sum(1<<j for j in J)
                large.add((P,L))
assert len(large)==2*v+2,len(large)  # both shores, each minus one vertex
assert {k.bit_count()+t.bit_count() for k,t in large}=={12,13}
assert all(P==0 or L==0 for P,L in large)
# Check all valid one/two member second colour classes by incidence distances.
# Two distinct points or two distinct lines have distance 2; nonincident point-line distance 3.
near=[]
for P,L in large:
    a=P.bit_count()+L.bit_count()
    if a==v:
        # lone 2-colour vertex on opposite shore
        for y in range(2*v):
            if not ( ((P>>y)&1) if y<v else ((L>>(y-v))&1) ):
                near.append((P,L,(y,)))
    if a==v-1:
        for x in range(v):
            for y in range(v):
                if not (P>>x&1) and not (L>>y&1) and not (neighbors[x]>>y&1):
                    near.append((P,L,(x,v+y)))
# only pairs on opposite shores valid.
assert len(near)==2*v*(1+p*p),len(near)
# Enumerate all skeletons and exchange exactly one vertex between classes 1 and 2.
nearset={ (P | (L<<v), sum(1<<x for x in B)) for P,L,B in near }
assert len(nearset)==len(near)
sizes=Counter();edges=0
for A,B in nearset:
    count=0
    for x in range(2*v):
        if (A>>x&1) and not (B>>x&1):
            z=(A^(1<<x),B|(1<<x))
        elif (B>>x&1) and not (A>>x&1):
            z=(A|(1<<x),B^(1<<x))
        else:continue
        if z in nearset:count+=1
    sizes[count]+=1;edges+=count
assert sizes==Counter({1:2*v*p*p,p*p:2*v}),sizes
assert edges//2==2*v*p*p
# Every skeleton belongs to a star determined by its fixed singleton opposite-shore vertex.
print('PG(2,3): points/lines=',v,'near-max independent sets=',len(large),'skeletons=',len(nearset),'degree counts=',dict(sizes),'edges=',edges//2,'stars=',2*v)
