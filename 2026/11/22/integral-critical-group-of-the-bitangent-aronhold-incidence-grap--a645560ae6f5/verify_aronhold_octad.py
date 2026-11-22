"""Exact finite verification of the Aronhold heptad graph and Frobenius spectra.
Uses only the Python standard library. Run: python3 verify_aronhold_octad.py.
"""
from itertools import combinations, permutations
from collections import Counter
import json

N=8
EDGES=list(combinations(range(N),2))
EMASK=[(1<<i)|(1<<j) for i,j in EDGES]
PAIR_INDEX={e:i for i,e in enumerate(EDGES)}

# Odd theta characteristics are the edges relative to the even Cayley-octad theta.
# A triple of odd thetas is azygetic iff its XOR mask has weight 0 or 4.
TRIPLE_OK=set()
for a,b,c in combinations(range(28),3):
    if (EMASK[a]^EMASK[b]^EMASK[c]).bit_count() in (0,4):
        TRIPLE_OK.add((a,b,c))

def enumerate_heptads():
    out=[]
    def grow(chosen,start):
        if len(chosen)==7:
            out.append(tuple(chosen))
            return
        for e in range(start,28):
            if all(tuple(sorted((i,j,e))) in TRIPLE_OK for i,j in combinations(chosen,2)):
                grow(chosen+[e],e+1)
    grow([],0)
    return out

def graph_family():
    H=set()
    for center in range(8):
        star7=tuple(sorted(PAIR_INDEX[tuple(sorted((center,x)))] for x in range(8) if x!=center))
        H.add(star7)
        for tri in combinations((x for x in range(8) if x!=center),3):
            others=[x for x in range(8) if x!=center and x not in tri]
            edges=[tuple(sorted((center,x))) for x in others]+list(combinations(tri,2))
            H.add(tuple(sorted(PAIR_INDEX[e] for e in edges)))
    assert len(H)==288
    return H

def partns(n,maxval=None):
    if maxval is None:maxval=n
    if n==0:
        yield ()
    else:
        for x in range(min(n,maxval),0,-1):
            for rest in partns(n-x,x):
                yield (x,)+rest

def perm_of_cycle_type(part):
    p=list(range(8)); j=0
    for l in part:
        for k in range(l):p[j+k]=j+(k+1)%l
        j+=l
    return p

def orbit_counts(items,perm):
    itemset=set(items)
    action=[PAIR_INDEX[tuple(sorted((perm[a],perm[b])))] for a,b in EDGES]
    def act(h): return tuple(sorted(action[e] for e in h))
    left=set(items); counts=Counter()
    while left:
        h=next(iter(left)); cur=h; length=0
        while True:
            assert cur in itemset
            left.discard(cur);length+=1
            cur=act(cur)
            if cur==h:break
            assert length<=840
        counts[length]+=1
    return dict(sorted(counts.items()))

def rational_count_formula(part):
    r=part.count(1);u=part.count(2);v=part.count(3)
    def choose(n,k):
        from math import comb
        return comb(n,k) if n>=k else 0
    return r*(1+choose(r-1,3)+(r-1)*u+v)

def main():
    direct=set(enumerate_heptads())
    model=graph_family()
    assert len(direct)==288 and direct==model
    def degree_class(h):
        deg=[0]*8
        for e in h:
            a,b=EDGES[e];deg[a]+=1;deg[b]+=1
        return tuple(sorted(deg))
    assert Counter(degree_class(h) for h in direct)=={
       (1,1,1,1,1,1,1,7):8,
       (1,1,1,1,2,2,2,4):280}
    tbl=[]
    for part in partns(8):
        p=perm_of_cycle_type(part)
        cs=orbit_counts(model,p)
        assert sum(s*k for s,k in cs.items())==288
        fixed=cs.get(1,0)
        assert fixed==rational_count_formula(part),(part,fixed,rational_count_formula(part))
        stars=orbit_counts([h for h in model if degree_class(h)[-1]==7],p)
        mixed=orbit_counts([h for h in model if degree_class(h)[-1]==4],p)
        assert sum(k*s for s,k in stars.items())==8
        assert sum(k*s for s,k in mixed.items())==280
        tbl.append({'cycle_type':list(part),'orbit_multiplicities':{str(x):y for x,y in cs.items()},'rational_heptads':fixed,'star_orbits':{str(x):y for x,y in stars.items()},'star_triangle_orbits':{str(x):y for x,y in mixed.items()}})
    assert len(tbl)==22
    # Independent action check using all 40320 octad permutations for stabilizer
    # and orbit sizes of two representatives; forced by 8 and 280 canonical shapes.
    one_star=next(h for h in model if degree_class(h)[-1]==7)
    one_mixed=next(h for h in model if degree_class(h)[-1]==4)
    orbit_star=set();orbit_mixed=set()
    for p in permutations(range(8)):
        action=[PAIR_INDEX[tuple(sorted((p[a],p[b])))] for a,b in EDGES]
        orbit_star.add(tuple(sorted(action[e] for e in one_star)))
        orbit_mixed.add(tuple(sorted(action[e] for e in one_mixed)))
    assert (len(orbit_star),len(orbit_mixed))==(8,280)
    assert orbit_star|orbit_mixed==model and not orbit_star&orbit_mixed
    with open('FROBENIUS_TABLE.json','w',encoding='utf-8') as f:
        json.dump({'description':'Aronhold heptad Frobenius cycle spectra for a stable regular Cayley octad','total_heptads':288,'partition_count':len(tbl),'rows':tbl},f,ensure_ascii=False,indent=2)
        f.write('\n')
    print('ARONHOLD_OCTAD_288_AND_22_FROBENIUS_TYPES_VERIFIED_OK')
    for row in tbl:print(''.join(map(str,row['cycle_type'])),'fixed',row['rational_heptads'],'orbits',row['orbit_multiplicities'])
if __name__=='__main__':main()
