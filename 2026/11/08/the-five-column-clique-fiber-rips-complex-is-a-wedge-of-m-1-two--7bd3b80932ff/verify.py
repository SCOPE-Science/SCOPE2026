"""Exhaustive small-parameter verification for scale-two Rips complexes of K_m square C_5.
Standard Python 3, no nonstandard packages. Mathematical proof in RESULT.md is uniform.
"""
from collections import Counter


def complex_for(m):
    N=5*m
    V=range(N)
    def pt(v): return divmod(v,m)
    def allowed(u,v):
        i,a=pt(u);j,b=pt(v)
        return min((i-j)%5,(j-i)%5)+(a!=b)<=2
    neighbors=[sum(1<<j for j in V if j!=i and allowed(i,j)) for i in V]
    faces=[(i,) for i in V]
    layer=faces[:]
    while layer:
        nxt=[]
        for sigma in layer:
            for x in range(sigma[-1]+1,N):
                if all(neighbors[y]>>x&1 for y in sigma):
                    nxt.append(sigma+(x,))
        if not nxt: break
        faces.extend(nxt);layer=nxt
    return set(faces)


def audit(m):
    V=lambda i:[m*(i%5)+a for a in range(m)]
    e=lambda i,a:tuple(sorted((m*(i%5)+a,m*((i+2)%5)+a)))
    B=set();F=[];R=[];M=[]
    for i in range(5):
        for S in [V(i),V(i)+V(i+1)]:
            for mask in range(1,1<<len(S)):
                B.add(tuple(sorted(S[j] for j in range(len(S)) if mask>>j&1)))
    for i in range(5):
        for a in range(m):
            S=list(e(i,a))+V(i+1)
            block={tuple(sorted(S[j] for j in range(len(S)) if mask>>j&1)) for mask in range(1,1<<len(S))}
            F.append((i,a,block))
    for a in range(m):
        S=[m*i+a for i in range(5)]
        block={tuple(sorted(S[j] for j in range(5) if mask>>j&1)) for mask in range(1,1<<5)}
        R.append(block)
    U=set(B)
    for _,_,block in F:U|=block
    X=complex_for(m)
    assert X==U.union(*R), (m,len(X),len(U.union(*R)),len(X-U.union(*R)))
    assert all(F[k][2].intersection(F[j][2])<=B for k in range(len(F)) for j in range(k))
    # Original U collapses to B, by actual free-pair removal in descending cardinalities.
    W=set(U);npairs=0
    for i,a,_ in F:
        endpoint=e(i,a); p=V(i+1)[0];Q=V(i+1)[1:]
        for t in range(len(Q),-1,-1):
            from itertools import combinations
            for sub in combinations(Q,t):
                low=tuple(sorted(endpoint+sub));up=tuple(sorted(endpoint+sub+(p,)))
                assert low in W and up in W
                # check only one inclusion-minimal upper immediate coface
                cofaces=[tuple(sorted(low+(v,))) for v in range(5*m) if v not in low and tuple(sorted(low+(v,))) in W]
                assert cofaces==[up],(m,i,a,low,cofaces,up)
                W.remove(low);W.remove(up);npairs+=1
    assert W==B
    for a in range(m):
        row=set(R[a]);intersection=row&U
        triangles={tuple(sorted((m*i+a,m*((i+1)%5)+a,m*((i+2)%5)+a))) for i in range(5)}
        es={e(i,a) for i in range(5)}
        C={tuple([m*i+a]) for i in range(5)}|{tuple(sorted((m*i+a,m*((i+1)%5)+a))) for i in range(5)}
        assert intersection==C|es|triangles, (m,a,len(intersection),len(C|es|triangles))
        z=set(intersection)
        for i in range(5):
            x=e(i,a); t=tuple(sorted((m*i+a,m*((i+1)%5)+a,m*((i+2)%5)+a)))
            assert x in z and t in z
            cofaces=[tuple(sorted(x+(v,))) for v in range(5*m) if v not in x and tuple(sorted(x+(v,))) in z]
            assert cofaces==[t]
            z.remove(x);z.remove(t)
        assert z==C
    # Binary boundary rank checks: reduced Betti rank m-1 in dimension two.
    levels={k:sorted(f for f in X if len(f)==k) for k in range(1,max(map(len,X))+1)}
    rank={}
    for k in range(2,len(levels)+1):
        ind={f:i for i,f in enumerate(levels[k-1])};pivots={}
        for face in levels[k]:
            b=0
            for j in range(k):b^=1<<ind[face[:j]+face[j+1:]]
            while b:
                x=b.bit_length()-1
                if x in pivots:b^=pivots[x]
                else:pivots[x]=b;break
        rank[k]=len(pivots)
    betti={k-1:len(levels[k])-rank.get(k,0)-rank.get(k+1,0)-(k==1) for k in levels}
    assert betti=={k: (m-1 if k==2 else 0) for k in betti},(m,betti)
    print('m=',m,'faces=',len(X),'fvector=',[len(levels[k]) for k in levels],
          'U_collapses=',npairs,'row_collapse_pairs=',5*m,'reduced_mod2_betti=',betti)

if __name__=='__main__':
    for m in (3,4,5):audit(m)
    print('ALL_VERIFY_OK')
