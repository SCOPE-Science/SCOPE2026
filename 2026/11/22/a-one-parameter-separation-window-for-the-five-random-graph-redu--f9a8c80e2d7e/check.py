"""Exact finite binary-edge calculations for five reduct actions.
All masks represent edges on ordered distinct vertices.
"""
from itertools import combinations

def edges(k): return list(combinations(range(k),2))
def mask_cut(k,S):
    return sum((1<<j) for j,(a,b) in enumerate(edges(k)) if bool(S & (1<<a)) != bool(S & (1<<b)))
def span(gens):
    out={0}
    for v in gens: out |= {w^v for w in tuple(out)}
    return out

def translations(kind,k):
    gens=[]
    if kind in ('switch','both'):
        gens += [mask_cut(k,1<<i) for i in range(k)]
    if kind in ('complement','both'):
        gens += [(1<<len(edges(k)))-1]
    return span(gens)

def degree(kind,k):
    if kind == 'graph': return 0
    if kind == 'complement': return int(k>=2)
    if kind == 'switch': return max(k-1,0)
    if kind == 'both': return 0 if k<=1 else (1 if k==2 else k)
    raise ValueError(kind)

def predicted(kind,n,r):
    if kind=='equality': return 1
    return 2**(len(edges(n+r))-len(edges(n))-(degree(kind,n+r)-degree(kind,n)))

def independent_count(kind,n,r):
    if kind=='equality': return 1
    k=n+r
    old_edges=[j for j,(a,b) in enumerate(edges(k)) if a<n and b<n]
    allowed=[h for h in translations(kind,k) if all(not ((h>>j)&1) for j in old_edges)]
    new_edges=[j for j in range(len(edges(k))) if j not in old_edges]
    # A quotient is enumerated independently, rather than assuming dimensions.
    all_patterns=[sum(((a>>t)&1)<<j for t,j in enumerate(new_edges)) for a in range(1<<len(new_edges))]
    remaining=set(all_patterns);count=0
    while remaining:
        x=remaining.pop();count+=1
        remaining.difference_update(x^t for t in allowed)
    return count

if __name__=='__main__':
    groups=('graph','complement','switch','both','equality')
    cases=0
    for k in range(0,6):
        for n in range(k+1):
            r=k-n
            for kind in groups:
                actual=independent_count(kind,n,r)
                expected=predicted(kind,n,r)
                assert actual==expected,(kind,n,r,actual,expected)
                cases+=1
    # Independently verify translation subgroup orders through seven vertices.
    ranks=0
    for k in range(8):
        for kind in groups[:-1]:
            assert len(translations(kind,k))==2**degree(kind,k)
            ranks+=1
    assert [predicted(kind,0,3) for kind in groups]==[8,4,2,1,1]
    assert [predicted(kind,0,4) for kind in groups]==[64,32,8,4,1]
    assert [predicted(kind,1,2) for kind in groups]==[8,4,2,1,1]
    assert [predicted(kind,1,3) for kind in groups]==[64,32,8,4,1]
    for n in range(2,8):
        for r in range(1,9):
            assert predicted('graph',n,r)==predicted('complement',n,r)
    for n in range(3,8):
        for r in range(1,9):
            assert predicted('switch',n,r)==predicted('both',n,r)
    print('FINITE_QUOTIENT_CASES_PASS',cases)
    print('TRANSLATION_RANKS_PASS',ranks)
    print('POINTWISE_SPECTRAL_IDENTITIES_PASS')
    print('ALL_CHECKS_PASS')
