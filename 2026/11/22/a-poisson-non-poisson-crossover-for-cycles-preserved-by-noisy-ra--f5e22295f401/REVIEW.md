# Scientific review

## Correctness — PASS
The result is based on a fully counted collection of vertex-disjoint oriented cycles. A prescribed \(k\)-cycle survives both mappings with probability \((s_n/n)^k\); ordered lists yield the exact falling-factorial formula. Compactly supported multiplicative-functionals are bounded by an exponential series, so the critical Riemann-sum limit, the intermediate Poisson limit and the finite-noise limit follow without an unwarranted moment-determinacy step. The critical cross-band covariance is a strict negative double integral because the union of two cycles consumes a joint set of vertices. A tail bound allows convergence of the largest-cycle distribution. The standalone verifier exhaustively enumerated 50,068 maps over sizes two through six and passed 115 rational checks. These finite checks corroborate, rather than certify, the asymptotic theorem.

## Originality — PASS (qualified)
The closest literature is Aldous–Pitman (1994 and their 2004 full-text treatment), Hansen–Jaworski (2007 and 2010), and Finch (2022). The 2010 primary paper's conditional uniform permutation representation is prior art; the 2022 longest-cycle law is prior art for the unrefreshed endpoint. The 2007 trimming process cuts **noncyclic** rather than cyclic edges. The selected claim is about **surviving identical directed cycles under independently refreshed outgoing edges**, with a noise-dependent critical factorial density, new strict negative cross-size covariance and a crossover to the Poisson extreme regime. No covering statement was found in accessible full text and actual indexed searches; this cannot establish absolute historical uniqueness. A full original copy of the 1994 paper was inaccessible, and unindexed general noise-marking equivalents remain possible.

## Mathematical value — PASS
The critical \(n^{-1/2}\) noise window and limiting cross-band covariance distinguish two different fluctuation mechanisms for cycle preservation. This is useful when assessing whether two closely related random functional networks retain the same periodic trajectories and how large the largest preserved trajectory can remain. It is not merely a restatement of the single-map cycle count or a fixed-size enumeration.

## Scope and limitations
The proof treats only identical oriented cycles and does not cover cyclic vertices whose trajectories have changed. It supplies weak convergence and explicit extreme-value formulas but not convergence rates. The \(a=0\) endpoint is classical. No independent mathematical audit was conducted.

Self-review: passed. Independent audit: not yet performed.
