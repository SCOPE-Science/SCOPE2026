# Review of the prime-cylinder Markov escape-rate counterexample

**Correctness — PASS.** The chain is strictly positive and stationary with \(\pi=(14/27,5/18,11/54)\). Both words \(21\) and \(23\) are prime by direct prefix/suffix check. Exact rational cylinder measures and characteristic polynomials establish opposite strict orderings. The Perron--Frobenius limit and exact survival identity justify the escape-rate conclusion with no unproved limiting assumption. The two-symbol boundary follows directly from stationary edge flow balance. `check.py` reproduces the critical rational identities; finite checks are not substituted for the infinite-time proof.

**Originality — PASS, subject to identified source risk.** Agarwal--Cheriyath--Tikekar (arXiv:2401.05118, Section 7) explicitly conjecture the measure/escape ordering when both words are prime. Their counterexamples either have equal prime-cylinder measures or let one word be nonprime. Bonanno--Cristadoro--Lenci's monotonicity theorem covers Bernoulli/product measures, not this nonproduct chain. Earlier position-sensitive Markov-map examples concern other configurations. Specific exact-matrix, prime-word and synonym searches located no published equivalent in the inspected materials. The complete 2026 journal version and full 2019 article were not exhaustively available; unindexed examples remain a publication-priority risk, not a reason to claim exhaustive novelty.

**Value — PASS.** An explicit length-two, alphabet-minimal counterexample answers a natural conjecture about the statistical interpretation of open symbolic dynamics. It distinguishes the influence of transition correlations from cylinder size and word overlap, with a short exact certificate rather than a purely approximate calculation.

**Scope and limitations.** The example disproves universal strict monotonicity for prime words under stationary Markov measures; it does not classify arbitrary words or all transition matrices. Correctness has been subjected to the stated same-process checks only.

Self-review: passed. Independent audit: not yet performed.
