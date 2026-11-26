# Independent mathematical audit

## correctness

PASS

Use an orthonormal pair beginning with b for Galerkin and one beginning with Ab/h for minimal residual. In either case the projected independent Gaussian in the direction of the first sketched vector has law N(0,1) independent of the chi length of that vector. Thus the laws stated are marginal, not a coupling. Z/R has density Cₘ(1+z²)⁻⁽ᵐ⁺¹⁾⁄², giving the minimal-residual index m and constant 2Cₘ(c/h²)ᵐ/m. The Galerkin denominator has positive continuous density at zero; integrating it over (−1/t,1/t) gives the stated index 1 and constant 2f(0). Subtracting a fixed exact solution changes the Euclidean error from |θ| by at most a constant, and norm equivalence preserves thresholds in the energy norm. At m=1 both cutoffs equal 1; m=2 is still outside the minimal-residual mean-square regime. The sign probability follows from √m Z/R ∼ tₘ and tends to zero since R grows in probability. Expanding the energy error as bᵀA⁻¹b−2θ+aθ² and using E[R⁻²]=1/(m−2) proves the squared-error formula (including the stated rational example). The c=0 excluded case is genuinely deterministic.

## originality

FAIL

The material conclusions are already covered, not merely suspected to overlap: an earlier Resultary record gives the same one-step marginal Student and reciprocal-Student laws, the sharp moment contrast, and the Galerkin pole coefficient. Bounded shift transfers its coefficient-tail constant to the indicated Euclidean error; the minimal-residual constant, direction probability and energy mean-square expression follow directly from the prior marginal laws. The prior numerical-linear-algebra papers alone would not establish this overlap, but the local record does.

## value

FAIL

The unconditioned moment contrast is a useful solver diagnostic in its own right, but that diagnostic and the sharp benchmark are already available. The remaining numerical-linear-algebra details are direct consequences of the same prior scalar laws: integrating the Student tail, reading the denominator sign, or taking the expectation of a quadratic. The record does not establish a further phenomenon or an independently useful unknown invariant beyond this known benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
