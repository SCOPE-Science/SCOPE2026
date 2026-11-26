# Independent mathematical audit

## correctness

PASS

The frozen formulas and asymptotic calculations are correct. The two-sided exponential already has norm one. With the unweighted coefficient sum the Walnut prefactor is η; after division by redundancy n it is η/n, the normalization used for the displayed bound formulas. The published optimizer localization and convexity ensure that bounded-strip stationary brackets contain the global optimizers: for A the log is strictly concave on (arccosh n,4 arccosh n) for large n, and B is strictly convex; the analogous K argument in the frozen proof uses strict log-convexity on the localization interval. Independently expand x csch x=1−x²/6+O(x⁴), x coth x=1+x²/3+O(x⁴) and the exponential factors with x=h/n, h=2 log n+s. The leading terms of the normalized deficits are h²/(6n²)+2(1+h)e^(−h) and h²/(3n²)+2(1+h)e^(−h). Taylor series bound derivative errors by O((log n)³/n⁴) on each bounded strip, so the stationary equations after division by h/n² give e^(−s)=1/6 or 1/3 up to O((log n)²/n²). In the ratio the leading terms add, giving the mathematically correct but previously covered condition-number result. In the repaired theorem, substituting h=2 log n+s and subtracting each optimum leaves J_A(s)−J_A(log 6) and J_B(s)−J_B(log 3) with uniform O(1/log n) error on compact strips. Thus evaluation at the previously established condition-number offset tending to log 4 is valid. Both regret coefficients are positive by strict convexity and unequal offsets; no statement for other windows or unbounded shifts follows. The independent bounded replay `python3 reproductions/frozen-1-5-reproduction.py gabor` used 55-digit arithmetic at n=127,4096,131071 and tested brackets, profiles and finite penalties, not normalization or the universal proof. The frozen script was inspected but not executed. The repaired proof explicitly treats the two individual objectives and cites the known K optimizer as an input.

## originality

PASS

This pass applies only to the substantive repaired theorem. The frozen three-objective originality claim fails in material part: the earlier identical-window result already explicitly states the log 4 location at the same error order, and its uniform expansion immediately implies the centered K loss. Corrected RESULT.md, SLOGAN.txt and the scientific notes in VERIFICATION.md remove those K results as contributions. The remaining log 6 and log 3 estimates, the two separate frame-bound loss profiles, and their sharp costs at the known condition-number optimum are distinct on the actual evidence checked.

## value

PASS

The retained result distinguishes two natural conflicting design objectives and measures, with exact positive constants, the loss in each if one instead chooses the known best-conditioned lattice. Neither the ratio optimum nor its loss alone tells which individual sharp frame bound deteriorates or by how much. Compact-uniform losses at the operative scale and the quantitative tradeoff remain useful after removing the duplicated condition-number result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
