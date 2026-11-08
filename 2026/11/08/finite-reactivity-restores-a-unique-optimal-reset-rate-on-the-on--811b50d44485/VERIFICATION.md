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

The statements in `RESULT.md` were checked analytically by direct resolvent recurrence, rank-one killing, the first-reset renewal identity, rational simplification, polynomial differentiation, Descartes' rule, and the explicit \(m=1\) root. The one-sign-change property counts multiplicities and establishes uniqueness without relying on sampling. For the monotonicity statement, the positivity of \(R_m'(q)\) places the mixed optimum between the separate perfect-target and reaction-resistance minimizers; implicit differentiation then gives the strict sign.

Run `python3 checker.py` using Python 3 standard library. It prints `PASS 1949 exact/numerical assertions`: exact rational agreement of independent formulas, exact differentiation, parameter sweeps for the unique root and monotonic reactivity shift, perfect-target endpoint checks, and the explicit nearest-neighbor formula. The independent finite-interval generator tests provide numerical cross-checks only and cannot establish uniqueness on the infinite line. No independent external audit has been performed. The validation domain is the model and parameter range explicitly quantified in `RESULT.md`.
