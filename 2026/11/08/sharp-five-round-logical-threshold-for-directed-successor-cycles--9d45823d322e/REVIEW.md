# Scientific review: sharp five-round logical threshold for directed successor cycles

**Correctness — PASS.** The exact recursive rank-type characterization was proved by induction. The provided program exhaustively computes each required tuple-extension type through cycle length \(32\) and rank five, with structural equality rather than probabilistic hashing. It independently cross-checks the smallest cycle comparisons through direct EF minimax. The cyclic-gap invariant proves the all-length tail for rank five and below. The finite computation and infinite proof have distinct, specified responsibilities.

**Originality — PASS (best-evidence assessment).** The motivating Gaifman normal-form papers concern more general locality and do not give the numerical \(19\) cutoff in material inspected. The closest published exact quantifier-rank statement concerns directed *paths*, whose endpoints make the claim logically different. A related one-red-order profile also uses a different signature. Specific successor-cycle, five-round, rank-type, and cutoff searches did not locate the same classification. Inaccessible full texts and potentially older specialized EF literature are priority risks, not assertions of proven uniqueness.

**Value — PASS.** A sharp finite-rank indistinguishability threshold is a natural invariant of finite directed successor models. Rank five yields exactly \(19\) theories, with the stable range starting at \(19\), substantially below the standard \(32\)-length generic EF guarantee. The complete ranks-one-through-five table is a motivated small-rank classification, rather than an arbitrary census.

**Scope and limitations.** Only single cycles, one binary successor relation, ordinary first-order quantifier rank through five. No higher-rank pattern or stronger signature is claimed. The mathematical argument remains open to independent validation and historical priority examination.

Self-review: passed. Independent audit: not yet performed.
