# Scientific review

## Correctness — PASS

The Gaussian projected transport formula, the uniform \(O(\varepsilon^3)\) integrand expansion, and the angular second/fourth moments imply both claimed variance coefficients with \(O(\varepsilon^5)\) errors. The strict sign classification is restricted to \(r>0\) away from \(r=4|m|\), so no uncontrolled boundary conclusion is needed. For the swapped-covariance family, quarter-turn invariance is pointwise, and nonconstancy of the cost makes the exact factor-two ratio well-defined. The included dependency-free verifier passed 1,471 tests, including rational leading-term identities and nonlinear Gaussian-cost checks. Finite tests are supporting evidence, not an infinite proof.

## Originality — PASS, with remaining specialist-search risk

The closest source is Rowland et al. (2019, arXiv:1903.03784), whose Section 4.2.2 already establishes that orthogonal directions do not always lower sliced-Wasserstein variance. That broader qualitative sign warning is explicitly treated as prior art. Its displayed negative example uses two-point empirical distributions and the \(1\)-sliced cost; the checked theorem and examples do not determine the present Gaussian squared-cost local ratio \(2r^2/(r^2+16m^2)\), its dividing surface \(r=4|m|\), or the entire exact swapped-covariance extremizer family. Nguyen and Ho (2023, arXiv:2305.00402) instead analyze Gaussian-based control variates; Nguyen, Ren and Ho (2023, arXiv:2301.03749) analyze Markov-dependent directions; Nadjahi et al. (2021, arXiv:2106.15427) analyze high-dimensional deterministic approximation. The relevant full-text sections were inspected. Searches for Gaussian orthogonal-direction variance, near-isotropic trace/anisotropy transitions, and equivalent formulations returned no source covering these quantitative statements. A missed specialized paper or an implicit consequence of an uncatalogued result remains possible.

## Value — PASS

The cost \(\mathrm{SW}_2^2\) between Gaussian distributions is a standard exact projection benchmark for Monte Carlo sliced-transport estimation. The dimension-two local calculation separates covariance-scale mismatch from anisotropy mismatch and supplies a sharp, readily computed diagnostic for when orthogonal projection coupling improves or worsens variance. Its exact worst-case family shows the maximum possible loss occurs already for smooth, nonsingular population Gaussians; the phenomenon is not an artifact of discrete sorting or nonsmooth empirical measures. The precise threshold and its contrasting regimes are the useful mathematical finding, not the textbook factor-two variance bound alone.

## Scientific limits and closest comparisons

Only fixed perturbations about a common isotropic covariance, with non-scalar leading difference, are classified locally. Equality at the sharp leading-order boundary does not resolve finite-perturbation ordering. No independence of external audit or comprehensive historical coverage is asserted. The known 2019 finite-support counterexamples and all Gaussian-projection formulas are acknowledged rather than presented as new.

Self-review: passed. Independent audit: not yet performed.
