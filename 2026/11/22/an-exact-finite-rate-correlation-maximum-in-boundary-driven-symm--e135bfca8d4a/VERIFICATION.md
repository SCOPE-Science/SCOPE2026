---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reservoir births of total population N are bounded by an affine function of N, and bulk jumps preserve N, with bounded rates on every finite set N≤m. This yields nonexplosion; the affine negative drift gives positive recurrence with irreducibility from the births and deaths. For a direct integrability justification of quadratic stationary generator identities, L exp(θN)/exp(θN) has constant term γn(ρ_A+ρ_B)(exp(θ)−1) and coefficients γ(exp(−θ)−1)+λ_X(exp(θ)+exp(−θ)−2) on shore occupations. These coefficients are strictly negative for small positive θ, giving stationary exponential integrability by the drift criterion. The mean bulk drift cancels the bilinear terms, while the centered-product jump term is negative only for adjacent distinct sites. These give the four displayed equations, including the equality of the two same-shore covariances. Put p=κv, d=γ+p. Substitution of a+b=[2pe+v(T+2e)+(B_A+B_B)/2]/d and c=pe/d into the cross equation reduces the coefficient to 2[n(d²−p²)+γv], giving exactly the stated covariance. With x=κv/γ, the derivative of x(1+x)/(1+2x)² is (1+2x)⁻³, so the full sign is the claimed cubic test; the strictly increasing cubic gives the sole positive root and its large-n limit. The absolute current grows strictly only with unequal baths; equal baths give identically zero covariance and current and no unique maximum. Read RESULT.md, VERIFICATION.md and CHECK.py; did not execute the supplied script. Its rational finite cases check the reduction but the proof covers all allowed n.

## originality

PASS

Prior SIP duality and positivity or squared-reservoir-contrast structure are not claimed new. The inspected closest theories give covariance in terms of geometry-dependent dual absorption or study different graphs and contacts. They do not provide the evaluated all-site bipartite coefficient or the finite-rate maximum and its contrast with the current.

## value

PASS

The rate is a natural control parameter for a symmetric transport network. The all-size formula determines quantitatively that greater mean transport does not imply greater cross-shore fluctuations: the current saturates monotonically while covariance peaks at an explicitly characterized finite rate and then vanishes. The within-shore ratio and large-size optimizer distinguish this from a finite example or an already-known positivity result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
