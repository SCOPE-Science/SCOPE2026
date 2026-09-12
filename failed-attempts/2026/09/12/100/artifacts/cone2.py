"""Cone invariance + expansion/contraction with F-norm boxes + interval-style margin sweep."""
import numpy as np
DP=np.load('output/artifacts/DPstar.npy')
ev,V=np.linalg.eig(DP)
iu=np.argmax(np.abs(ev));is_=1-iu
eu=np.real(V[:,iu]);eu/=np.linalg.norm(eu)
es=np.real(V[:,is_]);es/=np.linalg.norm(es)
S=np.column_stack([eu,es]);Si=np.linalg.inv(S)
lamu=np.real(ev[iu]);lams=np.real(ev[is_])
print("lamu=%.6f lams=%.6f cond(S)=%.4f"%(lamu,lams,np.linalg.cond(S)))
# cone Ku(gamma)={|eta|<=gamma|xi|}; image slope bound for D0=diag(lamu,lams)+E, |E|<=e (F-norm coords)
# exact: xi'=lamu xi + E11 xi + E12 eta; eta'=lams eta + E21 xi + E22 eta
# |eta'|/|xi'| <= (|lams| g + e(1+g))/(|lamu| - e(1+g)) <= g  and expansion |xi'|>= mu|xi| with mu=|lamu|-e(1+g)
# same for stable cone under inverse.
L=40.0  # Lipschitz bound rounded up from 37.35
for r in [5e-4,1e-3,2e-3]:
    e=L*r*np.linalg.norm(Si,2)*np.linalg.norm(S,2)
    print(f"r={r}: E-bound e={e:.4f}")
    for gmm in [0.05,0.1,0.15,0.2]:
        num=abs(lams)*gmm+e*(1+gmm);den=abs(lamu)-e*(1+gmm)
        slope=num/den if den>0 else np.inf
        mu=abs(lamu)-e*(1+gmm)
        print(f"   gamma={gmm}: slope'={slope:.4f} (need <={gmm}) mu={mu:.3f}")
# stable cone under inverse: DPinveig = diag(1/lamu,1/lams)
DPi=np.linalg.inv(DP)
m1=1/abs(lamu);m2=1/abs(lams)
print("inv diag entries:",m1,m2)
for r in [5e-4,1e-3,2e-3]:
    e=L*r*np.linalg.norm(Si,2)*np.linalg.norm(S,2)
    ei=e/(min(abs(float(np.real(ev[0]))),abs(float(np.real(ev[1]))))**2*0.9)  # rough; compute exactly below instead
    print(f"r={r} e={e:.4f}")
# exact inverse perturbation: compute DPi at samples? Instead bound via smallest sing val
smin=np.linalg.svd(DP,compute_uv=False).min()
print("sigma_min(DP)=",smin)
for r in [5e-4,1e-3]:
    E=L*r  # operator 2-norm in std coords
    # DPi perturbation <= E/(smin(smin-E))
    Ep=E/(smin*(smin-E)) if smin>E else np.inf
    ei=np.linalg.norm(Si,2)*np.linalg.norm(S,2)*Ep
    print(f"r={r}: Ep_std={Ep:.4f} ei_eigcoords={ei:.4f}")
    for gmm in [0.05,0.1,0.15,0.2]:
        # stable direction eigenvalue 1/lams=8.215 expands backward; unstable 1/lamu=0.1216 contracts
        num=(1/abs(lamu))*gmm+ei*(1+gmm);den=(1/abs(lams))-ei*(1+gmm)
        print(f"   gamma={gmm}: slope_back={num/den if den>0 else np.inf:.4f} lam_back={1/abs(lams)-ei*(1+gmm):.3f}")
