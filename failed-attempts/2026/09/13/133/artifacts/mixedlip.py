import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
from delta import eu, es, B
# Mixed pairing: Q(y)=r(y+u+v)-r(y+u)-r(y+v)+r(y), u=lam^k a eu, v=mu^k b es.
# Corner-integral: Q = int_0^1int_0^1 D2r(y+su+tv)[u,v] dsdt.
# grad Q = int int D3r(...)[u,v,.]: |grad Q| <= max|D3r| |u||v| (operator). max|D3r|=(2pi)^3*0.04=9.92.
# |grad_x S_k| <= lam^k * 9.92 * |u_k||v_k| = 9.92 h^2 lam^k (since lam^k mu^k=1).
D3=(2*np.pi)**3*0.04; L2=(2*np.pi)**2*0.04; LipR=0.32
lam=(3+np.sqrt(5))/2; mu=(3-np.sqrt(5))/2
print("D3",D3)
def Lmixed(h,K1):
    L=0.0
    for k in range(K1+1):
        stab = 2*L2*h*mu**k          # stable pairing
        mix = D3*h*h*1.0             # mixed (lam^k*|u||v| = h^2)
        unst = 2*L2*min(h*lam**k,1.0)
        L+=lam**k*min(stab,mix,unst)
    for j in range(1,K1+1):
        stab = 2*L2*h*mu**j
        mix = D3*h*h
        unst = 2*L2*min(h*lam**j,1.0)
        L+=lam**j*min(stab,mix,unst)
    return L
for h in [0.05,0.03,0.015]:
    for K1 in [8,12,16]:
        print("h",h,"K1",K1,"Lmixed",round(Lmixed(h,K1),4))
# empirical local Lipschitz: sample max |grad| proxy: |D(x+d)-D(x)|/|d| at random
rng=np.random.default_rng(0)
for h in [0.05,0.03,0.015]:
    X=rng.random((3000,2)); d=2e-4; E=rng.random((3000,2))-0.5; E/=np.linalg.norm(E,axis=1)[:,None]
    D1=Delta_grid(X,h,h,N=14); D2=Delta_grid((X+d*E)%1.0,h,h,N=14)
    print("h",h,"emp Lip: max",np.abs(D1-D2).max()/d,"p99",np.percentile(np.abs(D1-D2)/d,99))
