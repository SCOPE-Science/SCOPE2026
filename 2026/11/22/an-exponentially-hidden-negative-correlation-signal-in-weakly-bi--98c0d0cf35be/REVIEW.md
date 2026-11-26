# Independent mathematical audit

## correctness

PASS

At kappa=m the column generator has nonzero eigenvalues -gamma(1+m) ± i gamma delta, and the exact stationary left probability is p=(delta^2+delta+m^2+m)/((1+m)^2+delta^2). The stationary covariance is p times the difference between the L-to-L transition probability and p. Its value and derivative at zero are p(1-p) and -gamma(1-delta)p, giving exactly the cosine and sine coefficients in the record with B/A tending to m. The first zero is at phase pi/2, and the subsequent first trough at pi/2+arctan(omega/Gamma) with the same phase shift; each later trough is reduced by exp(-2 pi Gamma/omega). The trough prefactor is of order delta, so only the exponential contributes to delta log M. For fixed reservoir occupancies, maximizing delta^2-(kappa-m)^2 proves precisely frequency optimality, not amplitude or detectability optimality. The checks are analytic; the supplied checker and verification notes were inspected, not executed.

## originality

PASS

The supported distinct claim is the singular visibility law for the frequency-maximizing path of this physical model, including the phase-dependent constant for the first zero and the global negative minimum. The model, equilibrium populations, generic two-mode covariance and possibility of oscillation are prior ingredients. The inspected prior statements do not supply the tuned asymptotic; the finite nonzero limiting phase and the sharp rate for the global extremum require the parameter-dependent amplitude and extremum calculation.

## value

PASS

The path is selected before calculation by the unique maximum oscillation frequency. Even there a mathematical sign-change diagnostic is delayed by order 1/delta and its greatest negative signal is exponentially small, with explicit phase-sensitive exponent. This quantifies the gap between oscillatory spectrum and a usable magnitude without making a measurement-precision or control-optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
