# Scientific review

## Correctness — PASS

The published signed statistic and inverse-moment estimator are used exactly. Under \(\operatorname{Gamma}(k,\theta)\), the fitted scale tends to \((k-1)\theta\), giving a computable signed integral. Its integrand switches sign once at \(8(k-1)\); multiplying the integral by the positive factor \(e^{8(k-1)a}\) produces a strictly decreasing function. Positivity at \(a\downarrow0\) for \(2<k\le5/2\) and negativity at \(a\to\infty\) force precisely one simple root. A first-order V-statistic expansion with the inverse-moment estimator proves a fixed-alternative centered normal limit. The finite variance of the inverse-moment influence needs \(k>2\), and strict positivity follows because the fitted-scale derivative is nonzero while its inverse-observation influence cannot cancel a bounded first projection. The bundled numerical checker passed 33 supporting assertions, not a substitute for the analytic proof.

## Originality — PASS, with residual priority risk

The primary 2023 source defines the statistic, proves null asymptotics, and presents Gamma power simulations, but does not establish the root curve, its uniqueness, the exact Gamma-shape range from the zero-damping tail, or a fixed-Gamma alternative CLT at a blind root. Its consistency statement is for the separate supremum statistic. The 2023 Kumari–Bhati test uses an estimator-ratio construction and is not an implication-dominating general theorem for this signed integral. Searches for integrated-Laplace Lévy test blind Gamma tuning, signed transform power, and Gamma exact roots did not identify a direct covering result. Historical integrated-transform alternatives outside inspected sources could contain overlapping examples; the completeness of literature discovery is not mathematically certified.

## Value — PASS

A tunable goodness-of-fit test can lose consistency against an entire natural continuum of smooth fixed Gamma alternatives at exactly one weight per alternative. The sign-crossing proof supplies a structurally determined and unique calibration-failure locus, rather than an isolated arbitrary numerical zero; the boundary \(k=5/2\) comes from the integrand's exact tail integrability, and \(k>2\) is dictated by the inverse-moment estimator CLT. This identifies the cost of compressing a characteristic Laplace-transform discrepancy into a signed scalar, without asserting a failure of the companion supremum statistic or of recommended source weights.

## Scope and closest literature

Lukić–Milošević, *Statistics* 2023, DOI 10.1080/02331888.2023.2238236, Eq. (4), Theorem 2, simulations and appendix, is the closest primary source; the Gamma(3,2) simulation is not a theorem excluding shape \(k\le5/2\). Kumari–Bhati, *Journal of Applied Statistics* 2024, DOI 10.1080/02664763.2023.2251098, is a different test. The exact root is proved only for \(2<k\le5/2\); small parameter values were outside the primary simulation grid. Independent validation and exhaustive historical priority checks were not performed.

Self-review: passed. Independent audit: not yet performed.
