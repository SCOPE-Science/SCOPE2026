# Self-review: sharp rare failure of greedy crown matching

## Correctness — PASS

The full proof gives the exact transition kernel on \((m,r)\), proves failure can occur only at the last unmatched pair, and telescopes the normalized overlap expectation. A two-tag survival product, with matching upper/lower factors and a uniform small-\(m\) bound, establishes the absolute \(O(n^{-2})\) remainder around the logarithmic coefficient. The exact rational verifier matches direct labelled-subset enumeration through six labels and checks the forward-state telescoping identity. Finite computations do not establish the infinite asymptotic.

## Originality — PASS (historically qualified)

Dyer–Frieze (1991) establishes the edge-uniform greedy matching model but the complete article was inaccessible, so implicit coverage remains possible. Gamarnik–Goldberg (arXiv:0807.1277) provides regular-graph matching bounds without the present sharp probability correction, although its hypotheses can apply to crown graphs. Mastin–Jaillet (arXiv:1307.2536) analyzes a different online graph/selection model. Searches of related published results located crown-graph structural invariants and different random greedy algorithms, not the same event or an implication of the new result. The evidence supports best-knowledge originality with the stated access risk, not uniqueness as a certainty.

## Value — PASS

Uniform-edge greedy matching can fail on a graph that is still dense and perfectly matchable. The precise rare failure probability and the nontrivial logarithmic second term characterize the reliability of a natural baseline matching algorithm. The structural overlap process explains the effect, rather than merely enumerating small examples.

## Closest literature and limits

The exact theorem is specific to crown graphs and uniform edge selection. The unavailable Dyer–Frieze full text is the principal historical-priority uncertainty. The constant-order term beyond the logarithmic correction is not computed. Full external scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
