"""Exact, standalone balanced-cut and swap-barrier certificate for middle levels Q_5[2,3]."""
from itertools import combinations
from collections import Counter, deque

base=range(5)
vertices=tuple(combinations(base,2))+tuple(combinations(base,3))
assert len(vertices)==20
edges=tuple((i,j) for i,u in enumerate(vertices) for j,v in enumerate(vertices) if len(u)==2 and len(v)==3 and set(u)<=set(v))
assert len(edges)==30 and all(sum(i in e for e in edges)==3 for i in range(20))
full=(1<<20)-1
# First certificate: a complete 2^10 table over all choices of 2-sets.
trips=tuple(combinations(base,3))
pairs=tuple(combinations(base,2))
max_internal=[-1]*11
witnesses=[[] for _ in range(11)]
for mask in range(1<<10):
    r=mask.bit_count()
    degrees=sorted((sum(bool(mask&(1<<j)) and set(e)<=set(T) for j,e in enumerate(pairs)) for T in trips),reverse=True)
    value=sum(degrees[:10-r])
    if value>max_internal[r]:max_internal[r]=value;witnesses[r]=[mask]
    elif value==max_internal[r]:witnesses[r].append(mask)
assert max_internal==[0,3,6,9,12,11,12,9,6,3,0]
assert [len(x) for x in witnesses]==[1,10,45,90,5,120,5,90,45,10,1]
print('internal maxima:',max_internal)
print('maximizing 2-set masks:',[len(x) for x in witnesses])

# Second certificate: all 184756 side-labelled balanced vertex subsets, not modulo complements.
cutby={}
spectrum=Counter()
for indices in combinations(range(20),10):
    m=sum(1<<i for i in indices)
    cut=sum(bool(m&(1<<i))!=bool(m&(1<<j)) for i,j in edges)
    cutby[m]=cut
    spectrum[cut]+=1
assert len(cutby)==184756
assert all(v%2==0 for v in spectrum.values())
assert dict(sorted((c,k//2) for c,k in spectrum.items()))=={
    6:5,8:180,10:2646,12:10320,14:22995,16:25950,
    18:20300,20:7926,22:1815,24:210,26:30,30:1}
minimum=[m for m,c in cutby.items() if c==6]
assert len(minimum)==10
coordinate=set()
for a in range(5):
    side=sum(1<<i for i,U in enumerate(vertices) if a in U)
    assert side.bit_count()==10
    coordinate.update((side,side^full))
assert set(minimum)==coordinate
print('unordered spectrum:',dict(sorted((c,k//2) for c,k in spectrum.items())))
print('minimum=6; ten side-labelled minima, five complementary bisections')

# Third certificate: all legal one-in/one-out swaps at each cut budget, including both orientations.
for budget,expected in ((6,Counter({1:10})),(8,Counter({31:10,1:60})),(10,Counter({5650:1,1:12}))):
    active={s for s,c in cutby.items() if c<=budget}
    comps=[]
    while active:
        seed=next(iter(active));active.remove(seed);Q=deque([seed]);n=0;opt=0
        while Q:
            x=Q.popleft();n+=1;opt+=(cutby[x]==6)
            a=x
            while a:
                bit=a&-a;a-=bit
                b=(~x)&full
                while b:
                    bit2=b&-b;b-=bit2
                    y=x^bit^bit2
                    if y in active:
                        active.remove(y);Q.append(y)
        comps.append((n,opt))
    distribution=Counter(c for c,o in comps)
    assert distribution==expected,(budget,distribution,expected)
    assert (max(o for _,o in comps)==10)==(budget==10)
    print('budget',budget,'components',dict(sorted(distribution.items())),'minima-in-largest',max(o for _,o in comps))
print('ALL CHECKS PASSED')
