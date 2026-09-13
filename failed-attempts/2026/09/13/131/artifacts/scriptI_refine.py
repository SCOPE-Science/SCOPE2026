"""Script I: Fourier matrix at K=3 and grid refinement K=2 N=24/32; check 2nd eigenvalue stability."""
import numpy as np, math, sys
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
def topm(K,N,n=6):
    modes=[(i,j,k) for i in range(-K,K+1) for j in range(-K,K+1) for k in range(-K,K+1)]
    d=len(modes); Jarr=np.array(modes,float)
    g=np.linspace(0,1,N,endpoint=False)
    X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
    M=np.zeros((d,d),complex)
    for n_,k in enumerate(modes):
        G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,np.array(k,float))[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
        M[:,n_]=np.array([G[...,j].mean() for j in range(d)])
    ev=np.linalg.eigvals(M); o=np.argsort(-np.abs(ev))
    return d,np.abs(ev[o[:n]]).round(4)
for K,N in [(2,24),(2,32),(3,20)]:
    print(f"K={K} N={N}:",topm(K,N))
