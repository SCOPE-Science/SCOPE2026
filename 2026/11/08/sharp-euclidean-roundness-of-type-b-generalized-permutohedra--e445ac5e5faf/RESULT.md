# Sharp Euclidean roundness of type-\(B\) generalized permutohedra

## Finding
For each integer \(n\ge 2\), let \(\mathcal D_n\) be the class of full-dimensional convex polytopes in \(\mathbb R^n\) whose normal fan coarsens the type-\(B_n\) reflection fan (equivalently, all their edges are parallel to a coordinate vector or a signed difference of two coordinate vectors). Let \(r(P)\) be the radius of a largest Euclidean ball contained in \(P\), and let \(R(P)\) be the radius of a smallest Euclidean ball containing \(P\). Put
\[
d_k=\sqrt{k}-\sqrt{k-1}\quad(1\le k\le n),\qquad
D_n=\sum_{k=1}^n d_k^2.
\]
Then the sharp, attained bound throughout this entire deformation class is
\[
\boxed{\displaystyle \frac{r(P)}{R(P)}\le D_n^{-1/2}.}
\]
Equality is attained by the signed-permutation orbit polytope
\[
T_n=\operatorname{conv}\bigl\{(\varepsilon_1d_{\pi(1)},\ldots,\varepsilon_nd_{\pi(n)}):\pi\in\mathfrak S_n,\ \varepsilon_i\in\{-1,1\}\bigr\}.
\]
Among *hyperoctahedrally invariant* members of \(\mathcal D_n\), this maximizer is unique up to positive homothety (the group invariance fixes the center). Its inradius is \(1\) and its circumradius is \(\sqrt{D_n}\). Every one of its \(3^n-1\) facets is tangent to its unit inball; these facets have the signed-subset normals \(\sum_{i\in S}\varepsilon_i e_i\), with \(\varnothing\ne S\subseteq[n]\). No uniqueness claim is made among nonsymmetric members of the deformation class.

The best possible ratio has the asymptotic law
\[
\boxed{\displaystyle D_n^{-1/2}=\frac{2}{\sqrt{\log n}}\left(1+O\!\left(\frac1{\log n}\right)\right)\quad(n\to\infty).}
\]
In dimension two this is the regular octagon, with sharp ratio \(\cos(\pi/8)\).

## Assumptions and scope
The Euclidean norm and radii are the *ambient* ones, with no freedom to apply nonorthogonal affine maps. The normal-fan condition allows degenerations and nonsymmetric generalized permutohedra, but the polytope itself must be full-dimensional and bounded. Radii are invariant under translation and scale linearly under positive homotheties. The optimization concerns the ratio of the maximal inscribed ball to the minimal enclosing ball, not the isoperimetric quotient, volume ratio, or Banach–Mazur distance.

Write \(W_n\) for the signed-coordinate-permutation group. The type-\(B_n\) Weyl chambers are the images of \(C=\{u_1\ge\cdots\ge u_n\ge0\}\) under \(W_n\). A polytope is in \(\mathcal D_n\) exactly when its support function is linear on every such chamber; this is the conventional definition of a type-\(B\) generalized permutohedron. The equivalence with the edge-direction criterion is established in the cited deformation theory.

## Proof
**1. Symmetrization extends the problem from orbit polytopes to all deformations.** Let \(P\in\mathcal D_n\) and average its rotated copies by Minkowski addition:
\[
Q=|W_n|^{-1}\sum_{w\in W_n}wP.
\]
Every \(wP\) has its normal fan coarsening the type-\(B\) fan. The common refinement of these normal fans, which is the normal fan of their Minkowski sum, also coarsens that fan. Thus \(Q\in\mathcal D_n\), and \(Q\) is \(W_n\)-invariant. For compact convex sets \(A,B\), elementary addition of inscribed balls gives \(r(A+B)\ge r(A)+r(B)\), while adding circumscribed balls gives \(R(A+B)\le R(A)+R(B)\). Both radii are invariant under orthogonal maps, so
\[
r(Q)\ge r(P),\qquad R(Q)\le R(P),\qquad \frac{r(P)}{R(P)}\le\frac{r(Q)}{R(Q)}.
\]
A \(W_n\)-invariant support function that is linear on each Weyl chamber is the support function of a signed-permutation orbit: on \(C\), write \(h_Q(u)=b\cdot u\) for its unique chamber-slope vector \(b\). Convexity and \(W_n\)-invariance allow \(b_1\ge\cdots\ge b_n\ge0\), and the global support function is \(h_Q(u)=\max_{w\in W_n}(wb)\cdot u\). Hence \(Q=\operatorname{conv}(W_nb)\). This reduction includes weak inequalities and zero coordinates.

**2. Exact radii of the symmetric orbit.** For \(Q(b)=\operatorname{conv}(W_nb)\) with \(b_1\ge\cdots\ge b_n\ge0\), define \(B_k=\sum_{i=1}^k b_i\). The classical signed majorization description is
\[
Q(b)=\bigl\{x:\sum_{i\in S}|x_i|\le B_{|S|}\text{ for every nonempty }S\subseteq[n]\bigr\}.
\]
Equivalently, these are all linear signed-subset inequalities, whose unit normals have length \(\sqrt k\) at support size \(k\). By symmetry, averaging centers of any maximum inscribed ball gives an equally large ball centered at the origin. Thus
\[
r(Q(b))=\min_{1\le k\le n}\frac{B_k}{\sqrt k}.
\]
All orbit vertices lie on the sphere centered at the origin of radius \(\|b\|_2\). Their barycenter is zero; averaging their squared distances from an arbitrary candidate center \(c\) gives \(\|b\|_2^2+\|c\|_2^2\). Hence every enclosing ball has radius at least \(\|b\|_2\), and
\[
R(Q(b))=\|b\|_2.
\]
This argument proves that the minimum enclosing ball center is unique. It does not assume uniqueness of the incenter.

**3. Sharp norm inequality and equality.** Since the ratio is scale invariant, normalize \(r(Q(b))=1\). The signed-majorization inequalities yield \(B_k\ge\sqrt k\) for every \(k\). The positive sequence \(d_k=\sqrt k-\sqrt{k-1}\) is strictly decreasing, and set \(d_{n+1}=0\). Summation by parts gives
\[
\begin{aligned}
\langle d,b\rangle
&=\sum_{k=1}^n(d_k-d_{k+1})B_k\\
&\ge\sum_{k=1}^n(d_k-d_{k+1})\sqrt k\\
&=\sum_{k=1}^n d_k^2=D_n.
\end{aligned}
\]
Cauchy–Schwarz now implies \(\|b\|_2\ge\sqrt{D_n}\), hence \(r(Q(b))/R(Q(b))\le D_n^{-1/2}\). Equality in Cauchy–Schwarz forces \(b\) to be a positive multiple of \(d\). Under \(r=1\) the only possibility is \(b=d\), since each partial sum of \(d\) equals \(\sqrt k\). Conversely, for \(b=d\), all these partial sums are exactly \(\sqrt k\), so \(r=1\) and \(R=\sqrt{D_n}\). Returning to Step 1 proves the universal sharp bound. The same equality argument proves uniqueness among \(W_n\)-invariant members.

**4. Tangency and number of facets.** The strict inequalities \(d_1>\cdots>d_n>0\) make the normal fan of \(T_n\) exactly the type-\(B_n\) fan, so all signed-subset inequalities in Step 2 are genuine facets. There are \(\sum_{k=1}^n\binom nk2^k=3^n-1\) such facets. At \(b=d\), every facet support number equals \(\sqrt k\), exactly the norm of its normal; consequently every facet hyperplane is at distance one from the origin. The origin is the unique incenter of \(T_n\): if another center \(c\) supported a unit ball, each pair of opposite signed-subset facet inequalities would force the corresponding normal to be orthogonal to \(c\), and the coordinate facet normals already span \(\mathbb R^n\).

**5. Asymptotics.** For \(k\ge2\),
\[
d_k^2=\frac1{(\sqrt k+\sqrt{k-1})^2}=\frac1{4k}+O(k^{-2}).
\]
Therefore \(D_n=\tfrac14\log n+O(1)\), which yields the asserted ratio by taking square roots. For \(n=2\), \(d=(1,\sqrt2-1)\); the eight signed orbit points are the vertices of a regular octagon, and \(D_2^{-1/2}=\cos(\pi/8)\).

## Verification
The accompanying Python 3 program `verify_roundness.py` independently enumerates all signed-permutation vertices and all signed-subset support directions for dimensions \(2\) through \(5\). It checks the predicted support values, that every purported facet has affine dimension \(n-1\), and exact tangent-facet counts \(8,26,80,242\), respectively. It also checks representative nonoptimal weight profiles and the sharp ratio in dimensions through \(127\). The checked total is \(356\) facets. Floating-point checks use explicit numerical tolerances; the all-dimensional theorem follows solely from Steps 1–5.

## Relationship to prior work
Ardila, Castillo, Eur, and Postnikov establish the deformation cone of Coxeter permutohedra, with the symmetric slice described by weight polytopes (arXiv:1904.11029, §§2 and 6). Godland and Kabluchko give the exact signed-majorization inequalities and type-\(B\) normal fan (arXiv:2009.04186, Lemma 4.2 and Theorem 4.4). Eur, Fink, Larson, and Spink further develop signed-permutohedron and bisubmodular-polytope theory (arXiv:2209.06752).

These established fan and facet descriptions are used as prerequisites and are **not** new. The asserted new step is the sharp optimization of Euclidean inradius divided by circumradius over the **entire nonsymmetric deformation class**, including the equality-weight characterization, simultaneous contact of every facet, and logarithmic asymptotic. Neither standard face enumeration nor the signed-majorization inequalities alone provide this optimization without an additional symmetrization and sharp summation-by-parts argument.

## Limitations
Historical originality is subject to priority review: an earlier equivalent result stated as optimal approximation of the Euclidean ball by type-\(B\) Weyl-orbit polytopes, by bisubmodular polytopes, or by symmetric Coxeter deformations could exist under different terminology. The full equality classification for *nonsymmetric* deformations is not determined here; uniqueness is asserted only among signed-coordinate-permutation invariant bodies. The ratio is not optimized over all convex polytopes with a fixed number of facets, and the result does not assert a volume- or surface-area-optimal realization. Numerical testing is finite and is not independent proof of the general theorem. Independent mathematical audit has not been performed.

## References
- F. Ardila, F. Castillo, C. Eur, A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, arXiv:1904.11029, first public 2019-04-24, https://arxiv.org/abs/1904.11029.
- T. Godland, Z. Kabluchko, *Projections and angle sums of belt polytopes and permutohedra*, arXiv:2009.04186, first public 2020-09-09, https://arxiv.org/abs/2009.04186; *Results in Mathematics* 78, 140 (2023).
- C. Eur, A. Fink, M. Larson, H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752, first public 2022-09-14, https://arxiv.org/abs/2209.06752; *Proceedings of the London Mathematical Society* 128 (2024).
