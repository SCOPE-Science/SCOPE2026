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

The paper derives the complete antidiagonal classification analytically from an explicit, strictly increasing radius map. The proof also gives full-plane Jacobian eigenvalues and the two endpoint asymptotic expansions.

The included standard-library Python checker `verify.py` executes 140 finite checks on representative parameters and initial conditions, followed by four fold-limit diagnostics. It may be run with `python3 verify.py` from the extracted directory. All universal assertions require the written inequalities in `RESULT.md` and are not inferred from finite tests. The verifier does not classify off-antidiagonal invariant objects.
