# Scientific review: degree-bounded open-adjacency types

## Correctness — PASS

The statement quantifies over every finite simple graph of maximum degree at most \(d\) and every size-\(m\) marked set, not merely bipartite graphs. A degree incidence budget imposes a sharp cardinality-layer upper bound. A uniform-hypergraph exchange lemma balances the partial layer, and a marked matching/path/triangle plus independent witnesses simultaneously realizes the optimal trace family *and* gives an extremal host with exactly one vertex per trace. The proof handles \(d=0\), singletons, partial layer thresholds, and the full Boolean layer. Independent computations from the embedded code cover 2,097,151 graph/marked-set cases with up to six graph vertices, all subset families on four marks, and explicit extremizers across large parameter ranges. These are finite checks; the all-size statement depends on the proof.

## Originality — PASS within inspected evidence

Comparisons used searchable previous claims, multiple semantic searches for degree-bounded neighborhoods and incidence-limited set systems, and mathematical reading of arXiv:2607.16889 and arXiv:2301.04217v2. The 2026 paper proves exact *closed*-neighborhood bounds under treewidth/pathwidth assumptions; the 2023 paper proves *open*-neighborhood bounds using twin-width, not maximum degree. Width-restricted results do not imply the exact formula for all maximum-degree-\(d\) graphs. The closest recorded cyclomatic-budget trace bound has an unrestricted cycle budget and therefore is not a specialization. A relevant 2025 abstract was checked, but not its full text. Historical priority remains provisional because unavailable sources and some older records may exist.

## Value — PASS

The theorem computes a natural exact invariant for a hereditary sparse class, identifies all binomial degree-budget transitions, gives the exact stable coefficient \((d+1)/2\), characterizes the precise shattering threshold and complete layers, and proves optimal identifying hosts with no redundant vertices. Unlike a qualitative \(O_d(m)\) estimate, each equality and boundary can guide sharp neighborhood-type calculations or identifying-set constructions.

## Scope and risks

Only finite, undirected, simple, potentially disconnected graphs, **open** neighborhoods, and a maximum-degree upper bound are covered. No uniqueness of extremizing graphs is asserted. The original literature comparison is evidence-based, not absolute historical priority verification; an independent check is still required.

Self-review: passed. Independent audit: not yet performed.
