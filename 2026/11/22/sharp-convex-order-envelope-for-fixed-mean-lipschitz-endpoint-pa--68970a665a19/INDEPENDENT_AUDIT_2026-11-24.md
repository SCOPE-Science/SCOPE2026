# Independent mathematical audit

## correctness

PASS

The path crosses the full range. For each nonnegative continuous test function, integrating its primitive along the path bounds the output-law integral below by the uniform integral divided by L, without monotonicity. Conversely if a=Q(s)<Q(t)=b at interior quantile levels, F(a)>=s and F(b-)<=t, and the mass of (a,b) is at least (b-a)/L. Thus Q(t)-Q(s)<=L(t-s) even in the presence of atoms. Full support gives endpoint traces 0 and 1. The residual is a probability with the prescribed mean, and Jensen and the endpoint chord give its two sharp bounds. For equality with a strictly convex loss, the residual support is finite and specified by the bounds. A decrease f(x)>f(y) at x<y forces three disjoint traversals of an interior band avoiding that support; applying the primitive inequality on [0,x], [x,y], [y,1] contradicts the prescribed density 1/L on that band. The continuous nondecreasing realization is unique. Endpoint means coalesce, and L=1 forces the identity. Independent bounded symbolic variance check: python3 /workspace/review_replay.py, check 2. Neither that check nor the recorded finite tests certify the general theorem.

## originality

PASS

Credit the general Jensen and chord bounds, quantile realization and one-dimensional crossing arguments as known tools. The supported distinct claim is the exact realizable occupation-law class for the nonmonotone-allowed endpoint/Lipschitz problem, together with strict equality rigidity at the path level. No inspected statement establishes this combination or implies it without the path-law and rigidity arguments; this is not a priority certification.

## value

PASS

The exact feasible laws reduce a constrained trajectory problem to a single residual moment for every continuous convex loss. This supplies sharp universal bounds and a mechanism excluding all nonmonotone equality paths despite allowing oscillations, not just a recomputed Jensen bound. The variance example is a usable benchmark under the stated fixed endpoint, mean and slope constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
