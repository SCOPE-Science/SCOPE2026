# Independent mathematical audit

## correctness

PASS

An excursion has length T=L/max_i V_i and survival exactly F(L/a)^N, so the tail exponent is γ=Nα, including divergent mean at equality. Continuity makes the renewal law nonarithmetic. For any fixed H>0 the probability of an observation age at most H is bounded, for t>H, by the expected renewals in (t−H,t], which tends to zero by the infinite-mean Blackwell renewal theorem. To disintegrate, sum over candidate last renewals: the next speeds are fresh and last status at age a is exactly the product event V_i<L/a for all i. Thus the displaced fractions have independent truncated CDFs F(zL/a)/F(L/a); these tend to z^α as a→∞, including the endpoints. The conditional cloud consequently converges on bounded continuous tests, which yields the unconditional iid Beta(1,α) limit, and bounded position moments yield vanishing covariance. For 0<γ<1 the same conditional expectation argument against a bounded function of A_t/t factors the joint limit with the classical Dynkin–Lamperti Beta(1−γ,γ) age fraction. For γ=1 only divergence of the absolute age is needed. In the finite-mean exact power family, the equilibrium of the age-and-speeds process is normalized excursion occupation, with age density Pr(T>a)/ET; the renewal reward kernels for bounded continuous position tests are continuous and bounded by a multiple of the integrable decreasing survival, so the key renewal theorem gives the stated convergence. Z=min(A/L,1) then has density (γ−1)/γ on (0,1) and an atom of mass 1/γ at one. Conditional means are 1−αZ/(1+α) and conditional covariance is zero. Integrating Z,Z² gives (γ+1)/(2γ), (γ+2)/(3γ), and the stated positive covariance. This coefficient requires the exact power law; no infinite-mean augmented stationary probability is inferred. Read check.py and VERIFICATION.md; the uploaded checks and simulation were not executed, and are not theorem certificates.

## originality

PASS

The strongest same-model indexed work treats exponential speeds with finite mean cycle length for N≥2, while the strongest renewal-boundary matches are Brownian or only about passage times. The shared-renewal argument and age theorem are credited premises. The distinct claim is the full unscaled independent spatial cloud and its independence from the macroscopic age for general regularly varying low speeds, with a positive finite-mean exact-power counterpart. The same-day comparison is based on mathematical scope, not inferred priority.

## value

PASS

A shared first-arrival clock creates dependence even with conditionally independent particles. The theorem gives a sharp example where that source of dependence disappears entirely from unscaled positions while the clock still has a random macroscopic age, against a strictly positive equilibrium covariance in the natural exact-power family. The equality case and general low-speed robustness make the result more than a numerical or single-particle observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
