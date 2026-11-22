# Scientific review

## Correctness

PASS. The six-regular threshold-four infection rule is exactly parallel deletion of residual vertices of degree at most two, so success means an empty induced three-core. A successful set is inclusion-minimal precisely when every one-seed deletion fails. Two complete and independent enumerations over all \(65,536\) initial subsets per graph, one in C++ using forward infection and the other in Python using core peeling, agreed on all cardinality-by-completion-time counts. In particular, there are \(2,160\) minimal Shrikhande six-seeds, \(64\) minimal seven-seeds, and \(864\) minimal rook six-seeds with no other minimal cardinalities. The independently enumerated affine orbit and seven-set degree signature agree exactly.

## Originality

PASS under the examined literature and indexed-record comparisons, not a claim of absolute publication priority. Coja-Oghlan et al. (arXiv:1306.2465) study general contagious sets and expanders; Guggiola and Semerjian (arXiv:1407.7361) study the asymptotic regular-graph core-removal problem; Bidgoli et al. (arXiv:1905.01942, Theorem 2.1) already establish the rook graph's minimum seed cardinality six. The last fact is explicitly credited. None of the inspected relevant full texts gives the exact two-graph irredundant-set and completion-time census or the single-orbit seven-set classification. Indexed related results concerning static site percolation, induced forests, or reversible majority dynamics do not imply these threshold-four claims. Residual risk: an unindexed finite census could subsume them.

## Value

PASS. Inclusion-minimal versus minimum-cardinality contagious sets are naturally distinct optimization objects. The exceptional seven-seed orbit demonstrates that two sixteen-vertex graphs with identical strongly regular parameters and minimum contagious-set size can have different maximum irredundant seed sizes; the induced-degree signature supplies a graph-theoretic recognition rule. The exact propagation-time separation is relevant to speed-sensitive seed selection on these canonical networks. Scope remains deliberately finite; no general theorem is promised.

## Limitations

The proof uses reproducible exhaustive finite computation, not formal proof-assistant certification; its assumptions and test coverage appear in the result and code. The historical search cannot exclude unpublished tables or inaccessible literature. The minimum rook seed size and the three-core connection are credited as established context, not claimed discoveries.

Self-review: passed. Independent audit: not yet performed.
