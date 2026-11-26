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

Normalize the sampled column to Q and let V be a unit orthogonal complement in the column plane. With G=ΨᵀQ and H=ΨᵀV, the two Frobenius-orthogonal residual terms give T_h²=‖(I−QQᵀ)Z_h‖²_F(1+(GᵀH)²/‖G‖⁴). Given the right sketch, G,H are independent standard Gaussian k-vectors and GᵀH/‖G‖ is N(0,1) independent of ‖G‖². This conditional law is constant in the right sketch. Direct projection yields the right factor h/(cos²θ+h²sin²θ)^(1/2) with uniform quadrant angle. The beta ratio W_k/(W_k+ξ²) has parameters k/2 and 1/2, giving B_{q,k} and finiteness exactly for q<k. For q<1 the angular limit is dominated by cos(θ)^(−q); for q>1 substituting cot(θ)=hu leaves, after dividing the angular moment by h, an integrand (1+h²u²)^(q/2−1)/(1+u²)^(q/2), dominated by an integrable bound with decay u^(−min(q,2)). The beta integrals give both constants. At q=1 the displayed elliptic integral and its endpoint expansion apply, but only k>1 admits the full first moment. At q=2 the transformed angular integral is h and the chi-square inverse mean is 1/(k−2). With fixed sketches the signed orthonormal basis converges almost surely and the limiting Gaussian denominator is nonzero. The square-root RMS claim therefore holds for each k≥3 and the second moment is infinite for k≤2.

## originality

FAIL

Two earlier explicit Resultary theorems compose directly. Resultary 6a0180b3e23e, eqs. (1)–(5), applied to A=Z_hᵀ Z_h with positive eigenvalues 1,h², gives the law, exact mean h and full small-gap moment spectrum of the squared right orthogonal residual: its PSD Nyström residual is exactly Z_hᵀ(I−QQᵀ)Z_h, rank one. Resultary 23a3fc6123ad applies conditional on the right sketch with r=1, left width k, and rank-one residual, yielding 1+BetaPrime(1/2,k/2) for the squared multiplier. This conditional law is constant, hence independent of the right factor. The product, finiteness cutoff and all leading asymptotics follow with q=2s in the angular law. The elliptic-integral notation for the first moment is the defining integral under this specialization. The constant-forcing ODE is a direct realization of the same matrices, not a distinct convergence result.

## value

FAIL

The distinction between the angular moment transition and the integrability cutoff is useful, but the contribution as presented is a direct combination and parameter specialization of two known laws. Choosing constant forcing only evaluates the known distribution on the same matrices and supplies no new integrator mechanism, repeated-step statement or additional quantitative separation. No independently valuable remainder beyond the covered diagram is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
