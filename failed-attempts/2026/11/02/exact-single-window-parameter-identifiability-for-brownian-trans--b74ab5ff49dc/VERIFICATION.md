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

For the stationary reset mobility, the generator sends w² to 2Λ²−αw² and w⁴ to 12Λ²w²−αw⁴. Thus E[D]=2Λ²/α and Var(D)=20Λ⁴/α²; the centered quadratic is an eigenfunction at −α, giving the stated exponential covariance. Conditional Gaussianity gives V=2E[H] and K=Var(H)/(E[H])² for H=∫D, and the conditional radial fourth moment is 4d(d+2)H². Integration yields K=10∫₀¹(1−u)exp(−zu)du, strictly decreasing with limits 5 and 0, so V and K identify both positive parameters at any known t>0. For disjoint windows the conditional increments are independent even for the same coordinate, so integrating the diffusivity covariance over the two windows gives the stated squared-increment covariance, including τ=h. The no-reset kernel follows by a Gaussian-in-w ansatz in Feynman–Kac; first-reset renewal gives the quotient with its denominator positive at s>0. Regenerative averaging of the integrated diffusivity gives the Gaussian limit. The bounded independent comparisons in /workspace/branches/frozen_math_replay.py (argument 5) passed; the uploaded script was inspected, not executed. The claim concerns ensemble moments, not measurement from one realized increment.

## originality

FAIL

The distinct same-model Resultary Gaussian–Weibull record, Proof §§1–3, contains the exact variance, strictly monotone kurtosis curve with both endpoints (in the convention 3K), and the exponential squared-mobility covariance under the identical stationary and partial-reset assumptions. Its variance and strict bijection immediately give the proposed one-window inverse; its conditional Gaussian representation and covariance immediately give the disjoint-window formula and dimension-independent radial normalization. This is demonstrable coverage of the scientific claim, not a finding that the matching catalogue entry was published before the frozen one. The 2022, 2024 and 2016 primary papers inspected separately cover ingredients or general identities, not this entire model-specific calculation.

## value

FAIL

Inferring hidden diffusivity parameters from position moments is well motivated and the stationary formulas are useful. But the claimed incremental result in the frozen form supplies no distinct exact invariant once the same-model variance, invertible excess-kurtosis curve and diffusivity covariance are known: the inverse and observables follow by solving for the scale, Gaussian normalization and elementary integration. No separate finite-sample or new-regime result survives in the submitted claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
