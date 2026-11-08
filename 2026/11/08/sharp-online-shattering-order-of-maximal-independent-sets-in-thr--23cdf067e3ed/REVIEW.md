# Scientific review: sharp online shattering on threshold graphs

## Correctness — PASS

The concept parametrization is exact: all zero-vertices, or precisely one one-vertex together with all subsequent zeros, are exactly the maximal independent sets. Consequently one-vertex membership queries are one-hot and zero-vertex membership queries are ordered prefix tests. This proves VC dimension one for every graph with at least one creation-one and zero otherwise. The interval rank recursion follows from the defining complete mistake-tree recurrence; one-hot queries cannot give a root of depth two. At depth above the last one, every query must be a proper prefix cut. The first \(h-1\) levels therefore require \(2^{h-1}-1\) distinct noninitial zero-vertices, while the leaves require \(2^h\) distinct concepts and hence \(2^h-1\) one-vertices. The exhibited word meets both inequalities and has a balanced depth-\(h\) tree. Equality forces the alternating block placement and gives uniqueness. The elementary proof applies for every integer \(h\ge1\); computational checks are only corroboration.

## Originality — PASS within inspected evidence

The closest specific prior paper, Gurski–Rehs (2017, arXiv:1710.08953), already gives the creation-sequence maximal-independent-set enumeration (Observation 8, Theorem 25). It does **not** report the membership-query VC/Littlestone ranks, the exact interval-splitting recurrence, the minimum order \(3\cdot 2^{h-1}-1\), or unique minimizers. Alon–Livni–Malliaris–Moran (2018, arXiv:1806.00949) develops the general online-rank framework and threshold concepts; its relevant text concerns private learnability and threshold functions rather than graph-order-optimal embeddings into maximal-independent-set families. Earlier known examples of large static–online gaps for other concept systems do not logically entail the threshold-graph-specific extremal order and rigidity. Searches for the exact expression, graph family, and alternate one-hot/prefix description did not return a dominating statement. Residual risk: the optimization might appear under a different interpretation of nested one-hot/prefix decision trees, or in unsurveyed literature.

## Mathematical value — PASS

The quantitative question is intrinsic: how many graph vertices are necessary for a class of *maximal feasible configurations* to support \(h\) adaptive membership mistakes when every threshold graph has VC dimension at most one? The answer is a sharp exponential order threshold together with a unique extremal isomorphism type, not just a logarithmic lower-bound example. The interval recurrence also computes exact online rank on every threshold graph without enumerating mistake trees, and the uniqueness proof reveals the necessary allocation of creation vertices into witness hypotheses and branching-query separators. The result therefore refines the familiar finite-threshold observation with a nontrivial graph-resource constraint. No claim of a general-purpose learning theorem or a randomized mistake bound is made.

## Remaining limits

The result is confined to finite threshold graphs and deterministic complete-tree Littlestone rank. Full historical priority cannot be certified from database searches alone. The 2,047-word finite checker reaches only eleven vertices and does not replace the unrestricted proof.

Self-review: passed. Independent audit: not yet performed.
