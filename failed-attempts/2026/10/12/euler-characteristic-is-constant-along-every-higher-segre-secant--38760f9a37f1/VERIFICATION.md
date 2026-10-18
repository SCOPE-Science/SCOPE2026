---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For B>max a_i, the tensor-coordinate weights sum_i j_i B^(i-1) are distinct; thus a generic diagonal C* subgroup fixes only the N=product a_i coordinate lines in ambient projective space. These are all decomposable, hence contained in X and every invariant secant sigma_r(X). As no other ambient fixed point exists, sigma_r(X) has precisely these N fixed points. The established Euler fixed-point identity for possibly singular projective varieties gives chi(sigma_r)=N for all r, including ambient-filling boundaries. Additivity of compact-support Euler characteristic gives chi_c(sigma_r\sigma_(r-1))=0 for r>=2, rank-one layer N. Independent small-format base-B distinctness was reconstructed. C* localization, not an exhaustive finite check, is the infinite proof.

## originality

FAIL

This final theorem is directly subsumed by the established general fixed-point formula chi(Y)=chi(Y^{C*}) for arbitrary singular complex projective Y with algebraic C* action, stated explicitly in Hu (2019 preprint / 2021 publication). Specializing the theorem to a coordinate-diagonal action on ANY C*-stable projective locus containing all ambient coordinate lines gives chi=N without a Segre-specific lemma beyond the immediate definition that each coordinate pure tensor belongs to X. Every secant sigma_r automatically meets these hypotheses. The border-rank-layer vanishing is then the one-line additivity difference. This is strong prior implication despite no paper wording matching Segre or r.

## value

FAIL

Although the varieties are natural, the precise submitted invariant is entirely determined by a generic diagonal action plus the tautology that every coordinate axis is already rank-one. Neither a new fixed-point class, a nontrivial enumeration, an unknown classification, nor a structural obstruction beyond the textbook fixed-point-specialization emerges. The exact-stratum statement is only subtraction of identical known fixed-point counts, so as submitted this is an elementary standard-theorem application rather than an independently useful new mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
