# Independent mathematical audit

## correctness

PASS

For the hollow symmetric normalized n×n Monge simplex n>=3, canonical corner matrices V_(a,b) and metric-face cuts F_k have Gram entries 1/[2 max(i,j)(n-min(i,j))] and the stated exact corner/cut overlap. The candidate Y=(b/(a+b))F_a+(a/(a+b))F_(n-b) is a convex face point. Exact gradients g_k=<Y−X,F_k> attain their minimum at its two supported cuts; explicit positive three-region gaps certify <Y−X,Z−Y>>=0 for every face Z, hence Y is the unique Frobenius projection. The Gram expansion gives the stated rational squared distance. The distance-to-face function is convex; for all other vertices ab>=2 its squared distance is <=1/4, while V_(1,1) has greater value for n>=4; n=3 has only that nonmetric corner. Strict inequality and convexity rule out nonvertex maximizers. Independent full-matrix rational checks at (n,a,b)=(5,1,2),(7,2,3),(9,1,1),(11,3,5) matched both projection gradients and exact distances; all-n proof is separate. Limit squared Hausdorff distance is 1/2.

## originality

PASS

Best-of-knowledge PASS. Erickson–Kretschmann arXiv:2311.07522 is the exact same normalized hollow symmetric Monge object: it establishes the complete corner vertices and identifies the cut-metric face but does not give an outward Frobenius closest point. The October 18 face-incenter theorem deals with distances INSIDE this metric face, not corners of its parent simplex; the November 17 shortest-vertex-gap theorem studies pairs of vertices, not nearest points in the convex face. No equivalent general projection or Hausdorff formula was located in targeted Resultary and primary-material reading. This is a genuine metric-face separation invariant rather than reused intrinsic inradius.

## value

PASS

The normalized Monge family has a natural face of metrics/path pseudometrics whose separation from nonmetric corners quantifies failure of triangle inequalities. A closed rational formula for the unique nearest metric-face point of every vertex, full vertex-distance spectrum, and unique deepest nonmetric matrix is a useful structural classification in all sizes, even though arbitrary interior-matrix projection remains open. Two-cut sparsity of the optimum is not an automatic consequence of the known vertex/face list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
