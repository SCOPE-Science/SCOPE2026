"""Construct exact full mistake-tree witnesses for comparator hypotheses."""
import itertools,functools,json,math,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def make(n):
    permutations=list(itertools.permutations(range(n)))
    edges=list(itertools.combinations(range(n),2))
    masks=[]
    for a,b in edges:
        masks.append(sum(1<<j for j,p in enumerate(permutations) if p.index(a)<p.index(b)))
    all_h=(1<<len(permutations))-1
    @functools.lru_cache(None)
    def depth(h):
        if h.bit_count()<2:return 0
        best=0
        for m in masks:
            yes=h&m; no=h^yes
            if yes and no:
                level=1+min(depth(yes),depth(no))
                if level>best:best=level
        return best
    d=depth(all_h)
    assert d==len(permutations).bit_length()-1
    def tree(h,k):
        if k==0:
            index=(h & -h).bit_length()-1
            return {'witness':list(permutations[index])}
        for edge,m in zip(edges,masks):
            yes=h&m;no=h^yes
            if yes and no and depth(yes)>=k-1 and depth(no)>=k-1:
                return {'query':list(edge),'zero':tree(no,k-1),'one':tree(yes,k-1)}
        raise AssertionError(('tree-not-found',n,k,h.bit_count()))
    cert={'n':n,'depth':d,'hypothesis_count':len(permutations),'tree':tree(all_h,d)}
    return cert,depth.cache_info().currsize

if __name__=='__main__':
    start=time.time()
    certificates=[]
    for n in (2,3,4,5,6):
        cert,states=make(n)
        certificates.append(cert)
        print(f'n={n} dim={cert["depth"]} perms={cert["hypothesis_count"]} states={states}',flush=True)
    target=ROOT/'order_certificates.json'
    target.write_text(json.dumps({'encoding':'Per node, query [a,b] means a precedes b, one = true. Every leaf stores an exact permutation witness.','certificates':certificates},separators=(',',':'),ensure_ascii=False)+'\n')
    print('CERTIFICATE_BYTES',target.stat().st_size,'ELAPSED',round(time.time()-start,2))
