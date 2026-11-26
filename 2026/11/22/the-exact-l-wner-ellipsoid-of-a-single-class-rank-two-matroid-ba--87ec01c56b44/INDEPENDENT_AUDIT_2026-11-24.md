# Independent mathematical audit

## correctness

PASS

The vertex set is exactly the cross pairs and B-pairs. To see the clipped-hypersimplex equality, aggregate the A-coordinates to a single coordinate in [0,1]; the projection is the second hypersimplex on b+1 coordinates. Decompose into its pair vertices and distribute each cross-pair mass among the A sites in the proportions x_i/x(A), if x(A)>0. The two within-part contrast spaces are spanned by vertex differences and a cross minus a B-pair adds a between-part direction, giving full intrinsic dimension. In the proposed vertex design, covariance along a zero-sum A contrast is p/a times its squared norm; along a zero-sum B contrast the unordered-pair contribution uses sum_{i<j}(z_i+z_j)^2=(b-2)sum_i z_i^2, giving the stated sigma_B with the singleton contribution. The between-block scores differ by sqrt(kappa), giving sigma_T; the cross covariances vanish from block symmetry and conditional mean zero. All eigenvalues are positive including b=2. The determinant has the stated strictly log-concave scalar factor with vanishing endpoints. Multiplication of its stationary equation by positive denominators gives the stated quadratic, and b=2 or 3 gives the stated fractions. Subtracting the two orbit gauges gives (a-1)/p+(1-2p)/(p(1-p))+(3-b)/(b sigma_B), exactly the log-determinant derivative. Their weighted average is d, so at the optimum each is d. Strict convexity excludes all nonvertex contact. For any competitor (m,R) average the containment inequality over the design: 1>=tr(R^{-1}C)+(c-m)^T R^{-1}(c-m). Trace–determinant AM–GM proves det R>=d^d det C with equality only for m=c and R=dC, establishing global uniqueness and the intrinsic volume/semiaxes. The a=2,b=3 example checks directly with p=2/3 and sigma_T=5/27. The 70-digit checker and its recorded 361 scalar and 49 matrix scopes were inspected, not independently run; those finite tests are not the proof.

## originality

PASS

Credit classical covariance/contact and D-optimal design principles, the known underlying matroid and hypersimplex representation, and related metric invariants. In the available statements the supported distinct claim is the exact two-orbit optimal mass, covariance and complete contact geometry throughout the specific rank-two family. The strongest plausible broader panhandle result could subsume this claim, not just share its method. Its available catalogue statement does not certify the needed rank/size domain, and bounded attempts did not recover those assumptions. The decision is from the available statements and is not a historical priority certification or a finding that the broader paper is noncovering.

## value

PASS

For a canonical minimally clipped hypersimplex, determining the intrinsic outer covariance geometry is a natural exact problem distinct from face counts, inradius or normal cones. The closed scalar design, all-vertex contact, global optimality and explicit axis classes give an independently useful complete metric description, including the small-head cases. Its value is in the exact family-specific geometry where not already supplied by a verified encompassing result, not in restating the general D-optimality criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
