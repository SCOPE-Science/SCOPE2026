# Mathematical review

## Correctness: PASS

The claim treats a strictly positive, uniformly convergent Fourier density with shape \(1<\alpha\le2\) and fixed positive scale. Subtracting the leading \(k^{-\alpha}\) coefficients leaves a cosine series with absolutely summable first derivative. The leading density decrement and derivative are reconstructed by an integrable Riemann-sum kernel and Dirichlet sine-series asymptotics; the exact cusp constants agree with the gamma reflection formula. The square-root cusp then implies the subcritical Hellinger constant by a dominated rescaling, the critical coefficient by a two-sided logarithmic derivative integral, and the regular coefficient by \(L^2\)-translation differentiability. Fisher information is four times the square-root derivative energy; this fixes the normalization and proves the sharp boundary. The accompanying checker passed 106 finite numerical assertions, but is not used as the proof of an infinite theorem.

## Originality: PASS with historical-priority qualification

The original 2023 wrapped Linnik work supplies the Fourier model and analyzes shape estimation, not the circular location Hellinger modulus. The subsequent full-text version establishes its Fourier representation and moment-estimator asymptotics but not this three-regime location information law. The 2024 review records the same model under the equivalent scale coefficient \(\sigma_{\mathrm{review}}=\sigma^\alpha\), without providing Fisher/location-Hellinger results. Lim and Teo's 2009 unwrapped density expansions are a useful local ingredient but not the full circular shift theorem; Shemyakin's generic framework states the normalized Hellinger/Fisher relationship without this model's threshold. Targeted searches of published mathematical results and public papers did not identify a statement that implies the exact three constants and cutoff without additional work. Priorities under other names remain uncertain; this is a scientific comparison rather than a claim of exhaustive uniqueness.

## Value: PASS

The model was introduced for non-Gaussian circular data, with an explicit location parameter. Smooth asymptotic inference often presumes finite location information, but here a single natural shape parameter changes the experiment from non-quadratic to logarithmically critical to quadratic. The complete fixed-model classification, constants and location score-integrability boundary identify exactly when standard differentiability-in-quadratic-mean arguments can be used. The result does not assert actual optimal rates or practical test power.

## Closest literature, residual risks and limits

The key sources are SenGupta–Roy (2023, two related papers), Lim–Teo (2009), Shemyakin (2023) and Bell–Nadarajah (2024). Classical power-cusp Fourier asymptotics, Sobolev translations and Hellinger regularity are prior tools. A possibly dominating general theorem about nonregular *periodic* location families, or an uncatalogued derivation for an equivalent fractional Bessel-potential kernel, remains a priority risk. Only the one-dimensional fixed-shape/fixed-scale circular location subexperiment is proved.

Self-review: passed. Independent audit: not yet performed.
