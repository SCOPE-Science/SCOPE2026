---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The exact original Exner--Tater coefficients c1 and c3 have Q terms +2Q*sinh(κℓ) and +2Q*sinh(κℓ). Hence ∂_Q Σ c_jκ^j=2κ(1+κ²)sinh(κℓ)>0 for every κ,ℓ>0, regardless of interior μ. Q(θ1,θ2)=cosθ1+cosθ2 is nonconstant analytic so every single level set is measure-zero in T²; a direct-integral eigenvalue requires positive-measure fiber eigenspace. Negative hyperbolic edge solution has no missing sin(kℓ)=0 Dirichlet singularity since sinh(κℓ)≠0. Independently reconstructed and simplified symbolic secular polynomial using SymPy, matching the actual frozen artifacts/verify.py; proof is analytic, not finite sampling.

## originality

FAIL

The ORIGINAL Exner--Tater paper already prints the exact entire negative-energy secular equation (22), affine in Q=cosθ1+cosθ2 with coefficient 2κ(1+κ²)sinh(κℓ) strictly nonzero for every κ,ℓ>0, and explicitly observes that the negative flat band at μ=0 becomes absolutely continuous for μ>0 (p.9 of source). The claimed no-negative-point-spectrum is a direct elementary corollary of this prior complete all-quasimomentum spectral description and the standard Bloch flat-band criterion. It cannot gain originality by a separate no-flat-band slogan.

## value

FAIL

The question is physically motivated by a disappearing negative flat band, but the original 2021 source already explicitly discusses its transition into absolutely continuous spectrum and prints the exact all-negative-energy Bloch determinant. The only added calculation is collecting two visible Q terms and applying a standard direct-integral level-set observation. With the same-object stronger formula already published, this is a routine negative/type check rather than a substantive new structural lemma or unknown natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
