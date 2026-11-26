---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the equal-moment opposite-sign witness

The proof in `RESULT.md` is exact: for the given finite-support laws it evaluates the excess exponential moments and reduces the differences from the fixed-gap response to two affine numerators in \(x=e^\mu\). Their ordered zeros prove the entire claimed interval, including strict positivity of the physical gaps because \(x>9/2>4\). The two response changes at \(x=5\) are exact rational numbers.

Run `python3 checker.py`. It uses standard-library rational arithmetic and checks the probabilities, mean and variance in units of \(J=\log2\), exponential excesses, thresholds and endpoint signs, witness differences, and the strict positive-gap bound. The script is not an empirical validation or a claim about arbitrary gap laws.
