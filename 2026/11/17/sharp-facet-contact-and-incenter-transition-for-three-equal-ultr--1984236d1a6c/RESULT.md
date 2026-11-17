# Sharp facet-contact and incenter transition for three equal ultrametric clusters

## Finding

Fix any integer \(m\ge3\) and \(0<t<1\). Partition a metric space \(M\) into three labelled clusters \(A,B,C\) each containing \(m\) points. Let two distinct points have distance \(t\) if they belong to the same cluster and distance \(1\) otherwise. In the canonical zero-sum Euclidean realization of the real Lipschitz-free unit ball \(K\), put

\[
Q_{m,t}(r)=m+r t^2-\frac{(m+rt)^2}{3m},\quad 0\le r\le m-1,
\qquad R_{m,t}=\operatorname*{argmax}_{0\le r\le m-1}Q_{m,t}(r).
\]

The exact **globally maximal** Euclidean inball radius is

\[
\boxed{\rho_{m,t}=(\max_{0\le r\le m-1}Q_{m,t}(r))^{-1/2}.}
\]

The origin is an optimal center. The maximizing set \(R_{m,t}\) consists of the integers in \(\{0,\ldots,m-1\}\) nearest to \(3m/2-m/t\), with both integers kept at a tie. Exactly

\[
\boxed{T_{m,t}=6\sum_{r\in R_{m,t}}\binom{2m}{r}}
\]

facets touch the largest ball centered at the origin. Define \(\tau_m=2m/(3m-1)\). The affine dimension of the set \(\mathcal I_{m,t}\) of **all** optimal centers is

\[
\boxed{\dim\operatorname{aff}\mathcal I_{m,t}
=\begin{cases}3m-3,&0<t<\tau_m,\\0,&\tau_m\le t<1.\end{cases}}
\]

At \(t=\tau_m\), precisely \(6(2m+1)\) facets touch the origin-centered optimal ball, and the center becomes unique. For every \(0<t<1\), the total number of facets of \(K\) is exactly \(6(2^m-1)^3\). The limit \(t\to1\) is not included; the facet combinatorics can change at the endpoint.

## Assumptions and scope

All spaces and potentials are real. Put \(N=3m\) and write

\[
H=\{x\in\mathbb R^{N}:\sum_{v\in M}x_v=0\},\qquad
\operatorname{Lip}_1(M)=\{f:M\to\mathbb R:|f(u)-f(v)|\le d(u,v)\}.
\]

Represent \(K\subset H\) by

\[
K=\{x\in H:\langle x,f\rangle\le1\text{ for every }f\in\operatorname{Lip}_1(M)\}.
\]

For a potential \(f\), let \(\overline f=N^{-1}\sum_{v\in M}f(v)\) and \(z_f=f-\overline f\mathbf1\in H\). Extreme potentials modulo constants are precisely the vertices of the polar body in \(H\), hence each gives a facet inequality \(\langle x,z_f\rangle\le1\). The Euclidean norm and inradius depend on the specified canonical coordinate realization; this is not a Banach–Mazur optimization over linear isomorphisms.

## Proof

**1. Exact polar-vertex classification.** For any feasible real potential \(f\), form the *tight graph* by joining distinct \(u,v\) whenever \(|f(u)-f(v)|=d(u,v)\). The equality-constraint normals are signed differences of coordinate vectors. Their span in \(H\) has dimension \(N-c\), where \(c\) is the number of connected components of the tight graph. Therefore \(f\), modulo constants, is a polar vertex if and only if this graph is connected.

Every connected tight graph contains a cross-cluster length-one edge, since within-cluster edges alone cannot join the three blocks. Translate \(f\) so the endpoints of that edge have values \(0\) and \(1\). Every other value lies in \([0,1]\): a point in the cluster of the lower anchor is bounded below by its distance-one constraint to the upper anchor; similarly for the upper cluster; a point in the third cluster is constrained from both anchors. All cross-cluster tight edges consequently join values \(0\) and \(1\). Since no cluster can contain both values (its internal diameter is \(t<1\)), connectivity forces every cluster to be of exactly one of two types: *lower*, with a nonempty set of zeros and every remaining point at \(t\); or *upper*, with a nonempty set of ones and every remaining point at \(1-t\). At least one cluster of each type occurs. Conversely every such assignment has a connected tight graph, because the zeros and ones form a cross-cluster complete bipartite tight core and every intermediate point is linked to an anchor by an internal tight edge.

Thus choosing a nonempty anchor subset in each block, and choosing a nonconstant assignment of lower/upper types to the three blocks, gives exactly \(6(2^m-1)^3\) distinct polar vertices. This proves the total facet count.

**2. Strict one-sided screening.** Suppose an extreme potential contains a lower intermediate value \(t\) and an upper intermediate value \(1-t\). Replace one \(t\) by \(0\), and simultaneously one \(1-t\) by \(1\), retaining the existing lower/upper types. These replacements preserve feasibility, tight-graph connectivity and the coordinate sum. Their squared-coordinate sum increases by

\[
(0^2-t^2)+(1^2-(1-t)^2)=2t(1-t)>0.
\]

The centered squared norm \(\|z_f\|_2^2=\sum f(v)^2-(\sum f(v))^2/N\) therefore strictly increases. Every maximum-norm polar vertex is consequently *one-sided*: all intermediate values occur exclusively in lower clusters or exclusively in upper clusters. Taking the complement \(1-f\), which negates its centered normal, exchanges these two cases.

**3. Integer quadratic optimization.** We may therefore suppose that the upper clusters are constant \(1\) and the lower clusters contain zeros and exactly \(r\) values equal to \(t\). If \(u\in\{1,2\}\) is the number of upper clusters, then

\[
\|z_f\|_2^2=um+rt^2-\frac{(um+rt)^2}{3m},
\qquad 0\le r\le(3-u)(m-1).
\]

For \(u=2\), the coefficient of \(r\) after expansion is \(t(t-4/3)<0\) and the quadratic term is negative. Hence this expression is strictly decreasing for \(r\ge0\), and its maximum is the pure cut at \(r=0\), with squared norm \(2m/3\). For \(u=1\), the expression equals \(Q_{m,t}(r)\) and has the same pure-cut value \(Q_{m,t}(0)=2m/3\). Its continuous vertex is \(\alpha=3m/2-m/t\). Since \(t<1\), \(\alpha<m/2\), so every maximizing nonnegative integer satisfies \(r\le m-1\) for \(m\ge3\). Every subset of \(r\) among the two lower blocks is then legal: neither lower block can have all \(m\) of its points at \(t\). The largest squared norm over all extreme polar potentials is therefore exactly \(\max_{0\le r\le m-1}Q_{m,t}(r)\), attained precisely by the stated nearest integers.

**4. Global inradius and contact count.** For each centered extreme normal \(z_f\), the opposite normal \(-z_f\) also occurs, and \(K\) has both inequalities \(\pm\langle x,z_f\rangle\le1\). The origin-centered Euclidean ball of radius \(1/L\), where \(L=\max_f\|z_f\|_2\), lies inside \(K\). For any other center \(c\) and radius \(\rho\), the two opposite supporting inequalities with \(\|z_f\|_2=L\) give \(\rho L+|\langle c,z_f\rangle|\le1\), hence \(\rho\le1/L\). This proves global optimality.

For any maximizing \(r\), choose which cluster is the pure upper one (three choices), and choose \(r\) of the \(2m\) points in the remaining two clusters to have value \(t\). Complementation yields their distinct opposite facets. Each \(r\) contributes \(6\binom{2m}{r}\) contacts; for \(r=0\), these are the three pure cuts and their opposites. This proves the tangent-facet formula.

**5. The sharp center-locus collapse.** The first competitor to \(r=0\) is \(r=1\), with

\[
Q_{m,t}(1)-Q_{m,t}(0)
=t\left[t\left(1-\frac1{3m}\right)-\frac23\right].
\]

Strict concavity in \(r\) shows \(R_{m,t}=\{0\}\) exactly for \(0<t<\tau_m=2m/(3m-1)\), and \(R_{m,\tau_m}=\{0,1\}\). Above \(\tau_m\), every maximizing integer is positive.

The contact normals determine the affine dimension of all optimal centers: their span is \(W\subseteq H\), and every optimal center belongs to \(W^\perp\cap H\), because opposite maximal facet inequalities are simultaneously saturated by a ball of the optimal radius. Every noncontact facet has strictly positive clearance at the origin; hence a sufficiently small relative neighborhood of \(0\) inside \(W^\perp\cap H\) remains feasible as a center. Thus the affine dimension is \(N-1-\dim W\). If \(R_{m,t}=\{0\}\), the contacts are the binary cluster cuts, whose centered normals span exactly the two-dimensional subspace of vectors constant on each cluster and summing to zero. The dimension is \(N-3=3m-3\).

If some maximizing \(r\ge1\), then \(r\le m-1\). For a fixed upper cluster, replacing one chosen intermediate point by a different one inside the union of the two lower clusters produces the difference \(t(e_i-e_j)\) of two contact normals. Such exchanges are available for every pair \(i,j\) in those two clusters, since \(1\le r\le2m-1\). Every pair of points in \(M\) lies in the union of two clusters, and the choice of upper cluster is arbitrary. The contact normals therefore span all of \(H\), giving a unique optimal center. At the threshold, the maximizing integers are \(0,1\), and the contact count is \(6(1+2m)\), as asserted.

## Verification

The standalone exact-arithmetic program `verify_three_clusters.py` constructs candidate potentials with values from the saturated constraint alphabet, independently enforces all intra-cluster distance bounds, builds the tight graph for each assignment, and retains only connected graphs. For \(m=2,3\) and eight rational parameter cases, it completely enumerated \(10,776\) polar vertices and compared maximal centered norms, tangent multiplicities, and exact contact-normal ranks. Another \(224\) exact integer-profile cases allow intermediate states simultaneously on both sides and compare the full optimization to the claimed screened quadratic. All checks passed. This finite verification is independent corroboration of, not a replacement for, the proof for all \(m\ge3\) and real \(0<t<1\). Run `python3 verify_three_clusters.py` from the package directory; the program uses Python's standard library and SymPy.

## Relationship to prior work

Bredies, Chirinos Rodriguez and Naldi (arXiv:2304.14039, first posted April 27, 2023; subsequently published in 2024) give a tight-path characterization of extreme points of finite-metric Lipschitz unit balls, with emphasis on vector-valued functions and representer theorems. The real-valued tight-graph viewpoint is therefore not claimed here as new. Gordon and Petrov (arXiv:1608.06848) analyze the combinatorics of general Lipschitz polytopes and generic metrics, without a fixed-Euclidean inradius or the nongeneric three-cluster transition established here. Prior results for *disjoint shortened pairs* give the dual facet classification when every cluster has size two, a case intentionally excluded from the new theorem. Related exact projections of arbitrary clustered finite-metric free spaces concern projection norms, not the canonical Euclidean insphere or optimal-center ranks. Earlier calculations for one and two clustered levels do not imply the three-equal-cluster formulas without the one-sided screening step.

## Limitations

The sharp radius, contact count and center dimension are proved for precisely **three clusters of equal cardinality \(m\ge3\)**, with one common intra-cluster distance \(t\in(0,1)\). They are not asserted for unequal cluster sizes, heterogeneous intra-cluster radii, additional hierarchical levels, or arbitrary changes of Euclidean coordinates. The endpoint \(t=1\) has different facet combinatorics and is excluded. The total-facet count follows from the tight-graph classification, but no full higher-face vector is claimed. Exact finite tests do not certify the infinite parameter range. An equivalent maximum-variance formulation in literature outside the searched sources could affect priority.

## References

- K. Bredies, J. Chirinos Rodriguez, E. Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces*, arXiv:2304.14039 (first posted 2023-04-27), https://arxiv.org/abs/2304.14039; open text https://doi.org/10.1007/s00013-024-01978-y.
- J. Gordon, F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848 (first posted 2016-08-24), https://arxiv.org/abs/1608.06848.
- S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first posted 2018-07-10), https://arxiv.org/abs/1807.03814.
