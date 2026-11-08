# Scientific review: chirality recovery from three-time count cumulants

## Correctness — PASS

The object is a homogeneous marked Poisson gas of independent chiral active Brownian particles with uniform initial headings. All count cumulant formulas follow directly by differentiating the marked Poisson exponential formula; in particular the third connected correlation is a single-particle three-position probability measure, rather than a Gaussian/Wick approximation. Reflecting the plane maps positive to negative angular drift, while the one-step displacement law is rotationally invariant and therefore reflection invariant. Thus all two-time count covariances are equal at opposite drifts.

The three-time signed area is exactly a spatially weighted cumulant measure, and orientation increments give the factor \(e^{-D_r u}\sin(\omega u)\). The factorized double integral yields the displayed closed form, with leading coefficient \(v^2\omega h^3\). The ordinary displacement variance derives from the even orientation correlation and gives all four stated right derivatives. Since the variance's second derivative is strictly positive under \(v>0\), the recovery formulas are well-defined. Both zero angular drift and zero angular diffusivity are handled by continuous limits. Independent quadrature and high-precision consistency checks passed; finite checks are not relied on as a continuum proof.

**Risk/limits:** exact spatially resolved ensemble cumulants are assumed. Finite observations, pixelation and interactions are outside the theorem.

## Originality — PASS, with qualified publication-priority risk

The 2026 Countoscope source develops two-time box counts and their intermediate scattering functions for ordinary active-particle models; accessible sections I and II explicitly give the pair-count construction. The 2024 chiral active Brownian work already gives the standard displacement moments and a handedness-sensitive position–orientation cross-correlation; these inputs are cited, not attributed here as new. The 2017 circle-swimmer paper's exact intermediate scattering function is stronger for one-lag positional distributions but does not itself supply three-time count cumulants. The 2008 independent Brownian gas paper treats n-time density correlations and already covers the general Poisson-correlation principle in an achiral Brownian setting. The assessed claim is specifically the count-only two-versus-three-time information separation and the exact handedness recovery formula in a uniformly initialized chiral active gas, not merely the cumulant algebra or the second moment.

Actual scholarly searches considered countoscope chirality, third-order multipoint statistics, signed displacement areas, exact circle-swimmer scattering, and related published claims. No directly covering statement was identified. The current Countoscope preprint's full later sections were not obtainable in the available material, and the accessible accepted-paper page was abstract-only; a stronger uninspected source cannot be excluded. The result therefore warrants independent priority verification before publication.

## Value — PASS

Number counting without particle tracking is the explicit motivation of the recent Countoscope literature. In an isotropic chiral gas, even using arbitrarily placed pairs of windows cannot reveal the handedness of individual swimmers; the theorem proves this limitation for all two-time count covariances, then provides a mathematically exact, physically natural three-time observable that does reveal handedness. Its short-lag coefficient identifies the signed angular velocity, and the combination with the pair-count variance uniquely determines both diffusivities and swimming speed. This is a complete observability distinction, not a normalization exercise or isolated numerical invariant. A finite-field estimator and practical noise analysis are not claimed.

Self-review: passed. Independent audit: not yet performed.
