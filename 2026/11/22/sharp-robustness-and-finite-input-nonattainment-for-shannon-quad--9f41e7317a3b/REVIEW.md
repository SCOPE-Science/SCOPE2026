# Independent mathematical audit

## correctness

PASS

For positive tau, the infinite negative one-sided penalty derivative at zero forces full support; the interior stationarity equation also realizes every positive probability by a finite score. Write H=diag(tau/p_i+kappa), J the inverse of its constrained tangent system. For tangent u, weighted Cauchy gives sum(u_i²/p_i)≥||u||_1², with equality only if |u_i| is proportional to p_i. If k,h count the positive and negative coordinates, sum u_i²≥||u||_1²(1/k+1/h)/4≥n||u||_1²/(4 floor(n/2)ceil(n/2)); equality forces full balanced supports and equal magnitudes within each. Thus the sharp Hessian bound is mu=tau+kappa n/(4 floor(n/2)ceil(n/2)), with equality exactly at the two-block shapes and directions in the finding. Integrating gives the closed-simplex strong-convexity bound (boundary by continuity); small interior segments prove sharpness. For a score direction s and u=Js, u^T H u=u^T s, giving ||J||≤1/mu, and any local equality forces the same Hessian equality. Conversely at an extremizing p take u=±p on the two blocks and s=sign u: H u differs from mu s by a scalar all-ones vector. Hence Js=u/mu, yielding sharpness and every stated local extremizer. On a segment between distinct output probabilities, the weighted Cauchy equality for the fixed nonzero difference would require p along the segment to be the same fixed |u|/||u||_1; the integrated strong-monotonicity inequality is therefore strict. Applied to the stationarity equations and Holder, this gives a strict finite-score secant bound, also strict when scores differ but outputs agree. The separate replay python3 /workspace/branches/independent_checks.py 3 tests direct exact output 1-norms on 102 profiles in dimensions 2–7; it supplements rather than proves this argument.

## originality

PASS

Best-knowledge pass for the exact mixed curvature/norm constant with all local extremizers and finite-score nonattainment, not for simplex-duality construction or balanced partition methods themselves. The prior exact pure-penalty and bounded Gibbs results give important neighboring cases and ingredients, not a displayed theorem for strictly positive Shannon and quadratic coefficients. Full-text limits are explicit.

## value

PASS

A tight sensitivity budget and its obstruction to finite attainment matter for the commonly used cross norm that bounds total probability change from coordinatewise score errors. The finite odd-dimensional correction and the full balanced extremizer shape identify why the standard dimension-only bound can be loose and where its substitute is sharp. The contribution is not general duality, nor a claim of improved generalization or training convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
