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

Independently checked with an angular-generator martingale. Write U=R(φ)b, g=b−U, and D_t=Σ_reset g(φ_−). The shared Stratonovich integral on a continuous excursion is g(φ_t), so X_t=M_th+D_t+g(φ_t), with the residual translation martingale driven independently. The angular generator A satisfies Ag=δb−(r+δ)g. With H=rg/(r+δ), D_t+H(φ_t)−H(φ_0)−vt is a martingale for v=rδb/(r+δ); its reset jumps are δg/(r+δ) and its continuous angular-noise coefficient is −√(2δ)rJU/(r+δ). The bounded end corrections do not affect the covariance rate. The stationary cosine moments are a_j=r/(r+jδ) for harmonics 1 and 2 at j=1 and 4, and sine moments vanish. The two angular bracket contributions to the contrast, divided by |b|², are 2δ[r/(r+δ)]²a_4 and r[δ/(r+δ)]²(−a_4−1+2a_1); their sum simplifies to the claimed cubic expression. Averaging 2ΘRCRᵀ over the same angle law yields the stated thermal term, with zero cross bracket. Equivalently, conditioning the centered cycle reward on its duration gives the isotropic term (1−a_4)|b|²/(2μ) and rank-one coefficient (a_4−a_2+z_L²)/μ in the frozen general identity. The straddling interval in the renewal proof has bounded second moment under the stated third-moment assumption (bound the renewal measure on unit intervals and sum the tails of E[L²;L>j]); its translation noise has conditional second moment bounded by a constant times its length. Thus boundary effects do not contaminate the covariance rate. Fixed-duration independent cycles give strictly positive excess contrast |b|²(e^(−2δτ)−e^(−4δτ))/τ. At the strictly unique positive root of the increasing cubic, the excess is scalar; the displayed axes are valid, but not uniquely selected there.

## originality

FAIL

A distinct indexed SCOPE result gives the same full-mobility Poisson covariance tensor, drift, and cubic sign reversal; its isotropic-noise wording for the total axes does not limit the tensor it actually proves. The deterministic excess comparison likewise follows immediately from the fixed-period covariance in a second record. Their displayed dates are later than the frozen record's; this is verified mathematical coverage, not a conclusion about chronological priority or dependence. The generic conditioning identity in the frozen proof is a standard conversion of the one-cycle moments to a centered renewal covariance, not a separate surviving classification of renewal laws. No repair is warranted on the claims as written.

## value

PASS

As a mathematical phenomenon, the crossover answers a concrete question about when random reset times reverse the ordering of coupling-induced transport fluctuations, and distinguishes timing variability from a matched mean period. The exact threshold is useful because the effect is not generally visible in the unadjusted total tensor. This value of the classification does not provide incremental originality in light of the equivalent explicit tensors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
