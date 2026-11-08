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

# Reproduction

Run `python3 verify_coupling.py` from the extracted package directory, using only the Python standard library. The checker constructs every quadratic-form output from a symmetric integer matrix, enumerates all twenty-four permutations of its four sign classes for multiple rational/integer cases, and recalculates exact marginal variances, couplings, the \(31\)-fold variance contrast, and the strict three-dimensional optimality obstruction. Compare its stdout to `verification_output.txt`.

The finite verification does not establish the universal theorem by itself. The proof uses a complete four-class reduction of every three-dimensional Rademacher coupling, rearrangement, and the full set of six order differences. Exact positive definiteness of the example follows from strict diagonal dominance. Only self-review has been performed; independent audit has not been performed.
