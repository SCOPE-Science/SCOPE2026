# A spatially marked Poisson field of microscopic pairs in uniform permutation plots

## Finding

Let \(\pi_n\) be uniformly distributed over the permutations of \(\{1,\ldots,n\}\). For integers \(h,k\ge1\) and a sign \(s\in\{-1,+1\}\), define the random finite point measure
\[
\Xi_n^{h,k,s}=\sum_{i=1}^{n-h}\mathbf1\{\pi_n(i+h)-\pi_n(i)=sk\}\,\delta_{(i/n,\,\pi_n(i)/n)}.
\]
**Theorem.** For every fixed finite collection of distinct marks \((h,k,s)\), the associated point measures converge jointly, in the weak topology of finite point measures on \([0,1]^2\), to *independent homogeneous Poisson point processes*, each having intensity equal to two-dimensional Lebesgue measure. Thus the total counts at different signed displacement marks converge to independent \(\operatorname{Poisson}(1)\) variables. The same applies jointly to counts in any fixed collection of marked spatial regions whose boundaries have zero Lebesgue area.

For a finite set \(B\subset\mathbb N_{\ge1}^2\), the total number of unordered plot-point pairs whose positive horizontal and absolute vertical displacements belong to \(B\) converges to \(\operatorname{Poisson}(2|B|)\). These are finite-mark conclusions: the set \(B\) is fixed as \(n\to\infty\).

Two useful consequences concern the minimum Manhattan and maximum-coordinate distances between distinct plot points:
\[
D_{1,n}=\min_{1\le i<j\le n}\left(j-i+|\pi_n(j)-\pi_n(i)|\right),\qquad
D_{\infty,n}=\min_{1\le i<j\le n}\max\left(j-i,|\pi_n(j)-\pi_n(i)|\right).
\]
For all fixed integers \(d,r\ge1\), writing
\[
J_{d,r}=\sum_{h=1}^{r}\max\{0,\min(r,d+1-h)\},
\]
we obtain the **joint**, not just marginal, limiting law
\[
\lim_{n\to\infty}\Pr(D_{1,n}\ge d+2,\ D_{\infty,n}>r)
=\exp\{-d(d+1)-2r^2+2J_{d,r}\}.
\]
In particular \(\Pr(D_{\infty,n}>r)\to e^{-2r^2}\) and \(\Pr(D_{1,n}\ge d+2)\to e^{-d(d+1)}\). The latter marginal was previously known; the complete marked spatial field and the joint multi-metric law are the conclusions assessed here.

There is also a location-and-direction corollary. For an integer \(m\ge2\), condition on \(D_{1,n}=m\), and choose uniformly among the plot-point pairs achieving that distance, independently of the permutation. The chosen pair's signed displacement \((h,k,s)\), with \(h+k=m\), converges to the uniform distribution on the \(2(m-1)\) possible marks; its anchor \((i/n,\pi_n(i)/n)\) converges to a uniform point on \([0,1]^2\), independent of the mark.

## Assumptions and scope

The permutation is uniform, the mark coordinates \(h,k\) are positive *fixed* integers, and \(s\) records the sign of the vertical displacement from the smaller to the larger horizontal coordinate. The spatial anchor is always the plot point with smaller horizontal coordinate. All point-measure statements concern finite sets of marks and weak convergence on the compact square. In the distance consequences the integer thresholds are held fixed. The theorem does not assert uniform error estimates for growing marks, arbitrary nonuniform permutations, or global independence among all finite-size displacement events.

## Proof

**1. Exact one-mark intensity.** Each ordered pair of distinct permutation values is uniformly distributed over \(n(n-1)\) possibilities. For any \(1\le h,k<n\), either sign \(s\) therefore has
\[
\mathbb E\,\Xi_n^{h,k,s}([0,1]^2)
=(n-h)\frac{n-k}{n(n-1)}\longrightarrow1.
\]
For a rectangle \(R\subset(0,1)^2\) with negligible boundary, its expected count is
\[
\frac{\#\{(i,a):\ (i/n,a/n)\in R,\ 1\le i\le n-h,\ 1\le a+sk\le n\}}{(n)_2}
\longrightarrow |R|,
\]
where \((n)_v=n(n-1)\cdots(n-v+1)\) and \(|R|\) is the rectangle's area.

**2. Factorial moments and the overlap bound.** Fix a positive integer \(t\) and \(t\) labelled, distinct pair events, each prescribing a signed bounded displacement and an anchor in one of finitely many boundary-null rectangles. In a mixed factorial moment, identical pair events are never selected twice. Events with the same unordered horizontal endpoint pair but conflicting marks are impossible.

Make a graph whose vertices are the horizontal indices appearing in the selected events and whose edges represent those events. Suppose this graph has \(v\) vertices and \(c\) connected components. Because the horizontal offsets are drawn from a fixed finite set, specifying one base horizontal index per component determines all other horizontal indices up to finitely many possibilities: there are \(O(n^c)\) horizontal choices. The signed vertical differences likewise determine all values in each connected component once one base value has been chosen, giving at most \(O(n^c)\) allowed vertical assignments. Any consistent assignment to \(v\) distinct indices has probability exactly \(1/(n)_v\), so all configurations of the given overlap type have total contribution \(O(n^{2c-v})\). Each component containing an edge has at least two vertices. If some component contains at least three vertices, then \(v\ge2c+1\), and its contribution is \(O(n^{-1})\). If all components have two vertices, no repeated horizontal pair can contribute, and we have precisely \(t\) disjoint pair events.

For these disjoint pairs, the \(t\) anchored position–value choices range over \(n^{2t}\prod_{j=1}^t|R_j|+o(n^{2t})\) configurations. The restrictions that all \(2t\) horizontal indices and all \(2t\) vertical values be distinct exclude only \(O(n^{2t-1})\) configurations, because every displacement is fixed. Each remaining choice has probability \(1/(n)_{2t}\). Consequently the mixed factorial moment converges to \(\prod_{j=1}^t|R_j|\), counting repeated regions with their appropriate multiplicities. This is exactly the mixed factorial-moment formula for independent unit-intensity Poisson measures on the marked rectangles.

**3. Point-process convergence.** The preceding calculation applies to arbitrary disjoint boundary-null rectangles, including rectangles carrying distinct marks. The factorial moments determine the multivariate Poisson law, and the expected total number of points for each fixed mark stays bounded. Tightness of the finite-mark point measures on the compact square, together with the rectangle-count characterization, proves their joint convergence to independent Poisson processes. This completes the theorem.

**4. Derived geometric laws.** An unordered pair has the unique displacement mark \((h,k,s)\) with \(h=j-i>0\), \(k=|\pi_n(j)-\pi_n(i)|>0\), and \(s\in\{-1,+1\}\). Among positive integer offsets, the forbidden triangle \(h+k\le d+1\) has \(d(d+1)/2\) cells; the forbidden square \(h,k\le r\) has \(r^2\) cells; their intersection has \(J_{d,r}\) cells. Each cell has two independent signed limiting Poisson counts of mean one. The probability that their union is empty therefore tends to the displayed exponential. This also establishes the separate marginal laws without asserting novelty for the already-known Manhattan marginal.

Finally, every Manhattan-distance shell \(h+k=m\) has \(2(m-1)\) signed marks. All its limiting point processes have the same unit intensity, and they are independent of processes on lower-distance shells. Conditional on the lower shells being empty and shell \(m\) being nonempty, a point sampled uniformly among the pooled shell points therefore has a uniform mark and uniform spatial anchor, independently. The finite-mark convergence just proved gives this conditional conclusion for each fixed \(m\). Its conditioning event has positive limiting probability, namely \(e^{-(m-2)(m-1)}-e^{-m(m-1)}\).

## Verification

Running `python3 verify_local_pairs.py` in the directory containing the standalone checker reports 364 passed exact checks. The checker exhaustively enumerates all permutations with \(3\le n\le8\), verifies every single-mark mean for offsets up to three in both signs, and independently reconstructs mixed second factorial moments via consistent injective value assignments on the selected horizontal vertices. It also checks the integer geometry of the triangle/square intersection and exact finite-size mean bounds. These checks test the event definitions and enumerations; the point-process limit is proved analytically, not by the finite checks.

## Relationship to prior work

Diaconis, Evans and Graham (2013) established an exact distributional correspondence for increasing adjacent consecutive-value pairs, the special signed mark \((1,1,+1)\), including the set of such positions. Crane and DeSalvo (first public preprint 2015) treat ordinal-pattern indicators and Poisson approximation; fixing a *numerical value gap* and a *two-dimensional spatial anchor* is a different event. Bevan, Homberger and Tenner (first public preprint 2016) characterize prolific permutations via their minimum Manhattan plot-point distance. Blackburn, Homberger and Winkler (first public preprint 2017) prove the limiting Manhattan-distance law and a Poisson limit for the **aggregate** number of close pairs. Therefore our Manhattan marginal is covered by that later paper, whereas none of these specifically states joint independent spatial Poisson fields for every fixed signed displacement, the paired Manhattan/max-coordinate law, or the conditional uniform mark and anchor of a nearest pair.

The exact single-mark Poisson law for adjacent consecutive values is also present as an ingredient of other permutation deletion-statistic results. Such a scalar projection does not determine the multivariate marked spatial law; bibliographic priority for the latter remains subject to further independent review.

## Limitations

The proof gives fixed-mark weak convergence and corresponding fixed-threshold statements, not a uniform rate in the mark size or quantitative point-process total variation. The finite checker is corroborative, not a proof of limiting independence. The already-published minimum Manhattan distance marginal and single-succession statistics are excluded from the novelty claim. Unindexed or inaccessible more general Poisson theorems could contain the full marked statement, and no independent expert review has been performed.

## References

1. P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822, publicly dated 2013-08-01. https://statistics.berkeley.edu/tech-reports/822
2. H. Crane, S. DeSalvo, *Pattern avoidance for random permutations*, arXiv:1509.07941, first posted 2015-09-26. https://arxiv.org/abs/1509.07941
3. D. Bevan, C. Homberger, B. E. Tenner, *Prolific permutations and permuted packings: downsets containing many large patterns*, arXiv:1608.06931, first posted 2016-08-24. https://arxiv.org/abs/1608.06931
4. S. R. Blackburn, C. Homberger, P. Winkler, *The minimum Manhattan distance and minimum jump of permutations*, arXiv:1706.01557, first posted 2017-06-05. https://arxiv.org/abs/1706.01557
