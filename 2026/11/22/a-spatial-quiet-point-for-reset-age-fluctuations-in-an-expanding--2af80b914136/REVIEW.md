# Independent mathematical audit

## correctness

PASS

For the exponential reset age T and U=1/lambda(T), the cutoff is inactive throughout the original support and the local density is 3(U-yU^3)/(4x0). The age law is nondegenerate on U in (0,1), so Var(U^3)>0 and Cov(U,U^3)>0. The strictly convex quadratic gives the claimed unique clipped y and two symmetric minimizers. Integrating the first integral of the expansion ODE yields the stated clock; for k>1 the small-rate moment coefficient is B(k-1,1/2)/(sqrt(2) omega) by dominated convergence. The mu_1 mean is O(r log(1/r)) at fixed omega. The unconstrained ratio tends to 21/16, forcing the edge; the edge second moment minus negligible squared mean gives 107/280 after normalization. For h=omega/r, ODE Taylor expansion gives the coefficients -1/2, 1/3 of U and -3/2, 7/4 of U^3 in h^2Y^2 and h^4Y^4, with an O(h^6) L2 remainder using an exponential-age tail split. For A=Y^2 and B=Y^4 the exact factorial moments give Var(A)=20, Cov(A,B)=672, Var(B)=39744. The quotient correction is delta=Cov(A,B)/(6 Var(A))=28/5. In the uncentered expansion at RESULT.md lines 146–149 the deterministic term should be written exactly as 1-y_*; the printed 2/3-delta h^2 could omit a deterministic O(h^4) term. Retaining 1-y_* (or centering both sides) leaves the random coefficient 3 delta A/2-B/4 with O(h^6) L2 remainder. This nonfatal proof erratum does not affect any variance or other theorem conclusion. The residual variance is the positive factorial-moment Schur complement times 9/(256x0^2), giving 12069/(20x0^2); for fixed y≠1/3 the h^2 fluctuation instead gives the claimed h^4 variance. Verified the four rational coefficients by fresh factorial/beta arithmetic; supplied check.py and requirements.txt were inspected, not executed. No claim of a unique rate transition or of a minimum outside the original support.

## originality

PASS

Pass for minimizing the age-induced local density variance on the original support and the two sharp regimes, especially the optimized rapid-reset coefficient. Not for the expansion law, stationary scale law, the covariance sign front, or the shared leading location 1/sqrt(3).

## value

PASS

Placement of a local monitor within the initial condensate is a meaningful objective in the prescribed age-only model. The exact optimizer, slow-reset preference for the edge, and rapid-reset cancellation with an explicit residual quantify how choice of observation point suppresses that particular fluctuation. A fixed y=1/3 also cancels the leading term; the reported displacement and smaller optimized coefficient identify a genuine further refinement. No shot-noise or detectability claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
