---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With one vacancy, each successful clockwise particle hop moves it one longitudinal site backward at the rate of its current lane. Its lane evolves autonomously on the symmetric cycle and has the uniform stationary law. Conditional on the lane path the total longitudinal count is Poisson with the integrated lane-dependent rate, by constructing longitudinal jumps with a clock independent of the lateral motion. Integrating the stationary intensity covariance gives variance rate p̄+2⟨f,(−Q)⁻¹f⟩ for f=p−p̄. If h solves −Qh=f and dᵢ=hᵢ−hᵢ₋₁, then χ(dᵢ−dᵢ₊₁)=fᵢ, so χdᵢ=F̄−Fᵢ by periodicity and summation by parts gives the claimed formula, independent of L. Balanced binary lanes give excess (a−b)²Var(H)/(2χ), with H the sign-prefix heights. The even/odd parity split forces Var(H)≥1/4, with equality only at two adjacent heights alternating by parity. For the maximum the cycle Green kernel, verified by second differences and zero average, reduces the objective to minimizing Σ_{x<y∈S}d(K−d) over high-rate sites. In cyclic gap coordinates the consecutive-pair terms yield strict concavity, including m=2, and the only minimizers are the equivalent vertices with one gap m+1. Those blocks have heights 0 and m once each and each height in between twice, giving variance (m²+2)/12 and both stated constants and their ratio. As a separate upper-bound check, if the range of a closed ±1 path is M≤m then the two endpoints are visited at least once and each interior level at least twice. Bounding any remaining visits by squared deviation M²/4 from the midpoint gives Var(H)≤[(3m−2M)M²+2M]/(12m), strictly increasing for 0≤M≤m. At M=m each of the two arcs between a minimum and a maximum is monotone, hence exactly a block. The fresh exact-rational replay matched 18 complete-cylinder generators and all 4704 balanced layouts at K=4,6,8,10,12,14. For K=3, L=2, p=(1,2,4), χ=11/5 the mean and variance rates were 7/3 and 833/297 by both calculations.

## originality

FAIL

The sharp layout contribution has demonstrably equivalent exact coverage in a distinct indexed result for binary circular words, which in fact covers unequal multiplicities. For the indexed rotation count Rₖ of scattered 01 pairs, Rₖ₊₁−Rₖ=Kxₖ−n₁ with xₖ the high-lane indicator and n₁ its sum. Thus the lane prefix is Fₖ=(a−b)(Rₖ−R₀)/K and the variance excess is exactly 2(a−b)²Var(R)/(χK²). With n₁=K/2, the two bounds and both rigidity statements transfer with no residual optimization. The arbitrary-profile formula is the standard Markov-modulated Poisson variance law evaluated by one periodic first-difference integration. The record therefore does not establish a further materially distinct originality contribution against the inspected coverage. This is a statement-level decision, not a claim that the separately indexed result historically precedes this frozen record or that one copied the other.

## value

FAIL

The contrast between equal mean transport and different count fluctuations is well motivated, and the application gives a clear physical interpretation. But as a standalone mathematical finding the exact optimizers and their quadratic separation are transferred by a constant scaling from the already-covered circular variance theorem. The only part outside that optimization is an elementary plug-in of the total-hop intensity into standard second-moment theory and a cycle prefix sum. No independently useful exact consequence requiring a new result beyond that reduction, such as a different count or interacting-vacancy regime, was established. Thus the physically natural interpretation does not rescue the routine remainder as a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
