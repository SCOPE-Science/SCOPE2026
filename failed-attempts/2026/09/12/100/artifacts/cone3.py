"""Backward cone via charts: bound D(P^{-1}) perturbation directly by FD of inverse map via implicit solve."""
import numpy as np
DP=np.load('output/artifacts/DPstar.npy');xstar=np.load('output/artifacts/xstar.npy')
ev,V=np.linalg.eig(DP)
iu=np.argmax(np.abs(ev));is_=1-iu
eu=np.real(V[:,iu]);eu/=np.linalg.norm(eu);es=np.real(V[:,is_]);es/=np.linalg.norm(es)
S=np.column_stack([eu,es]);Si=np.linalg.inv(S)
lamu=abs(float(np.real(ev[iu])));lams=abs(float(np.real(ev[is_])))
print("lamu",lamu,"lams",lams)
# forward cone check (done). For backward: instead of perturbing inverse, use forward characterization:
# stable cone Ks(gamma)={|xi|<=gamma|eta|} is backward invariant iff complement Ku is forward invariant
# under invertible D (standard cone criterion). Since D is invertible and Ku(gamma') forward invariant
# for suitable gamma' related by... Simpler: certify expansion of eta-component directly:
# for v in Ks: |eta'|>= (|lams|^{-1}... no.
# Direct approach: certify the stable manifold contraction FORWARD: for v in Ks(gamma),
# |eta'| >= lam_s_back |eta| with lam_s_back>1 means forward |.| grows?? No: forward stable contracts.
# Standard: need D^{-1} expands Ks. Equivalent: D contracts the stable cone's eta? Let's just directly
# compute DPi = inv(DP) and bound its Lipschitz from forward Lipschitz via identity:
# DPi(y)-DPi(y*) with y=P(x): DPi(y) = D(x)^{-1}, so |DPi(y)-DPi(y*)| <= |D(x)^{-1}||D(x*)-D(x)||D(x*)^{-1}|
# in STD coords: <= L r /(smin (smin - Lr)). smin=0.0796 too small -> useless since DP nearly singular? No:
# DP has det 1.0009? check.
print("det DP:",np.linalg.det(DP))
# det should be ~1 for area-preserving section? det=1.0009 yes. smin=0.0796 because lamu=8.22 stretches.
# The inverse perturbation bound blows up due to 1/smin^2 ~ 158. Alternative: certify backward cone in the
# ADAPTED norm where D ~ diag. In eigenbasis, D0=diag(8.22,0.1217), whose inverse is diag(0.1216,8.215).
# Perturbation of inverse in eigenbasis: Etilde with |Etilde|<=e=0.1086 (r=0.001). Inverse of (D0+E):
# (D0+E)^{-1} - D0^{-1} = -(D0+E)^{-1} E D0^{-1}; bound <= e |D0^{-1}| |(D0+E)^{-1}|.
# |D0^{-1}|=8.215, |(D0+E)^{-1}| ~ 1/(0.1217-ish?) NO: smallest eig of D0+E is ~0.12 -> inverse norm ~8.2.
# So bound ~ e*8.2*8.2 ~ 7.3 at r=0.001. Still big vs backward expansion 8.215? borderline.
# Reduce r to shrink e: try r=2e-4,5e-4.
L=40.0;kappa=np.linalg.norm(Si,2)*np.linalg.norm(S,2)
print("kappa",kappa)
for r in [1e-4,2e-4,3e-4,5e-4,1e-3]:
    e=L*r*kappa
    nD0i=1/lams  # =8.215 operator norm of D0^{-1}
    # bound |(D0+E)^{-1}| <= 1/(1/|D0^{-1}|... use 1/(smin0 - e), smin0=lams=0.1217
    s0=lams
    if e>=s0: print(f"r={r} e={e:.4f} TOO BIG"); continue
    Ni=1/(s0-e)
    dInv=Ni*e*nD0i
    ei=dInv  # already in eigenbasis coords
    print(f"r={r} e={e:.4f} dInv={dInv:.4f}")
    for gmm in [0.1,0.2,0.3]:
        num=(1/lamu)*gmm+ei*(1+gmm);den=(1/lams)-ei*(1+gmm)
        mu=(1/lams)-ei*(1+gmm)
        print(f"   g={gmm}: slope_back={num/den if den>0 else np.inf:.4f} mu_back={mu:.3f} OK={num/den<=gmm and mu>1.5}")
