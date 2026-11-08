# Review of the sharp weak-partial-reset tail result

## Correctness — PASS

The new theorem is a *relative* rare-tail asymptotic, not just a large-deviation logarithmic equivalence. The proof checks the stationary independent-Laplace product and moment-generating domain, then obtains a uniform-on-parameter-compacts Euler–Maclaurin expansion with the half-endpoint term. It establishes the uniquely optimizing positive tilt and, crucially, a **density-level** tilted local central limit theorem from an integrable Fourier bound. Inverting that tilt returns both the asymptotic probability and its exact multiplicative coefficient. Explicit checks fix the Brownian diffusivity \(D\), Poisson rate \(r\), Laplace scale \(\ell=\sqrt{D/r}\), contraction \(e^{-\varepsilon}\), and strict positive threshold before the weak-reset limit. The standalone script passed 289 finite diagnostic assertions; the analytical proof, not the script, supports the asymptotic quantifier.

## Originality — PASS, with residual risk

Pierce (arXiv:2204.07215), Tal-Friedman–Roichman–Reuveni (arXiv:2205.03363), Di Bello et al. (arXiv:2305.13722), and Biroli et al. (arXiv:2406.08387) establish the stationary transform and fixed-parameter Gaussian-core/exponential-tail facts. The first two have earliest public dates in 2022. Vysotsky (arXiv:1909.00374, Theorem 6.1) and the stronger general weighted-sum theorem of Najim discussed there substantially cover the **logarithmic LDP**, which is not claimed as new. They do not directly supply the model's evaluated one-sided relative-tail prefactor, requiring the subleading logarithmic Euler–Maclaurin term and tilted density control. The semantic-result search returned no exact match and the accessible prior claims were checked for overlap; absence in search is not proof of global priority. A broad unindexed precise-deviation theorem could still imply the specialized coefficient.

## Mathematical value — PASS

The exact factor \(\sqrt\varepsilon/[\theta_y\sqrt{2\pi\Lambda_\ell''(\theta_y)(1-\ell^2\theta_y^2)}]\) matters quantitatively: keeping only the large-deviation exponential loses a factor tending to zero. It makes rare displacement probabilities under progressively weaker multiplicative resets computable without unstable fixed-parameter asymptotic interchange, while retaining a natural nonlinear rate transition between Gaussian and exponential regimes. This is a motivated sharp asymptotic beyond restating an existing moment or stationary law.

## Limitations

The probability asymptotic is pointwise for fixed positive threshold and fixed physical scales. It is not uniform near the central-limit window or at thresholds growing with inverse contraction, and it does not address arbitrary resets or finite-time transients. Independent scrutiny and priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
