# Independent mathematical audit

## correctness

PASS

At p^a the weighted divisor factor is (ceil(a/r)+1)/2 for a>=1, and its first differences are 1/2 exactly at a=jr+1, j>=1. Hence f_r=1*b_r with b_r nonnegative and C_r=G_r(1). In H_r=G_r/zeta((r+1)s)^(1/2) the order-p^(-(r+1)s) terms cancel and absolute local coefficient tails start at exponent 2r+1. The transfer of the standard half-divisor summatory law to B_r is valid: coefficients of H_r are absolutely summable with weight d^(-sigma) for 1/(2r+1)<sigma<alpha=1/(r+1), and the portion d>exp(sqrt(log X)) is bounded by X^alpha exp(-(alpha-sigma)sqrt(log X)) times that weighted sum. The small-d portion gives the stated kappa_r, including sqrt(r+1). Partial summation gives X times the tail as -B_r(X)+X integral_X^infinity B_r(t)/t^2 dt, with leading coefficient kappa_r alpha/(1-alpha). The floor remainder is nonnegative and at most B_r(X); the prime support above any finite X makes the tail strictly positive, also for noninteger X. This proves the displayed brackets, not their optimality or the existence of a limit. The frozen verifier was inspected as finite arithmetic corroboration, not as proof of the analytic steps.

## originality

FAIL

A distinct earlier published record, 2026/10/18 SCOPE-sharp-power-log-deficit-for-weighted-minimal-power-divisor-means--658bad68f3aa, treats the identical half-weighted sequence and fixed r>=2, gives the identical positive convolution and its asymptotic, and evaluates the exact leading signed discrepancy. Its equation (7) and nonnegative kernel already imply strict positivity for every finite real X>=1; (6)-(8) imply the submitted brackets. The stronger limit proves the same sharp order. Bouderbala's journal/preprint comparison is weaker and does not remove this published overlap.

## value

FAIL

A signed power-log second-order scale for an existing arithmetic mean is mathematically useful, but this submission gives neither a new regime nor a new bound for that mean. The simple change from squarefree half-weights to the coefficients of zeta(s)^(1/2) in the analytic transfer does not add a mathematical consequence, and the submitted liminf/limsup enclosure is weaker than the existing exact constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
