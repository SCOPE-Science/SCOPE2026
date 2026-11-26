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

The degree-q+1 vanishing forms are the alternating Frobenius forms, by projective reduction of x_i^q x_j followed by interpolation, valid also in characteristic two. Alternating congruence gives the normal form, a smooth base on 2r variables and k free coordinates; over a field of size Q these multiply the base count by Q^k and add the vertex. I checked the all-extension formula independently by additive characters. For Q=q^s and nonzero character parameter a, summing a single alternating pair over y leaves Q times the indicator of a^q x^(q²)=a x. By cyclicity of the multiplicative group, for odd s there are q solutions x for every a; for even s there are q² on the subgroup a^((Q−1)/(q+1))=1 and one otherwise. Multiplying over the r pairs and projectivizing yields the primitive correction Q^(r−1) times q^r for odd s and (q^(2r)+q)/(q+1) for even s. Its formal exponential splits into the two claimed signs with the announced multiplicities; the k unused coordinates yield the shifts and vertex factors. This also covers r=1 (q+1 separate base-field points) and k=0. The q² excess over the ambient hyperplane count has one strictly rank-decreasing term, and congruence identifies the corresponding projective class. The frozen purity argument is consistent with this derivation; the two signs are characteristic-polynomial multiplicities, not an assertion of semisimplicity.

## originality

PASS

Only the uniform full base-field Frobenius spectrum across all alternating ranks is credited as the distinct contribution. The normal form and smooth subclass are known; the quadratic count and its rank-separation interpretation follow from the classical degenerate Hermitian formula and alternating congruence. A quadratic spectrum alone loses signs under squaring; recovering the base-field characteristic polynomial and extending across all cones uses the space-filling trace in addition to those prior results. No inspected separate statement gives that all-rank, all-extension formula.

## value

PASS

Computing the complete arithmetic invariant of the entire natural minimum-degree family is meaningful when every base-field rational point set is identical, and when the Hermitian model over the quadratic field hides the odd-extension behavior. The formula uniformly includes all singular ranks and gives a concrete, readily usable distinction between their projective classes. The value is in the full descent spectrum, not the routine quadratic monotonicity corollary alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
