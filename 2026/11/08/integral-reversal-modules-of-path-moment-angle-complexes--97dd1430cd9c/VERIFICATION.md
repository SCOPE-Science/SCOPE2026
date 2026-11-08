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

The reproducible standalone checker is `path_moment_verification.py` (Python 3 standard library only). It enumerates all 524,264 nonempty supports in paths with 3 through 18 vertices and verifies their induced-component cohomology ranks, exact closed integer module multiplicities, signed cellular Lefschetz supertraces, reversal trace formulas, and finite-quotient rational ranks. For sizes 3 through 10 it separately checks the cellular-to-augmented-simplicial integral cochain differential and reversal sign identities for every support and admissible face. For sizes 3 through 9 it corroborates the induced-forest incidence ranks by modular elimination.

The proof of the infinite-family theorem is mathematical: the signed integral support decomposition reduces every summand to a quotient of the free module on forest components; an explicit integral basis splits each symmetric component quotient into regular and sign modules. The computational checks do not replace or extend that proof, and do not establish publication priority or independently certify the result.
