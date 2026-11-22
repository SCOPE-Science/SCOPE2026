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

# Verification procedure and evidentiary limits

Run `python3 verify_icosa_brightness.py` from the directory containing this file, with Python 3's standard library. The program builds the golden icosahedral vertices and exact supporting facets, identifies the ten antipodal face-normal generators, exhaustively enumerates the 1024 sign sums over the ordered quadratic field \(\mathbb Q(\sqrt5)\), compares all eighteen norm levels and counts, identifies the twenty maximal rays with the twenty face-normal rays, and checks the angular separation, sign-chamber containment and six-silhouette-edge conditions. All these finite checks are exact integer-pair arithmetic and strict algebraic comparisons; no floating-point test is used to decide a mathematical inequality.

The proof combines those finite certificates with Cauchy's projection-area formula, Cauchy–Schwarz for the global maximum, and the normalized area of twenty disjoint spherical caps. It covers all real thresholds in the stated interval. The script additionally reports three deterministic 65,536-direction quadrature diagnostics; these are expressly not a substitute for the infinite-quantifier proof. The certificate does not compute the distribution below the stated lower threshold, nor prove independent publication priority.

No independent mathematical audit has been performed.
