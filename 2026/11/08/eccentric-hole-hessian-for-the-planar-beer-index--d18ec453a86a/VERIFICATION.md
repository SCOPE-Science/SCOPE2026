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

# Verification and limits

The analytic proof in `RESULT.md` supplies the line-coordinate Jacobian, full pair-crossing integral, exact quadratic Taylor coefficient, elementary definite integrals and uniform analyticity at every fixed positive radius. A separate symbolic differentiation checked the expression for the quadratic integrand; it simplified to zero difference. The numerical executable `verify_eccentric_visibility.py` uses a smooth sine substitution in deterministic quadrature and tests \(a=0.2,0.5,0.8\). It also generates independent area-uniform point pairs, computes their segment-to-hole-center minimum distance without relying on the line integral, and compares probabilities. The executable returned `ECCENTRIC_BEER_LOCAL_HESSIAN_AND_DIRECT_SEGMENTS_OK` in the actual source directory.

Run: `python verify_eccentric_visibility.py` (Python 3 standard library only). The numerical tests illustrate the theorem but do not prove its all-radius or infinite-precision assertions. They are supplemental to the supplied elementary proof. No mathematical claim of a global hole-location optimizer, a fixed error constant uniform in radius, or a result in dimensions above two is made. Historical-priority assessment and independent audit are not performed.
