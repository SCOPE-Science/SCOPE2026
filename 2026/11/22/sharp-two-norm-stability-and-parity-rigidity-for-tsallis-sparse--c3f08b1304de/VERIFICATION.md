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

Run `python3 verify.py` from the extracted files using Python 3.9 or later. The script contains an independent threshold-based entmax implementation, exhaustive sign-vector norms for dimensions 2 through 9, a balanced extremizer construction, deterministic random Jacobian tests, and finite-difference checks. It prints `PASS: 11040 deterministic supplementary assertions; no universal proof claimed` when all checks pass. These computations do not certify arbitrary dimensions or all real \(\alpha\). The mathematical proof is the five-part analytic argument in RESULT.md. The numerical checks use deterministic pseudorandomness and stated tolerances; no external data, internet access, or installed numerical packages are needed.

The parameter normalization, score shifts, support boundaries, and endpoints \(n=1\), \(\alpha=2\) are treated explicitly in the proof. The proof does not classify all boundary support degeneracies, and originality is based on the inspected primary sources rather than an exhaustive search of all literature. Independent audit: not performed.
