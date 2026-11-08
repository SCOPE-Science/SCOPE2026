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

# Verification details

The executable `verify_multipartite_m4.py` was run directly with Python 3. It uses exact integer fourth-moment numerators, thereby avoiding floating-point tolerance and integer-overflow assumptions. It independently compares all feasible integer one-Lipschitz potentials (anchoring the first coordinate) with the formula for every integer partition of each graph order from two through eight; its equality check distinguishes the binary and one-part polarized forms. A further parameter sweep checks strict improvement of the polarized branch when the part size increases and the exact first parity-skew threshold through total order 300. It prints `ALL_MULTIPARTITE_FOURTH_MOMENT_CHECKS_OK` on success.

The analytical proof, not the finite enumeration, establishes the result for all finite orders and all allowed part-size compositions. Strict convexity and integrality reduce the continuum of real functions to the enumerated shapes for the theorem, rather than for the checker alone. The experiment does not test all real inputs, nonuniform masses, general graphs or other powers. External independent audit has not been performed.
