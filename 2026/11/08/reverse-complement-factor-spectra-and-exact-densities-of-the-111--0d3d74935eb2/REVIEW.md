# Review

## Correctness

**PASS.** The digit recursion follows by considering the appended binary digit; the two-block formula partitions length-\(d\) pattern occurrences into parent, suffix and boundary-crossing cases. State closure represents every nonnegative parent. The program enumerates all \(1792\) and \(12288\) relevant state/residue/even-length combinations, verifies the exact two-family factor lists and the absence of the first excluded length, and obtains densities by a rational stationary distribution of an irreducible aperiodic finite transition chain. Odd lengths are impossible by the central-letter obstruction. Direct finite-prefix diagnostics are auxiliary and are not offered as an infinite proof.

## Originality

**PASS, qualified.** The 2019 pattern-sequence paper treats maximum-order complexity of square subsequences. The 2020 palindrome paper treats ordinary palindromic factorization of the classical Rudin–Shapiro word, not reverse-complement factors of the two higher-pattern words. The 1993 generalized Rudin–Shapiro paper treats ordinary factor complexity, which does not supply an involution-fixed factor set or individual densities. Targeted exact, alias, reduction and broader-coverage searches found no claim implying the present two-pattern classification. The strongest residual risk is an unindexed earlier computation of antipalindromic factors for the same pattern sequences.

## Mathematical value

**PASS.** The two smallest nonclassical constant-one pattern words form a natural testbed for how local binary-pattern parity constrains reverse-complement symmetry. The sharp cutoff doubles in scale from length \(14\) to length \(30\), while the complete language uses only two explicit families. The per-word rational densities and precise maximal-factor starting states provide a factor-level refinement of general automatic-word decidability and ordinary factor-complexity results; this is a complete infinite-word statement rather than a finite prefix census.

## Closest literature and limits

Sun–Winterhof (2019), https://arxiv.org/abs/1910.13763; Frid–Laborde–Peltomäki (2020), https://arxiv.org/abs/2009.02934; Allouche–Shallit (1993), https://doi.org/10.5802/jtnb.94. All comparisons concern the actual statements, not title similarities. The result does not cover \(d\ge5\), and a potentially unindexed equivalent cannot be categorically excluded.

Self-review: passed. Independent audit: not yet performed.
