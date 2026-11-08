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

The standalone file `verify_binary_quartic_tangents.py` is the complete finite certificate. Python 3.10+ and SymPy are required. Run `python3 verify_binary_quartic_tangents.py` from this directory.

The program constructs all \(168\) projective substitutions over \(\mathbb F_2\), partitions the \(32,767\) nonzero quartic coefficient vectors into \(279\) disjoint orbits, and tests all representatives for geometric singularities using Gröbner unit ideals in all three projective affine charts. The \(78\) smooth orbits weigh \(10,920\) equations.

For each smooth orbit, the program calculates rational points, gradients and rational tangent lines. A direct pass over all \(10,920\) smooth equations reproduces the same four joint frequencies and independently recomputes the polynomial and derivative evaluations from literal monomials; all results agree. The final success sentinel is `BINARY_QUARTIC_TANGENT_BLOCKING_CENSUS_PASS`.

The computation does not examine general fields, degrees, or geometric equivalence over extension fields. The calculation is a complete finite proof within the stated domain, not an external or independent audit. Source and historical-priority questions remain distinct from computational correctness.
