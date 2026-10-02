# Independent audit — SCOPE-20260919-7580e8e0e8e1

Audited: 2026-10-01 UTC.

Disposition: **failed**.

## Final claim

Within the newly classified generalized-chi permutation family, effective odd block lengths give exactly \(\tau(n_0)-1\) affine classes, and each class inherits the normalized maximum Walsh correlation of the corresponding ordinary chi block.

## Correctness (C) — PASS

Given the interleaved-track decomposition, each nondegenerate map is affine-equivalent to a Cartesian power of ordinary odd chi. Every divisor \(\ell>1\) of the odd part \(n_0\) is realized, and the known inverse degree \((\ell+1)/2\) separates distinct block lengths under affine equivalence. Walsh transforms factor multiplicatively over Cartesian products; choosing one nonzero output-mask block and zero masks elsewhere gives equality in the maximum, yielding the exact normalized correlation identity. The committed exhaustive checks corroborate the formulas for tested small parameters but are not used as an infinite proof.

**Sources checked.** assigned RESULT.md and verifier blobs; published SCOPE 2026-09-18 generalized-chi invariant record; Feng–Wang–Yu–Zhang arXiv:2609.19548 metadata and revised-source status

**Risks / limits.** The proof relies on the revised source’s track decomposition and the published ordinary-chi inverse-degree theorem, both explicitly acknowledged as prior.

## Originality (O) — FAIL

The revised source already supplies the direct-product track decomposition and canonical-family equivalence. The earlier 2026-09-18 SCOPE record then explicitly transfers the known ordinary-chi inverse degree to the same blocks. From those prior facts, the divisor-indexed class count follows immediately by listing possible \(\ell\) and separating them by inverse degree. The Walsh identity is the standard tensor-product factorization of a vectorial Boolean transform. These are mechanically implied corollaries of prior structure, so implication-based originality fails even though the exact count and normalized-correlation sentence are not stated verbatim in the source.

**Sources checked.** published SCOPE record Exact inherited invariants for stretched generalized chi permutations, dated 2026-09-18; Feng et al. arXiv:2609.19548 revised abstract/metadata; Resultary semantic search for generalized chi affine classes and Walsh scaling

**Risks / limits.** Full revised primary text was not retrievable through the lawful full-text routes attempted; however, the decisive prior structural facts are explicitly preserved in the earlier published SCOPE record and in the current package’s own corrected scope.

## Value (V) — FAIL

An exact affine-class count is normally a natural classification invariant, but here its value is obtained by a one-line divisor enumeration once the prior block decomposition and inverse degree are known. The Walsh scaling is generic Cartesian-product algebra. Under the required bar excluding mechanically implied narrow invariants and routine deductions, the surviving claim does not independently qualify.

**Sources checked.** same prior decomposition, inverse-degree result, and standard Walsh factorization

**Risks / limits.** None material beyond the stated scope.

## Originality comparison

**Equivalent formulations.** The affine-class count is equivalently the number of attainable odd block lengths, since inverse degree is a strictly increasing affine invariant of that block length. The Walsh statement is the standard transform tensorization for the same direct product.

**Broader coverage.** The source v2 gives the decomposition; the earlier SCOPE record already transfers ordinary-chi inverse degree and several other direct-product invariants. Together these dominate the only nonstandard inputs needed for the final claim.

**Exact database or table checks.**

- Resultary: generalized chi permutation affine classes inverse degree Walsh scaling Cartesian product — Returned the audited record and the earlier 2026-09-18 direct-product invariant record as the closest prior SCOPE coverage.

- published SCOPE archive: generalized-chi-direct-product-differential-structure — Full RESULT.md inspected; it states the v2 decomposition and exact inherited inverse degree before the audited record.

**Claim versus prior implication.** Possible block lengths are exactly divisors of \(n_0\); the prior inverse-degree formula separates them, so the count is immediate. Standard Walsh tensorization then gives the normalized correlation formula without a new nonstandard lemma.

## Source inspections

- Assigned package, verifier source and saved output inspected from the frozen Git tree.

- Full published 2026-09-18 SCOPE generalized-chi RESULT.md inspected.

- arXiv:2609.19548 abstract/revision metadata inspected; full v2 text unavailable through lawful routes.

## Residual risks

- Primary v2 full text was inaccessible, but this does not rescue originality because the needed decomposition and inverse-degree implication are already established in the published record inspected.

## Scope boundary

Scientific rejection is on originality and value, not correctness. The track decomposition, canonical-family equivalence, and ordinary-chi inverse data are prior; the remaining count and Walsh scaling are routine consequences.
