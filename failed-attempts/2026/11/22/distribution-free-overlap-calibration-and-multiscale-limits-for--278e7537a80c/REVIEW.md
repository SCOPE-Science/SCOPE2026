# Independent mathematical audit

## correctness

PASS

On each size class the label action is transitive, so independent exchangeable matchings become independent uniform matchings given their sizes. Counting completions of r prescribed disjoint edges in size b gives 2^r (b)_r/(n)_{2r}; summing over the binom(a,r) subsets of the first matching proves the exact PGF including empty size classes of positive probability. For the circle, root the cyclic order at a sampled label; the spacings are Dirichlet(1,...,1) and their order is that of iid exponentials. The shortest direction from a point meets an adjacent point first; hence reciprocal edges are exactly strict cyclic gap minima. Their mean is 1/3, adjacent joint probability 0 and distance-two joint probability 2/15 (integrate independent uniform gap ranks x,y with factor (1-x)(1-y)(1-max(x,y))); triples farther apart are independent. This gives the stated mean and variance for n>=5 and a stationary two-dependent CLT after changing at most two seam terms. Given M_i the two overlaps sharing sample i are independent and have means 2R_i/[3(n-1)], which gives the finite covariance. For the joint factorial-moment expansion, in a pattern with m distinct prescribed edges, v distinct label vertices, and D required incidences of a prescribed edge in a particular matching, the contribution is O(n^{v-D}) or zero if matching constraints conflict. Always v<=2m and D>=2m. A shared vertex makes the first strict; reuse of an entire edge across distinct pair types makes the second strict. The remaining configurations have (n)_{2T}/2^T assignments for T ordered slots and tend to the product factorial moments of independent Poisson variables of means 2 rho_i rho_j. These estimates hold along every deterministic size sequence tending to the stated ratios, with uniformly bounded moments for each fixed multi-index. The product Poisson law is moment-determinate. With random sizes whose ratios tend in probability to 1/3 the conditional expectations of bounded overlap test functions therefore tend in probability to constants, giving joint independence from the Gaussian size vector.

## originality

FAIL

Deng's earlier Lemma 3.3 and Theorem 1.2 cover the mathematically substantive matching claims by fixed-size thinning of a uniform perfect matching. The exact PGF follows by thinning the perfect-matching overlap count against a single disjoint-edge target. The fixed-q joint conditional Poisson law follows by exposing replicates in order with the previous partial matchings as bounded-degree targets and then thinning. The Gaussian size limit is the interval local-minimum limit with a bounded change at the seam; the Gaussian–Poisson product is the usual conditioning consequence of the conditional limit having a constant limit law. The finite shared-replicate covariance is a direct law-of-total-covariance specialization of the edge marginals and size variance. The distribution-free calibration is a useful interpretation, but follows immediately by transitivity and does not make these implications new. This decision is based on actual earlier results and their implications, not a same-day similarity or an inaccessible paper.

## value

PASS

The inference problem is meaningful: conditioning on observed sizes gives an exact nuisance-free null calibration for whether a reciprocal pair persists under independent resampling. Simultaneous asymptotics explain why a real finite shared-replicate dependence can vanish, and when size fluctuations separate from the overlap statistics. This is usefulness of the benchmark, not credit for a new mathematical contribution beyond the sources and implications assessed above.

The dated certificate retains the supplied scientific assessment, sources and limitations.
