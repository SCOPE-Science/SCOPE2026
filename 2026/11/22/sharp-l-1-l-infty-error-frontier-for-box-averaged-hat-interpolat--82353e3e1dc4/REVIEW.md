# Independent mathematical audit

## correctness

PASS

A homogeneous BV input is a constant plus the superposition of unit steps against its finite signed derivative measure. The operator fixes constants; integrating the step error against the total variation measure bounds both norms, and individual steps certify sharpness. After rescaling and reflecting, t lies in [0,1/2] at h=1. The reconstructed unit step is a cumulative distribution with constant densities W, Z-W, 1-Z on [-1,0], [0,1], [1,2] respectively, where W=max(0,1/2-t/alpha) and Z=min(1,1/2+(1-t)/alpha). The integrated error is the mean absolute distance of this distribution from t. Direct integration gives the frozen formula; as the region changes from W>0,Z=1, the derivative first has sign of t(alpha+3t-4), then is either 2t-1 (if W has clipped) or (1-2t)/alpha (if Z has become interior). Thus the maximum is at phase zero or one half, changing at alpha=3/2. The essential uniform error is the larger of the two one-sided jump discrepancies. The lower trace U=(1-t)W+tZ is at most 1/2 on the chosen half-cell; on the first region it is a convex quadratic with vertex (2-alpha)/4, on the W=0 region it is t, and on the both-interior region it equals 1/2. The minimum therefore occurs at the first clipping point t=alpha/2 for alpha<=2/3 and at the vertex for alpha>=2/3. At alpha=2 the profile allows all phases and the formula gives 1/2. This yields both sharp coefficients, including the ties and exact 49/96 at the unique constrained bandwidth 3/2. Summing averaged adjacent differences gives total variation diminution, and centered masses plus affine interpolation reproduce affine functions locally.

## originality

PASS

The operator itself already occurs as an exact specialization of a generalized Kantorovich sampling series, and the shape and approximation-order background are not credited as new. The supported distinct contribution is the two sharp homogeneous-BV norm constants over the full width interval, with jump witnesses and the resulting constrained bandwidth choice. The closest exact catalogue comparison uses a different norm and periodic inputs; the closest general published operator result treats continuous-function estimates and does not supply these constants.

## value

PASS

A single bandwidth must trade integrated error against oversmoothing and the worst pointwise jump discrepancy. An unspecified convergence constant cannot choose the width or locate the worst shock relative to the mesh. The two different phase thresholds give a meaningful exact design rule: up to alpha=3/2, increasing width improves the worst uniform error without paying more integrated error, and immediately beyond it the sharp integrated coefficient increases. This is a complete family-specific result, not an arbitrary single-width computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
