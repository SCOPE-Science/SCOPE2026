"""Common-window (hmax=0.6 for both modes) common-LKF synthesis. mu=1 -> arbitrary switching."""
import numpy as np, json, sys
sys.path.insert(0,'output/artifacts')
from synth_adt import build_Phi, unpack, maxeig_sym, objective as _
A1=np.array([[-2.,0.],[0.,-0.9]]); Ab1=np.array([[-1.,0.],[-0.5,-1.]])
A2=np.array([[-1.,0.5],[0.,-1.]]); Ab2=np.array([[-1.,0.],[0.1,-1.]])
H=0.6
def obj(th,a):
    P,Q,R=unpack(th)
    f1=maxeig_sym(build_Phi(A1,Ab1,H,a,P,Q,R)); f2=maxeig_sym(build_Phi(A2,Ab2,H,a,P,Q,R))
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
    s0=int(sys.argv[2]) if len(sys.argv)>2 else 100
    out=sys.argv[3] if len(sys.argv)>3 else "output/artifacts/synth_common_a03.json"
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
