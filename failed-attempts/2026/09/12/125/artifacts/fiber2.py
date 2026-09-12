import numpy as np
def B3(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
def Gk(k,x):
    # x array
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in range(-8,9):
        tot+=B3(x-n*a)*B3(x-n*a-k*beta)
    return tot
# test periodicity Gk(x+a)==Gk(x)
xs=np.linspace(0,1,9)
for k in [-7,-1,0,3]:
    print(k, np.max(np.abs(Gk(k,xs)-Gk(k,xs+a))))
# fiber
def Mmat(y,th):
    M=np.zeros((11,11),complex)
    for s in range(11):
        ys=y+s*delta
        for sp in range(11):
            tot=0j
            for v in range(-12,13):
                num=(s-sp+11*v)
                if num%12!=0: continue
                k=num//12
                if abs(k)>7: continue
                tot+=Gk(k,np.array([ys]))[0]*np.exp(2j*np.pi*v*th)
            M[s,sp]=binv*tot
    return M
for (y,th) in [(0.01,0.3),(0.0,0.0),(0.04,0.9),(delta*0.5,0.123)]:
    M=Mmat(y,th)
    print("herm",np.max(np.abs(M-M.conj().T)), "eigmin",np.linalg.eigvalsh(M)[0].real)
# coarse scan
for N,Mn in [(12,12),(24,24)]:
    ys=np.linspace(0,delta,Mn,endpoint=False)
    ths=np.linspace(0,1,Mn,endpoint=False)
    mn=1e9; arg=None; mx=-1e9
    for y in ys:
        for th in ths:
            e=np.linalg.eigvalsh(Mmat(y,th))
            if e[0]<mn: mn=e[0]; arg=(y,th)
            mx=max(mx,e[-1])
    print(f"grid {N}x{Mn}: min={mn:.6f} at y={arg[0]:.6f},th={arg[1]:.6f} max={mx:.6f}")
