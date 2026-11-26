# Independent mathematical audit

## correctness

PASS

Orthogonal changes of coordinates reduce C to its diagonal singular values without breaking block locality. The inverse covariance gives the reported alpha_i and beta_i terms. Testing the stationary divergence with cutoffs in the discarded block validly gives each standard-Gaussian marginal divergence identity: the cutoff-gradient terms vanish by Gaussian L2. The mixed x_j,y_k derivative is beta_k times the x_j derivative of u_k plus beta_j times the y_k derivative of w_j, with the pure-block distributions dropping out. If both beta_i are positive this separable identity forces all first derivatives constant. Marginal divergence then makes the affine terms homogeneous and skew-symmetric, and the x_1x_2 and y_1y_2 coefficients exclude both rotations when the singular values differ; at equal positive values the cross term requires the two speeds to agree. At rank one, the first component of each field depends only on its first coordinate. A further one-coordinate marginal divergence identity gives f'=xf, whose sole Gaussian-L2 solution is zero. Applying the original marginal identity to the remaining component gives the same exponential dependence on the second coordinate, hence zero by Fubini and L2. At zero correlation, smooth radial cutoffs times Jx give infinitely many independent divergence-free alternatives. The drift -Z with noise covariance 2Σ_C realizes the invariant Gaussian; adding the coordinated skew rotation preserves stationarity and linear stability. At C=0 the bounded smooth rotational perturbations give nonexplosive dissipative diffusions with that invariant law and uniqueness by ellipticity. Identifiability in the zero-kernel regimes correctly holds only within the given class and with diffusion fixed. VERIFICATION.md and verification/check.py were inspected, not executed; exact polynomial nullity tests do not exclude non-polynomial fields.

## originality

PASS

Pass for the pointwise nonlinear canonical-correlation classification with two reciprocal feedback pairs. The general linear Lyapunov rank test already reduces every linear subcase to a finite calculation, and known examples explain how correlated noise can recover linear identifiability. Neither settles the absence of all nonlinear null currents, in particular at rank one, or the fact that the full resonant kernel is only a coordinated rotation. Rotational blindness itself is not new.

## value

PASS

The model isolates a concrete obstacle in graph-local inverse problems: reciprocal drift pairs can hide stationary currents, yet known cross-correlated noise and anisotropic canonical correlations can remove every such current, including nonlinear ones. The exact rank-one and resonance boundaries distinguish mere generic linear identifiability from a pointwise nonlinear result. The proof also gives actual stable stationary diffusions on the nonidentifiable strata rather than just formal Fokker–Planck solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
