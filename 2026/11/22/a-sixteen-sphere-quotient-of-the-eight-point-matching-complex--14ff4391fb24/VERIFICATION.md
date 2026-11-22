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

# Reproducibility

Run `python3 verify_m8_cyclic.py` from the directory containing this file. It requires only Python's standard library. A successful execution prints `M8_ROTATION_QUOTIENT_INTEGRAL_CHECKS_OK`.

The program exhaustively enumerates the nonempty matchings of the complete eight-vertex graph, all strict nested matching flags in its barycentric subdivision, and their orbits under the eight rotations. It checks the complete signed integer quotient boundaries, their compositions, exact integral unit-pivot reductions and several independent finite-field ranks. The counts are 763 nonempty matchings, quotient cell vector \((107,576,804,318)\), 894 integral cancellations, and residual chain-group vector \((1,0,16,0)\).

The homological computation alone does not establish simple connectivity. That step separately uses the classical connectivity theorem for the original complex and the fixed-point orbit-space theorem of Armstrong. The final homotopy equivalence uses Hurewicz and Whitehead. Neither a homeomorphism nor an all-sizes statement is verified. No external mathematical audit has been performed.
