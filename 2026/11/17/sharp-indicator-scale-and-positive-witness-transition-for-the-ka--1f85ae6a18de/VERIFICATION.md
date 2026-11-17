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
# Verification of the centralizer indicator-gauge theorem

The mathematical proof is in `RESULT.md`. In particular, the key nonstandard step is the pointwise Lambert bound \(\min\{1,u\log(u/s)\}\le W_0(1/s)u\) for \(u\ge s\), with the separate estimate \(|u\log(u/s)|\le s/e\) for \(u<s\). The derivative of \(sW_0(1/s)\) equals \(W_0(1/s)^2/(1+W_0(1/s))\). The golden ratio is the unique positive root of \(H^2-H-1=0\). The positive restriction has an attained measure-saturation minimizer, but this does not establish an unrestricted finite-mass formula.

Run `python CHECK.py` (standard library only). It numerically compares the constructed positive costs on 299 mass points, tests 7,360 random finite-cell signed real-witness configurations, 660 signed complex-witness configurations and 6,633 scalar Lambert-envelope configurations, with deterministic seed 6079. These checks do not prove the universal inequality or rule out uninspected earlier literature. The proof and bibliographic comparison are given separately in `RESULT.md` and `REVIEW.md`.

Independent audit: not performed.
