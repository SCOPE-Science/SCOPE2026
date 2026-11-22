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

# Verification and limits

The accompanying `verification.py` is a standalone, deterministic, finite numerical check. Executed with Python, NumPy and SciPy, it passes 75 comparisons: 63 exact stopped-martingale identities over three starting positions and 21 step counts, six independent Pareto/Bessel free-kernel tail checks, and six reflected half-line tail-coefficient checks. The numerical kernel integral uses the exact expression \(e^{-a}I_k(a)\) and Pareto mixing; its finite high-rate cutoff is selected only for corroboration.

Proof verification rests on the analytic finite-sum regular variation, the fractional Fourier cusp, the monotone Fourier Tauberian theorem, the exact reflection telescoping identity, and the exact moment cutoff. Finite tests do not prove an asymptotic equivalent. The companion code does not test the long-time mean-first-passage theorem, which is a cited prior result. This package is self-reviewed only; no independent audit or third-party certificate was performed.
