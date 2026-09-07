#!/usr/bin/env python3
"""Verify symmetry canonicalization + extremal lemma + generic checker agreement."""
import itertools

def all_syms(p):
    # p tuple of 0..k-1 ranks; dihedral group of square: reverse, complement, inverse
    # generate group of 8
    n=len(p)
    def rev(q): return q[::-1]
    def comp(q): return tuple(n-1-x for x in q)
    def inv(q):
        r=[0]*n
        for i,v in enumerate(q): r[v]=i
        return tuple(r)
    seen=set(); stack=[tuple(p)]
    while stack:
        q=stack.pop()
        if q in seen: continue
        seen.add(q)
        stack.append(rev(q)); stack.append(comp(q)); stack.append(inv(q))
    return seen

# 24 patterns length 4
perms=list(itertools.permutations(range(4)))
orbits=[]
seen=set()
for p in perms:
    if p in seen: continue
    o=all_syms(p)
    orbits.append(sorted(o))
    seen|=o
print(f"single-pattern orbits: {len(orbits)}")
for o in sorted(orbits, key=lambda x:x[0]):
    print(len(o), o[0])
assert len(orbits)==7, "expected 7 orbits"

# pair types: unordered pairs of orbits with rep choices -> count distinct under simultaneous symmetry?
# Count orbits of group G (size 8) acting diagonally on unordered pattern pairs {p,q}, p<=q lex?
# Use Burnside / direct enumeration: all C(24+1,2)=300 unordered pairs (with repetition), quotient by G.
pairs=set()
for i,a in enumerate(perms):
    for b in perms[i:]:
        pairs.add((a,b))
print(f"unordered pairs (with rep): {len(pairs)}")
# group elements as functions; build 8 maps explicitly
def maps(n=4):
    def rev(q): return q[::-1]
    def comp(q): return tuple(n-1-x for x in q)
    def inv(q):
        r=[0]*n
        for i,v in enumerate(q): r[v]=i
        return tuple(r)
    # generate group closure on functions
    import collections
    ids=tuple(range(n))  # not a pattern but ok
    funcs=[]
    # brute: all compositions of generators
    gens=[rev,comp,inv]
    seen_f={}
    def apply(f,q): return f(q)
    # represent group elements by their action on all 24 perms (tuple of images)
    def compose(f,g):
        return lambda q, f=f,g=g: f(g(q))
    cur=[lambda q: q]
    seen_s=set()
    elems=[]
    # BFS
    sigs=set()
    queue=[lambda q: q]
    # simpler: enumerate images by BFS on a single generic object? group may not act freely.
    # Instead enumerate distinct action-signatures by BFS over function composition
    funcs=[lambda q: q]
    sigs.add(tuple(sorted([ (p, funcs[0](p)) for p in perms ])) if False else None)
    # Easier: BFS building set of functions via closure, comparing by action table
    tables=set()
    table_list=[]
    def table(f): return tuple(f(p) for p in perms)
    tables.add(table(lambda q:q)); table_list.append(lambda q:q)
    queue=[lambda q:q]
    while queue:
        f=queue.pop()
        for g in gens:
            h=lambda q,f=f,g=g: g(f(q))
            t=table(h)
            if t not in tables:
                tables.add(t); table_list.append(h); queue.append(h)
    print(f"group size: {len(table_list)}")
    return table_list

G=maps()
# orbits on unordered pairs
seenp=set(); norb=0; reps=[]
for (a,b) in pairs:
    if (a,b) in seenp: continue
    norb+=1
    orb=set()
    for g in G:
        x,y=g(a),g(b)
        if x<=y: orb.add((x,y))
        else: orb.add((y,x))
    seenp|=orb
    reps.append((a,b))
print(f"pair-type orbits (with repetition): {norb}")
assert norb==63, f"expected 63 with repetition got {norb}"
# distinct unordered pairs exclude diagonal (p,p): 63-7 = 56
print("distinct unordered pair types: 63-7 = 56 OK")

# check A and B are in distinct orbits and fix reps
A=( (0,1,2,3),(0,2,3,1) )
B=( (3,1,2,0),(3,0,1,2) )
def canon(a,b):
    if a>b: a,b=b,a
    best=None
    for g in G:
        x,y=g(a),g(b)
        if x>y: x,y=y,x
        if best is None or (x,y)<best: best=(x,y)
    return best
print("canon A:",canon(*A),"canon B:",canon(*B))
assert canon(*A)!=canon(*B), "A and B must be symmetry-distinct"
print("A,B symmetry-distinct OK")

# extremal lemma check
def rank4(a,b,c,d):
    s=sorted((a,b,c,d)); r={v:i for i,v in enumerate(s)}
    return (r[a],r[b],r[c],r[d])
FA={(0,1,2,3),(0,2,3,1)}; FB={(3,1,2,0),(3,0,1,2)}
for vals in itertools.permutations(range(4)):
    a,b,c,d=vals
    r=rank4(a,b,c,d)
    inA = r in FA
    lemmaA = (a==min(vals) and ((b<c<d) or (d<b<c)))
    assert inA==lemmaA, (vals,r,inA,lemmaA)
    inB = r in FB
    lemmaB = (a==max(vals) and ((b<c<d) or (d<b<c)))
    assert inB==lemmaB, (vals,r,inB,lemmaB)
print("extremal lemma verified over all 24 rank tuples OK")
