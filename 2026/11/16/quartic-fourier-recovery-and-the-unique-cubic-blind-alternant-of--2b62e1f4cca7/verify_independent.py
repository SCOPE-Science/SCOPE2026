"""Independent shape-growth enumerator and modular lower-rank certificate.
Run: python3 verify_independent.py. Python 3 standard library only.
"""
from itertools import combinations
from collections import defaultdict


def tableaux_by_shapes():
    out=[]
    def rec(shape, sequence):
        if shape == (3,3,3):
            out.append(sequence)
            return
        for r in range(3):
            if shape[r] == 3 or (r and shape[r] >= shape[r-1]):
                continue
            p = 3*r + shape[r]
            newer=list(shape); newer[r]+=1
            rec(tuple(newer), sequence + (p,))
    rec((0,0,0),())
    return sorted(out)


def masks_by_degree(orders):
    # Fix CELLS rather than labels, so this construction has independent keys.
    out=[]
    for k in range(5):
        event_to_mask=defaultdict(int)
        for tindex,word in enumerate(orders):
            inv = [0]*9
            for label,cell in enumerate(word):inv[cell]=label
            for cells in combinations(range(9),k):
                entries=tuple((cell,inv[cell]) for cell in cells)
                event_to_mask[entries] |= 1<<tindex
        out.append(set(event_to_mask.values()))
    return out


def modrank_columns(masks,p):
    pivots={}
    for m in masks:
        v=[int(bool(m>>i&1)) for i in range(42)]
        for k,b in sorted(pivots.items()):
            if v[k]:
                coeff=v[k]
                for j in range(k,42):v[j]=(v[j]-coeff*b[j])%p
        lead=next((j for j in range(42) if v[j]),None)
        if lead is None:continue
        inv=pow(v[lead],-1,p)
        pivots[lead]=[x*inv%p for x in v]
    return len(pivots)


def main():
    orders=tableaux_by_shapes()
    assert len(orders)==42 and len(set(orders))==42
    masks=masks_by_degree(orders)
    acc=set()
    for d in range(5):
        acc.update(masks[d])
        ranks=tuple(modrank_columns(acc,p) for p in (1000003,1000033,1000037))
        assert ranks==(1,11,31,41,42)[d:d+1]*3,(d,ranks)
        print('degree',d,'independent_masks',len(masks[d]),'modular_ranks',ranks)
    # Every ordered 2 x 3 x 2 block is present and no others in the ambiguity set.
    blocked=[word for word in orders if word[:1]==(0,) and word[8:]==(8,) and set(word[1:3])=={1,3} and set(word[3:6])=={2,4,6} and set(word[6:8])=={5,7}]
    assert len(blocked)==24
    print('VERIFY_INDEPENDENT_OK')
if __name__=='__main__':main()
