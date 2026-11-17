# Cubical incenter loci and complete tangency strata of multipartite Hansen polytopes

## Finding
For every integer \(r\ge2\) and all positive integers \(n_1,\ldots,n_r\), let \(G=K_{n_1,\ldots,n_r}\) have nonempty color classes \(V_1,\ldots,V_r\). Its canonical Hansen polytope in standard Euclidean coordinates is
\[
H(G)=\operatorname{conv}\{\pm(1,\mathbf1_I):I\subseteq V(G)\text{ is stable}\}\subset\mathbb R^{1+N},\qquad N=\sum_{j=1}^r n_j.
\]
The Euclidean inradius is the known perfect-graph value \(R=(4r+1)^{-1/2}\). The new classification is the **entire set of centers of maximum-radius contained Euclidean balls**:
\[
\boxed{\mathcal I(G)=\{(2\sum_{j=1}^r a_j,\ a_1\mathbf1_{V_1},\ldots,a_r\mathbf1_{V_r}):\ |a_j|\le h_r\ (1\le j\le r)\},}
\qquad h_r=\frac12\left(1-\sqrt{\frac{4r-3}{4r+1}}\right).
\]
It is an \(r\)-dimensional parallelotope in the ambient Euclidean metric, **regardless of the class sizes**. Its intrinsic Euclidean \(r\)-volume is
\[
\boxed{(2h_r)^r\sqrt{\left(\prod_{j=1}^r n_j\right)\left(1+4\sum_{j=1}^r\frac1{n_j}\right)}.}
\]
At every center, all \(2\prod_{j=1}^r n_j\) signed maximal-clique facets are tangent to the optimal ball. Write \(J=\{j:|a_j|=h_r\}\). Then there are **precisely**
\[
\boxed{2\prod_{j=1}^r n_j+\sum_{j\in J}\prod_{k\ne j}n_k}
\]
tangent facets. Each extra facet belongs to a clique that omits exactly the saturated class; no facets from cliques omitting two or more classes ever touch any optimal ball. In particular, at a relative interior point of an \((r-|J|)\)-dimensional face of the center parallelotope the displayed tangency count is exact. At a vertex of the incenter parallelotope, every class contributes extra tangencies.

For example, for \(G=K_{p,q}\) with \(p,q\ge1\), the inradius is \(1/3\), but the complete set of incenters is a nondegenerate Euclidean parallelogram. With \(h_2=(3-\sqrt5)/6\), its interior balls touch exactly \(2pq\) facets; its corner balls touch exactly \(2pq+p+q\).

## Assumptions and scope
All graph parts are nonempty; singleton parts are allowed, and \(r\ge2\). The empty stable set contributes a Hansen vertex. The first Euclidean coordinate is the twisted-prism sign coordinate; all remaining coordinates are individual graph vertices. No affine or metric renormalization is made. A facet is counted by its supporting hyperplane with orientation; opposite facets are distinct. Tangency means that the contained radius-\(R\) sphere meets the facet's supporting hyperplane. The displayed incenter locus and tangency formulas hold for every integer parameter tuple, not just sampled cases. The scalar inradius and centered maximum-clique contacts are attributed to earlier work; the classification of **all** optimal centers and their varying contacts is the claim.

## Proof
**1. Complete facet system and the known optimal radius.** Since \(G\) is complete multipartite, it is perfect, and every clique chooses at most one vertex of each class. The complete irredundant Hansen facet inequalities are, for every clique \(C\),
\[
-1\le -z+2\sum_{v\in C}x_v\le1.
\tag{1}
\]
The two outward facet normals have squared Euclidean norm \(4|C|+1\). Hence a radius-\(t\) ball centered at \(c=(z,x)\) fits precisely when
\[
\left|-z+2\sum_{v\in C}x_v\right|+t\sqrt{4|C|+1}\le1
\quad\text{for all cliques }C.
\tag{2}
\]
The largest cliques have size \(r\). The opposite facet pair corresponding to one such clique forces \(t\le(4r+1)^{-1/2}\), and the zero-centered ball attains this value against all smaller cliques. This familiar radius computation is not the new contribution.

**2. Necessary constraints on all optimal centers.** Fix \(t=R=(4r+1)^{-1/2}\). Equality in (2) for every maximal clique yields
\[
z=2\sum_{v\in C}x_v\qquad (|C|=r).
\tag{3}
\]
Holding the choices of all but one color class fixed and comparing two maximal cliques shows that all coordinate values in class \(V_j\) coincide, say \(x_v=a_j\) for all \(v\in V_j\). Formula (3) gives \(z=2\sum_j a_j\). Thus any optimal center lies in the claimed \(r\)-dimensional linear subspace.

**3. Collapse of all remaining inequalities.** A clique selecting vertices from the parts indexed by \(S\subseteq\{1,\ldots,r\}\) has \(r-t\) vertices, where \(T=\{1,\ldots,r\}\setminus S\) has \(t\) members. Substituting (3) into (2) gives exactly
\[
\left|\sum_{j\in T}a_j\right|\le\beta_t,
\qquad
\beta_t=\frac12\left(1-\sqrt{\frac{4(r-t)+1}{4r+1}}\right),
\qquad 1\le t\le r.
\tag{4}
\]
For \(t=1\), these inequalities are exactly \(|a_j|\le h_r=\beta_1\). For real \(0\le t\le r\), the function \(\beta_t\) is strictly convex, with \(\beta_0=0\); for example its first derivative is positive and strictly increasing. Consequently \(\beta_t>t\beta_1\) for every integer \(2\le t\le r\). Therefore the singleton bounds imply
\[
\left|\sum_{j\in T}a_j\right|\le t\beta_1<\beta_t
\qquad (|T|=t\ge2).
\tag{5}
\]
This both proves sufficiency of the claimed cube and ensures strict slack for **all** clique constraints missing two or more parts. There is no hidden inequality and no omitted class-size exception.

**4. Complete tangent-facet classification.** For a maximal clique, equation (3) makes both opposite signs in (2) tight; there are \(\prod_j n_j\) maximal cliques. For a clique missing precisely class \(j\), (4) is tight if and only if \(|a_j|=\beta_1\). Exactly one orientation is tight in that case, and there are \(\prod_{k\ne j}n_k\) such cliques. All other clique inequalities have strict slack by (5). As the clique facet description is irredundant, these counts are counts of distinct geometric facets, proving the full face-stratified formula.

**5. Intrinsic center-locus volume.** Parametrize the center set by \(a\in[-h_r,h_r]^r\). Its tangent vectors are \(b_j=(2,\mathbf1_{V_j})\), with Gram matrix
\[
\bigl(\langle b_i,b_j\rangle\bigr)_{i,j}=\operatorname{diag}(n_1,\ldots,n_r)+4\mathbf1\mathbf1^\mathsf T.
\]
The matrix determinant lemma gives determinant \(\prod_j n_j(1+4\sum_j1/n_j)\). Multiplication by the parameter cube volume \((2h_r)^r\) yields the displayed intrinsic volume formula. Since every \(n_j>0\), the Gram matrix is positive definite and the affine dimension is exactly \(r\).

## Verification
The bundled standalone Python 3 checker `verification/check.py` reconstructs every clique and evaluates its signed facet inequalities at all \(3^r\) parameter choices with \(a_j\in\{-h_r,0,h_r\}\) for 32 parameter profiles. It compares all exact/near-exact tangency counts to the combinatorial formula and checks the strict scalar convexity inequalities for all integer \(r\) from 2 to 60. Running `python verification/check.py` prints:

`HANSEN_MULTIPARTITE_INCENTER_PASS profiles=32 center_patterns=2520 convexity_inequalities=1770`

The checker uses only the Python standard library and independently tests the support inequalities; its finite tests are corroboration, not a substitute for the arbitrary-parameter proof above.

## Relationship to prior work
Hansen (1977) introduced the construction. Freij, Henze, Schmitt and Ziegler (2012 preprint, published 2013) give the complete perfect-graph clique-facet description, reproduced in (1), and investigate face numbers and Hanner polytopes. Hibi and Tsuchiya's publicly available 2017 treatment places Hansen polytopes among perfect-graph twisted stable-set constructions, discussing reflexivity, integer decomposition and Ehrhart invariants. Previously published work *Clique and stability numbers as exact Euclidean radii of perfect-graph Hansen polytopes* computes the scalar inradius and the **origin-centered** contacting maximal-clique facets in all perfect graphs; these are not claimed as new.

The present theorem determines instead **every noncentral optimal ball**, the complete incenter parallelotope and its intrinsic Euclidean volume, and exactly how the touching-facet set changes with its face stratification. In a complete multipartite graph, one has many maximal-clique constraints yet their common kernel has dimension \(r\); strict convexity makes every lower-rank constraint except the next-to-top rank redundant on the optimal-center locus. This is additional geometry not implied by a radius formula or an origin-contact count alone. No directly equivalent incenter-locus theorem was identified in the inspected material; historical priority remains provisional.

## Limitations
The argument treats the canonical Euclidean Hansen realization of complete multipartite graphs, not arbitrary perfect graphs, nonperfect graphs or arbitrary affine images. The formula is for all largest-ball centers; it does not classify maximum-volume inscribed ellipsoids. The original 1977 Hansen article was identified but not examined in full; an older equivalent center-locus computation cannot be excluded. The global original-versus-covered judgment requires an independent literature review beyond the reported comparisons.

## References
1. A. B. Hansen, *On a certain class of polytopes associated with independence systems*, Mathematica Scandinavica 41 (1977), 225–241, DOI 10.7146/math.scand.a-11716.
2. R. Freij, M. Henze, M. W. Schmitt, and G. M. Ziegler, *Face numbers of centrally symmetric polytopes from split graphs*, arXiv:1201.5790 (2012-01-27), Electronic Journal of Combinatorics 20(2) (2013), P32. See Lemma 2.4; https://arxiv.org/html/1201.5790v1.
3. T. Hibi and A. Tsuchiya, *Reflexive polytopes arising from perfect graphs*, arXiv:1703.04410 (first public 2017-03-13), Journal of Combinatorial Theory A 157 (2018), 233–246; https://arxiv.org/html/1703.04410v2.
4. *Clique and stability numbers as exact Euclidean radii of perfect-graph Hansen polytopes*, published research record (2026-10-11), identifier 5c60f4f604ef; prior scalar-radius and centered-contact results credited.
5. *Fractional antiblockers determine every Hansen inradius, with an unbounded failure of the clique law*, published research record (2026-11-08), identifier 79ea53f863b0; general-graph radius reduction credited.
