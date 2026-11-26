# Independent mathematical audit

## correctness

PASS

In normalized time, integrating the linear equations for X as a function of Y gives X_L=e^{-Y}(F(Y)-kappa) and X_R=(1/2)e^{-2Y}(F(Y)^2-lambda), with F(y)=(y-1)e^y. Because F'=y e^y and F(0)=-1, there are exactly two crossing roots p<0<q<1 for -1<kappa<0. Between them F<kappa<0, so the kappa and lambda=kappa^2 arcs are in their correct half-planes. At p both horizontal components are positive and at q both are negative; other roots above 1 are not transverse crossings of the periodic component. A transverse cycle must have crossings of each of these two types, since Y is strictly monotone in each zone; each flight takes q-p, and neither can close earlier. Thus the least normalized period is 2(q-p). Branch inversion yields the stated W difference and p'<0<q' gives strict growth. At the inner end the signed square root of 2(F(y)+1) is analytic with derivative 1 at zero, so its inverse at oppositely signed arguments gives q-p=2 sqrt(2(kappa+1))+O((kappa+1)^{3/2}). At the outer end set u=-W_{-1}(kappa/e); then u-log u=L, u tends to infinity, and u/L tends to 1, so u=L+log L+o(1), while W_0 tends to zero. This gives the sharp stated divergence at an unbounded boundary, not a finite saddle. The original tau-time scaling is division by delta. The assessment is analytic; no independent numerical spot checks were necessary or run.

## originality

FAIL

The Lambert-W representation was not explicitly found in the inspected thesis and is not alleged to have been stated there. But the prior source proves the unbounded annulus for the identical normalized system and explicitly integrates both half-plane orbit equations in the relevant regime. Together with the displayed constant vertical velocities, those already determine the least time by direct subtraction of the two crossing heights. The proposed period law, monotonicity, and outer term are the immediate branch inversion and elementary endpoint estimates of that published orbit/velocity description. The reason for failure is this concrete implication, not missing full text for the later piecewise-linear paper or a negative index search.

## value

FAIL

The period is a natural invariant and the closed form is useful exposition, but for this very family the known orbit equations and already specified constant vertical speeds reduce the entire timing question to subtracting the two known crossing ordinates. Monotonicity and both boundary laws add only the standard branch inversion and elementary estimates of the same scalar level equation. No further dynamical invariant or independently nonroutine remainder is established; a reformulation or certificate would not repair this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
