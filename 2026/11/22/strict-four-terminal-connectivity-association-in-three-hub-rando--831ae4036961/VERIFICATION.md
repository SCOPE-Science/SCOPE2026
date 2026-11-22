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

# Reproducibility and claim boundary

Run `python CHECK.py` with SymPy installed. It constructs the exact three-hub neighborhood forest census for all symbolic peripheral sizes \(n\ge4\), checks all three partition-event numerator polynomials, proves the factorization in the theorem, and confirms each coefficient of the positivity certificate is strictly positive. It then exhaustively enumerates all edge subsets on \(K_{3,4}\), \(K_{3,5}\), and \(K_{3,6}\) to compare the three generating polynomials directly.

The observed successful output includes `NEIGHBORHOOD_POLYNOMIAL_IDENTITIES_OK`, three `EXHAUSTIVE_FOREST_CHECK_OK` entries with respective forest counts 1856, 9984 and 51712, and `ALL_K3N_FOREST_CHECKS_PASSED`.

The finite-state symbolic enumeration is exact for arbitrary \(n\) because in every forest the set of peripheral branching vertices has at most two elements, of which a pair must join different hub pairs. This reduction, rather than sampled finite sizes, supports the quantified theorem. Symbolic computation verifies the finite polynomial certificate; independent mathematical review remains unperformed.
