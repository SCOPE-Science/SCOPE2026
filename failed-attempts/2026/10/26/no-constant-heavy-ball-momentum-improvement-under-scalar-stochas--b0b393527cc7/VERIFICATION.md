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

Independence closes the three covariance coordinates with a=1+β−α, α=ημ, ν=tα² and t=v/μ². Expanding the characteristic determinant yields (s+β)(s²−β²)−s(s−β)a²−s(s+β)ν. To see sharpness of the spectral radius for deterministic initial states, rank-one initial covariances span the symmetric matrices, and positivity bounds the images of bounded symmetric matrices by a multiple of the image of the identity in cone order. The trace of that image is the sum of the second moments for the two deterministic coordinate states, so it has the same exponential factor as the operator norm. At zero momentum the radius is (1−α)²+tα² with the claimed unique minimizing α. At β>0 the polynomial is negative at β, so its real root to the right suffices if β≥r=t/(1+t). For 0<β<r, divide P(r) by r(r+β), minimize the two subtracted weighted squares in α, and combine the fractions: their optimal remainder is −β²(r−β)(1−r)²/[r(r−β+2rβ)], strictly negative. Hence there is a real root above r. For stability the mean matrix must first be Schur; in its Schur region the deterministic Lyapunov sum S for E=e1 e1^T has S_11=(1+β)/[(1−β)((1+β)²−a²)]. If νS_11≥1, the full covariance map sends S to a matrix at least S. If νS_11<1, solving the perturbed Lyapunov equation with positive definite forcing I gives a positive definite witness P satisfying T(P)=P−I, so the cone map contracts strictly. This gives the exact open interval including nondecay at equality. The Bernoulli formulas follow by setting μ=p and v=p(1−p)/m.

## originality

FAIL

The scope of the headline is broader than the literal earlier Gaussian Kaczmarz theorem, but the earlier proof already proves the same spectral inequality by a formal substitution. The 2026/10/12 scalar Gaussian Resultary record's §1 matrix is identical up to coordinate order under p=2μ²/v, α=ημ and ω=β. Its §4 determinant, sign and discriminant proof works verbatim for every real p>0; no Gaussian or integrality assumption enters it. The exact all-initial stability interval is also directly stated for strictly positive IID curvatures in the 2026/10/13 Resultary record. Allowing H=0 does not change the covariance operator at matched first and second moments, and every admissible moment pair has a strictly positive two-point realization. The Bernoulli minibatch conclusions are substitutions in these already covered results. Neither the use of an all-initial uniform metric nor the presence of zero curvatures leaves a materially distinct theorem.

## value

FAIL

The contrast between optimized rate and optimized stability allowance is useful, but the proposed mathematical extension does not require a new argument or establish a new boundary: the rate proof is unchanged under a positive-real variance reparametrization and the stability proof transfers exactly by matching two moments. The Bernoulli rule and high-momentum minibatch threshold reduce to substitution and rearrangement. No valuable distinct remainder beyond these prior implications was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
