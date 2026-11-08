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

# Verification and scope

The included `verification/verify.py` was executed with Python and SymPy and produced `verification/output.txt`. Checks comprise the exact symbolic determinant and all derivatives for sizes \(3\) and \(4\) in characteristic \(2\), the complete \(\mathbb F_2\)-point rank and Gauss incidence checks at these sizes, the two-dimensional alternating-normal congruence transformation, and exact Grassmannian coefficient extraction giving the rank-two four-by-four degree \(10\). The recorded run ended in `ALL_CHECKS_PASSED`.

For arbitrary \(n\), correctness rests on the written proofs: the adjugate identity, smooth kernel-incidence fibration, the Schur complement, the kernel-frame transition and the projective-bundle integral. Finite enumerations alone cannot establish the infinite-parameter statement. The proof identifies no global associated-primary decomposition along corank \(\ge3\); possible lower-dimensional embedded structure is deliberately left open. Historical priority is provisional, and no independent audit has been performed.
