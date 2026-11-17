# A sharp metric-to-\(L^1\) Poincaré transition on unbalanced complete tripartite graphs

## Finding
For all integers \(a\ge3\) and \(b\ge2\), consider the unweighted complete tripartite graph \(G=K_{a,a,b}\), with two classes of \(a\) vertices and one of \(b\) vertices. For a map \(f\) from its vertices into any metric space, define its exponent-one Poincaré ratio as the mean pairwise target distance over **distinct unordered vertex pairs**, divided by the mean target distance over undirected graph edges (when the denominator is positive). Let \(\Gamma_{\mathrm{met}}\) be the sharp supremum over all metric targets, and \(\Gamma_{L^1}\) the sharp supremum over all real \(L^1\) targets. Put \(N=2a+b\) and \(P=\binom N2\). Then
\[
\boxed{\Gamma_{\mathrm{met}}(K_{a,a,b})=\max\left\{\frac{a+2b}{2a+b},\frac{3a^2+2ab+b^2-2a-b}{\binom{2a+b}{2}}\right\}.}
\]
The second branch is strictly larger when \(b<4a-3\), the first is strictly larger when \(b>4a-3\), and the two coincide exactly at \(b=4a-3\). In addition, the **target-class transition** is exact:
\[
\boxed{\Gamma_{L^1}(K_{a,a,b})<\Gamma_{\mathrm{met}}(K_{a,a,b})\quad\Longleftrightarrow\quad b<4a-3.}
\]
For \(b\ge4a-3\), both constants equal \((a+2b)/(2a+b)\). When \(b<4a-3\), a norming metric is the graph's shortest-path metric, and no real \(L^1\) target attains its sharp value. For \(b>4a-3\), a norming \(L^1\) metric collapses both \(a\)-vertex classes to one center and places the \(b\) remaining vertices at the coordinate unit vectors; at equality \(b=4a-3\) both the shortest-path and collapsed-star metrics are sharp.

Among pseudometrics invariant under all permutations inside the three classes and interchanging the two equal classes, the normalized maximizer is unique, up to scale, in each strict regime. At the threshold there is a one-parameter family of invariant maximizers interpolating between these two geometries. No uniqueness claim is made for unsymmetrized maximizing metrics.

## Assumptions and scope
The graph is simple and has \(N=2a+b\) labeled vertices and \(E=a^2+2ab\) undirected edges. Target metrics may identify vertices, since an arbitrary map need not be injective. The denominator is \(E^{-1}\sum_{uv\in E}d(f(u),f(v))\); the numerator is \(P^{-1}\sum_{u<v}d(f(u),f(v))\). In particular, this is the distinct-unordered-pair normalization, not the ordered-all-pairs normalization sometimes used for nonlinear spectral gaps. A pseudometric on the vertex set is realizable by mapping the vertices into a true metric space after identifying zero-distance points. All \(L^1\) spaces and maps here are real, with arbitrary underlying measure spaces and dimensions.

## Proof
**1. Symmetrization and metric reduction.** For any target map, pull back its distances to a finite pseudometric \(d\) on the vertex set. Average \(d\) over all permutations inside each part and the interchange of the equal parts. The result is again a pseudometric and preserves both the total distance over all pairs and the total distance over graph edges. Thus it preserves the ratio. Every invariant pseudometric has four parameters: \(x\), the distance between distinct vertices in either equal part; \(y\), the distance between distinct vertices in the size-\(b\) part; \(z\), the distance across the two equal parts; and \(w\), the distance between a size-\(a\) part and the size-\(b\) part. Triangle inequalities give
\[
0\le z\le2w,\qquad 0\le x\le2\min\{z,w\},\qquad0\le y\le2w.
\]
Conversely, these conditions are sufficient for the four-parameter array to be a pseudometric: all triangle types have at most two different orbit distances, and their nontrivial constraints are precisely those displayed. If the edge sum is positive then \(w>0\); scale to \(w=1\), and write \(t=z\in[0,2]\).

**2. Exact optimization.** The edge-distance sum is \(a^2t+2ab\). The sum over all unordered vertex pairs is
\[
a^2t+2ab+a(a-1)x+\binom b2 y.
\]
Since \(a,b\ge2\), for fixed \(t\) the objective increases strictly with \(x\) and \(y\). Hence any invariant maximizer must have \(x=2\min\{t,1\}\) and \(y=2\), and its ratio becomes
\[
R(t)=\frac{a^2+2ab}{P}\left[1+\frac{2a(a-1)\min\{t,1\}+b(b-1)}{a^2t+2ab}\right],\quad 0\le t\le2.
\]
On \([0,1]\) the derivative of the fraction has the sign of \(4a-b-3\) (its numerator after clearing the positive squared denominator is \(a^2b(4a-b-3)\)). On \([1,2]\) the fraction is strictly decreasing. Thus its maximum occurs at \(t=1\) when \(b<4a-3\), at \(t=0\) when \(b>4a-3\), and at every \(t\in[0,1]\) at equality. Direct substitution gives
\[
R(0)=\frac{a+2b}{2a+b},\qquad R(1)=\frac{3a^2+2ab+b^2-2a-b}{P}.
\]
The \(t=1\) metric has every cross-part distance one and every distinct same-part distance two, precisely the shortest-path metric of \(G\). For \(t=0\), all \(2a\) vertices of the first two classes are identified with one point, and the \(b\) other vertices have pairwise distance two and distance one to that center. These are feasible and attain their respective branches. This establishes the metric formula and all invariant maximizing geometries.

**3. An \(L^1\) obstruction in the noncollapsed regime.** Restrict any real \(L^1\) pseudometric to the union of the two equal classes, each with \(a\) vertices. Let \(W\) be its average across the \(a^2\) cross-class pairs and \(U\) its average over the \(a(a-1)\) within-class pairs. Every cut \(S\), containing \(u\) vertices from the first class and \(v\) from the second, satisfies the exact identity
\[
W(\delta_S)-\frac{a-1}{a}U(\delta_S)=\frac{(u-v)^2}{a^2}\ge0.
\]
Because any finite collection of real \(L^1\) distances is a nonnegative integral of cut semimetrics (apply the scalar layer-cake formula coordinatewise), every real \(L^1\) pseudometric satisfies \(W\ge(a-1)U/a\). The shortest-path metric restricted to these two parts has \(W=1\), \(U=2\), which violates the inequality for every \(a\ge3\). Hence it is not a real \(L^1\) metric.

For \(b<4a-3\), suppose the \(L^1\) sharp constant equaled the metric one. Normalize all nonzero candidate \(L^1\) pseudometrics by requiring their graph-edge sum to be one. Each edge distance is then at most one; all other distances are at most two by connectedness and triangle inequalities, making the feasible set bounded. The real \(L^1\) semimetric cone on a finite vertex set is the **closed, finitely generated cut cone**. Therefore an optimal \(L^1\) pseudometric exists. Its automorphism average is again \(L^1\) and preserves the ratio. The strict \(b<4a-3\) invariant-maximizer classification forces this average to be a positive multiple of the shortest-path metric, contradicting the displayed cut inequality. This proves \(\Gamma_{L^1}<\Gamma_{\mathrm{met}}\) in that regime.

**4. Coincidence in the collapsed regime.** For \(b\ge4a-3\), send all vertices in the two equal classes to \(0\in\ell_1^b\), and send the \(b\) remaining vertices bijectively to the standard coordinate unit vectors. This is exactly the \(t=0\) collapsed-star metric and attains \((a+2b)/(2a+b)\), the already proved unrestricted metric upper bound. Hence \(\Gamma_{L^1}=\Gamma_{\mathrm{met}}\). At the threshold the \(t=0\) and \(t=1\) witnesses coexist; both are metric extremizers but only the former is required to be \(L^1\).

## Verification
The proof is uniform for all integers \(a\ge3,b\ge2\). The standalone `metric_tripartite_checker.py` implements the exact formula with rational arithmetic, checks all sampled invariant-orbit parameters for \(2\le a\le8\) and \(2\le b\le27\), enumerates every block-count cut triple for selected small sizes, and verifies the exact two-block cut identity. It reported `TRIPARTITE_CHECK_OK orbit_points=4550 cut_count_vectors=4408 l1_cut_identities=1482`. The finite checks are supplementary and do not establish the universal claim; the analytic symmetrization, triangle constraints, derivative sign, and finite cut-cone argument do.

## Relationship to prior work
Polavarapu, arXiv:2611.05649v1, proves cotype-based nonlinear Poincaré **upper bounds** for regular graphs and Banach targets and uses a different pair-normalization convention. Its inspected introduction and main theorem do not determine exact arbitrary-metric constants for the nonregular \(K_{a,a,b}\), or the sharp \(L^1\) coincidence threshold. Altschuler–Dodos–Tikhomirov–Tyros, arXiv:2509.25489v1, study general metric Poincaré inequalities and random regular graphs; their inspected main statements likewise do not imply this graph-specific exact phase diagram.

Published research on the same graph family has an exact **two-summing/free two-convex Banach-lattice** edge-difference norm with screening at \(b\ge2a+2\). Its full stated theorem and proof concern maximization of a trace-square-root Laplacian objective, not the present ratio of two linear distance functionals; its threshold differs from \(4a-3\). Published equal-block multipartite results identify an \(L^1\) snowflake distortion and a balanced-cut identity. Their exact fixed-metric embedding problem does not establish this unbalanced tripartite metric Poincaré formula or the target-class transition. Earlier sharp bipartite Poincaré and clique-join examples also involve different graphs and do not imply the present sharp two-branch optimization. The cut decomposition and graph-distance embedding techniques used here are classical and are not claimed as new.

## Limitations
The exact formula requires the two smaller classes to have equal cardinality and the third to have at least two vertices; the strict \(L^1\) gap conclusion is proved for \(a\ge3\), not \(a=2\). No exact \(L^1\) constant below the coincidence threshold is claimed, only a strict inequality with the unrestricted metric optimum. No classification of all nonsymmetric extremizing pseudometrics is claimed. The source literature and searches do not constitute a proof of universal bibliographic novelty; equivalent older graph flow/cut or metric spectral-gap formulations remain a publication-priority risk. Independent mathematical validation has not been performed.

## References
1. A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1, first posted 3 November 2026, https://arxiv.org/html/2611.05649v1.
2. D. J. Altschuler, P. Dodos, K. Tikhomirov and K. Tyros, *Metric Poincaré inequalities for graphs*, arXiv:2509.25489v1, first posted 29 September 2025, https://arxiv.org/html/2509.25489v1.
3. *Sharp two-summing screening in three-cluster graph-edge free lattices*, published mathematical research, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-two-summing-screening-in-three-cluster-graph-edge-free-lat--9bddcd86cf8d.
4. *Sharp \(\ell_1\) snowflake threshold and cut rigidity for equal-block multipartite metrics*, published mathematical research, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-ell-1-snowflake-threshold-and-cut-rigidity-for-equal-block--8c35bbb3adef.
5. A. Naor, *Comparison of metric spectral gaps*, arXiv:1308.2851v1, https://arxiv.org/abs/1308.2851.
