# Scientific review: spectral zero ladders in burst-fed two-target diffusion

## Correctness (PASS)

The endpoint-hitting transforms solve the stated killed Brownian boundary-value problems. A stationary Poisson source with independent offspring yields the off-diagonal cluster covariance density \(b\mathbb E[K(K-1)]\int f_L(u)f_0(u+t)du\), with the correct Fourier orientation and no same-particle contribution, because one particle cannot hit both targets. The exact hyperbolic-sine ratio yields an exponentially controlled cosine of phase \((L-2x)\operatorname{Im}\sqrt{(\mu+i\omega)/D}\). Differentiable uniform error control proves one simple zero per sufficiently high cosine crossing, rather than merely observing numerical sign changes. Expansion of \(\omega=2Dv\sqrt{v^2+\mu/D}\) proves both the quadratic zero coefficient and the additive mortality intercept. The delivered checker passes 106 analytic/eigenfunction/complex-frequency comparisons; it is not used in place of the infinite proof.

## Originality (PASS, with explicit residual risk)

The initiating November 2026 synthesis/degradation paper (arXiv:2611.04843) contains burst injection, density and first-passage statistics but no two-absorber stationary cross-spectral zero-ladder classification in its inspected sections. Classical multivariate point-process spectra (Bartlett 1963; Hawkes 1971) and Poisson-cluster theory (Westcott 1973) already cover the general point-process spectral ingredients, which are fully credited. The distinguishing result is the sharp midpoint/off-center **sign** dichotomy, eventual simplicity and quadratic-plus-mortality root locations for killed interval diffusion. Searches of indexed related findings and literature did not identify a statement or stronger theorem asserting this complete spectral zero classification. Westcott's full original paper was not accessible, so implicit coverage through a specialized corollary cannot be excluded; this remains a real publication-priority risk, not a proof of uniqueness.

Closest indexed comparisons include a prior renewal-production result for mortal diffusive searchers (which determines long-time survival rather than target-current spectra), a spatial factorial-cumulant result for burst immigration (which does not concern two absorbing endpoints or cospectral zeros), and a resetting-diffusion boundary-current tomography result (which uses mean flux and reset rates rather than burst point-process arrival cross-spectra). The classical Poisson cluster cross-spectrum is not presented as new.

## Value (PASS)

Two target-reaction streams are a natural observable in burst-fed molecular transport. The signed cospectral bands offer a subtle frequency-domain distinction: all real-time target covariance densities are nonnegative, yet every off-center source has infinitely many negative real cross-spectral bands. The high-frequency zero locations reveal both source asymmetry and molecular mortality using no knowledge of the burst rate or factorial burst intensity, provided diffusion and interval geometry are calibrated. The same model has a sharp symmetric exception; the result is not an arbitrary numerical slice. This is exact mathematical identifiability, not a robust finite-noise estimation guarantee, since the high-frequency cospectral amplitudes are exponentially small.

## Limitations and source comparison

The result assumes independent offspring, Poisson synthesis bursts, perfectly absorbing interval endpoints and constant diffusivity/degradation; non-Poisson clocks or partial radiation boundaries may alter the classification. Source theory of spectra is older and very broad. The Boyer–Mercado-Vásquez full preprint and the accessible Hawkes spectral exposition were materially examined; Westcott was available only in abstract/landing page, and the Pal–Prasad interval FPT work was accessible in abstract form. A plausible omitted or unindexed derivation could still dominate the novelty claim. No independent reproduction or external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
