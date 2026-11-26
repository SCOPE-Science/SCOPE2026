#!/usr/bin/env python3
"""Exact full finite k-cut homotopy census for the Petersen graph (standard library)."""
import itertools, collections, functools, json
VERTICES=tuple(itertools.combinations(range(5),2))
ADJ=tuple(tuple(not bool(set(a)&set(b)) for b in VERTICES) for a in VERTICES)
N=10; ALL=(1<<N)-1

def connected(vertices):
    seen={vertices[0]}; todo=[vertices[0]]
    while todo:
        v=todo.pop()
        for w in vertices:
            if ADJ[v][w] and w not in seen:seen.add(w);todo.append(w)
    return len(seen)==len(vertices)

def face_sets(k):
    disconnected=[tuple(s) for s in itertools.combinations(range(N),k) if not connected(s)]
    facets=[ALL ^ sum(1<<v for v in s) for s in disconnected]
    by_facets=set()
    for f in facets:
        s=f
        while s:by_facets.add(s);s=(s-1)&f
    # Independent exhaustive direct vertex-complement test, not downward closure.
    by_witness=set()
    for s in range(1,1<<N):
        complement=tuple(v for v in range(N) if not (s>>v)&1)
        if len(complement)>=k and any(not connected(x) for x in itertools.combinations(complement,k)):
            by_witness.add(s)
    assert by_facets==by_witness
    return by_facets,len(facets)

@functools.lru_cache(None)
def boundary(f):
    out=[];i=0;remaining=f
    while remaining:
        b=remaining&-remaining
        out.append((f^b,1 if i%2==0 else -1))
        remaining^=b;i+=1
    return tuple(out)

def match(faces,order,root):
    rem=faces.copy();low={};upper={}
    for v in order:
        b=1<<v
        lows=[s for s in rem if s!=root and not s&b and s|b in rem]
        for s in lows:low[s]=s|b;upper[s|b]=s
        rem.difference_update(lows);rem.difference_update((s|b) for s in lows)
    assert len(rem)+2*len(low)==len(faces)
    return rem,low,upper

def acyclic(faces,low):
    indeg={s:0 for s in faces};arrows=0
    for s in faces:
        for g,_ in boundary(s):
            if not g:continue
            arrows+=1
            if low.get(g)==s:indeg[s]+=1
            else:indeg[g]+=1
    todo=[s for s,d in indeg.items() if d==0];visited=0
    while todo:
        s=todo.pop();visited+=1
        if s in low:
            t=low[s];indeg[t]-=1
            if not indeg[t]:todo.append(t)
        for g,_ in boundary(s):
            if g and low.get(g)!=s:
                indeg[g]-=1
                if not indeg[g]:todo.append(g)
    assert visited==len(faces),('gradient cycle',visited,len(faces))
    return arrows

def signed_morse(critical,low,upper,d):
    lows=sorted(s for s in critical if s.bit_count()==d)
    highs=sorted(s for s in critical if s.bit_count()==d+1)
    if not lows or not highs:return [],len(lows),len(highs)
    rows={s:i for i,s in enumerate(lows)}
    @functools.lru_cache(None)
    def project(s):
        if s in upper:return ()
        if s in critical:return ((s,1),)
        assert s in low
        up=low[s];pivot=dict(boundary(up))[s]
        acc=collections.defaultdict(int)
        for g,t in boundary(up):
            if g==s:continue
            for h,n in project(g):acc[h]-=pivot*t*n
        return tuple((h,n) for h,n in acc.items() if n)
    mat=[[0]*len(highs) for _ in lows]
    for j,s in enumerate(highs):
        for g,sg in boundary(s):
            if not g:continue
            for h,n in project(g):mat[rows[h]][j]+=sg*n
    return mat,len(lows),len(highs)

def smith(M):
    A=[x[:] for x in M];m=len(A);n=len(A[0]);k=0
    while k<min(m,n):
        pivots=[(abs(A[i][j]),i,j) for i in range(k,m) for j in range(k,n) if A[i][j]]
        if not pivots:break
        _,i,j=min(pivots)
        A[k],A[i]=A[i],A[k]
        for r in A:r[k],r[j]=r[j],r[k]
        while True:
            assert A[k][k]
            restart=False
            for i in range(k+1,m):
                if A[i][k]:
                    q=A[i][k]//A[k][k]
                    if q:A[i]=[a-q*b for a,b in zip(A[i],A[k])]
                    if A[i][k]:A[i],A[k]=A[k],A[i];restart=True;break
            if restart:continue
            for j in range(k+1,n):
                if A[k][j]:
                    q=A[k][j]//A[k][k]
                    if q:
                        for i in range(m):A[i][j]-=q*A[i][k]
                    if A[k][j]:
                        for row in A:row[k],row[j]=row[j],row[k]
                        restart=True;break
            if restart:continue
            if any(A[i][k] for i in range(k+1,m)) or any(A[k][j] for j in range(k+1,n)):continue
            bad=next((i for i in range(k+1,m) for j in range(k+1,n) if A[i][j]%A[k][k]),None)
            if bad is not None:A[k]=[a+b for a,b in zip(A[k],A[bad])];continue
            break
        if A[k][k]<0:A[k]=[-a for a in A[k]]
        k+=1
    diag=[A[i][i] for i in range(k)]
    assert all(diag[i+1]%diag[i]==0 for i in range(len(diag)-1))
    assert all(A[i][j]==0 for i in range(m) for j in range(n) if i!=j)
    return diag

def run_one(faces,order,root):
    crit,low,up=match(faces,order,root)
    h=acyclic(faces,low)
    counts={str(d):v for d,v in sorted(collections.Counter(s.bit_count()-1 for s in crit).items())}
    boundaries={};diags={}
    for d in range(1,10):
        mat,m,n=signed_morse(crit,low,up,d)
        if m and n:
            diag=smith(mat);boundaries[str(d)]={'rows':m,'columns':n,'nonzero_smith':diag}
            diags[d]=diag
    betti={}
    for dim,c in sorted((int(k),v) for k,v in counts.items()):
        if dim==0:continue
        betti[str(dim)]=c-len(diags.get(dim,[]))-len(diags.get(dim+1,[]))
    return dict(critical=counts,matched_pairs=len(low),hasse_incidences=h,boundaries=boundaries,
                integral_reduced_betti={d:v for d,v in betti.items() if v})

def main():
    assert len(VERTICES)==10
    assert all(sum(row)==3 for row in ADJ)
    assert all(ADJ[i][j]==ADJ[j][i] for i in range(10) for j in range(10))
    result={}
    for k in range(2,11):
        faces,facet_count=face_sets(k)
        if not faces:
            result[str(k)]={'facets':0,'nonempty_faces':0,'homotopy':'void'};continue
        forward=run_one(faces,range(10),1<<0)
        backward=run_one(faces,range(9,-1,-1),1<<9)
        assert forward['integral_reduced_betti']==backward['integral_reduced_betti']
        result[str(k)]={'facets':facet_count,'nonempty_faces':len(faces),'forward':forward,'reverse':backward}
    assert result['2']['forward']['integral_reduced_betti']=={'6':6}
    assert result['3']['forward']['integral_reduced_betti']=={'6':6}
    assert result['4']['forward']['integral_reduced_betti']=={'5':26}
    assert result['5']['forward']['integral_reduced_betti']=={'3':1,'4':5}
    assert result['6']['forward']['integral_reduced_betti']=={'3':11}
    assert result['7']['forward']['integral_reduced_betti']=={'1':11}
    assert all(result[str(k)]['homotopy']=='void' for k in range(8,11))
    print(json.dumps({'results':result,'verification':'PETERSEN_ALL_CUT_COMPLEXES_EXACT_Z_HOMOTOPY_OK'},indent=2,sort_keys=True))
if __name__=='__main__':main()
