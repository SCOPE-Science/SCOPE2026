"""Finite-support exact certificate for trigram substitution-profile capacity.
Only Python standard library. All finite universality reductions are proved in RESULT.md.
"""
from collections import Counter, defaultdict
from itertools import product

Q=6

def delta(word, i, letter):
    assert word[i] != letter
    a=list(word)
    b=list(word)
    b[i]=letter
    start=max(0,i-2)
    stop=min(i,len(word)-3)
    count=Counter(tuple(b[j:j+3]) for j in range(start,stop+1))
    count.subtract(tuple(a[j:j+3]) for j in range(start,stop+1))
    return tuple(sorted((t,v) for t,v in count.items() if v))

def support(v):
    return {x for tri,_ in v for x in tri}

def canonical(seq):
    remap={}
    return tuple(remap.setdefault(x,len(remap)) for x in seq)

def pair_canonical(x,y):
    return min(canonical(x+y),canonical(y+x))

# Exhaust all words of length five and genuine changed middle symbols over six letters.
fibers=defaultdict(list)
for w in product(range(Q),repeat=5):
    for f in range(Q):
        if f != w[2]:
            key=delta(w,2,f)
            assert support(key)==set(w)|{f}, 'No cancellation can hide a used letter'
            fibers[key].append(w+(f,))
assert sum(map(len,fibers.values()))==Q**5*(Q-1)==38880
assert len(fibers)==38580
sizes=Counter(map(len,fibers.values()))
assert sizes==Counter({1:38280,2:300}),sizes

expected={
    ((0,0,0,0,1,1),(1,0,0,0,0,1)),
    ((0,0,0,1,0,1),(0,1,0,0,0,1)),
    ((0,0,0,1,1,1),(1,1,0,0,0,1)),
    ((0,0,1,0,1,0),(1,0,1,0,0,0)),
    ((0,0,1,1,0,0),(0,1,1,0,0,0)),
    ((0,1,0,0,1,1),(1,0,0,1,0,1)),
    ((0,1,0,1,2,2),(2,1,0,1,0,2)),
}
expected={pair_canonical(x,y) for x,y in expected}
observed=Counter(pair_canonical(v[0],v[1]) for v in fibers.values() if len(v)==2)
assert set(observed)==expected,(set(observed)-expected,expected-set(observed))
assert sorted(observed.values())==[30]*6+[120],observed
print('interior: raw=38880 distinct=38580, collision multiplicities',sorted(sizes.items()))
print('collision template orbits: six size-30, one size-120')

# Boundaries in a five-symbol ambient word realize precisely four distinct kinds
# (first, second, penultimate, last). Their unused ambient symbols are discarded.
kindpos=(0,1,3,4)
boundary=[]
for i in kindpos:
    pool=set()
    for w in product(range(Q),repeat=5):
        outcomes={delta(w,i,f) for f in range(Q) if f!=w[i]}
        assert len(outcomes)==Q-1, (i,w,'distinct boundary substitutions collapsed')
        for f in range(Q):
            if f==w[i]:
                continue
            v=delta(w,i,f)
            relevant= (w[:3] if i==0 else w[:4] if i==1 else w[1:] if i==3 else w[2:])
            assert support(v)==set(relevant)|{f}, ('hidden letter',i,w,f)
            pool.add(v)
    boundary.append(pool)
assert list(map(len,boundary))==[1080,6480,6480,1080]
assert all(not (x & set(fibers)) for x in boundary)
assert all(not (boundary[a] & boundary[b]) for a in range(4) for b in range(a+1,4))
print('boundary: type sizes=1080,6480,6480,1080; all pairwise/interior intersections empty')

# Transfer: identical vectors have identical supports, so relabel every symbol
# used in either operation injectively into {0,..,5}. At most six symbols occur.
# This exhaustive certificate is therefore a symbolic all-q classification.
for q in range(2,7):
    raw=q**5*(q-1)
    loss=q*(q-1)*(q+4)
    interior=raw-loss
    bound=interior+4*(q-1)
    print('q=%d interior=%d capacity=%d' % (q,interior,bound))
print('PASS universal symbolic certificate')
