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

# Reproducible checks and their limits

Run `python3 verify.py` in the directory containing the scientific files. The script requires no third-party modules. It builds the actual integer matrices of existential incomparability of all interval-indexed types, computes the explicit integer change-of-basis columns, and checks the exact Gram congruence and the unimodular determinant for each \(0\leq n\leq9\). It also checks, for every pair of one-types when \(0\leq n\leq5\), whether adding two distinct incomparable points to the old chain yields a transitive strict order. The expected complete output is in `verification_output.txt` and ends in `ALL_CHECKS_PASS`.

The verifier was executed on the distributed source. The proof in `RESULT.md` establishes the conclusion for every finite \(n\); verification of finitely many matrices alone cannot prove an infinite statement. No outside audit, hardware attestation or independent certification is claimed.
