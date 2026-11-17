# Mathematical review

## Correctness — PASS

The Petersen graph is defined as \(KG(5,2)\); every neighbourhood has exactly three vertices and the update is uniquely defined. The proof covers all 1,024 configurations by the 34 complete \(S_5\)-orbits of five-vertex graphs, generated and checked by the standalone standard-library Python certificate. The exact identities \(T^6=T^4\), \(T^5\ne T^3\), the recurrent set of 124 states, the 14/55 Petersen fixed/two-cycle census, the eight recurrent symmetry classes, and three fiber sizes are verified by explicit exhaustive integer operations. A checked 20-vertex isomorphism establishes that the bipartite double is \(GP(10,3)\). The algebraic swap conjugacy \((u,T(v))\mapsto(v,T(u))\) proves 124 fixed configurations and 7,626 primitive two-cycles. Fibers of \(T^4\) imply the nine exact basin classes. An independently implemented C++ graph update exhausts all 1,048,576 configurations, reproducing the orbit counts, basin sizes, and sharp four-step clock. These are exact finite certificates, not probabilistic tests or extrapolated values.

## Originality — PASS, qualified

The general period-at-most-two statement is explicitly attributed to Goles–Olivos, as reviewed in the full text of Benjamini et al. (arXiv:1405.2486) and Kaaser et al. (MFCS 2016). The published Heawood majority classification instead has 58 recurrent symbols and sharp entry time two; the dodecahedral classification has 118 equilibria and a sharp seven-step entry clock. Their graph hypotheses do not apply to the Petersen/Desargues pair, and their conclusions do not imply the eight \(S_5\)-orbit types, weights 1/10/226, or the exact lifted basin spectrum. Searches for the graph names, the numerical counts, temporal aliases, covers, and prior exact tables did not identify a statement implying this result. This is support for qualified originality, not proof of global historical priority. The Goles–Olivos full text and unindexed enumerations remain priority risks.

## Mathematical value — PASS

The Petersen graph is a canonical cubic symmetric graph and the Desargues graph is its canonical bipartite double. The result identifies the complete recurrent geometry of a nonlinear local majority map by the 34 unlabeled graphs on five vertices, and explains how the doubling operation turns 124 shore symbols into a 124-symbol swap with 7,626 distinct oscillatory orbits. The three nontrivial predecessor weights reveal both thousands of isolated attractors and a unique very large basin; their values are not consequences of the general period-two property. This is a natural exact finite invariant and a reproducible benchmark for synchronous threshold-network dynamics, not an unmotivated parameter slice.

## Closest literature and residual limits

Benjamini et al. (2014) and Kaaser et al. (2016) establish general convergence and voting-time results, not graph-specific enumerations. Published Heawood and dodecahedral classifications use different graphs and different recurrent geometries. The identification of the Desargues graph as a bipartite Petersen double is standard, and no graph-theoretic novelty is asserted for it. Stronger or equivalent results could exist in unindexed primary literature. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
