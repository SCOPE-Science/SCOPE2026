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
# Verification evidence and scope

`python verify.py` runs entirely with Python 3's standard library. It enumerates every vertex permutation for the wheel and clique-joined-cycle test cases satisfying \(4\le n\le7\), \(1\le k\le2\), \(n+k\le8\), and compares exact rational distributions with the derived finite mixture. It separately evaluates the random-first-vertex recursion for path lengths 0 through 15, checking total probability, exact mean and second factorial moment against coefficients of the stated closed rational-exponential generating functions. It checks large-index mean and variance coefficients at three path lengths. The current package checker completes with `VERIFY_OK 68 exact-moment-and-enumeration-assertions`.

The proof, not the checker, establishes the all-parameter mixture law, complex-analytic Gaussian limit, and asymptotic moment calculations. In particular, finite enumeration does not certify limiting normality, and variance convergence is not inferred from weak convergence.

The primary scientific sources are arXiv:2009.08609 (full text, Sections II–III and Appendix A) and DOI 10.1002/rsa.21200 (full text, Sections 1–3), with arXiv:1510.05560 as background. Uninspected work could contain prior versions of the clique-joined-cycle result; independent priority and proof review have not been performed.
