---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For a nonempty atom, restricting its parent to a branch and taking the closure of the affine image gives a compact interval, shrinks diameter by at least the required factor, and cannot decrease the gap to another restricted parent before the map is applied. Induction gives diameter at most Lλ^n and pairwise gap at least gλ^(n−1): differing final branches already give g, and equal final branches multiply the parent gap by exactly λ even if orientation reverses. This also proves uniqueness of the word labelling a nonempty atom. The atoms cover K by the nested attractor definition. Every itinerary factor lands in an active atom; conversely, any point of K in an atom is approximated by a regular orbit tail in K, and positive same-level separation forces the tail into that very atom. Tail density follows by applying minimality to f^n(x), which is again regular and in K. Thus the active count is exactly p_θ(n), independent of x. The established separation-complexity theorem gives the affine law and its precise left–right recurrence interpretation. At n_−=floor(log(g/ε)/log(1/λ)) the gap is strictly larger than ε, while at n_+=ceil(log(L/ε)/log(1/λ)) the diameters are at most ε. One point per active atom at the former level and a cover at the latter squeeze N_K(ε) as stated. If the complexity slope vanishes, boundedly many atoms of vanishing diameter cannot cover an infinite K: any larger finite selection of distinct points has positive minimum spacing. For a periodic component its q distinct points require exactly q sufficiently short intervals. The metric proof is conditional on the stated basic component and its regular dense orbits; it does not require a stronger global decomposition assertion from the wording of D.

## originality

PASS

The published decomposition, unique disjoint atom coding, exact active count, eventual affine complexity and logarithmic-order upper bound are prior ingredients. The distinct same-day Resultary law gives the exact bounded remainder and a common-suffix lower separation argument for a two-branch Sturmian class, including the same coefficient on the shared equal-slope subclass. This is material coverage of that special case and proof geometry, not a priority determination or full coverage. The submitted componentwise coefficient for arbitrary numbers of separated equal-absolute-slope branches, including orientation reversals and arbitrary recurrent-discontinuity counts, remains distinct in the inspected comparisons. It requires a scale-uniform lower separation not provided by the older qualitative disjointness lemma or box-dimension argument.

## value

PASS

Zero dimension does not quantify covering growth. The uniform metric squeeze finds its first nonzero coefficient with bounded error and turns it into a recovery formula for a component's count of recurrent discontinuities. This provides a component invariant for arbitrary separated equicontractive branches beyond the already covered two-branch Sturmian example, rather than repeating the prior zero-dimension theorem or computing selected cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
