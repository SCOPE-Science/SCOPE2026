# Scientific review: consecutive dual cut complexes of the Petersen line graph

## Correctness — PASS

The precisely defined graph and simplicial face condition are rebuilt from first principles in the included `verify.py`. There are 767 and 2,457 nonempty dual faces. Complete discrete-Morse matchings have 285 and 916 pairs and leave one vertex together with 196 critical two-cells or 624 critical three-cells; the entire reversed-Hasse directed graphs (2,355 and 9,690 covers) were independently checked for acyclicity by topological sorting. Standard discrete Morse theory proves the integral sphere-wedge homotopy types. Integral combinatorial Alexander duality proves the stated cut-side homology ranks. The separate mod-two cut-side rank checker corroborates, not replaces, the integral proof.

## Originality — PASS against inspected evidence

The closest published articles are Bayer et al., *Topology of Cut Complexes of Graphs* (arXiv:2304.13675) and *Topology of Cut Complexes II* (arXiv:2407.08158). They define the relevant cut complexes and cover multiple graph families but not the exact dual topology of the line graph of Petersen. The published Petersen four-cut result concerns ten rather than fifteen vertices. The cuboctahedral three-cut result concerns a distinct line graph and cut parameter. A radius-three intrinsic Čech result uses the same Petersen line graph but a nonequivalent complex. General girth-at-least-five four-cut theorems exclude this graph, which contains triangles; triangular-graph formulas concern the line graphs of complete graphs. Equivalent unknown calculations remain possible; absence of search results alone does not certify priority.

## Value — PASS

This is a complete, natural finite classification of both adjacent cut thresholds in the canonical fifteen-vertex edge-overlap graph of Petersen. The dual sphere wedges describe exact integral homotopy, and Alexander duality yields all original cut-side integral homology. The high-dimensional dual faces reflect natural Petersen cycle geometry, so the fact is not a routine parameter renaming or arbitrary slice. The result deliberately makes no general-family, equivariant, or cut-side homotopy claim.

## Limitations

Finite exhaustive code is essential to the proof. The independent cut-side rank check uses the same graph constructor, and no independent expert audit was carried out. The published-finding corpus and literature comparison is best-knowledge, not proof that no unindexed equivalent exists.

Self-review: passed. Independent audit: not yet performed.
