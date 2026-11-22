# Scientific assessment of the finite triangular-graph excitation classification

## Correctness — PASS

The claim is a precise, finite statement about two fully defined update maps on the ten vertices of \(T(5)\). `verification/census.py` classifies every one of the \(59{,}049\) states using full functional-graph indegree pruning. `verification/independent.cpp` independently rebuilds the maps and classifies every initial state by Floyd's cycle algorithm, checking both entire transient tables and the pointwise period equality. `verification/symmetry.py` traverses every primitive-three temporal cycle under all \(120\) induced vertex permutations, and the proof identifies this as the complete automorphism group via its five intrinsic maximal four-cliques. All actual package programs were executed successfully; exact reference data files and array invariants were compared. The argument applies to this finite graph only.

## Originality — PASS, qualified

published-finding corpus searches used aliases \(T(5)\), \(J(5,2)\), \(L(K_5)\), *triangular graph*, complementary Petersen graph, CCA, Greenberg–Hastings, and orbit multiplicities, and the current accessible prior claims were checked for coverage. The closest published exact comparison studies the Petersen graph itself, giving 4,800 mismatched periods there, not its triangular-graph complement. The biclique theorem establishes period matching on graphs not isomorphic to this one; the \(KG(6,2)\) theorem is about fifteen vertices and disjointness adjacency. Gravner–Lyu–Sivakoff (2018), Theorem 3, concerns qualitative synchronization and excitation-rate invariants, not the finite first-entry and symmetry census. No located primary source or accessible prior claim implies the full new table. An unindexed prior exact enumeration remains a residual priority risk, and that uncertainty is not represented as proof of uniqueness.

## Value — PASS

The graph \(T(5)\) is the strongly regular ten-vertex complement of the Petersen graph. The exact transition from 4,800 mismatched eventual periods on the Petersen graph to *pointwise matching* periods and common recurrent waves on its complement is a motivated comparison of two canonical interacting media. The 118 spatial wave classes and the complete, sharply different first-entry distributions are natural dynamical invariants of that comparison, rather than an arbitrary bit slice or a mere numerical bound.

## Scope and limitations

Proof consists of complete and reproducible enumeration on a fixed finite graph; no theorem for all line graphs, all complementary pairs, alternative thresholds or other color counts is inferred. Independent external review and complete historical-priority certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
