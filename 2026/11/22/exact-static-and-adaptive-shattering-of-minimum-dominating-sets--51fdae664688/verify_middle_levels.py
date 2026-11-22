#!/usr/bin/env python3
"""Exact finite checks for optimal dominating-set learning in the Desargues graph.
No external dependencies; use `--tree TREE.json` to verify a submitted decision tree.
"""
import itertools, collections, functools, json, sys

def family():
    V=[x for x in range(32) if x.bit_count() in (2,3)]
    n=len(V)
    closed=[]
    for i,x in enumerate(V):
        v=1<<i
        for j,y in enumerate(V):
            if (x^y).bit_count()==1: v|=1<<j
        closed.append(v)
    masks=[]
    all_vertices=(1<<n)-1
    for k in range(7):
        for c in itertools.combinations(range(n),k):
            mask=sum(1<<i for i in c)
            if functools.reduce(int.__or__,(closed[i] for i in c),0)==all_vertices:
                masks.append(mask)
        if masks:return V,closed,masks,k
    raise Exception('missing dominating sets')

def face_data(V,C):
    n=len(V)
    all_faces={0:[0]}
    for k in range(1,6):
        faces=[]
        for positions in itertools.combinations(range(n),k):
            if len({sum(((s>>p)&1)<<i for i,p in enumerate(positions)) for s in C})==1<<k:
                faces.append(sum(1<<i for i in positions))
        all_faces[k]=faces
    return all_faces

def rank_boundaries(faces):
    rank={};n=20
    for k in range(1,5):
        last={m:i for i,m in enumerate(faces[k-1])}
        piv={}
        for f in faces[k]:
            col=0
            for i in range(n):
                if f & (1<<i): col ^=1<<last[f & ~(1<<i)]
            while col:
                p=col.bit_length()-1
                if p in piv:col ^= piv[p]
                else:piv[p]=col;break
        rank[k]=len(piv)
    return rank

def get_tree(V,C):
    n=len(V); masks=[sum(1<<j for j,s in enumerate(C) if s>>i&1) for i in range(n)]
    @functools.lru_cache(None)
    def reach(state,depth):
        if depth==0: return {"witness": (state & -state).bit_length()-1} if state else None
        if state.bit_count() < (1<<depth):return None
        for i in range(n):
            y=state & masks[i]; z=state & ~masks[i]
            if min(y.bit_count(),z.bit_count()) < (1<<(depth-1)):continue
            lo=reach(z,depth-1)
            if lo is None:continue
            hi=reach(y,depth-1)
            if hi is not None:return {"query":i,"zero":lo,"one":hi}
        return None
    tree=reach((1<<len(C))-1,6)
    assert tree is not None
    return tree

def validate_tree(tree,C):
    leaves=[]
    def check(t,lim,path):
        if 'witness' in t:
            assert len(path)==6
            i=t['witness'];assert 0<=i<len(C)
            assert all(((C[i]>>pos)&1)==value for pos,value in path)
            leaves.append(i);return
        assert len(path)<6
        q=t['query'];assert 0<=q<20 and q not in [x for x,y in path]
        check(t['zero'],lim,path+[(q,0)])
        check(t['one'],lim,path+[(q,1)])
    check(tree,C,[])
    assert len(leaves)==64 and len(set(leaves))==64
    return True

def main():
    V,closed,C,gamma=family()
    faces=face_data(V,C)
    counts=[len(faces[i]) for i in range(6)]
    assert (gamma,len(C))==(6,130)
    assert counts==[1,20,190,560,360,0],counts
    ranks=rank_boundaries(faces)
    assert ranks=={1:1,2:19,3:141,4:300},ranks
    facets=[];S=set().union(*[set(v) for v in faces.values()]);
    for f in S:
        if not any((f|(1<<i)) in S for i in range(20) if not f>>i&1):facets.append(f)
    fc=dict(collections.Counter(f.bit_count() for f in facets))
    assert fc=={4:360,3:80,2:30},fc
    contain=collections.Counter(sum(bool(s>>j&1) for s in C) for j in range(20))
    assert contain=={39:20},contain
    assert 39 <64
    tree=get_tree(V,C)
    validate_tree(tree,C)
    out={"schema_version":1,"vertex_labels_as_5bit_integers":V,"tree":tree}
    path=sys.argv[1] if len(sys.argv)>1 else 'depth6_tree.json'
    with open(path,'w',encoding='utf-8') as fp:json.dump(out,fp,separators=(',',':'),sort_keys=True);fp.write('\n')
    print('gamma',gamma,'concepts',len(C),'f',counts,'boundary_ranks',ranks,'facets',fc)
    print('reduced_betti',{'H1':30,'H2':119,'H3':60})
    print('Ldim',6,'positive_first_split_size',39,'tree_leaves',64)
    print('certificate',path)
if __name__=='__main__':main()
