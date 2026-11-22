# Scientific review of the Franklin paired-domination exchange theorem

## Correctness — PASS
The explicit vertex-and-edge definition reconstructs the standard Franklin graph. Exact domination and induced-perfect-matching tests cover all possible smaller candidates and every six-vertex candidate. A second, nonidentical bipartite-incidence implementation confirms the 184 minimum sets, one-exchange graph on 984 edges, complete pairwise Johnson-isometry property and non-matroid witness. The local target-improvement test checks all 33,672 ordered pairs, so it proves a shortest path for each pair; BFS independently checks all 16,836 unordered distances. Finite conclusions only, with no extrapolation to all cubic bipartite graphs.

## Originality — PASS (best-knowledge, priority risk retained)
The closest published Franklin-specific result establishes only the paired-domination **number** six among the five twelve-vertex cubic bipartite isomorphism classes; its result file has been read and it does not state or imply the 184-optimum census or exchange metric. Full primary text of the 2021 paired-domination complexity paper and 2023 shortest dominating-set reconfiguration paper was inspected: they establish different problem-wide complexity/algorithmic facts, not this finite exchange system. A 2026 sharp bound covers possible optimum cardinalities but not exact graph-specific configurations or geodesics. Related paired-domination and Johnson-isometric findings concern other graphs or predicates. Neither exact numeric lookup nor equivalent-formulation searches identified covering prior work. Unindexed priority remains possible.

## Value — PASS
The Franklin graph is singled out by the existing complete order-twelve cubic bipartite classification as the uniquely sharp paired-domination example. Precisely for this natural extremal instance, the 184 optimal placements admit a globally exact replacement metric despite lacking the much stronger matroid basis-exchange property. This separates efficient monotone optimal relocation from matroidal structure, with complete and reusable exact finite data. The bipartite token-slide impossibility is elementary context, not the novelty claim. A generalization or external theorem is not claimed.

## Scope and limits
The certificate concerns one specific twelve-vertex graph and exhaustive finite enumeration, and the proof depends on the packaged self-contained checkers. Bibliographic coverage may omit unindexed or inaccessible sources. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
