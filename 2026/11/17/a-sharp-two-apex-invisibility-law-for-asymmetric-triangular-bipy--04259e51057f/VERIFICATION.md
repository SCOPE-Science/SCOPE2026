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

# Verification evidence and limits

Run `python3 verify.py` with Python 3.8+ and its standard library. The script independently constructs five planar projected vertices from random viewing directions and checks whether the projected upper and lower apex coordinates lie strictly inside the projected base triangle. No spherical-angle formula is used in that geometric event check. It then compares the measured frequency with the exact theorem, allowing 4.5 binomial standard errors.

Seven parameter pairs produce a total of 1,260,000 independently generated directions. Further independent midpoint quadrature integrates the normalized spherical-area density over the slope-polygon radial function for five parameter pairs, with absolute error below \(2\times10^{-8}\). Fixed-total grid comparisons also test the strict equal-height maximizer at six scales. The observed terminal marker is `ASYMMETRIC_BIPYRAMID_BOTH_APICES_HIDDEN_OK 1260000`.

These experiments and quadratures do not prove equality for all parameter pairs or directions. The analytic proof in `RESULT.md` establishes the exact geometry, area formula, fixed-total optimizer, and quadratic remainder.
