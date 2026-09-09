"""R1=256 fallback certificate workhorse: deterministic GL boxes + ray-scan tails."""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
t0=time.time()

R1=256.0; delta=1/16; N=12
phis=np.arange(N)*delta
NQ=16
zq,wq=leggauss(NQ); off=(delta/2)*zq; qw=(delta/2)*wq
PHf=(phis[:,None]+off[None,:]).ravel(); QW=np.tile(qw,N)
cP=np.cos(PHf); sP=np.sin(PHf)
print("cap area:",QW.sum()," E(0) expect:",N*0.375*delta,flush=True)

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

def fields(Y,chunk=6000):
    M=Y.shape[0]; St=np.zeros(M,complex); E0=np.zeros(M,complex)
    for s in range(0,M,chunk):
        Yc=Y[s:s+chunk]
        E=G(Yc[:,0:1]*cP[None,:]+Yc[:,1:2]*sP[None,:]+Yc[:,2:3])*QW[None,:]
        St[s:s+chunk]=E.sum(1); E0[s:s+chunk]=E[:,:NQ].sum(1)
    return St,E0

# freq convergence at probe points
Yp=np.array([[0,0,0],[5,3,-4],[0,0,100],[70.7,0,-70.7],[0,0,250]])
for nq in [10,16,24]:
    z,w=leggauss(nq); o=(delta/2)*z; q2=(delta/2)*w
    P2=(phis[:,None]+o[None,:]).ravel(); W2=np.tile(q2,N)
    c2=np.cos(P2); s2=np.sin(P2)
    E=G(Yp[:,0:1]*c2[None,:]+Yp[:,1:2]*s2[None,:]+Yp[:,2:3])*W2[None,:]
    print("NQ=",nq,"Stot=",np.abs(E.sum(1)),flush=True)

def gl_cube(a,n):
    z,w=leggauss(n); x=a*z; wx=a*w
    X,Yg,Z=np.meshgrid(x,x,x,indexing='ij')
    W3=(wx[:,None,None]*wx[None,:,None]*wx[None,None,:]).ravel()
    Y=np.stack([X.ravel(),Yg.ravel(),Z.ravel()],1)
    St,E0=fields(Y)
    return (W3*np.abs(St)**6).sum(),(W3*np.abs(E0)**6).sum()

for n in [40,48,56]:
    It,I0=gl_cube(32,n); print(f"cube a=32 n={n}: Itot={It:.8f} I0box={I0:.6e}",flush=True)
print("cube time",time.time()-t0,flush=True)

# plate box for single packet 0: s along d=(1,0,1)/2^.5, u along e1=(0,1,0), v along m=(1,0,-1)/2^.5
sq=np.sqrt(2); D=np.array([1,0,1])/sq; E1=np.array([0,1,0]); Mv=np.array([1,0,-1])/sq
def gl_plate(sr,ur,vr,ns,nu,nv):
    zs,wz=leggauss(ns); zu,wu=leggauss(nu); zv,wv=leggauss(nv)
    S=sr*zs; U=ur*zu; V=vr*zv
    SS,UU,VV=np.meshgrid(S,U,V,indexing='ij')
    W3=((sr*wz)[:,None,None]*(ur*wu)[None,:,None]*(vr*wv)[None,None,:]).ravel()
    Y=(SS.ravel()[:,None]*D+UU.ravel()[:,None]*E1+VV.ravel()[:,None]*Mv)
    _,E0=fields(Y)
    return (W3*np.abs(E0)**6).sum()
for cfg in [(16,40,280,48,32,24),(16,40,280,64,48,32),(16,40,280,80,64,40)]:
    print("plate",cfg,"I0=",gl_plate(*cfg),flush=True)
print("plate time",time.time()-t0,flush=True)

# ray scans (both fields), fibonacci dirs
rng=np.random.default_rng(11); Dd=3000
ga=np.pi*(3-np.sqrt(5)); kk=np.arange(Dd)
th=ga*kk; zy=1-2*(kk+0.5)/Dd; rr=np.sqrt(1-zy*zy)
Dirs=np.stack([rr*np.cos(th),rr*np.sin(th),zy],1)
radii=np.concatenate([np.linspace(1,40,20),np.linspace(45,256,30)])
St_list=[]; E0_list=[]
for r in radii:
    St,E0=fields(Dirs*r); St_list.append(np.abs(St)); E0_list.append(np.abs(E0))
StA=np.array(St_list); E0A=np.array(E0_list)
Smax_tot=StA.max(1); Smax_0=E0A.max(1)
Smean_0=(E0A**6).mean(1)
print("r : max|Etot| max|F0| mean|F0|^6",flush=True)
for i in range(0,len(radii),7):
    print(f"{radii[i]:6.1f} {Smax_tot[i]:.4e} {Smax_0[i]:.4e} {Smean_0[i]:.3e}",flush=True)
np.savez("artifacts/rays_R1.npz",radii=radii,Smax_tot=Smax_tot,Smax_0=Smax_0,Smean_0=Smean_0)
print("total time",time.time()-t0,flush=True)
