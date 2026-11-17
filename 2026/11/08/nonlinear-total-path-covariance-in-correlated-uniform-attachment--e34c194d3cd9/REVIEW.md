# Independent mathematical audit

## correctness

PASS

For each uniform-attachment arrival, M_n^{(a)}=(S_n^{(a)}−n(H_n−1))/n has centered martingale increment (D_parent−empirical depth mean)/(n+1). Aligned parent selection yields conditional cross-increment covariance αQ_n/(n+1)^2; independent selections contribute zero. The exact centered sample-covariance update gives q_{n+1}=n(n+1+α)q_n/(n+1)^2+n/(n+1)^2, c_{n+1}=c_n+αq_n/(n+1)^2. Product solution n q_n=[1+αn−∏_{j=1}^n(1+α/j)]/[α(1−α)] and endpoint limits check. L² boundedness follows by domination by identical-tree empirical depth variance O(log n), yielding almost-sure and L² martingale limits. Binomial generating-function integral and partial fractions give C(α)=∑_{j≥2} α/[j²(j−α)], with strictly positive zeta expansion coefficients and attenuation C(α)<α(2−ζ2). Independently enumerated all paired parent histories for n=2..5 at α=0,1/2,1 and compared q_n,c_n to exact recurrences, all equal. Finite enumeration is not the proof of infinite series or convergence.

## originality

PASS

PASS best-of-knowledge for the exact nonlinear two-tree root-path covariance, not the already-known single-tree variance or the general coupling construction.

## value

PASS

The exact covariance response quantifies a natural global growth-cost statistic under continuously tuned inter-tree attachment dependence. Strict ρ(α)<α, strict convexity and the complete finite-n recurrence are informative structural facts beyond copying a marginal constant. Relevant to correlated tree statistics even without a general graph-matching estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
