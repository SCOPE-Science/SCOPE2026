# Scientific review

## Correctness — PASS
The starting residual is contained in the positive spectral subspace for a consistent full-column-rank linear system. Direct expansion of the RD difference step yields the two spectral multipliers and the **exact** recurrence \(e_{k+1}=e_k/(\kappa^4e_{k-1}^2)\). The ordinary first step fixes \(e_1=1/e_0\), so the transformed logarithmic data cannot both be zero. Completing the square establishes the sharp gap \(C\ge2\log\kappa\). Exact multiplication of multipliers, bounded log-sum-exp errors and a uniformly positive phase envelope establish the all-integer doubly-exponential bound. `verify_rd.py` passed 417 independently formulated finite checks. The numerical tests do not establish the infinite assertions; the analytic derivation does.

## Originality — PASS, qualified
Xu (arXiv:2611.02743v1) introduces both delayed residual and residual-difference methods but only proves the two-spectral window statement for the delayed residual (DR) rule, not RD. Earlier mathematical records include a scaled-log profile for **matched BB1** and an all-start sharp exponent for an **alternating BB1/BB2** rule. Both full claim texts were compared: neither states the pure RD result with the specified first steepest-descent step nor its sharp initial-ratio-uniform lower amplitude. Older BB theory proves generic two-dimensional superlinear convergence and bounds fixed BB2 worst-case root factors, which are weaker statements. Spectral-weight conjugacy and unindexed historical BB2 analyses may implicitly contain this calculation; they remain priority risks, as do unavailable full texts of pertinent older sources. No novelty conclusion is inferred merely from negative keyword searches.

## Value — PASS
The RD algorithm is an explicit proposed residual solver with its canonical convergence behavior less understood than DR. For two active singular values, eliminating the exceptional slow trajectory **without alternation** and locating the unique smallest possible growing log-ratio amplitude answers a natural question about reliable startup and spectral adaptation. The result is not a routine known-rate restatement: its full all-initialization claim and sharp amplitude constraint distinguish it from existing fixed-BB and alternating-BB results.

## Boundaries and limitations
Two positive active spectral values, consistency, the stipulated SD initialization and exact arithmetic are necessary scope assumptions. No many-eigenvalue, floating-point or wall-clock estimate follows. Independent mathematical audit is pending; earlier equivalent specialist work cannot be ruled out by this review.

Self-review: passed. Independent audit: not yet performed.
