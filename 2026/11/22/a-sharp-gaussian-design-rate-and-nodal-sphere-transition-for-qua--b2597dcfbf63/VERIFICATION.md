---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For d≥1, a≥0 and c,D,s>0, distributional stationarity forces a unique source even among Borel measures: q=p−(L*p)/r. Gaussian differentiation gives (L*p)/p=cs[dθ+(d+2−θ)y−y²]. Its integral against p is zero since E[y]=d and E[y²]=d(d+2). Maximization over y≥0 gives y_*=(d+2−θ)_+/2 and the stated sharp positive rate. Strictly below it the forced continuous density is negative on an open set. Completing the square, or factoring out y if the maximum is at zero, gives the positive-radius shell (two points if d=1), fourth-order origin zero, and quadratic origin zero in exactly the stated regimes. For sufficiency the conservative diffusion has a well-posed martingale problem; one can also identify the invariant last-reset resolvent directly. For compactly supported smooth f let M(t)=∫p P_t f. The dissipative drift gives contraction for synchronous diffusion starts, so P_t f has bounded gradient; applying the backward equation with a cutoff and Gaussian tails gives M'(t)=∫(L*p)P_t f. Thus r∫exp(−rt)∫q P_t f dt=∫exp(−rt)(rM−M')dt=M(0). This argument needs no assumption of a semigroup preserving C₀. Common resets give uniqueness. The quartic polynomial tilt is nonconstant for finite r and is not a Gaussian density ratio; the exact optimization also gives the claimed cs d²/4 leading asymptotic and the harmonic variance obstruction. The supplied VERIFICATION.md and verify_quartic_reset.py were inspected, not run; reported finite moment checks are not the stationarity or dimension proof.

## originality

PASS

The distributed-reset forward equation and its inverse rearrangement are not original. The assessed result is the exact nonlinear quartic-trap, isotropic Gaussian feasibility diagram, including its rate scaling and specific nodal boundaries. The strongest retrieved antecedents cover Gaussian targets with linear drift or analogous boundary geometry for a different target and drift, not the stated diagram.

## value

PASS

This gives an exact feasibility benchmark for a natural nonlinear perturbation of the harmonic trap: the variance obstruction of the harmonic model disappears, but the critical intervention rate grows quadratically with dimension and the forced density can first fail at a nonzero radius. Those features require a global positivity analysis and cannot be read off from moment matching or the existence of a distributed-reset forward equation. Value lies in the model-specific sharp diagram, not in maximizing a quadratic as a standalone exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
