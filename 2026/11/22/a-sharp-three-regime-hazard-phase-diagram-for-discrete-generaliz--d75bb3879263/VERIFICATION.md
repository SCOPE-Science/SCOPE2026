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

Run `python check_hazard.py` with Python 3 and the `mpmath` package. The checker uses exact rational arithmetic to bound elementary logarithms in the critical-ratio separation and high-precision arithmetic for the critical exponent, sample hazard increments, and tail thresholds. It reports 238 passed assertions in the reviewed execution. Its finite parameter and count checks are diagnostic; the complete infinite-support classification rests on the four analytical proof steps in `RESULT.md`.

## Primary mathematical checks

1. Derived the exact identity \(\log[(1-h(k+1))/(1-h(k))]=B_k-tD_k\) from the published survival tail, including \(k=0\).
2. Proved strict increase in \(\beta\) of \(D_{k+1}/D_k\) using likelihood-ratio ordering of adjacent translated triangular weights.
3. Proved strict decrease of \(B_k/d_k\) using the stochastic ordering of weights proportional to \(w(u)/(k+u)\), completing \(T_{k+1}<T_k\) for \(k\geq1\).
4. Established the unique critical crossing and checked the strict initial endpoint inequality with rational log-series remainder bounds; the unique three-count equality follows.
5. Used a full asymptotic finite-difference expansion to establish the large-count turning location; numerical tables were not used to prove the infinite limit.

The checks are internal mathematical and computational review, not independent audit. No claim of formal theorem-prover certification is made.
