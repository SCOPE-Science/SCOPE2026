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

# Reproducibility and scope

Run `python3 verify.py` with Python 3 and SymPy available. The script (i) builds the complete \(ab\)-state continuous-time count generator for every \(a,b\in\{2,3,4,5\}\); (ii) solves its stationary linear equations using exact rational arithmetic; (iii) compares each exact mean and variance with the stated closed formulas; (iv) symbolically checks the underlying first-/second-moment equations and variance algebra; and (v) verifies the first twelve Beta moment recurrences. Successful output is `VERIFY_OK: 16 exact finite-chain solutions; symbolic pair equations, variance, and 12 Beta moment recurrences`.

Finite exact calculations do not by themselves establish unique recurrence for all graph sizes or the weak convergence for unbounded sizes. Those statements require the self-contained recurrent-class and stationary-generator/moment arguments in `RESULT.md`. This is a self-review with no external independent audit; no outside certification is claimed.
