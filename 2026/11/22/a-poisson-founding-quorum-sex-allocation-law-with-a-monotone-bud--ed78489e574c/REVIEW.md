# Independent mathematical audit

## correctness

PASS

Poisson thinning, or the explicitly assumed independent counts, gives a product of two tails. For 0<u<n and y=n−u, Q'_r(y)=e^(−y)y^(r−1)/(r−1)!, and Q_r/Q'_r=B_r−1. Comparing the two positive denominators in the log derivative gives the sign of log B_r(n−u)−u. B_r is the MGF of Beta(1,r−1) (or of the constant one at r=1); strict positivity of its tilted mean gives strictly increasing y+φ_r(y), and the derivative changes sign once from positive to negative. Endpoint success is zero. The strictly positive tilted variance for r≥2 makes φ_r(y)/y strictly increasing from 1/r toward 1, with derivative bound φ'_r<1; the limiting slope also follows directly from φ_r(y)=y−(r−1)log y+log((r−1)!)+o(1). This last argument avoids the imprecise tilting sentence in Step 3. At fixed budget the beta variables decrease in strict stochastic order as r increases, which raises y_* and lowers u_*; r=1 gives parity. The tilted logarithm has quadratic coefficient Var(V_r)/2=(r−1)/(2r²(r+1)); inversion gives r(r−1)/(2(r+1)^4) for the n-term of the share. The large-budget equation has y_*=n/2+O_r(log n), so log y_* can be replaced by log(n/2) with o(1) error. Both one-sex failure terms are then equivalent to e^(−n/2)(n/2)^((r−1)/2)/√((r−1)!), and their product is negligible. The small-budget leading probability follows from u~n/(r+1) and Q_r(y)~y^r/r!. These are fixed-r and initial-quorum statements, not dynamic persistence.

## originality

PASS

Neither Poisson splitting, the Gamma/Poisson tail identity, the beta MGF, nor the general log-concave resource-allocation first-order condition is original here. The contribution assessed is the all-budget share law for unequal thresholds, the strict order in quorum and the sharp small/large-budget and optimized-failure expansions. Related exact founder and dynamic extinction results solve different optimization or probability problems. No covering statement is established by examined material; the broader reliability comparison is explicitly qualified by access limits.

## value

PASS

For an initial two-sex feasibility event there is a meaningful distinction between obtaining any pair and obtaining an asymmetric founding quorum. The entire female-bias response to population budget and to quorum is resolved, not just a numerical optimum or a stationarity equation. The departure from parity and the optimized failure scale quantify a tradeoff not captured by either deterministic proportions or a fixed universal founder share. These are model benchmarks, not release recommendations or persistence predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
