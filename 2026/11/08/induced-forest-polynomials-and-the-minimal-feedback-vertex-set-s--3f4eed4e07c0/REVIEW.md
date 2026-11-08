# Scientific review

## Correctness
PASS. The proof gives a complete shore-cardinality partition: three vertices on each shore force at least six edges on six vertices and therefore a cycle; two versus four force a rectangle. The remaining \((2,2)\) and \((2,3)\) cases are exactly characterized by matched-index overlaps. Every counted class is disjoint after the two-vertex overlap subtraction; each maximal configuration is shown maximal and each other forest is explicitly enlarged. Duality with inclusion-minimal feedback vertex sets is exact. Literal exhaustive checks cover all \(87296\) subsets in five graph orders.

## Originality
PASS on the accessible evidence, with provisional publication priority. The graph occurs in deranged-matching enumeration [2], but that work concerns perfect matchings, not forests. The 2022 maximum-minimal-feedback-set work [1] studies algorithms and complexity, not this labelled crown-graph classification. The 2025 balanced-bipartite forest theorem [3] covers the maximum-forest cardinality \(n+1\), hence the minimum feedback vertex set cardinality \(n-1\) here; for odd \(n\) it further constrains the maximum forest structure. Those portions are acknowledged rather than claimed. The present all-subset enumerator, nonmaximum inclusion-maximal induced-path class, and full minimal-feedback-set spectrum are not stated in the inspected primary texts. Database and broader-description searches found no directly covering item. Residual risk: unindexed equivalent enumerations or specialized dense-bipartite results.

## Mathematical value
PASS. The maximum-minimal feedback vertex set problem asks about large minimal cycle transversals. This family exhibits an unbounded exact difference \(n-4\) between largest and smallest minimal transversal sizes while admitting a complete two-class structural classification and counts. The full induced-forest polynomial additionally describes the entire acyclic-subset complex, rather than reproducing a known extremal size. These naturally motivated graph invariants are not arbitrary parameter slices.

## Closest literature and limitations
[1] arXiv:2208.01953 (minimal feedback vertex sets and algorithmic complexity); [2] arXiv:2209.11319 (deranged matchings in the same graph family); [3] arXiv:2501.05145 (broader 2025 maximum induced-forest cardinality theorem, partially subsuming the scalar minimum and odd-order maximum-structure consequences). The current proof is for a full deleted matching and for labelled vertex subsets. Equivalent literature under other terminology remains possible; no independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
