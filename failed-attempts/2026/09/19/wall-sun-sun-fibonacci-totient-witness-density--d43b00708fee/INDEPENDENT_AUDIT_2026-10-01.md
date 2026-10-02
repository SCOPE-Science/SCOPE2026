# Independent mathematical audit — 2026-10-01

## Final claim assessed

For odd q != 5 and every a>=1, along a fixed Pisano-period residue class the density of indices with q to the power a dividing F_m is 0 when z(q) does not divide the class and otherwise q to the power {-max(a-e_q,0)}; this yields the stated Wall--Sun--Sun square branch and external-prime-witness density consequences.

## Correctness — PASS

The argument follows from the standard Fibonacci valuation lift v_q(F_m)=e_q+v_q(m/z(q)) when z(q)|m. Since z(q)|P=pi(q) and q does not divide P for q!=5, P/z(q) is a unit modulo every q to the power s; hence one residue class of the progression parameter modulo q to the power s gives density q to the power -s. A fresh q=3 check reproduced densities 1, 1/3, and approximately 1/9 for a=1,2,3. The totient witness deduction is then immediate from the prime-factor formula for phi.

## Originality — FAIL

The scientifically decisive square-power branch and positive-density external-witness correction were already published in SCOPE on 2026-09-18. The new all-a formula is the direct iteration of the classical p-adic Fibonacci lifting law together with the invertible arithmetic-progression slope. Under implication-based originality this is a mechanically implied extension, not a separate original theorem.

## Value — FAIL

The all-prime-power formula is tidy, but once the prior square-density theorem and classical valuation lift are known, the extension is a routine one-congruence count. It does not identify a further motivated gap beyond the already published correction, so it fails the value bar for a new record.

## Source inspections and risks

- **Wall--Sun--Sun exceptional branch in Fibonacci-totient residue classes** (SCOPE 2026/09/18/wall-sun-sun-branch-in-fibonacci-totient-residue-classes--e366d007c171): Complete RESULT.md from audited Git snapshot. Assessment: COVERING_CORE.
- **Sophie Germain Primes and the Totient of Fibonacci Numbers** (arXiv:2604.17847v3): Primary abstract plus accessible full-text excerpt containing Lemma 4.3 and its use of the nonexistence assumption. Assessment: BACKGROUND_AND_TARGET.

Residual risks: No Wall--Sun--Sun prime existence is assumed. The rejection does not depend on unindexed literature because earlier SCOPE coverage plus the classical lift already implies the claimed extension.
