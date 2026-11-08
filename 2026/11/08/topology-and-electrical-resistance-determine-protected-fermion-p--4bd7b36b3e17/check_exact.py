"""Exact integer/rational graph-cycle and fermion-Hamiltonian verification."""
from itertools import combinations
import sympy as s
import random

def components(n,edges):
    groups=[{i} for i in range(n)]
    for a,b in edges:
        ai=next(i for i,g in enumerate(groups) if a in g)
        bi=next(i for i,g in enumerate(groups) if b in g)
        if ai!=bi:
            groups[ai].update(groups[bi]);groups.pop(bi)
    return [sorted(g) for g in groups]

def exact(n,F):
    edges=list(combinations(range(n),2));idx={e:i for i,e in enumerate(edges)}
    loss=set(F);safe=set(edges)-loss;N=len(edges)
    H=s.zeros(N)
    for (a,b),i in idx.items():
        for c in range(n):
            if c!=a and c!=b:
                e=tuple(sorted((b,c)));H[idx[e],i]+=1 if c<b else -1
                e=tuple(sorted((a,c)));H[idx[e],i]+=1 if a<c else -1
    assert H==H.T
    cf=components(n,loss)
    cbar=components(n,safe)
    high=[]
    for i in range(len(cf)-1):
        v=[0]*n
        for a in cf[i]:v[a]=len(cf[-1])
        for a in cf[-1]:v[a]=-len(cf[i])
        high.append(s.Matrix([v[b]-v[a] for a,b in edges]))
    # spanning-forest fundamental cycle construction
    tree=[];back=[]; forest_components=[{i} for i in range(n)]
    for a,b in sorted(safe):
        ai=next(i for i,g in enumerate(forest_components) if a in g)
        bi=next(i for i,g in enumerate(forest_components) if b in g)
        if ai==bi:back.append((a,b))
        else:
            tree.append((a,b)); forest_components[ai].update(forest_components[bi]);forest_components.pop(bi)
    adjacency={i:[] for i in range(n)}
    for a,b in tree: adjacency[a].append(b);adjacency[b].append(a)
    low=[]
    for a,b in back:
        # cycle a -> b followed by b -> a along the tree
        stack=[(b,[b])];found=None
        while stack:
            cur,path=stack.pop()
            if cur==a:found=path;break
            for nxt in adjacency[cur]:
                if nxt not in path:stack.append((nxt,path+[nxt]))
        assert found is not None
        y=[0]*N;y[idx[(a,b)]]=1
        for p,q in zip(found,found[1:]):
            y[idx[tuple(sorted((p,q)))]]+=1 if p<q else -1
        low.append(s.Matrix(y))
    for v in high:
        assert H*v==(n-2)*v
        assert all(v[idx[e]]==0 for e in loss)
    for v in low:
        assert H*v==-2*v
        assert all(v[idx[e]]==0 for e in loss)
    B=s.Matrix.hstack(*high,*low) if high or low else s.zeros(N,0)
    expected=len(safe)-n+len(cf)+len(cbar)-1
    assert B.cols==expected
    assert B.rank()==expected
    D=B*(B.T*B).inv()*B.T if expected else s.zeros(N)
    assert D*D==D and H*D==D*H
    # Test maximality independently: ranks of loss projection on each eigenspace
    Pplus=(H+2*s.eye(N))/n
    Pminus=s.eye(N)-Pplus
    cols=[idx[e] for e in sorted(loss)]
    rankplus=Pplus[:,cols].rank() if cols else 0
    rankminus=Pminus[:,cols].rank() if cols else 0
    assert expected==N-rankplus-rankminus
    def resistance(a,b):
        C=next(c for c in cbar if a in c);assert b in C
        L=s.zeros(len(C));loc={w:i for i,w in enumerate(C)}
        for x,y in safe:
            if x in loc and y in loc:
                i=loc[x];j=loc[y];L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
        v=s.zeros(len(C),1);v[loc[a]]=1;v[loc[b]]=-1
        w=s.zeros(len(C),1)
        if len(C)>1:
            solved=L[:-1,:-1].inv()*v[:-1,:]
            for i in range(len(C)-1):w[i]=solved[i]
        return (v.T*w)[0]
    tag={a:i for i,c in enumerate(cf) for a in c}
    siz={a:len(c) for c in cf for a in c}
    for (a,b),i in idx.items():
        highprob=(s.Rational(1,siz[a])+s.Rational(1,siz[b]))/n if tag[a]!=tag[b] else s.Rational(0)
        lowprob=1-resistance(a,b) if (a,b) in safe else s.Rational(0)
        assert D[i,i]==highprob+lowprob, (n,loss,a,b,D[i,i],highprob,lowprob)
    return expected

def run():
    rng=random.Random(1843);tests=0
    for n in (3,4):
        edges=list(combinations(range(n),2))
        for bits in range(1<<len(edges)):
            F=[e for k,e in enumerate(edges) if (bits>>k)&1]
            exact(n,F);tests+=1
    for n in (5,6,7):
        edges=list(combinations(range(n),2))
        Fs=[[],edges,[(i,i+1) for i in range(n-1)],[(0,i) for i in range(1,n)],
            [(i,i+1) for i in range(0,n-1,2)],
            [e for e in edges if (e[0]+e[1])%3==0],
            [e for e in edges if rng.random()<.4]]
        for F in Fs:
            d=exact(n,F);tests+=1
        print('n',n,'examples',len(Fs),'last dark dimension',d)
    print('exact checked graph selections:',tests)
if __name__=='__main__':run()
