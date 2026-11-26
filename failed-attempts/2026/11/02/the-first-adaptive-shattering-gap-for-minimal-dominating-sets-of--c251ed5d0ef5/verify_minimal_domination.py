#!/usr/bin/env python3
"""Finite certificate of vertex-query shattering for minimal dominating sets on paths.
Independent private-neighbor and deletion definitions; exact VC and adaptive ranks.
"""
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent

def neighbor_masks(n, edges):
    nb = [1 << i for i in range(n)]
    for a,b in edges:
        nb[a] |= 1 << b
        nb[b] |= 1 << a
    return nb

def is_dominating(mask, neighborhoods):
    return all(mask & nb for nb in neighborhoods)

def is_minimal_via_deletion(mask, neighborhoods):
    return is_dominating(mask, neighborhoods) and all(
        not is_dominating(mask ^ (1<<i), neighborhoods)
        for i in range(len(neighborhoods)) if mask & (1<<i)
    )

def is_minimal_via_private_neighbors(mask, neighborhoods):
    if not is_dominating(mask, neighborhoods):
        return False
    for i in range(len(neighborhoods)):
        if mask & (1<<i):
            if not any((mask & nb) == (1<<i) for nb in neighborhoods):
                return False
    return True

def concepts_of_path(n):
    nb = neighbor_masks(n, [(i,i+1) for i in range(n-1)])
    from_deletion = [s for s in range(1<<n) if is_minimal_via_deletion(s, nb)]
    from_private = [s for s in range(1<<n) if is_minimal_via_private_neighbors(s, nb)]
    assert from_deletion == from_private
    return from_deletion

def vc_and_support(concepts, n):
    best=0; witness=0
    for support in range(1<<n):
        k = support.bit_count()
        if k <= best: continue
        traces={c&support for c in concepts}
        if len(traces) == (1<<k):
            best=k; witness=support
    return best,witness

def ranks_and_tree(concepts,n):
    qbits=[sum(1<<j for j,c in enumerate(concepts) if c & (1<<i)) for i in range(n)]
    @lru_cache(None)
    def rank(state):
        if state == 0 or state & (state-1) == 0:
            return 0
        ans=0
        for q in qbits:
            yes=state&q; no=state&~q
            if yes and no:
                ans=max(ans, 1+min(rank(yes),rank(no)))
        return ans
    initial=(1<<len(concepts))-1
    d=rank(initial)
    def tree(state,depth):
        if depth==0:
            j=(state & -state).bit_length()-1
            return {'witness_mask': concepts[j]}
        for i,q in enumerate(qbits):
            yes=state&q; no=state&~q
            if yes and no and rank(yes)>=depth-1 and rank(no)>=depth-1:
                return {'query_vertex':i,'zero':tree(no,depth-1),'one':tree(yes,depth-1)}
        raise AssertionError('missing branch')
    return d,tree(initial,d),rank.cache_info().currsize

def check_tree(obj, concepts,n,depth,history=()):
    if depth==0:
        c=obj['witness_mask']
        assert c in concepts
        assert all(bool(c & (1<<i)) == bool(a) for i,a in history)
        return [c]
    i=obj['query_vertex']
    assert 0<=i<n and all(j!=i for j,a in history)
    left=check_tree(obj['zero'],concepts,n,depth-1,history+((i,0),))
    right=check_tree(obj['one'],concepts,n,depth-1,history+((i,1),))
    return left+right

def main():
    rows=[]; certs={}
    expected_v=[0,0,1,1,2,2,2,3,3,4,4,4]
    expected_l=[0,0,1,1,2,2,2,3,3,4,4,5]
    for n in range(1,12):
        concepts=concepts_of_path(n)
        vc, support=vc_and_support(concepts,n)
        ld, tree, states=ranks_and_tree(concepts,n)
        leaves=check_tree(tree,concepts,n,ld)
        assert len(leaves)==(1<<ld) and len(set(leaves))==len(leaves)
        assert vc==expected_v[n] and ld==expected_l[n],(n,vc,ld)
        rows.append({'n':n,'number_of_minimal_dominating_sets':len(concepts),'VCdim':vc,'Ldim':ld,'memoized_states':states,'max_shattered_support':[i for i in range(n) if support&(1<<i)]})
        certs[str(n)]={'n':n,'dimension':ld,'tree':tree}
    assert rows[-1]['number_of_minimal_dominating_sets']==36
    assert rows[-1]['VCdim']==4 and rows[-1]['Ldim']==5
    # Independently enumerate all five-element supports: every one fails shattering.
    cs=concepts_of_path(11)
    five=0
    for supp in combinations(range(11),5):
        mask=sum(1<<i for i in supp)
        assert len({c&mask for c in cs})<32
        five+=1
    assert five==462
    # Explicit sample of all 36^2 local selections on two copies joined at support vertices.
    n=22
    edges=[(i,i+1) for i in range(10)]+[(i,i+1) for i in range(11,21)]+[(1,12)]
    nb=neighbor_masks(n,edges)
    for a in cs:
        for b in cs:
            assert is_minimal_via_deletion(a|(b<<11),nb)
    result={'method':'complete exhaustive path enumeration and exact finite recursive Littlestone rank',
            'rows':rows,'all_five_supports_checked':five,
            'connected_two_copy_pairs_checked':len(cs)**2,
            'certified_11_path_depth':5,'certified_11_path_leaves':32,
            'status':'MINIMAL_DOMINATING_PATH_FIRST_GAP_ALL_CHECKS_PASS'}
    (OUT/'path_census.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    (OUT/'adaptive_trees.json').write_text(json.dumps(certs,indent=2,sort_keys=True)+'\n')
    print('N PATH_CONCEPTS VC LDim STATES')
    for r in rows:
        print(r['n'],r['number_of_minimal_dominating_sets'],r['VCdim'],r['Ldim'],r['memoized_states'])
    print('FIVE_SUPPORTS',five,'JOINED_PAIRS',len(cs)**2)
    print(result['status'])

if __name__=='__main__':main()
