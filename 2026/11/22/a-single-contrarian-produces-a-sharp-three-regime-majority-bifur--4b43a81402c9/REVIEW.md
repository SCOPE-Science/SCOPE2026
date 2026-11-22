# Review of the single-contrarian biclique classification

## Correctness — PASS

The definition uses strict open-neighbour majority, opposite strict majority for exactly one marked vertex, and identical incumbent tie retention. The proof reconstructs the complete update on \((x,c,y)\) and derives a decisive structural threshold: the canonical pattern has shore majority \(a-1\) or \(1\), which is strict exactly when \(a\ge3\). The cases \(a=1\) and \(a=2\) are proved separately rather than inferred from the larger case. Each exact basin and first-entry formula is traced to disjoint state classes and binomial weights. The identity of the oscillation *set*, not just its probability, follows from strict initial shore-majority disagreement.

Four actual checks passed: exhaustive bit-mask iteration across 260,100 labelled initial configurations on 64 parameter pairs; a distinct weighted quotient across 1,600 parameter pairs; an independent 64-pair individual-basin enumeration; and a 257,040-state configuration-by-configuration comparison against unmodified majority. Finite checks corroborate but do not replace the all-parameter proof. No independent external audit has been carried out.

## Originality — PASS, with historical risk

The nearest primary paper is J. Haslegrave and C. Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496v1 (2016), especially Theorem 2 on the possible periods in triangle-free networks and its examples of period four. That broad result does not assert the sharp \(a=1,2,\ge3\) transition, all individual basins, the entrance-time polynomial, or invariance of the oscillation basin to a single contrarian. Its period-four example on one edge is consistent with the \(a=1,b=1\) endpoint but does not imply the infinite classification. A separate 2009 study by Cannings treats mixtures of majority and minority players on complete networks, hypercubes and cubic examples; accessible abstract material does not establish the biclique formulas, but its inaccessible full paper remains a historical priority risk. Bagnoli and Rechtman (2015) address stochastic reasonable contrarians and mean-field bifurcations with different update probabilities, not the present deterministic tie-retaining map.

Relevant published computational records concerning deleted edges in bicliques, mixed majority/minority complete graphs, ordinary majority on tripartite networks, and excitable bicliques differ by update rule or graph. Comparison of hypotheses and conclusions, not mere title mismatch, finds no displayed result subsuming this claim. Searches cannot prove novelty and older unindexed equivalents remain possible.

## Value — PASS

One rule-defective vertex is a natural structural perturbation of the standard majority automaton. The result reveals a counterintuitive zero/positive transition in oscillation under changing the number of ordinary conformists in the contrarian's shore: guaranteed period four for a single marked vertex, complete oscillation suppression upon adding one conformist, and restoration of a macroscopic period-two attraction basin upon adding a second. Beyond merely finding the attractor types, the exact all-size result proves the oscillation basin is *identical as a set of labelled initial states* to that for the original all-conformist graph once the shore has at least three vertices, with explicit parity corrections and full individual-basin sizes. These statements measure robustness and criticality of a local defect in an infinite natural graph family.

## Limits

Other tie policies, two or more contrarians, noncomplete bipartite graphs and stochastic versions are not classified. The older 2009 primary full text was not inspected; the originality assessment is contingent on available material. The mathematical proof and programmatic tests are available for independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
