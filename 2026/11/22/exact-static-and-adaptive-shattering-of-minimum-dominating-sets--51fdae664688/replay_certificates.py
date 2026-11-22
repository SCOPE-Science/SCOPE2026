#!/usr/bin/env python3
"""Replay explicit geometric and adaptive certificates for optimal domination.
Standalone Python standard library only; no data other than accompanying JSON files.
"""
import json, itertools, sys
from pathlib import Path

def main(folder):
    base=Path(folder)
    geo=json.loads((base/'vertex_isomorphism.json').read_text())
    V=geo['two_three_subset_order']
    iso=geo['middle_levels_index_to_GP103']
    assert len(V)==20 and len(set(V))==20
    assert all(x.bit_count() in (2,3) for x in V)
    assert sorted(iso)==list(range(20))
    E1={(i,j) for i in range(20) for j in range(i+1,20) if (V[i]^V[j]).bit_count()==1}
    GP=set()
    for i in range(10):
        for a,b in ((i,(i+1)%10),(i,i+10),(i+10,10+(i+3)%10)):
            GP.add(tuple(sorted((a,b))))
    E2={tuple(sorted((iso[i],iso[j]))) for i,j in E1}
    assert GP==E2 and len(GP)==30
    N=[1<<i for i in range(20)]
    for i,j in E1:N[i]|=1<<j;N[j]|=1<<i
    C=[]
    for k in range(7):
        for s in itertools.combinations(range(20),k):
            mask=sum(1<<i for i in s)
            cover=0
            for i in s: cover|=N[i]
            if cover==(1<<20)-1:C.append(mask)
        if C:
            assert k==6 and len(C)==130
            break
    treejson=json.loads((base/'depth6_tree.json').read_text())
    assert treejson['schema_version']==1 and treejson['vertex_labels_as_5bit_integers']==V
    leaves=[]
    def walk(t,questions,answers):
        if 'witness' in t:
            assert set(t)=={'witness'} and len(questions)==6
            i=t['witness'];assert 0<=i<len(C)
            assert all(((C[i]>>q)&1)==ans for q,ans in zip(questions,answers))
            leaves.append(i);return
        assert set(t)=={'query','zero','one'}
        q=t['query']; assert 0<=q<20 and q not in questions
        walk(t['zero'],questions+[q],answers+[0])
        walk(t['one'],questions+[q],answers+[1])
    walk(treejson['tree'],[],[])
    assert len(leaves)==64 and len(set(leaves))==64
    print('CERTIFICATE REPLAY PASS: explicit graph isomorphism, 130 minimal dominating sets, 64 distinct depth-six leaf witnesses')
if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent)
