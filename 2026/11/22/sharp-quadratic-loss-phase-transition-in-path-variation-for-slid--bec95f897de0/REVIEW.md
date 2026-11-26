# Independent mathematical audit

## correctness

PASS

The Euler equation for p>1 has a unique root and gives coordinate monotonicity and translation equivariance. Together they imply max-norm Lipschitz continuity. For triples, if the mean equals one datum, the other two residuals are opposite, so the exceptional residual-zero configurations are contained in the finite union of midpoint hyperplanes. Away from these, implicit differentiation gives weights proportional to absolute residuals to power p-2, summing to one. Generic translates of a segment miss or intersect each exceptional hyperplane at isolated times, so integrating the derivative and passing to the limit is valid even for exceptional pairs. For p>2, with q=p-1, the sign balance gives |r_i|^q<=sum_{j!=i}|r_j|^q and subadditivity of power (q-1)/q then bounds every weight by 1/2. The input seminorm is the l1 norm of jumps modulo constants. A Jacobian applied to one unit jump gives a truncated (0,r,1-ell,1) sequence, so its variation is at most min(n-3,3), is at most one in the weight-half regime, and at p=2 is at most min((n-3)/3,1), by the constant weights. For exactness, the stated short input pairs give those step responses with mixed outputs a and delta-a by reflection and translation. Specifically a is the mean of (-1,1,delta) and obeys (delta-a)^q=2qa+O(a^3), with 0<a<delta. This forces a/delta to tend to 1 for q<1 and 0 for q>1, and equal 1/3 at q=1. The length-four, length-five and longer witnesses respectively have ratios |1-2r|, |1-2r|+r and |1-2r|+2r. At n=3 the output has one entry and zero variation. The p=2 witnesses already have the exact ratios; for p>2 and n>=6 an increasing step with both a pure zero and pure constant window attains one. The frozen checker was inspected, not executed; the generic-segment and limiting arguments establish the continuum and lengths beyond the numerical tests.

## originality

PASS

The distinct contribution supported by the comparisons is the exact nonquadratic path-length dependence and exponent split for a nonlinear two-input seminorm. The finite-set mean, arithmetic-average slice and step decomposition do not by themselves constitute novelty. The inspectable rank, dispersion and blend results use other statistics or different window conventions. This is not a historical priority certification.

## value

PASS

Three samples are a natural smallest window for an unweighted scalar p-mean with genuine p dependence (one sample is trivial and two average to the midpoint). The result identifies a discontinuous stability change across p=2 for differences of separately filtered inputs and pinpoints the length-six saturation and the shorter-path constants. The weight restriction and matching two-window witnesses explain the mechanism rather than just tabulating examples. This is a sharp benchmark for robust sliding smoothers, limited to real full-window paths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
