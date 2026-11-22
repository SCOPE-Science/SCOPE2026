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
# Computational verification and scope

Run `python3 verify_cayley_boundary.py` using the Python standard library. The program verifies the six base points and three diagonal lines in explicit projective coordinates, checks that the diagonal intersection points are distinct, forms the thirteen divisor classes and intersection graph, and evaluates exact determinant/characteristic polynomial/modular ranks. Three different roots of the graph give the same determinant and prime-local ranks.

Expected output is provided in `verification_output.txt`, and the key assertion is `CAYLEY_13_CURVE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK`.

These calculations are finite and exhaustive for the explicit thirteen-vertex graph. The complete geometric configuration and the conditional Néron interpretation are established in the mathematical proof, not inferred from a finite search or a software log. No independent audit has been performed.
