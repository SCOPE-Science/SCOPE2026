"""Independent verifier for the PRESET_FALLBACK certificate (stdlib + numpy only).
Recomputes wall containment, disjoint t-slab numerator, denominator budget,
and final ratio from the spec in DRAFT.md. Prints VERIFY_OK or raises."""
import numpy as np
from numpy.polynomial.legendre import leggauss

R1=256.0; W=16.0; D1=4; N=12; delta=1/16
phis=np.array([j*delta for j in range(N)])
NQ=16
zq,wq=leggauss(NQ); off=(delta/2)*zq; qw=(delta/2)*wq
PHf=(phis[:,None]+off[None,:]).ravel(); QW=np.tile(qw,N)
cP=np.cos(PHf); sP=np.sin(PHf)
sq=np.sqrt(2); Dv=np.array([1,0,1])/sq; E1=np.array([0,1,0]); Mv=np.array([1,0,-1])/sq

# (1) wall containment: P1=(x1^2+x2^2-x3^2)^2, tube axes A_j(t)=t*m_j (cone normal line)
def q(x): return x[0]**2+x[1]**2-x[2]**2
for j,ph in enumerate(phis):
    m=np.array([np.cos(ph),np.sin(ph),-1.0])/sq
    for t in [-256.0,-100.0,0.0,100.0,256.0]:
        assert abs(q(t*m))<1e-9,(j,t)  # axis on cone up to fp trig error
# tube half-width 8: dist(p,Z)<=|transverse|<=8*sqrt2<11.4<16=R1^{1/2}
assert 8*np.sqrt(2)<16
print("wall containment OK: 12 tube axes on Z(P1); 8*sqrt2<16 transverse margin")

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

def slab(tlo,thi,ns,nt,nu):
    zt,wt=leggauss(nt); zs,ws=leggauss(ns); zu,wu=leggauss(nu)
    T=(tlo+thi)/2+(thi-tlo)/2*zt; Wt=(thi-tlo)/2*wt
    S=16*zs; Ws=16*ws; U=40*zu; Wu=40*wu
    TT,SS,UU=np.meshgrid(T,S,U,indexing='ij')
    W3=(Wt[:,None,None]*Ws[None,:,None]*Wu[None,None,:]).ravel()
    assert (250.0**2+16.0**2+40.0**2)<256.0**2  # every slab box inside B_256
    Y=(TT.ravel()[:,None]*Mv+SS.ravel()[:,None]*Dv+UU.ravel()[:,None]*E1)
    St,_=fields(Y)
    return (W3*np.abs(St)**6).sum()

edges=list(np.arange(-250,-40,25))+list(np.arange(-40,41,10))+list(np.arange(50,251,25))
num=sum(slab(edges[i],edges[i+1],16,20,22) for i in range(len(edges)-1))
print(f"numerator disjoint-slab integral = {num:.6f} (claimed 1.4850)")

def onebox(t,s,u,ns,nt,nu):
    zt,wt=leggauss(nt); zs,ws=leggauss(ns); zu,wu=leggauss(nu)
    T=(t[0]+t[1])/2+(t[1]-t[0])/2*zt; Wt=(t[1]-t[0])/2*wt
    S=(s[0]+s[1])/2+(s[1]-s[0])/2*zs; Ws=(s[1]-s[0])/2*ws
    U=(u[0]+u[1])/2+(u[1]-u[0])/2*zu; Wu=(u[1]-u[0])/2*wu
    TT,SS,UU=np.meshgrid(T,S,U,indexing='ij')
    W3=(Wt[:,None,None]*Ws[None,:,None]*Wu[None,None,:]).ravel()
    Y=(TT.ravel()[:,None]*Mv+SS.ravel()[:,None]*Dv+UU.ravel()[:,None]*E1)
    _,E0=fields(Y)
    return (W3*np.abs(E0)**6).sum()
plate=onebox((-280,280),(-16,16),(-40,40),16,20,22)
S1=onebox((-300,300),(16,300),(-300,300),16,20,22)
S2=onebox((-300,300),(-300,-16),(-300,300),16,20,22)
U1=onebox((-300,300),(-300,300),(40,300),16,20,22)
U2=onebox((-300,300),(-300,300),(-300,-40),16,20,22)
den=plate+S1+S2+U1+U2  # union bound over cover of [-300,300]^3 superset B_256
print(f"denominator budget = {den:.6e} (claimed 2.7698e-05)")
R=(num**(1/6))/(np.sqrt(12)*(den**(1/6)))
print(f"R = {R:.4f}")
assert num>=1.48 and den<=2.78e-05 and R>=2, "thresholds failed"
print("VERIFY_OK")
