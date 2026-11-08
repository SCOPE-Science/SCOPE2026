# Matching-deletion Ehrhart formula and additive polar-volume law for complete graph metrics

## Finding

Let \(n\ge4\) and delete a matching of \(2\le k\le\lfloor n/2\rfloor\) edges from the complete graph \(K_n\), obtaining \(G=K_n\setminus M\). Let \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and set
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G)\}\subset H,
\qquad Q_G=P_G^\circ\subset H.
\]
Equip \(Q_G\) with the lattice \(A_{n-1}^*=\{x\in H:x_i-x_j\in\mathbb Z\text{ for all }i,j\}\). Its Ehrhart polynomial, for every integer \(m\ge0\), is
\[
\boxed{L_{Q_G}(m)=(m+1)^n-m^n+2k\sum_{h=1}^{m}h^{n-2}.}
\]
Define the Eulerian polynomial \(E_r(z)\) by \(\sum_{m\ge0}(m+1)^r z^m=E_r(z)/(1-z)^{r+1}\). The entire Ehrhart numerator is then
\[
\boxed{h^*_{Q_G}(z)=E_n(z)+2kzE_{n-2}(z).}
\]
It is palindromic and \(\gamma\)-nonnegative, and hence symmetric and unimodal.

There is a simultaneous continuous-volume theorem: assign each of the \(k\) disjoint distinguished pairs an arbitrary length \(t_j\in[1,2]\), and every other pair length \(1\). Let \(Q(\boldsymbol t)\subset H\) be the corresponding Lipschitz polytope \(\{|x_u-x_v|\le d_{uv}\}\). Then
\[
\boxed{\operatorname{vol}_{n-1}(Q(\boldsymbol t))=
 \frac1{\sqrt n}\left[n+\frac2{n-1}\sum_{j=1}^{k}\bigl(1-(2-t_j)^{n-1}\bigr)\right].}
\]
In particular, all mixed derivatives with respect to two *different* length parameters vanish in the open cube \((1,2)^k\), while the second derivatives with respect to each individual parameter are strictly negative. At the graph-metric endpoint \(t_j=2\) for every pair, this gives
\[
\boxed{\operatorname{vol}_{n-1}(Q_G)=\frac{n+2k/(n-1)}{\sqrt n},\qquad
 \operatorname{Vol}_{A_{n-1}^*}(Q_G)=(n-1)!\left(n+\frac{2k}{n-1}\right).}
\]
The complete-graph polar has volume \(n/\sqrt n\); hence deleting a matching of size \(k\) increases its polar volume by precisely the fraction \(2k/[n(n-1)]\).

## Assumptions and scope

The graph is a connected simple complete graph with a pairwise-disjoint nonempty edge deletion set, with at least two deleted edges. In this range \(n\ge4\), it remains connected. All polars are taken inside \(H\), using its inherited Euclidean inner product. Distances \(t_j\) lie between \(1\) and \(2\), ensuring the triangle inequality; for the Ehrhart claim all \(t_j\) equal \(2\). Integer points are counted in \(A_{n-1}^*\), *not* in the ambient integer lattice \(A_{n-1}\). Fixing the last potential to zero gives the lattice coordinates \(y_i=x_i-x_n\), \(1\le i<n\), with \(y_i\in\mathbb Z\). Relative Euclidean volume in \(H\) equals rooted-coordinate volume divided by \(\sqrt n\). The convention for \(\operatorname{Vol}_{A_{n-1}^*}\) is normalized lattice volume, namely \((n-1)!\) times the rooted-coordinate volume.

## Proof

**1. Integer potentials and translation classes.** By polarity,
\[
Q_G=\{x\in H:|x_i-x_j|\le1\text{ whenever }\{i,j\}\notin M\}.
\]
Modulo adding a constant to all coordinates, a lattice point of \(mQ_G\) is exactly an integer labeling \((a_1,\ldots,a_n)\) with \(|a_i-a_j|\le m\) for every edge of \(G\). The class has a unique representative with global minimum zero. Denote the range of this representative by \(S=\max_i a_i\).

**2. The ordinary cube-range region.** If \(0\le S\le m\), every coordinate belongs to \(\{0,\ldots,m\}\) and at least one is zero. Thus the number of these classes is exactly \((m+1)^n-m^n\). These labelings automatically satisfy every edge inequality.

**3. Excursions beyond the equilateral range.** Suppose \(S>m\). A minimum vertex and a maximum vertex must be nonadjacent in \(G\), since their difference exceeds \(m\). The only nonadjacent pairs are the deleted matching pairs. There is exactly one minimum and one maximum: if, for instance, two distinct vertices attained the minimum, each would have to be the unique matching partner of the same maximum, which is impossible. There are therefore exactly \(2k\) possible oriented extreme pairs.

Fix one oriented missing pair, and set its minimum and maximum values to \(0\) and \(S\), respectively. Every one of the other \(n-2\) vertices is adjacent to both extreme vertices. It must therefore lie in
\[
[S-m,m]\cap\mathbb Z.
\]
This interval is nonempty precisely for \(m<S\le2m\), has \(2m-S+1\) integer points, and its width is strictly less than \(m\). Consequently all inequalities among the remaining vertices are automatic, independent of their matching relations. For any fixed \(S\) there are exactly \((2m-S+1)^{n-2}\) labelings. Summing over \(S=m+1,\ldots,2m\), reindexing \(h=2m-S+1\), and multiplying by the \(2k\) oriented pairs yields the stated Ehrhart formula. The regions are disjoint because their extrema are unique. When \(m=0\), only the all-zero class occurs, and the formula still holds.

**4. Ehrhart numerator and \(\gamma\)-positivity.** The defining generating-function identity implies
\[
\sum_{m\ge0}\bigl((m+1)^n-m^n\bigr)z^m=\frac{E_n(z)}{(1-z)^n},
\quad
\sum_{m\ge0}\left(\sum_{h=1}^mh^{n-2}\right)z^m
=\frac{zE_{n-2}(z)}{(1-z)^n}.
\]
This proves the numerator expression. Since \(E_r(z)\) is palindromic of degree \(r-1\), both \(E_n(z)\) and \(zE_{n-2}(z)\) are palindromic with ambient degree \(n-1\). More precisely, write
\[
E_r(z)=\sum_{j\ge0}\gamma_{r,j}z^j(1+z)^{r-1-2j}.
\]
The Eulerian recursion implies \(\gamma_{1,0}=1\) and
\[
\gamma_{r+1,j}=(j+1)\gamma_{r,j}+2(r-2j+1)\gamma_{r,j-1},
\]
with out-of-range coefficients zero. Every coefficient in the relevant range is nonnegative, inductively; hence the \(\gamma\)-coefficient of \(z^j(1+z)^{n-1-2j}\) for \(h^*\) equals \(\gamma_{n,j}+2k\gamma_{n-2,j-1}\ge0\). This proves \(\gamma\)-nonnegativity and unimodality, including all boundary indices.

**5. Exact continuous volumes.** Fix the metric lengths \(\boldsymbol t\in[1,2]^k\). For a real potential modulo constants, choose the representative whose minimum is zero. Up to lower-dimensional boundaries, either its range is at most \(1\), or its unique minimum and maximum are an oriented distinguished pair. The first region is a union of \(n\) disjoint unit cubes (one per chosen minimum), contributing rooted-coordinate volume \(n\). For a fixed oriented distinguished pair \(j\) with maximum \(S>1\), feasibility requires \(1<S\le t_j\), while every other potential lies freely in \([S-1,1]\), a segment of length \(2-S<1\). Pairwise constraints among these remaining potentials are automatic. In coordinates given by the maximal value \(S\) and the \(n-2\) other coordinate values, the quotient measure has Jacobian one. The added volume is therefore
\[
2\sum_{j=1}^k\int_1^{t_j}(2-S)^{n-2}\,dS
=\frac2{n-1}\sum_{j=1}^k\bigl[1-(2-t_j)^{n-1}\bigr].
\]
This proves the rooted-coordinate expression. Finally, the affine map \((y_1,\ldots,y_{n-1})\mapsto (y_1,\ldots,y_{n-1},0)-\frac1n(\sum_{i<n}y_i)\mathbf1\) from rooted coordinates into \(H\) has Gram matrix \(I-\mathbf1\mathbf1^{\mathsf T}/n\), whose determinant is \(1/n\). Its Euclidean Jacobian is \(1/\sqrt n\). The stated volume formulas, additive dependence, and derivative claims follow.

## Verification

The included `artifacts/verify.py` independently enumerates rooted integer potentials in small cases, applies the generating-function transformation, checks full coefficient palindromicity, and computes several rooted volumes from halfspace intersections and convex hulls using SciPy. Exact finite calculations use integer arithmetic; convex-hull volumes use numerical tolerances. Its completed run reported `MATCHING_LIPSCHITZ_EHRHART_CHECKS_PASSED integer_profiles=34 hstar_profiles=6 independent_hulls=8`. Run `python artifacts/verify.py` in an environment with Python 3, NumPy, and SciPy. The infinite claims rely on the exact counting/integration proof above, not finite case enumeration.

For illustration, \(n=4\) and \(k=2\) give \(L(m)=(m+1)^4-m^4+4\sum_{h=1}^m h^2\) and \(h^*(z)=1+15z+15z^2+z^3\). The new result covers all allowed \((n,k)\), not merely this example.

## Relationship to prior work

D'Alì, Delucchi and Michałek [1] relate symmetric edge polytopes to Lipschitz polytopes and study their faces; Proposition 65 concerns lattice points at the first dilation for planar graph polars. D'Alì, Juhnke-Kubitzke and Koch [2, Proposition 5.1] establish a general bijection between polar Ehrhart lattice points and bounded cuts of a regular matroid. That general bijection does not evaluate the matching-deleted complete-graph cut counts or their \(h^*\) polynomials. Higashitani, Jochemko and Michałek [3, Section 3] describe facets of complete-multipartite symmetric edge polytopes, not the polar Ehrhart expression found here. Gordon and Petrov [4] develop general Lipschitz-polytope face combinatorics; the corresponding metric family is not given this Ehrhart and volume calculation.

The isolated \(n=4,k=2\) graph is \(K_{2,2}\); its scalar polar volume can also be obtained from an existing complete-bipartite polar-volume formula and is not claimed as a newly discovered value. The present complete-multipartite graphs have parts of sizes at most two, specifically \(k\) parts of size two and \(n-2k\) singleton parts. In a previously available single-missing-edge complete-split case, a scalar polar-volume expression is known. Neither that one-pair special case nor general bounded-cut correspondences determine the full exact \(k\ge2\) Ehrhart numerator, its \(\gamma\)-positivity, or independent-parameter real-volume additivity by direct parameter substitution. The complete-graph baseline and classical Eulerian \(\gamma\)-positivity are not presented as new.

## Limitations

No general formula is asserted for overlapping removed edges, or for within-pair lengths outside \([1,2]\), or for arbitrary complete multipartite parts of size three or larger. The lattice in the Ehrhart theorem is the dual root lattice; using the ambient root lattice would produce different counts. The volume uses the inherited Euclidean metric, not a free choice of lattice measure. The explicit formula is independently derived here, but an earlier equivalent statement under bounded-cut, graphical metric, or lattice-point terminology could exist. A related published general bijection gives a powerful reduction rather than an explicit formula; scientific priority requires further independent bibliographic verification. Independent mathematical audit has not been performed.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193v1 (first public 11 October 2019), especially the Lipschitz-polytope discussion and Proposition 65. https://arxiv.org/abs/1910.05193 . Full journal text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i3p24/pdf/ .
2. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933v1 (first public 10 July 2023), especially Section 5 and Proposition 5.1. https://arxiv.org/abs/2307.04933 .
3. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public 20 July 2018), Section 3. https://arxiv.org/abs/1807.07678 .
4. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848 (2016), especially the general facial-combinatorial framework. https://arxiv.org/abs/1608.06848 .
