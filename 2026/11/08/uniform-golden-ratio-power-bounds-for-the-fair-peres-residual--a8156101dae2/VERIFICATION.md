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

# Reproduction and scope

Use `python3 checker.py` with Python 3 and the standard library. The script independently implements the binary exhaustive Peres transformation and an exact Fraction-valued binomial recurrence; it verifies that the expected length of the residual agrees for every input length through twelve, and checks finite numerical inequalities at lengths one through 150. At the time of packaging these commands passed.

These experiments support only finitely many cases and do **not** certify the infinite claim. The all-length proof is the analytic induction in `RESULT.md`. Its nonstandard step is the global quadratic minorant for \(z^\alpha\), valid for every \(z\ge0\), which bounds the binomial Jensen deficit. The two extreme odd/even induction steps and the cases \(N=0,1\) are all treated explicitly.

This is an ordinary self-review. No independent audit or external certification has been performed. The theorem does not assert regular variation or convergence of the ratio, and it concerns mean residual length, not a deterministic bound on residual one count.
