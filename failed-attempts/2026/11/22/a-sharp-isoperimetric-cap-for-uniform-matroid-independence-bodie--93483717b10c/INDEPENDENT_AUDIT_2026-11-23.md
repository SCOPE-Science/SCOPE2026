# Independent mathematical audit

## correctness

PASS

Coarea gives rank-facet area A=√n f_n; the lower and upper coordinate areas sum to L=nF_{n−1}(t) and U=nF_{n−1}(t−1). Independently, the divergence theorem with the fields x and the constant all-ones vector gives nV=U+tA/√n and U−L+√n A=0. This verifies the two facet identities even at knots, without needing to differentiate a discontinuous one-dimensional density. With H=F_n^(1/n), the quotient is 2nH+n(n−2t+√n)H'; its derivative between knots is n(n−2t+√n)H''. Brunn–Minkowski makes H concave, linear for t≤1 and strictly concave between distinct cuts above 1 since the full coordinate projections force any homothety to be identity. A normalized simplex from t≤1 cannot be homothetic to a cut above 1, since the latter contains points beyond the unit-simplex cap while having the same full normalized coordinate projections. In integrating the sign of the derivative, strict concavity rules out an interval of zero derivative, not necessarily isolated zeroes. Continuity joins the knots. The two integer candidates really are floor and ceiling, without a tie/nearest-integer claim. The CLT gives F_n(t*) and both nearby integer CDFs tending to Phi(√3); the O(1) density coefficient at adjacent ranks contributes O(n^−1/2) by the uniform-sum local CLT. At t=n the rank-facet area vanishes and one gets the cube; as t decreases within the simplex range the scale-invariant quotient stays constant. Replay: RESULT.md lines 42–86; VERIFICATION.md and verify.py were inspected, not executed. The independent fixed-normal proof below verifies the optimum and equality, but not the global derivative profile on its own.

## originality

FAIL

The frozen record's central claim of a new sharp continuous Euclidean surface inequality and equality case is covered by a direct specialization of the known Wulff inequality. The match with the John contact value alone would not show coverage. The full derivative profile, integer localization and asymptotics are not asserted to be separately published in the sources inspected.

## value

FAIL

Minimizing ordinary whole-boundary area at fixed volume is natural, and the integer application is correctly stated. But the advertised exact continuous optimum is the mechanical fixed-normal specialization of an established principle. The supplementary profile follows from the tangent evaluation of a concave volume-root function, and the two-rank localization and leading constant are routine consequences of that profile and the usual uniform-sum CLT. As submitted, the remainder does not decide which of the two ranks minimizes, analyze ties, or establish a distinct nonroutine geometric question sufficient to support a separate repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
