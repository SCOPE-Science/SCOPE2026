"""Script J: anisotropic-weight probe. Weight w(k)= <k_u'>^p <k_s'>^{-q} with axes from
A eigenbasis; weighted matrix Mw = W M W^{-1}; report operator-2-norm proxy (top singular)
vs p,q. INDICATIVE: truncation + finite grid only."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
w,P=np.linalg.eigh(Amat)
U=np.stack([P[:,1],P[:,2]],axis=1)  # unstable plane basis (2 cols)
s=P[:,0]
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
K,N=2,24
modes=[(i,j,k) for i in range(-K,K+1) for j in range(-K,K+1) for k in range(-K,K+1)]
d=len(modes); Jarr=np.array(modes,float)
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
M=np.zeros((d,d),complex)
for n_,k in enumerate(modes):
    G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,np.array(k,float))[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
    M[:,n_]=np.array([G[...,j].mean() for j in range(d)])
Ks=np.array(modes,float)
ku=np.linalg.norm(Ks@U,axis=1); ks=np.abs(Ks@s)
for p,q in [(1,1),(2,1),(2,2),(3,2)]:
    wv=(1+ku)**p*(1+ks)**(-q); wv[ks==0]= (1+ku[ks==0])**p
    Mw=(M*wv[None,:])/wv[:,None]
    s1=np.linalg.svd(Mw,compute_uv=False)[0]
    ev=np.linalg.eigvals(Mw); o=np.argsort(-np.abs(ev))
    print(f"p={p} q={q}: top singular={s1:.3f} top|eig|={np.abs(ev[o[1]]):.4f},{np.abs(ev[o[2]]):.4f} (excl. 1: zero-mode weight?)")
    print("   w(0)=",wv[modes.index((0,0,0))],"eig0 =",ev[o[0]])
