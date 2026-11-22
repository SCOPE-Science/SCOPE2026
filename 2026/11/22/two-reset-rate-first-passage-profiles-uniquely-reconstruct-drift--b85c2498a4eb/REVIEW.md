# Scientific review

## Correctness — PASS

The stated generator convention is \(D f''+b f'\), with absorbing at zero and reflecting at \(L\). Renewal of reset cycles gives the exact mean profile \(m_r=(1-\phi_r)/(r\phi_r(x_\star))\). The positive Green-integral identity \(-p\phi_r'=r\int_x^L p\phi_r/D\) proves positive profile slopes. Strong Markov first-hitting factorization strictly orders the ratios \(\phi_r(y)/\phi_r(x)\) across reset rates, hence the logarithmic slopes and strictly positive Wronskian; Cramer's rule reconstructs the coefficients. Compactly supported perturbation shows that one rate is insufficient. The supplied numerical checker independently verifies example coefficients, Wronskian signs, and inverse normalization. No finite computation is substituted for the all-coefficient proof.

## Originality — PASS, qualified

The initiating full primary text (Keidar–Reuveni–Sokolov, arXiv:2611.03831) concerns known constant diffusion, no resetting, and a potential inferred from a single MFPT profile. Bal–Chou (2004), whose full text was inspected, uses a complete FPT-time distribution at a fixed start, not two spatial MFPT scans. A drift-only inverse paper (Fok, 2013) was available only through bibliographic abstract. Searches for multiple Laplace hitting transforms, two resetting rates, coefficient recovery, Wronskian nonvanishing and inverse first-exit theory, including indexed result comparisons, did not identify a covering theorem. A general diffusion-inversion principle or unpublished equivalent could establish implicit prior coverage; novelty is a qualified scientific comparison, not a claimed exhaustive uniqueness certificate.

## Value — PASS

Two controllable reset-rate experiments provide an explicit and **minimal** way to identify two nonparametric spatial transport coefficients from just mean passage times. The strict denominator theorem makes this meaningful for every smooth nondegenerate drift/diffusion pair, not merely generic data, and the one-rate ambiguity proves the extra experiment carries indispensable information. This addresses model identifiability in reset-assisted search and transport. Practical finite-sample stability remains open; differentiation near the reflecting endpoint is fragile.

Self-review: passed. Independent audit: not yet performed.
