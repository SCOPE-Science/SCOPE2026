# Self-review

## Correctness: PASS

The claim uses the standard Wolfram truth-table convention and includes cyclic lengths one and two. The four-state and sixteen-state closed-walk correspondences are proved for **every** spatial period. A marked edge in a directed cycle of the second-iterate constraint graph is equivalent to a primitive temporal two-cycle: it imposes the correct two-step equation at every position and witnesses a genuinely changing first step at one position. The strongly connected component criterion therefore certifies all-length **absence** for 107 rules. Exact exhaustive evaluation of each of the 256 rule tables finds a length-at-most-six witness for the other 149 rules, with twelve sharp length-six cases. Two separately constructed verification programs passed; one checks the graph criterion, the other computes exact characteristic polynomials and direct traces, and validates the 256-row table and each listed witness. The finite checks support a complete finite rule classification, not an extrapolation to arbitrarily large rings.

## Originality: PASS, qualified

The closest published exact temporal-two zeta result treats only Rule 18, and the corresponding existing single-rule Rule 73 result likewise does not give a full 256-rule or sharp finite-witness theorem. Published eight-site tests for equality of cyclic **image languages** concern a different invariant: output reachability, not fixed points of a second iterate. Banks–Djirar's 1992 graph method and the 2025 trajectory-counting transfer-matrix method anticipate the *technique*, which is explicitly credited. Epperlein's 2015/2017 classification includes temporal periodic-point invariants for the 256 elementary rules and poses the strongest historical-coverage risk, but the inspected chapter and conference abstract do not present the six-site first-witness distribution or exact 40-class rational-zeta census. Targeted searches found no exact matching statement. Residual risk: unindexed tables or uninspected material, notably the 2015 conference full paper, may contain an equivalent classification; no assertion of exclusive historical priority is made.

## Mathematical value: PASS

This is not a short-ring sample or a routine isolated-rule variant. It gives a **uniform sharp decision bound** for all elementary rules, distinguishing finitely checkable existence from infinite-ring nonexistence using a directed-cycle invariant. The exact 107-rule negative family is certified against *all* finite ring lengths, and twelve rules show the cutoff cannot be reduced. Beyond existence, 40 distinct exact second-iterate denominator polynomials and 51 joint first/second-iterate classes give every labelled temporal-one and temporal-two configuration count at every ring length. These are natural dynamical invariants of the full elementary-rule universe, not arbitrarily selected parameter values.

## Limits and closest literature

The proof relies on a complete 256-case exact finite graph computation, the full reproducible classification table, and independently replayable code. It does not apply automatically to bi-infinite nonperiodic states, temporal periods above two, or larger-radius automata. Classical transfer-matrix methods are prior art. Relevant primary comparisons are Wolfram (1983), Banks and Djirar (1992), Epperlein (Automata 2015; fuller 2017 thesis chapter), and Koller and Hudcová (2025). A published Rule 18 temporal-two zeta result and a separate cyclic-image-language finite test are distinct special or neighboring results. Bibliographic and full-text priority risks remain; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
