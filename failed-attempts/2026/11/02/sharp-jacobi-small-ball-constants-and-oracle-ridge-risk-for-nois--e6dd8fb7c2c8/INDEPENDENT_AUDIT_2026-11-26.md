# Independent mathematical audit

## correctness

PASS

With epsilon=sqrt(s), mean/deviation coordinates give Jacobian sqrt(m) and a transverse ball of dimension m-1. Away from the ends the product density converges to the beta density to the m-th power. For a subcritical end, scaling all coordinates by epsilon gives s^(ma/2) times the stated integral: bounded rescaled boxes are integrable because a>0 and the unbounded mean integral converges because m(a-1)<-1. At a critical end the section contributes proportional to s^q times the integral of dt/t from M epsilon to eta. Its relative integrand error can be made arbitrarily small by first choosing large M and small eta; the remaining parts of this endpoint's neighborhood contribute O(s^q) for fixed M and eta. This gives the factor 1/2 in the log coefficient. The two disjoint ends add even at equal exponents. The interior beta integral, inverse-moment boundary, and uniform and arcsine calibrations agree with this normalization. For fixed S>0 and lambda*=sigma^2/b^2, the conditional excess risk is b^2 S (lambda-lambda*)^2/[(S+lambda)^2(S+lambda*)], proving uniqueness also against lambda=0, whether or not the OLS expectation is finite. For the oracle risk the Stieltjes kernel integral yields the beta-function coefficient below delta=1, a logarithm at delta=1, and dominated or monotone convergence above it. No geometric critical logarithm enters the delta<=1 regimes since q>=3/2.

## originality

FAIL

The full two-endpoint statement is not quoted verbatim in the inspected prior sources, but its constants are mechanically implied. Royen's Theorem 3 already gives the exact subcritical and critical coefficients for each power endpoint in the same statistic and all sample counts. On S<=s, coordinate spread is at most sqrt(2s), so fix a small eta and split into all coordinates within eta of one end or the other and the remaining interior. In either endpoint neighborhood the beta joint density differs from the matching pure-power joint density by (a B(alpha,beta))^(-m) times a factor tending uniformly to one as eta decreases. For the pure-power law the excluded part of S<=s is O(s^q), negligible both below and at criticality. This transfers Royen's constants endpoint by endpoint; two matching contributions just add. Above criticality the ordinary diagonal tube coefficient follows from L^m translation continuity, and the integral is a beta function. The risk optimizer and its small-noise constants are then elementary conditional squared-error and one-variable integral deductions. Thus the arbitrary-parameter synthesis is correct but is not a distinct non-mechanical finding.

## value

FAIL

Exact design-noise benchmarks are well motivated, and the formulas are useful as an exposition. Here the endpoint coefficients transfer by a local multiplicative density comparison, the rest is the standard diagonal tube, and the oracle risk adds only a pointwise squared-error identity and elementary integration. No independent non-mechanically-implied result survives the comparisons; the explicit four-arcsine ridge benchmark follows by the same steps and does not warrant a separate repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
