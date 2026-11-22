# Review of the sharp comaximal-hypergraph degree-mode transition

## Correctness — PASS

The fixed-vertex degree formula follows from three independent combinatorial constraints after reduction modulo the Jacobson radical: a private coordinate for the fixed vertex, nonzero coverage at every complementary coordinate, and a private complementary coordinate for each other member. The first is a difference of products; the third is inclusion–exclusion over missing private coordinates. The factor of \(j^{k-1}\) counts lifts of the remaining vertices, and division by \((k-1)!\) removes only ordering, since private coordinates force distinct supports. For the Boolean rank-three case, the product simplifies to an explicit two-factor expression. The all-\(n\) maximum is proved by strict ratios: support codimension at least five is dominated, codimension two loses to three for \(n\ge5\), and four overtakes three exactly when \((4/3)^{n-4}>7\), beginning at \(n=11\). Direct enumeration verifies all vertex degrees in products through eight binary factors and heterogeneous/nonreduced small cases, and finite mode checks agree through thirty factors. The infinite assertion rests on the algebraic inequalities, not on finite tests.

## Originality — PASS, with historical-priority qualification

Mehdi-Nezhad (2026) proves that hyperedges correspond to irredundant co-support coverings and determines the blow-up and automorphism structure, but does not state the all-residue-profile individual degree formula or the maximum-degree mode transition. Selvakumar–Amritha (2020) study the same edges, including a regularity criterion at maximal uniformity \(k=n\), but not the three-uniform degree spectrum across arbitrary product length. Classical minimal-cover enumerations and an earlier exact ring-theoretic *total-edge* count are credited as already covered. The new fixed-vertex formula is a strict refinement: a total edge count controls only the weighted sum of degrees, while the sharp maximizing-stratum transition depends on their separate values. Searches for equivalent rooted-cover counts, degree-stratified hypergraphs and the dimension-eleven threshold did not identify a stronger covering theorem. The possible existence of historical enumerations under another name is a residual risk; absence from search results is not itself novelty proof.

## Value — PASS

Incidence degrees are intrinsic, natural hypergraph invariants, and the largest incidence degree controls local incidence concentration in these ring-derived hypergraphs. The first genuinely non-graph uniformity, \(k=3\), admits a sharp all-dimensional optimization theorem whose maximizing support changes twice and stabilizes at codimension four, with the nontrivial second switch at exactly eleven field factors. Its detailed vertex-degree distribution distinguishes support layers that a total edge count does not. The result is an exact structural boundary, not an arbitrary numerical sample or a claim of a general theorem for arbitrary hypergraphs.

## Scope and caveats

The classification of the maximizing stratum is limited to the three-uniform minimal comaximal hypergraph of Boolean product rings. The general fixed-vertex degree formula applies to any finite commutative ring and any \(2\le k\le n\); it does not solve the optimization for arbitrary heterogeneous residue sizes. A previously known total-edge count is used only for computational consistency and is not a novel finding. Historical priority and external mathematical validation have not been independently established.

Self-review: passed. Independent audit: not yet performed.
