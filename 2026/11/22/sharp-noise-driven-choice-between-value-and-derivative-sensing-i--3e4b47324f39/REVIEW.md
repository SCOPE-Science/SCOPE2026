# Scientific review: sharp value-versus-derivative observation threshold

## Correctness — PASS

The domain is an exactly specified zero-start once-integrated Brownian process on \( [0,1] \) and one independent, equally calibrated Gaussian noisy observation, either \(X(x)\) or \(X'(y)\). Stochastic Fubini and Itô isometry yield the precise numerator covariances \(C(x)=x^2(x^2-4x+6)/24\), \(D(y)=y(y^2-3y+3)/6\) and variances \(x^3/3\), \(y\). Differentiation proves each branch's unique global maximizer. The value branch reaches the terminal boundary at noise variance \(1/24\). The ratio of the optimized derivative information reduction to the endpoint value reduction is strictly increasing, starts below one at \(1/24\) and tends to \(16/9\), hence has one crossing. The sextic and unique root are exact consequences. A reproducible symbolic-and-grid checker supports—but does not replace—the proof. The zero-noise zero-time observation is explicitly addressed.

## Originality — PASS, qualified

The exact result is **not** Gaussian posterior conditioning, the pre-existing unique value-only observation optimizer, or a two-point Gaussian quadrature algorithm. It is the sharp global choice between two different observation functionals for a fixed one-measurement budget, with a unique positive noise crossover and complete locations. Xi–Briol–Girolami (2018, arXiv:1801.04153) provide general multi-output Gaussian quadrature conditioning but not a sharp noisy IWP modality-switch theorem. Zhang–Stringer–Brown–Stafford (2023, arXiv:2302.02053) establish IWP smoothing and its derivative structure but no exact one-measurement decision between value and derivative. Related published Brownian-bridge and Ornstein–Uhlenbeck quadrature findings involve other covariance kernels, sample counts or information functionals. Search failure does not prove absolute publication priority; older optimal-recovery literature and unindexed equivalences are residual risks.

## Value — PASS

A measurement budget of exactly one requires choosing both a site and a measurement type. Integrated-Wiener priors encode a natural second-order regularity model in probabilistic numerical integration, where derivative data may be available from a different instrument. An exact crossover and complete optimum identify when a derivative observation improves integral prediction despite near-origin noise and how this changes with observation precision; the high-noise information gain factor \(16/9\) quantifies the effect. The result is a natural complete classification rather than a single arbitrary numerical test, while explicitly depending on equal dimensionless calibrated error variances. The claim does not assert superior physical accuracy outside the specified prior or arbitrary instrumentation.

## Sources and residual limits

Primary sources: https://arxiv.org/html/1801.04153v7 and https://arxiv.org/abs/2302.02053. Also compared published Brownian-bridge i.i.d. quadrature and Ornstein–Uhlenbeck node-design results through searchable scientific descriptions. The multi-output Gaussian identity is standard, and no independent priority or independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
