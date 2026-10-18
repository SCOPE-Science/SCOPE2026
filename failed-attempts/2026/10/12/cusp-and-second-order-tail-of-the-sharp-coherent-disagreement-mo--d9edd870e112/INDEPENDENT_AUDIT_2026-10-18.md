# Independent mathematical audit

## correctness

PASS

Use the already published exact piecewise Kravchenko formula: M=2^-alpha left and M=2 a_alpha d_alpha^alpha right with a=(alpha+3-sqrt(alpha²+6alpha+1))/4, d=(3alpha+1-sqrt(...))/(2alpha). Stationarity of log(2a)+alpha log[(1-2a)/(1-a)] removes da/dalpha in differentiation, giving right log derivative log d and left -log 2; alpha0>2 implies d0>1/2, so nonzero positive jump. Exact formal expansion in t=1/alpha yields log[M/(2t/e)]=-3t/2+13t²/6-21t³/4+O(t^4), hence relative -3/2 and 79/24. Independent SymPy rational-series calculation and numeric alpha0 root/slope checks agree. Relies entirely on published exact optimizer formula and does not reprove its global validity.

## originality

FAIL

Scientific rejection by prior implication: Kravchenko 2024 Theorem 1.3 already gives M(alpha) exactly for every alpha>0 including crossover; Lemma 3.9 supplies stationary branch. One elementary envelope derivative and binomial/Taylor expansion of those published expressions yield every claimed new number and the cusp without further analytic classification. Although coefficients/jump may not be printed verbatim, they are mechanically implied by an exact all-parameter stronger theorem; wording/search nonmatch is not novelty.

## value

FAIL

The crossover smoothness and refined high-alpha tail are mathematically natural descriptive features, but in this package they are routine differentiations and Taylor coefficients of a fully established closed formula, without an independent structural lemma or additional barrier. Under the shared value bar, such immediate textbook consequences do not constitute a separate substantive contribution. The correctness finding is preserved; scientific rejection is based on full-text prior implication, not limited access.

The dated certificate retains the supplied scientific assessment, sources and limitations.
