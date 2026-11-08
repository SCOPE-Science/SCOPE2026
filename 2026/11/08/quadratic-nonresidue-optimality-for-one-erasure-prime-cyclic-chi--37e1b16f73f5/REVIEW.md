# Scientific review

## Correctness — PASS

The proof independently reconstructs the masked autocorrelation as the two deleted terms from the zero cyclic correlation of a prime-length chirp. The algebraic identity gives the full complex correlation, including all factors of two and the erasure-location phase. Coset analysis yields exact maxima; the standard quadratic Gauss-sum formula gives exact integrated energies. Quantifiers cover all odd primes, every nonzero root, every erased position, and all nonzero shifts. The packaged standalone checker directly recomputes the complex correlations for all roots and two erased sites for each odd prime through 101. This check is finite corroboration rather than proof.

## Originality — PASS, with documented residual risk

Full text inspected: Andrews, arXiv:2211.05702, sections on chirp definitions, cyclic autocorrelation, and modified sequences; Gregoratti–Arteaga–Broquetas, arXiv:2311.01035, sections 2–4 and Appendix B. These establish full-period ideal autocorrelation and Gauss sums but do not formulate the one-hole optimization. Research-record searches using Zadoff–Chu, CAZAC, single erasure, missing chip, root, quadratic nonresidue, and sidelobe aliases returned related chirp tomography and phase-rigidity findings but not this claim. Related accessible mathematical statements were checked for the same implication. Lee–Yang (2014) is a plausible specialized source on partial-period correlations, but only abstract-level material could be inspected: an equivalent hidden implication there remains a specific priority risk, not a verified noncoverage claim.

## Mathematical value — PASS

Robustness of ideal cyclic correlation under one missing symbol is a canonical damage model for phase-coded reference sequences. Exact worst sidelobe and total sidelobe energies are complementary engineering and mathematical invariants; their common optimizer, the \(p\bmod4\) dichotomy, and the explicit quadratic-nonresidue criterion give a complete, unbounded-prime root-selection classification. The result is not a general CAZAC optimality theorem or a model of multi-symbol losses.

Self-review: passed. Independent audit: not yet performed.
