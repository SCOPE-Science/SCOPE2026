# Self-review

## Correctness — PASS

The claim quantifies over all positive binary run lengths and all positive factor lengths. The proof first excludes all factors with at least two transitions by the unequal interior-run obstruction, next gives a necessary and sufficient condition for unary and one-transition factors, then derives the finite generating polynomial and count. The equal-run case is separately proved by a half-period complement shift. There are no unproved external lemmas in the derivation. The independent direct-substring regression program matches each literal factor set and count for all 256 ordered positive run-length pairs up to 16, testing 13,568 length profiles; enumeration is explicitly not a proof for unbounded lengths.

## Originality — PASS (best-knowledge, with risk)

The closest paper is Currie et al., *Complement Avoidance in Binary Words* (arXiv:2209.09598, preprint 2022). Its introduction and Sections 2, 3 and 5 investigate the existence of complementary factor pairs, total-budget classes, and repetition thresholds. Neither the inspected preprint's results nor targeted searches gave the explicit complemented-factor set of a two-run periodic host or its length generating function. Dvořáková et al. (DMTCS 2020) concern complementary-symmetric aperiodic Rote sequences, not this finite spectrum. Earlier formulas for two-run total factor complexity, closed-factor counts and antisquare counts are not equivalent to complement membership. Exact-phrase searches and semantic database searches did not return a covering theorem. This is a qualified originality assessment, not proof of novelty; the published final version and unindexed special-case work remain priority risks.

## Mathematical value — PASS

The invariant is one of the two principal observables in the published complement-avoidance framework: allowable lengths of complemented factors and their total number. This is a *complete natural family classification*, not a finite example or table lookup. The exact language description gives every length multiplicity, the maximum length, and the sharp transition from finite to infinite when the two run lengths coincide. The exact product-form polynomial and dependence solely on the shorter run provide explicit structured benchmarks and show that increasing the longer run has no effect on the complemented-factor spectrum. The claim is intentionally limited to this natural family and makes no unsupported broad downstream assertion.

## Closest literature and residual limits

Primary: Currie et al., https://arxiv.org/html/2209.09598v2 (Sections 1–3 and 5, checked against statement and implications); journal DOI https://doi.org/10.37236/11555. Context: Dvořáková et al., https://dmtcs.episciences.org/articles/6519. Equivalence to periodic-factor language intersection and possible implicit specializations were searched. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
