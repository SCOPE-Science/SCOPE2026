import numpy as np
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
an = np.arange(-8,9)  # exact: covers all nonzero terms
def Gk(k, x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in an:
        tot+=B3f(x-n*a)*B3f(x-n*a-k*beta)
    return tot
# check support cutoff: |k|>=8 -> 0
for k in [7,8,9]:
    print(k, np.max(np.abs(Gk(k,np.linspace(0,0.5,501)))))
# precompute gk_s(y) = G_k(y+s*delta) for y grid
def Mmat(y,th):
    M=np.zeros((11,11),complex)
    for s in range(11):
        ys=y+s*delta
        for sp in range(11):
            tot=0j
            # k = s-sp mod 11, |k|<=7
            for k in [s-sp, s-sp-11, s-sp+11]:
                if abs(k)>7: continue
                v=(s-sp-12*k)/11.0
                assert abs(v-round(v))<1e-9, (s,sp,k,v)
                v=int(round(v))
                tot+=Gk(k,np.array([ys]))[0]*np.exp(2j*np.pi*v*th)
            M[s,sp]=binv*tot
    return M
for (y,th) in [(0.0,0.0),(0.01,0.3),(0.04,0.9),(0.02,0.5)]:
    M=Mmat(y,th)
    print("y,th=",y,th,"herm",np.max(np.abs(M-M.conj().T)))
    e=np.linalg.eigvalsh(M)
    print("  eig:",np.round(e,6))
    print("  trace:",np.trace(M).real)
