---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the specified centered Gaussian redraw and independent Exp(r) intervals, the renewal reward per unit time is r E[Phi(T)], not merely reward per cycle. Write a=1-c, u=2 lambda and z=r/u; adding the Gaussian KLs cancels their logarithms and gives Phi(t)=c^2(1-exp(-ut))^2/[2a(1-c exp(-ut))]. The normalized rate F=2a J/(u c^2)=z^2 L[h_c](z) has h_c(t)=(1-exp(-t))^2/(1-c exp(-t)). Geometric expansion and integration give the stated series. The curvature polynomial P_c has P_c(0)<0<P_c(1), and its derivative decreases to 4(1-c)^2>0 on [0,1]; thus h_c'' switches once from positive to negative. Twice integrating by parts gives F'=−L[t h_c'']; for the respective positive and absolute negative masses, (log(A/B))' is the later tilted mean minus the earlier one, strictly positive. Hence at most one critical point. For existence, the objective is positive inside and tends to zero at both ends (h_c tends to one at late times and is t^2/a+O(t^3) near zero); this suffices without inferring derivative signs just from equivalent asymptotics. At c=0 the normalized profile F_0 has its nondegenerate maximum at s=sqrt(2); F_1=F_0 z/(z+3), F_0''(s)=−4s/(4+3s)^2. The first implicit variation is 3(4+3s)/[2(s+3)^2]=(24+27s)/98, and max J=u(3−2s)c^2+O(c^3). Analyticity near (s,0) follows from local uniform convergence with z-derivatives of the geometric series, and global uniqueness fixes the branch. The physical optimizer is r_*=u z_*. Exact endpoints c=0,1 are excluded; in particular at c=0 the unnormalized reward is identically zero. This reconstruction does not use the frozen finite quadrature as proof and does not equate the proxy with total entropy production.

## originality

FAIL

The strongest indexed match proves uniqueness for the same finite-width Gaussian Poisson cycle reward over the entire cooling range. Changing the parameter and giving an alternative proof does not make that theorem new. The displayed weak-cooling coefficient is not printed in the closest match, but is mechanically implied by its exact objective and uniqueness: expand its kernel to first order and differentiate the nondegenerate stationarity equation. The task does not establish a distinct optimizer phenomenon outside those results.

## value

FAIL

Optimization of this endpoint proxy is motivated, but the qualitative optimizer theorem is already covered. At the nonsingular weak-cooling boundary the exact objective gives a regular, nondegenerate Taylor problem; the single coefficient is a routine deduction, with no stated new application, boundary phenomenon or independent mechanism requiring that particular coefficient. The alternate curvature proof proves the same theorem in the same regime, without a separately established new optimization result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
