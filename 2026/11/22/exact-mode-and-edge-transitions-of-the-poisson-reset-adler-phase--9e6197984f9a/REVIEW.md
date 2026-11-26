# Independent mathematical audit

## correctness

PASS

Subtracting the two ODEs gives v=Delta-K sin(phi); the assumptions specify one shared rate-r Poisson clock independent of the dynamics. The exponential-age pushforward constructs the stationary law, and common-clock coupling gives uniqueness with total-variation error bounded by exp(-rt). Phase preimages are a singleton on the locked and critical open arcs, and a countable sequence A(phi)+jT in rotation, so there are no atoms, including at reset or at a locking equilibrium. The inverse-flow Jacobian and geometric sum give the normalized densities. Shifting the full-period integral to the cosine form and using the tangent half-angle substitution gives T=2pi/sqrt(Delta^2-K^2); the equal drift at both sides of reset gives the e^(rT) density ratio. On each open occupied arc the logarithmic derivative is (K cos(phi)-r)/v. It determines the two rotating interior extrema iff 0<r<K, and strict decrease for r>=K. In the locked regime K cos(phi) decreases from K to gamma. For r<=gamma the density is strictly increasing and has its one-sided supremum at the locking edge; for gamma<r<K it peaks in the interior; for r>=K it decreases from reset. Thus the Finding's reset-point/interior contrast concerns the switch at K, not the edge-dominated r<=gamma regimes explicitly specified below it. At equality r=K the derivative vanishes at reset, not on the open arc. The simple-root expansion v=gamma*delta+O(delta^2) makes A+log(delta)/gamma converge to a finite real B and yields the positive prefactor (r/gamma)exp(-rB), with finite nonzero density limit at r=gamma. At Delta=K, differentiating tan(phi)+sec(phi) gives (1-sin(phi))^(-1); its edge value cot(delta/2)=2/delta+O(delta) and v~K*delta^2/2 give the prefactor 2r exp(r/K)/K and essential factor exp(-2r/(K*delta)). The density decays faster than every algebraic power. All endpoint density language is about one-sided limits, not assigning mass at points. Replay: RESULT.md lines 9–63; verification notes and verify.py inspected, uploaded diagnostic not executed. The analytic proof, not finite quadrature, covers both equality boundaries.

## originality

PASS

Credit is limited to the full stationary phase-density morphology for the deterministic, positively detuned Adler drift with simultaneous resetting to a common phase. Neither the drift nor the generic reset-age pushforward nor the generic simple-equilibrium edge exponent is treated as new. The actual available statements of the closest reset Kuramoto and deterministic-flow sources do not give the same density diagram, for which wrapped ages, two distinct thresholds, and the critical edge must be analyzed together.

## value

PASS

In this minimal synchronization model the reset-rate transition in the preferred phase is not the same as loss of the locking-edge density, nor as the dynamical locked-to-rotating transition. The two exact thresholds distinguish those effects, the formula resolves both equality regimes and the winding-sector discontinuity, and the saddle-node prefactor specifies where the usual algebraic edge law fails. The complete regime diagram is useful for interpreting or checking reset phase histograms even without a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
