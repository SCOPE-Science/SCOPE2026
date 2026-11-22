# Scientific assessment

## Correctness — PASS

The result concerns the explicitly defined length-three, two-premise Horn rules and the canonical proper meet-irreducibles of their closure lattices. The central path bijection uses the unique largest missing atom and a maximal independent prefix; the cyclic criterion uses the number of unselected vertices that can be inserted without violating independence. These characterizations cover all boundary cases, including the empty path and all rings with at least three vertices. The two bivariate generating functions follow from weighted maximal-independent-set recurrences and labelled cyclic gap compositions, respectively. The all-length growth laws follow from their rational singularities. The standalone Python checker directly tests the meet-irreducibility definition and the full omitted-atom distributions, but finite tests are not treated as the infinite proof.

## Originality — PASS within checked evidence

Babin (2026, arXiv:2607.18534) already gives the general maximal-omitter lemma, hardness of general canonical-representation checking, and the definitions. Defrain, Ohana and Vilmin (2025, arXiv:2506.24052) treat bounded-degree acyclic Horn representation translation in general. Earlier enumerations of maximal independent sets of paths and cycles, including their Padovan/Perrin totals and cardinality refinements, are prior work. The claimed distinction is the explicit **Horn canonical-model** normal form for consecutive path and ring bases, the additional cyclic one-undominated-vertex family, both complete omitted-atom series, and the contrasting leading polynomial growth factors. Accessible full-text material did not supply these results or imply them via an exact published parametric theorem. One close published note about cycle maximal-independent-set contexts was identified in a database summary, but its complete public repository text could not be retrieved; this leaves residual historical-priority risk. The absence of a search hit is not a uniqueness proof.

## Value — PASS

The exact minimal intersection-generating family is a natural invariant in Horn representation conversion, rather than an arbitrarily chosen graph statistic. The theorem computes the entire size spectrum of that canonical family on the elementary local two-premise propagation bases and shows that cyclic closure changes its leading growth by a factor linear in the number of atoms. This quantifies the gap between all models (golden-ratio growth) and characteristic models (plastic-root growth), while furnishing explicit canonical representatives. The result does not claim a general hardness improvement, a broad algorithmic advance, or a new Padovan/Perrin count independently of its closure interpretation.

## Closest sources and limitations

- Babin, *Completeness of Canonical Closure Representations Is coNP-Complete* (2026), https://arxiv.org/abs/2607.18534 — general theorem and maximal-omitter machinery
- Defrain, Ohana, Vilmin, *Translating between the representations of an acyclic convex geometry of bounded degree* (2025), https://arxiv.org/abs/2506.24052 — general bounded-degree translation framework
- Bisdorff and Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph* (2008), https://orbilu.uni.lu/handle/10993/387 — Perrin cycle enumeration is known
- *On the existence and the number of independent (1,2)-dominating sets in the G-join of graphs* (2020), https://doi.org/10.1016/j.amc.2020.125155 — known path/cycle cardinality refinements

Historical priority of the precise Horn normal forms remains provisional, and the checker exhausts only finite sizes. No independent scientific or literature audit has occurred.

Self-review: passed. Independent audit: not yet performed.
