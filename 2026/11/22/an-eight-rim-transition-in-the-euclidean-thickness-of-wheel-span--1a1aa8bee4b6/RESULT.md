# An eight-rim transition in the Euclidean thickness of wheel spanning-tree polytopes

## Finding

Let \(W_m=K_1\vee C_m\) denote the wheel with \(m\ge3\) rim vertices, one hub, and \(2m\) edges. Its canonical spanning-tree polytope is
\[
 P_m=\operatorname{conv}\{\mathbf 1_T:T\text{ is a spanning tree of }W_m\}\subset\mathbb R^{2m}.
\]
The Euclidean minimum width within its intrinsic affine hyperplane is
\[
 \boxed{\operatorname{width}(P_m)=\min\!\left\{\sqrt{\frac{2m}{2m-1}},\;2\sqrt{\frac2m}\right\}.}
\]
All unit minimizing normal directions are classified. For \(3\le m\le7\) they are exactly the signs of centered single-edge indicators. For \(m\ge8\) they are exactly the signs of centered indicators of subsets of \(m\) edges with graphic-matroid connectivity \(2\). Both kinds of cut are explicit; the transition occurs between rim lengths \(7\) and \(8\), with no integer tie.

## Assumptions and scope

Throughout, coordinates are indexed by the edge set \(E=E(W_m)\), with its standard orthonormal coordinate basis and no rescaling. The graph has hub \(0\), rim vertices \(1,\ldots,m\), spokes \((0,i)\), and rim edges \((i,i+1)\) with indices interpreted cyclically. Every spanning tree has exactly \(m\) edges, so \(P_m\) lies in \(\sum_{e\in E}x_e=m\). Its affine dimension is \(2m-1\), because the wheel cycle matroid is connected. For a nonempty proper \(S\subset E\), set
\[
 c_S=\mathbf 1_S-\frac{|S|}{2m}\mathbf 1_E,\qquad
 \lambda(S)=r(S)+r(E\setminus S)-m,
\]
where \(r\) denotes graphic-matroid rank. Thus \(\|c_S\|^2=|S|(2m-|S|)/(2m)\), and the phrase 'normal of \(S\)' means \(c_S/\|c_S\|\). The width in a unit vector \(u\perp\mathbf 1_E\) is \(\max_{x\in P_m}\langle u,x\rangle-\min_{x\in P_m}\langle u,x\rangle\). We optimize over all such unit vectors, not only coordinate directions.

## Proof

**Cut-normal principle.** For any connected matroid \(M\) on \(n\ge2\) elements with base polytope \(B(M)\), order the coordinates of a vector \(u\) as \(u_{\sigma(1)}\ge\cdots\ge u_{\sigma(n)}\). Write \(S_j=\{\sigma(1),\ldots,\sigma(j)\}\) and \(\delta_j=u_{\sigma(j)}-u_{\sigma(j+1)}\ge0\). The matroid greedy algorithm evaluates the maximum of \(\langle u,x\rangle\) on bases by successive rank increments; the minimum is obtained by reverse greedy order. Subtracting their summation-by-parts expressions gives the *exact* width identity
\[
 w_{B(M)}(u)=\sum_{j=1}^{n-1}\delta_j
 \bigl[r(S_j)+r(E\setminus S_j)-r(E)\bigr]
 =\sum_{j=1}^{n-1}\delta_j\lambda(S_j).
\]
Also, with \(\overline u=n^{-1}\sum_i u_i\),
\[
 u-\overline u\mathbf1_E=\sum_{j=1}^{n-1}\delta_j
 \left(\mathbf1_{S_j}-\frac{j}{n}\mathbf1_E\right).
\]
Define \(L=\min_{\varnothing\ne S\subsetneq E}\lambda(S)/\|\mathbf1_S-|S|\mathbf1_E/n\|\). The triangle inequality now yields
\[
 w_{B(M)}(u)\ge L\sum_j\delta_j\|c_{S_j}\|
 \ge L\|u-\overline u\mathbf1_E\|.
\]
Equality holds for a centered indicator realizing \(L\), proving that minimum Euclidean width is precisely \(L\). Conversely, in a minimizing direction the triangle inequality must be an equality. Two distinct proper nested subsets have nonparallel centered indicators (the coordinate values on their three nonempty blocks rule out collinearity). Hence at most one \(\delta_j\) can be positive. **Every** minimizing normal is a signed centered cut indicator achieving \(L\). This includes tied cut values, but excludes unrelated directions.

**Wheel connectivity bound.** The wheel graphic matroid has ground-set size \(n=2m\), rank \(m\), and is 3-connected for \(m\ge3\) [1, Example 2.26]. Therefore for a singleton edge \(S\), \(\lambda(S)=1\), and for every partition with \(2\le|S|\le2m-2\), \(\lambda(S)\ge2\). Consequently
\[
 \frac{\lambda(S)}{\|c_S\|}\ge
 \begin{cases}
 \sqrt{2m/(2m-1)},& |S|=1\text{ or }2m-1,\\
 2\sqrt{2/m},& 2\le|S|\le2m-2,
 \end{cases}
\]
because \(\|c_S\|\le\sqrt{m/2}\), with equality for \(|S|=m\). Singleton edges attain the first lower bound.

**Sharp balanced 3-separations.** Put \(a=\lceil m/2\rceil\). Let \(S\) contain all spokes \((0,i)\), \(1\le i\le a\), and all consecutive rim edges \((i,i+1)\), \(1\le i<a\). If \(m\) is even, add the rim edge \((a,a+1)\) as well. In either case \(|S|=m\). Writing \(c(F)\) for the number of connected components (including isolated vertices) of the spanning subgraph with edge set \(F\), the graphic rank formula is \(r(F)=m+1-c(F)\). A direct component count gives \(c(S)+c(E\setminus S)=m\), whence
\[
 \lambda(S)=m+2-c(S)-c(E\setminus S)=2.
\]
Thus the second lower bound is achieved for *every* \(m\ge3\). The two regimes follow from comparing squared candidate widths:
\[
 \frac{2m}{2m-1}\le\frac8m
 \quad\Longleftrightarrow\quad m^2-8m+4\le0.
\]
The positive crossing is \(4+2\sqrt3\), strictly between \(7\) and \(8\). No integer value ties. In the first regime equality forces \(|S|=1\) or \(2m-1\) and \(\lambda=1\). In the second it forces \(|S|=m\) and \(\lambda=2\). Combined with cut-normal rigidity this proves the exhaustive classification.

## Verification

The standalone reproducibility file `verify_wheel.py` performs integer-rank and exact-rational enumeration of all proper nonempty edge subsets for rim lengths \(3\le m\le9\). It compares every squared cut width with the theorem and classifies the minimizing subset types. The same checker independently enumerates spanning-tree indicator vertices for \(m=3,4\) and confirms the greedy support-width identity for every vector with coordinates in \(\{-1,0,1\}\), except constants. It checks the balanced 3-separation construction for \(3\le m\le64\). All checks pass. The all-dimensional proof above, rather than finite enumeration, establishes the quantifiers over arbitrary \(m\) and real unit directions.

## Relationship to prior work

The matroid base-polytope and submodular normal-fan framework is classical; see [2] for deformation theory and [3, Section 2.3] for the standard geometric realization of base polytopes. The 3-connectivity and wheel construction are explicitly established in [1, Example 2.26]. They supply premises, not this exact Euclidean-width evaluation. Related geometric investigations of wheel spanning-tree polytopes include uniform-vertex covariance anisotropy, and an unrelated family of complete-bipartite spanning-tree polytopes has an inradius classification; neither implies the present wheel minimum-direction threshold. Analogous minimum-width results for hypersimplices and hyper-permutahedra concern different matroid/polytope families. The derivation here identifies the exact wheel-specific phase change and its complete minimizing-normal characterization. Historical priority outside the inspected literature is not certified.

## Limitations

The result uses the canonical edge-coordinate Euclidean metric: affine or nonuniform coordinate scalings need not preserve the formula. It does not evaluate higher-dimensional widths, random-direction width distributions, or nonwheel graphic matroids. The cut-condition description of the large-rim minimizer set is complete but does not assert an explicit orbit-count classification for all rim lengths. Checks of finite wheel sizes do not replace the analytic proof. No independent mathematical audit has been performed.

## References

1. G. Denham, M. Schulze, and U. Walther, *Matroid connectivity and singularities of configuration hypersurfaces*, arXiv:1902.06507 (first posted 2019-02-18), Example 2.26; open-access version, https://doi.org/10.1007/s11005-020-01352-3.
2. A. Padrol, V. Pilaud, and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422 (first posted 2021-11-24), https://arxiv.org/html/2111.12422v2.
3. L. Ferroni and B. Schröter, *Valuative invariants for large classes of matroids*, Journal of the London Mathematical Society (2024), Section 2.3, https://doi.org/10.1112/jlms.12984.
