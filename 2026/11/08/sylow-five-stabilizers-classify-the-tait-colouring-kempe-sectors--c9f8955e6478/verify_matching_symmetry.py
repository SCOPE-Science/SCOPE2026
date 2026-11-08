"""Exact finite certificate for syntheme-incidence Tait-colouring sectors.
Independent state construction by perfect matchings; Python 3 standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

D = tuple(combinations(range(6),2))
dindex = {d:i for i,d in enumerate(D)}

def partitions(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for b in xs[1:]:
        for tail in partitions(tuple(x for x in xs[1:] if x!=b)):
            yield ((a,b),) + tail

S = sorted(tuple(sorted(dindex[e] for e in p)) for p in partitions(tuple(range(6))))
sindex = {s:i for i,s in enumerate(S)}
inc = tuple(tuple(j for j,t in enumerate(S) if i in t) for i in range(15))
assert len(D) == len(S) == 15 and all(len(row)==3 for row in inc)
E = tuple((i,j) for i in range(15) for j in inc[i])
edge_index = {e:k for k,e in enumerate(E)}
FULL = (1<<45)-1

# Perfect matchings: exact-cover assignment of synthemes to duads.
matchings = []
def assign(d, occupied, edge_bits):
    if d == 15:
        matchings.append(edge_bits)
        return
    for s in inc[d]:
        if occupied & (1<<s): continue
        assign(d+1, occupied|(1<<s), edge_bits | (1<<edge_index[d,s]))
assign(0,0,0)
assert len(matchings)==288 and len(set(matchings))==288
matching_set = set(matchings)

# Unlabelled edge-colourings are partitions into three perfect matchings.
factorizations=set()
for i,a in enumerate(matchings):
    for b in matchings[i+1:]:
        if a&b: continue
        c=FULL^(a|b)
        if c in matching_set:
            factorizations.add(tuple(sorted((a,b,c))))
factors=sorted(factorizations)
assert len(factors)==144

adjacent = [set() for _ in factors]
findex={x:i for i,x in enumerate(factors)}
length_patterns=Counter()
for i,F in enumerate(factors):
    for j,k in combinations(range(3),2):
        a,b=F[j],F[k]
        union = a | b
        # Build 2-regular graph on all 30 vertices, decomposed independently.
        neighbors=[[] for _ in range(30)]
        for e,(d,s) in enumerate(E):
            if (union>>e)&1:
                neighbors[d].append((15+s,e))
                neighbors[15+s].append((d,e))
        assert all(len(v)==2 for v in neighbors)
        unseen=set(range(30));components=[]
        while unseen:
            seed=min(unseen);queue=[seed];vset={seed};edge_cycle=0
            while queue:
                u=queue.pop()
                for v,e in neighbors[u]:
                    edge_cycle |= 1<<e
                    if v not in vset:vset.add(v);queue.append(v)
            unseen -= vset
            components.append((len(vset),edge_cycle))
        pattern=tuple(sorted(sz for sz,_ in components))
        length_patterns[pattern]+=1
        for _,mask in components:
            A= a^mask
            B= b^mask
            updated=list(F)
            updated[j]=A;updated[k]=B
            result=tuple(sorted(updated))
            assert result in findex
            if result != F: adjacent[i].add(findex[result])
assert length_patterns=={(30,):144,(10,20):288}
assert all(len(n)==2 for n in adjacent)
assert all(i in adjacent[j] for j,N in enumerate(adjacent) for i in N)

# The incidence automorphisms induced by permutations of the original six points.
perms=list(permutations(range(6)))
transforms=[]
for p in perms:
    dmap=tuple(dindex[tuple(sorted((p[a],p[b])))] for a,b in D)
    smap=tuple(sindex[tuple(sorted(dmap[i] for i in s))] for s in S)
    emap=tuple(edge_index[dmap[d],smap[s]] for d,s in E)
    transforms.append(emap)

def mask_image(mask,emap):
    result=0
    while mask:
        low=mask&-mask
        i=low.bit_length()-1
        result |= 1<<emap[i]
        mask -= low
    return result

def image(F,emap):
    return tuple(sorted(mask_image(m,emap) for m in F))

# A single S6 orbit, and a unique stabilizing subgroup of order 5 per factorization.
seed_orbit={image(factors[0],tr) for tr in transforms}
assert seed_orbit==factorizations and len(seed_orbit)==144
stabilizers=[]
for F in factors:
    st=frozenset(i for i,tr in enumerate(transforms) if image(F,tr)==F)
    assert len(st)==5
    stabilizers.append(st)
assert len(set(stabilizers))==36
counts=Counter(stabilizers)
assert set(counts.values())=={4}

# Every nontrivial permutation in every stabilizer has a 5-cycle and a fixed point.
def cycle_sizes(p):
    unseen=set(range(6)); sizes=[]
    while unseen:
        x=min(unseen);z=x;c=0
        while True:
            unseen.remove(z); c+=1;z=p[z]
            if z==x:break
        sizes.append(c)
    return tuple(sorted(sizes))
for st in set(stabilizers):
    assert Counter(cycle_sizes(perms[i]) for i in st)=={(1,1,1,1,1,1):1,(1,5):4}
# Flip invariance and connectivity on each of the 36 four-element stabilizer fibres.
for i,js in enumerate(adjacent):
    assert all(stabilizers[i]==stabilizers[j] for j in js)
for st, count in counts.items():
    group={i for i,s in enumerate(stabilizers) if s==st}
    assert len(group)==4
    assert all(len(adjacent[i]&group)==2 for i in group)
    assert all(adjacent[i] <= group for i in group)
    # A simple 2-regular graph on four vertices must be a cycle.

# Symmetry of components: all 36 stabilizers are conjugate, S6 transitive.
assert {stabilizers[findex[image(factors[0],tr)]] for tr in transforms} == set(stabilizers)
assert len(set(stabilizers)) == 6*24//4
print('MATCHINGS_288_FACTORIZATIONS_144_PASS')
print('SINGLE_S6_ORBIT_144_STABILIZER_C5_PASS')
print('36_DISTINCT_SYLOW5_SUBGROUPS_FOUR_FACTORIZATIONS_EACH_PASS')
print('EACH_QUOTIENT_C4_AND_KEMPE_STABILIZER_INVARIANT_PASS')
print('TWOFACTOR_PATTERNS_30_AND_10_20_PASS')
