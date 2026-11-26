#!/usr/bin/env python3
from itertools import combinations, permutations, product
from hashlib import sha256
from collections import Counter

ALPH=(0,1,2)
V=tuple(product(ALPH, repeat=3))
IDX={v:i for i,v in enumerate(V)}

def separated(a,b,c):
    return any(len({a[r],b[r],c[r]})==3 for r in range(3))

def is_phf(S):
    return all(separated(V[a],V[b],V[c]) for a,b,c in combinations(S,3))

def maxima():
    c7=[]
    for S in combinations(range(27),7):
        if is_phf(S): c7.append(S)
    c6=[]
    for S in combinations(range(27),6):
        if is_phf(S): c6.append(S)
    return c7,c6

def structure(S):
    pos={x:i for i,x in enumerate(S)}
    edges=[]
    row_edges=[]
    for r in range(3):
        cnt=Counter(V[x][r] for x in S)
        assert sorted(cnt.values())==[2,2,2]
        rr=[]
        for s in ALPH:
            pair=tuple(sorted(pos[x] for x in S if V[x][r]==s))
            assert len(pair)==2
            rr.append(pair); edges.append(pair)
        row_edges.append(tuple(sorted(rr)))
    E=set(edges)
    assert len(E)==9
    adj={i:set() for i in range(6)}
    for a,b in E: adj[a].add(b);adj[b].add(a)
    assert all(len(adj[i])==3 for i in range(6))
    color={0:0}; stack=[0]
    while stack:
        u=stack.pop()
        for w in adj[u]:
            if w in color: assert color[w]!=color[u]
            else: color[w]=1-color[u]; stack.append(w)
    sides=tuple(sorted((tuple(sorted(i for i,c in color.items() if c==0)),tuple(sorted(i for i,c in color.items() if c==1)))))
    assert [len(x) for x in sides]==[3,3]
    return tuple(row_edges),sides

def transform(S,rp,sps):
    out=[]
    for x in S:
        a=V[x]
        b=tuple(sps[j][a[rp[j]]] for j in range(3))
        out.append(IDX[b])
    return tuple(sorted(out))

def main():
    c7,c6=maxima()
    assert len(c7)==0
    assert len(c6)==36
    structs=[structure(S) for S in c6]
    rep=c6[0]
    perms=list(permutations(ALPH))
    orbit=set(); stab=0; G=0
    for rp in permutations(range(3)):
        for sps in product(perms, repeat=3):
            G+=1
            T=transform(rep,rp,sps)
            orbit.add(T)
            if T==rep: stab+=1
    assert G==1296
    assert orbit==set(c6)
    assert stab==36
    # Count ordered arrays by ordering six distinct columns.
    ordered=len(c6)*720
    assert ordered==25920
    # Independent combinatorial count from labeled K_3,3 one-factorizations.
    # 10 bipartitions; 2 one-factorizations per K_3,3; 3! row assignments; (3!)^3 symbol assignments.
    structural_count=10*2*6*(6**3)
    assert structural_count==ordered
    rows=[]
    for S in c6:
        rows.append(','.join(''.join(map(str,V[x])) for x in S))
    census='\n'.join(rows)+'\n'
    digest=sha256(census.encode()).hexdigest()
    rwords=[''.join(map(str,V[x])) for x in rep]
    print('VERIFY_OK')
    print('maximum=6')
    print('size7=0')
    print('unordered_literal_maxima=36')
    print('ordered_arrays=25920')
    print('natural_group=1296')
    print('orbits=1')
    print('orbit_size=36')
    print('stabilizer=36')
    print('representative='+';'.join(rwords))
    print('representative_bipartition='+'|'.join(','.join(map(str,x)) for x in structs[0][1]))
    print('census_sha256='+digest)

if __name__=='__main__': main()
