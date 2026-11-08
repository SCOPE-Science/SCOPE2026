# Scientific review: Jacobsthal reciprocal-square tail floors

## Correctness — PASS
The stated formula follows from a direct absolutely convergent double series. Its first four coefficients and a uniform geometric tail estimate yield \(0<A_n-S_n^{-1}<1/9\) for every \(n\ge3\). The exact congruence \(3\cdot4^{n+3}-4(-2)^{n+3}\equiv3\cdot4^n-4(-2)^n\pmod{36}\) gives fractional parts at least \(2/9\), so the integer floors coincide. The two small cases are covered separately. The limit \(7/135\) is obtained from leading analytic coefficients. The standalone exact-rational checker validates the constants and gives finite tail-enclosure cross-checks through index 64. Computations do not substitute for the infinite proof.

## Originality — PASS within inspected evidence
The closest primary paper is Gaber (2022), on exactly these reciprocal-square tails, but its Theorem 2.2 prints a one-sided inequality restricted to odd indices rather than a correct all-index floor: the displayed inequality is incompatible with the direct instance \(n=3\). Koshy and Gao (2024, Class and Family) use different sparse weighted squared-polynomial sums and do not state this floor identity. Targeted published-finding corpus searches for aliases and error-correction formulations identified unrelated Fibonacci fifth-power, Fibonacci cubic, and balancing fourth-power tail results. Other prior mathematical claim statements were compared for implication overlap, and none concerned the present inverse Jacobsthal-square tail. Residual risk: unindexed or differently formulated literature might contain this exact identity; search absence alone is not a uniqueness proof.

## Mathematical value — PASS
Integer parts of inverse reciprocal tails are a natural invariant of classical recurrence sequences and are the direct object of the 2022 motivating paper. The complete formula handles every starting index and both parities and replaces a defective printed one-sided estimate with an exact infinite classification, together with a uniform rigorous enclosure and sharp residual limit. This is not an arbitrary finite slice or a new symbol for a known table.

## Closest literature and limitations
Ahmed Gaber, *On the reciprocal sum of Jacobsthal numbers*, arXiv:2207.12857v1 (19 July 2022), particularly Theorem 2.2. Thomas Koshy and Zhenguang Gao, Fibonacci Quarterly 62 (2024), papers on a *Class* (pp. 40–44) and a *Family* (pp. 130–135) of Jacobsthal polynomial square sums. The result does not cover alternating sums, higher inverse powers, or generalized recurrence parameters. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
