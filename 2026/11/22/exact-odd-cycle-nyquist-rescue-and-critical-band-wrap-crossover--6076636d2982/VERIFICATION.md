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

Absolute summability (p≥2) allows grouping the DFT by residues. The wrapped continuous convolution density has Fourier coefficients s_a(j)^p/(2π), yielding the exact normalization and positivity in (1). For circular monotonicity, let r,s≤π be two arc half-lengths and ℓ(x)=max(0,min(2r,2s,r+s−x)) the corresponding line overlap at displacement x≥0. For 0≤d≤π the circular overlap is ℓ(d)+ℓ(2π−d). The second summand can increase only where d>2π−r−s≥|r−s| and d<r+s, hence its increase is canceled by the first summand. Layer cake iterates that monotonicity for all wrapped uniform convolution powers even past later wraps. The minimum is therefore at a nearest-to-π bin, with no uniqueness claim. Strict support yields the ceiling count (2) and the strict thresholds (3), including bins exactly on endpoints. At the nearest bin θ=π−δ_N, the only possible copies in (5) are at θ and θ−2π: other copies have absolute value at least 3π−δ_N, exceeding 5π/4 since δ_N≤π/3. Their signed edge depths are ε+δ_N and ε−δ_N. Positive depths in [0,2a] give the stated density via the volume of a p-dimensional simplex of deficits. Substituting ε=0 and then ε=πt/N gives (4) and (6), including exact zero at each support threshold. These checks reconstruct the universal argument, independent of the finite checker.

## originality

PASS

The matched Toeplitz primary source gives the spline description and edge exponent in the no-aliasing setting; the finite circular operator has a different spectrum. The closest distinct Resultary record shows a parity effect for Bernstein approximants to circle covariances, not equivalent sinc-power coverage. The supported distinction is the combined exact cyclic classification and two-sided crossover, not the classical DFT, support of a uniform convolution, or B-spline edge formula in isolation.

## value

PASS

First circular wrap is a natural bandwidth boundary for invertibility and conditioning, and the corresponding question for a cyclic operator is not resolved by the known Toeplitz quantile exponent. Exact finite positive-definiteness thresholds and a parity-sensitive scaled eigenvalue across the boundary are useful spectral information, not arbitrary samples of a spline. The value is the full transition from zero to positive, its finite-grid constants, and the all-band minimum-location guarantee, not novelty of Fourier diagonalization or the classical edge power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
