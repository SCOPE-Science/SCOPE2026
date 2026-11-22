# Scientific review

## Correctness (PASS)

The theorem concerns all deterministic nonadaptive zero-threshold sign measurement times and all measurable decoders, without assuming Gaussian conditional linearity (the observation has only two values). The reflection-principle density \(2(a+d)\phi(a+d)\), its exchangeability, and the independent future reflected maximum give the exact mixed moment \(\mathbb E[M\operatorname{sgn}(W_s)]\). The Gaussian integrations defining \(I_b\) and \(K_b\) are explicitly evaluated and checked independently with quadrature. The derivative \(q'(s)\) changes sign exactly once at \(s=16/21\). The risk therefore has one unique global minimum. The supplied verifier passed 27 assertions. Numerical checks confirm identities at sampled times but are not relied upon for the continuum theorem. Limits: no arbitrary threshold/encoder claim.

## Originality (PASS, with historical-priority risk)

Published-record searches for the nonterminal sign-sensor/maximum problem, its \(16/21\) parameter and Gaussian conditioning aliases found no matching theorem. The exact published maximum–endpoint odd-transform theorem gives the **terminal sign case** but says nothing about the interior time curve. The cyclic-bridge maximum–position theorem concerns a different stochastic process (pinned bridge), and hence does not imply this free-Brownian optimum. Inspecting the available full texts of Bisewski–Crommelin–Mandjes (2017), Grill–Valko–Munos (2019) and Riedel (2019), their subjects are respectively barrier-crossing probability, full-valued adaptive maximum optimization, and reverse conditional estimation of Brownian trajectories given extrema. The central one-bit Bayes-risk/timing result is not stated or implied by the assessed claims. Aksenov et al. (2019) could be assessed only through summaries, and another equivalent result under a different title may exist; independent exhaustive historical priority is not certified.

## Value (PASS)

The precise information budget (one 0-threshold sign, fixed in advance), natural numerical target (running maximum), and exact risk permit a sharp sensor-placement policy. The unique rational location \(16/21\) is counterintuitive relative to using the terminal sign: it improves Bayes MSE by \(8.8164\ldots\%\), while recovering \(48.7534\ldots\%\) of prior maximum variance. The result determines a complete one-bit design problem in a natural constrained class, rather than a fixed arbitrary numerical slice. Its mathematical scope is deliberately restricted to Brownian motion and zero-threshold bits.

Self-review: passed. Independent audit: not yet performed.
