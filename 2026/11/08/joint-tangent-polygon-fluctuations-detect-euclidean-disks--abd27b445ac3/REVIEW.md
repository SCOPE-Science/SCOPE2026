# Scientific review: joint tangent-polygon fluctuations

## Correctness — PASS
The theorem concerns homogeneous Poisson support-normal sampling, conditioned on a gap event of exponentially high probability. The exact one- and two-point Palm identities give the cubic-gap mean and covariance, including the two negative neighboring-gap boundary terms. This yields the constant \(504\), which differs from the fixed-sample-size coefficient. A block argument establishes the weighted Gaussian limit. The geometric area and perimeter errors admit local cubic-gap expansions with \(O_K(\sum d_i^4)\) remainders, and the remainder has \(L^2\) order \(O(\lambda^{-3})\), negligible at the claimed fluctuation scale. The Cauchy–Schwarz equality case and periodic support-function ODE prove disk rigidity. The standalone checker independently validates polygon geometry, mean coefficients, and covariance in the disk and noncircular cases; finite simulations do not establish an infinite theorem.

## Originality — PASS, historical priority provisional
Bakó-Szabó and Fodor, *On the variance of the mean width of random polytopes circumscribed around a convex body* (DOI 10.1112/mtk.12266), analyze random-offset circumscribed halfspaces and provide mean-width variance estimates, not joint sharp covariance for exactly tangent, Poisson-angular halfplanes. Hug and Schneider, *Poisson hyperplane processes and approximation of convex bodies* (arXiv:1908.09498), study stationary hyperplanes and approximation bounds, likewise not this support-only sampling law. Calka, Demichel and Enriquez, *Large planar Poisson–Voronoi cells containing a given convex body* (DOI 10.5802/ahl.86), use a Poisson–Voronoi model. Existing related polygon sampling and random rotation results concern materially different random objects and observables. The claim is the explicit joint covariance and its vanishing-determinant characterization, not a general CLT technique. The main residual risk is an earlier equivalent result under Poisson-spacings or renewal-reward terminology.

## Mathematical value — PASS
Area and perimeter are natural paired approximation errors. Their separate leading fluctuations cannot identify a circle, whereas the joint covariance determinant is exactly zero only for disks. The theorem therefore gives a quantitative, structural inverse-geometric characterization with a sharp covariance matrix and specifies when the conclusion does not transfer (fixed-count tangents and random-offset models). This is not merely a reparametrization of an existing scalar variance bound.

## Limitations
The body must be strictly convex with \(C^4\) support and strictly positive curvature radius; the tangent normals follow a homogeneous Poisson process, and the polygon is conditioned on the good-gap event. No rate of Gaussian convergence or nonsmooth extension is proved. Historical priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
