# Independent mathematical audit

## correctness

PASS

The clocks run on one continuing path without extra reset or killing at discovery; the reset site lies strictly between -a and b, and a,b,D,r are positive. The ODE with opposite Dirichlet boundary values gives the two discounted exit-side probabilities. A failed cycle has discounted mass r(1-f_+-f_-)/(r+s); summing the renewal series gives the frozen G_±. The analogous one-sided renewal starting at the opposite level gives H_± with initial distance a+b and subsequent distance a or b. The strong Markov property at the first hit factors the remaining-clock transform conditional on the exit side, yielding the claimed joint transform. The relevant derivatives exist: failed cycle transforms extend locally about zero, with total failure mass strictly below one, so the one-sided clocks have exponential moments near zero. Differentiating at zero gives the two marginal means and the mixed moment. Independent exact symbolic reduction (branches/12ba63cd-d031-413b-8a3d-ab487b783415/independent_check.py) reproduces r² Cov = -(A+B)(x²-1)(y²-1)/(2(x+y)(xy-1)) at x=e^A,y=e^B; the expression is negative and equals the hyperbolic formula. The subtraction cancels the ab(r/D) numerator term and leaves ab(a+b)(r/D)^{3/2}/2, with covariance and mean product still of order r^{-1}. The marginal variance from the one-sided transform has leading small-r numerator A or B, giving the stated Pearson asymptote; at large r the variance factors grow exponentially faster than their normalized covariance numerator. The finite lattice approximations in the frozen script were inspected, not executed; they are not the continuum proof.

## originality

PASS

Best of current knowledge for the continuing-clock bivariate transform, exact sign and weak-reset mixed-moment asymptotic. The inspected closest work concerns first exit, cover/completion means, or different joint observables. Standard killed exit and resetting renewal formulas are inputs, not new results.

## value

PASS

The persistent opposite-target clock pair is a natural two-target search observable. A shared reset clock and single particle do not make the sign immediate. The exact covariance settles it for all positive distances and rates, and the weak-reset cancellation makes the mixed moment diverge on a genuinely different scale from the product of means. The full joint transform also supports other two-target observables without replacing this process by a killed or forcibly restarted protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
