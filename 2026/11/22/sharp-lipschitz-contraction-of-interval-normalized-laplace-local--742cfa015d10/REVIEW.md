# Self-review

## Correctness — PASS

For every finite positive rate and nondegenerate interval the normalized density is smooth in its center in the weak derivative sense and strictly positive. The center-indexed densities have a monotone likelihood ratio; therefore their exact \(W_1\) distance equals the difference of means. The score calculation gives \(m'(x)=2\lambda AB(H(u)+H(v))\). Both factors are maximized at the interval midpoint: \(AB\le1/4\), while strict concavity of the truncated-exponential distance mean \(H\) supplies \(H(u)+H(v)\le2H((b-a)/2)\). The identity function witnesses sharpness. Reversibility follows from symmetry, and the mixing bound follows by iterated contraction and stationary averaging. Supplementary independent direct quadrature and finite-difference tests passed 2,532 assertions. No claim of optimality for the multi-step upper bound is made.

## Originality — PASS, with residual risk

The 2019 *Wasserstein Transform* develops local probability distributions and analyzes data-distribution perturbations; its studied results do not state the present exact center-indexed Laplace interval contraction coefficient. The 2020 Tosatto–Akrour–Peters analysis bounds Nadaraya–Watson bias, particularly with Gaussian kernels, rather than giving the global Lipschitz seminorm. General Wasserstein contractivity theory supplies methods but not this explicitly optimized sharp formula for this kernel. Literature searches also covered normalized exponential distance, truncated Laplace location, Dobrushin coefficients and Wasserstein Markov averaging. Earlier equivalent exact formulas in less indexed location-family literature remain possible.

## Mathematical value — PASS

A continuous-domain Markov smoothing kernel that looks nearly translation-invariant has a strictly contracting, exactly computable Lipschitz factor solely because of boundary normalization. The explicit transition from small-rate strong smoothing to large-rate almost-identity, the unique midpoint extremizer and stationary mixing rate give sharp, interpretable robustness and convergence benchmarks for finite-domain exponential-kernel localization. This is a motivated exact operator norm, not a parameter restatement of generic nonexpansivity.

## Closest literature and limitations

See the three sources in RESULT.md; in particular the normalized local-measure framework is prior work and stochastic order/Wasserstein duality are classical. The proved formula requires a uniform base measure on an interval; no corresponding sharp coefficient is claimed for arbitrary designs, higher dimensions or kernel families. Historical originality cannot be independently certified from a search, and independent mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
