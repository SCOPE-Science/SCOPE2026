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

# Mathematical verification

The full proof is in `RESULT.md`, and `VERIFY.py` is executable with the Python standard library. Execute `python VERIFY.py` from this directory. It checks two independently constructed finite stationary weight systems (one by an infection-count recurrence and one directly on every binary configuration), validates every single-site detailed balance equation for populations of sizes 2 through 7 at three rational importation strengths, checks the rising-factorial summation identity at rational strengths, and compares numerical finite-population distributions with the analytic limit. Successful output:

```
exact finite-state checks: PASS
asymptotic finite-size sanity checks: PASS (not a proof)
```

The infinite-population limit is established by the explicit factorization of stationary weights, the exact gamma-ratio finite sum, and rigorous uniform small-index and Gaussian-tail estimates. No finite computation is treated as an infinite proof. The analytic statement excludes exactly zero immigration in any finite system and does not address finite-time convergence or more general epidemic network structures.

The finite stationary formula was known before this work and is not asserted to be new. Independent scientific review is not yet performed.
