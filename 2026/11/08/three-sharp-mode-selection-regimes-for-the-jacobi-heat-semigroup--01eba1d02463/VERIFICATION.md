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

The complete analytic proof is in `RESULT.md`. It derives the exact fourth moment from the Chebyshev product identity, proves every maximization branch and equality case from a quadratic deficit, and proves uniqueness of the contractivity time by strict monotonicity.

Run `python3 verify.py` from the package root. It uses only Python standard-library exact integers and rational arithmetic. Ten degree pairs and seven rational spectral ratios per pair were tested; it reports `CHEBYSHEV_MOMENT_AND_BRANCH_EXACT_CHECKS_PASSED 140 CASES` on success. These cases check normalization, cross terms, strict mixed-branch completion of the square, and all three mode-selection regimes. They do not replace the proof for arbitrary positive integer degrees or all real times.

The result is reviewed within the same analytical process only. No independent audit or independent validation has occurred. The scope is real coefficients, opposite-parity pairs, semicircle Jacobi diffusion, and fourth-power output moments.
