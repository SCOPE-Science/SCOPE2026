# Independent mathematical audit

## correctness

PASS

Anchor the cyclic ordering at a labeled sample point so that rotating to that point gives Dirichlet(1,...,1) gaps. The minimum of the two incident arc gaps equals a point's nearest-neighbor distance; a local-minimum gap is necessarily shorter than a semicircle. Thus the mutual pairs are exactly the strict cyclic gap minima. With independent Exp(1) gaps before normalization, the Gamma total is independent of the normalized vector and both gap ranks and mutual-pair labels survive normalization. Consequently the raw mixed covariance divides by E[S^alpha], not by (E[S])^alpha. Put m=Gamma(alpha+1)/3^(alpha+1). Per index, the diagonal 2m/3 cancels the two adjacent terms -m/3. At offset two there are exactly five distinct gaps even for n=5. Integrating the first marked gap out of exp(-2x-2y-max(x,y)) gives (1/2)exp(-3y)-(1/6)exp(-5y); multiplication by y^alpha and subtraction of m/3 gives Gamma(alpha+1)(3^(-alpha-1)-5^(-alpha-1))/6. Both offsets contribute, and larger offsets use disjoint exponential variables. This proves the mean and covariance, including the alpha=0 extension, the alpha=1 constants and the scale change via the gamma ratio. The supplied rational rank-order code was inspected, not executed; its finite integer-power cases are not the all-real proof.

## originality

PASS

The finite-n circular covariance for the mutually marked power sum differs materially from the inspected directed, unweighted, and interval results. Credit the interval power-one constant and the shared distance-two computation rather than treating either as new. The bounded comparisons do not establish historical priority.

## value

PASS

Mutual edges are a natural subgraph and powers are a standard one-parameter family of length costs. The exact covariance shows how using that subgraph reverses the sign of the ordinary-length directed result and identifies precisely which length cost has order-one count coupling as sample size changes. The power-one limiting constant alone would not add the same value; the finite-sample result for every positive power makes a useful benchmark for marked geometric-graph moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
