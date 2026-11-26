# Independent mathematical audit

## correctness

PASS

Gaussian regression gives E[Q|Y]=1/12+(K/v^2)(Y^2-v) with K the integrated squared cross-covariance, so the unconditional risk is Var(Q)-2(K/v)^2. Integrating over the triangular time domain gives Var(Q)=(4/8)(1/20-1/36+1/252)=11/840. Both piecewise covariances follow by integrating min(t,u), and their squares give the two polynomial scores. At the sole degenerate reading (site zero, zero noise), the conditional mean gives no risk reduction. For positive sites, derivatives have the signs of eta M_B-N_B and eta M_X-N_X. M_B>0 below one; the derivative of N_B/M_B is strictly positive from the unique cubic zero to one, by the three negative factors and leading minus sign. M_X>=273 and N_X/M_X grows strictly from zero at r to 8/273 at one: the first factored polynomial is negative, and the second is concave and positive at 4/5 and one. The signs also exclude maximizers below the respective zero thresholds. Thus the B maximizer is always unique and interior, and the X maximizer reaches one uniquely at eta=8/273. The completed-square quartic certificate bounds every B score strictly below R_X(1,8/273), ruling out a crossing at smaller eta. Above that noise the ratio of optimized scores strictly increases by evaluating the B maximizer at the smaller noise (it is always >1/3); it is continuous by compact maximization, and tends to 21/11 by uniform convergence of the rescaled score on the site interval. Eliminating eta via the B stationarity equation yields the stated quintic; its discarded factors do not vanish in the eligible interval. The exact endpoint substitutions at 57779/100000 and 57780/100000 have opposite signs. Independent high-precision bisection gives z=0.5777921928217725563627524 and eta=0.1124913180550581605740688. Uniqueness concerns the global risk, not the numerical grid.

## originality

PASS

The neighboring results overlap in either competing modalities or the quadratic target, but not both in this observation model. The materially distinct claim is the exact globally optimizing quadratic-energy switch, including the two site classifications; Gaussian moment formulas and the general monotone-envelope method are not claimed new. Same-day catalog dates do not independently establish priority.

## value

PASS

Quadratic-energy estimation supplies a specific non-linear design criterion for choosing between experimentally different readings of position and derivative. Determining exactly when preference reverses, and separating that switch from the earlier slide of the optimal value site to the endpoint, are useful structural consequences, not grid-level comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
