# Independent mathematical audit

## correctness

PASS

Rotating a distinguished sampled point to zero makes the remaining circular spacings uniform on the (n-1)-simplex. Translating distinct exceedance coordinates and rescaling the remaining simplex gives the positive-part power in (5), including zero mass at saturation. In the mixed second moment the same-gap term uses s by nesting, while the distinct-gap term uses r+s; subtracting the product of means gives (1). Dividing by the positive factor n(1-s)^(n-1) yields the strictly decreasing bracket before s=1-r and its constant plateau thereafter. The plateau yields r_c, which is at most 1/2 since n<=2^(n-1), with equality only at n=2. Below r_c the variance at s=r is strictly positive: open simplex sets give exactly one and at least two exceedances. This supplies the unique interior crossing, and solving the bracket gives the stated s_*. At r=r_c the zero plateau includes all admissible s for n=2. For the PGF, each factor is 1+(u-1)I_r+u(v-1)I_s, so disjoint coordinate selections yield the claimed exact multinomial sum. Expanding the exact powers at r=x/n,s=y/n gives the stated kernel, and its positive diagonal and strict sign crossing justify bracketing the finite root; e^x-1>x^2 for x>0 follows from e^x>=ex>2x for the derivative comparison. Independent rational polygon clipping of the n=3 simplex at r=1/10 and s=3/5 gives means 243/100 and 12/25 and product moment 51/50, hence covariance -183/1250. Replay with python3 /workspace/branches/ac27b14d-0ad4-4dd3-bb1b-b3b51bab8d0b/exact_reproduction.py. The replay checks this example only; the uploaded VERIFICATION.md and verify.py were inspected, not run.

## originality

FAIL

The submitted distinct claim is the explicit finite-size threshold-indexed sign diagram. An earlier distinct indexed finding gives it completely, including the zero interval and n=2 case, under the literal specialization to all coordinates of a symmetric Dirichlet vector with shape 1. A second earlier record independently covers the same specialization for n>=3. The frozen result specifically disclaims novelty for the simplex-volume input, PGF construction and limiting kernel. The PGF was not located verbatim in these matches, but is obtained mechanically by multiplying the elementary indicator factors and inserting the classical joint exceedance volumes, not a surviving distinct claim of the submitted kind. This is a coverage failure, not false mathematics or an access-based decision.

## value

FAIL

The finite sign question is natural and the result is correct, but as a standalone contribution it fills no remaining gap: the complete boundary and the nested-count counterexample are supplied by the indexed stronger theorem. The remaining two-variable PGF is a routine coefficient encoding of classical simplex survival probabilities, and the scaled limit is known. No scientifically valuable unredundant remainder warrants a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
