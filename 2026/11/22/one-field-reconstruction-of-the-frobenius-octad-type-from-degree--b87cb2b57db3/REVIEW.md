# Self-review: one-field exceptional-curve flag reconstruction

## Correctness — PASS

The domain is the finite-field blow-up of a Galois-stable general-position octad, in characteristic at least five; the theorem classifies the possible Frobenius permutation types without claiming that every type occurs over every field. The 240 exceptional divisor classes are taken from the complete classical seven-pattern list, not inferred merely from a bounded experiment. The intersection matrix is exact, and the Frobenius action is the coordinate permutation on the eight exceptional-point indices. All 22 conjugacy partitions are exhausted, and finite fixed-flag sets are enumerated by two structurally different implementations: orbit decompositions and direct sorted-set invariance. Both generate the full 22-row table, establish its injectivity, and independently check the \((5,3)\)–\((7,1)\) arity boundary. The scripts are replayable from the supplied files. The generality follows from the classification of all \(\mathfrak S_8\) cycle types, not from a claim that finite-field samples prove an infinite theorem.

## Originality — PASS, with residual priority risk

Winter–van Luijk (arXiv:1901.06945, Corollary 1 and Remark 5) already give the total \(60{,}480\) pairwise-disjoint triples and geometric Weyl graph orbit facts; these are expressly not original. Desjardins–Winter (arXiv:2210.11659, Theorem 2.1 and subsequent sections) give the 240-curve catalogue and study intersections/concurrency, not the fixed-flag arithmetic character table. Kulkarni (arXiv:2109.14106) studies arithmetic Weyl actions and inverse Galois realizations, not these four fixed-flag statistics. A related earlier arithmetic statement determines the eight-point Frobenius partition from three extension-field genus-four tritangent counts; it does not establish the one-field exceptional-curve pair/triple table or its arity-two failure. Searches in published mathematical findings and previously available research claims did not locate an equivalent table. A legacy unindexed \(E_8\)/\(S_8\) permutation-character computation could nonetheless cover it; this is a genuine residual priority risk rather than proof of uniqueness.

## Mathematical value — PASS

The eight-point Galois cycle partition is the concrete descent datum of a rational blow-up marking. The theorem identifies a complete diagnostic using only the ground-field finite étale exceptional-curve incidence flags and establishes a sharp boundary: even the entire intersection-labeled pair profile fails on \((5,3)\) and \((7,1)\), whereas disjoint triples distinguish them. Thus it gives a natural, exact local-to-global-marking reconstruction criterion with a motivated obstruction, rather than an arbitrary isolated count. The result is conditional on the marked blow-up and is not a computation of Picard or Brauer torsion.

## References and limitations

Primary sources examined are Winter–van Luijk's open-access \(E_8\) graph article; Desjardins–Winter's complete exceptional-curve classification and its concurrence applications; and Kulkarni's degree-one del Pezzo Galois paper. The published geometric triple count and 240-curve list are incorporated as prerequisites. The proof does not classify all possible Weyl Frobenius types for unmarked degree-one surfaces or prove universal existence of every octad partition over a fixed small finite field. Historic unindexed incidence tables remain a possible originality risk.

Self-review: passed. Independent audit: not yet performed.
