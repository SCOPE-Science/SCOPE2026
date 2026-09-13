"""Script H (corrected Fourier probe): P e_k = e_k o f^{-1}; coefficient
<P e_k, e_j> = int e_k(f^{-1}(x)) conj(e_j(x)) dx = int e_{k}(y) conj(e_j(f(y))) dy
(j-th Fourier coeff of e_k o f^{-1} equals that oscillatory integral; evaluate on grid in y)."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
K,N=2,24
modes=[(i,j,k) for i in range(-K,K+1) for j in range(-K,K+1) for k in range(-K,K+1)]
d=len(modes); idx={m:n for n,m in enumerate(modes)}
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1)
Fy=f(grid)
Karr=np.array(modes,float); Jarr=np.array(modes,float)
# E[y,k,j] too big (24^3*125^2); loop over k instead
M=np.zeros((d,d),complex)
for n,k in enumerate(modes):
    kv=np.array(k,float)
    G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,kv)[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
    M[:,n]=np.array([G[...,j].mean() for j in range(d)])
ev=np.linalg.eigvals(M); o=np.argsort(-np.abs(ev))
print("dim",d,"grid",N)
print("top12 |eig|:",np.abs(ev[o[:12]]).round(4))
print("top12 arg:",np.angle(ev[o[:12]]).round(3))
print("eigvals:",ev[o[:12]].round(4))
# column-stochasticity check: |P e_0| should be 1 at j=0
print("col0 mass at j=0:",abs(M[idx[(0,0,0)],idx[(0,0,0)]]))
