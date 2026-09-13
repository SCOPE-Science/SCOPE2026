"""Script Z: K=4 Galerkin spectrum + resolvent margin on |lam|=0.9; column-tail norms
at K=4/5 (need operator tail < s0). Operator tail <= sqrt(#cols in box)*max col tail
is too crude; instead estimate HIGH-LOW block norm directly by power iteration on
E = M - P_K M P_K restricted... simpler: randomized operator-norm estimate of the
off-block via matvecs on the R=6 reference matrix."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
R=6; N=20
modes=[(i,j,k) for i in range(-R,R+1) for j in range(-R,R+1) for k in range(-R,R+1)]
d=len(modes); idx={m:i for i,m in enumerate(modes)}
Jarr=np.array(modes,float)
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
def colvec(k):
    G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,np.array(k,float))[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
    return np.array([G[...,j].mean() for j in range(d)])
import pickle
M=np.zeros((d,d),complex)
KK=[m for m in modes if max(abs(mm) for mm in m)<=5]
for k in KK:
    M[:,idx[k]]=colvec(k)
np.save("output/artifacts/refmat_R6_N20.npy",M)
for K in [4,5]:
    inb=np.array([i for i,m in enumerate(modes) if max(abs(mm) for mm in m)<=K])
    s=np.array(sorted(set(range(d))-set(inb.tolist())))
    E=np.zeros_like(M); E[np.ix_(s,inb)]=M[np.ix_(s,inb)]; E[np.ix_(inb,s)]=M[np.ix_(inb,s)]; E[np.ix_(s,s)]=M[np.ix_(s,s)]
    print(f"K={K}: off-block op norm <={np.linalg.svd(E,compute_uv=False)[0]:.4f}")
    MK=M[np.ix_(inb,inb)]
    ev=np.linalg.eigvals(MK); o=np.argsort(-np.abs(ev))
    print(f"   Galerkin top |eig|: {np.abs(ev[o[:4]]).round(4)}")
    ss=min(min(np.linalg.svd(0.9*np.exp(1j*t)*np.eye(len(inb))-MK,compute_uv=False)) for t in np.linspace(0,2*math.pi,25)[:-1])
    print(f"   resolvent s0(24pts, no pad)={ss:.4f}")
