import numpy as np, time
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-16,17))
def precompute_G(y):
    G={}
    for k in KS:
        row=np.zeros(11)
        for s_ in range(11):
            x=y+s_*delta; tot=0.0
            for n in NS: tot+=float(B3f(np.array([x-n*a]))[0])*float(B3f(np.array([x-n*a-k*beta]))[0])
            row[s_]=tot
        G[k]=row
    return G
def lo_at(G,th):
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=G[k][s_]*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    return np.linalg.eigvalsh(M)[0]
for y in [0.0, delta/2, 0.01]:
    G=precompute_G(y)
    ths=np.linspace(0,1,4001)
    los=np.array([lo_at(G,th) for th in ths])
    j=np.argmin(los)
    print(f"y={y:.6f}: coarse min lo={los[j]:.4e} at th={ths[j]:.5f}; max lo={los.max():.4e}  med={np.median(los):.3e}")
    # refine around best with 40001 local
    th0=ths[j]
    ths2=th0+np.linspace(-0.0005,0.0005,2001)
    los2=np.array([lo_at(G,th) for th in ths2])
    j2=np.argmin(los2)
    print(f"   refined: min lo={los2[j2]:.4e} at th={ths2[j2]:.8f}")
