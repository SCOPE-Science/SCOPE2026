# Scientific review of the two-sided location-normalized empirical-process tail

**Correctness — PASS.** The statistic is defined using the same maximizing rank before division as Ferger's two-sided formulation. The event of a large ratio localizes to an order statistic near either null-CDF endpoint. At the lower corner the other order statistics must occupy explicit disjoint intervals, yielding an exact integral. Reflection doubles its contribution; any other high-ratio event requires at least two endpoint-near observations, with probability of order at most the fourth inverse power. A 96-assertion checker independently evaluates the formulas and simulates the unmodified statistic. Infinite tail-threshold conclusions are proved analytically.

**Originality — PASS, with residual historical risk.** The primary paper's one-sided full null CDF is known, and that side is not presented as original. Its two-sided result is a weak limit, not the stated fixed-sample endpoint-corner tail coefficient. Searches targeted the two-sided argmax weight, exact tail, moment threshold, generalized weighted KS statistics and old maximizing-location results. No stronger, explicitly covering result was located. A classical joint maximum/location distribution could conceivably imply the coefficient after additional analysis, so this is not a certification of historical priority.

**Value — PASS.** The exact factorial coefficient is relevant to extreme-null calibration of a published two-sided goodness-of-fit procedure. The infinite finite-sample variance, logarithmic truncated-moment growth and very rapidly shrinking coefficient with sample size explain a consequential distinction between finite-sample tail risk and ordinary weak-limit calibration. This is more than a renamed identity or arbitrary finite-sample case.

Closest literature: Ferger (2022/2023), Theorem 2.1 (one-sided exact CDF), Theorem 2.3 and Appendix A.1 (two-sided weak law and order-statistic representation), arXiv:2207.07947. The journal version has the same title and publication metadata, but exhaustive comparison of every possible earlier general result is not claimed.

Limitations: fixed \(n\), asymptotic in the tail threshold only; no complete two-sided finite-sample CDF, no uniform-in-sample-size rate, no claimed finite-level calibration accuracy. External independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
