# Scientific review: first degree–Tutte twins in unicyclic graph-nilmanifold cohomology

## Correctness: PASS

The statement is restricted to connected simple unicyclic graphs on three through six vertices. A labelled exhaustive enumeration, quotienting by all vertex relabelings, finds 1, 2, 5 and 13 isomorphism classes at the four consecutive sizes. After grouping by cycle length and degree multiset, precisely two collision pairs occur at size six. The bridge contraction formula proves that cycle length and order completely specify the Tutte polynomial among unicyclic graphs. Canonical signatures match all four declared edge lists.

For each of the four graphs, the rank computation uses the Chevalley–Eilenberg differential on the entire 4096-element exterior basis, split into invariant vertex-support subcomplexes. All ranks are exact over the rationals, not estimates from modular calculations. The differential squares to zero on every monomial; the resulting Betti vectors satisfy rank-nullity, Euler characteristic zero and Poincaré duality. The separate atlas/SymPy rational computation reproduces all four vectors. The passage from Lie algebra cohomology to graph nilmanifold rational cohomology uses the established Nomizu identification. The proof makes no infinite-range assertion.

## Originality: PASS, with remaining priority uncertainty

Aldi–Butler–Gardiner–Grandini–Lichtenwalner–Pan (arXiv:2402.14188, Section 3, Theorems 17 and 23) already provide the general vertex-support decomposition and an exact formula for third-degree Betti numbers of arbitrary graphs. That contribution, together with all low-degree consequences, is recognized as prior work. Example 24 there concerns a four-cycle with a single pendant path of length two; its degree multiset is different from the two pairs here. Aldi and collaborators (arXiv:2611.17014, submitted 2026-11-12, Sections 1 and 5, Table 6) give full Poincaré polynomials for paths rather than six-vertex unicyclic twin pairs. Their general lower bound for arbitrary graph nilmanifolds does not fix these exact values.

The claimed addition is the **complete all-degree polynomials for the two nonisomorphic same-degree/same-Tutte pairs and the sharp exhaustive unicyclic cutoff**, not the cochain construction, the general low-degree formulas, or a broad implication for all graphs. Related published work on cohomological graph separations with different graph conditions does not directly imply this four-profile classification. Available mathematical-index and literature queries did not identify a previously tabulated equivalent; this does not establish exhaustive world-wide priority. A stronger unindexed computation or atlas remains a material residual risk.

## Mathematical value: PASS

Two standard, naturally coarser invariants—the degree sequence and entire Tutte polynomial—are simultaneously held fixed, yet graph-nilmanifold cohomology differs in *every* pair at the earliest possible unicyclic graph order. The exact full Betti vectors and total ranks distinguish two attachment geometries at each of two distinct girths, thus establish a small but complete and reproducible boundary result. These complete degree-by-degree tables are a specific reference for the more difficult problem of understanding graph cohomology beyond paths; the finite cutoff is not an arbitrary parameter choice. The result is not presented as a new general cohomology algorithm or an infinite family.

## Limitations and risk

The proof is finite and exact, but independent mathematical review and absolute priority assessment are not performed. It gives no integral torsion, cup products, general unicyclic recurrence, or manifold classification. The general low-degree values already follow from prior literature; the value resides in the joint minimality and complete higher-degree calculations.

Self-review: passed. Independent audit: not yet performed.
