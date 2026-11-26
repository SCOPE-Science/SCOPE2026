# Independent mathematical audit

## correctness

PASS

On the constant direction W and K are the identity; on its orthogonal complement K=(1-theta)W, with W's eigenvalues in [3/5,1] by the cubic adjacency bound. Hence the condition bound holds even for disconnected G. The Neumann series and the positive rank-one term give entrywise positivity, and symmetry gives column as well as row stochasticity. With J the orthogonal projection onto constants, the same splitting gives K^{-1}=(I+L_G/9-theta J)/(1-theta). Writing y=Kx reduces the reciprocal dual ratio to the maximum of y^T K^{-1}y on the cube; strict convexity forces sign vertices. In the primal ratio use a sign s with s^Tx=||x||_1 and Cauchy–Schwarz in the K-metric, with equality only along K^{-1}s for maximizing s. The sign-adjusted numerator of each coordinate of K^{-1}s is at least 1-theta>0, giving the stated normalization and converse. Since s^T L_G s=4c(s) and s^T J s=b(s)^2/n, the total possible penalty is at most 1/100, below a one-edge gain of 4/9, which also proves the balance tie-break. The bound M=1/mu<1.7n makes the reciprocal error at most eta M^2/(1-eta M)<0.03 for eta=1/(100n^2), n>=4. After scaling by at most 9/4 and allowing the exact balance bias 9/400, the error in cut recovery is <0.1. Rational matrix construction has polynomial bit complexity, e.g. by minors of the integer matrix 12I-A and exact rational arithmetic. Thus the known cubic MAX CUT hardness gives a polynomial-time reduction to the advertised additive approximation of mu, not of an individual coordinate update. The support code was inspected as finite evidence, not executed.

## originality

PASS

Credit sharp l1 curvature and the incidence-matrix max-cut norm identity to prior work. What is supported as distinct is their conditioned positive stochastic realization with an exact secondary optimizer criterion and a recovery guarantee at inverse-quadratic additive precision for the curvature itself. Generic hypercube hardness alone is not a claim about this inverse-matrix class.

## value

PASS

The construction answers a concrete optimization question: can the exact l1 certificate used to assess a Gauss–Southwell bound remain hard to evaluate on benign, uniformly well-conditioned Hessians? It shows that positivity, stochastic normalization and good spectral conditioning do not make sharp parameter evaluation easy, while identifying the worst gradient signs and preserving polynomially bounded input and requested precision. This is not a claim about the cost of a step or the observed trajectory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
