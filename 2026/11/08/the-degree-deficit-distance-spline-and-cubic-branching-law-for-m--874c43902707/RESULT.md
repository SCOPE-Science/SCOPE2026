# The degree-deficit distance spline and cubic branching law for metric trees

## Finding

Let \(T\) be any finite, connected metric tree with at least one edge, all edge lengths strictly positive, vertex set \(V\), total arclength \(L>0\), and shortest-path metric \(d\). Let \(X,Y\) be independent uniformly arclength-distributed points of \(T\), and set \(D=d(X,Y)\). Write \(b_v=2-\deg(v)\), \(Q=\sum_{v\in V}\deg(v)^2-4|E|\), and \((z)_+=\max\{z,0\}\). Then for every \(r\ge0\), the complete distance distribution is the explicit signed quadratic spline

\[
\Pr(D\le r)=\frac{2r}{L}+\frac{Qr^2}{2L^2}
+\frac{1}{2L^2}\sum_{\substack{v,w\in V\\v\ne w}}
 b_vb_w\big(r-d(v,w)\big)_+^2.
\]

It has a continuous piecewise-affine density

\[
f(r)=\frac2L+\frac{Qr}{L^2}+\frac1{L^2}
\sum_{\substack{v,w\in V\\v\ne w}}b_vb_w\big(r-d(v,w)\big)_+.
\]

In particular the slope jump of \(f\) at a positive radius \(t\) equals
\[
\Delta f'(t)=L^{-2}\!\sum_{\substack{v\ne w\\d(v,w)=t}}b_vb_w.
\]
These are *signed* contributions: at coincident distances they may cancel. Artificial degree-two subdivisions have \(b_v=0\) and do not alter the formula.

For each branching vertex \(v\) of degree at least three, let \(L_{v,i}\) be the total lengths of the distinct branches of \(T\setminus\{v\}\), including the open incident edge leading into each branch. Define the nonnegative cubic branching mass
\[
\mathcal B(T)=\sum_{v:\deg(v)\ge3}\ \sum_{i<j<k} L_{v,i}L_{v,j}L_{v,k}.
\]
Then the *same distribution* has mean
\[
\boxed{\mathbb E[D]=\frac L3-\frac{2\mathcal B(T)}{L^2}.}
\]
Consequently \(\mathbb E[D]\le L/3\), with equality **exactly when** \(T\) is isometric to a closed interval. For every genuine branching tree the inequality is strict.

## Assumptions and scope

Every graph in the theorem is finite, connected, acyclic, and equipped with positive real edge lengths; no rationality, general-position, or distinct-distance assumptions are imposed. The probability measure is normalized one-dimensional Hausdorff/arclength measure. Vertex weights \(b_v\) refer to graph degree including any degree-two subdivisions. An empty sum is zero. The CDF expression is valid for every nonnegative real radius (including radii beyond the diameter, where it equals one); the displayed density is the continuous representative, so its derivative jumps are interpreted as one-sided slopes. The term \(\mathcal B(T)\) has units of length cubed.

## Proof

**1. Radial counting and full spline.** For a point \(x\) strictly inside an edge and outside a set of arclength measure zero, the number of points at distance \(r\) from \(x\) is initially two. Each time an outward distance wave crosses a vertex \(v\), its number of active tips changes by \(\deg(v)-2=-b_v\). Thus, for almost all \(r>0\), the derivative of the length of the ball around \(x\) is
\[
2-\sum_{v\in V}b_v\mathbf1_{\{d(x,v)<r\}}.
\]
At a vertex \(v\), the analogous wave starts with \(\deg(v)\) tips. Integrating its radial tip count gives the exact length of its ball:
\[
H_v(r)=\deg(v)r-\sum_{w\ne v}b_w\big(r-d(v,w)\big)_+.
\]
Fubini's theorem now gives the density of \(D\):
\[
\begin{aligned}
L^2 f(r)&=\int_T\!\left(2-\sum_vb_v\mathbf1_{\{d(x,v)<r\}}\right)dx\\
&=2L-\sum_v b_vH_v(r)\\
&=2L+Qr+\sum_{v\ne w}b_vb_w\big(r-d(v,w)\big)_+,
\end{aligned}
\]
where \(-\sum_v b_v\deg(v)=\sum_v\deg(v)^2-4|E|=Q\). Integrating from \(0\), using \(\Pr(D=0)=0\), yields the CDF and proves the slope-jump statement, including all colliding vertex distances.

**2. Degree-deficit separator identity.** For every component \(C\) produced by cutting one tree edge, the sum of \(b_v\) over the vertices of \(C\) is exactly one: indeed, the sum of original degrees over \(C\) is twice its number of internal edges plus one outgoing edge, so \(\sum_{v\in C}(2-\deg v)=1\). Therefore, for any one edge, any two edges, or any three edges lying on a common simple tree path, the signed sum \(\sum_{v,w}b_vb_w\) over ordered vertex pairs whose unique path traverses all specified edges is two (the extreme components each have deficit mass one). If three distinct edges do not lie on one path, this sum is zero, because no vertex-pair path can traverse all three.

**3. Cubic identity.** Write \(S_k=\sum_{v,w}b_vb_w d(v,w)^k\). Express each vertex distance as the sum of edge lengths on its unique path, then expand the first three powers and apply the separator identity. Every monomial involving at most two distinct edges has multiplicity two. A product of three distinct edge lengths contributes to \(S_3\) with coefficient twelve exactly when those three edges lie on one path, and contributes zero otherwise. It follows that
\[
S_1=2L,\qquad S_2=2L^2,\qquad S_3=2L^3-12\mathcal B(T),
\]
because every non-collinear three-edge selection has a unique median branching vertex whose three distinct branches contain the three edges. Grouping their edge-length products over this median gives precisely \(\mathcal B(T)\).

**4. Mean-distance identity.** The Laplace transform of the already proved density is, for \(s>0\),
\[
\mathbb E[e^{-sD}]=\frac{2}{Ls}+\frac{\sum_{v,w}b_vb_we^{-s d(v,w)}-4}{L^2s^2}.
\]
Here \(\sum_vb_v=2\) and \(Q-\sum_vb_v^2=-4\). Taylor expanding the finite exponential sum and applying the three identities above cancels the apparent poles, gives constant term one, and gives coefficient \(-S_3/(6L^2)\) at \(s\). Since \(D\) is bounded, its negative first moment is this coefficient. Hence
\(\mathbb E[D]=S_3/(6L^2)=L/3-2\mathcal B(T)/L^2\).
Every summand defining \(\mathcal B(T)\) is nonnegative; a degree-three-or-more vertex has three branches of strictly positive length, forcing strict positivity. Conversely a finite connected tree without branching is a path. This proves equality characterization.

## Verification

The standalone Python program `verify_tree_spline.py` uses exact rational arithmetic, not floating-point tolerances. It computes the CDF independently by partitioning ordered pairs of points into same-edge and distinct-edge rectangles and integrating their shortest-path inequalities. The independent edge-pair result is compared at 10,120 rational test radii with the degree-deficit spline. It also checks the first three signed vertex-distance moment identities and the branching cubic formula for 116 weighted trees (including paths, stars, degree-two subdivisions, repeated lengths and randomized branching). The successful output was:

`EXACT_TREE_SPLINE_OK cases=116 exact_cdf_evaluations=10120 exact_weighted_moment_orders=3 mean_distance_branching_identities=116`

The finite tests are not a proof for all trees; the analytical argument above supplies that proof. To repeat: run `python3 verify_tree_spline.py` with the Python standard library.

## Relationship to prior work

Zmazek and Žerovnik (2007) study weighted-tree Hosoya–Wiener polynomials for distances between graph vertices, a distinct discrete sampling model. Their abstract and bibliographic record were accessible, but their complete text was not inspected. Bose and coauthors (2013) treat farthest-point geometry for the continuum along network edges, not the sampled pair-distance law. Mémoli and Needham (first public preprint October 23, 2018) establish the small-radius \(2r/L+Qr^2/(2L^2)\) law (their Lemma 6.6), show nonisometric trees can share a global distance histogram (Example 6.12), and analyze local-distance injectivity. Thus the first two spline terms and global noninjectivity are acknowledged as prior knowledge. Garijo, Márquez and Silveira (2023) give exact computational methods for the **mean** continuous geodesic distance, including trees, but do not state the signed all-radii CDF spline and its cubic branching identity in the inspected sections. The proposed contribution is precisely that global spline/branching law, not the existence of continuous distance histograms or mean-distance algorithms. Earlier implicit derivations or independently discovered formulas remain a historical-priority risk.

## Limitations

The theorem concerns finite acyclic metric networks. A general metric graph with cycles has multiple geodesics and need not satisfy this signed tree spline. The global distance distribution does **not** uniquely identify every finite metric tree: known counterexamples exist, so no general inverse-isometry claim is made. Zero-length edges and nonuniform sampling are outside scope. Signed slope jumps can cancel when vertex-pair distances coincide. No noisy-data reconstruction, statistical stability or computational optimality is claimed. The literature comparison is not an independent historical-priority certification.

## References

1. B. Zmazek and J. Žerovnik, *The Hosoya-Wiener Polynomial of Weighted Trees*, Croatica Chemica Acta 80 (2007), 75–80, published 2007-03-11, https://hrcak.srce.hr/12827.
2. P. Bose, K. Dannies, J. De Carufel et al., *Network Farthest-Point Diagrams*, Journal of Computational Geometry 4 (2013), 182–211, preprint https://arxiv.org/abs/1304.1909, DOI 10.20382/jocg.v4i1a8.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, arXiv:1810.09646 (first posted 2018-10-23), particularly Lemma 6.6 and Example 6.12, https://arxiv.org/abs/1810.09646.
4. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics 78 (2023), article 139, https://doi.org/10.1007/s00025-023-01902-w.
