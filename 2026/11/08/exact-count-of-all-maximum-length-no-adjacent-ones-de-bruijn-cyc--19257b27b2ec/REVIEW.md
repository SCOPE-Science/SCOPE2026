# Scientific review: complete enumeration of optimal constrained de Bruijn cycles

## Correctness — PASS

The known optimal support is exactly the set of length-\(n\) cyclically no-`11` binary words; this premise is established by Chee et al. (arXiv:2403.01454, Corollaries 2.12 and 2.14) under exchanging zeros and ones. The derived overlap graph has degrees \(1\) except at the vertices beginning and ending in `0`, where they equal \(2\). Its unique outgoing arcs from nonbranch vertices append `0`, reaching a branch. The bijection between full-graph rooted in-arborescences and those of the two-outgoing-arc compressed multigraph is proved, including acyclicity and parallel-arc distinctions. BEST and the directed matrix-tree theorem therefore give a correct exact determinant for the number of *all* optimal cyclic words modulo rotation. This is a proof for all \(n\ge2\), not an inference from finite experiments.

The final extracted computations reproduced exact determinant values via C++ modular CRT and independently written Python Bareiss (both compressed and full-graph), plus exhaustive short circular-word and balanced-support tests. The C++ modulus product exceeds a proven numerical bound and the counts through \(n=15\) are exact.

## Originality — PASS, qualified

The 2024 source decisively covers maximum length, the Lucas count of admissible windows, and uniqueness of the maximizing support, so none of those assertions is presented as original. Moreno–Matamala (2004/2007) and Sawada–Williams–Wong (2016) already develop constrained-language cycles. The 2024 paper Theorem 3.1 generates a lower-bounded family of optimal cycles, whereas its Section 4 enumerates **word/necklace populations**, not the total population of **all distinct optimal cycles**. The present compressed Laplacian determinant, proof of exact correspondence, and full integer census up to length 15 do not follow from that paper's claimed number of constructive choices. BEST/matrix-tree are explicitly credited as standard tools.

There remains genuine risk of unindexed older full-tour tables, or a previously published equivalent cofactor for the golden-mean shift. We do not equate an unsuccessful search with priority proof. The narrowly stated exact full-cycle enumeration nevertheless survives comparison of the strongest relevant theorems inspected.

## Value — PASS

For maximum-length constrained de Bruijn sequences, knowing a single efficient construction or even many choices does not tell how many inequivalent optimal cyclic schedules exist. The exact total is a natural invariant for diversity, uniform selection, and the complexity of the full solution space. A forced-degree-one-corridor argument reduces the arborescence count to a graph with \(F_{n-1}\) rather than \(F_{n+1}\) vertices, enabling a reproducible complete numerical census of orders through \(15\). Unlike a routine restatement of the known maximum length, this evaluates a motivated previously unreported population size at each order, with an all-order exact counting expression.

## Compared literature and remaining limitations

- Moreno–Matamala: https://arxiv.org/abs/0711.1695 (restricted de Bruijn Euler constructions; WG 2004 antecedent)
- Sawada–Williams–Wong: https://doi.org/10.37236/5517 (specified cyclic forbidden-substring families)
- Chee et al.: https://arxiv.org/abs/2403.01454 (maximal length and unique support already proved; many constructions, not an evaluated total cycle census)

The determinant counts all orders; only the evaluated integers through length 15 are certified by included programs. Independent mathematical and historical-priority audits remain outstanding.

Self-review: passed. Independent audit: not yet performed.
