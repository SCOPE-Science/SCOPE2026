# Scientific review

## Correctness (C) — PASS

For each column, the objective involves only four endpoint entries. Identity (1) in `RESULT.md` decomposes a weighted endpoint contribution into a phase-alignment loss and three explicit real squares; its polynomial part is checked using exact rational evaluations. Summing the additional unused-mass term and using the four full row norms gives the universal maximum \(5/4\). Equality forces exactly four active columns, all with endpoint entry moduli \(1/2\); the phase relation and pairwise orthogonality yield the stated complete class. A four-by-four Walsh block reaches the bound for every \(N\ge4\). The statistical corollary is derived from the independent proper-symbol fourth-moment identity (arXiv:2610.02843, Lemma 1 and Appendix A). Finite tests are checks, not proofs for all dimensions.

## Originality (O) — PASS, relative to inspected sources

The closest full primary source is Y. Xiong et al., *On the Optimality of OFDM for Aperiodic Ranging*, arXiv:2610.02843 (2026-10-02), including the exact single-lag results, prefix EISL theorem, and Appendices A/B/G/H/I. Its known single-lag terminal values add to \(3/2\), but the sharp joint maximum is \(5/4\). Its prefix claims cannot be restricted to a non-prefix pair while preserving optima. The previously studied full EISL is not the same objective. Targeted searches for endpoint-pair aperiodic energies, Fourier/Walsh equivalents, relevant published-finding corpus statements and relevant available published claims did not reveal a matching theorem. This is evidence for noncoverage only within the inspected material, not a proof of universal novelty. The original 2025 unitary-OFDM article was compared via its precise quoted results in the 2026 source, rather than independently from full text.

## Mathematical value (V) — PASS

The result answers an explicit and natural non-prefix tail-delay optimization question, supplies an exact dimension-independent constant and all equality cases, and quantifies a nonzero loss caused by incompatible individually optimal lags. It also gives the sharp improvement over complete OFDM for every \(N>4\) in the proper, sub-Gaussian random-symbol regime. The sum-of-squares defect yields a quantitative certificate for departures from optimal structure.

## Limitations and closest literature

No optimality is asserted for weighted tail lags or arbitrary non-prefix sets, nor for symbols with fourth moment at least two. The possibility of equivalent statements in unindexed literature remains; no independent mathematical validation has been performed. References and comparisons are in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
