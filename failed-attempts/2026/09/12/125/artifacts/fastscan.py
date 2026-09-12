import numpy as np
# vectorized Zak: Za(x,nu) for arrays: precompute B3 shifts
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6
ks=np.arange(-8,9)
E = lambda nu: np.exp(2j*np.pi*ks*nu)
def smin_grid(xs,nus):
    # Z[r,s](x,nu)=Za(x+s*a/12-r/b,nu); vectorize over x: for each (r,s) shift array
    # Za(x0,nu)=sum_k B3(x0-a k) e^{2pi i k nu}
    M=np.zeros((len(xs),len(nus)))
    # precompute phases P[nu,k]
    P=np.exp(2j*np.pi*np.outer(nus,ks))  # (Nnu,K)
    for i,x in enumerate(xs):
        Z=np.zeros((11,12,len(nus)),complex)
        for r in range(11):
            for s in range(12):
                x0=x+s*a/12-r/b
                bv=B3f(x0-a*ks)  # (K,)
                Z[r,s,:]=bv@P.T  # (Nnu,)
        for j in range(len(nus)):
            M[i,j]=np.linalg.svd(Z[:,:,j],compute_uv=False)[-1]
    return M
xs=np.linspace(0,0.5,51); nus=np.linspace(0,1,51)
M=smin_grid(xs,nus)
print("min",M.min(),"max",M.max(),"mean",M.mean())
print("frac<1e-3:",np.mean(M<1e-3),"frac<1e-2:",np.mean(M<1e-2),"frac<0.05:",np.mean(M<0.05))
i,j=np.unravel_index(np.argmin(M),M.shape); print("argmin",xs[i],nus[j])
np.save("output/artifacts/smin_map.npy",M)
