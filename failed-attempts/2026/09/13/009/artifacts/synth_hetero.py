"""Heterogeneous-delay COMMON LKF synthesis: common window H=0.6, common (P,Q,R).
zeta1 (10-dim) = [x(t); x(t-h1); x(t-H); v1; v2], zeta2 (8-dim) = [x(t); x(t-H); v1; v2].
Objective: max(lammax(Phi1_10), lammax(Phi2_8))."""
import numpy as np, json, sys
I2=np.eye(2); Z2=np.zeros((2,2))
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
H=0.6
sys.path.insert(0,'output/artifacts')
from synth_adt import build_Phi, unpack, maxeig_sym
def Phi1_10(P,Q,R,a):
    E=np.block([[I2,Z2,Z2,Z2,Z2],[Z2,Z2,Z2,I2,Z2],[Z2,Z2,Z2,Z2,I2]])
    D=np.block([[A1,Ab1,Z2,Z2,Z2],[(1/H)*I2,Z2,-(1/H)*I2,Z2,Z2],[(1/H)*I2,Z2,Z2,-(1/H)*I2,Z2]])
    G=np.block([A1,Ab1,Z2,Z2,Z2])
    C0=np.block([I2,Z2,-I2,Z2,Z2]); C1=np.block([I2,Z2,I2,-2*I2,Z2]); C2=np.block([I2,Z2,-I2,6*I2,-12*I2])
    e=np.exp(-2*a*H)
    Phi=E.T@P@D+D.T@P@E+2*a*(E.T@P@E)
    Phi+=np.block([[Q,Z2,Z2,Z2,Z2],[Z2,Z2,Z2,Z2,Z2],[Z2,Z2,-e*Q,Z2,Z2],[Z2,Z2,Z2,Z2,Z2],[Z2,Z2,Z2,Z2,Z2]])
    Phi+=(H**2)*(G.T@R@G)
    Phi-=e*(C0.T@R@C0+3*C1.T@R@C1+5*C2.T@R@C2)
    return 0.5*(Phi+Phi.T)
def obj(th,a):
    P,Q,R=unpack(th)
    f1=maxeig_sym(Phi1_10(P,Q,R,a)); f2=maxeig_sym(build_Phi(A2,Ab2,H,a,P,Q,R))
    return max(f1,f2),f1,f2
def search(a,iters=25000,sigma0=0.12,seed=0):
    rng=np.random.default_rng(seed); best=None; bestf=np.inf
    th=np.zeros(27); th[0],th[7],th[13],th[18],th[22]=1.,1.,1.,1.,1.
    th[21]=0.7; th[23]=0.7; th[24]=0.3; th[26]=0.3
    cur=th.copy(); curf,_,_=obj(cur,a)
    for it in range(iters):
        sig=sigma0*(1.-it/iters)+0.002
        prop=cur+sig*rng.standard_normal(27)
        f,_,_=obj(prop,a)
        if f<curf:
            cur,curf=prop,f
            if f<bestf: bestf,best=f,prop.copy()
    return best,bestf
if __name__=="__main__":
    a=float(sys.argv[1]) if len(sys.argv)>1 else 0.3
    s0=int(sys.argv[2]) if len(sys.argv)>2 else 200
    out=sys.argv[3] if len(sys.argv)>3 else "output/artifacts/synth_hetero_a03.json"
    bf,bo=np.inf,None
    for s in range(8):
        b,f=search(a,seed=s0*100+s)
        print(f"restart {s}: {f:.4f}",flush=True)
        if f<bf: bf,bo=f,b
    P,Q,R=unpack(bo); f,f1,f2=obj(bo,a)
    json.dump({"alpha":a,"maxeig":f,"mode1":f1,"mode2":f2,
      "minP":float(np.linalg.eigvalsh(P)[0]),"minQ":float(np.linalg.eigvalsh(Q)[0]),"minR":float(np.linalg.eigvalsh(R)[0]),
      "P":P.tolist(),"Q":Q.tolist(),"R":R.tolist()},open(out,"w"))
    print(f"A={a} OVERALL={f:.4f} M1={f1:.4f} M2={f2:.4f}")
    print("FEASIBLE" if f<-1e-6 else "NOT_FEASIBLE")
