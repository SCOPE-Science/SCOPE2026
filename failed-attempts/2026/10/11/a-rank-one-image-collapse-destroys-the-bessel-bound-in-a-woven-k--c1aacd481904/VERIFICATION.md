---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

On H=ℓ²(N), W_i=V_i=span{e_i} with unit weights form identical orthogonal Parseval fusion frames; all partitions retain exactly ||f||². The rank-one bounded Kx=<x,a>e_1 with a_i=2^{-i} has ||K||=||a||=(Σ4^{-i})^{1/2}=1/√3, nonzero closed range span{e_1}, and closed images K W_i=K V_i=span{e_1}. The transformed fusion projection at e_1 is 1 for every i, giving Σ_i1=∞ and hence no upper Bessel bound for any weave. The source’s Proposition 2.5 purports preservation for every bounded K, and its proof proves only the lower inequality and invokes Proposition 1.5 for upper bound despite that proposition assuming the transformed families already are K-fusion Bessel. The sufficient amended theorem with closed image subspaces and separate image-Bessel bounds C_W,C_V then has lower A/||K||² and upper C_W+C_V, as in the original lower projection estimate and Proposition 1.5. The source makes no uniqueness/necessity assertion. This is a complete exact infinite-dimensional contradiction, not inference from finite truncation.

## originality

FAIL

The proposed image-subspace collapse and its exact coefficients are already supplied, up to a simple restriction and projection, by a substantially earlier full-text primary counterexample. In Ruiz–Stojanoff (2007), Example 7.1, an orthonormal decomposition into two-dimensional blocks E_k has T e_{2k-1}=2^{-k} e_1 and T e_{2k}=e_{k+1}; image subspaces T E_k=span{e_1,e_{k+1}} share e_1 and violate the uniform Bessel bound. Taking the isometric embedding U e_k=e_{2k-1} and P=P_{span{e_1}}, the submitted K is exactly PTU: K e_k=2^{-k}e_1. The submitted identical woven source families add no nontrivial hypothesis, and their transformed upper-Bessel failure is the same stronger earlier obstruction. A 2018 weaving-fusion paper also explicitly warns that even onto operators fail to preserve fusion Besselness, citing this prior work. Naming a later 2019 proposition and its unjustified reliance on a Bessel premise is a useful source-specific correction, but the mathematical counterexample is mechanically implied by the earlier stronger example; under statement-and-implication comparison rather than titles, it fails originality. This is a scientific coverage failure, not a failure of literature access.

## value

PASS

The precise false claim is a blanket construction rule for weaving fusion frames and its error is a missing upper-Bessel premise, not a cosmetic sign or type issue. Exhibiting the failure under a closed-range rank-one operator, with closed image subspaces, provides a useful explicit warning about loss of coefficient amplitudes when replacing vectors with image subspaces. A sufficient amended statement adds quantitative image-Bessel bounds. Locating the exact flaw in the 2019 proposition is useful to readers even though the mathematical obstruction and essentially the submitted example are derived directly from a 2007 primary result, causing a separate originality FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
