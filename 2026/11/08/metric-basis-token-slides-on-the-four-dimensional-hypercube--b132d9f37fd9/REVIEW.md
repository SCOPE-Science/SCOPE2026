# Scientific review: four-cube metric-basis token slides

## Correctness — PASS

The domain and update rule are specified without ambiguity. Equality of distance profiles is equivalent to a ternary null vector for the sign-row matrix. The signed-cofactor lemma proves that every rank-at-most-three sign-row matrix has a nonzero ternary null vector, giving a paper proof that the metric bases are exactly nonsingular four-row selections. An independent direct profile enumeration agrees. The precise input domain has \(1820\) four-subsets. The C++ check examines all of them, all legal adjacent bit flips, and a shortest-path search from every one of the \(928\) bases; the Python check uses signed displacements, validates all determinants, and enumerates the entire \(384\)-element cube-isometry group. Both reruns agree on the eight orbits, component structure and exact radius/diameter. Reproducibility is self-contained and uses exact arithmetic.

## Originality — PASS (historical priority qualified)

Ganesan's 2011 full note gives the four-cube's metric dimension \(4\) but no reconfiguration graph. Beardon's 2013 work provides a general linear resolvability criterion (abstract-level inspection), not an identified constrained-slide metric. The Laird–Tillquist–Becker–Lladser preprint's full web-rendered text (sections on tests, Gröbner/ILP methods, experiments and appendices) gives general resolution testing and does not determine the present slide-graph invariants. Nikolić–Čangalović–Grujičić's 2014 online paper treats symmetry of hypercube resolving sets and heuristics; only its abstract/presentation were accessible. Indexed mathematical research results closest in theme concern a different edge-multiset localization notion, directional localization, and a matroid basis-pair diameter rather than adjacent one-bit landmark moves in \(Q_4\). A matching exact relocation graph, dominating theorem, or table was not found. The claimed novelty is the *reconfiguration graph*, not the pre-existing minimum dimension or general null-vector criterion. Inaccessible full texts and unindexed results remain genuine residual risks.

## Value — PASS

The four-cube is the smallest high-symmetry hypercube for which minimum resolving bases have four landmarks. Moving one landmark by one network edge while retaining full distance identification is a natural dynamic sensor-relocation constraint. The exhaustive classification answers connectedness and *optimal* worst-case relocation cost, and the eight orbit types expose unequal mobility among configurations that have equal immediate degree. The \(928\)-state graph is not a handpicked parameter slice: it is all optimal solutions on this canonical host. The exact radius/eccentricity distribution provides a reusable small benchmark for constrained metric-basis exchange.

## Limitations and scope

The theorem concerns \(Q_4\) only; no higher-dimensional or independent human certification claim is made. The numerical part is a complete, reproducible finite case analysis, not an unbounded-family result. The full text of Nikolić–Čangalović–Grujičić and Beardon was not accessible for complete comparison, so priority cannot be asserted beyond accessible evidence. A failed search alone does not certify originality.

Self-review: passed. Independent audit: not yet performed.
