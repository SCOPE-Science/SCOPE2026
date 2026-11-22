# Optimal planar Latin-hypercube extension and the three-quarter retention law

## Finding

Consider a two-dimensional Latin-hypercube design with \(n\) points, each coordinate lying in a different one of the \(n\) equal strata of \([0,1]\). When both axes are re-stratified into \(N>n\) equal intervals, let \(R_{n,N}\) be the largest number of old points that can be preserved *at exactly their original coordinates* inside a completed, strict \(N\)-point Latin-hypercube design.

**Deterministic structural theorem.** For all integers \(N>n\ge1\) and all old designs avoiding stratum boundaries, the conflict graph of old points is the union of two matchings. All its components are paths or even cycles, so \(R_{n,N}\) is computable exactly by a linear scan of the original stratum-order lists and a traversal of these components. On a path of \(t\) vertices its contribution is \(\lceil t/2\rceil\); on an even cycle of \(t\) vertices it is \(t/2\). This is an exact optimum, not a heuristic.

**Random one-point extension theorem.** Suppose the original design is a standard random planar Latin hypercube: in first-coordinate stratum \(i\in\{0,\ldots,n-1\}\), put
\[
X_i=\frac{i+U_i}{n},\qquad Y_i=\frac{\pi(i)+V_i}{n},
\]
where \(\pi\) is an independent uniform permutation and all \(U_i,V_i\) are independent \(\operatorname{Uniform}(0,1)\) variables. Define the minimum deletion cost \(D_n=n-R_{n,n+1}\). Then
\[
\boxed{\frac{D_n}{n}\xrightarrow{\mathbb P}\frac14,\qquad \frac{R_{n,n+1}}n\xrightarrow{\mathbb P}\frac34.}
\]
In particular, \(\mathbb E[D_n]/n\to1/4\), since \(0\le D_n/n\le1\). The exact finite-sample probability that *all* original points may be kept is
\[
\boxed{\Pr(D_n=0)=\left(\frac{2^n n!}{(n+1)^n}\right)^2,\quad n\ge1,}
\]
so by Stirling's formula
\[
\Pr(D_n=0)\sim\frac{2\pi n}{e^2}\left(\frac4{e^2}\right)^n.
\]

## Assumptions and scope

A strict \(N\)-point two-dimensional Latin hypercube has exactly one point in each interval \([j/N,(j+1)/N)\) for every coordinate and every \(j\in\{0,\ldots,N-1\}\). Existing coordinates are *fixed*, not moved, and newly evaluated points may be placed anywhere in the remaining coordinate strata. The boundaries have probability zero in the random model; the deterministic theorem may use a fixed half-open convention at boundaries. The sequence \(N=n+1\) concerns a one-point *target size increase*, not a restriction on the number of fresh evaluations after old observations are removed. The theorem concerns two coordinate dimensions; it does not assert the same computational complexity or retention limit in higher dimensions.

## Proof

### 1. Exact extension equals maximum independent set

Place an edge between old points precisely when they occupy the same new stratum on at least one coordinate. Any preserved subset must be independent. Conversely, if \(r\) old points are independent, the \(N-r\) unused first-coordinate strata and the \(N-r\) unused second-coordinate strata can be arbitrarily paired. Placing one new point in each resulting product rectangle completes a strict \(N\)-point design. Thus \(R_{n,N}\) is exactly the conflict graph's independence number.

A new stratum has width \(1/N<1/n\), so it intersects at most two old strata. As each old stratum initially contains exactly one point, any new stratum contains at most two old points. Moreover, a point belongs to only one new stratum on a given coordinate and therefore can collide with at most one other old point on that coordinate. Each coordinate's conflict edges consequently form a matching. A union of two matchings has maximum degree two and every cycle alternates between the two edge colours, so each cycle is even (a duplicated edge is harmless). The claimed path-and-cycle formula gives a linear-time exact independent set. When old stratum indices are available, adjacent old-stratum points suffice to detect all edges, and the two scans plus graph traversal take \(O(n)\) arithmetic steps.

### 2. Exact full-retention probability

For \(N=n+1\), the old first-coordinate point in stratum \(i\) falls either into new stratum \(i\) or new stratum \(i+1\). Let \(B_i\in\{0,1\}\) be this new-stratum offset. The bits are independent, with
\[
\Pr(B_i=0)=\frac{n-i}{n+1},\qquad
\Pr(B_i=1)=\frac{i+1}{n+1}.
\]
A collision occurs precisely at adjacent ranks \(i,i+1\) when \((B_i,B_{i+1})=(1,0)\). Thus a coordinate is collision-free exactly for sequences \(0^k1^{n-k}\), \(k=0,\ldots,n\), whose total probability is
\[
\sum_{k=0}^n\frac{n!}{(n-k)!(n+1)^k}\,
\frac{n!}{k!(n+1)^{n-k}}
=\frac{2^n n!}{(n+1)^n}.
\]
The coordinate-wise bits for the other axis are independent and have the same distribution when indexed in second-coordinate stratum order. Hence the two-coordinate full-retention probability is the square shown above. Stirling yields the asymptotic equivalent.

### 3. Collision counts and a two-matching limit

The number \(E_n\) of conflicts along one coordinate is \(\sum_{i=0}^{n-2}\mathbf1\{B_i=1,B_{i+1}=0\}\). Its indicators are one-dependent, and
\[
\mathbb E E_n
=\sum_{j=1}^{n-1}\frac{j(n-j)}{(n+1)^2}
=\frac{n(n-1)}{6(n+1)}.
\]
Since bounded indicators are independent at separations exceeding one, \(\operatorname{Var}(E_n)=O(n)\). Hence \(E_n/n\to1/6\) in probability on each axis. The two axes give two independent random conflict-matchings with sizes \(m_{A,n},m_{B,n}\) satisfying \(2m_{A,n}/n,2m_{B,n}/n\to p=1/3\).

Conditional on these sizes, the second coordinate's uniformly random permutation relabels its matching uniformly over all matchings of \(m_{B,n}\) edges on the \(n\) old-point labels, independently of the first matching. Relabeling the first matching shows that conditional graph-shape statistics are those of two independent uniform partial matchings of the prescribed sizes.

### 4. Counting the odd-edge path components

For a union of two edge-coloured matchings, write \(m_A,m_B\) for its edge counts, and \(T_A,T_B\) for the number of nontrivial path components having an odd number of edges and starting and ending with an edge of colour \(A\), respectively \(B\). A path of \(e\) edges has matching number \(e/2\) if \(e\) is even and \((e+1)/2\) if \(e\) is odd. Every cycle has even length and matching number half its edge count. Consequently, with duplicate coloured edges counted twice as a two-cycle,
\[
\boxed{D_n=\frac{m_{A,n}+m_{B,n}+T_{A,n}+T_{B,n}}2.}
\]

For the uniform two-matching graph with both endpoint-incidence proportions tending to \(p\in(0,1)\), a uniformly chosen vertex is incident only to an \(A\)-edge with limiting probability \(p(1-p)\). Starting from such an \(A\)-only endpoint, follow its alternating path. The probability that its other endpoint is also \(A\)-only converges to
\[
(1-p)\sum_{k\ge0}p^{2k}=\frac1{1+p}.
\]
For each fixed path radius, these statements follow directly from sampling uniform partial matchings without replacement. Explorations of two independent uniformly sampled roots are asymptotically independent: for fixed radii, the chance their exposed vertex sets intersect tends to zero. These facts give a second-moment law of large numbers for bounded path explorations. The probability that a root exploration survives another \(2k\) alternating edges tends to at most \(p^{2k}\); letting \(k\) grow after the large-\(n\) limit makes the fraction of unclassified endpoints vanish. Every such path has exactly two \(A\)-only endpoints, so
\[
\frac{T_{A,n}}n\xrightarrow{\mathbb P}
\frac{p(1-p)}{2(1+p)},\qquad
\frac{T_{B,n}}n\xrightarrow{\mathbb P}
\frac{p(1-p)}{2(1+p)}.
\]
The double-match and cycle events do not invalidate the path identities; their finite-radius occurrence probability at a uniformly sampled root vanishes. Inserting these limits and \(m_{A,n}/n,m_{B,n}/n\to p/2\) into the exact decomposition gives
\[
\frac{D_n}{n}\xrightarrow{\mathbb P}
\frac p2+\frac{p(1-p)}{2(1+p)}
=\frac p{1+p}=\frac14.
\]
Therefore \(R_{n,n+1}/n\to3/4\). Boundedness gives convergence in mean.

## Verification

The accompanying Python standard-library checker `check_lhs.py` exhausts every pair of coordinate occupancy-bit patterns and every pairing of coordinate strata through \(n=4\), independently brute-forces the maximum independent set and checks the path/cycle computation. It also checks exact rational formulas for one-axis full retention and mean conflicts through \(n=9\), and 1,800 further randomized exact-rational new-grid comparisons across \(n=2,\ldots,10\). The checker reported 46,948 passed assertions. A seeded 350-repetition illustration at \(n=500\) gave deletion proportion \(0.24990\). None of these finite calculations substitutes for the limit proof.

To reproduce: `python3 check_lhs.py` from the directory containing the accompanying file; no package installations, other data files, or network access are required.

## Relationship to prior work

Liu, Li and Yang (2015) formulate non-integral Latin-hypercube extension as a maximum-independent-set problem and propose general and greedy algorithms. The present theorem uses that explicit optimization target, but isolates a structural two-coordinate matching decomposition and gives a stochastic sharp preservation fraction for the minimally enlarged target size. The inspected sections on graph transformation, algorithms, and conclusions in that work do not state these results. The 2017 follow-up by Yang, Liu and Li describes faster general extension with graph decomposition and bounds; its accessible abstract does not establish the present two-coordinate linear algorithm or the \(3/4\) limiting preservation law, but its full body remains a historical-priority risk. Classical results about sparse-graph matchings use distinct graph ensembles; the two-colour partial-matching limit is derived here explicitly for the extension model. The result does not assert originality of the independent-set formulation, random-matching techniques, or factorial/Stirling identities themselves.

## Limitations

The deterministic algorithm requires two coordinates and exact retention of original points; higher-dimensional conflict graphs can have larger degree. The probabilistic \(3/4\) constant assumes independently jittered uniform old strata, independent random relative coordinate ordering, and extension specifically from \(n\) to \(n+1\); it is not universal for optimized or dependent Latin hypercubes. The result is a convergence-in-probability law and exact no-deletion probability; no central-limit theorem or sharp finite-\(n\) error bound is claimed. The 2017 full-text comparison is incomplete, and independent scientific assessment has not been performed.

## References

1. Z.-Z. Liu, W. Li, and M. Yang, *Two General Extension Algorithms of Latin Hypercube Sampling*, Mathematical Problems in Engineering (2015), 450492, first published 2015-07-29. https://doi.org/10.1155/2015/450492
2. M. Yang, Z.-Z. Liu, and W. Li, *A fast general extension algorithm of Latin hypercube sampling*, Journal of Statistical Computation and Simulation 87 (2017), 3398–3411. https://doi.org/10.1080/00949655.2017.1368080
3. D. Gamarnik, T. Nowicki, and G. Świrszcz, *Maximum weight independent sets and matchings in sparse random graphs: Exact results using the local weak convergence method*, Random Structures & Algorithms 28 (2006), 76–106. https://doi.org/10.1002/rsa.20072
4. S. C. Hora, J. C. Helton and C. J. Sallaberry, *Extension of Latin Hypercube Samples With Correlated Variables* (2006), https://digital.library.unt.edu/ark:/67531/metadc885396/
