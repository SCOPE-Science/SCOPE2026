# Self-review

## Correctness — PASS
The defined graph and edge distances determine 24 domination witnesses and 276 edge-pair distinction witnesses, so each jointly feasible set is exactly a hitting set of 300 known constraints. Exhausting all 65,536 vertex subsets therefore proves the cardinality polynomial and absence of four-element joint solutions, provided the reconstructed graph and witness conditions agree with the definitions. The Python checker builds shortest-path signature vectors and checks edge coverage, while the independently written C++17 checker uses Floyd–Warshall and pairwise vertex-witness masks. Both agree on 512 minima of cardinality five and the full polynomial, and independently enumerate each move and run 512 all-root breadth-first searches. The Python verifier additionally exhausts graph automorphisms. No infinite extrapolation is made.

## Originality — PASS, provisional
The motivating 2022 primary paper introduces the joint invariant but covers classical graph families and some Cartesian products, not the Möbius–Kantor instance. The 2018 generalized Petersen edge-resolution paper studies a weaker condition and lacks a combined census. An accessible exact result for complete prisms treats the *same* invariant on a structurally different graph; its claims do not imply the present finite graph's configuration list. Full closely related records on Möbius–Kantor identifying-code slides and zero-forcing exchange graphs have different feasibility rules, optimum counts and reconfiguration state spaces. Actual indexed record and primary-literature searches found no covering statement. Residual risk: unindexed or inaccessible work may have the same result; negative retrieval does not certify priority.

## Mathematical value — PASS
The original invariant couples two natural and competing edge-sensor requirements: complete local edge surveillance and unique edge localization. On a canonical cubic vertex-transitive host, the requirements individually have optimum size four yet cannot be combined at that cost. The sharp one-extra-sensor threshold, the complete labelled polynomial, eight symmetry classes and nontrivial connected self-centered *adjacency-constrained* mobility are useful configuration-level information not entailed by either scalar minimum. This is a motivated exact finite classification; no claim of a universal or paper-sized theorem is required.

## Closest literature and limits
See RESULT.md References [1]–[5], especially the 2022 definition and 2018 edge-resolution study. The proof is finite exhaustive; it does not cover arbitrary generalized Petersen graphs, and complete publication-priority clearance remains outstanding.

Self-review: passed. Independent audit: not yet performed.
