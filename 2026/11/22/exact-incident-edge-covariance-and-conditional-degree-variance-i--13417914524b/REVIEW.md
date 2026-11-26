# Independent mathematical audit

## correctness

PASS

The iid atomless ranks can be represented by iid uniforms. The endpoint pair must occupy the two top ranks against its edge's blockers, giving p_m. For the incident joint law without endpoint obstructions, partition by which of i,j,k has the smallest uniform. If i is smallest, a root value x gives integrand x^h(1-x)^2. If j is smallest with value v, the m blockers of its edge must be below v, while the n-s remaining blockers must be below z=min(U_i,U_k). Integrating v<z gives z^(h+1)/(m+1) against the density 2(1-z), and the k-smallest case exchanges m and n. These three contributions give the first branch. If j blocks ik instead, only v<z is allowed and the number of additional external blockers is n-s-1, giving z^h/(m+1); interchange j and k for the third branch. The zero assigned to mutual obstruction is algebraically correct, and in fact that branch is geometrically vacuous here: a positive-length crossing of j on ik gives a point x strictly closer to j than to k (the distinct squared-distance affine functions cannot tie throughout the segment since they differ at k). Thus |ij| <= |ix|+|xj| < |ix|+|xk|=|ik|. The reverse membership would imply the opposite strict inequality. This sharpens the scope note without changing the theorem. Variance follows by summing indicator variances and pairwise covariances. Independent rational halfspace clipping for the witnesses gave, on 01 and 02, exactly the stated cells, with respective intervals [73/202,97/138], [73/164,74/139] for P_+, and [13/30,3/5], [25/58,27/44] for P_-. The squared-norm cocircular determinants were nonzero (13226 and 3500), and all triple determinants were nonzero. Covariances are 5/36 and -1/36. The frozen checker and verification were inspected, not executed. These laws are conditional on fixed sites, not annealed laws for random sites.

## originality

PASS

The supported contribution is the arbitrary fixed-site incident-edge joint law, covariance and conditional second moment of degree, with actual site examples of both signs. The graph definition and marginal/mean are prior, and mutual obstruction is an abstract rank-algebra branch rather than an additional Euclidean configuration. The relevant one-dimensional and direction-restricted lattice degree laws do not cover this claim.

## value

PASS

For this irregular-site graph the degree mean misses substantial signed dependence. The result supplies a way to calculate conditional uncertainty from the site configuration without sampling heights or enumerating rank orders. The signed witnesses show that treating incident edges as uniformly positively correlated, or as independent, gives a materially wrong second moment. The useful invariant is conditional variance at prescribed sites, not a proposed asymptotic scaling for a random geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
