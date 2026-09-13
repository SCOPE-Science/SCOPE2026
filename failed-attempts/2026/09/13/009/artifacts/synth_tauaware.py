"""Tau-aware COMMON-(P,qI,rI) synthesis, per-mode windows (8-dim Phi each mode, own h_i).
Common P (6x6) + scalars q,r>0 shared across modes. mu via sup-norm envelopes (rigorous, code-verified):
  Vbar = lamPmax*3 + q*hmax + r*hmax^3*cD ; Vlow = lamPmin ; mu=Vbar/Vlow.
  tau_a(k*) = ln(mu)/(2(a-k*)).
Objective: minimize tau_a at fixed a,k* subject to both Phi<0 (barrier penalty)."""
import numpy as np, json, sys
I2=np.eye(2); Z2=np.zeros((2,2))
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
H1,H2,HMAX=0.3,0.6,0.6
nA=max(np.linalg.norm(A1,2),np.linalg.norm(A2,2)); nAb=max(np.linalg.norm(Ab1,2),np.linalg.norm(Ab2,2))
CD=2*(nA**2+nAb**2)
sys.path.insert(0,'output/artifacts')
from synth_adt import build_Phi, maxeig_sym
def unpack2(th):
    M=np.zeros((6,6)); idx=0
    for r in range(6):
        for c in range(r+1): M[r,c]=th[idx]; idx+=1
    P=M@M.T+1e-9*np.eye(6)
    q=float(np.exp(th[21])); r=float(np.exp(th[22]))
    return P,q*I2,r*I2
def tau_of(P,qm,rm,a,ks):
    lmn=np.linalg.eigvalsh(P)[0]; lmx=np.linalg.eigvalsh(P)[-1]
    lq=qm[0,0]; lr=rm[0,0]
    Vbar=lmx*3+lq*HMAX+lr*(HMAX**3)*CD; mu=Vbar/lmn
    return float(np.log(mu)/(2*(a-ks))),float(mu)
def obj(th,a,ks,big=1e4):
    P,qm,rm=unpack2(th)
    f1=maxeig_sym(build_Phi(A1,Ab1,H1,a,P,qm,rm)); f2=maxeig_sym(build_Phi(A2,Ab2,H2,a,P,qm,rm))
    feas=max(f1,f2)
    tau,mu=tau_of(P,qm,rm,a,ks)
    if feas<-5e-3: return tau,feas,tau,mu
    return big+feas,feas,tau,mu
def search(a,ks,iters=30000,seed=0):
    rng=np.random.default_rng(seed); best=None; bestf=np.inf; info=None
    th=np.zeros(23); th[0],th[7],th[13],th[18]=1.,1.,1.,1.; th[21]=np.log(2.); th[22]=np.log(0.5)
    cur=th.copy(); curf,_,_,_=obj(cur,a,ks)
    for it in range(iters):
        sig=0.10*(1.-it/iters)+0.002
        prop=cur+sig*rng.standard_normal(23)
        f,feas,tau,mu=obj(prop,a,ks)
        if f<curf: cur,curf=prop,f
        if f<bestf: bestf,best,info=f,prop.copy(),(feas,tau,mu)
    return best,bestf,info
if __name__=="__main__":
    a=float(sys.argv[1]) if len(sys.argv)>1 else 0.3
    ks=float(sys.argv[2]) if len(sys.argv)>2 else 0.05
    s0=int(sys.argv[3]) if len(sys.argv)>3 else 400
    out=sys.argv[4] if len(sys.argv)>4 else "output/artifacts/synth_tauaware.json"
    bf,bo,info=np.inf,None,None
    for s in range(8):
        b,f,inf=search(a,ks,seed=s0*100+s)
        print(f"restart {s}: F={f:.4f} feas={inf[0]:.4f} tau={inf[1]:.4f} mu={inf[2]:.2f}",flush=True)
        if f<bf: bf,bo,info=f,b,inf
    P,qm,rm=unpack2(bo)
    tau,mu=tau_of(P,qm,rm,a,ks)
    f1=maxeig_sym(build_Phi(A1,Ab1,H1,a,P,qm,rm)); f2=maxeig_sym(build_Phi(A2,Ab2,H2,a,P,qm,rm))
    json.dump({"alpha":a,"kstar":ks,"tau_a":tau,"mu":mu,"mode1":f1,"mode2":f2,
      "minP":float(np.linalg.eigvalsh(P)[0]),"maxP":float(np.linalg.eigvalsh(P)[-1]),
      "q":float(qm[0,0]),"r":float(rm[0,0]),"P":P.tolist()},open(out,"w"))
    print(f"A={a} k*={ks} TAU={tau:.4f} MU={mu:.2f} M1={f1:.4f} M2={f2:.4f}")
    print("FEASIBLE-IMPROVED" if (f1<-5e-3 and f2<-5e-3 and tau<6.5147) else "NOT_YET")
