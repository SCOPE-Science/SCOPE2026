# Scientific review: An exact moment dichotomy for noisy Aitken extrapolation

## Correctness — PASS

The claim is about one unmodified scalar Aitken \(\Delta^2\) transformation applied to three geometrically spaced real values plus centered jointly Gaussian observation noise. The proof explicitly retains every singular-covariance case. When the random second difference has zero variance, it is the nonzero deterministic curvature \(b(q-1)^2\), and the output is a quadratic Gaussian polynomial. Otherwise, Gaussian regression writes the numerator's first difference as \(\kappa V+H\) with \(H\) independent of the random curvature \(V\). The only way to cancel the pole is \(\mathbb E H^2=0\), which is equivalent to maintaining the unperturbed geometric ratio almost surely. In all remaining cases, both one-sided tail coefficients are \(f_V(0)\mathbb EH^2\), strictly positive. The proof controls Gaussian tails away from the denominator pole and uses conditioning and layer cake for the precise moment threshold. SymPy and high-precision normal-integral verification pass 93 assertions. These numerical checks supplement, rather than establish, the limit theorem.

## Originality — PASS, with residual precedent risk

The classical Aitken kernel and small-denominator sensitivity are known. Pomeranz (2017), which directly supplies the numerical-extrapolation context and classification 65B05, develops deterministic sign-pattern extensions, not exact Gaussian covariance-dependent moment laws. Chen et al. (2021) discuss abnormal estimates when an Aitken denominator nearly vanishes in fixed-data gradient estimation; their displayed convergence analysis is not a single random triple with arbitrary positive-semidefinite noise covariance. Hodgkinson–Mahoney (2020) develop heavy-tail mechanisms in stochastic optimization dynamics, not one-step Aitken ratio poles. Existing two-evaluation Gaussian Anderson calculations also have order-one moment tails: the bare observation of a Cauchy-like instability is therefore **not** the novelty claim. The distinct result is the complete three-observation covariance-dependent finite-moment dichotomy and exact two-sided coefficient, including the perfect-versus-imperfect exchangeable-noise boundary. Closely related specialist treatments of noisy Shanks transforms could remain undiscovered.

## Value — PASS

Three-run extrapolation of noisy discretization or fixed-point data is a natural numerical task; using common or correlated random numbers is a motivated variance-control choice. Here even Gaussian perturbations with arbitrarily small positive curvature noise invalidate the absolute expectation of the unmodified accelerated value, while precisely identifiable correlated designs avoid the pole. A closed tail constant distinguishes formal infinite variance from practically rare extreme events and allows a principled diagnosis of whether clipping, shared randomness, or a different extrapolator is warranted. This provides stronger actionable information than a generic caution about small denominators, while making no unsupported claim for higher-order or nonlinear algorithms.

## Limits and provenance

The result assumes Gaussian additive noise and exactly three scalar geometric terms. It says nothing about robust or denominator-regularized extrapolation, and the finite verification sample is not an infinite-tail proof. An earlier mathematically equivalent calculation under Gaussian ratio statistics, Shanks extrapolation or Anderson acceleration remains possible. No independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
