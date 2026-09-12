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
for L in [4.0,6.0,8.0]:
    delta=1/22; N=int(2*L/delta); xs=np.linspace(-L,L-delta,N)
    S=np.zeros((N,N))
    for k in range(-7,8):
        g=Gk(k,xs)
        if np.max(np.abs(g))<1e-15: continue
        shift=int(round(k*beta/delta))
        j=np.arange(N); js=j-shift
        valid=(js>=0)&(js<N)
        S[j[valid],js[valid]]+=binv*g[valid]
    e=np.linalg.eigvalsh(S)
    print(f"L={L} N={N} min={e[0]:.3e} #<0.01={np.sum(e<0.01)} #<0.1={np.sum(e<0.1)} #<0.5={np.sum(e<0.5)} max={e[-1]:.4f}")
# test with periodic BC on torus length T=multiple of both a and beta: T=6? 6/0.5=12, 6/beta=11 -> T=6 works: indices mod N
T=6.0; delta=1/22; N=int(T/delta); xs=np.linspace(0,T-delta,N)
P=np.zeros((N,N))
for k in range(-7,8):
    g=Gk(k,xs)
    if np.max(np.abs(g))<1e-15: continue
    shift=int(round(k*beta/delta))
    for j in range(N):
        P[j,(j-shift)%N]+=binv*g[j]
print("periodic herm err",np.max(np.abs(P-P.T)))
ep=np.linalg.eigvalsh(P)
print("periodic: min=%.6e max=%.6f #( <0.01)=%d #( <0.1)=%d #( <0.5)=%d"%(ep[0],ep[-1],np.sum(ep<0.01),np.sum(ep<0.1),np.sum(ep<0.5)))
print(ep[:12])
