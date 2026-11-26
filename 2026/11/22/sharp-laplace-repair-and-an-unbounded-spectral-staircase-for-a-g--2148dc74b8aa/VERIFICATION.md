---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Integration of the base Laplace profile gives I_n=a(1−(−1)^n exp(−πa))/(π(a²+n²))>0. Write A=1−(−1)^n exp(−πa) and x=(a²+n²)^{-1}. Independently differentiating axA twice and forming I_n−a I_n′+(a²/3)I_n″ gives the ratio (a² A″−a A′)/(3A)−4a³ A′ x/(3A)+8a⁴ x²/3. It is positive at odd n; n=0 is positive by integration. At nonzero even n the sharp constraint is exactly b≥L+cx_m−hx_m². The coefficient series is absolutely summable, so no infinite Fourier sign issue is lost. The expression is L+hx_*²−h(x_m−x_*)², and since x_m↓0, some 0<x_m<2x_* gives a value above L. The lattice maximum is attained at one or both bracketing indices, or at 1 if the continuous optimum lies below that index. The adjacent difference has the sign of R_m−1 for R_m=2x_*/(x_m+x_{m+1}). The log derivative of x_* is <−2/a, whereas that of x_m+x_{m+1} is >−2/a. Thus R_m decreases from ∞ to 0 in a and increases in m for fixed a. The resulting ordered adjacent crossings are unbounded since R_m→∞ at each fixed a; the signs before and after each crossing prove the asserted set of maximizers without skips. At threshold, consecutive large frequencies give a Vandermonde system forcing any null Gram weights to vanish. The missing characters obstruct uniform RKHS density; above threshold every character belongs to the RKHS. The real bracketing index is (4aQ/π−a²)^{1/2}/2 and is asymptotic to √(a/π) exp(πa/2); x_m has mesh O((aQ)^{-3/2}) there. Multiplying the squared mesh error by h=O(a⁴) gives O(aQ^{-3}), with continuous gain π²a²/(6Q²). At small a the first mode is active and the O(a²) correction to L leaves the stated linear term unchanged.

## originality

PASS

The earlier modulated-covariance results supply a close methodological precedent for a finite active Fourier mode and a staircase. But the repaired geodesic distance-polynomial mixture has different coefficient algebra and the sharp threshold and active modes do not follow from the prior specific families. The distinct supported content is the least ratio and unbounded no-skips even-mode classification, not the general Fourier or strict-PD methods.

## value

PASS

This is a natural feasibility problem for the least rough component that repairs a standard but inadmissible covariance within a fixed matched-scale family. The high-frequency necessary bound is strictly insufficient for every a; the obstruction is a moving finite notch with no skipped even index and an exponential index law. Strict finite-site PD versus failure of universality at equality is a meaningful boundary consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
