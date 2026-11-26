# Independent mathematical audit

## correctness

PASS

The 2026 primary article's eqs. (3.7), (3.12) and Proposition 4.1 give the two scalar spectral thresholds and the strict local interpretation. In the second pencil the variable is v=gI, whose Neumann condition is exactly the original no-flux condition; multiplying its divided equation by g>0 gives the displayed nondivergence pencil. The undivided Fickian and divided Fokker–Planck weak forms on H¹ have positive masses and uniformly coercive elliptic forms near epsilon=0. Their coefficients are C³ in epsilon in L-infinity, which suffices without assuming an extra spatial derivative of g. At epsilon=0 their ground state is constant and simple by connectedness and the Neumann gap. For the mean-one normalization the linearization of the eigenpair equation is invertible: test by the constant to solve the scalar eigenvalue variation, invert the mean-zero Neumann Laplacian on the remaining dual data, and fix the mean by normalization. This supplies C³ branches by the implicit function theorem; the variational gap locates them at the principal eigenvalues. Differentiating gives zero first-order eigenvalue shift and common mean-zero first eigenfunction coefficient u with −g0 Δu=q. Independently, test each weak pencil with 1: exactly ⟨(nu_F beta−gamma)u_F⟩=0 and ⟨(nu_P beta−gamma)v/g⟩=0. Since g0/g=1−(g1/g0)r epsilon+O(epsilon²), the second identity has precisely the extra −(g1/g0)⟨rq⟩ epsilon² in the integrated residual. Both share the terms nu0⟨d⟩−⟨h⟩ and ⟨qu⟩. Subtracting gives beta0(nu2_P−nu2_F)=(g1/g0)⟨rq⟩; taking reciprocals gives the sign and factor in the record. The second-order difference contains no Neumann resolvent or spectrum, although the spatial average is taken over the given profiles/domain. For the witnesses cos x has Neumann eigenvalue 1 and squared average 1/2, giving ⟨qu⟩=(B−1)² and ⟨rq⟩=(B−1)/2. The two displayed pairs yield opposite (−1/8,+1/8) and (+1/8,−1/8) quadratic shifts as claimed, with positive coefficients for sufficiently small amplitudes. Independent finite-volume replay /workspace/reviews/evidence/5-neumann-check.py used 180 and 360 no-flux cells, symmetric tridiagonal generalized-eigenvalue reduction, and epsilon 0.08, 0.025 and 0.008. Both sign pairs and approach to the exact coefficients passed; these finite checks corroborate the example, not the continuum theorem. No sign when the covariance coefficient vanishes, global ordering or endemic-state conclusion is certified.

## originality

PASS

The closest independently read primary formulas are exactly the two spectral pencils, so neither the variational characterization, smooth eigenvalue dependence nor use of generalized eigenfunction perturbation is new. The contribution is the shared-coefficient weak-heterogeneity comparison at finite diffusivity: the resolvent-dependent terms cancel, leaving a local covariance with both signs and allowing opposite strict threshold verdicts at the same coefficients. The 2026 primary source expressly leaves the heterogeneous comparison difficult and states equality at constant recovery; other near sources were inspected only to the extent specified below.

## value

PASS

The primary source explicitly identifies a comparison it cannot make by the constant-recovery argument. The local covariance criterion gives a useful analytic answer without solving two distinct elliptic eigenvalue problems to second order, and the exact opposite witnesses rule out a universal ordering even near homogeneity. This concerns a deterministic onset threshold; it does not prescribe movement, predict final outbreak size, or imply a real-world intervention result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
