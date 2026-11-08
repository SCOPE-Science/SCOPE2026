"""Numerical independent Hamiltonian/projector test for pair-selective fermion loss."""
import itertools, random
import numpy as np
from numpy.linalg import eigh,svd,pinv
from scipy.linalg import expm

def ncomponents(n,edges):
    p=list(range(n))
    def find(i):
        while p[i]!=i:
            p[i]=p[p[i]];i=p[i]
        return i
    for a,b in edges:p[find(a)]=find(b)
    d={}; groups=[]
    for a in range(n):
        r=find(a)
        if r not in d:d[r]=len(groups);groups.append([])
        groups[d[r]].append(a)
    return groups

def projector_direct(n,loss_edges):
    pairs=list(itertools.combinations(range(n),2)); idx={e:i for i,e in enumerate(pairs)}
    N=len(pairs); H=np.zeros((N,N))
    for (a,b),i in idx.items():
        for c in range(n):
            if c!=a and c!=b:
                x,y=sorted((c,b));H[idx[x,y],i]+=1 if c<b else -1
                x,y=sorted((a,c));H[idx[x,y],i]+=1 if a<c else -1
    assert np.max(abs(H-H.T))<1e-12
    es, vs=eigh(H); plus=np.where(np.abs(es-(n-2))<1e-8)[0]; minus=np.where(np.abs(es+2)<1e-8)[0]
    assert len(plus)==n-1 and len(minus)==N-n+1
    D=np.zeros((N,N))
    for eig_inds in [plus,minus]:
        V=vs[:,eig_inds];B=V[[idx[e] for e in loss_edges],:]
        if not len(loss_edges): Q=V
        else:
            u,s,vh=svd(B,full_matrices=True)
            rank=int(np.sum(s>1e-9));Q=V@vh[rank:].T
        D+=Q@Q.T
    return pairs,H,D

def predicted(n,loss_edges):
    pairs=list(itertools.combinations(range(n),2));F=set(loss_edges);Ebar=set(pairs)-F
    compsF=ncomponents(n,F);compsBar=ncomponents(n,Ebar)
    cf={a:len(c) for c in compsF for a in c}; labs={a:i for i,c in enumerate(compsF) for a in c}
    L=np.zeros((n,n))
    for a,b in Ebar:L[a,a]+=1;L[b,b]+=1;L[a,b]-=1;L[b,a]-=1
    Lp=pinv(L,hermitian=True,rcond=1e-12)
    probs=[]
    for a,b in pairs:
        high=(1/cf[a]+1/cf[b])/n if labs[a]!=labs[b] else 0.0
        if (a,b) in Ebar:
            d=np.zeros(n);d[a]=1;d[b]=-1
            low=1-d@Lp@d
        else: low=0.0
        probs.append(high+low)
    dim=len(Ebar)-n+len(compsBar)+len(compsF)-1
    return dim,np.array(probs)

def run():
    rng=random.Random(721001)
    tests=0
    for n in range(3,9):
        pairs=list(itertools.combinations(range(n),2));N=len(pairs)
        Fs=[[],pairs,[(a,b) for a,b in pairs if a==0],[(a,b) for a,b in pairs if b==a+1],[(a,b) for a,b in pairs if a%2==0 and b==a+1]]
        Fs += [[p for p in pairs if rng.random()<pedge] for pedge in [0.12,0.33,0.5,0.81,0.93] for _ in range(3)]
        for F in Fs:
            _,H,D=projector_direct(n,F)
            dim,pr=predicted(n,F)
            assert abs(np.trace(D)-dim)<3e-7,(n,F,np.trace(D),dim)
            assert np.max(abs(np.diag(D)-pr))<3e-7,(n,F,np.diag(D),pr)
            assert np.min(np.linalg.eigvalsh(D))>-3e-7
            tests+=1
    for n in (4,6,8):
        F=[(2*i,2*i+1) for i in range(n//2)]
        pairs,H,D=projector_direct(n,F)
        matched={e for e in F}
        for i,e in enumerate(pairs):
            assert abs(D[i,i]-(0 if e in matched else 1-1/(n-2)))<1e-8
        print('perfect matching',n,'dim',round(np.trace(D)),'unmonitored survival',1-1/(n-2))
    n=5;F=[(0,1),(0,2),(2,3)]
    pairs,H,D=projector_direct(n,F)
    Gamma=np.zeros(len(pairs))
    for j,e in enumerate(pairs):
        if e in F:Gamma[j]=[1,2,5][F.index(e)]
    # exponential e^{-i(H-i Gamma/2)t} for increasing t, verify convergence to dark norm
    state=np.zeros(len(pairs));state[pairs.index((1,3))]=1
    target=D[pairs.index((1,3)),pairs.index((1,3))]
    at=[]
    for t in (25,100,400):
        y=expm((-1j*H-np.diag(Gamma)/2)*t)@state
        at.append(float(np.vdot(y,y).real))
    assert at[-1]>=target-1e-8 and abs(at[-1]-target)<3e-5,(at,target)
    print('tested graph subsets:',tests,'numerical trajectories:',at,'predicted final',target)
if __name__=='__main__':run()
