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

For the one-vector sketch, z is Gaussian with covariance K=ACρA. The planar uniform-angle integral gives E[P_z]=K^(1/2)/tr(K^(1/2))=(K+dI)/(tr K+2d), d=√det K. The trace of A²(I−E[P_z]) is exactly (1). Rank-one K at |ρ|=1 confines z almost surely to its range and gives the same formula at d=0. Differentiation in d gives (a²−b²)(a²c₁−b²c₂)/(tr K+2d)²; d is strictly decreasing in |ρ|, so the sign and minimizer claims hold including equality and the endpoints. In the standardized case the excess above κδ, δ=√(1−ρ²), is 2κ²ρ²/(κ²+1+2κδ), in [0,2]. This proves the boundedness equivalence, and the fraction tends to 2 whenever κδ has a finite limit. The frozen script and recorded verification were inspected, not executed; the log reports 935 deterministic checks, including finite quadratures and scaling checks. The verdict rests on the exact argument, not the finite samples.

## originality

FAIL

The core identity is exactly the older bivariate spatial sign covariance formula (Dürre, Vogel and Fried, 2014 public preprint, Proposition 1). Applying it to z and taking the loss trace gives (1); the phase boundary is the derivative of the resulting linear fraction and the sharp crossover is obtained by subtracting κδ and bounding the resulting fraction. The singular endpoint is the direct rank-one projector. The frozen statements are mathematically true, but the claimed extension is mechanically implied by the prior exact formula. A distinct Resultary entry gives the same nonsingular expectation via Nyström; it is later-dated and is not used to establish earlier coverage.

## value

FAIL

The phase distinction and limiting scale are useful ways to present this one-probe example, but the frozen exact claim gives only a routine specialization of the earlier planar moment and elementary consequences of its resulting rational function. No distinct exact phenomenon beyond that mechanically implied instance is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
