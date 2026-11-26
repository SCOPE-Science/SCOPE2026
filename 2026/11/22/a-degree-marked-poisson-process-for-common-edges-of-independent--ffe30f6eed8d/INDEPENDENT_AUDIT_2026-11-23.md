# Independent mathematical audit

## correctness

PASS

Conditioning on a fixed matching, the quotient tree has weight product c_i^{deg(i)}, and its n-r-2 Prüfer letters have probabilities c_i/n. Independently lifting each incidence gives one fair endpoint allocation per matched component plus a multinomial of length n-r-2 with probability 1/n per marked endpoint. This yields (1), also at n=r+2, and covariance -1/4-(n-3)/n². Two layers still factor after conditioning on both containments. For h distinct edges inclusion in both is at most (2/n)^{2h} (zero for cycles; otherwise use c≤2^{c-1}); only O_h(n^{2h-1}) tuples overlap. Disjoint tuples give the Riemann-sum intensity and the product limiting mark law. In particular all total factorial moments are bounded by 2^h, which dominates the multivariate generating-function expansion and justifies Poisson identification. Boundary strips and mark tails have uniformly negligible expected mass in the limit; one can work on the closed triangle to include finite atoms at y=1, or restrict those atoms out at a cost at most 4(n-1)/n². A fixed endpoint is a leaf with probability (1-1/n)^{n-3}/2 given the edge, and for n≥3 both endpoints cannot be leaves. This yields (2) and the nine independent Poisson limits. The uploaded checker was inspected as finite evidence, not used for the limit or executed.

## originality

PASS

Best-of-knowledge PASS for the joint space/four-degree overlap process, not for the unmarked law or the general underlying weighted enumeration. The familiar weighted forest count and sparse-collision moment methods are close inputs; the new content is their assembly into an explicit simultaneous conditional degree law and independence of marks across random common edges, including the pendant alignment projection. Credit Moon (1964) for the earlier exact unmarked formula and its implicit scalar limit, as documented by Bóna–Wagner; the record’s historical discussion omits Moon.

## value

PASS

A natural refinement of the classical overlap law distinguishes strong negative correlation of degree marks within an edge from asymptotic independence between collision sites. It calculates genuinely discriminating motif probabilities (aligned/opposed pendancy), and jointly predicts all fixed oriented degree classes, not just a numerical scalar or a cherry-picked finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
