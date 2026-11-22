# Scientific review: sharp five-residue balance

## Correctness — PASS

The two hyperbinary parity decompositions give exact polynomial recurrences. Specialization at a primitive fifth root yields two integer-linear transitions for the adjacent pair of evaluations. Every positive index descends to one by halving; hence a finite set containing the initial state and closed under *both* transitions covers every positive index. The explicitly supplied 120-state table is distinct, contains the seed, is closed under all 240 transitions, and has maximum coordinate spread two. Coefficients in the degree-four cyclotomic basis are precisely the differences of the five residue counts from the fifth. Sharpness follows from the explicit polynomial at ten. The previously established hyperbinary/fence rank correspondence transfers the inequality to every finite fence. The secondary recurrence-only computation through index 12000 corroborates the derivation but does not replace the induction.

## Originality — PASS, historical priority provisional

Alekseyev (arXiv:2611.01243v1, Theorem 19 and Corollary 20) proves three-class discrepancy at most one, not five-class discrepancy at most two. McConville–Propp–Sagan (arXiv:2508.20026v1, Theorems 3.16–3.17) establish the underlying combinatorial correspondence and generating polynomials, not the root-of-unity bound. Kogiso–Miyamoto–Ren–Wakui–Yanagawa (arXiv:2403.08446v2, Section 7) gives restrictions at third/fourth roots and discusses a fifth-root divisibility obstruction, but does not show a 120-state fifth-root closure or the present coefficient discrepancy. Direct external text searches, a semantic-result search, and comparison with all recoverable current accessible claims found no theorem dominating the new sharp five-class assertion. Semantic search and finite access do not establish historical uniqueness. Older literature on Stern polynomials remains a risk to be checked independently.

## Value — PASS

This is a natural next-prime structural question after the recently published modulo-three theorem. The bound is uniform across arbitrarily many hyperbinary expansions and arbitrary finite fence posets, is sharp on a natural five-expansion example, and arises from a complete finite cyclotomic orbit rather than a finite list of tested integers or an arbitrary slice. Its proof supplies an exact reusable 120-state certificate for these rank distributions.

## References and limitations

- M. A. Alekseyev, *Halving Partitions and Hyperbinary Expansions*, arXiv:2611.01243v1, Theorem 19 and Corollary 20, https://arxiv.org/html/2611.01243v1.
- T. McConville, J. Propp, B. E. Sagan, *Hyperbinary partitions and q-deformed rationals*, arXiv:2508.20026v1, Theorems 3.16–3.17, https://arxiv.org/html/2508.20026v1.
- T. Kogiso et al., *Arithmetic on q-deformed rational numbers*, arXiv:2403.08446v2, Section 7, https://arxiv.org/html/2403.08446v2.

Self-review: passed. Independent audit: not yet performed.
