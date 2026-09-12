import numpy as np, time
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-4,6))
def precompute_G(ys):
    # ys: (Ny,) base; Y: (Ny,11) nodes y+s*delta
    s=np.arange(11)
    Y=ys[:,None]+s[None,:]*delta  # (Ny,11)
    G={}  # k -> (Ny,11)
    for k in KS:
        tot=np.zeros_like(Y)
        for n in NS:
            tot+=B3f(Y-n*a)*B3f(Y-n*a-k*beta)
        G[k]=tot
    return G
def Mmat_from_G(Garr, yi, y, th):
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=Garr[k][yi,s_]*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    return M
ys=np.linspace(0,delta,9,endpoint=False)
G=precompute_G(ys)
# 1) hermitian + trace
for yi,y in enumerate(ys[:3]):
    for th in [0.0,0.3,0.9]:
        M=Mmat_from_G(G,yi,y,th)
        print(f"y={y:.5f} th={th} herm={np.max(np.abs(M-M.conj().T)):.2e} tr={np.trace(M).real:.6f}")
# 2) y periodicity: M(y+delta) unitarily equiv to M(y) (cyclic shift) -> same eig
ys2=np.array([0.01]); G2=precompute_G(ys2); ys3=np.array([0.01+delta]); G3=precompute_G(ys3)
e1=np.linalg.eigvalsh(Mmat_from_G(G2,0,ys2[0],0.3)); e2=np.linalg.eigvalsh(Mmat_from_G(G3,0,ys3[0],0.3))
print("y-shift eig diff:",np.max(np.abs(e1-e2)))
print("eig@sample:",np.round(e1,6))
