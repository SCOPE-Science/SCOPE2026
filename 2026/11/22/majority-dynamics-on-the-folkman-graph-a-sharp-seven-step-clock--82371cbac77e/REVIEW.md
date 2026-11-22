# Scientific review

## Correctness — PASS

The finite graph, vertex labeling, time convention and strict-majority-with-tie-retention rule are explicit. A complete enumeration of all \(2^{20}\) labelled states was independently implemented twice: adjacency-vector iterate matching and a bitmask/indegree functional digraph decomposition. The two methods agree on 4,036 fixed states, 351 temporal two-cycles, all first-entry-time populations, all 4,387 basin sizes, and the sharp seven-update witness `64030`. A separate spatial-generator action verifies 44 fixed and eight two-cycle geometric classes. The proof is a replayable exhaustive finite computation, not an infinite result.

## Originality — PASS (qualified)

Folkman (1967) specifies the semisymmetric graph; the Goles–Olivos finite threshold theorem, as recalled by Benjamini et al. (2014), supplies the general period-two restriction. Neither establishes exact orbit, basin, transient or symmetry counts for this graph. Directly inspected complete published dodecahedral and prism/Desargues results concern nonisomorphic three-regular twenty-vertex graphs; they do not imply the Folkman counts by specialization. published-finding corpus searches of graph name, subdivided-double synonyms, claimed counts and majority terminology did not surface an exact equivalent. The original Folkman article was read at abstract level only, and unindexed exact work remains a genuine historical-priority uncertainty.

## Value — PASS

The Folkman graph is the canonical smallest semisymmetric graph. Its full attraction landscape is a motivated, graph-specific invariant rather than a routine example: only 351 primitive oscillations exist despite 4,036 equilibria, and more than nine-tenths of configurations settle at equilibria, with two enormous unanimous basins and a complete 26-size spectrum. The 52 geometric recurrent classes and sharp relaxation time make the result useful for precise comparisons with other natural regular networks. No generalization to larger graphs is suggested without proof.

## Scientific limits

The classification is for one labelled twenty-vertex graph and deterministic synchronous binary rule only. Reproduction requires a C++17 compiler and the included source files; the computed counts are not independently externally audited. Some historical sources were inaccessible in full, so priority is qualified.

Self-review: passed. Independent audit: not yet performed.
