# Scientific review

## Correctness

**PASS.** The claim is finite and fully quantified: all \(3^{10}=59049\) labelled colorings of the exact Kneser presentation \(KG(5,2)\) are traced. The update is specified by four exhaustive cases. The functional-graph algorithm correctly computes first repetition and hence minimal periodic-entry time and least period for every initial coloring. Independent tuple-level orbit tracing reproduces every table cell; a third implementation on the nontrivially different pentagon–star presentation reproduces the period spectrum and all entry-time layers. The symmetry classification follows from an explicit proof of the \(S_5\) automorphism group and enumeration of 120 induced permutations. Extrema and orbit counts are checked against the complete state totals, not just a sample. The code is part of the result package, and printed outcomes were obtained by running it.

## Originality

**PASS, with bounded historical risk.** The 1978 Greenberg–Hastings model, 1993 excitable-media results, and the arbitrary-graph synchronization and circulation theorem of Gravner–Lyu–Sivakoff (2016 preprint) provide existing qualitative theory, which is acknowledged. The full text of the arbitrary-graph theorem's relevant sections and proof was inspected: it states a circulation criterion and asymptotic rate but not the present Petersen exact temporal census or the two maximal-delay symmetry orbits. The graph-theoretic reference provides the graph's 5-, 6-, 8-, and 9-cycles and automorphism group but no excitation census. Focused published-source and mathematical-record searches under Petersen, Kneser, Greenberg–Hastings, and 3-state excitation aliases found no exact table or stronger covering theorem. The nonmatching previous results concern different graphs, different cellular rules, or different mathematical invariants; their statements do not imply the numeric census. A missing full older source or unindexed equivalent remains a priority risk, not a reason to claim independent novelty certification.

## Mathematical value

**PASS.** The Petersen graph is the smallest cubic girth-five cage, a canonical compact network with highly overlapping cycles of four different lengths. The complete basin-by-entrance-time census is a natural finite dynamical invariant resolving its global transient behavior, beyond the qualitative nonconservative circulation criterion. The graph has six- and nine-cycles, yet its excitation dynamics has no primitive periods six or nine; it has 60 period-eight orbits. In addition, the extremal first-entry population splits into exactly two symmetry types, a structural classification not supplied by raw simulation frequencies. These precise facts provide a reproducible benchmark for graph-wave classifications and symmetry-aware approaches, rather than an arbitrary subfamily or a retabulation of known cycle counts.

## Closest work and limits

Most relevant: Gravner–Lyu–Sivakoff, arXiv:1610.07320, especially their Lemma 1 and Theorem 3, whose full accessible text was read. Foundational but less directly comparable: Greenberg–Hastings (1978) and Durrett–Griffeath (1993), available only through abstracts for this comparison. Petersen ordinary cycle data and automorphism group come from the graph reference. No claim is made for larger graph families or to external priority certification. Independent human assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
