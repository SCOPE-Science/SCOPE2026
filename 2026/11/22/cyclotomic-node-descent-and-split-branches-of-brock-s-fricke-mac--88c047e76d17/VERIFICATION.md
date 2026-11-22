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

# Verification record

The `verify_brock_octic.py` file is an executable exact-arithmetic verifier (Python with SymPy). It was run successfully against the packaged source, printing `BROCK_OCTIC_NODE_GALOIS_AND_BRANCH_CERTIFICATE_OK`. Checked identities include the two singularity-elimination factorizations, the resultant \(392\), the genus-one discriminant \(2^{12}7^2\), smoothness of the tangent cones, the rational diagonal-node substitutions, the irreducible coordinate polynomial factors of degrees \(2,6,6\), the seventh-root quadratic Gauss sum, and all six Frobenius multiplier permutations. Exhaustive affine singular-point scans over twelve explicitly listed auxiliary prime fields agree with the predicted rational counts.

The universal proof does not depend on the finite scans: it uses polynomial identities valid in all characteristics other than two and seven, the seventh-power Kummer argument at an infinite place of a smooth genus-one quotient, and cyclotomic Galois action. No assertion is made for either excluded characteristic. A machine test is not an independent mathematical audit, and the external literature search does not independently certify historical priority.
