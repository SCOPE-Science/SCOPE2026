"""Construct depth-six complete mistake tree for pair-equality from 3+6 partitions."""
from itertools import combinations
from functools import lru_cache
import json
from pathlib import Path

n=9
edges=list(combinations(range(n),2))
hyp=list(combinations(range(n),3))
mask=[sum(1<<i for i,A in enumerate(hyp) if ((u in A)==(v in A))) for u,v in edges]
FULL=(1<<len(hyp))-1

@lru_cache(None)
def dimension(sp):
    best=0
    for j,bit in enumerate(mask):
        pos=sp & bit
        if not pos or pos==sp:continue
        neg=sp^pos
        val=1+min(dimension(pos),dimension(neg))
        if val>best:best=val
    return best

assert dimension(FULL)==6

def witness(sp,d):
    if d==0:
        i=(sp & -sp).bit_length()-1
        return {'witness':list(hyp[i])}
    for j,bit in enumerate(mask):
        pos=sp & bit; neg=sp^pos
        if pos and neg and dimension(pos)>=d-1 and dimension(neg)>=d-1:
            return {'query':list(edges[j]),'no':witness(neg,d-1),'yes':witness(pos,d-1)}
    raise AssertionError((sp,d))

cert={'n':n,'block_size':3,'depth':6,'root':witness(FULL,6)}
p=Path('depth6_tree.json')
p.write_text(json.dumps(cert,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print('DIMENSION',dimension(FULL),'CACHED_STATES',dimension.cache_info().currsize,'CERT_BYTES',p.stat().st_size)
