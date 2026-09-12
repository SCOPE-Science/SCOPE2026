import numpy as np
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-16,17))
def Gk(k,x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in NS:
        tot+=B3f(x-n*a)*B3f(x-n*a-k*beta)
    return tot
def Mmat(y,th):
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        ys=y+s_*delta
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=Gk(k,np.array([ys]))[0]*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    return M
# th dependence: each (s,sp) entry has <=2 Fourier modes in th (q in small set). det as trig poly in th.
# Fix y=0: sweep th fine
y=0.0
ths=np.linspace(0,1,2001)
lo=np.zeros_like(ths); deta=np.zeros_like(ths)
for j,th in enumerate(ths):
    M=Mmat(y,th)
    e=np.linalg.eigvalsh(M)
    lo[j]=e[0]; deta[j]=np.linalg.det(M).real
print("y=0: min lo over th:",lo.min(),"max:",lo.max())
print("det min/max:",deta.min(),deta.max())
# print th values where lo small
idx=np.argsort(lo)[:8]
for j in idx: print(f" th={ths[j]:.5f} lo={lo[j]:.3e} det={deta[j]:.3e}")
# cross-check at th=0: null vector?
M0=Mmat(0.0,0.0)
e,v=np.linalg.eigh(M0)
print("eig th=0:",np.round(e,8))
print("null vec:",np.round(v[:,0],4))
