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

The analytic proof establishes the complete finite angular orbit, its reachability using positive-probability Feres branches, irreducibility, exact nearest-angle geometry, Liouville class weighting, and the resulting change-of-variables formulas. The proof relies on the branch definitions and invariant Liouville law stated in the cited originating papers, not on empirical sampling.

Run `python3 check_caustic.py` from this directory. It uses the Python standard library and checks all integer \(n\) from \(7\) to \(50\), including explicit angle-orbit cardinalities and positivity of angle domains, direct unsigned minimum radius, trigonometric orbit-weight sums, probability normalization, 19 cumulative-probability evaluation points per \(n\), and first and second moments by Simpson quadrature. At authoring time it passed 14,036 direct cases, 44 normalization checks, and 88 moment checks.

These finite calculations do not certify the infinite theorem, all floating-point error claims beyond the stated numerical tolerances, or novelty. No external independent verification or expert audit has been performed. The physical radius is defined by the unsigned Euclidean distance \(\lvert\cos\theta\rvert\), not by a signed oriented cosine.
