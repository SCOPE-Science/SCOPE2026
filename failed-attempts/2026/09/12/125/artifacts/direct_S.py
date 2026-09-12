import numpy as np
def B3(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11; binv=6/11
def Gk(k,x):
    x=np.asarray(x,float); tot=np.zeros_like(x)
    for n in range(-12,13):
        tot+=B3(x-n*a)*B3(x-n*a-k*beta)
    return tot
# zero-BC model on [-L,L] with grid multiple of delta=1/22
delta=1/22
L=6.0
N=int(2*L/delta)
xs=np.linspace(-L,L-delta,N)
print("N=",N)
# map x value -> index
def idx_of(x):
    return np.round((x+L)/delta).astype(int)
S=np.zeros((N,N))
for k in range(-7,8):
    g=Gk(k,xs)
    if np.max(np.abs(g))<1e-15: continue
    shift=int(round(k*beta/delta))  # =12k
    j=np.arange(N); js=j-shift
    valid=(js>=0)&(js<N)
    S[j[valid],js[valid]]+=binv*g[valid]
print("S built, symmetric err:",np.max(np.abs(S-S.T)))
e=np.linalg.eigvalsh(S)
print("eig min5:",e[:5])
print("eig max5:",e[-5:])
print("min:",e[0],"max:",e[-1])
np.save("output/artifacts/direct_eig.npy",e)
