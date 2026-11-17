# Global distance-histogram rigidity for a metric circle with pendant arms

## Finding
Let \(G\) be a compact intrinsic metric graph formed by a circle of circumference \(c>0\) and \(k\ge1\) pendant segments of lengths \(a_1,\ldots,a_k>0\), all attached at one point of the circle and otherwise disjoint. Two independent points are sampled according to normalized arclength; let \(D\) be their shortest-path distance. The **full one-dimensional law of \(D\)** uniquely determines \(c\), \(k\), and the unordered arm-length multiset, even when lengths repeat or arm sums coincide with lengths or other sums. Thus the histogram is a complete isometry invariant *within this specified graph family*.

Writing \(L=c+\sum_i a_i\), \(h=c/2\), and \(f\) for the density of \(D\), the identification begins with
\[
f(0+)=\frac2L,\qquad f'(0+)=\frac{k(k+1)}{L^2}.
\]
The density has exactly one jump, of size \(2c/L^2\) downward, occurring at \(r=h\). Hence \(L\), \(k\), and \(c=2h\) are read directly from the law. Define \(R(r)=L^2f(r)/2-c\mathbf1_{(0,h)}(r)\). On \((0,\infty)\), its second distributional derivative obeys
\[
R''+2k\delta_h=-k\sum_i\delta_{a_i}+2\sum_i\delta_{a_i+h}+\sum_{i<j}\delta_{a_i+a_j}.\tag{1}
\]
The arms are then determined constructively from this finite signed measure.

## Assumptions and scope
All arm lengths and the circle circumference are strictly positive and finite; \(k\) is an unknown integer at least one. The graph is considered with its **intrinsic shortest-path metric**, not any Euclidean embedding, and the measure is uniform with respect to total arclength \(L\). A vertex of valence \(k+2\) is the unique attachment point. The conclusion is injectivity *within this class*; it makes no claim that arbitrary metric graphs or their topologies are identified by the same histogram. The one-dimensional histogram is known exactly, not estimated from finitely many distances.

For a real \(x\), let \(x_+=\max\{x,0\}\). All formulas for the density are interpreted at continuity points and by one-sided limits at its finite set of breakpoints; the distribution of \(D\) has no atoms.

## Proof
**Distance-density decomposition.** The circle contains length \(c\). The geodesic distance between two independent uniform circle points is uniform on \([0,c/2]\), so its contribution to the *unconditional* density is \(2c/L^2\) on \((0,h)\) and zero outside it. The two orientations of a circle/arm pair contribute a convolution of the arm coordinate \([0,a_i]\) with distance-to-attachment on the circle. The latter pushes unnormalized circle arclength to twice Lebesgue measure on \([0,h]\). Same-arm pairs contribute the usual triangular difference law, while distinct-arm pairs contribute a sum of independent uniform coordinates.

More precisely, for \(r>0\) away from breakpoints, put \(g(r)=L^2f(r)/2\). Direct integration over all ordered point pairs gives
\[
\begin{aligned}
g(r)={}&c\mathbf1_{(0,h)}(r)+\sum_{i=1}^k(a_i-r)_+\\
&+2\sum_{i=1}^k\big[r_+-(r-a_i)_+-(r-h)_++(r-a_i-h)_+\big]\\
&+\sum_{i<j}\big[r_+-(r-a_i)_+-(r-a_j)_++(r-a_i-a_j)_+\big].\tag{2}
\end{aligned}
\]
Every term after the indicator is continuous. Consequently the indicator creates the sole jump of \(g\), located at \(h\), of downward size \(c\); the jump of \(f\) is \(2c/L^2\). For sufficiently small positive \(r\), smaller than \(h\) and all \(a_i\), equation (2) reduces exactly to \(g(r)=L+\tfrac12k(k+1)r\), proving both displayed near-zero formulas. In particular \(L=2/f(0+)\) and \(k\) is uniquely determined by the strictly increasing integer function \(k\mapsto k(k+1)\). Then the jump location gives \(c=2h\).

**Signed second derivative.** Subtract the known discontinuous term and use \(\tfrac{d^2}{dr^2}(r-b)_+=\delta_b\) for \(b>0\), in the distributional sense on \((0,\infty)\). From (2), every arm \(a_i\) contributes \(+1-2-(k-1)=-k\) at \(a_i\); the circle/arm term contributes \(+2\) at \(a_i+h\) and \(-2k\) at \(h\); each unordered pair of distinct arms contributes \(+1\) at its sum. This establishes (1), with all coincident atoms combined algebraically.

**Constructive reconstruction without genericity assumptions.** Let \(\nu=R''+2k\delta_h\). Initially no arms have been recovered. Suppose a multiset \(B\) of arms is already recovered; from \(\nu\) subtract its completely known terms: \(-k\sum_{b\in B}\delta_b+2\sum_{b\in B}\delta_{b+h}+\sum_{\{b,b'\}\subseteq_{\mathrm{ind}}B}\delta_{b+b'}\). Let \(U\) be the still-unknown multiset. The residual equals
\[
-k\sum_{u\in U}\delta_u+2\sum_{u\in U}\delta_{u+h}
+\sum_{\{u,u'\}\subseteq U}\delta_{u+u'}
+\sum_{b\in B,u\in U}\delta_{b+u}.\tag{3}
\]
All lengths and \(h\) are strictly positive. If \(u_0\) is the minimum element of \(U\), no positive-shift or pair-sum term in (3) is supported at or below \(u_0\). Therefore the *least* atom in the residual is at \(u_0\), with coefficient precisely \(-k m\), where \(m\) is its multiplicity among the remaining arms. Read off \(u_0,m\), add \(m\) copies to \(B\), and repeat. At most \(k\) nonempty steps recover all arms; there is no reliance on separated breakpoints, generic lengths, or an exhaustive search. The circle and multiset of arms determine the intrinsic graph up to isometry. \(\square\)

## Verification
The independent exact-arithmetic checker in `verify.py` tests the signed-atom equation and peeling algorithm on 960 rational configurations with between one and eight arms, including repeated and coincident breakpoint values. It also checks the two near-zero density formulas, three explicit jump-collision cases, and seven numerical CDF thresholds against 350,000 directly simulated independent arclength-uniform pairs. Reported execution: `VERIFY_OK exact_reconstructions=960continuity_collision_cases=3 direct_pairs=350000max_cdf_discrepancy=0.000782`. These are finite reproducibility checks, not a substitute for the distributional proof.

## Relationship to prior work
Lecci–Rinaldo–Wasserman (2013) recover embedded metric-graph topology from point clouds, a much richer data type than the one-dimensional distribution here. Mémoli–Needham (2018; revised 2022), especially their Section 4, develop local/global shape distributions on metric graphs: their sphere/circle characterization and local-profile results do not give full parameter recovery for the single-loop, multiply-branched family using only the global histogram. Garijo–Márquez–Silveira (2023) and Baptista–Kennedy–Mugnolo (2024) treat mean distance on metric graphs; one averaged scalar cannot supply the full inverse argument. The present result relies on a discontinuity caused specifically by the circle and on signed-atom peeling. Related tree/star reconstruction has a different, entirely continuous density and does not itself prove this result for spaces with nontrivial first homology.

## Limitations
The theorem is restricted to one circle with all arms attached at a **single** common point. It does not settle metric cactus graphs with attachment points distributed along a cycle, arbitrary unicyclic graphs, or stability of the inverse procedure under noise. In practice, density jumps and distributional derivatives are sensitive to finite-sample error. The theorem claims exact injectivity, not a stable estimation algorithm or a characterization among *all* graph topologies. Historical priority requires further independent assessment.

## References
1. F. Lecci, A. Rinaldo, L. Wasserman, *Statistical Analysis of Metric Graph Reconstruction*, arXiv:1305.1212, first posted 2013-05-06; Journal of Machine Learning Research 15 (2014), 3425–3446. https://arxiv.org/abs/1305.1212
2. F. Mémoli, T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646, first posted 2018-10-23; Studies in Applied Mathematics 149 (2022), 943–1001. https://arxiv.org/abs/1810.09646
3. D. Garijo, A. Márquez, R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics 78 (2023), article 139. https://doi.org/10.1007/s00025-023-01902-w
4. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean Distance on Metric Graphs*, Journal of Geometric Analysis 34 (2024), article 137. https://doi.org/10.1007/s12220-024-01574-0
