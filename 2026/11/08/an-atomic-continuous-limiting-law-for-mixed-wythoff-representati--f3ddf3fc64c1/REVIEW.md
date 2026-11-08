# Scientific assessment: mixed Wythoff representation distribution

## Correctness — PASS

The domain is all positive integers with ordered lower/upper Wythoff summand roles. Beatty membership is derived from the exact floor-difference identity, not guessed from examples. The mixed convolution is an exact rotation-arc count, and the interval length is calculated in all three phase regimes. An independent derivation of a uniform \(O(\log n)\) discrepancy bound uses Fibonacci convergents; it does not assume that finite enumeration proves an infinite result. Circular equidistribution gives the exact continuous-plus-atomic pushforward law. Variation bounds and the discrepancy lemma give the quantitative Lipschitz estimate, and the moment formula follows by integration. Exact-integer computational checks support, but do not replace, these steps.

## Originality — PASS, with historical-priority uncertainty

The October 2026 Ashburn paper proves the sparse levels \(0,1,2\) of the *same* representation function, rather than its scaled global law. Shallit's 2020 rank-19 linear representation computes exact individual values, which is not an explicitly stated quantitative atomic-continuous limit law. The OEIS sequence gives formulas and data but no phase-profile theorem. Pongsriiam's 2022 full open-access paper focuses on the existence and cofinite coverage of Beatty sumsets, not representation-weight distributions. Searches for aliases, stronger implication, exact databases and related circular correlations did not identify equivalent published coverage, but a 2021 mixed-Wythoff sumset paper was not available for full-text assessment. The result's historical priority is not independently certified.

## Mathematical value — PASS

The count of representations \(r(n)\) is a named, actively studied Wythoff-sequence arithmetic invariant. Published work establishes exactly when the smallest representation counts occur. The present result instead identifies the complete *typical scale and law* of these multiplicities, including a positive atom at the maximal normalized density and a quantitative error against every one-Lipschitz statistic. The atom is a structural consequence of a plateau in the exact phase profile, rather than a generic density calculation. The theorem is a meaningful distributional counterpart to sparse-value classification and cannot be obtained just by reading off a few OEIS terms.

## Limits and independent validation

No optimality of the logarithmic pointwise error is asserted. A highly relevant 2021 source was not available in full, so additional priority checking would be appropriate. The symbolic proof supports the infinite statement; the packaged exact-integer computations test finite cases only. This assessment is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
