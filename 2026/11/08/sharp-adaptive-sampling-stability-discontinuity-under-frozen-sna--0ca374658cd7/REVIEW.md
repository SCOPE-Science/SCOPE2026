# Independent mathematical audit

## correctness

PASS

With a frozen error and T independent draws, each count has second moment T p_i+T(T-1)p_i^2. Expanding coordinate squares gives the exact conditional change -beta T(2U-beta V), hence the single-batch strict-descent criterion. For uniform probabilities V/U=1+(T-1)/m and U=||x||^2/m; iteration yields the exact factor and excludes nonzero starts at or above the mean-square boundary. For positive ell, the weights and squared errors are ordered together, giving U>=||x||^2/m by the pairwise covariance identity. Since V<=TU, beta T<2 gives the claimed geometric mean-square bound, hence almost-sure convergence by summable Markov bounds. At equality an axis start is a deterministic sign flip. Above it, on the path selecting one initially nonzero coordinate in every draw, probability of another all-i batch is (1+C R^(-ell k))^-T, where R=beta T-1>1. The sum of the negative logarithms is bounded by TC/(1-R^(-ell)), so this infinite event has positive probability and supplies an exponentially growing lower bound on the second moment for every nonzero start. For the stated m=4,T=3,beta=1 example the uniform factor is 5/8, while beta T=3 lies in the adaptive divergent regime.

## originality

PASS

The mechanics of a duplicate-draw penalty, related two-row thresholds, and zero-power singularities have substantial prior coverage. The supported distinction is the joint sharp stability classification for any orthonormal dimension and every finite positive exponent, and the positive-probability exponentially divergent path from every nonzero supercritical start. The exact moment expansion alone is not claimed as new.

## value

PASS

Holding the update schedule fixed isolates a genuine stability discontinuity between exact uniform selection and arbitrarily weak positive residual weighting. The all-start escape result rules out interpreting the instability as an artifact of starting on a single coordinate. The classification gives exact limits in a meaningful frozen model and separates positive-probability divergence and second-moment blowup from typical-trajectory or hardware performance claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
