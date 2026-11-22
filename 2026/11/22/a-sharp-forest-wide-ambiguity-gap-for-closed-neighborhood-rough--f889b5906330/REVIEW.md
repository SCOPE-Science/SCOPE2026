# Scientific review

## Correctness

PASS. Every coloring of a forest is uniquely described by its bichromatic edge set together with one root color per component. Vertices with a monochromatic closed neighborhood are exactly the vertices not incident to the bichromatic edge set. This gives the exact edge-cover/parity formula. Augmenting any edge cover of the induced non-definite subforest with fixed edges incident to definite vertices is an injection into the edge covers of the whole forest. The resulting multiplicity gap is strict and matching forests attain it. Independent direct-subset and parity-enumerator checks cover all labeled isolate-free forests of at most five vertices and sampled larger trees. No finite exhaustive check is used to claim an infinite proof.

## Originality

PASS on the inspected evidence, with historical priority provisional. The March 2026 graph rough-set paper studies valid covering-based approximations, not inverse-fiber optimization; the 2020 neighborhood-based paper studies definitions and accuracy measures. The 2012 matroid interpretation concerns equivalence-relation granules. A published clique-bouquet observation-spectrum result is confined to that family, while available path and crown enumerations count different families or different invariants. The present exact parity count and sharp forest-wide stability bound are not implications of their stated claims. The 2020 neighborhood-approximation full text was not fully accessible from the primary host, and not all historical sources could be exhaustively verified.

## Value

PASS. Rough approximation maps discard input information; the cardinality of each inverse fiber is a direct quantitative measure of that information loss. This theorem identifies the unique worst possible observation on every finite forest, sharply quantifies the loss for every noncentral observation by its component support, and gives an exact all-fiber reconstruction via cuts and edge covers. The result applies to arbitrarily branching forests and arbitrary observation labels, not only paths or a small census.

## Remaining scientific limits

The graph must be a forest without isolated vertices, and this result is not asserted for cyclic graphs, arbitrary neighborhood systems or edge-cover counting complexity. Historical priority should be checked independently. The standalone checker supplies finite regression tests, not a substitute for the proof.

Self-review: passed. Independent audit: not yet performed.
