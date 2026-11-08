# Scientific review: cyclic-alphabet phase-shift deletion profiles

## Correctness

**PASS, subject to independent validation not performed.** The first-occurrence and positive-increment rule is exact for any cyclic permutation word, including a repeated symbol (increment equal to the alphabet size). Mapping an initial symbol and a sequence of positive cyclic increments to a distinct received word is a bijection, so the generating-polynomial count is for distinct words, not deletion masks. Explicit comparison of both initial phase positions gives the two threshold intervals with multiplicity, including overlapping threshold values. Coefficient extraction is a formal geometric-series identity. Threshold cumulative distributions give the weak phase ordering; the minimal threshold and unit increments give exact LCS length and multiplicity. All arguments cover the finite boundaries and zero-length received word. Direct enumeration and the independent polynomial calculation agree for 280 parameter profiles and 1,820 retained-length entries, including truncations that are not complete cycles. Finite comparisons corroborate but do not replace the proof.

## Originality

**PASS against the inspected literature; historical priority remains provisional.** Sun–Ge (2026) prove general upper bounds on intersections of deletion balls under lower-order and run-count constraints, not exact profiles of all cyclic permutation shifts. Gaevoy–Zolotov–Tiskin (2025) give algorithms for a **single** LCS score of doubly periodic strings, not all distinct common-subsequence counts, the multiplicity of longest words, or an all-radii ordering by phase. Wang–Li–Fu (2026) determine maxima over restricted pairs of q-ary words; a worst-case envelope does not imply an individual-pair spectrum. The latest paper's full text remained inaccessible, so a nested special-case derivation could be missed. Searches of semantic research records, relevant original papers, and accessible prior claim titles found no dominating formula. Search absence is not proof of priority.

## Value

**PASS.** Deletion-ball intersections specify exactly how many different noisy reads can be shared by two possible codewords. Cyclic words using each alphabet symbol once per period are canonical high-transition test families for nonbinary synchronization and periodic string comparison. The theorem gives a uniform closed expression for every alphabet, truncation length, phase, and deletion count, plus an ordered phase hierarchy and exact longest-word multiplicities. Neither a generic LCS algorithm nor an extremal intersection upper bound supplies that full structural classification. The result is useful as an exact benchmark for restricted reconstruction instances, not merely a small-parameter count.

## Closest literature and limits

- Y. Sun and G. Ge (2026), arXiv:2606.25822v1: 15-page primary PDF inspected for Theorems 1.1–1.12, definitions, proofs and conclusion; no individual cyclic-shift profiles or phase hierarchy located.
- N. Gaevoy, B. Zolotov and A. Tiskin (2025), DOI 10.4230/LIPIcs.CPM.2025.13: accessible complete HTML inspected, including problem formulation, main algorithmic results and appendices; only LCS scores are computed.
- X. Wang, H. Li and F.-W. Fu (2026), arXiv:2609.16837: verified abstract examined, full preprint unavailable through attempted lawful access paths. This is a residual comparison risk; its stated scope is extremal values rather than individual-pair spectra.

The result does not cover arbitrary periodic blocks, insertion ambiguity, or optimal reconstruction-code design. No independent human or external mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
