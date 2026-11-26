#!/usr/bin/env python3
from itertools import combinations, permutations
from math import gcd

classes = {
    "A":(1,0),
    "B":(2,0),
    "C":(0,1),
    "D":(0,2),
    "E":(1,1),
    "F":(1,2),
    "G":(2,1),
}
names=list(classes)

def incomparable(x,y):
    le=all(a<=b for a,b in zip(x,y))
    ge=all(a>=b for a,b in zip(x,y))
    return not le and not ge

Q={x:set() for x in names}
for x,y in combinations(names,2):
    if incomparable(classes[x],classes[y]):
        Q[x].add(y); Q[y].add(x)

expected_edges={
    tuple(sorted(e)) for e in [
        ("A","C"),("A","D"),
        ("B","C"),("B","D"),("B","E"),("B","F"),
        ("D","E"),("D","G"),
        ("F","G"),
    ]
}
actual_edges={tuple(sorted((x,y))) for x in names for y in Q[x] if x<y}
assert actual_edges==expected_edges,(actual_edges,expected_edges)

def is_qaut(perm):
    mp=dict(zip(names,perm))
    return all(((y in Q[x]) == (mp[y] in Q[mp[x]]))
               for x,y in combinations(names,2))
qauts=[dict(zip(names,p)) for p in permutations(names) if is_qaut(p)]
assert len(qauts)==4
print("quotient automorphisms:", [
    tuple(m[x] for x in names) for m in qauts
])

# No false or true twins in the quotient.
for x,y in combinations(names,2):
    assert Q[x] != Q[y]
    assert (Q[x]|{x}) != (Q[y]|{y})

def weights(p,q):
    return {
        "A":(p-1)*q*(q-1),
        "B":q*(q-1),
        "C":p*(p-1)*(q-1),
        "D":p*(p-1),
        "E":(p-1)*(q-1),
        "F":p-1,
        "G":q-1,
    }

def weighted_qauts(p,q):
    w=weights(p,q)
    return [m for m in qauts if all(w[x]==w[m[x]] for x in names)]

def vertex_count(p,q):
    n=p*p*q*q
    return n - p*q*(p-1)*(q-1) - 1

def direct_graph(p,q):
    n=p*p*q*q
    V=[x for x in range(1,n) if gcd(x,n)!=1]
    N={x:set() for x in V}
    for x,y in combinations(V,2):
        dx,dy=gcd(x,n),gcd(y,n)
        if dx%dy!=0 and dy%dx!=0:
            N[x].add(y); N[y].add(x)
    return n,V,N

def class_of_gcd(d,p,q):
    i=0
    while d%p==0:
        i+=1; d//=p
    j=0
    while d%q==0:
        j+=1; d//=q
    assert d==1
    for k,v in classes.items():
        if v==(i,j): return k
    raise AssertionError((i,j))

def check_direct(p,q):
    n,V,N=direct_graph(p,q)
    by={k:[] for k in names}
    for x in V:
        by[class_of_gcd(gcd(x,n),p,q)].append(x)
    w=weights(p,q)
    assert {k:len(v) for k,v in by.items()}==w
    assert len(V)==vertex_count(p,q)==sum(w.values())
    # Each class is independent and has identical external neighborhood.
    for k,vs in by.items():
        for x,y in combinations(vs,2):
            assert y not in N[x]
            assert N[x]==N[y]
    # Quotient adjacency exactly Q.
    for a,b in combinations(names,2):
        observed=all(y in N[x] for x in by[a] for y in by[b])
        assert observed == (b in Q[a]),(p,q,a,b)
    # Different quotient classes are not full-graph twins.
    reps={k:by[k][0] for k in names}
    for a,b in combinations(names,2):
        x,y=reps[a],reps[b]
        assert N[x] != N[y]
        assert (N[x]|{x}) != (N[y]|{y})
    return len(V)

for p,q in [(2,3),(2,5),(3,5),(5,3),(3,7),(5,7)]:
    wa=weighted_qauts(p,q)
    assert len(wa)==1 and all(wa[0][x]==x for x in names)
    w=weights(p,q)
    M=max(w.values())
    assert M==(p-1)*(q-1)*max(p,q)
    N=vertex_count(p,q)
    det=N-7
    assert det==sum(v-1 for v in w.values())
    print(f"p={p}, q={q}: N={N}, Det={det}, D={M}, weighted quotient rigid")

for p,q in [(2,3),(2,5),(3,5)]:
    nv=check_direct(p,q)
    print(f"Z/({p*p*q*q})Z direct graph OK: {nv} vertices")

print("VERIFY_OK")
