"""Refine denominator plate + scan numerator over wider (T,S,U) boxes (R1 fallback)."""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
t0=time.time()
R1=256.0; delta=1/16; N=12
phis=np.arange(N)*delta
NQ=16
zq,wq=leggauss(NQ); off=(delta/2)*zq; qw=(delta/2)*wq
PHf=(phis[:,None]+off[None,:]).ravel(); QW=np.tile(qw,N)
cP=np.cos(PHf); sP=np.sin(PHf)
sq=np.sqrt(2); Dv=np.array([1,0,1])/sq; E1=np.array([0,1,0]); Mv=np.array([1,0,-1])/sq
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
def fields(Y,chunk=10000):
    M=Y.shape[0]; St=np.zeros(M,complex); E0=np.zeros(M,complex)
    for s in range(0,M,chunk):
        Yc=Y[s:s+chunk]
        E=G(Yc[:,0:1]*cP[None,:]+Yc[:,1:2]*sP[None,:]+Yc[:,2:3])*QW[None,:]
        St[s:s+chunk]=E.sum(1); E0[s:s+chunk]=E[:,:NQ].sum(1)
    return St,E0
def box(t,s,u,ns,nt,nu,which='both'):
    zt,wt=leggauss(nt); zs,ws=leggauss(ns); zu,wu=leggauss(nu)
    T=(t[0]+t[1])/2+(t[1]-t[0])/2*zt; Wt=(t[1]-t[0])/2*wt
    S=(s[0]+s[1])/2+(s[1]-s[0])/2*zs; Ws=(s[1]-s[0])/2*ws
    U=(u[0]+u[1])/2+(u[1]-u[0])/2*zu; Wu=(u[1]-u[0])/2*wu
    TT,SS,UU=np.meshgrid(T,S,U,indexing='ij')
    W3=(Wt[:,None,None]*Ws[None,:,None]*Wu[None,None,:]).ravel()
    Y=(TT.ravel()[:,None]*Mv+SS.ravel()[:,None]*Dv+UU.ravel()[:,None]*E1)
    St,E0=fields(Y)
    o={}
    o['tot']=(W3*np.abs(St)**6).sum(); o['one']=(W3*np.abs(E0)**6).sum()
    return o
# denominator plate refinement
for cfg in [(16,20,22),(24,28,32),(32,36,40)]:
    ns,nt,nu=cfg
    print("plate",cfg,box((-280,280),(-16,16),(-40,40),ns,nt,nu)['one'],flush=True)
print("den time",time.time()-t0,flush=True)
# numerator: widen S,U coverage per T range (coarse ns,nt,nu = 12,14,14)
C=(12,14,14)
tests=[((-250,250),(-16,16),(-40,40)),
 ((-240,240),(-32,32),(-80,80)),
 ((-240,240),(16,64),(-80,80)),
 ((-240,240),(-64,-16),(-80,80)),
 ((-240,240),(-32,32),(40,160)),
 ((-240,240),(-32,32),(-160,-40)),
 ((-200,200),(-32,32),(160,240)),
 ((-200,200),(-32,32),(-240,-160)),
 ((-200,200),(64,160),(-80,80)),
 ((-200,200),(-160,-64),(-80,80))]
for (t,s,u) in tests:
    mx=max(abs(t[0]),abs(t[1]))**2+max(abs(s[0]),abs(s[1]))**2+max(abs(u[0]),abs(u[1]))**2
    o=box(t,s,u,C[0],C[1],C[2])
    print(f"T{t} S{s} U{u} inball={mx<65536} tot={o['tot']:.6f}",flush=True)
print("scan time",time.time()-t0,flush=True)
