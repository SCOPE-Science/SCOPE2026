# Independent mathematical audit

## correctness

PASS

A generic projected convex edge is a silhouette edge precisely when the adjacent outward facet-normal dot products with the random viewing vector have opposite signs; for spherical Haar directions the probability is exterior angle/pi. The antiprism has exactly 2n cap/base edges and 2n connecting edges. Writing c=cos(pi/n), d=1-c and M=4h^2+d^2, cross products give normal-angle cosines d/sqrt(M) and (4ch^2-d^2)/M. Consequently E N=(2n/pi)(alpha+beta). With s=sin^2 alpha, kappa=1+c, cos beta=kappa s-1, differentiation gives 1-2 sqrt[kappa(1-s)/(2-kappa s)], with one zero at s=(4kappa-2)/(3kappa), derivative negative then positive for all n>=3. Solving h gives stated h^2; comparing squared base and connector edges proves lateral faces equilateral exactly there. Limits are 2n at h downarrow0 and n+2 at h to infinity; small-angle expansions yield n+sqrt(3)+O(n^-2). Independently evaluated the formula and strict sample comparisons at orders 3,4,5,9,20; n=4 yields h=0.594603558 and mean=5.716099405. These numerical checks are not the all-order proof.

## originality

PASS

The general expected-silhouette edge-angle sum is classical and the published square-antiprism random-view law gives an n=4 first moment. Neither establishes the all-n strict global minimizer or equilateral-face characterization. A separate triangular-antiprism max-vertex probability law optimizes a different statistic. This is best-of-knowledge only; the inaccessible original Kettner–Welzl technical report creates a meaningful priority risk.

## value

PASS

A natural all-order geometric shape optimization problem for average random-view combinatorial complexity has a unique geometrically rigid solution: the uniform (equilateral-faced) antiprism. The exact mean, strict monotonicity, and n+sqrt3 asymptotic make the result useful to convex geometry and randomized projections; it is neither an arbitrary finite slice nor just re-evaluation of the classical silhouette formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
