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
The embedded Python program checks exact symbolic derivative, factorization, resultant identities, and cubic Taylor coefficient with SymPy, then performs 50,331 deterministic finite numerical diagnostics using direct support optimization, extremal root comparisons, mean-width integration, critical-band probabilities and local splitting rates. It reports the exact quantitative tolerances in source. The reference execution returned PASS.

## Critical analytic checks
1. The support formula treats both the upper chord and all points on the quadratic lower boundary for every positive aspect parameter and normal direction.
2. The stationary polynomial's positive local minimum changes sign only at \(a=\sqrt2\), with a double root there; there are exactly two simple roots for larger \(a\).
3. The two envelope derivatives have strict opposing signs, ruling out missed or recurring global optimizer crossings.
4. Algebraic elimination verifies the exact two global thresholds, and Taylor expansion derives the singular mass and unfolding amplitudes.

Finite numerical checks do not certify global statements; those follow from the analytic proof. Historical priority is provisional. No independent mathematical audit was performed.
