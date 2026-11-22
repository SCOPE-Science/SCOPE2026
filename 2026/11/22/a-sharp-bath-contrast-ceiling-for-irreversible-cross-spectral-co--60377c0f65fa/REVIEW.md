# Self-review

## Correctness — PASS

For all \(a>k>0\) and \(T_x,T_y>0\), the independent resolvent calculation yields the stationary complex cross-spectrum. The ratio, positive-frequency derivative with exactly one zero, strictly positive coupling derivative, and exact boundary substitution are shown algebraically in RESULT.md; no finite computation is used as an infinite proof. The equal-temperature degeneracy and loss of stability at \(k=a\) are explicitly separated. The standalone checker verifies exact symbolic identities and rational sample cases. Residual correctness risk concerns conventional Fourier sign normalization only, which disappears upon squaring and normalizing.

## Originality — PASS, qualified

The nearest complete primary source, Cerasoli et al. (2022), studies the same Brownian-gyrator general framework, so that framework and standard spectral computation are not claimed. Its Eq. (17) is a Pearson coefficient of two single-trajectory power-spectral densities; the inspected body (Secs. III–V, pp. 4–9) and Appendix C discuss this and its small-frequency behavior rather than the imaginary complex cross-spectrum's global sharp temperature ceiling, optimizer and edge nonattainment. Henkel (2021) analyzes two quantum harmonic oscillators with baths and spectra but without the claim for this overdamped model. General spectral Cauchy bounds are insufficient to imply the nontrivial temperature-only envelope. The finite literature/database searches cannot prove uniqueness; hidden implicit coverage in other response-theory treatments remains a publication-priority risk.

## Mathematical value — PASS

The standard magnitude squared coherence can be nonzero for reciprocally coupled equilibrium coordinates, so it is not intrinsically a time-arrow witness. The squared imaginary component isolates chronology-antisymmetric coupling: it vanishes identically at equal temperatures and its maximum at fixed coupling is at one exactly prescribed measurement frequency. The unexpected bath-temperature-only global limit and unattainability for stable traps provide a sharp calibrated benchmark beyond a restatement of a resolvent or an arbitrary numeric invariant. This is an exact ideal-spectrum structural statement, not a claim about finite-sample signal-to-noise or entropy-production efficiency.

Closest source: https://www.smri.it/Publications/Phys_Rev_E_Gyrator_Spectra.pdf, in particular discussion of Eqs. (16)–(20) and Appendix C. Additional spectral context: https://onlinelibrary.wiley.com/doi/full/10.1002/andp.202100089. No independent scientific validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
