# Perron synchronization and complete fixed-set geometry at the matrix nonexpansive threshold

## Finding

Consider nonlinear maps whose coordinatewise Lipschitz bounds are controlled by an **irreducible** nonnegative matrix at spectral radius \(1\). Every pair of fixed points has coordinate distances in the **same Perron ratio**. With strictly convex coordinate spaces this forces the fixed set to be an affine, mutually isometric coordinate graph; for real scalar coordinates it collapses to one interval on a signed Perron line. Every sign pattern and every compact interval on that line is realized by an explicitly given map on a full-dimensional box. An explicit resolvent bound controls deviations from the Perron ratio for approximate fixed points.

## Assumptions and scope

Let \(N\ge2\), \(A=(a_{ij})\in[0,\infty)^{N\times N}\) be irreducible with spectral radius \(r(A)=1\). Fix the right and left Perron eigenvectors \(u,w\in(0,\infty)^N\), normalized by
\[
Au=u,\qquad w^{\mathsf T}A=w^{\mathsf T},\qquad w^{\mathsf T}u=1.
\]
Let \(X_i\) be arbitrary real or complex normed spaces and \(X=\prod_iX_i\). Let \(K\subseteq X\) and \(T:K\to K\) satisfy, for every \(x,y\in K\) and each \(i\),
\[
\|T_i(x)-T_i(y)\|_i\le\sum_{j=1}^Na_{ij}\|x_j-y_j\|_j.\tag{1}
\]
Write \(F=\{x\in K:T(x)=x\}\). Fixed-point existence is not assumed except when a nonempty set is needed for a geometric description; under weak compactness, convexity and normal structure, existence follows from the cited 2026 fixed-point theorem. No compactness, convexity or completeness is required for the pairwise distance law.

The exact conclusions are:

**Distance synchronization.** For all \(x,y\in F\), there exists \(c\ge0\) with
\[
(\|x_1-y_1\|_1,\ldots,\|x_N-y_N\|_N)=cu.\tag{2}
\]
In particular each coordinate projection is injective on \(F\), and for any \(i,j\) its transition between coordinate images scales all distances by \(u_j/u_i\).

**Affine fixed-set geometry.** If \(K\) is convex and every \(X_i\) is strictly convex, then \(F\) is convex. Each \(\pi_i(F)\) is convex and every transition \(\pi_j\circ(\pi_i|_F)^{-1}\) is an affine, \(u_j/u_i\)-scaled isometry. Whenever all coordinates are finite dimensional, this implies
\[
\dim_{\mathbb R}\operatorname{aff}F\le\min_i\dim_{\mathbb R}X_i.\tag{3}
\]
The bound is attainable for any common finite coordinate dimension, using a stochastic averaging operator on a product of Euclidean balls (details below).

**Exact scalar classification and realization.** If \(X_i=\mathbb R\) for all \(i\), and \(F\) has two distinct members, there are \(a_0\in\mathbb R^N\) and \(\varepsilon\in\{-1,1\}^N\) such that
\[
F\subseteq a_0+\mathbb R(\varepsilon_1u_1,\ldots,\varepsilon_Nu_N).\tag{4}
\]
This holds without convexity of \(K\). If \(K\) is convex and closed, \(F\) is a closed interval (possibly a point, an unbounded interval or the whole line) on such a line. Conversely, on the full-dimensional box \(K_u=\{x\in\mathbb R^N:|x_i|\le u_i\}\), every sign vector \(\varepsilon\) and every closed interval \([a,b]\subseteq[-1,1]\) arise as exactly
\[
F=\{t(\varepsilon_1u_1,\ldots,\varepsilon_Nu_N):a\le t\le b\}.\tag{5}
\]
This converse includes singleton intervals.

**A posteriori synchronization.** For any \(x,y\in K\), define
\[
d_i=\|x_i-y_i\|_i,\quad e_i=\|T_i(x)-x_i\|_i+\|T_i(y)-y_i\|_i,\quad c=w^{\mathsf T}d,
\]
and \(Z=I-A+uw^{\mathsf T}\), \(\|z\|_{1,w}=\sum_iw_i|z_i|\). The matrix \(Z\) is invertible and
\[
\boxed{\quad\|d-cu\|_{1,w}\le2\|Z^{-1}\|_{1,w\to1,w}\sum_iw_ie_i.\quad}\tag{6}
\]
The coefficient is explicit and finite; it is not asserted to be optimal.

## Proof

**1. Perron saturation.** For \(x,y\in F\) define \(d_i=\|x_i-y_i\|_i\). The hypothesis gives \(0\le d\le Ad\) entrywise. Because \(w\) has strictly positive coordinates and \(w^{\mathsf T}A=w^{\mathsf T}\), the nonnegative vector \(Ad-d\) has weighted sum zero and hence vanishes coordinate by coordinate. Thus \(Ad=d\). The Perron eigenvalue of an irreducible nonnegative matrix is algebraically simple; its eigenspace at \(1\) is \(\mathbb R u\). Since \(d\ge0\), we obtain \(d=cu\) for some \(c\ge0\). In particular, if any distance coordinate is zero then all are zero, proving injectivity of every coordinate projection. Dividing (2) for two coordinates gives the scaled isometry statement.

**2. Convexity and affine graphs.** Let \(x,y\in F\), \(0<t<1\), and \(z=(1-t)x+ty\in K\). Applying (1) to \((z,x)\) and \((z,y)\) and using (2), for every \(i\) we obtain
\[
\|T_i z-x_i\|_i\le t\|y_i-x_i\|_i,\qquad
\|T_i z-y_i\|_i\le(1-t)\|y_i-x_i\|_i.
\]
The triangle inequality between the endpoints forces equality in both bounds. In a strictly convex normed space the unique point simultaneously at those two respective distances from \(x_i,y_i\) is \((1-t)x_i+ty_i=z_i\). (When the endpoints coincide, both bounds force the same conclusion.) Thus \(Tz=z\), so \(F\) is convex. Since every coordinate projection restricts to an injective affine map on the convex set \(F\), the inverse from its coordinate image is affine; composing with any other coordinate projection yields an affine transition map. Its distance scaling follows from (2). The affine-dimension bound follows from injectivity of these affine coordinate maps.

For sharpness of the bound let all \(X_i\) be a common finite-dimensional real Hilbert space \(H\). Set \(p_{ij}=a_{ij}u_j/u_i\). Every row sum of \(P=(p_{ij})\) equals \(1\). On \(K=\prod_i\{x_i\in H:\|x_i\|\le u_i\}\), put \(T_i(x)=\sum_ja_{ij}x_j\). The triangle inequality verifies (1), and row-stochastic averaging in normalized coordinates shows \(T(K)\subseteq K\). Every fixed point is \((u_i v)_i\) with \(\|v\|\le1\): to prove this, take a unit real-linear functional maximizing \(\|v_i\|\) among normalized fixed coordinates, and propagate equality by irreducibility, or apply the elementary Markov maximum principle to each real coordinate in an orthonormal basis. Hence \(F\) is a diagonal copy of the full ball of \(H\), with affine dimension \(\dim_{\mathbb R}H\).

**3. Scalar line rigidity without convexity.** For real scalar coordinates choose distinct fixed points \(x,y\). Equation (2) gives \(y_i-x_i=\varepsilon_i c u_i\), with \(c>0\) and signs \(\varepsilon_i\). If \(z\in F\), the equality of all relative coordinate distances for the pairs \((z,x)\) and \((z,y)\) determines each scalar \(z_i\) uniquely from \(z_1\): the two distances to the distinct anchors \(x_i,y_i\) must be in the same ratios as those to \(x_1,y_1\). Explicitly, with \(t=(z_1-x_1)/(y_1-x_1)\), the unique solution is \(z_i=x_i+t(y_i-x_i)\). Thus all fixed points lie on the affine line through \(x,y\). If \(K\) is convex, Part 2 makes \(F\) convex; if \(K\) is closed, continuity from (1) makes \(F\) closed, giving the claimed interval.

**4. Every sign/interval is attainable.** Fix \(\varepsilon\in\{-1,1\}^N\) and \(-1\le a\le b\le1\), and let \(P=(p_{ij})\) be the irreducible row-stochastic matrix from Part 2. For \(x\in K_u\), write \(t_i=\varepsilon_i x_i/u_i\), let \(h(s)=\min\{b,\max\{a,s\}\}\), and define
\[
T_i(x)=\varepsilon_i u_i\,h\Big(\sum_jp_{ij}t_j\Big).\tag{7}
\]
Since \(h\) is nonexpansive on \(\mathbb R\), this maps the entire box into itself and satisfies
\[
|T_i(x)-T_i(y)|\le u_i\sum_jp_{ij}|t_j(x)-t_j(y)|=\sum_j a_{ij}|x_j-y_j|.
\]
For a fixed point, \(t_i=h((Pt)_i)\in[a,b]\). Let \(M=\max_i t_i\). If \(M=a\), every coordinate equals \(a\). Otherwise choose \(i\) with \(t_i=M>a\); since \((Pt)_i\le M\le b\), equality \(h((Pt)_i)=M\) implies \((Pt)_i=M\). Every \(j\) with \(p_{ij}>0\) must therefore have \(t_j=M\). Irreducibility propagates this equality to all coordinates, so \(t\) is constant. Conversely every constant vector \(t_i=s\in[a,b]\) is fixed because \(P\) is row-stochastic and \(h(s)=s\). This gives exactly (5), for every \(A\) and sign vector. With reducible \(A=I_N\) and \(T=I\) on a box, the fixed set can instead be full-dimensional, demonstrating the genuine role of irreducibility.

**5. Residual stability.** For arbitrary \(x,y\in K\), triangle inequalities and (1) imply \(d\le Ad+e\). Write \(q=(I-A)d\), so \(q_i\le e_i\) and \(w^{\mathsf T}q=0\). Therefore
\[
\|q\|_{1,w}=2\sum_iw_i(q_i)_+\le2\sum_iw_i e_i.
\]
The Perron eigenvalue \(1\) is simple; hence \(Z=I-A+uw^{\mathsf T}\) is invertible (it equals the identity on \(\mathbb R u\) and equals \(I-A\) on \(\ker w^{\mathsf T}\)). With \(c=w^{\mathsf T}d\) we have \(Z(d-cu)=q\), giving (6) by the induced operator-norm inequality.

## Verification

The derivation is self-contained once the classical Perron–Frobenius theorem is used. In particular, no finite sample proves the universal assertions. The accompanying standalone Python checker uses exact rational arithmetic for an irreducible weighted three-cycle, checks left/right Perron normalization, and exhaustively tests a finite input grid for three clipping intervals and all eight sign vectors. This is consistency evidence only. The algebraic steps in Parts 1–5 establish the all-dimensional theorem. No computational or external certification of novelty is claimed.

## Relationship to prior work

Ćwiszewski and Kryszewski (2026) prove fixed-point existence for coordinatewise Lipschitz mappings with \(r(A)\le1\), including reducible systems, and discuss Perron-adapted norms. The present result **does not claim that existence or matrix scalarization is new**. It addresses fixed-set geometry, exact real-scalar classification with converse construction, and a posteriori synchronization at the irreducible threshold. Bruck (1973) studies nonexpansive fixed-point sets and retractions in general Banach spaces; his general conclusions do not themselves determine the Perron-coordinate distance ratios or the clipped realization of every signed interval. Ezearn (2015) studies higher-order Lipschitz and contraction properties, not the geometry of the present coordinatewise fixed sets. The needed Perron eigenvector simplicity and the strictly convex triangle-equality argument are classical tools.

## Limitations

The fixed-set rigidity assumes a **single irreducible nonnegative control matrix** with spectral radius exactly \(1\), not merely an upper spectral estimate from different matrices for different point pairs. Strict convexity is used only for the convex affine-graph conclusion; the distance law and scalar collinearity require no such assumption. Fixed points need not exist for arbitrary nonconvex \(K\). For closed convex but unbounded real-scalar \(K\), the interval may be unbounded. The resolvent coefficient is finite but not necessarily best possible. A priori publication priority cannot be established from finite literature searches; an older formulation in consensus/nonlinear fixed-point literature may cover some components.

## References

1. A. Ćwiszewski and W. Kryszewski, *A Spectral Approach to Fixed Points in Product Spaces*, arXiv:2610.22666, first submitted 2026-10-15. https://arxiv.org/abs/2610.22666 .
2. R. E. Bruck, *Properties of Fixed-Point Sets of Nonexpansive Mappings in Banach Spaces*, Transactions of the American Mathematical Society **179** (1973), 251–262. DOI:10.1090/S0002-9947-1973-0324491-8.
3. J. Ezearn, *Higher-order Lipschitz mappings*, Fixed Point Theory and Applications **2015**, article 88 (2015). DOI:10.1186/s13663-015-0334-1.
4. R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013 (classical Perron–Frobenius theory).
