# Scientific review

## Correctness (C): PASS

The assertion is finite and quantifies over exactly all triples of positions for the specified three substitution words. Both bundled Python programs independently enumerate all distinct factors, use the equivalent exact hitting-set condition and establish set equality with all four disjoint boxes. The first explicitly visits all 4,010,618 triples; the second branches on uncovered-factor masks. Because all three symbols occur, the lower bound of three positions is elementary and completes minimality. Computational checks are reproducible with complete source, not inferred from numerical samples; the results are not extrapolated to further substitution orders.

## Originality (O): PASS, with residual historical risk

Schaeffer and Shallit's Theorem 6 proves existence and minimum size three for all Tribonacci prefixes, but does not give the exact number or box classification of all optimal triples. Banbara and colleagues' 2026 research provides complete classifications for Fibonacci and period-doubling words (later Thue–Morse), not these Tribonacci substitution words. The inspected related source by Faro and colleagues concerns Thue–Morse. Indexed mathematical research results addressing string attractors in Thue–Morse, paperfolding, Rudin–Shapiro and antipalindromic words do not imply the specific ternary 4-box classification. Both aliases (Tribonacci finite substitution words and prefixes) and equivalent hitting-set / smallest-attractor formulations were searched. Absence of an exact searchable match is not proof of global priority, and unindexed or unpublished work remains a risk.

## Value (V): PASS

Counting all smallest attractors, rather than simply establishing their minimum size, is the natural fine-grained invariant investigated by recent 2026 papers for morphic sequences. This complete classification gives explicit positional structure—four disjoint products, including their cross-stage nesting—rather than just a short list of computed cardinalities, across three consecutive canonical ternary substitution stages of increasing sizes (81, 149, 274). It provides precisely reproducible finite benchmarks and possible constraints for a future all-stage theorem. The result stands on its exact finite scope and does not claim an unproved eventual law.

## Closest literature and risks

Closest: Schaeffer–Shallit (arXiv:2012.06840, Theorem 6), Banbara et al. (arXiv:2602.16152, 2026 CPM), Faro et al. (arXiv:2610.10950). The first already covers the minimum cardinality; the others give analogous other-sequence classifications. The independent external review is unperformed, and historical priority is provisional.

Self-review: passed. Independent audit: not yet performed.
