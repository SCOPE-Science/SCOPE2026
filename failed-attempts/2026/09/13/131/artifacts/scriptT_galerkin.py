"""Script T: Galerkin eigenvalue exclusion certificate on {|lam|>=0.9}.
M_K = K-box Fourier Galerkin (K=2, d=125); computed spectrum: 1.0, next 0.0712.
Bauer-Fike exclusion: need ||M-M_K|| (tail+quad) <= delta with delta < gap to 0.9
circle... Bauer-Fike radius = cond(V)*||E||; computed cond(V) huge for nonnormal M.
Instead use resolvent certificate: for |lam|=0.9, ||(lam-M_K)^{-1}|| = 1/smin;
if smin(0.9 e^{it}-M_K) >= s0 uniformly and ||E||< s0 then no spectrum of M on circle
=> same #eigs inside (1: just eig 1) by homotopy. Compute s0 = min_t smin on 64 pts
+ Lipschitz pad in t. Then required ||E|| < s0. Report s0 and the required tail."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
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
smin_list=[]
thetas=np.linspace(0,2*math.pi,65)[:-1]
for t in thetas:
    smin_list.append(min(np.linalg.svd(0.9*np.exp(1j*t)*np.eye(d)-M,compute_uv=False)))
s0=min(smin_list); print(f"min_t smin(0.9 e^it - M_K) = {s0:.4f} over 64 pts")
print(f"Lipschitz pad in t: 0.9*2pi/64 = {0.9*2*math.pi/64:.4f} => certified s0 >= {s0-0.9*2*math.pi/64:.4f}")
print("quadrature error: grid 24 vs 32 agreed to 4 decimals (Script I) => quad err < 1e-4 (indicative)")
print("tail: needs analytic-nonstationary-phase bound (Script N route) below required threshold")
