# Review

## Correctness — PASS

The statement concerns a synchronous, indexed Rule 45 map on every positive odd ring. The elementary-rule truth table agrees with \(1\oplus a\oplus c\oplus bc\). The identity \(x_i=1\oplus y_{i+1}\oplus y_{i+2}x_{i+2}\) is verified algebraically, and the only nonstandard step — annihilation of the closing term — follows by a finite odd-cycle propagation contradiction. The resulting formula determines all input coordinates for each attainable output, proving injectivity and, on a finite set, bijectivity. All claimed ANF monomials are distinct and the exact influences are counted by independent output coordinates. The extracted self-contained checker independently exhausts odd lengths through 15 and checks the full ANF support through 13. No infinite conclusion relies on finite enumeration.

## Originality — PASS (historical priority qualified)

Hudcová's Section 3.3, Theorem 28, is a direct and important predecessor: odd-ring reversibility and output preimage counts are known and are explicitly excluded from the novelty claim. Its section on Rule 45 (including the Cayley graph and preimage-count theorem) does not state an all-length inverse coordinate polynomial or single-bit inverse influences. Gadnayak–Bhattacharjee give small-size inverse-rule information, including the three-site inverse Rule 101; the present formula agrees at that size but covers every odd size and gives full sensitivity probabilities. The 1984 Martin–Odlyzko–Wolfram paper studies additive rules and nonlinear Rule 18, not this nonlinear Rule 45 inverse. Searches under rule-number aliases, inverse Boolean derivatives and inverse radii did not identify a covering theorem. Historical priority is qualified because unindexed or inaccessible equivalent formulations may exist; lack of a search result is not a proof of uniqueness.

## Value — PASS

An explicit sparse, degree-growing inverse for a nontrivial finite-ring reversible automaton and the exact anisotropic differential/avalanche profile quantify distinct aspects of inverse information propagation. The contrast is structural: optimal radius grows with the whole ring even though the inverse has a linear-size nested implementation and influence decays by powers of two. These quantities are natural diagnostics for inversion and Boolean diffusion, and they are not implied numerically by the already-known bijectivity theorem alone. No security property is inferred.

## Limits and closest literature

The conclusion does not cover even rings, multi-step dynamics, cryptographic security, or external mathematical certification. Closest prior source: B. Hudcová, *Complexity in Cellular Automata*, Section 3.3, Theorem 28. Additional comparisons: K. K. Gadnayak and K. Bhattacharjee, *Finding the Inverse Cellular Automata of a given 1-D Reversible CA* (2022); O. Martin, A. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata* (1984); S. Wolfram, *Statistical Mechanics of Cellular Automata* (1983).

Self-review: passed. Independent audit: not yet performed.
