# Independent mathematical audit — SCOPE-20260921-301b67b881e5
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **failed**.

## Final claim
For a fixed admissible support of distinct odd primes, exponent vectors of weak Carmichael numbers form the positive part of a finite-index lattice, primitive weak Carmichael numbers correspond to primitive lattice vectors, and their logarithmic-height density tends to \(1/\zeta(s)\), with the stated lattice-point asymptotics.

## Correctness
Status: **PASS**.

The mathematics reconstructs. Meštrović’s criterion \(p-1\mid n-1\) for every prime divisor converts, for fixed support, into finitely many multiplicative-order congruences on the exponent vector; these are exactly the kernel of the stated homomorphism to a finite product of unit groups. The primitive-power definition is equivalent to divisibility of the exponent vector inside that lattice. Standard lattice-point counting in a weighted simplex gives the leading constant, and Möbius inversion gives the \(1/\zeta(s)\) primitive proportion with the stated error orders. The bounded source computations are consistent with, but not needed for, the proof.

## Originality
Status: **FAIL**.

Originality fails by implication. Meštrović’s full 2013 primary paper already gives the exact global criterion for weak Carmichael numbers and, in Proposition 2.36, even specializes the two-prime support to explicit divisibility conditions on the exponents; it also defines primitive weak Carmichael numbers by exclusion of proper powers. For an arbitrary fixed admissible support, rewriting the same global congruences as the kernel of a homomorphism to a finite group is immediate algebra. Once that finite-index lattice is exposed, the counting asymptotic and primitive density are the standard lattice-simplex and Möbius-inversion consequences. Thus the claimed result is mechanically implied by a broader prior characterization plus textbook lattice facts even though the exact \(1/\zeta(s)\) wording was not located.

### Equivalent formulations
- Search/source: Published-record semantic query: weak Carmichael primitive fixed support exponent lattice density zeta primitive vectors.
- Search/source: R. Meštrović, Generalizations of Carmichael numbers I, arXiv:1305.1867 (2013).
- Evidence: Meštrović Theorem 2.4 gives the exact global weak-Carmichael criterion; Proposition 2.36 explicitly gives exponent-divisibility conditions on two-prime supports.
- Reasoning: Originality fails by implication. Meštrović’s full 2013 primary paper already gives the exact global criterion for weak Carmichael numbers and, in Proposition 2.36, even specializes the two-prime support to explicit divisibility conditions on the exponents; it also defines primitive weak Carmichael numbers by exclusion of proper powers. For an arbitrary fixed admissible support, rewriting the same global congruences as the kernel of a homomorphism to a finite group is immediate algebra. Once that finite-index lattice is exposed, the counting asymptotic and primitive density are the standard lattice-simplex and Möbius-inversion consequences. Thus the claimed result is mechanically implied by a broader prior characterization plus textbook lattice facts even though the exact \(1/\zeta(s)\) wording was not located.

### Broader coverage
- Search/source: R. Meštrović, Generalizations of Carmichael numbers I, arXiv:1305.1867 (2013).
- Search/source: J. M. Borwein and E. Wong, criterion for weak/pseudo-Carmichael numbers cited and reproved by Meštrović.
- Search/source: Classical geometry-of-numbers lattice-point asymptotics and Möbius inversion for primitive lattice vectors.
- Evidence: The prior global criterion plus the primitive definition already dominates the fixed-support membership problem; standard lattice counting supplies the asymptotic once rewritten.
- Reasoning: Originality fails by implication. Meštrović’s full 2013 primary paper already gives the exact global criterion for weak Carmichael numbers and, in Proposition 2.36, even specializes the two-prime support to explicit divisibility conditions on the exponents; it also defines primitive weak Carmichael numbers by exclusion of proper powers. For an arbitrary fixed admissible support, rewriting the same global congruences as the kernel of a homomorphism to a finite group is immediate algebra. Once that finite-index lattice is exposed, the counting asymptotic and primitive density are the standard lattice-simplex and Möbius-inversion consequences. Thus the claimed result is mechanically implied by a broader prior characterization plus textbook lattice facts even though the exact \(1/\zeta(s)\) wording was not located.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No decisive exact database/table coverage was found; where the claim is theorem-level, the primary literature comparison is the controlling check.
- Reasoning: Originality fails by implication. Meštrović’s full 2013 primary paper already gives the exact global criterion for weak Carmichael numbers and, in Proposition 2.36, even specializes the two-prime support to explicit divisibility conditions on the exponents; it also defines primitive weak Carmichael numbers by exclusion of proper powers. For an arbitrary fixed admissible support, rewriting the same global congruences as the kernel of a homomorphism to a finite group is immediate algebra. Once that finite-index lattice is exposed, the counting asymptotic and primitive density are the standard lattice-simplex and Möbius-inversion consequences. Thus the claimed result is mechanically implied by a broader prior characterization plus textbook lattice facts even though the exact \(1/\zeta(s)\) wording was not located.

### Claim versus prior implication
- Search/source: R. Meštrović, Generalizations of Carmichael numbers I, arXiv:1305.1867 (2013).
- Search/source: J. M. Borwein and E. Wong, criterion for weak/pseudo-Carmichael numbers cited and reproved by Meštrović.
- Evidence: The prior global criterion plus the primitive definition already dominates the fixed-support membership problem; standard lattice counting supplies the asymptotic once rewritten.
- Reasoning: The audited theorem is a direct algebraic/lattice corollary of the broader prior criterion and textbook primitive-lattice counting, so implication-based originality fails.

### Primary-source inspections
- **Generalizations of Carmichael numbers I** (arXiv:1305.1867): trigger — primary source of the exact weak-Carmichael criterion and primitive definition; material read — full arXiv PDF, including Theorem 2.4/2.4 prime-divisor criterion, Proposition 2.6, Definition 2.25, and Proposition 2.36 for two-prime supports; method — lawful arXiv full-text inspection with page-level verification; assessment — BROADER_COVERAGE_PLUS_DIRECT_COROLLARY; evidence — Theorem 2.4 gives \(p_i-1\mid n-1\) for every support prime; Proposition 2.36 turns this into exponent divisibility in the two-prime case, and Definition 2.25 supplies the proper-power notion used for primitiveness.

## Scientific value
Status: **FAIL**.

The support-lattice viewpoint is tidy and correct, but after the prior exact weak-Carmichael criterion is in hand, every substantive step is a routine change of coordinates followed by standard lattice-point and primitive-vector counting. Under the required value bar this does not supply a new structural obstruction, motivated boundary, or non-mechanically implied invariant; correctness and a clean asymptotic presentation alone are insufficient.

## Checked sources
- R. Meštrović, Generalizations of Carmichael numbers I, arXiv:1305.1867 (2013).
- J. M. Borwein and E. Wong, criterion for weak/pseudo-Carmichael numbers cited and reproved by Meštrović.
- Classical geometry-of-numbers lattice-point asymptotics and Möbius inversion for primitive lattice vectors.
- Published-record semantic query: weak Carmichael primitive fixed support exponent lattice density zeta primitive vectors.

## Limitations and residual risks
- The failure is scientific originality/value, not access or transport.
- The source computations remain valid evidence for the formulas but do not alter the implication analysis.

This audit reports the mathematical assessment only. It is not a formal proof-assistant certificate or a guarantee of priority.
