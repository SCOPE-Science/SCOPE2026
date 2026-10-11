from itertools import permutations, product

# Fano plane as nonzero vectors in F_2^3; block iff x+y+z=0.
pts = [i for i in range(1,8)]
def add(a,b): return a ^ b
blocks = {tuple(sorted((a,b,add(a,b)))) for a in pts for b in pts if a<b and add(a,b) not in (a,b,0)}

def is_auto(p):
    mp={pts[i]:p[i] for i in range(7)}
    return all(tuple(sorted(mp[x] for x in B)) in blocks for B in blocks)

autos=[p for p in permutations(pts) if is_auto(p)]
assert len(autos)==168

def orbit_partition(k):
    tuples=list(product(pts, repeat=k))
    idx={t:i for i,t in enumerate(tuples)}
    parent=list(range(len(tuples)))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for p in autos:
        mp={pts[i]:p[i] for i in range(7)}
        for t in tuples:
            union(idx[t],idx[tuple(mp[x] for x in t)])
    return tuples,[find(i) for i in range(len(tuples))]

def closure_size(k):
    tuples,orb=orbit_partition(k)
    idx={t:i for i,t in enumerate(tuples)}
    good=0
    for p in permutations(pts):
        mp={pts[i]:p[i] for i in range(7)}
        ok=True
        for i,t in enumerate(tuples):
            u=tuple(mp[x] for x in t)
            if orb[idx[u]]!=orb[i]:
                ok=False; break
        good += ok
    return good

sizes=[closure_size(k) for k in (1,2,3)]
assert sizes==[5040,5040,168], sizes
print('VERIFY_OK', sizes)
