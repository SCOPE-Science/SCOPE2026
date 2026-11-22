#!/usr/bin/env python3
"""Regenerate the complete decision-tree witness used by verify.py."""
import json
from functools import lru_cache
from verify import colorings,palette_masks
from pathlib import Path
C=list(colorings([2,2,2],5)); masks=palette_masks(C,5); full=(1<<len(C))-1
@lru_cache(maxsize=None)
def find(state,depth):
    if depth==0:return None
    if state.bit_count()<1<<depth:return False
    for v,a,mask in masks:
        yes=state&mask;no=state&~mask
        if yes.bit_count()<1<<(depth-1) or no.bit_count()<1<<(depth-1):continue
        if find(no,depth-1) is not False and find(yes,depth-1) is not False:return (v,a,mask)
    return False
assert find(full,6) is not False

def build(state,d):
    if d==0:
        idx=(state&-state).bit_length()-1
        return {'coloring':list(C[idx])}
    v,a,mask=find(state,d)
    return {'query':[v,a],'zero':build(state&~mask,d-1),'one':build(state&mask,d-1)}
P=Path(__file__).parent/'tree_certificate.json'
P.write_text(json.dumps(build(full,6),separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf-8')
print('tree nodes',2**7-1,'depth',6,'hypotheses',len(C),'file_bytes',P.stat().st_size)
