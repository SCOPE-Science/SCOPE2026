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

# Verification and limitations

The exact multivariate generating-function identity is derived from first-block decomposition and formal Lagrange inversion; the result follows through a nonnegative extension-ratio monotonicity proof. The proof's quantified scope is every integer n at least three and every finite multiset of positive block sizes. An impossible total size gives a zero left side. The sharpness pertains to all two-block cases and the uniform extension constant, not a separate optimality statement for each higher order.

Reproducibility: run `python3 check.py` from this package using Python 3 and only its standard library. The checker constructs every set partition by restricted growth and directly rejects crossing patterns; for sizes three through eight it verifies Catalan totals and mixed factorial-moment identities through four selected blocks. It separately checks all two-block inequalities and equality classification for three through ninety-nine points using exact fractions. The actual package replay returned `VERIFY_OK 328671 exact assertions`.

Finite checks do not certify the infinite theorem; the analytic derivation is essential. Scientific originality is assessed against the cited published generating-function literature; historical priority and independent mathematical validation remain open.
