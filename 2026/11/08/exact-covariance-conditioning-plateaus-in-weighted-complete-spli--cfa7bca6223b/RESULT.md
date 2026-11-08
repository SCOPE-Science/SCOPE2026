# Exact covariance-conditioning plateaus in weighted complete-split graphical zonotopes

## Finding

Let \(p,q\ge2\) be integers, let \(C\) be a clique of \(p\) vertices and \(I\) an independent set of \(q\) vertices, and let \(G=K_p\vee\overline{K_q}\). For any real weight \(t>0\), define the graphical zonotope
\[
Z_{p,q}(t)=t\sum_{\{i,j\}\subset C}[e_i,e_j]+\sum_{i\in C,\,j\in I}[e_i,e_j]\subset\mathbb R^{p+q}.
\]
Choose a vertex \(X\) **uniformly among distinct vertices**, and let \(\Sigma(t)=\operatorname{Cov}(X)\). Its complete spectrum, including multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
0&1\\
L_C(t)=\dfrac{p(p+1)t^2+2pqt+\dfrac{pq^2+q(p+2)}{p+1}}{12}&p-1\\[6pt]
L_I=\dfrac{p(p+2)}{12}&q-1\\[6pt]
L_A=\dfrac{(p+q)(p+2)}{12}&1
\end{array}.
\]
In particular, the only weight-dependent eigenvalue is \(L_C(t)\), which increases strictly for \(t>0\), while \(L_I<L_A\) always. Define the two possible crossing weights
\[
t_I=\frac{\sqrt{(p+2)(p(p+1)-q)/p}-q}{p+1},\qquad
t_A=\frac{\sqrt{(p+2)(p+q+1)}-q}{p+1},
\]
where \(t_I\) is used only when \(q\le p\), and let
\[
T(p)=\frac{p+2+\sqrt{(p+2)(5p+6)}}{2}.
\]
The **exact conditioning phase diagram** is as follows.

* If \(2\le q\le p\), then \(0<t_I<t_A<1\). The intrinsic condition number \(\kappa(t)=\lambda_{\max}(\Sigma(t))/\lambda_{\min}^{+}(\Sigma(t))\) decreases strictly as \(L_A/L_C(t)\) on \(0<t<t_I\), is exactly \((p+q)/p\) throughout the nondegenerate closed interval \([t_I,t_A]\), and increases strictly as \(L_C(t)/L_I\) for \(t>t_A\).
* If \(p<q<T(p)\), then \(0<t_A<1\). The condition number equals \((p+q)/p\) for every \(0<t\le t_A\), and equals the strictly increasing \(L_C(t)/L_I\) for \(t>t_A\).
* If \(q\ge T(p)\), then \(L_I<L_A<L_C(t)\) for every \(t>0\) and \(\kappa(t)=L_C(t)/L_I\), strictly increasing.

Coincident eigenvalues at crossing weights have the summed multiplicities shown in the table. The universal lower bound \(\kappa(t)\ge(p+q)/p\) is attained at some positive weight **if and only if** \(q<T(p)\). When \(q\ge T(p)\), the sharp, unattained infimum is
\[
\inf_{t>0}\kappa(t)=\frac{pq^2+q(p+2)}{p(p+1)(p+2)}.
\]
The ordinary unit-weight graphical zonotope always lies strictly beyond the last possible crossing and has
\[
\kappa(1)=\frac{p(p+q+1)^2+q(p+2)}{p(p+1)(p+2)}>
\frac{p+q}{p}.
\]
Thus tuning clique-edge lengths can create an **exactly flat covariance-condition-number optimum**, not merely an isolated best weight, while sufficiently large independent sets preclude the plateau. For fixed \(p\), the best possible conditioning over positive weights grows quadratically in \(q\), with coefficient \(1/((p+1)(p+2))\).

## Assumptions and scope

Coordinates are Euclidean with the standard orthonormal basis. Each edge segment is the convex hull of its two indicated basis vectors; each clique edge has coefficient \(t\), each clique-to-independent edge has coefficient \(1\), and there are no edges within the independent set. The ambient affine hull is the constant-coordinate-sum hyperplane of dimension \(p+q-1\). The condition number is calculated on its tangent space, excluding the one deterministic zero direction. Every formula concerns uniform sampling among **distinct vertices**, not uniform intrinsic volume, independent random segment coefficients, or random total orders without identifying equivalent orientations. Real weights satisfy \(t>0\); the zero-weight limit is taken only when computing an infimum and is not claimed to have the same uniform-vertex distribution at \(t=0\).

## Proof

**1. Exact uniform vertex parametrization.** All edge weights are positive, so the normal fan is that of the graphical hyperplane arrangement and its full-dimensional regions correspond bijectively to acyclic orientations. The clique orientation is a total order, which has \(p!\) choices. In an acyclic orientation, each independent vertex must place its incident edges around a unique gap of that total order: among the \(p+1\) gaps choose how many clique vertices precede it. Conversely, any clique order and any independent choice of gaps gives an acyclic orientation. Different choices give distinct orientations, and hence distinct vertices. Thus the number of vertices is exactly \(p!(p+1)^q\), and uniform vertex sampling is equivalent to a uniform random clique order together with independent uniform gaps in \(\{0,\ldots,p\}\).

Fix the orientation in which each edge contributes its weight to the *later* endpoint. The resulting coordinate vector differs from any alternative consistent endpoint convention only by a global translation or sign, neither of which changes the covariance spectrum. Let \(R_i\in\{1,\ldots,p\}\) be the uniformly permuted rank of clique vertex \(i\), and let \(G_j\in\{0,\ldots,p\}\) be independent uniform gaps. Then the vertex coordinates are
\[
X_i=t(R_i-1)+\sum_{j=1}^{q}{\bf1}_{\{G_j<R_i\}},\quad i\in C;\qquad
X_j=G_j,\quad j\in I.
\]
All such coordinates have constant sum \(t\binom p2+pq\), since every segment contributes its weight once.

**2. Independent-vertex contrasts and mixed covariance.** Uniform gaps give
\[
\operatorname{Var}(G_j)=\frac{p(p+2)}{12},\quad
\operatorname{Cov}(G_j,G_k)=0\quad (j\ne k).
\]
For fixed \(1\le r\le p\),
\[
\operatorname{Cov}({\bf1}_{\{G<r\}},G)
=\frac{r(r-p-1)}{2(p+1)}.
\]
Average over uniform \(r\) to obtain
\[
\operatorname{Cov}(X_i,G_j)=-\frac{p+2}{12}
\]
for every clique coordinate \(i\) and independent coordinate \(j\). These facts imply that the \((q-1)\)-dimensional independent-set contrast space has eigenvalue \(L_I=p(p+2)/12\).

**3. Clique contrasts.** Condition on the clique ranks. The conditional expectation of a clique coordinate is
\[
\mathbb E[X_i\mid R_i]=\Bigl(t+\frac{q}{p+1}\Bigr)R_i-t.
\]
For different rank positions \(R_i,R_k\), the difference between their individual rank variance and cross-covariance equals \(p(p+1)/12\). More explicitly, for two distinct uniformly permuted ranks, \(\mathbb E[\min(R_i,R_k)]=(p+1)/3\) and \(\mathbb E[R_iR_k]=(p+1)(3p+2)/12\). For one independent gap the centered indicator \({\bf1}_{\{G<R_i\}}-R_i/(p+1)\) has mean conditional variance \((p+2)/(6(p+1))\) and mean conditional covariance between two distinct clique ranks \((p+2)/(12(p+1))\). Applying total covariance and subtracting clique off-diagonal covariance from diagonal covariance gives
\[
L_C(t)=\frac{p(p+1)}{12}\Bigl(t+\frac{q}{p+1}\Bigr)^2+\frac{q(p+2)}{12(p+1)}.
\]
This is precisely the displayed expression and is positive and strictly increasing on \(t>0\).

**4. Axial block.** Permuting clique vertices and independently permuting independent-set vertices leaves the distribution unchanged. The only remaining space is spanned by the two normalized group-indicator vectors. The covariance has zero row sums by the constant-sum property. The mixed block has every entry \(-(p+2)/12\), so its restriction to the normalized constant-group vectors is exactly
\[
\frac{p+2}{12}
\begin{pmatrix}
q&-\sqrt{pq}\\
-\sqrt{pq}&p
\end{pmatrix}.
\]
The eigenvalues of this block are \(0\) and \(L_A=(p+q)(p+2)/12\). This establishes the entire spectrum, its multiplicities, the unique zero mode, and positivity of every other mode.

**5. Sharp phase boundaries and optimization.** Since \(L_I<L_A\) and \(L_C(t)\) increases strictly, each possible eigenvalue crossing happens at most once. Solving \(L_C(t)=L_I\) and \(L_C(t)=L_A\) gives \(t_I\) and \(t_A\). Directly at zero weight,
\[
L_C(0)=\frac{pq^2+q(p+2)}{12(p+1)}.
\]
The strict inequality \(L_C(0)<L_I\) holds exactly for integer \(q\le p\): the numerator difference is strictly increasing in \(q\), negative at \(q=p\), and positive at \(q=p+1\). Likewise \(L_C(0)<L_A\) is equivalent to
\[
q^2<(p+2)(p+q+1),
\]
which, since \(q>0\), is equivalent to \(q<T(p)\). Whenever both crossings exist, \(t_I<t_A\) follows from \(L_I<L_A\), and \(t_A<1\) follows from \(p+q+1>p+2\) for \(q\ge2\). These inequalities give all three cases, including equality weights and the disappearance of the plateau.

For any positive \(t\), the two fixed eigenvalues force \(\kappa(t)\ge L_A/L_I=(p+q)/p\). Equality holds exactly when \(L_I\le L_C(t)\le L_A\), and the preceding crossing classification gives the asserted full minimizing sets. If \(q\ge T(p)\), then \(L_C(t)>L_A\) for all \(t>0\), so strict increase implies an unattained infimum \(L_C(0)/L_I\). Finally, substitution of \(t=1\) yields \(L_C(1)-L_A=p(q-1)(p+q+1)/(12(p+1))>0\), proving the unit-weight statement. Dividing the infimum by \(q^2\) at fixed \(p\) gives the last asymptotic coefficient.

## Verification

A standalone Python-standard-library checker is included as `verify.py`. It enumerates every clique permutation and every independent-vertex gap choice, constructs exact rational covariance matrices for four positive rational weights at each of nine graph-size pairs, and compares **every matrix entry** with the three-eigenspace projector formula. It separately enumerates all total orders in 24 smaller cases and confirms the claimed number of *distinct* vertices. It also checks the exact integer crossing-sign criteria over 35,164 parameter pairs. A successful replay prints `SPLIT_WEIGHTED_ZONOTOPE_COVARIANCE_CHECKS_PASSED`. These are finite cross-checks of the general algebraic proof, not replacements for the infinite proof.

## Relationship to prior work

Graphical zonotope vertices correspond to acyclic orientations; this premise is classical and is explicitly described in Padrol--Pilaud--Poullot, *Deformed Graphical Zonotopes* (first public preprint 24 November 2021), whose main theorems characterize deformation-cone equations and facets for arbitrary graphs. Its complete accessible article does not calculate vertex-uniform covariance or optimize its condition number under weighted edge orbits. Pešović--Stojadinović, *Between graphical zonotope and graph-associahedron* (first public preprint 24 September 2022), constructs interpolating graph polytopes and studies quasisymmetric enumerators and normal fans, not the Euclidean covariance here. These are relevant frameworks, not asserted priority for the new spectral calculation.

Related available results concern intrinsic-volume covariance of cactus and book-graph graphical zonotopes, unit-weight graphical-zonotope inballs, and complete-multipartite graphical-zonotope circumspheres. The book-graph case is exactly the \(p=2\) graph with the same positive spine-edge parameter, but the earlier volume-uniform measure is mathematically different from the present vertex-uniform law. Intrinsic-volume sampling is different from sampling vertices, and the complete-split graph has extra clique edges absent from the bipartite cases. Neither those results nor the general acyclic-orientation correspondence itself implies the two crossing formulas and sharp weight-plateau classification. Historical priority against any differently formulated work on random acyclic orientation indegrees has not been fully certified.

## Limitations

The result concerns complete-split graphs with \(p,q\ge2\) and exactly two positive edge-weight orbits. It does not give an analogous phase diagram for arbitrary split graphs, arbitrary edge weights, intrinsic-volume covariance, or a continuous limit distribution as both graph sizes diverge. The zero-weight endpoint changes the normal fan and may change the uniform-vertex measure discontinuously, so all actual optimization is over strictly positive weights. Numerical and finite exact checks alone cannot establish the infinite claims; those are proved above. No independent mathematical audit has been performed, and a previously published equivalent statistic or spectral reduction under other terminology remains a residual priority risk.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first public 24 November 2021; later *Discrete & Computational Geometry* 73 (2025), 447–465. https://arxiv.org/abs/2111.12422 ; https://doi.org/10.1007/s00454-023-00586-x .
2. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053, first public 24 September 2022. https://arxiv.org/abs/2209.12053 .
3. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, first public 23 April 2016, for the classical acyclic-orientation vertex correspondence. https://arxiv.org/abs/1604.06931 .
