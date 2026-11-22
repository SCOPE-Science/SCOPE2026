#!/usr/bin/env python3
"""Exhaustively classify simultaneous reset lengths for ordered triples of binary three-state complete DFAs."""
from itertools import product
from collections import defaultdict
from hashlib import sha256

TRANS = list(product(range(3), repeat=3))

def action(t, s):
    return sum(1<<j for j in set(t[i] for i in range(3) if s & (1<<i)))

def reset_masks(pair, max_len=7):
    maps = [[action(t,s) for s in range(8)] for t in pair]
    states=[7]
    ans=[]
    for length in range(1,max_len+1):
        states=[maps[c][state] for state in states for c in (0,1)]
        bits=sum((1<<i) for i, s in enumerate(states) if s in (1,2,4))
        ans.append(bits)
    return tuple(ans)

def main():
    classes=defaultdict(list)
    nonsync=0
    for a in TRANS:
        for b in TRANS:
            masks=reset_masks((a,b))
            if masks[-1]==0:
                nonsync+=1
            else:
                classes[masks].append((a,b))
    assert nonsync==180
    signatures=list(classes)
    print('automata', len(TRANS)**2, 'sync',sum(map(len,classes.values())), 'non_sync',nonsync,'reset_types',len(classes))
    print('type_multiplicities', sorted(map(len, classes.values())))
    distribution=[0]*8
    certificate=None
    classes_items=list(classes.items())
    for i,(x,ox) in enumerate(classes_items):
        for j,(y,oy) in enumerate(classes_items):
            for k,(z,oz) in enumerate(classes_items):
                m=next((ell for ell in range(1,8) if x[ell-1] & y[ell-1] & z[ell-1]),None)
                assert m is not None
                distribution[m]+=len(ox)*len(oy)*len(oz)
                if m==7 and certificate is None:certificate=(ox[0],oy[0],oz[0]); badclass=(i,j,k)
    assert sum(distribution)==549**3
    print('ordered_triple_reset_distribution', [(i,v) for i,v in enumerate(distribution) if v]); print('sum',sum(distribution))
    print('sharp_example', certificate, 'class_indices',badclass)
    print('witness_reset_lengths', [next((l for l in range(1,8) if reset_masks(pair)[l-1] & reset_masks(certificate[1])[l-1] & reset_masks(certificate[2])[l-1]),None) for pair in [certificate[0]]])
    for length in range(1,8):
        wbits=(reset_masks(certificate[0])[length-1]& reset_masks(certificate[1])[length-1]&reset_masks(certificate[2])[length-1])
        print('witness_common_length',length,'count',wbits.bit_count(),'first_word',format((wbits&-wbits).bit_length()-1,f'0{length}b') if wbits else '-')
if __name__=='__main__': main()
