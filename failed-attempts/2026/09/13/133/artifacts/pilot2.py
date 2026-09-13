import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
# IMPROVED uniform constants for fixed diagonal pair (h,h):
# S_k^fwd as f of y=B^k x: Q_k(y)=r(y+u_k+vs_k)-r(y+u_k)-r(y+vs_k)+r(y), u_k=lam^k a eu, vs_k=mu^k b es.
# grad_x S_k = (B^k)^T grad Q_k; |grad Q_k|<= min(2*L2*|vs_k| (stable pairing), 2*L2*|u_k| (unstable pairing)).
# Take per-k min bound and also cap by 4*LipR sup; mixed-pairing refinement available but start here.
# Same backward with Bi: |grad|<= lam^j min(2 L2 mu^j|a|, ...).
L2=(2*np.pi)**2*0.04; LipR=0.32; lam=(3+np.sqrt(5))/2; mu=(3-np.sqrt(5))/2
def Lpair(h,K1):
    L=0.0
    for k in range(K1+1):
        L+=lam**k*min(2*L2*h*mu**k, 2*L2*((lam**k*h)%1.0 if False else h*lam**k))
    for j in range(1,K1+1):
        L+=lam**j*min(2*L2*h*mu**j, 2*L2*h*lam**j)
    return L
for h in [0.05,0.03,0.015]:
    for K1 in [8,12,16]:
        print("h",h,"K1",K1,"Lpair",Lpair(h,K1))
