# Scientific review: early small fringe subtrees

## Correctness — PASS

The proof derives the exact one-root beta-binomial size law and conditional uniformity of the internal tree and outside tree. Induction on any fixed number of early marked roots shows that disjoint marked subtrees supply the product rare-event probability, while any nesting imposes at least one extra factor of order inverse tree size. Summed mixed factorial moments converge to those of independent point processes; the Poisson-superposition calculation supplies the uniform first-size mark. The standalone deterministic checker passed 1,336 assertions for all recursive trees through eight vertices and additional first-moment checks. No finite experiment substitutes for the proof.

## Originality — PASS, with historical priority risk

Holmgren–Janson (arXiv:1406.6883, Theorems 1.4, 1.5, 1.9) treats global size/shape totals, including normal laws for small sizes and Poisson laws for large sizes, not birth-rank-resolved small-subtree extremes. Feng–Mahmoud (2010, DOI 10.1239/jap/1269610825) establishes a global fixed-shape Gaussian law and a shape functional. The published earliest-leaf process covers the case of subtree size one exactly, which is not claimed new. None of the inspected statements covers the simultaneous independent point processes for all fixed sizes/shapes and the uniform mark at the first qualifying birth label. The full 1991 Mahmoud–Smythe paper was unavailable for complete inspection, so a priority risk remains.

## Value — PASS

The theorem identifies a natural earliest-birth boundary for unexpectedly short descendant branches. It shows that different fixed fringe sizes have *equal* early rarity, despite their unequal global abundances, and determines the joint law of all early exceptions and their increasing shapes. The first-event uniform size mark is a direct structural consequence with interpretation independent of global fringe counts.

## Limitations

Only fixed finite size/shape sets and fixed ranked arrivals are proved. No rate or growing-cutoff extension is claimed; complete historical priority requires further literature review. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
