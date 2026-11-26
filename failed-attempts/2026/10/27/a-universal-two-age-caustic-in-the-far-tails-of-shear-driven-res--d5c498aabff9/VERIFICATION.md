---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Poisson regeneration gives a unique stationary law with exponential age and the Gaussian mixture of RESULT.md, with Var(Y)=2t, Cov(X,Y)=t², Var(X)=2δt+2t³/3. The determinant 4δt²+t⁴/3 is positive even at δ=0. Conditional on Y=L, X has mean tL/2 and variance t³/6+2δt, so at t=Ls the exact exponent including resetting is L[s+1/(4s)+(c−s/2)²/(s³/3+4δs/L²)]. This is LF_c+O(L⁻¹) locally uniformly and the scaled Gaussian prefactor is √3/(2πLs²)(1+O(L⁻²)). At small ages the transverse exponent L²/(4t) and prefactor bound proportional to t⁻² give an exponentially negligible tail once ε is small enough; at large ages e^(−t) gives the other localization. F'_c=1−(s−3c)²/s⁴ gives the young minimum and, for c<1/12, the old minimum and a separating maximum. At 1/12 the merged old critical point does not minimize. Equality of branch costs and d=v−u=u²+v² imply d(1/(uv)−4)=2 with uv=(d−d²)/2, hence d=1/2. This gives c*=√3/24 and J(c*)=√3. The young cost diverges at zero, and it is lower near the old-branch fold; uniqueness of the equality fixes the ordering for all c>0. Evaluating ∂_cF at the two nondegenerate saddles gives the stated slopes. Laplace's formula gives the sharp density and, applied with bounded continuous age tests, the mixture; the Hessian and amplitude ratio is √(v/u)=√(2+√3). The density posterior uses the canonical Gaussian-mixture version. The argument is for finite δ≥0 and c>0 fixed, not a shrinking ray window. Replay: RESULT.md lines 31–62. VERIFICATION.md and checks/checker.py were inspected, not executed.

## originality

FAIL

A distinct indexed result, Resultary b065d0aa90c8, explicitly gives the same two-saddle limiting action, unique exchange and exact implicit threshold; its exact age kernel and uniform compact perturbation also imply the submitted fixed-diffusivity sharp asymptotic and mixture. This goes beyond a shared model, matching number, or possible overlap. Reparameterization and the elementary exact evaluation of its root, saddle derivatives and weights account for the remaining formulas. This is a coverage judgment relative to the inspected record, not a claim about historical precedence, copying, or chronology.

## value

FAIL

Age coexistence is a meaningful rare-event phenomenon, but the inspected coverage already supplies the competition, threshold equation, exact kernel and saddle-weight law that give it scientific significance. The remaining additions are radical evaluations and the direct fixed-noise scaling of the same formulas; they do not establish an independent unknown invariant, new regime of competition, or quantitative critical-window result. No repaired finding is being submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
