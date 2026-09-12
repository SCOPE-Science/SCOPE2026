import numpy as np, time
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-16,17))
def precompute_G(ys):
    s=np.arange(11); Y=ys[:,None]+s[None,:]*delta
    G={}
    for k in KS:
        tot=np.zeros_like(Y)
        for n in NS:
            tot+=B3f(Y-n*a)*B3f(Y-n*a-k*beta)
        G[k]=tot
    return G
def Mmat(G,yi,th):
    M=np.zeros((11,11),complex)
    E={q:np.exp(2j*np.pi*q*th) for q in range(-8,9)}
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=G[k][yi,s_]*E[q]
            M[s_,sp]=binv*tot
    return M
y=np.array([0.0]); G=precompute_G(y)
ths=np.linspace(0,1,361)
los=[]; dets=[]
t0=time.time()
for th in ths:
    M=Mmat(G,0,th)
    e=np.linalg.eigvalsh(M)
    los.append(e[0]); dets.append(np.linalg.det(M).real)
los=np.array(los); dets=np.array(dets)
print(f"y=0 th-sweep ({time.time()-t0:.1f}s): min lo={los.min():.3e} max={los.max():.6f}")
print("det min/max:",dets.min(),dets.max())
for j in np.argsort(los)[:8]:
    print(f" th={ths[j]:.5f} lo={los[j]:.3e} det={dets[j]:.3e}")
