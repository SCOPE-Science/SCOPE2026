---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At any nonzero stationary ℓ¹ state, a=λ(1−m)>0. Irreducibility gives strictly positive coordinates, and summing yields μ−δ<a<μ. Thus the free resolvent of the mutation operator exists in ℓ¹ by a norm-convergent geometric series. Write Δ=√(μ²−4a²pq), r=(μ−Δ)/(2aq), s=(μ−Δ)/(2ap), z=√(rs). The free resolvent kernel at displacement i is r^i/Δ for i≥0 and s^(−i)/Δ for i≤0, which follows from the off-origin recurrence and the unit jump at zero. Hence one refuge requires δ=Δ. The two adjacent refuges have matching matrix (δ/Δ)[[1,s],[r,1]], whose unique positive eigenvector has ratio x₁/x₀=√(r/s)=√(p/q). Its Perron matching equation δ(1+z)=Δ is equivalent to μ+Δ−2δ=2a√(pq). The left side minus the right side decreases strictly in a; at a=μ its sign is that of μ(1+v−w)−2δ, so the root is admissible exactly at δ>δ₂. Squaring gives the stated positive a₂; the unsquared sign holds since √(μ²+4δ(μ−δ))>|μ−2δ|. The one-site condition a₁<μ is δ>μv. Both tail ratios are strictly less than one when a<μ, and at a=μ at least one is one, with both one in the unbiased case. The mass and geometric-sum normalization give exactly the unique positive profile for λ>a₂ or λ>a₁ as applicable. At the birth threshold mass is zero; at the localization threshold no positive summable state has a=μ. For 0<v<1, 1−v<√(1−v²) proves the strict rescue gap; the given example has t=4/5 and a₂=8√3/15. Supplied numerical/symbolic diagnostics were inspected but not run; these analytic checks cover the infinite lattice.

## originality

FAIL

The central biased one-versus-two result is mechanically covered by the distinct published finite-favorable-set equilibrium theorem, Resultary 8019b402a893. Its strict mortality threshold, effective birth equation, uniqueness, kernel reconstruction and mass normalization specialize to the frozen claims, not just to a similar physical model. The displayed radical and numerical example are direct evaluations of its 1×1 and 2×2 conditions. The general record is dated 2026-11-22, after the frozen record's 2026-10-18 date: this establishes coverage in the inspected catalogue, not earlier priority, and does not call the frozen result false. The zero-drift endpoint is not within that record's stated assumption p>q; at subcritical effective birth the same elementary kernels extend to it and it does not furnish the claimed directional rescue distinction.

## value

PASS

As an equilibrium theorem, an exact parameter interval in which two adjacent favorable sites permit a summable population while one fails for all birth rates is a meaningful mechanism and an informative boundary case of the infinite-trait problem. This assessment credits the scientific question and classification, not the already covered algebraic presentation as a separate contribution. The distinctness failure is decisive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
