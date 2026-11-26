# Independent mathematical audit

## correctness

PASS

Normalized monomial projection gives the +2 shift A_n=√[(n+1)/(n+3)] and the −1 shift B_n=√[n(n+1)]/(n+2), with absent entries zero. Commuting gives diagonal A_n²−A_(n−2)²+t²(B_n²−B_(n+1)²) and third off-diagonal t[A_n B_(n+3)−A_(n+1)B_(n+1)], where t=|b/a|. Rotation removes the relative phase. These agree with D_n,E_n,O_n. At t=2/3 the first three row lower margins are 59/405, 61/162 and 191/1050; for n≥3 the all-index rational lower margin is positive by shifting the numerator polynomial by n−3. The quadratic form is nonnegative on finite vectors by the row bound, and then by boundedness and density; decreasing t improves the same bound. For t>2/3, first choose a finite alternating chain length L so 4−3t²−4t(1−1/L)<0, then translate the chain to sufficiently high indices to produce a negative form. If a=0 and b≠0 the backward-shift diagonal is negative; the zero operator is normal. Boundary differentiation gives minimum Jacobian 4|a|²−4|a||b|−3|b|², and summability on the three bands proves trace class. The diagonal sums telescope to 2 and −1 for the two individual shifts, so the trace is 2|a|²−|b|². Replay: frozen RESULT.md proof §§1–4. The finite checker was inspected, not executed.

## originality

FAIL

The exact cutoff is mechanically recoverable from two earlier results on this same opposite-angular family: the Fleeman–Liaw explicit sufficient row criterion at the endpoint, and the Revilla–Simanek exact form with their high-index block test for the other direction. Neither source is claimed to print the coefficient equivalence in these words. The actual specializations and deductions are given below.

## value

FAIL

The concrete example is natural and can illustrate why checking only diagonal moments misses positivity. As an independent exact finding, however, its coefficient boundary is a routine specialization of a published sufficient comparison and a published high-index test in the same symbol family. Neither its algebraic boundary-Jacobian reformulation nor the telescoping trace yields an independently valuable new remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
