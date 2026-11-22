#!/usr/bin/env python3
"""Self-contained finite check of independent-domination traces in the Fano Levi graph."""
from itertools import combinations, permutations
from collections import Counter

def objects():
    # Point i is the nonzero vector i+1 in F_2^3.
    lines=sorted({tuple(sorted((a-1,b-1,(a^b)-1)))
                  for a in range(1,8) for b in range(a+1,8)})
    assert len(lines)==7
    return lines

def mask(values):
    x=0
    for v in values:x|=1<<v
    return x

def enumerate_independent_dominating(lines):
    edges=[(p,7+j) for j,L in enumerate(lines) for p in L]
    adj=[0]*14
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    return {s for s in range(1<<14)
            if all(not((s>>u&1) and (s>>v&1)) for u,v in edges)
            and all(s>>v&1 or s&adj[v] for v in range(14))}

def geometric_families(lines):
    # Complete 37-element classification: two full shores;
    # seven point-centered, seven line-centered and 21 pair-centered sets.
    ans={mask(range(7)), mask(range(7,14))}
    for p in range(7):
        ans.add(mask([p]+[7+j for j,L in enumerate(lines) if p not in L]))
    for j,L in enumerate(lines):
        ans.add(mask([7+j]+[p for p in range(7) if p not in L]))
    for p,q in combinations(range(7),2):
        ans.add(mask([p,q]+[7+j for j,L in enumerate(lines) if p not in L and q not in L]))
    assert len(ans)==37
    return ans

def independent(s,lines):
    return all(not((s>>p&1) and (s>>(7+j)&1))
               for j,L in enumerate(lines) for p in L)

def predicted(s,lines):
    if not independent(s,lines):return False
    k=s.bit_count()
    return k<=3 or (k==4 and 0<(s&127).bit_count()<4)

def trace(s,concepts):
    return {m&s for m in concepts}

def symmetry_checks(lines,facet):
    L2id={l:i for i,l in enumerate(lines)}
    automorphisms=[]
    for pi in permutations(range(7)):
        try: lp=tuple(7+L2id[tuple(sorted(pi[p] for p in L))] for L in lines)
        except KeyError:continue
        automorphisms.append(tuple(pi)+lp)
    assert len(automorphisms)==168
    # Polarity: exchange p with its orthogonal F_2^3 line.
    dual=[]
    for p in range(7):
        l=tuple(v for v in range(7) if ((p+1)&(v+1)).bit_count()%2==0)
        dual.append(7+L2id[l])
    dual += [dual.index(7+j) for j in range(7)]
    assert sorted(dual)==list(range(14))
    automorphisms+= [tuple(dual[a] for a in t) for t in automorphisms]
    assert len(set(automorphisms))==336
    def transform(s,pi):return mask(pi[v] for v in range(14) if s>>v&1)
    remain=set(facet);orbits=[]
    while remain:
        s=min(remain)
        orbit={transform(s,pi) for pi in automorphisms}
        assert orbit<=remain
        orbits.append((s.bit_count(),len(orbit)))
        remain-=orbit
    assert sorted(orbits)==[(3,14),(4,21),(4,56)],orbits
    return sorted(orbits)

def main():
    lines=objects()
    brute=enumerate_independent_dominating(lines)
    geo=geometric_families(lines)
    assert brute==geo
    assert Counter(x.bit_count() for x in brute)=={4:21,5:14,7:2}
    count=Counter();shattered=set()
    for s in range(1<<14):
        is_shattered=len(trace(s,brute))==(1<<s.bit_count())
        assert is_shattered==predicted(s,lines),(s,is_shattered)
        if is_shattered:
            shattered.add(s);count[s.bit_count()]+=1
    assert [count[i] for i in range(6)]==[1,14,70,154,77,0]
    facets={s for s in shattered
            if all((s|1<<v) not in shattered for v in range(14) if not s>>v&1)}
    assert Counter(s.bit_count() for s in facets)=={3:14,4:77}
    line_triples={mask(L) for L in lines} | {mask(7+j for j,L in enumerate(lines) if p in L) for p in range(7)}
    assert {s for s in facets if s.bit_count()==3}==line_triples
    orbits=symmetry_checks(lines,facets)
    for support in [(5,6,7,8),(3,4,5,7),(0,1,2)]:
        assert all(any(all((c>>v&1)==(bits>>i&1) for i,v in enumerate(support))
                       for c in geo) for bits in range(1<<len(support)))
    print('HEAWOOD_MIS_SHATTER_PASS 37 concepts; 16384 supports; faces 1,14,70,154,77; facets 14+77; orbits',orbits)

if __name__=='__main__':main()
