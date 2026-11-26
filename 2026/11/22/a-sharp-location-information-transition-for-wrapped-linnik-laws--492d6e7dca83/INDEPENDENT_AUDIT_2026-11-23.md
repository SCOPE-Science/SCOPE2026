# Independent mathematical audit

## correctness

PASS

The Fourier series uses length measure and integrates to one. The exponential mixture of strictly positive periodized stable transition densities gives a positive minimum: the mixture restricted to t in [1,2] already has a uniform positive lower bound. Write a_k=σ^(−α)k^(−α)+r_k with ∑k|r_k|<∞; the remainder is C¹, even, and has derivative zero at the cusp. The leading decrement is a Riemann sum for ∫₀∞(1−cos t)t^(−α)dt=π/[2Γ(α) sin(π(α−1)/2)], obtained by the Laplace representation of t^(−α) and the beta integral. Dirichlet summation bounds the scaled sine-series tail beyond k=T/|x| by O(T^(−β)), where β=α−1; rescaling the finite part gives the derivative constant −βB on the positive side, with the opposite sign on the negative side. At α=2 the sawtooth sine series gives the same one-sided result. Passing to g=√f divides the cusp constant by 2√f(0). For β<1/2, after x=hu the squared increment is dominated on the rescaled tails by C|u|^(2β−2), with bounded integrand on compact sets; away from the cusp the original integral is O(h²). This gives the exact Jβ and the power 2β+1. At β=1/2, on M|h|<|x|<δ the derivative asymptote and |h/x|≤1/M give relative errors made arbitrarily small by taking δ small and M large after the h limit. The two sides each give A²/4 times h² log(1/|h|); the remaining pieces are O_{M,δ}(h²). Independently, Parseval gives ||f(·−h)−f||²=(2/π)∑a_k²(1−cos kh); at α=3/2 the harmonic sum gives σ^(−3)h² log(1/|h|)/π. The square-root difference divides this leading term by 4f(0) since it is concentrated near the cusp, agreeing with A²/2. For β>1/2 the integrable derivative near the cusp is also square integrable, so g is in periodic H¹ and the translation derivative is −g′ in L², giving I/4. At and below β=1/2 the squared Hellinger discrepancy divided by h² diverges, ruling out DQM. The integrand of truncated information is 4g′²∼4A²β²|x|^(2β−2), which gives both asserted constants by two-sided integration. This is fixed-scale, fixed-shape circular location inference for 1<α≤2 using non-halved Hellinger loss, not uniform asymptotics or a statement about joint estimators. The source checker was inspected, not executed.

## originality

PASS

Narrow pass for the complete normalized wrapped-Linnik location classification and its model-specific constants. The model, real-line cusp ingredient, generic square-root-cusp logarithm, and regular Sobolev/DQM principle are not original. A prior generic critical formula really does apply after checking the wrapped square-root remainder and matching the Hellinger convention. The inspected cases and general frameworks do not supply the full calibrated circular result with both divergent-information constants. This is a bounded assessment with a relevant inaccessible follow-up, not a claim that the underlying cusp mechanism or the number 3/2 by itself is novel.

## value

PASS

For a standard circular family this answers whether location inference falls under the usual finite-information translation model, and quantifies the loss of regularity in the actual wrapped normalization. In particular it separates the pure fractional modulus from the critical logarithm and identifies how the scale and the entire wrapped density peak enter the leading constants. Checking and calibrating those regimes for this model is useful beyond repeating a generic Sobolev criterion; it does not establish an optimal estimator or a joint-parameter inference theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
