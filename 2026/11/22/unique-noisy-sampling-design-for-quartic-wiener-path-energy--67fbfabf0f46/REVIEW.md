# Scientific review

## Correctness — PASS
The claimed design is the exact risk minimizer for the stated Gaussian experiment. Gaussian-Hermite projection gives the two orthogonal explained-variance terms; Wick contraction gives total target variance \(38/5\). Direct differentiation and an eight-coefficient Mobius-transform polynomial with exactly one Descartes sign change prove one interior stationary point and hence the unique global optimum for every finite \(\eta\ge0\). Positivity of two explicit quotient derivatives proves that the quartic optimum is strictly later than the quadratic optimum. The high-noise expansion follows from the analytic local derivative expansion and the implicit-function theorem. Exact symbolic checks were executed from the package's own verifier; finite sampling comparisons support, but do not replace, the proof.

## Originality — PASS (qualified)
The principal full-text comparison, Foster–Lyons–Oberhauser (arXiv:1904.06998, Theorems 1.2 and 3.7), establishes a *quadratic* Brownian time-integral conditional estimator given endpoint and extra space–time-area information. It does not state or imply the noisy single-point quartic design, its Descartes certificate, or strict cross-chaos ordering. Cui–Chronopoulou (arXiv:2304.07661, model/Section 3) optimizes whole-process state-reconstruction distortion, not quartic energy. Kałuża–Morkisz–Przybyłowicz (arXiv:1812.10708, introduction/noise formulation) uses a distinct noisy Ito-integration minimax model. Scientific searches for equivalent quartic-energy titles, closed constants, and broader point-evaluation results did not yield covering accessible results; failed searches are not a novelty proof. A historically unindexed theorem or unpublished derivation remains possible. The basic conditional-Gaussian identities are not claimed as new.

## Value — PASS
The object is a natural fourth-degree Brownian path observable, needed in high-moment path simulation and nonlinear weak-error studies. Its optimal one-measurement location is not the quadratic-energy location, and the strict ordering holds at every Gaussian noise level, not just a computed example. The result gives a complete, finite-parameter optimal design and risk formula together with an exact uniqueness certificate and sharp high-noise location scale. This is a nonlinear sensing classification rather than a renaming of the known quadratic endpoint formula. It does not promise general-purpose SDE error-rate improvements or multi-observation optimality.

## Closest literature and scientific limitations
- Foster, Lyons, Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998, https://arxiv.org/abs/1904.06998; quadratic time integral with richer linear data, not the specified quartic single-point noisy decision.
- Cui, Chronopoulou, *Optimal Sampling for Estimation of Fractional Brownian Motion*, arXiv:2304.07661, https://arxiv.org/abs/2304.07661; real-time signal reconstruction distortion, not nonlinear integral error.
- Kałuża, Morkisz, Przybyłowicz, *Optimal Approximation of Stochastic Integrals in Analytic Noise Model*, arXiv:1812.10708, https://arxiv.org/abs/1812.10708; noisy Ito-integration complexity model.

The literature searches are bounded and cannot exclude all historical equivalents. The analytic model assumes additive independent Gaussian measurement noise of known finite variance and only a predetermined one-point observation. An independent scientific audit is required for external acceptance.

Self-review: passed. Independent audit: not yet performed.
