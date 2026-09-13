"""Script Y: duality check. M[j,k] for OUTPUT j=(3,0,0): which INPUTS k feed it?
k ≈ A^{-1} j + sidebands. A^{-1}(3,0,0) = (3,-3,3): outside box2! So row mass inside
box2 = 0 is EXPECTED (adjoint expands). The D-block question is about the HIGH-HIGH
block norm, and columns show mass concentrates at k' = A^{-T}j sidebands with
exponential sideband decay (0.99/0.09/0.006). Column tails outside box2 are ~0.09
for low inputs -- small but not < 0.0116. Remedy: LARGER box K=4/5: column mass
outside boxK decays exponentially (sideband order grows). Measure tails vs K."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
R=6; N=24
modes=[(i,j,k) for i in range(-R,R+1) for j in range(-R,R+1) for k in range(-R,R+1)]
Jarr=np.array(modes,float)
rad=np.array([max(abs(mm) for mm in m) for m in modes])
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
def coltail(k):
    G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,np.array(k,float))[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
    c=np.abs(np.array([G[...,j].mean() for j in range(len(modes))]))
    return {K: float(np.sqrt((c[rad>K]**2).sum())) for K in [2,3,4,5]}
for k in [(1,0,0),(0,1,0),(1,1,1),(2,-1,1)]:
    print(f"k={k}: tail vs K:", {K: round(v,5) for K,v in coltail(k).items()})
