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

# Reproduction and limitations

The standalone `verify.py` computes Lagrange weights directly for stratified triples and checks exact polynomial reproduction of constants, affine functions, and quadratics. It numerically evaluates the symmetric face integral for \(K_3(1/2)\), checks the two collision residues at four decreasing positive gaps for each face, and compares seeded rare-event estimates against the coefficient at four thresholds. The exceptional two-node midpoint case is checked by direct nonnegative weights. Run `python verify.py` with Python 3 and NumPy. It prints 18 successful checks and numerical tail diagnostics.

The analytic theorem is certified here only by the written argument: independence and the full-cell uniform law yield exact triangular small-gap probabilities; a global inverse-gap bound and disjointness of small-gap events control overlooked singularities; dominated convergence derives the exact coefficient. Finite computations are not replacements for these infinite-probability arguments. The conclusion is restricted to fixed degree, exact arithmetic in the interpolation functional, deterministic evaluation location and independent sampling errors. No independent validation has been performed.
