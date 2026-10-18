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

For partition λ=(λ_1,...,λ_e) of d≥1, diagonal C* action on P(Sym^d C²) has exactly d+1 monomial coordinate fixed points [x^(d-s)y^s]. Such a monomial lies in the closed coincident-root locus Δ_λ if and only if the exponent s is the sum of a subset of the λ_i: forward by choosing factors x or y, reverse by unique factorization. Distinct subset sums index DISTINCT points, not multiplicity. Projective torus localization gives χ_top(Δ_λ)=|Σ(λ)|. The d+1 extremum follows from elementary sorted complete-subset-sum criterion a1=1 and aj≤1+Σ_(i<j)ai. Independent subset enumeration checked partitions (2,1),(3,3),(2,2,2),(3,2,1),(1,2,3,5), with respective χ candidates 4,3,4,7,12. This is an all-partition proof, not an extrapolation from checked partitions.

## originality

FAIL

FAIL: The main invariant is already completely determined by Balázs Kőműves’s publicly available 2018 motivic-characteristic-class treatment and computational package for the same coincident root loci, including closures. The 2018 χ_y generating function for every exact-root open stratum yields χ at y=−1, and the published finite coarsening-stratum sum yields χ for every projective closure Δ_λ. The source explicitly identifies Euler characteristic of coincident root loci as previously trivial. The concise distinct-subset-sum expression and sorted equality test were not found stated verbatim; however the claimed exact Euler invariant is a corollary of stronger same-object prior coverage. Search failure for matching formula wording is not evidence of originality.

## value

PASS

The torus-fixed monomial interpretation and exact distinct-subset-sum equality criterion are mathematically natural and give an exceptionally concise way to evaluate a classical singular projective variety invariant. They are motivated and potentially useful as a simple closed reformulation even though the Euler characteristic is already determined by stronger prior computational and characteristic-class results; value does not override originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
