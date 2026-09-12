import numpy as np, json
g=9.81
def pack(q1,q2): return np.concatenate([q1,q2])
def unpack(q): return q[:2], q[2:]
def gradU(q):
    return np.array([0.,g,0.,g])
def Gmat(q):
    q1,q2=unpack(q); d=q2-q1
    G=np.zeros((2,4))
    G[0,:2]=2*q1; G[1,:2]=-2*d; G[1,2:]=2*d
    return G
def gvec(q):
    q1,q2=unpack(q); d=q2-q1
    return np.array([q1@q1-1., d@d-1.])
def H(q,p): return 0.5*(p@p)+g*(q[1]+q[3])

def rattle_step(q,p,h):
    nU=gradU(q); G=Gmat(q)
    lam=np.zeros(2)
    a = q + h*(p-0.5*h*nU)  # q_new = a - (h^2/2) G^T lam
    for _ in range(12):
        qn = a - (h*h/2.0)*(G.T@lam)
        gv=gvec(qn); 
        if np.max(np.abs(gv))<1e-15: break
        Gn=Gmat(qn)
        J=-(h*h/2.0)*(Gn@G.T)
        try: dl=np.linalg.solve(J,-gv)
        except: dl=np.linalg.lstsq(J,-gv,rcond=None)[0]
        lam+=dl
        if np.max(np.abs(dl))<1e-14: break
    qn = a-(h*h/2.0)*(G.T@lam)
    phalf = (qn-q)/h
    nUn=gradU(qn); Gn=Gmat(qn); GGT=Gn@Gn.T
    rhs = (2.0/h)*(Gn@phalf) - (Gn@nUn)  # GGT mu = rhs? check: G phalf -h/2 G nUn -h/2 GGT mu=0
    # Actually: p_new = phalf -h/2 nUn -h/2 Gn^T mu; G p_new=0 => GGT mu = (2/h)(G phalf) - G nUn... but G phalf here means Gn@phalf
    mu=np.linalg.solve(GGT,rhs)
    # NOTE rhs above: (2/h)(Gn phalf) - Gn nUn ; since Gn phalf = (Gn(qn-q))/h
    pn = phalf-(h/2.0)*nUn-(h/2.0)*(Gn.T@mu)
    return qn,pn

def init_state(th1,th2,w1,w2):
    q1=np.array([np.sin(th1),-np.cos(th1)])
    d=np.array([np.sin(th2),-np.cos(th2)])
    q2=q1+d
    v1=w1*np.array([np.cos(th1),np.sin(th1)])
    vd=w2*np.array([np.cos(th2),np.sin(th2)])
    v2=v1+vd
    return pack(q1,q2),pack(v1,v2)

for (th1,th2,w1,w2) in [(1.0,1.2,1.5,1.0),(0.9,-0.7,1.2,-1.5),(1.1,0.4,-1.0,2.0)]:
    q,p=init_state(th1,th2,w1,w2)
    print((th1,th2,w1,w2),"H0=",H(q,p),"g=",gvec(q),"Gp=",Gmat(q)@p)

# scaling test
q0,p0=init_state(1.0,1.2,1.5,1.0)
H0=H(q0,p0)
print("H0=",H0)
res={}
for h in [0.01,0.005,0.0025]:
    T=200.0; n=int(T/h)
    q,p=q0.copy(),p0.copy()
    mx=0.0; mg=0.0
    for k in range(n):
        q,p=rattle_step(q,p,h)
        e=abs(H(q,p)-H0); mx=max(mx,e)
        mg=max(mg, np.max(np.abs(gvec(q)))+np.linalg.norm(Gmat(q)@p))
    print(f"h={h} steps={n} maxE={mx:.6e} scaled={mx/h**2:.3f} maxdef={mg:.2e}")
    res[str(h)]={"maxE":mx,"scaled":mx/h**2,"maxdef":mg}
json.dump({"H0":H0,"T":200.0,"results":res},open("output/artifacts/rattle_results.json","w"),indent=1)
