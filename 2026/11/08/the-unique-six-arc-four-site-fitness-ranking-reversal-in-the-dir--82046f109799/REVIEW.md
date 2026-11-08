# Scientific review

## Correctness — PASS

The mutation-free birth–death process reduces, after cancelling a common reproduction normalization, to a finite Dirichlet system on nonempty proper mutant sets. Strong connectivity makes the absorption system nonsingular for positive mutant fitness. Exact symbolic elimination proves the displayed fixation-difference rational function for the witness graph; a strictly positive denominator and Descartes' rule give one crossing in \((3,4)\). Exhaustive isomorphism-reduced enumeration of all admissible graphs up to four vertices and six arcs establishes the precise minimum and uniqueness claims. The symbolic checker enumerates 113 nonidentically-zero pairwise comparisons, 112 with no positive shifted-numerator sign variation; the other is the stated pair. A separate standard-library rational solver checks the algebra at seven exact parameter values. The proof, rather than sampled checks, supplies the continuous-parameter conclusions.

## Originality — PASS, subject to stated historical risk

The foundational directed replacement model in Lieberman–Hauert–Nowak (2005) treats average-location fixation and graph-level selection behavior. Broom–Rychtář–Stadler (2009, 2011) study individual insertion sites on undirected rather than directed graphs; their results do not imply a unique directed four-vertex rank switch. Zhang (2014) studies special directed examples, and Adlam–Nowak (2014) studies aggregate behavior of randomly structured digraphs. Keller–Uğurlu (2024) analyzes martingale conditions and a two-vertex family under a stationarity-based selection policy. None of the inspected material establishes, implies, or tables the six-arc crossing classification. This is novelty relative to the inspected evidence, not a guarantee that no earlier uncatalogued exact computation exists. An inaccessible or unlocated historical small-digraph table remains a residual risk.

## Value — PASS

The initial site of a new advantageous mutation is a natural and consequential choice in structured populations. The result identifies the first possible reversal of relative site success as selective fitness changes, within an exact and explicitly delimited graph class. It provides a complete sharp minimum and uniqueness theorem, not an arbitrary isolated numerical instance. The direction and threshold of reversal are certified by exact formulas, offering a benchmark against heuristics based only on site centrality or neutral drift. It does not imply any conclusion for larger weighted graphs or for empirical evolution.

## Closest literature and limitations

See the six full citations in `RESULT.md`. In particular, the 2011 study's full text explicitly restricts its structural model to connected undirected graphs and gives approximate general-fitness vertex comparisons, not an exact directed census. The 2024 microscopic model allows directed matrices but selects using the stationary distribution, which is generally not uniform across vertices. The theorem is restricted to strongly connected loopless directed graphs with uniform weights on the arcs leaving each vertex, homogeneous fitness, and birth–death updating. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
