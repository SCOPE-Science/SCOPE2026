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

# Verification

This theorem is analytically proved in `RESULT.md`, using exact radial diagonalization, the gamma integration-by-parts relation, endpoint unimodality, a strict monotone crossing, and Stirling's asymptotics. The primary nonstandard step is the global maximin classification: the zero-mode eigenvalue decreases in annulus radius and the top-band eigenvalue rises through the unique crossing, so the minimum is uniquely optimized there. The intermediate modes are strictly larger at that crossing for every integer \(K\ge2\).

Execute `python3 check_annulus.py` in a standard Python 3 environment. It performs independent scaled Simpson quadrature, bisection, endpoint and intermediate eigenvalue comparisons for \(K=2,3,10,20,100,500\) and area \(s=0.3,1,3\); it also tests off-optimal radii, additional unimodality cases, and the \(K/e\) logarithmic asymptotic. Expected final marker: `FINITE_HERMITE_ANNULUS_PASS`. The computed numbers and tolerance-bound tests are not an infinite proof, and none of the general claims rely on finite enumeration.

The original result is limited to prescribed finite Hermite bands, a normalized Gaussian analysis window, and a single concentric area-\(s\) annulus; independent audit has not been performed.
