# Review: forest independence and triangular successor dependence

## Correctness — PASS

The elementary but fully general root/relative-permutation bijection supplies an exact joint product law along every forest. Path equality is expressed by a two-variable sentence; its joint probability over a graph \(G\) is \((n!)^{-(k-c(G))}\), which distinguishes forests from graphs containing cycles for every \(n\ge2\). The quantitative part separates identical, exactly-two-equal, and three-distinct compatible directed-edge triples. The resulting centered mixed third moment is strictly positive and has leading term \(1/n\). The independently implemented finite checks in `checker.py` test both sides of these calculations on small domains. No extrapolation from computation substitutes for the proof.

## Originality — PASS within inspected evidence

The 2026 article on finite satisfiability with arbitrarily many successors supplies the precise logical language but addresses decision complexity. Diaconis–Evans–Graham determine the one-pair directed-adjacency law; their theorem does not imply triple interactions. Bender–Canfield give general sparse-graph intersection Poisson limits, not an exact joint law of different pairwise intersections. Searches of the mathematical research index for relative-permutation, forest, pairwise-overlap, and mixed-cumulant aliases located no covering statement. A related exact triangular cumulant for LKJ correlation matrices concerns different random objects. The forest result follows a classical group-coordinate principle and originality is not claimed for that abstract device. General probability results could affect priority for parts of this work.

## Value — PASS

For the natural finite-model measure associated with several independent successor relations, the theorem gives a complete graph-theoretic criterion for universal independence of arbitrary pair-local first-order truth events. It identifies exact definable cyclic obstructions and computes the first nonzero interaction of the basic common-successor statistics, including its sharp finite-size scale. The statement is a motivated structural classification rather than a small finite example.

## Scope and residual limitations

The random orders must be independent and uniform, and pair-local logical sentences may not use extra fixed labels or relations. The numeric count statistic need not be expressible in plain FO². The result establishes an exact third cumulant but does not determine the full multivariate distribution or historical priority. One older PDF was read through extracted text because visual rendering failed. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
