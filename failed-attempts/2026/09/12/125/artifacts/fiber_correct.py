import numpy as np
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
an=np.arange(-10,11)
def Gk(k,x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in an:
        tot+=B3f(x-n*a)*B3f(x-n*a-k*beta)
    return tot
def Mmat(y,th):
    """M(y,th)_{r,s} = b^{-1} sum_{k = s-r mod 11, |k|<=7} G_k(y - r*delta) e^{+2 pi i 12 k th}"""
    M=np.zeros((11,11),complex)
    for r in range(11):
        xr = y - r*delta
        for s in range(11):
            d = s - r
            tot=0j
            # lifts k = d + 11 t with |k|<=7
            for t in range(-2,3):
                k = d + 11*t
                if abs(k)>7: continue
                tot += Gk(k,np.array([xr]))[0]*np.exp(2j*np.pi*12*k*th)
            M[r,s]=binv*tot
    return M
# 1) Hermitian
for (y,th) in [(0.01,0.3),(0.0,0.0),(0.04,0.9),(0.02,0.5),(delta*0.3,1/7)]:
    M=Mmat(y,th)
    print("herm",np.max(np.abs(M-M.conj().T)),"trace",np.trace(M).real)
# 2) theta-shift unitary equivalence: eig(M(y,th)) == eig(M(y,th+1/11))
for (y,th) in [(0.01,0.3),(0.02,0.5)]:
    e1=np.linalg.eigvalsh(Mmat(y,th)); e2=np.linalg.eigvalsh(Mmat(y,th+1/11))
    print("shift-equiv",np.max(np.abs(e1-e2)))
# 3) y-periodicity delta
e1=np.linalg.eigvalsh(Mmat(0.01,0.3)); e2=np.linalg.eigvalsh(Mmat(0.01+delta,0.3))
print("y-period",np.max(np.abs(e1-e2)))
# 4) scan
import time; t0=time.time()
Ny=24; Nt=24
ys=np.linspace(0,delta,Ny,endpoint=False); ths=np.linspace(0,1/11,Nt,endpoint=False)
mn=1e9; arg=None; mx=-1e9
for y in ys:
    for th in ths:
        e=np.linalg.eigvalsh(Mmat(y,th))
        if e[0]<mn: mn=e[0]; arg=(y,th)
        mx=max(mx,e[-1])
print(f"scan {Ny}x{Nt}: min={mn:.6e} at y={arg[0]:.8f},th={arg[1]:.6f} max={mx:.6f} ({time.time()-t0:.1f}s)")
