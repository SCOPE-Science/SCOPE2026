import numpy as np, time
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; delta=1/22; binv=6/11
KS=list(range(-7,8)); NS=list(range(-16,17))
def precompute_G(ys):
    s=np.arange(11)
    Y=ys[:,None]+s[None,:]*delta
    G={}
    for k in KS:
        tot=np.zeros_like(Y)
        for n in NS:
            tot+=B3f(Y-n*a)*B3f(Y-n*a-k*beta)
        G[k]=tot
    return G
def minmax(y, th, G, yi):
    M=np.zeros((11,11),complex)
    for s_ in range(11):
        for sp in range(11):
            tot=0j
            for k in KS:
                if (s_-12*k)%11 != sp: continue
                q=(s_-12*k-sp)//11
                tot+=G[k][yi,s_]*np.exp(2j*np.pi*q*th)
            M[s_,sp]=binv*tot
    e=np.linalg.eigvalsh(M)
    return e[0], e[-1]
t0=time.time()
Ny=33; Nt=33
ys=np.linspace(0,delta,Ny,endpoint=False); ths=np.linspace(0,1,Nt,endpoint=False)
G=precompute_G(ys)
mn=1e9; arg=None; mx=-1e9
for yi,y in enumerate(ys):
    for th in ths:
        lo,hi=minmax(y,th,G,yi)
        if lo<mn: mn=lo; arg=(y,th)
        mx=max(mx,hi)
print(f"grid {Ny}x{Nt}: MIN={mn:.10e} at y={arg[0]:.8f}, th={arg[1]:.6f}; MAX={mx:.6f} ({time.time()-t0:.1f}s)")
