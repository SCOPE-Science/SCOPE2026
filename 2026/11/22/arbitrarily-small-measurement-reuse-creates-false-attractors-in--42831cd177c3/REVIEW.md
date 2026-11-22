## Correctness — PASS

The winner law follows from strict absolute-residual ordering and the probability that all screened observations have the adverse sign. Conditional independence given the winning cached sign and total variance yield the exact \(p\)-dependent covariance, including all endpoints. The stopped squared-error supermartingale, the explicit Basel sum, and square-summable/noise-divergent-step convergence prove a lower bound on actual wrong-limit probability, not merely a mean-drift picture. Exact rational checker: `VERIFY_OK 2268`. The checker does not prove asymptotic claims.

## Originality — PASS, qualified

Compared with the relevant full-text literature, independent update sampling in Battaglia et al. (2026) makes its convergence question different; Cai et al. (2025/2026) control screening sample size, not partial-refresh dynamics. Shvaiko–Rebrova (public 16 November 2026) already discuss selection bias and full refresh. An earlier scalar cached/fresh constant-step identity also gives a noise floor. The material not implied by those claims is the exact Bernoulli-partial-refresh \(p\)-interpolation, its **sharp \(p=0\) phase boundary**, and a constructive lower bound for actual convergence to a false attractor despite Robbins–Monro steps. Unindexed specialized work, and alternate algorithm reductions, remain residual priority risks; no exhaustive historical uniqueness is claimed.

## Value — PASS

Fresh versus reused observations is an operationally motivated numerical solver design choice. A positive-probability trajectory that converges to an incorrect solution even with decreasing steps is a stronger defect than a static positive variance floor. The exact law makes clear why a very small reuse fraction cannot be repaired by scaling only update batch size, while full-refresh sampling has a rigorously different consistency outcome. These conclusions are restricted to the specified scalar minimum-residual selection and do not claim arbitrary-matrix algorithm failure.

Self-review: passed. Independent audit: not yet performed.
