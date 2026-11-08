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

# Reproducible finite checks

The companion `verify_pms_inball.py` was run with Python 3, NumPy and SciPy. Its reported successful completion marker was:

`PMS_BICLIQUE_INBALL_HALL_AND_FACET_CHECKS_PASSED 15`

For all integer pairs \(2\le n\le6\), \(1\le s<n\) (15 total), it computed the orthogonal projection onto the affine hull and solved the corresponding linear program for the largest inscribed Euclidean ball. It compared the optimized radius with the closed formula, tested the constructed center and tangent-hyperplane counts, and verified that the two bounds are unequal. For \(n\le5\), it additionally enumerated each of the \(2^{2n}\) candidate binary vertex vectors, independently searched for perfect matchings by permutations, confirmed the equivalence to the Hall test, checked the affine span, and verified the ranks of every predicted tangent facet.

These tests do not exhaust the infinite family or independently certify the literature. The proof's Euclidean-normal computations, global upper bounds and equality cases are the mathematical justification for all dimensions. Independent mathematical audit has not been performed.
