# Self-review

## Correctness

**PASS.** The proof accounts for every possible trace of size zero, one or at least two. Each marked vertex of marked degree at least two is charged to a marked edge, and each unmarked high-degree witness consumes two incidences. The subgraph cycle-space budget then proves \(p+q\le m-1+\beta(G)\), giving the stated upper bound. Connected triangular cacti attain it for every displayed parameter pair. Independently coded exhaustive finite tests match the claim. The proof, not the tests, establishes all sizes.

## Originality

**PASS within inspected evidence.** The closest current work establishes almost-linear open-neighborhood growth on broad monadically dependent classes, while an exact 2026 treewidth/pathwidth census explicitly treats *closed* neighborhoods. Qualitative bounded-expansion results do not fix an additive independent-cycle budget. Earlier sharp forest bounds cover only \(\beta(G)=0\); the sharp positive-cycle extension and simultaneous cactus extremizers are not implied by those statements. Search coverage and inaccessible historical sources remain residual risks; absolute priority is not certified.

## Value

**PASS.** Bounded cyclomatic number is the natural distance-to-forest parameter, and the number of adjacency types over a marked set is a direct finite-model-theoretic and neighborhood-complexity invariant. The theorem gives the exact coefficient, the exact price of each independent cycle, and tight witnesses in a very sparse graph subclass, rather than a qualitative big-O bound or a single numerical experiment.

## Limits

The extremal formula is asserted for \(m\ge\max\{1,3c\}\); smaller marked sets, equality classification and richer first-order types are not determined. The sources are compared only to the material actually accessible and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
