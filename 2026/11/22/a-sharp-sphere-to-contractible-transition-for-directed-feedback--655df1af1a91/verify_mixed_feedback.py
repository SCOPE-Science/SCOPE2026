"""Finite independent model/chain checks for directed multi-arm feedback networks.
Python 3 standard library; finite experiments only, not a general proof.
"""
def reduced_mod2_betti(faces):
    bydim={}
    for f in faces:
        if f:bydim.setdefault(f.bit_count()-1,[]).append(f)
    ranks={}
    for k in sorted(bydim):
        if k==0:continue
        index={f:i for i,f in enumerate(bydim[k-1])}
        pivots={}
        for face in bydim[k]:
            vec=0;bits=face
            while bits:
                bit=bits&-bits;bits-=bit
                vec^=1<<index[face^bit]
            while vec:
                i=vec.bit_length()-1
                if i in pivots:vec^=pivots[i]
                else:pivots[i]=vec;break
        ranks[k]=len(pivots)
    beta={k:len(a)-ranks.get(k,0)-ranks.get(k+1,0) for k,a in bydim.items()}
    beta[0]-=1
    return {k:v for k,v in beta.items() if v}


def sample(lengths, r):
    assert len(lengths)>=2 and all(k>=2 for k in lengths) and r>=1
    m=len(lengths); s,t=0,1;v=2;arms=[]
    for length in lengths:
        internal=list(range(v,v+length-1));v+=length-1
        path=[s]+internal+[t]
        arms.append([tuple(x) for x in zip(path,path[1:])])
    internal=list(range(v,v+r-1));v+=r-1
    ret=[tuple(x) for x in zip([t]+internal,internal+[s])]
    arcs=sum(arms,[])+ret;N=len(arcs)
    first=[];last=[];full=[];ix=0
    for A in arms:
        first.append(ix);last.append(ix+len(A)-1)
        full.append(tuple(range(ix,ix+len(A))));ix+=len(A)
    actual=set();predicted=set();fullC=list(range(ix,N))
    for mask in range(1<<N):
        # Independent direct digraph test
        indeg=[0]*v;out=[-1]*v;valid=True
        for j,(a,b) in enumerate(arcs):
            if (mask>>j)&1:
                indeg[b]+=1
                if indeg[b]>1 or out[a]>=0:valid=False;break
                out[a]=b
        if valid:
            for u in range(v):
                seen=set();z=u
                while z!=-1 and z not in seen:
                    seen.add(z);z=out[z]
                if z!=-1:valid=False;break
        if valid:actual.add(mask)
        # Independently predicted face model
        if sum((mask>>j)&1 for j in first)>1:continue
        if sum((mask>>j)&1 for j in last)>1:continue
        if all((mask>>j)&1 for j in fullC) and any(all((mask>>j)&1 for j in A) for A in full):continue
        predicted.add(mask)
    assert actual==predicted,(lengths,r,'face mismatch')
    b=reduced_mod2_betti(actual)
    long=[l for l in lengths if l>=3]
    expected=({r+long[0]-2:1} if len(long)==1 else {})
    assert b==expected,(lengths,r,b,expected)
    print(f'lengths={lengths} return={r} faces={len(actual)} mod2={b} PASS')

if __name__=='__main__':
 for lengths,r in [([3,2],1),([3,2],2),([4,2],2),([2,2,3],2),([2,3,2],3),([2,2,4],1),([3,3],1),([3,3],2),([2,3,3],2),([2,3,4],1),([4,4],2),([3,3,3],1)]:sample(lengths,r)
 print('ALL 12 MIXED-ARM CHECKS PASS')
