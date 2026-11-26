# Independent mathematical audit

## correctness

PASS

Positive weights and the quadratic term give a unique proximal map. In the disjoint case, combine duplicate weights; radial soft thresholding subtracts t times the aggregate weight from the radius with a floor at zero, which composes additively, including zero blocks and coordinates in no group. At strictly positive x the implicit proximal equation gives T_h(x)=x-hg+h²Hg+O(h³), g=grad F(x), H=Hess F(x). The solution is analytic jointly in input and step nearby, so the two-step and one-double-step expansions have h² coefficients 3Hg and 4Hg. Each Hessian group term is a positive scalar times the orthogonal projection onto the within-group tangent space perpendicular to x_G. Consequently Hg=0 requires g_i/x_i constant within every group. Any unequal intersecting groups provide a pair i,j in one group distinguished by another, oriented so that a group contains i but not j. Increasing x_i with the other coordinates set to 1 makes the sum of i-only contributions to g_i/x_i tend to zero and leaves the j-only sum fixed; if that fixed sum is zero then the i-only sum stays strictly positive at every finite x_i. Thus the two ratios differ at a finite positive witness, making the Hessian quadratic form and Hg nonzero. This includes proper nesting and singleton groups. Independent symbolic differentiation (/workspace/replay/local_formulas.py) confirms the stated crossing-pair coefficient and the nested two-coordinate obstruction. The frozen checker does not exhaust all distinct group families on three coordinates: it caps family size at four in n<=3. The accompanying all-family language about numerical checks should be read with that limit; the proof, not sampling, proves the all-family theorem. No claim is made for the latent penalty or non-Euclidean group norms.

## originality

PASS

Closest inspected prior work supplies direct group penalty algorithms, projection duality or a general gradient-flow criterion. Neither the individual principles nor the same-day classifications for different penalties give this necessary and sufficient group-incidence condition with its local obstruction.

## value

PASS

The classification determines exactly when repeated parameterized regularization can be replaced by a single step for a standard penalty. The necessity includes overlaps for which the individual proximal map is easy to compute, and the explicit defect witnesses show failure already at arbitrarily small steps, uniformly as a qualitative assertion over all positive weight choices. This is a structural result rather than a generic statement that resolvents need not compose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
