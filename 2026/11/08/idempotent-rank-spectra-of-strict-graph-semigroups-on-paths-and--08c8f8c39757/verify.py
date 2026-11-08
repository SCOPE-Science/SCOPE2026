"""Finite checks using distinct constructions for strict graph semigroup idempotents.
Only the Python standard library is required. Run: python verify.py.
"""
from itertools import product, combinations
from math import comb


def graph(kind, n):
    assert kind == 'P' and n >= 1 or kind == 'C' and n >= 3
    edges = [(i, i+1) for i in range(n-1)]
    if kind == 'C':
        edges.append((n-1, 0))
    E = {frozenset(e) for e in edges}
    return E, edges


def predicted(kind, n):
    d = n//2
    ans=[]
    for k in range(d+1):
        if kind == 'P':
            ans.append(comb(2*n-3*k+1,k))
        elif n == 2*k:
            ans.append(4)
        else:
            m=n-2*k
            numerator=n*comb(2*n-3*k-1,k)
            assert numerator%m == 0
            ans.append(numerator//m)
    return tuple(ans)


def directly_enumerated_strict_idempotents(kind, n):
    """Enumerate ALL partial maps, test full simplex pullbacks, then f^2=f."""
    E, edges=graph(kind,n)
    out=[0]*(n//2+1)
    simplices=[{x} for x in range(n)]+[set(e) for e in edges]
    for f in product(range(-1,n),repeat=n):
        if any((f[x] >=0 and (f[f[x]]!=f[x])) for x in range(n)):
            continue
        good=True
        for simplex in simplices:
            inverse=frozenset(x for x in range(n) if f[x] in simplex)
            if inverse and len(inverse)!=2 or (inverse and inverse not in E):
                good=False
                break
        if good:
            rank=len({v for v in f if v>=0})
            out[rank]+=1
    return tuple(out)


def directed_matchings(kind,n):
    """Independent oriented-matching enumeration; no transfer-matrix shortcut."""
    E,edges=graph(kind,n)
    out=[0]*(n//2+1)
    for k in range(n//2+1):
        for match in combinations(edges,k):
            occupied=[v for e in match for v in e]
            if len(set(occupied))!=2*k:continue
            for choice in product((0,1), repeat=k):
                picked=[e[o] for e,o in zip(match,choice)]
                if all(frozenset((u,v)) not in E for u,v in combinations(picked,2)):
                    out[k]+=1
    return tuple(out)


def conflict_edges(kind,n):
    E,edges=graph(kind,n)
    vs=[(i,s) for i in range(len(edges)) for s in (0,1)]
    conflicts=set()
    for a,b in combinations(range(len(vs)),2):
        i,s=vs[a];j,t=vs[b]
        u,v=edges[i]; x,y=edges[j]
        if i==j or len(set((u,v,x,y)))<4 or frozenset((edges[i][s],edges[j][t])) in E:
            conflicts.add(frozenset((a,b)))
    return vs, conflicts


def conflict_polynomial(kind,n):
    vs,conflicts=conflict_edges(kind,n)
    m=len(vs)
    out=[0]*(n//2+1)
    for mask in range(1<<m):
        k=mask.bit_count()
        if k>n//2:continue
        if not any(((mask>>a)&1) and ((mask>>b)&1) for a,b in (tuple(c) for c in conflicts)):
            out[k]+=1
    return tuple(out)


def check_no_claw(kind,n):
    vs,conflicts=conflict_edges(kind,n)
    adj={i:set() for i in range(len(vs))}
    for e in conflicts:
        a,b=tuple(e);adj[a].add(b);adj[b].add(a)
    for v,N in adj.items():
        for a,b,c in combinations(N,3):
            if all(frozenset(e) not in conflicts for e in ((a,b),(a,c),(b,c))):
                raise AssertionError(('claw',kind,n,vs[v],vs[a],vs[b],vs[c]))


def main():
    direct=0;matching=0;confpol=0;claw=0
    for kind in ('P','C'):
        for n in (range(1,6) if kind=='P' else range(3,6)):
            assert directly_enumerated_strict_idempotents(kind,n)==predicted(kind,n),(kind,n,'direct')
            direct+=1
        for n in (range(1,13) if kind=='P' else range(3,13)):
            assert directed_matchings(kind,n)==predicted(kind,n),(kind,n,'matchings')
            matching+=1
        for n in (range(1,9) if kind=='P' else range(3,9)):
            assert conflict_polynomial(kind,n)==predicted(kind,n),(kind,n,'conflict')
            confpol+=1
        for n in (range(1,24) if kind=='P' else range(3,24)):
            check_no_claw(kind,n)
            claw+=1
    print('VERIFY_OK direct_partial_map_cases=%d oriented_matching_cases=%d conflict_polynomial_cases=%d clawfree_cases=%d'%(direct,matching,confpol,claw))
    for kind,n in [('P',6),('P',7),('C',6),('C',7),('C',8)]:
        print('%s%d'%(kind,n),predicted(kind,n))

if __name__ == '__main__':main()
