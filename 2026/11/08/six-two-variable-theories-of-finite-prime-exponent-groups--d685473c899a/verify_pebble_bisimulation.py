#!/usr/bin/env python3
"""Check closure of atomic two-pebble types under all pebble replacements.

This finite certificate checks samples; the general theorem uses the symbolic proof
that every nonidentity anchor has exactly the same available relative types.
"""
from verify_prime_exponent import class_model, pair_profile

CASES=[
 ['C2',(2,1,False)],['E2',(2,2,False)],
 ['C3',(3,1,False)],['E3',(3,2,False)],['H3',(3,1,True)],
 ['C5',(5,1,False)],['E5',(5,2,False)],['H5',(5,1,True)],
 ['C7',(7,1,False)],['C11',(11,1,False)],['H7',(7,1,True)]
]

def signature(g):
    items,unit,mul=g
    # By conjugation/scalar automorphism homogeneity is not assumed in this computation.
    prof={(x,y):pair_profile(g,x,y) for x in items for y in items}
    alltypes=set(prof.values())
    transitions={}
    for x in items:
        row=frozenset(prof[x,z] for z in items)
        for y in items:
            key=prof[x,y]
            col=frozenset(prof[z,y] for z in items)
            sig=(row,col)
            if key in transitions:
                assert transitions[key]==sig, 'Atomic type is not bisimulation-stable'
            else:transitions[key]=sig
    assert set(transitions)==alltypes
    return transitions

def main():
    outs={name:signature(class_model(*args)) for name,args in CASES}
    blocks=[['C2'],['E2'],['C3'],['E3','H3'],['C5'],['E5','H5','C7','C11','H7']]
    for block in blocks:
        assert all(outs[name]==outs[block[0]] for name in block),block
    for a in range(len(blocks)):
        for b in range(a+1,len(blocks)):
            assert set(outs[blocks[a][0]]) != set(outs[blocks[b][0]])
    print('Two-pebble transition certificates: PASS')
    print('Eleven sampled groups; all ordered pairs and legal one-pebble replacements covered.')
    for block in blocks:
        print('class',','.join(block),'tuple types',len(outs[block[0]]))
    print('Six pairwise distinct sentence classes; no mismatches.')

if __name__=='__main__':main()
