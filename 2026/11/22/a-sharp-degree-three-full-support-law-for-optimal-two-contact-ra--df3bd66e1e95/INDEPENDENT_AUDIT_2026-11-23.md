# Independent mathematical audit

## correctness

PASS

For fixed iid draws independent of the initial disagreement, the rank-one endpoint projections give trace(P_e P_f)-1=n-3+(b_e^T b_f)^2/4, so the matrix is A=(1/2)I+(1/4)C^TC=I+(1/4)Adj(L(G)), positive definite even if C is rank deficient. Thus there is one simplex minimizer. The interior condition Ap=lambda*1 gives p proportional to C^T w with (2I+CC^T)w=1. The vertex fixed point sends [0,1/3]^V into itself, with maximum row contraction 3/5 at degree 3. On an edge, each endpoint equation with other neighbors moved to the right is >=1/3; adding gives 6(w_u+w_v)>=2/3, and Z<=2m/3 proves the positive bound. Independently, substituting a=(1-b)/(2k) into the balanced double-star quadratic gives (k+3)/(8k)+(k-3)b/(4k)+(5k+3)b^2/(8k). Its minimum over 0<=b<=1 yields exactly the two cases in the theorem; at k=3 the excess is 3b^2/4. Symmetry of the unique optimizer justifies uniform leaf probabilities. The frozen rational checker was inspected, not run. A separate mask count gave 1, 4, 38 and 472 labeled connected subcubic graphs at orders 2–5, consistent with the 526 counted cases after the three extra graphs and eight double-stars. The theorem is proved for arbitrary size, not by that count.

## originality

PASS

The general finite-horizon objective, uniqueness and interior inverse criterion have an exact counterpart in a distinct same-day path record. The comparable double-star result has a different objective despite the same family and sharp cutoff. The verified surviving content is the graph-class positivity theorem with quantitative bound and the sharp boundary for this particular objective, not the quadratic reduction or a generic inverse formula.

## value

PASS

Optimal support is an operationally meaningful invariant: subcubic graphs retain every interaction with a quantitative guarantee, but the smallest permitted maximum-degree increase can yield a uniquely optimal disconnected support. The exact double-star solution distinguishes a boundary equality from a strictly active bridge constraint and illustrates why a two-contact optimum does not guarantee long-run consensus. These are structural conclusions beyond the standard quadratic reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
