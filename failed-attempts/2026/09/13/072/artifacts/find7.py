"""Newton search for order-7 (a:b:c) with fixed group law. Unknowns (a,b) in C (c=1)."""
import numpy as np, sys
sys.path.insert(0,"output/artifacts")
from hesse_grouplaw import pnorm,F,mul,peq,O
def res(v):
    a=v[0]+1j*v[1]; b=v[2]+1j*v[3]; c=1.0
    if abs((a**3+b**3+c**3)**3-27*(a*b*c)**3)<1e-4: return np.array([1e3]*6)
    P=np.array([a,b,c])
    try: Q=mul(7,P,a,b,c)
    except Exception: return np.array([1e3]*6)
    if not np.all(np.isfinite(Q)): return np.array([1e3]*6)
    cr=np.cross(pnorm(Q),O); n=np.max(np.abs(Q))
    return np.array([cr[0].real,cr[0].imag,cr[1].real,cr[1].imag,cr[2].real,cr[2].imag])/max(n,1e-30)
rng=np.random.default_rng(21)
found=None
for trial in range(30):
    v=rng.normal(size=4)*1.5
    lam=1e-3
    for it in range(200):
        r=res(v); n=np.linalg.norm(r)
        if n<1e-12: break
        J=np.zeros((6,4)); h=1e-7; ok=True
        for j in range(4):
            dv=np.zeros(4); dv[j]=h
            rp=res(v+dv); rm=res(v-dv)
            if not (np.all(np.isfinite(rp)) and np.all(np.isfinite(rm))): ok=False; break
            J[:,j]=(rp-rm)/(2*h)
        if not ok: break
        A=J.T@J+lam*np.eye(4); g=J.T@r
        try: step=np.linalg.solve(A,g)
        except Exception: break
        v2=v-step
        if np.linalg.norm(res(v2))<n: v=v2; lam*=0.5
        else: lam*=2.0
        if lam>1e6: break
    n=np.linalg.norm(res(v))
    print(trial,f"res={n:.2e}")
    if n<1e-9:
        a=v[0]+1j*v[1]; b=v[2]+1j*v[3]
        P=np.array([a,b,1.0])
        ords=[peq(mul(k,P,a,b,1.0),O) for k in range(1,9)]
        if all(o>1e-4 for o in ords[:6]) and ords[6]<1e-8:
            found=(a,b); print("ORDER-7:",a,b,"ords:",ords); break
        else: print("  torsion order:",[round(float(o),4) for o in ords])
print("found:",found)
if found: np.save("output/artifacts/order7abc.npy",np.array(found))
