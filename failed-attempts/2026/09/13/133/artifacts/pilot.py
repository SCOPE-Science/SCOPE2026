import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
# RIGOROUS constants (crude but valid):
# Lip(r)<=0.32, L2=max|D2r|=(2pi)^2*0.04=1.579; per-term Lip(S_k)<=2*L2*h; tail sup T(K1)=2*LipR*h*(mu^(K1+1)/(1-mu)) each side
L2=(2*np.pi)**2*0.04; LipR=0.32; mu=(3-np.sqrt(5))/2
K1=12; h=0.05
Tside=2*LipR*h*(mu**(K1+1)/(1-mu)); T=2*Tside
Lhead=(K1+1)*2*L2*h*2  # fwd+bwd
print("K1",K1,"tail T",T,"Lhead",Lhead)
thresh=0.001*h*h
print("threshold c0*h^2 =",thresh)
menu=[(s1*h,s2*h) for s1 in (1,-1) for s2 in (1,-1)]
n=200; xs=np.linspace(0,1,n,endpoint=False)
XX,YY=np.meshgrid(xs,xs); Xg=np.stack([XX.ravel(),YY.ravel()],axis=1)
diam=np.sqrt(2)/n
# head = N=K1 evaluation (use N=K1 as head proxy; true tail beyond K1 bounded by T)
H=np.zeros((len(Xg),len(menu)))
for j,(a,b) in enumerate(menu):
    H[:,j]=np.abs(Delta_grid(Xg,a,b,N=K1))
M=np.max(H,axis=1)
certified = M - Lhead*diam - T - thresh
print("grid max-head-min:",M.min(),"median:",np.median(M))
print("certified fraction:",np.mean(certified>=0)," (need 1.0)")
print("Lhead*diam =",Lhead*diam," vs typical signal",np.median(M))
print("time",round(time.time()-t0,1))
