# Scientific review: alternating public-goods improvement on graphs

## Correctness — PASS

The exact best-response utility is realized by a strictly increasing common benefit sequence with alternating positive and negative net marginal incentives. Equilibria solve the binary linear system \((I+A_G)s=\boldsymbol 1\); symmetry and a zero adjacency diagonal make this system consistent for all undirected graphs. On each clique, all agents are dissatisfied exactly when the total active count is even; a flip permanently settles that clique. The integer potential counting odd-parity components therefore rises by one on every move. On an induced \(P_3\), the four stated flips are strict even with all other players fixed at zero. The lower bounds of four moves and three vertices are proved, not inferred from samples. The standalone verifier enumerated all \(33{,}867\) graphs through six vertices and passed its exact assertions.

## Originality — PASS, qualified

Papadimitriou–Peng (2021) give the alternating equilibrium linear system; that known special case is expressly excluded from the claimed new contribution. Klimm–Stahlberg (2023) prove best-response convergence for decreasing patterns, which do not contain the infinite alternating pattern. Gilboa–Nisan (2022) analyze equilibrium computational complexity, not an all-schedules FIP graph dichotomy. Related records for synchronous parity automata use simultaneous updates, so their orbit statements do not imply this unilateral-improvement theorem. The exact new comparison is the finite-improvement iff cluster-graph condition, plus its sharp four-step witness and exact clique path length. The inspected sources do not contain a covering statement; indexing gaps or a differently named prior characterization remain genuine priority risks.

## Value — PASS

The result gives a complete forbidden-induced-subgraph characterization of universal convergence in a nonmonotone, homogeneous local public-goods game; it distinguishes equilibrium existence from the stronger robustness demanded by arbitrary sequential strategic adjustment. The smallest obstruction and exact convergence clock on every compliant graph make the mathematical boundary operational rather than an isolated small instance. The parity response is both studied in the cited literature and realizable through a strictly increasing common benefit function, rather than an artificial rule with no public-goods interpretation.

## Scientific scope and residual risks

The four-step cycle requires only two agents to move while a third remains active; it does not imply failure of all fair or random schedules. The result does not carry over automatically to heterogeneous response patterns, weighted or directed graphs, or synchronous dynamics. Priority was compared against accessible relevant texts and mathematical records, not all possible unindexed formulations. Finite exhaustive verification is not an infinite-graph proof. Independent validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
