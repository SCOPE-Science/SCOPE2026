# Independent mathematical audit

## correctness

PASS

For iid independently oriented shorter great-circle arcs with L in (0,pi), conditioning on an arc of length ell gives an intersection probability g(ell)=ell E[L]/(2pi^2): one point of the antipodal supporting-circle intersection pair hits the fixed arc with chance ell/pi, and an independent arc of length s covers it with chance s/(2pi). This gives the exact conditional Binomial(n-1,g(ell)) degree law and star moments. Crossing indicators of disjoint pairs are independent; covariances of two pairs sharing one arc equal Var(g(L))=E[L]^2 Var(L)/(4pi^4). Counting 3*C(n,3) unordered overlapping pairs proves the stated variance with coefficient 6*C(n,3). The first Hoeffding projection gives the n^(3/2) normal CLT when length variance is positive; the degenerate remainder has L2 variance O(n^2). Uniform Hoeffding tails and Borel–Cantelli imply empirical normalized-degree weak convergence. For L density sin(L)/2, E[L]=pi/2, Var(L)=pi²/4-2, p=1/8 and degree density 2pi sin(4pi x) on (0,1/4). For deterministic L the pairwise indicators, though not necessarily mutually jointly independent, have zero covariance, so variance is exactly binomial-order. The proof distinguishes that case from any unproved smaller-scale CLT.

## originality

PASS

The pair crossing probability 1/8 and general graphon edge-density/convergence machinery are prior results, not original claims. Bonamy–Mohar–Wesolek treat geodesic drawings with arcs sharing endpoints and their graphon statistics; their inspected primary proof does not give the exact iid isotropic independent-needle conditional degree mixture, all star moments, all-n variance correction and length-variance-dependent CLT/scale transition. General U-statistic results furnish the limiting mechanism, not these specialized evaluated invariants.

## value

PASS

A natural sphere-intersection random graph model has a complete explicit degree mixing law and all centered crossing-count second-order statistics. Detecting that heterogeneous arc lengths create order n^3 variance while fixed lengths retain order n^2, despite the same edge marginal at the endpoint specialization, is a structural probabilistic distinction of use in stochastic-geometry and network models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
