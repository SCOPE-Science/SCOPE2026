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

# Verification record

The source directory contains `RESULT.md`, `SLOGAN.txt`, `METADATA.json`, `REVIEW.md`, `AUDIT.json`, `VERIFICATION.md`, and `checker.py`. Run `python3 checker.py` in that directory using only Python's standard library. The checker independently evaluates binomial majority tails with exact fractions, checks the two-added-voter increment identity, first-difference signs and monotone shape on rational grids, and tests the rational global-optimum witness. Recorded result: `PASS 3095 finite exact rational assertions`.

The proof itself establishes the formula for all nonnegative integers \(m\), not just tested cases. The full classification is a consequence of the monotonicity of the geometric sequence \(z^m\), and the asymptotic claim uses a fixed-interior first-order expansion. Finite checks do not establish historical originality or the infinite quantifiers. Independent validation is not performed; publication-priority risk is disclosed in `REVIEW.md` and `AUDIT.json`.
