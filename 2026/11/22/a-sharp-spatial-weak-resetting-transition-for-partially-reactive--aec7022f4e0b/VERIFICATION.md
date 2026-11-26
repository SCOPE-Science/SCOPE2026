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

In time units 1/λ the folded generator is ±s⁻¹∂a plus unit-rate heading reversal. A failed inward crossing at zero renews on the outward branch with weight exp(−ks); at the outer wall the outward lifetime adds an independent Exp(1) wait to the inward lifetime. These give g(1)=1/2, G(1)=1+f(1)−g(1), f(0)=cg(0), F(0)=cG(0) and the stated moment equations. A crossing with capture has a state-uniform positive probability in a fixed finite time block (allow an outward start time to reach the wall, reverse there, then travel inward without another reversal), so the needed moments and Taylor expansion are justified. Complete independent restarting gives right derivative −Δ/(2λ²) in physical units. Reconstructing the moment polynomials confirms the endpoints and the Bernstein signs: b0 and b1 are positive, and b1>b2>b3>b4; no ordering of b0 and b1 is needed. Descartes' rule with multiplicities and the endpoint signs give the unique simple interior crossover when the wall sign is negative. On P>0, coth(ks/2)P strictly decreases in s while Q strictly increases; P≤0 cannot furnish an extra root. At fixed s, increasing k decreases the positive product, proving strict decrease of the threshold; compactness between the strong and weak limits and the defining root equation give both limits. Integrating F and f under uniform launch and squaring only the integrated first moment gives the positive uniform susceptibility. Equality at the wall or at the crossover specifies only the first derivative; a=0 enters solely as the limiting folded value, not as an allowed restart site. The independent symbolic check reconstructed f,g,F,G from the integrals, expanded Δ, and compared the coefficients using b_j=Σ_{i≤j}[a^i]Δ·binom(j,i)/binom(4,i). This checks the identities, not the stochastic model or the sign theorem by sampling. Uploaded code was inspected but not executed.

## originality

PASS

The closest unreset process and the general restart criterion are known. Neither supplies the claimed fixed-site sign classification across all s,k>0; the endpoint polynomial and uniqueness argument are substantive additional results. No equivalent or dominating result was identified in the bounded comparisons.

## value

PASS

The exact threshold and unique change of sign identify where restarting helps or hurts in a standard confined persistent-search model. This sign information cannot be inferred from the uniform-launch benefit, and it gives an actionable distinction without claiming an optimal finite restart rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
