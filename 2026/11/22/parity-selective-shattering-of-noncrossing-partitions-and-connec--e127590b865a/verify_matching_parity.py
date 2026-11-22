"""Independent finite checks of parity-refined noncrossing matching shattering.
All enumerations use exact integers; no external packages required.
"""
from itertools import combinations, product
from collections import Counter

def restricted_growth(n):
    v = [0] * n
    def rec(i, maxlabel):
        if i == n:
            yield tuple(v)
        else:
            for a in range(maxlabel+2):
                v[i] = a
                yield from rec(i+1, max(maxlabel,a))
    yield from rec(1,0)

def noncrossing(p):
    n = len(p)
    for a,b,c,d in combinations(range(n), 4):
        if p[a] == p[c] and p[b] == p[d] and p[a] != p[b]:
            return False
    return True

def all_matchings(v):
    if not v:
        yield ()
        return
    a = v[0]
    for i in range(1,len(v)):
        b = v[i]
        rem = v[1:i] + v[i+1:]
        for other in all_matchings(rem):
            yield ((a,b),) + other

def crosses(e,f):
    a,b=e; c,d=f
    return (a<c<b<d) or (c<a<d<b)

def intersection_connected(matching):
    if len(matching)<=1:
        return True
    seen={0}; q=[0]
    for i in q:
        for j in range(len(matching)):
            if j not in seen and crosses(matching[i],matching[j]):
                seen.add(j);q.append(j)
    return len(seen)==len(matching)

def faces_matching(p,match):
    # All equality traces observed on the fixed coordinate matching.
    return {tuple(int(p[a] == p[b]) for a,b in match)}

def check_matching(m):
    n=2*m
    allp=[p for p in restricted_growth(n) if noncrossing(p)]
    classes={par:[p for p in allp if (max(p)+1)%2==par] for par in (0,1)}
    counters=Counter()
    for mat in all_matchings(tuple(range(n))):
        conn=intersection_connected(mat)
        counters['matching_total']+=1
        counters['connected']+=int(conn)
        for parity in (0,1):
            observed=set()
            for p in classes[parity]:
                observed.update(faces_matching(p,mat))
            shattered=len(observed)==1<<m
            predicted=(parity==1 or not conn)
            assert shattered==predicted, (m,mat,parity,shattered,predicted)
            counters['shattered_'+str(parity)]+=int(shattered)
    count={'n':n,'Catalan':len(allp),'odd_blocks':len(classes[1]),
           'even_blocks':len(classes[0]), **counters}
    print(count,flush=True)
    return count

def check_first_distinction():
    # The rank-parity stratification on six points has 66 concepts on
    # each side, yet their complete three-query VC counts differ by 4.
    n=6
    ps=[p for p in restricted_growth(n) if noncrossing(p)]
    es=[p for p in ps if (max(p)+1)%2==0]
    os=[p for p in ps if (max(p)+1)%2==1]
    assert len(es)==len(os)==66
    qs=list(combinations(range(n),2))
    e3=o3=0
    for supp in combinations(qs,3):
        e3+=len({tuple(int(p[a]==p[b]) for a,b in supp) for p in es})==8
        o3+=len({tuple(int(p[a]==p[b]) for a,b in supp) for p in os})==8
    assert (e3,o3)==(371,375), (e3,o3)
    print({'n6_three_query_even':e3,'n6_three_query_odd':o3})

if __name__ == '__main__':
    outputs=[check_matching(m) for m in (2,3,4)]
    assert [(x['matching_total'],x['connected'],x['shattered_0'],x['shattered_1']) for x in outputs]==[(3,1,2,3),(15,4,11,15),(105,27,78,105)]
    check_first_distinction()
    print('MATCHING_PARITY_PROOF_FINITE_CHECKS_PASS')
