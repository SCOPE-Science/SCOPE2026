# Independent mathematical audit

## correctness

PASS

A coordinate multiplier is c=1-dah with probability 1/d, otherwise 1; the full-dimensional independent Gaussian innovation variance is v=(1-c^2)/(da). The shared selection couples chains with strict mean-square contraction u=1-(1-c^2)/d and every coordinate is selected infinitely often; the backward stationary innovation series converges in L4 since E[A_i^4]<1. Independently derived E[X_i^2]=1/a, fourth moment via M4=w M4+6uv/a+3v^2, and E[X_i^2 X_j^2] via exclusive coordinate selection; algebra gives the stated kurtosis and negative squared-pair covariance. At c=0 the time since last selection is geometric with success 1/d; conditional Gaussian variance is (k+1)/(da) and nonnegative geometric MGF series converges iff |t|<sqrt(2da log(d/(d-1))), with divergence at endpoints. Exact symbolic recurrence cross-checks independently corroborate the algebra.

## originality

PASS

Ding and Li introduced the full-noise coordinate-gradient algorithm and bounded its Wasserstein error, but did not establish this covariance-calibrated invariant fourth-order and geometric-age MGF classification. Prior exact covariance calculations are acknowledged, not claimed as new. Coordinate-only-noise RC-LMC and deterministic-multiplier SGLD toy recursions have different updates; general concentration theorems require a bounded conditional sub-Gaussian gradient proxy, which fails here. Potential unindexed specialist random-affine prior remains a risk.

## value

PASS

Exact covariance cannot certify a Gaussian stationary sampler: these formulas detect strict non-Gaussian marginals, negative dependence of coordinate energies and non-sub-Gaussian stationary tails at the natural reset step. The exact fourth-order/tail diagnostics are natural experimentally useful invariants of a published gradient-subsampling method and not a recomputation of its second moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
