"""R1=256 fallback certificate: disjoint t-slab lower bound (numerator),
plate + complement-box upper bound (denominator). All boxes documented vs ball."""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
t0=time.time()

R1=256.0; delta=1/16; N=12
phis=np.arange(N)*delta
NQ=16
zq,wq=leggauss(NQ); off=(delta/2)*zq; qw=(delta/2)*wq
PHf=(phis[:,None]+off[None,:]).ravel(); QW=np.tile(qw,N)
cP=np.cos(PHf); sP=np.sin(PHf)
sq=np.sqrt(2); D=np.array([1,0,1])/sq; E1=np.array([0,1,0]); Mv=np.array([1,0,-1])/sq

def G(beta):
    beta=np.asarray(beta,dtype=complex); out=np.empty_like(beta)
    sm=np.abs(beta)<1e-2; b=beta[~sm]
    e1=np.exp(1j*b); e2=np.exp(1j*b*0.5); ib=1j*b
    out[~sm]=e1*(1.0/ib+1.0/b**2)-e2*(0.5/ib+1.0/b**2)
    bs=beta[sm]; s=np.zeros_like(bs)
    from math import factorial
    for k in range(14):
        ck=(1.0-2.0**(-(k+2)))/(k+2)/factorial(k); s=s+ck*(1j*bs)**k
    out[sm]=s; return out

def fields(Y,chunk=8000):
    M=Y.shape[0]; St=np.zeros(M,complex); E0=np.zeros(M,complex)
    for s in range(0,M,chunk):
        Yc=Y[s:s+chunk]
        E=G(Yc[:,0:1]*cP[None,:]+Yc[:,1:2]*sP[None,:]+Yc[:,2:3])*QW[None,:]
        St[s:s+chunk]=E.sum(1); E0[s:s+chunk]=E[:,:NQ].sum(1)
    return St,E0

def box_int(tr,sr,ur,ns,nt_,nu,which,center_t=0.0):
    """Box in (t,s,u): t in center_t+tr, s in sr, u in ur. which: 'tot'|'one'|'both'."""
    zt,wt=leggauss(nt_); zs,ws=leggauss(ns); zu,wu=leggauss(nu)
    T=center_t+tr[1]*zt if isinstance(tr,tuple) else None
    # tr=(lo,hi)
    T=np.linspace(tr[0],tr[1],1)  # placeholder
    T=(tr[0]+tr[1])/2+(tr[1]-tr[0])/2*zt; Wt=(tr[1]-tr[0])/2*wt
    S=(sr[0]+sr[1])/2+(sr[1]-sr[0])/2*zs; Ws=(sr[1]-sr[0])/2*ws
    U=(ur[0]+ur[1])/2+(ur[1]-ur[0])/2*zu; Wu=(ur[1]-ur[0])/2*wu
    TT,SS,UU=np.meshgrid(T,S,U,indexing='ij')
    W3=(Wt[:,None,None]*Ws[None,:,None]*Wu[None,None,:]).ravel()
    Y=(TT.ravel()[:,None]*Mv+SS.ravel()[:,None]*D+UU.ravel()[:,None]*E1)
    St,E0=fields(Y)
    out={}
    if which in ('tot','both'): out['tot']=(W3*np.abs(St)**6).sum()
    if which in ('one','both'): out['one']=(W3*np.abs(E0)**6).sum()
    return out

# ---- numerator: disjoint slabs s in [-16,16], u in [-40,40], t partitioned ----
edges=np.concatenate([np.arange(-250,-40,25),np.arange(-40,41,10),np.arange(50,251,25)])
print("slab edges:",edges,flush=True)
tot_lo=0.0
for res,ns,nt_,nu in [('coarse',10,12,14),('fine',16,20,22)]:
    tot=0.0
    for i in range(len(edges)-1):
        tot+=box_int((edges[i],edges[i+1]),(-16,16),(-40,40),ns,nt_,nu,'tot')['tot']
    print(f"slabs {res}: Num6>={tot:.8f}",flush=True)
    tot_lo=tot
print("slab time",time.time()-t0,flush=True)

# ---- denominator: plate + 4 complement boxes ----
for res,ns,nt_,nu in [('coarse',10,12,14),('fine',16,20,22)]:
    plate=box_int((-280,280),(-16,16),(-40,40),ns,nt_,nu,'one')['one']
    S1=box_int((-300,300),(16,300),(-300,300),ns,nt_,nu,'one')['one']
    S2=box_int((-300,300),(-300,-16),(-300,300),ns,nt_,nu,'one')['one']
    U1=box_int((-300,300),(-300,300),(40,300),ns,nt_,nu,'one')['one']
    U2=box_int((-300,300),(-300,300),(-300,-40),ns,nt_,nu,'one')['one']
    print(f"denom {res}: plate={plate:.6e} S1={S1:.3e} S2={S2:.3e} U1={U1:.3e} U2={U2:.3e} SUM={plate+S1+S2+U1+U2:.6e}",flush=True)
print("total time",time.time()-t0,flush=True)
