"""Exhaustive finite certificate builder for betweenness-query shattering of paths.
Runs standalone using Python 3 standard library. The output JSON contains local
adaptive trees and static trace witnesses. No network or external packages.
"""
from functools import lru_cache
from itertools import combinations, permutations
import json
from pathlib import Path


def families(n):
    paths = [p for p in permutations(range(n)) if n < 2 or p[0] < p[-1]]
    if n == 1: paths = [(0,)]
    if n == 2: paths = [(0,1)]
    queries = []
    for s in combinations(range(n),3):
        a,b,c=s
        queries.extend(((a,b,c),(a,c,b),(b,a,c)))
    def ans(p,q):
        index={v:i for i,v in enumerate(p)}
        a,b,c=q
        return min(index[a],index[c]) < index[b] < max(index[a],index[c])
    masks=[]
    for q in queries:
        masks.append(sum((1 << i) for i,p in enumerate(paths) if ans(p,q)))
    return paths,queries,masks


def build(n):
    paths,queries,masks = families(n)
    full = (1 << len(paths))-1
    @lru_cache(None)
    def ld(M):
        if M.bit_count()<=1: return 0
        out=0
        for mask in masks:
            a=M&mask;b=M&~mask
            if a and b and min(a.bit_count(),b.bit_count())>=2**out:
                out=max(out,1+min(ld(a),ld(b)))
        return out
    d=ld(full)
    def rec(M,k):
        if not k:
            idx=(M&-M).bit_length()-1
            return {'witness':list(paths[idx])}
        for j,mask in enumerate(masks):
            M0=M&~mask;M1=M&mask
            if M0 and M1 and ld(M0)>=k-1 and ld(M1)>=k-1:
                return {'query':list(queries[j]),'zero':rec(M0,k-1),'one':rec(M1,k-1)}
        raise RuntimeError('missing tree')
    tree=rec(full,d)
    v=0; vc_q=[]; vc_w={"":list(paths[0])}
    # first VC witnesses for each size
    for k in range(1,len(queries)+1):
        if 2**k>len(paths): break
        found=False
        for combo in combinations(range(len(queries)),k):
            seen={}
            for p in paths:
                signature=''.join(str(int(min(p.index(q[0]),p.index(q[2]))<p.index(q[1])<max(p.index(q[0]),p.index(q[2])))) for q in (queries[j] for j in combo))
                seen.setdefault(signature,list(p))
                if len(seen)==2**k:break
            if len(seen)==2**k:
                v=k;vc_q=[list(queries[j]) for j in combo];vc_w=seen;found=True;break
        if not found:break
    print('n',n,'hypotheses',len(paths),'VC',v,'Ldim',d,'rec_states',ld.cache_info().currsize, flush=True)
    return {'n':n,'number_of_unoriented_labeled_paths':len(paths),
            'VCdim':v,'Ldim':d,'vc_queries':vc_q,'vc_witnesses':vc_w,
            'littlestone_tree':tree}

if __name__=='__main__':
    content=[build(n) for n in range(1,6)]
    p=Path(__file__).with_name('finite_betweenness_certificate.json')
    p.write_text(json.dumps({'format':'betweenness_path_concept_cert_v1','cases':content},sort_keys=True,separators=(',',':'))+'\n')
    print('wrote',p, 'bytes',p.stat().st_size)
