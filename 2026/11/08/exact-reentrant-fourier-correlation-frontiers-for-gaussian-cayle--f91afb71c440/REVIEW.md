# Review of the Gaussian Cayley Fourier-correlation result

## Correctness — PASS

The theorem concerns only the stated Gaussian Cayley integrator on planar rotational Brownian motion. The matrix identity yields a rotation by \(2\arctan(\sqrt hZ/2)\); the Gaussian chi-square transform yields its precise Laplace–Chebyshev representation. The exponentials' Chebyshev zero theorem is proved by a Rolle-induction argument and, with an explicitly constructed exponential polynomial, bounds the number of positive roots by the number of kernel sign changes. Formulae for the first two modes follow from Gaussian integration by parts. The strict negative certificate at \(h=4\), endpoint signs, and zero bounds prove the asserted root counts without numerical extrapolation. The 151 deterministic checks agree with those identities, but do not substitute for analytic proof. Decimal root values are approximations rather than certified enclosures.

## Originality — PASS, with residual uncertainty

The arXiv full text of Jauch–Hoff–Dunson establishes Cayley parametrizations and Gaussian approximations for random orthogonal matrices, not the fixed-Gaussian-increment Brownian transition Fourier eigenvalue count. The original Muniz–Ehrhardt–Günther preprint, Sections 2–4 and its stated Cayley alternative, establishes the geometric method's motivation and not the present spectral thresholds. Armstrong–King studies more general invariant-manifold numerical SDE schemes and convergence. Current subject-specific literature queries and the mathematical-record search did not identify a result that implies the two-root second-harmonic classification or the all-mode zero bound for this distribution. This is not a proof of unique publication priority. Older specialized random-rotation results and inaccessible full text remain residual risks; the established Cayley map, Fourier diagonalization, and exponential Chebyshev property are not claimed new.

## Value — PASS

A basic requirement of geometric stochastic integrators is exact preservation of the state manifold, while numerical transition spectra determine long-time relaxation and lag correlations. Here even a second harmonic switches from positive to negative and back as the step increases, although the true heat semigroup has positive decreasing multipliers and the numerical scheme preserves the correct invariant distribution. The two exact crossover roots and analytic nonnumerical witness are natural, quantitative benchmarks for assessing the limits of invariant-preserving integrators. The extension bounds the number of modewise sign reversals. This exceeds a generic numerical negative test or algebraic reformulation.

## Closest literature and limitations

Jauch–Hoff–Dunson: arXiv:1810.02881 (initial public date 2018-10-05), Cayley random orthogonal matrix distributions and Gaussian approximations. Muniz–Ehrhardt–Günther: BUW-IMACM 20/05 (March 2020), stochastic Lie-group methods and Cayley mapping suggestion. Armstrong–King: DOI 10.1098/rspa.2021.0785, geometric schemes for manifold SDEs. The theorem does not extend to arbitrary diffusion matrices, non-Gaussian noise, or general matrix groups. Mode counts beyond two are bounded, not classified.

Self-review: passed. Independent audit: not yet performed.
