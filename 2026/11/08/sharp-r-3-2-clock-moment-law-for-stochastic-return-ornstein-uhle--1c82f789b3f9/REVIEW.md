# Scientific review

## Correctness — PASS

The pure-return OU potential \(U\) solves the backward hitting-time equation and has gradient \(-K\). The generator defect \(1+\mathcal L_1U=(k_1-k_2)xK(x)\), combined with the return stopping rule, gives the exact cycle identity. The short-time killed-OU estimates have the explicit coefficients \(2t\) and \(\sqrt t/(S_2\sqrt\pi)\); the second moment of \(W\) supplies the required domination. The moment-ratio coefficient follows without an exponential-clock assumption. Independent quadrature against killed Brownian kernels checks the Poisson renewal identity and the deterministic/two-point asymptotic coefficients. Finite tests do not prove the limit.

## Originality — PASS, qualified

The closest source, Dubey and Pal (arXiv:2610.18814v1), gives a Poisson-clock exact MFPT and its finite high-rate saturation; its complete model section and appendices were compared with the proposed arbitrary-clock high-rate two-moment theorem. Biswas, Kundu and Pal (arXiv:2307.16294) give a general stochastic-return renewal approach for arbitrary clocks, but do not state this specific universal fast-clock coefficient. Biswas et al. (arXiv:2406.08975v1) treat drift diffusion with linear return force. Equivalence, broader parameter coverage, direct formula implication, and table coverage were separately examined. The central novelty is the non-Poisson moment-ratio law, not the pre-existing Poisson renewal model, a generic renewal formula, or a finite-rate MFPT formula. An unindexed general fast-clock theorem is a residual risk.

## Value — PASS

The sharp \(r^{-3/2}\) approach quantifies a limiting regime already explicitly relevant to finite-time-return experiments. At equal mean clock duration, deterministic, two-point and Poisson renewal protocols have different explicit leading corrections, so clock-shape information survives the fast-clock limit. The two controlling moments and exact equal-stiffness cancellation give a useful universality and boundary classification, rather than a routine single-parameter numerical refinement.

## Limitations

Proof assumes \(W>0\), \(\mathbb E W^2<\infty\), fixed \(k_1\ge0\), fixed \(k_2>0\), and identical diffusion intensity in both phases. Neither uniformity in a vanishing return stiffness nor finite-rate global optimality is proved. All novelty claims remain subject to independent literature review.

Self-review: passed. Independent audit: not yet performed.
