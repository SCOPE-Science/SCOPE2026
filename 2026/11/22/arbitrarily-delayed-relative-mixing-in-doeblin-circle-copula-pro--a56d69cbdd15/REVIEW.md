# Scientific review

## Correctness

**PASS.** The chain density integrates to one in both variables and is reversible with uniform stationary marginal. The exact independent-regeneration decomposition yields the formula for every multi-step kernel. On centered Fourier characters the transition operator has a signed two-dimensional spectrum, giving the exact maximal-correlation coefficient. The strict finite-lag threshold follows from generalized Young's inequality on one side and diverging positive Fejér means on the other, including odd lags and equality cases. The even-lag formula follows from nonnegative Fourier coefficients; the pole coefficient follows from a uniform incomplete-gamma oscillatory asymptotic. Boundary parameters are deliberately excluded. The standalone numerical consistency checker passed, but is not used as an infinite proof.

## Originality

**PASS, with residual priority risk.** The source construction by Lalancette–Zimmerman (arXiv:2204.04336, 2022) supplies the parent copula, not the lagwise relative-mixing classification. Their extended rotational family (arXiv:2509.26635, 2025) includes the Markov-product convolution closure and Fourier description; these are acknowledged and do not state the power-cusp critical lags or exact even-lag coefficients. Longla's 2022 mixing theorem (doi:10.1007/s44199-022-00045-1) supplies a general sufficient condition for eventual mixing, not the first finite coefficient nor its divergence. Classical harmonic estimates are used, not presented as new. Related published results on spectral mixing for other stationary copula chains concern distinct transition objects and do not imply the displayed singular-cusp threshold. Other harmonic-analysis accounts of power singularities could contain an equivalent convolution criterion; further specialist bibliographic review remains advisable.

## Value

**PASS.** Exact onset of bounded multi-step transition densities is a natural question in dependent-data error control, since relative-mixing coefficients quantify worst-case multiplicative event dependence rather than merely average correlation. The theorem provides the complete parameter-and-lag classification in a natural singular generator family, including an infinite relative-mixing plateau of arbitrary length under a uniform Doeblin bound. The exact even-lag formula and critical pole explain how the plateau ends. These properties cannot be inferred solely from small correlations or total-variation mixing and sharpen interpretation of highly irregular copula models.

## Limits and comparison

The result is restricted to the specified circle copula with a power singularity mixed with uniform independence. The exact series identifies even-lag coefficients, not a closed extremal formula for every odd lag. It is a mathematical analysis, not a statistical calibration validated on observations. Literature searches and direct comparisons cannot certify universal historical priority; the general reflected/random-walk equivalence is acknowledged. The proof and reproducibility checker are included in the package, with no claim of external independent validation.

Self-review: passed. Independent audit: not yet performed.
