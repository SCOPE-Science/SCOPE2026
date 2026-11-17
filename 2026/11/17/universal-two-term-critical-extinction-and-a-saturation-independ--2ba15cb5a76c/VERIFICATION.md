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

# Verification and reproducibility

From the directory containing `RESULT.md` and `check.py`, run `python3 check.py`. It uses Python standard-library exact fractions to verify three rational instances of the critical parameter equalities, the exact coordinate update identities, the stationary-defect coefficients \(a,b\), the effective cubic and quartic map coefficients \(K,L\), and the algebraic cancellation yielding \(+1/\theta\). It then performs finite numerical orbit diagnostics from three interior initial states, with strict positivity assertions and printed convergence comparisons. These are actual reproducible checks, not an infinite-time proof.

The theorem's global positivity is proved by monotonicity of \(B(u)=(2-u)(1+cu)\), critical extinction by a reciprocal multiplier and logistic comparison, coefficient control by contracting difference equations, and the remainder estimate by summing \(v_n^{-2}\) increments. The proof is contained in `RESULT.md` and does not depend on printed diagnostic values. No independent audit or independently certified computation is claimed.
