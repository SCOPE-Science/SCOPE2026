# Independent mathematical audit

## correctness

PASS

The threshold calculation is correct for the specified natural-scale clock. The killed Green operator gives m=L^beta(1-rho^beta)/C and p=1-(1-rho)/(2(1-rho^beta)). The displayed Dirichlet solution has continuous derivative, vanishes at both exits and at the reset point, and its stopped Ito martingale has quadratic-variation expectation 2 integral G(x0,y)u'(y)^2 dy. Dividing by m gives the stated variance. Independently, the integrals of K_rho|y|^t on the negative and positive halves are (1-rho)/[(t+1)(t+2)] and (1+rho-2rho^(t+2))/[(t+1)(t+2)]. Substituting t=0, beta-1 and 2beta-2 in the squared-bracket expansion simplifies the full formula to V(rho)=V(0)(1-rho^2)/(1-rho^beta), and gives the stated symmetric constant. For variance convergence, stop the centered cycle-sum martingale at the first renewal STRICTLY after T. Its second moment is E[Z^2] times the expected stopping index, asymptotic to T/m. The error from the straddling cycle is bounded by its duration; that duration has uniformly bounded second moment by convolution of the renewal measure (uniformly bounded mass on unit intervals) with the exponentially decreasing second-moment tail of one cycle. This also makes the error negligible for the renewal-reward CLT. For the Poisson comparison, the symmetric free time change has occupation exponent mu=1/beta: the half-line Laplace resolvent slopes scale as q^mu, so matching derivatives at zero gives the double Laplace transform [(s+u)^(mu-1)+s^(mu-1)]/[(s+u)^mu+s^mu] for E exp(-u H_t). Two u derivatives give the centered exponential-cycle second moment (1-mu)/(2r^2). Thus the matched-rate expression, derivative and strict bounds check, including alpha=0.

## originality

FAIL

The distinct November 2 catalogue statements already describe the exact occupation-fraction fluctuation coefficient for this threshold-reset process. The second specifically states that the centered cycle second moment is proportional to 1-rho^2 independent of exponent. The evaluated proposed integral gives exactly that dependence and the Brownian benchmark of the first statement. A different Green representation of the same regenerative coefficient does not establish a distinct result. The symmetric value is its specialization, and the equal-frequency ratio is division by the known Poisson result at r=1/m, with the monotonicity then elementary. This is substantive statement-level and implication evidence, not rejection on the ground that the prior files could not be downloaded.

## value

FAIL

Threshold-triggered occupation fluctuations are a meaningful observable, but the exact coefficient and its location dependence are already the subject of earlier exact results. The symmetric equal-rate comparison adds an instructive interpretation of their ratio to a known Poisson coefficient, not a distinct mathematical result beyond direct substitution and differentiation. No independently valuable surviving claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
