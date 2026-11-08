# Scientific review: Five-class connectivity census of three-player binary games

## Correctness — PASS

A strict three-player binary best-response graph is an arbitrary orientation of the twelve edges of the three-cube. The two structural implications have self-contained geometric proofs by sink location and source/sink bipartition. The complete 4096-orientation enumeration, class labels, and 112 symmetry classes are checked by the embedded standard-library verifier. Independent reverse graph searches, topological sorting, Burnside counting, and exact sink-factorial moments check critical computations without statistical inference. The exact domain excludes ties and larger games.

## Originality — PASS, with priority risk

The connected and super-connected definitions and asymptotic typicality results originate with Johnston, Savery, Scott and Tarbush (arXiv:2309.10609, September 19, 2023); their full accessible text's Appendix H gives simulations rather than this exact table. Fabrikant, Jaggard and Schapira (2013, Lemma 5) already prove the weak acyclicity of strict three-player binary games with an equilibrium, so that implication and the general weak-acyclicity concept are expressly prior work. No checked source gave this five-class joint census, orbit breakdown, or the combined structural restrictions as stated. Existing acyclic-orientation and cube unique-sink classifications make an independently published equivalent possible; an unindexed table remains the principal originality risk. The result is not claimed as independently certified.

## Value — PASS

This is the smallest three-player binary game size, with 4096 possible response-direction graphs and nontrivial separation of connected, super-connected and acyclic dynamics. The exact connected proportion among games having equilibria is \(1246/1567\), while the exact super-connected proportion is only \(192/1567\); these provide finite-scale benchmarks for existing asymptotic theorems and replace sampling uncertainty. The no-cyclic-nonconnected and no-acyclic-super-connected restrictions are sharp structural information that a table of marginal counts would not supply. No extrapolation to other game sizes is made.

## Closest literature and remaining limits

The primary game-connectivity paper includes the definitions, large-player results and simulations for small samples, but not these exact joint counts in the inspected text. The 2013 weak-acyclicity lemma provides a known part of the result, not the remaining joint classification. Graph-orientation literature may hide equivalent combinatorial counts; no comprehensive publication-priority guarantee is possible.

Self-review: passed. Independent audit: not yet performed.
