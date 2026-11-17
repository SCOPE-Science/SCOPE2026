---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

This theorem is verified analytically; no finite computation certifies the infinite-dimensional statements. The key logical dependencies are (1) the weighted norm identity under a change of variables, (2) superadditivity of least interval mass, (3) the orbit-growth criterion and approximate-generator obstruction from Huynh (2026), and (4) the explicit quantitative coercivity bound from the generator displacement, and (5) the explicitly normalized broad-bump construction on low-mass intervals.

For \(1\le p<\infty\), \(0\le a\le M\), normalized test functions satisfy
\[
 \frac{\|A_af_N\|_p}{\|f_N\|_p}
 \le\frac{\|\varphi'\|_p}{N\|\varphi\|_p}
 +\frac{M^{1-1/p}}{N^{2/p}\|\varphi\|_p}\to0.
\]
The potential mass on each supporting interval is selected below \(1/N\), which exists precisely in the failure-of-uniform-interval-mass case. The test functions vanish near both ends of their support and so satisfy the generator's zero boundary trace.

Independent elementary checks: \(\int_0^t x/(1+x)\,dx=t-\log(1+t)\), and \(\inf_{s\ge0}\int_s^{s+t}(1+x)^{-1}\,dx=0\). The first gives a nonattained maximal rate of \(1\); the second gives a kinematic-but-not-positive example. Finite \(p\), boundedness of the potential, and nonnegativity are indispensable assumptions in the presented proof.

Limit: Originality is assessed against the identified and inspected literature; a logically equivalent older theorem could have different terminology. No independent external mathematical audit has been performed.
