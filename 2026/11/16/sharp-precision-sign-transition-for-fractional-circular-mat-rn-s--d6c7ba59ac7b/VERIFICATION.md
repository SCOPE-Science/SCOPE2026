---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Point evaluations continuous when s>1/2, positive Fourier weights make Σ invertible; reproducing-kernel minimum H^s energy is vᵀΣ⁻¹v. For 0<s<1, subordination of κ²−∂² produces a positive off-diagonal jump kernel, so the min/max lattice energy inequality is strict for basis-data interpolants whose difference changes sign at two sample sites. The resulting inequality is precisely 2Q_ij<0. At s=1, the minimizer on each circular arc solves −f″+κ²f=0 and the arc Dirichlet energy has cross-term −κ/(π sinh κℓ), giving Q_ij=−κ/(2π)∑(sinh κℓ_a)⁻¹ on cycle-neighbors and zero elsewhere. Four-point DFT gives Q_13=[S_0⁻¹+S_2⁻¹−2S_1⁻¹]/16 and limit (2^(2s−1)−2)/[16(1−2^(−2s))ζ(2s)]>0 for every s>1. Independent four-site high-precision checks at s=.75,1,1.25,1.7,2.2 corroborate limits; finite truncation at s=1 is not claimed exact. All quantifiers are resolved analytically.

## originality

PASS

Best-of-knowledge original scope after positive mathematical implication comparisons, not inferred from mere negative search. Equispaced order-two and order-one CAR are special parameter/subconfiguration checks, not equivalent to all fractional s and arbitrary irregular sample sets; possible general trace-Dirichlet operator equivalence remains a stated priority risk. General Markovian Dirichlet-form arguments imply much of the s<1 direction, and novelty is not claimed for the machinery; inspected broader theories do not directly provide the combined two-sided sharp classification. Known facts are proper special cases or proof tools, not statements dominating both directions of the submitted theorem; an older general total-positivity/trace theorem may still give an equivalent formulation.

## value

PASS

A universal sign boundary for inverses of an irregular sampled covariance identifies when all Gaussian partial correlations are positive versus when higher smoothness can create positive precision interactions; an exact Markov/local endpoint and a minimal explicit violation matter for Gaussian graphical inference and fractional Sobolev trace forms. This is not a numerical or normalization-only result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
