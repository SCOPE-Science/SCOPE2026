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

The analytical proof in `RESULT.md` supplies the all-dimensional, all-direction statement. `checker.py` uses Python 3 standard-library `fractions.Fraction` to evaluate the differentiated Lyapunov equations and compare their trace with the closed-form kernel. Executing `python3 checker.py` produced `PASS: 2043 exact rational assertions` on the packaged source.

The reproducible checks include dimensions one through six, a two-mode strict counterexample, equal-rate cases, and an exact symbolic-factor identity evaluated at a rational grid. Finite tests are not an exhaustive parameter search and do not replace the determinant factorization or analytic remainder proof. This result has undergone the self-review reported in `REVIEW.md`; no independent audit or independent validation has been performed. Earlier literature or more general Riccati sensitivity results may imply parts of the theorem.
