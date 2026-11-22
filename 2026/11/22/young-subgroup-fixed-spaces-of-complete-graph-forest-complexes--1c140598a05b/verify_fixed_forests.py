"""Independent exhaustive checks for Young-subgroup fixed points of forest complexes.

Requires only Python 3 standard library. The general theorem is proved symbolically;
these computations test the finite orbit/face description, not an infinite range.
"""
from itertools import combinations, product, permutations
from math import factorial


def independent_forest(n, edges):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for u,v in edges:
        a,b=find(u),find(v)
        if a==b: return False
        parent[a]=b
    return True


def orbit_edges(n, block_sizes, m):
    blocks=[]; p=0
    for k in block_sizes:
        blocks.append(tuple(range(p,p+k)))
        p+=k
    assert p+m==n
    singles=tuple(range(p,n))
    group=list(product(*[list(permutations(b)) for b in blocks]))
    actions=[]
    for gs in group:
        sigma=list(range(n))
        for block,per in zip(blocks,gs):
            for x,y in zip(block,per): sigma[x]=y
        actions.append(tuple(sigma))
    all_e=set(combinations(range(n),2))
    orbits=[]
    while all_e:
        e=min(all_e)
        orbit={tuple(sorted((g[e[0]],g[e[1]]))) for g in actions}
        assert orbit<=all_e
        orbits.append(frozenset(orbit));all_e-=orbit
    return blocks,singles,orbits


def expected_allowed(blocks,singles):
    common={frozenset({tuple(sorted((a,b)))}) for a,b in combinations(singles,2)}
    from_block=[]
    for block in blocks:
        candidates=[]
        if len(block)==2:
            candidates.append(frozenset({tuple(sorted(block))}))
        for s in singles:
            candidates.append(frozenset(tuple(sorted((x,s))) for x in block))
        from_block.append(candidates)
    return common,from_block


def run_one(block_sizes,m):
    n=m+sum(block_sizes)
    blocks,singles,orbits=orbit_edges(n,block_sizes,m)
    expected_common,factors=expected_allowed(blocks,singles)
    allowed=[o for o in orbits if independent_forest(n,o)]
    expected=expected_common|set(o for factor in factors for o in factor)
    assert set(allowed)==expected,(block_sizes,m,'vertex orbits')
    if len(allowed)>18: return (n,len(allowed),None)
    # Structural classification gives independent sets as: an ordinary forest on
    # singleton labels, plus at most one orbit from each permutation block.
    for mask in range(1<<len(allowed)):
        selected=[allowed[i] for i in range(len(allowed)) if mask>>i&1]
        merged=set().union(*selected) if selected else set()
        actual=independent_forest(n,merged)
        common_merged=set().union(*(o for o in selected if o in expected_common)) if selected else set()
        presumed=independent_forest(n,common_merged)
        for candidates in factors:
            presumed &= sum(o in selected for o in candidates)<=1
        assert actual==presumed,(block_sizes,m,mask,'faces')
    return n,len(allowed),1<<len(allowed)


def beta(m):
    e=list(combinations(range(m),2))
    s=0
    for bits in range(1<<len(e)):
        selected=[e[i] for i in range(len(e)) if bits>>i&1]
        if independent_forest(m,selected): s+=(-1)**len(selected)
    return (-1)**(m-1)*s


if __name__=='__main__':
    cases=[((2,),3),((3,),3),((4,),3),((2,2),2),((2,3),2),((3,3),2),((2,2),1),((2,3),1),((3,3),1),((2,2),0),((3,3),0),((2,2),3),((2,3),3),((2,),4)]
    for blocks,m in cases:
        n,v,checks=run_one(blocks,m)
        print('orbit-face',blocks,m,'n',n,'eligible',v,'subsets_checked',checks)
    vals=[beta(m) for m in range(3,7)]
    assert vals[:3]==[1,6,51],vals
    print('beta_m m=3..6:',vals)
    print('VERIFY_OK')
