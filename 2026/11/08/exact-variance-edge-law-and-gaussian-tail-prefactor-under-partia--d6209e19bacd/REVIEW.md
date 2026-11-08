# Scientific review

**Finding:** Exact variance-edge law and Gaussian-tail prefactor under partial Ornstein–Uhlenbeck resetting.

## Correctness (PASS)

The stationary Brownian convolution conditioned on Poisson history is Gaussian, with normalized conditional variance constrained between zero and one. Independent Poisson backward age yields the rigorous deficit perpetuity \(1-V=A(1-q^2V')\) with \(A\sim\operatorname{Beta}(r/(2\gamma),1)\). It implies the **exact** endpoint probability \(\mathbb P(1-V\le u)=B_{\alpha,q}u^\alpha\) throughout \(0<u<1-q^2\). The stationary variance generator gives the absolutely convergent explicit series for \(B_{\alpha,q}\); endpoint Laplace asymptotics give the exact Gaussian spatial far-tail coefficient. Coupled Poisson paths prove strictly increasing coefficient and divergence as \(q\uparrow1\). The standalone checker passes 336 exact and 10 high-precision tests. Those finite tests do not replace the distributional proof.

## Originality (PASS, with stated priority risks)

The closest same-model source is Olsen and Gupta, *Thermodynamic work of partial resetting* (arXiv:2401.11919), Section III.3, which derives the second stationary moment for harmonic exploration and proportional resetting, **not** the exact deficit-edge density or full sharp tail. Assefa, Keller-Ressel and Palmowski (arXiv:2610.01363) give a general affine-resetting moment framework, acknowledged here; finite polynomial moments do not state the new asymptotic coefficient. Biroli and colleagues (arXiv:2406.08387) obtain exponential tails for unconfined Brownian motion under proportional resetting, and Grzywny and colleagues (arXiv:2412.15626) cover stable free drivers without continuous harmonic damping. The \(q=0\) case of standard site resetting is acknowledged, not proposed as new. Related Frydel 2026 fluctuating-trap work (arXiv:2607.05173) was compared through its abstract, not inaccessible full text. Indexed-search and published-claim comparisons disclosed no direct coverage; broader unindexed results remain a priority risk. The explicit source/claim implication comparisons and search expressions are in `AUDIT.json`.

## Mathematical value (PASS)

At fixed trap and resetting rate, the rare spatial tail depends on reset amplitude only through a computable coefficient, while its algebraic decay exponent remains \(r/\gamma\) for every fixed partial reset. This is an exact rare-fluctuation prediction and a meaningful singular boundary as resetting becomes ineffective, rather than a routine re-expression of the pre-existing second moment. The exact variance-deficit power law supplies a structural explanation and a reusable link between conditional variance near its maximal support and particle tails.

## Limitations

The theorem is restricted to a scalar stable harmonic OU drift, additive Brownian noise, positive Poisson reset rate and constant \(0\le q<1\). The fixed-amplitude tail is not uniform as \(q\uparrow1\); the unperturbed case is exactly Gaussian. Models with stochastic stiffness, nonlinear traps, random amplitudes or nonexponential reset clocks are not covered. A relevant recent source was accessible only by abstract; external publication-priority verification and independent scientific review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
