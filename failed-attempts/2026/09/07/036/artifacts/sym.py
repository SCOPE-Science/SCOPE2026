"""Symmetry reduction for S4 pairs. Stdlib only."""
import itertools

def reverse(p): return tuple(reversed(p))
def complement(p):
    k=len(p); return tuple(k+1-x for x in p)
def inverse(p):
    k=len(p); inv=[0]*k
    for i,v in enumerate(p): inv[v-1]=i+1
    return tuple(inv)

def orbit_of_perm(p):
    seen=set([p]); stack=[p]
    while stack:
        cur=stack.pop()
        for f in (reverse,complement,inverse):
            nxt=f(cur)
            if nxt not in seen:
                seen.add(nxt); stack.append(nxt)
    return seen

def canonical_pair(p,q):
    cur_set=set([(p,q)])
    frontier=[(p,q)]
    seen_unordered=set([tuple(sorted((p,q)))])
    while frontier:
        a,b=frontier.pop()
        for f in (reverse,complement,inverse):
            na,nb=f(a),f(b)
            key=tuple(sorted((na,nb)))
            if key not in seen_unordered:
                seen_unordered.add(key)
                cur_set.add((na,nb)); frontier.append((na,nb))
    cands=[tuple(sorted(pair)) for pair in cur_set]
    return min(cands)

if __name__=="__main__":
    S4=list(itertools.permutations([1,2,3,4]))
    print("S4 size",len(S4))
    orbits=[]
    seen=set()
    for p in S4:
        if p in seen: continue
        o=orbit_of_perm(p)
        orbits.append(o); seen|=o
    print("single-pattern orbits:",len(orbits),sorted([len(o) for o in orbits]))
    for o in sorted([sorted(x) for x in orbits]):
        print(o)
    raw=[(S4[i],S4[j]) for i in range(24) for j in range(i+1,24)]
    print("raw pairs",len(raw))
    rep_map={}
    for (p,q) in raw:
        c=canonical_pair(p,q)
        rep_map.setdefault(c,[]).append((p,q))
    print("distinct pair reps:",len(rep_map))
    from collections import Counter
    print(Counter(len(v) for v in rep_map.values()))
    reps=sorted(rep_map.keys())
    for r in reps:
        print(r,"orbit size",len(rep_map[r]))
    print("target1 canon:",canonical_pair((1,3,4,2),(2,1,4,3)))
    print("target2 canon:",canonical_pair((3,1,4,2),(2,3,4,1)))
    print("le2a:",canonical_pair((1,3,4,2),(3,1,2,4)))
    print("le2b:",canonical_pair((1,2,4,3),(2,1,3,4)))
