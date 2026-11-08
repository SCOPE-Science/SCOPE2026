# Scientific review

## Correctness — PASS

The modal reduction uses a symmetric positive-definite Hessian and one iid common scalar jitter, so every eigenmode has the same mean-zero noise with curvature-scaled variance but its squared Euclidean norm remains the sum of modal squares. The explicit positive-definite solution \(W\) of the deterministic covariance Lyapunov equation, and the identity \(\mathcal K_v^2(W)-W=(vW_{11}-1)(E+\mathcal K_v(E))\), establish strict two-sided necessity and sufficiency. The latter bracket has determinant \(1+v>0\), with a strictly positive diagonal. The threshold decreases in curvature, giving the exact all-matrix maximum-eigenvalue frontier. Independent exact symbolic checks and exhaustive rational finite-horizon examples passed. The experimental checks are not used as proof for infinite-time convergence.

## Originality — PASS, qualified

The inspected full texts on minibatch heavy-ball, noise-adaptive stochastic heavy-ball, spectrally expressible minibatch momentum, stochastic heavy-ball convergence, multiplicative random recurrences and stochastic SGD do not state this distribution-free sharp common scalar-jitter threshold and its strict Chebyshev-versus-GD contrast. Their general sufficient conditions, random-matrix concentration, model-specific generating functions and SGD moment formulas do not directly imply the stated boundary without additional specialization and proof. The threshold method is related to classical random-coefficient AR(2) moment stability and could conceivably be a known disguised result; a specialist precedence risk persists. The claim is not that second-moment Lyapunov methods or Chebyshev tuning are new.

## Value — PASS

The exact inequality answers a concrete robustness-design question for accelerated quadratic optimization, differentiating momentum from gradient descent under the same calibrated multiplicative stepsize uncertainty. The \(\kappa^{-3/2}\) versus \(\kappa^{-1}\) sharp variance budgets, and a nonnegative-jitter-step rational separation example, exhibit a structural cost of deterministic acceleration; this is more informative than a merely sufficient bound, a routine parameter substitution or an arbitrary finite table. It is a controlled benchmark, not an all-algorithm speed comparison.

## Closest literature and remaining limitations

Bollapragada–Chen–Ward (2022), arXiv:2206.07553, prove sufficient stochastic minibatch acceleration conditions; Dang–Babanezhad–Vaswani (2024), arXiv:2401.06738, study noise-adaptive heavy-ball; Velikanov–Kuznedelev–Yarotsky (2022), arXiv:2206.11124, consider a structured spectrally expressible minibatch noise operator; Loizou–Richtárik (2017), arXiv:1710.10737, have distinct stochastic sketch settings. Common-step iid jitter here is not independent per coordinate, minibatch sampling, or additive noise. Unindexed specialist random-coefficient AR(2) or robust-control work may subsume the scalar Lyapunov identity. Deterministic-optimal versus robustly-retuned methods should not be conflated.

Self-review: passed. Independent audit: not yet performed.
