# Independent mathematical audit

## correctness

PASS

All transition rates follow from the specified independent, fixed-marginal catastrophe clocks. I independently reconstructed the four-state generator, the 0/1/2 lumped generator, and the stationarity equations, then symbolically proved p0+p1+p2=1 and the exact p0, p2 and mean derivatives. Independent rational four-state stationary-system calculation for lambda=2, mu=3, rescue c=5, kappa=7, theta=2/3 gave (p00,p10,p01,p11)=(279/413,46/413,46/413,6/59), exactly matching the submitted formulas, without running the package verifier. The denominator is affine and strictly positive at theta=0 and theta=1; h=mu+kappa>kappa ensures positivity at the latter. Consequently p0 prime>0, M prime<0 and sign(B prime)=sign(mu+kappa+lambda-c), all for strictly positive parameters; equality/unique optima and theta endpoints follow. Finite example is corroboration only; symbolic identities are the universal proof. The source package tree and all seven actual file blobs were inspected at its frozen commit.

## originality

FAIL

The November 2, 2026 already published Resultary theorem is exactly the same binary symmetric two-patch Poisson CTMC at fixed marginal catastrophe hazard. Its parameters (c,d,e,k,rho) map to the submitted (lambda,c,mu,kappa,theta). After substitution the full three-state generator, positive denominator, p0,p1,p2 and both published M and joint-occupancy derivatives agree identically. It already gives the same strict monotonic mean occupancy and sharp d=c+e+k rescue threshold, neutral hyperplane, and all theta endpoints. The submitted strictly decreasing regional-occurrence probability is a one-derivative corollary of the previously published p0 formula. An extra numerical/rational demonstration and equivalent parameter labels do not salvage originality. The earlier RESULT.md and its November 2 publication metadata were inspected in full, not just a similarity snippet.

## value

FAIL

The distinction between regional and joint occupancy under matched marginal catastrophes is naturally motivated, but the exact same all-parameter synchrony/rescue threshold and mean-occupancy phenomenon were published November 2, 2026. The only apparent addition, strict regional R decrease, is a one-line derivative of the earlier full p0 stationarity formula, not an independently useful exact unknown invariant, motivated new boundary, or nonroutine structural lemma. Reproducing the published algebra with a separate finite-state checker and renamed parameters has no surviving scientific contribution after subtracting the direct predecessor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
