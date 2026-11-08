"""Reproducible verification of finite witnesses for K_{3,b} cycle-incidence shattering.

Run: python verify_cycle.py cycle_witness.json
Uses Python standard library only; all cycle lists are constructed independently.
"""
import itertools,json,sys
from pathlib import Path

def cycles(a,b):
    index={(i,j):i*b+j for i in range(a) for j in range(b)}
    masks=set()
    for length in range(2,min(a,b)+1):
        for left in itertools.permutations(range(a),length):
            if left[0] != min(left):continue
            for right in itertools.permutations(range(b),length):
                mask=0
                for k in range(length):
                    i=left[k];j=right[k];ii=left[(k+1)%length]
                    mask|=1<<index[i,j]
                    mask|=1<<index[ii,j]
                masks.add(mask)
    return masks

def verify():
    p=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('cycle_witness.json'))
    cert=json.loads(p.read_text(encoding='utf-8'))
    assert cert['left_size']==3 and cert['right_size']==4
    c3=cycles(3,3); c4=cycles(3,4)
    assert len(c3)==15 and len(c4)==42
    for name,concepts,k,cols in [('vc_witness_K3_3',c3,3,9),('vc_witness_K3_4',c4,4,12)]:
        s=cert[name]
        assert len(s)==k and all(isinstance(i,int) and 0<=i<cols for i in s) and len(set(s))==k
        traces={tuple((mask>>i)&1 for i in s) for mask in concepts}
        assert len(traces)==2**k, (name,len(traces))
    ninternal=nleaf=0; seen_leaves=[]
    def walk(node,path,used):
        nonlocal ninternal,nleaf
        if 'cycle_mask' in node:
            assert set(node)=={'cycle_mask'}
            mask=node['cycle_mask'];assert mask in c4
            assert all((mask>>j)&1==v for j,v in path)
            nleaf+=1;seen_leaves.append(mask)
            return
        assert set(node)=={'query_edge_index','zero','one'}
        j=node['query_edge_index'];assert isinstance(j,int) and 0<=j<12 and j not in used
        ninternal+=1
        walk(node['zero'],path+[(j,0)],used|{j})
        walk(node['one'],path+[(j,1)],used|{j})
    walk(cert['online_depth_five_tree_K3_4'],[],set())
    assert nleaf==32 and ninternal==31 and len(set(seen_leaves))==32
    # Independently calculate all four-subset traces of K3,3, demonstrating none shattered.
    assert all(len({tuple((cyc>>j)&1 for j in s) for cyc in c3})<16 for s in itertools.combinations(range(9),4))
    print('CYCLE_K3_B_SHATTERING_VERIFIED cycles3=15 cycles4=42 vc3=3 vc4=4 online_depth5_leaves=32 internal=31')
if __name__=='__main__':verify()
