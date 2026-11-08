# Scientific review: spectral-spike crossover for Legendre-residual acceleration

## Correctness — PASS

The claim is restricted to the explicitly defined normalized Legendre residual, the exact midpoint spectral grid, and Gaussian coordinate initialization. The reflected-outlier response follows exactly from parity and strictly positive hypergeometric coefficients of \(P_n(u)\) for \(u>1\). The bulk denominator concentration uses the exact Legendre \(L^2\) norm, the degree-\(n\) Markov derivative bound, midpoint discrepancy, and a direct Gaussian variance calculation. Exterior fixed-argument Laplace asymptotics yield the precise critical coefficient \(A=q/(\pi\sqrt{z^2-1})\), after which Slutsky proves the chi-square law. `check.py` passed 204 finite checks. The checks do not establish the asymptotic result by themselves; the displayed proof does.

## Originality — PASS, with explicit historical risk

Full relevant sections of the Legendre acceleration paper (Pedregosa–Scieur 2020, arXiv:2002.04756) were inspected, including the polynomial construction and its outlier-eigenvalue future-work paragraph; neither gives this Gaussian single-spike dimension/iteration crossover. The related Scieur–Pedregosa 2020 paper studies limiting momentum parameters for bulk laws, not one-spike relative error. Classical Chebyshev endpoint sensitivity does anticipate the stability aspect, so the reflected boundary is not being advertised in isolation as wholly unprecedented. The earlier Li 1995 comparison was abstract-only, and a specialist historical check could identify an equivalent specialization. Generic Legendre asymptotics do not by themselves state the probability of a rare initialized eigendirection dominating a discrete, randomly initialized numerical iterate; the proof supplies the discrete concentration and the exact constant.

## Value — PASS

A uniform-density-calibrated numerical optimizer may lose spectral robustness through a single low-mass outlier. The result separates absolute amplification (controlled by \(c=a+b\)) from relative takeover (controlled by the exponential dimension scale \(q^{2n}\)). This separation is mathematically and computationally motivated: relative error can become almost entirely outlier-driven even when every eigencomponent contracts. The sharp chi-square window quantifies the likelihood of that takeover rather than giving a worst-case statement only.

## Closest literature and limitations

The closest constructive source is Pedregosa and Scieur (2020), §6, plus Scieur and Pedregosa (2020) on coefficient asymptotics; the related Chebyshev-sensitivity paper of Li (1995) was assessed from its abstract only. The proof uses classical Legendre identities and fixed-exterior-point asymptotics, not a new asymptotic formula for Legendre polynomials. The theorem does not cover multiple spikes, changing spectral bounds, non-Gaussian initialization, or noisy/nonlinear gradients. Its dimension growth condition is sufficient, not asserted sharp.

Self-review: passed. Independent audit: not yet performed.
