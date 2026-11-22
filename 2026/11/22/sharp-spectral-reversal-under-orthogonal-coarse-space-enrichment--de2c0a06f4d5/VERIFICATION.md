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

## Checks
- Exact algebra: \(E_U=S^2\) and \(E_{V_\theta}=Szz^TS\) with \(z=-\sin\theta e_2+\cos\theta e_3\).
- Nonzero rank-one eigenvalue equals \(z^TS^2z=\rho^2-\rho t\sin(2\theta)\); the other eigenvalues vanish.
- Contraction follows from \(\|S\|_2=(t+\sqrt{t^2+4\rho^2})/2<1\) iff \(t+\rho^2<1\) for positive parameters.
- Exact-rational checker: 4,003 assertions across 800 prescribed rational-angle parameter triples and the reference numerical witness.
- Floating-point tests of eigenvalues and singular values at 20 parameter-angle combinations matched the analytic formulas.

## Limits
Finite calculations are consistency tests, not an exhaustive parameter search. The uniform theorem follows from the displayed analytic rank-one factorization and exact inequality comparison. No independent mathematical audit or floating-point backward-error analysis has been performed.
