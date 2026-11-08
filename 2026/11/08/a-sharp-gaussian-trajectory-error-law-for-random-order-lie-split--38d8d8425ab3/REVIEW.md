# Scientific review

## Correctness (PASS)

For any fixed real matrices \(A,B\), and independent fair choices of the order of the two exact Lie factors, Taylor expansion gives the centered local perturbation \(\varepsilon h^2[A,B]/2\) and a uniform \(O(h^3)\) remainder. Expanding the entire finite noncommutative product shows that every term with at least two local perturbations contributes a uniform \(O(h^2)\) remainder; all single-step higher-order terms also contribute \(O(h^2)\). The leading centered array has variance of order \(h^3\), a Gaussian limit by the triangular-array central limit theorem, and an exact leading Frobenius risk integral by orthogonality of its independent signs. The commutator criterion follows because both exponential propagators are invertible. The complete proof does not extrapolate finite experiments to infinite-dimensional or infinite-time conclusions.

The standalone `check.py` verifies the local expansion symbolically on the oscillator and computes exact (not Monte Carlo) finite-step second moments. All checks passed, and the scaled oscillator risk approaches the analytically derived constant \(1/2\).

## Originality (PASS, with source risk)

Berger (1984, §§5–6) studies general random matrix product CLTs with leading \(n^{-1/2}\) stochastic terms; direct substitution of the present \(n^{-2}\) per-step random commutator into those hypotheses gives a degenerate zero-noise limit, not the rescaled \(n^{-3/2}\) Gaussian trajectory defect. An augmented or second-order reduction remains plausible and is a publication-precedence risk. The forward/reverse product-formula randomization and its mean-level order improvement are **not** original: Zhang (arXiv:0910.4145, §2) and Childs–Ostrander–Su (arXiv:1805.08385, product-formula comparison and randomization theorems) precede this statement. The distinct proposed result is the full matrix-valued **trajectory-level Gaussian limit**, its exact nonzero propagated-commutator covariance and sharp expected squared Frobenius risk coefficient, for all fixed real matrix pairs. The earlier statements concerning the *average quantum channel* neither imply the distribution of a single independently randomized trajectory nor give its covariance coefficient. Jin–Li (arXiv:2109.07987) randomize Hamiltonian-term selection rather than per-step forward/reverse order; Veldman–Zuazua (arXiv:2109.13798) study random splitting in LQ control with different randomization and rate objectives. Chen–Huang–Kueng–Tropp (arXiv:2008.11751) derive single-trajectory concentration bounds for qDRIFT, not this specific Gaussian limit or exact constant. No exactly covering result was identified in the inspected material; an equivalent special case in general stochastic-product or probabilistic numerical analysis theory remains possible.

## Value (PASS)

Averaged-propagator order can be misleading for a numerical solver operated once per sample path. The exact coefficient shows that randomization produces root-mean-square \(h^{3/2}\) error even as the mean propagator attains \(O(h^2)\) bias. The propagating commutator integral is a computable matrix-specific diagnostic; zero versus positive risk is characterized sharply by commutation, and the canonical harmonic-oscillator splitting gives an explicit nonzero benchmark. This separates weak/ensemble error from realizable pathwise accuracy without relying on a prescribed arbitrary parameter slice.

## Closest literature and limitations

- M. A. Berger, *Central limit theorem for products of random matrices*, Trans. AMS 285 (1984), 777–803, §§5–6: random near-identity matrix products and stochastic Lie–Trotter CLTs, but for a different leading noise scaling.
- C. Zhang, *Randomized Algorithms and Lower Bounds for Quantum Simulation*, arXiv:0910.4145, §2: random-order Hamiltonian formulas and mixed-state error estimates.
- A. M. Childs, A. Ostrander and Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385, §§2–3: forward/reverse-order randomization and averaged quantum-channel convergence.
- S. Jin and X. Li, *A Partially Random Trotter Algorithm for Quantum Hamiltonian Simulations*, arXiv:2109.07987, §§2–3: random terms, bias and variance.
- D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798, §§2–3: different random time-splitting scheme.
- C.-F. Chen, H.-Y. Huang, R. Kueng and J. A. Tropp, *Concentration for random product formulas*, arXiv:2008.11751: single-realization martingale concentration (abstract and article overview inspected, not its complete proof).

Scope: arbitrary fixed **finite-dimensional real** matrix generators, one pair of factors, independent fair signs, fixed terminal time. The finding makes no claim of being the first randomization algorithm, no claim of general nonlinear or unbounded-operator validity, and no claim of complete publication precedence.

Self-review: passed. Independent audit: not yet performed.
