"""Exact combinatorial verification of tritangent-line-flag Frobenius data.

No external dependencies. Run: python3 verify_tritangent_flags.py
"""
from itertools import permutations, combinations
from collections import Counter
from math import gcd, factorial

U = tuple(range(6))
PAIRS = tuple(combinations(U, 2))

def matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for b in xs[1:]:
        for tail in matchings(tuple(x for x in xs[1:] if x != b)):
            yield tuple(sorted(((a, b),) + tail))

MATS = tuple(matchings(U))
LINES = tuple([('E', i) for i in U] + [('Q', i) for i in U] + [('L', a, b) for a, b in PAIRS])
PLANES = tuple([('A', i, j) for i in U for j in U if i != j] + [('B', mat) for mat in MATS])

def through(t):
    if t[0] == 'A':
        i, j = t[1:]
        return (('E', i), ('Q', j), ('L', *sorted((i, j))))
    return tuple(('L', a, b) for a, b in t[1])

FLAGS = tuple((t, l) for t in PLANES for l in through(t))
assert (len(LINES), len(PLANES), len(FLAGS), len(MATS)) == (27, 45, 135, 15)
assert len(set(LINES)) == 27 and len(set(PLANES)) == 45 and len(set(FLAGS)) == 135

def act(x, p):
    typ = x[0]
    if typ in ('E','Q'):
        return (typ, p[x[1]])
    if typ == 'L':
        return (typ, *sorted((p[x[1]], p[x[2]])))
    if typ == 'A':
        return (typ, p[x[1]], p[x[2]])
    if typ == 'B':
        return (typ, tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in x[1])))
    return (act(x[0],p), act(x[1],p))

def orbit_profile(items, p):
    unseen = set(items)
    counts = Counter()
    while unseen:
        origin = next(iter(unseen))
        cur = origin
        length = 0
        while True:
            assert cur in unseen, ('revisited early', cur)
            unseen.remove(cur)
            length += 1
            cur = act(cur,p)
            if cur == origin:
                break
        counts[length] += 1
    return tuple(sorted(counts.items()))

def cycle_partition(p):
    unseen = set(U)
    lens=[]
    while unseen:
        first=next(iter(unseen));cur=first; n=0
        while cur in unseen:
            unseen.remove(cur);n+=1;cur=p[cur]
        assert cur==first
        lens.append(n)
    return tuple(sorted(lens,reverse=True))

def permutation_for_partition(t):
    p=list(U); offset=0
    for n in t:
        ids=list(range(offset,offset+n))
        for a,b in zip(ids,ids[1:]+ids[:1]):p[a]=b
        offset+=n
    assert offset==6
    return tuple(p)

def invariant_matching_count(sigma, subset):
    if not subset: return 1
    return sum(all(tuple(sorted((sigma[a],sigma[b]))) in m for a,b in m) for m in matchings(tuple(sorted(subset))))

def analytic_fixed(sigma):
    fixed=set(i for i in U if sigma[i]==i)
    fixedpairs=[(a,b) for a,b in PAIRS if set((sigma[a],sigma[b]))==set((a,b))]
    nA=len(fixed)*(len(fixed)-1)
    nB=invariant_matching_count(sigma, U)
    flagsA=3*nA
    flagsB=sum(invariant_matching_count(sigma, set(U)-set(pair)) for pair in fixedpairs)
    return (2*len(fixed)+len(fixedpairs), nA+nB, flagsA+flagsB)

def compose(p,q): return tuple(p[q[i]] for i in U)
def power(p,n):
    result=U
    for _ in range(n): result=compose(p,result)
    return result

def check_cycle_formula(items,p,k):
    profile=dict(orbit_profile(items,p))
    assert sum(c*d for d,c in profile.items()) == len(items)
    for n in range(1,k+1):
        fixed=sum(1 for x in items if act(x,power(p,n))==x)
        expected=sum(d*c for d,c in profile.items() if n%d==0)
        assert fixed==expected

EXPECTED = {
 (6,): ((3,1,6,4), (1,1,2,1,3,2,6,6), (3,3,6,21), (1,0,0)),
 (5,1): ((1,2,5,5), (5,9), (5,27), (0,0,0)),
 (4,2): ((1,1,2,3,4,5), (1,1,2,2,4,10), (1,1,2,5,4,31), (0,1,0)),
 (4,1,1): ((1,5,2,1,4,5), (1,3,2,1,4,10), (1,7,2,2,4,31), (0,1,2)),
 (3,3): ((3,9), (1,3,3,14), (3,45), (3,0,0)),
 (3,2,1): ((1,3,2,3,3,4,6,1), (2,3,3,5,6,4), (2,9,3,15,6,12), (0,0,0)),
 (3,1,1,1): ((1,9,3,6), (1,6,3,13), (1,18,3,39), (0,0,6)),
 (2,2,2): ((1,3,2,12), (1,7,2,19), (1,9,2,63), (0,6,1)),
 (2,2,1,1): ((1,7,2,10), (1,5,2,20), (1,11,2,62), (0,2,3)),
 (2,1,1,1,1): ((1,15,2,6), (1,15,2,15), (1,45,2,45), (0,0,15)),
 (1,1,1,1,1,1): ((1,27), (1,45), (1,135), (0,0,45))
}

def unpack_flat(x): return tuple((x[i],x[i+1]) for i in range(0,len(x),2))

def main():
    class_counts=Counter()
    for p in permutations(U):
        typ=cycle_partition(p); class_counts[typ]+=1
        lines=orbit_profile(LINES,p); planes=orbit_profile(PLANES,p); flags=orbit_profile(FLAGS,p)
        assert lines==unpack_flat(EXPECTED[typ][0]), (typ,lines)
        assert planes==unpack_flat(EXPECTED[typ][1]), (typ,planes)
        assert flags==unpack_flat(EXPECTED[typ][2]), (typ,flags)
        direct=(sum(1 for l in LINES if act(l,p)==l),sum(1 for t in PLANES if act(t,p)==t),sum(1 for f in FLAGS if act(f,p)==f))
        assert direct==analytic_fixed(p), (typ,direct,analytic_fixed(p))
        rational_lines={l for l in LINES if act(l,p)==l}
        hist=Counter(len(rational_lines.intersection(through(t))) for t in PLANES if act(t,p)==t)
        assert (hist[0], hist[1], hist[3])==EXPECTED[typ][3], (typ,hist)
        assert hist[2]==0
    assert sum(class_counts.values())==factorial(6)==720
    assert len(class_counts)==11
    for typ in EXPECTED:
        p=permutation_for_partition(typ)
        k=1
        for c in typ:k=k*c//gcd(k,c)
        for items in (LINES,PLANES,FLAGS): check_cycle_formula(items,p,k)
        print('type',typ,'class_size',class_counts[typ], 'line',dict(orbit_profile(LINES,p)),'plane',dict(orbit_profile(PLANES,p)), 'flag',dict(orbit_profile(FLAGS,p)), 'rational-plane-line-pattern',EXPECTED[typ][3])
    no_line_with_plane=[]
    for typ in EXPECTED:
        p=permutation_for_partition(typ)
        if not orbit_profile(LINES,p)[0][0]==1: # no fixed length-one orbits
            if any(act(t,p)==t for t in PLANES):no_line_with_plane.append(typ)
    assert set(no_line_with_plane)=={(6,),(3,3)}
    print('TRITANGENT_FLAG_FROBENIUS_CLASSIFICATION_VERIFIED_OK')

if __name__=='__main__':main()
