"""Standalone verification of exhaustive complete permutation comparator mistake trees.

Usage: python check_order_certificates.py order_certificates.json
"""
import itertools,json,math,sys
from pathlib import Path

def verify(cert):
    n=cert['n'];d=cert['depth']
    assert isinstance(n,int) and 2<=n<=6
    perms=set(itertools.permutations(range(n)))
    assert len(perms)==cert['hypothesis_count']==math.factorial(n)
    assert d==math.factorial(n).bit_length()-1
    leaves=[];internal=0
    def traverse(node,position,remaining):
        nonlocal internal
        if remaining==0:
            assert set(node)=={'witness'}
            p=tuple(node['witness']);assert p in perms
            for a,b,value in position:
                assert (p.index(a)<p.index(b)) == bool(value),('bad-leaf',p,a,b,value)
            leaves.append(p);return
        assert set(node)=={'query','zero','one'},node
        ab=node['query'];assert len(ab)==2
        a,b=ab; assert isinstance(a,int) and isinstance(b,int) and 0<=a<b<n
        internal+=1
        traverse(node['zero'],position+[(a,b,0)],remaining-1)
        traverse(node['one'],position+[(a,b,1)],remaining-1)
    traverse(cert['tree'],[],d)
    assert len(leaves)==1<<d
    assert len(set(leaves))==1<<d
    assert internal==(1<<d)-1
    # The cardinality bound rules out depth d+1 because any full tree
    # of depth d+1 requires at least 2**(d+1) distinct hypotheses.
    assert len(perms)<(1<<(d+1))
    print(f'n={n} VC={n-1} Ldim={d} full_tree_leaves={len(leaves)} distinct_witnesses={len(set(leaves))} internal_nodes={internal} hypotheses={len(perms)}')

if __name__=='__main__':
    target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('order_certificates.json')
    obj=json.loads(target.read_text())
    assert len(obj['certificates'])==5
    for cert in obj['certificates']:verify(cert)
    print('ALL_PERMUTATION_COMPARATOR_CERTIFICATES_PASS')
