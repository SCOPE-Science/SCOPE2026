"""Pinching-obstruction lemma: formal derivation + numeric check (pure numpy).

Claim (obstruction to removing Ricci mult-3 by pure-A pinching):
For every eps in (0,1/3), the scale-invariant cone K_eps = {A >= eps (tr A) I_3}
is NOT preserved by the Hamilton ODE reaction
    F(A,B) = A^2 + B B^T + 2 A^#   (A^# = adjugate/cofactor matrix),
i.e. the reaction points strictly outward at an explicit boundary point of the
cone for large traceless-Ricci coupling B. Hence no maximum-principle argument
using a pure-A pinching function can close without a bound on B (equivalently,
without control of the traceless Ricci tensor, which is exactly what the
Ricci-multiplicity-3 hypothesis supplies in the known proof).

Boundary data: tr A = 1, A0 = diag(eps, (1-eps)/2, (1-eps)/2),
B(t) = t * E_22 (matrix unit, (2,2) entry 1). Note tr F includes tr(BB^T)=t^2.
With Q(A) = A - eps (tr A) I, boundary means Q_11 = 0, and the normal
direction is E_11. Preservation would require (F - eps tr(F) I)_11 >= 0.
Computation:
  A0^2 = diag(eps^2, m^2, m^2), m=(1-eps)/2;
  (BB^T) = t^2 E_22, so (BB^T)_11 = 0 but tr(BB^T) = t^2;
  A0^# = diag(m^2, eps*m, eps*m);
  F_11 = eps^2 + 2 m^2;
  tr F = (eps^2+2m^2) + t^2 + 2(m^2+2 eps m).
Hence G(t) := (F - eps tr F I)_11 = [eps^2+2m^2] - eps*[(eps^2+2m^2)+2(m^2+2eps m)] - eps t^2
       =: c(eps) - eps t^2 -> -infinity as |t| -> infinity.
So at t* = sqrt(c(eps)/eps) the reaction is tangent and for |t|>t* points
strictly outward. QED.

Note: this is an ODE-level (reaction-term) obstruction: it shows the CONE is not
invariant under the reaction, so Hamilton's ODE-preservation criterion fails.
It does not by itself prove failure of the PDE claim; it proves the standard
pinching route cannot work and identifies B-control (= Ricci hypothesis) as
load-bearing. This is reported as an obstruction increment, not a disproof.
"""
import numpy as np
import json, os

def adj(M):
    a,b,c = M[0,0],M[1,1],M[2,2]
    # M diagonal here; adjugate diag(bc,ac,ab)
    return np.diag([b*c,a*c,a*b])

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results_obstruction.json")
E22 = np.zeros((3,3)); E22[1,1]=1.0
rec = {}
for eps in [0.05, 0.1, 0.2]:
    m=(1-eps)/2
    A0=np.diag([eps,m,m])
    F_A = A0@A0 + 2*adj(A0)
    c = float(F_A[0,0] - eps*np.trace(F_A))
    assert c>0, (eps,c)
    row=[]
    for t in [0.0,1.0,2.0,3.0,5.0]:
        B=t*E22
        F=F_A + B@B.T
        G=(F - eps*np.trace(F)*np.eye(3))[0,0]
        # closed form check
        assert abs(G-(c-eps*t*t))<1e-12,(eps,t,G,c-eps*t*t)
        row.append([t,float(G)])
    t_star=float(np.sqrt(c/eps))
    rec[str(eps)]={"c":c,"t_star":t_star,"G_paired":[row],
                   "formula":"G(t) = c(eps) - eps*t^2",
                   "outward_for":"|t| > t_star"}
    print(f"eps={eps}: c={c:.6f} t*={t_star:.4f} G={[round(g,3) for _,g in row]}")
with open(OUT,"w") as f:
    json.dump(rec,f,indent=2)
print("wrote",OUT)
