# Independent mathematical audit

## correctness

PASS

Under the stated independent conditional-Poisson and fixed-spurious-positive model the all-negative probabilities are α^n under absence and α^n·product(q(vi)) under presence, where α=1−f and q(v)=1−p+p exp(−λ(v−c)). Their difference is Youden discrimination. g=−log q has g′>0 and g″<0; strict Jensen yields exactly the equal split, including the trivial n=1 case. For E=n g(B/n), direct differentiation gives E″=(B/n)^2 g″(B/n)/n<0, and log(1−exp(−E)) is increasing and strictly concave in E>0. Adding n log α preserves strict log-concavity, which orders secant slopes and makes strict neighbor wins globally decisive (one-sided at an endpoint). This does not assert unique maximizers at every intermediate budget; adjacent finite-budget ties can occur. At fixed count E increases strictly with B. I independently certified the four comparisons with exact rational alternating partial sums of exp(−x), rather than the frozen checker’s reciprocal positive sums. The four certified lower margins exceed 0.0003434316, 0.0011327059, 0.0044248467 and 0.0002921463 respectively; the scores therefore certify the asserted 5-to-4 reversal. For large B, Cn=α^n(1−β^n), β=1−p, and the sign of C(n+1)−Cn is the sign of (1−αβ)β^n−f. Its one crossing gives the ceiling formula with equality only at an integer threshold. The geometric upper bound α^n and the positive limit of J1 restrict all large-budget maximizers to a fixed finite set. At a tie k,k+1 the positive deficits have leading terms α^n n β^(n−1) p e^(λc) e^(−λB/n), so the smaller count approaches faster and wins eventually. The witness threshold is strictly between 3 and 4 by rational signs. As a check on the credited f=0 contrast, the continuous optimum maximizes g(v)/v, with derivative sign v g′−g decreasing strictly from positive at c to negative at infinity; its fixed v gives a count proportional to B, and the integer optimum differs by at most one. Replay: /workspace/reviews/replay_statistics.py and replay_statistics.txt; frozen checker inspected, not executed.

## originality

PASS

The pass is for the budget reversal with fixed independent assay false alarms under the specified patch model and OR Youden objective, together with its exact ceiling and tie resolution. Equal allocation and the zero-false-alarm staircase are not credited as new. The closest formal and empirical sources use a different objective, an effort-dependent false-alarm term, or no false alarms at all. None of the verified alternatives implies the positive-f comparison.

## value

PASS

More water improves discrimination at each fixed count, but can strictly reduce the unique globally preferred count because a new assay incurs an additional false-alarm risk. The exact example establishes that this is a real optimization phenomenon rather than numerical error, and the limiting count and tie-break explain the saturation regime. The result is a useful idealized design benchmark with independent grabs and symmetric sensitivity/specificity weighting, not a field prescription or a claim about correlated occupancy or biological uncertainty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
