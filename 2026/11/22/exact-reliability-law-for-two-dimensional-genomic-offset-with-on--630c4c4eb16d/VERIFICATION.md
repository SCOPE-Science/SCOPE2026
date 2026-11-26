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

The original formulas are mathematically correct, and the narrowed result in /workspace/repairs/3/RESULT.md was rechecked. For fixed architecture the Gaussian fourth-moment identity gives X=Q²/tr(A²), where Q=wᵀAw/(wᵀw) and w has covariance proportional to the positive definite environment-whitened GEA metric A. Normalizing and diagonalizing A gives Q=(κ²+T)/(κ+T) with T=(V/U)² for independent standard normals. Strict decrease for κ>1 gives the law, its nonattained endpoints, and the unique median at T=1; κ=1 is degenerate at 1/2. Averaging the squared quotient over the uniform angle of (U,V) yields the closed mean, and the derivative factorization proves strict monotonicity of the mean and median. Substitution at κ=4 confirms mean 10/17, median 17/25 and probability below 1/2 of about 0.37337399348. For the repaired centerpiece, at each fixed T the scaled deficit κ(1-X) tends to 2T, but T has infinite mean. Replacing T by κu² gives X=(1+u²)^(-2)+O(κ^-1) uniformly. The rescaled half-Cauchy density factor is bounded by 2/(πu²); multiplied by 1-(1+u²)^(-2) it is integrable and gives an integral of (2+u²)/(1+u²)² equal to 3π/4 before the factor 2/π. This proves the mean scale and constant, while the Cauchy tail at u tending to √(x^(-1/2)-1) proves the fixed-threshold constant. This is for the conditional mean loss, with probabilities over allelic effects, not a realized-fitness correlation.

## originality

PASS

Originality of the original headline exact law fails: the CDF is an exact special case of Forchini's stronger result once the pre-existing genomic-offset covariance identity is used. An elementary arctangent simplification, median substitution or an application-specific name does not rescue that claim. The complete replacement in /workspace/repairs/3/RESULT.md makes the finite-κ law and median prior inputs and restricts the contribution to the anisotropy comparison of the ensemble mean versus typical reliability, with exact deficit rates and an explicit rescaled integral explaining the mean. The original correctness is preserved; originality passes only for this repaired claim. The compared sources do not furnish that integrated comparison; priority is not certified beyond the material examined.

## value

PASS

The adjusted claim answers a concrete reliability question: the usual architecture improves much faster than the ensemble average because an order-κ^(-1/2) fraction of directions still produces appreciably low correlation. Neither a deterministic bound nor recomputing the known CDF alone explains why the mean and a fixed quantile should be treated differently. The distinct rates, constants, and integrable rescaling give an interpretable calibration result; no value credit is assigned for a routine distribution substitution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
