# Sharp five-half-power endpoint and marked ellipsoid law for four spherical chord-energy points

## Finding

Let \(X_1,X_2,X_3,X_4\) be independent, normalized surface-area-uniform points on the unit sphere \(S^2\subset\mathbb R^3\). Let
\[
L=\sum_{1\le i<j\le4}\|X_i-X_j\|_2,\qquad M=4\sqrt6.
\]
The maximum \(M\) and its regular-tetrahedron equality case are classical; neither is claimed as new. The present endpoint law is
\[
\boxed{\Pr\{L>M-t\}=K t^{5/2}+o(t^{5/2}),\qquad
K=\frac{256\,2^{1/4}3^{3/4}\sqrt5}{3375}\approx0.45977952817530277.}
\]

There is a corresponding *marked conditional limit in total variation*, which describes the complete local shape of exceptionally large-energy configurations. Fix the first point at the north pole by a common rotation, and rotate azimuth so the second point has longitude zero. Put \(u=X_1\cdot X_2\), \(v=X_1\cdot X_3\), \(w=X_1\cdot X_4\); let \(p,q\in[0,2\pi)\) be the longitudes of the third and fourth points relative to the second, and write \(Y=(u,v,w,p,q)\). The two maximizing coordinates are
\[
y_+=(-\tfrac13,-\tfrac13,-\tfrac13,\tfrac{2\pi}3,\tfrac{4\pi}3),\qquad
y_-=(-\tfrac13,-\tfrac13,-\tfrac13,\tfrac{4\pi}3,\tfrac{2\pi}3).
\]
Let \(H_+\) be the positive-definite Hessian matrix displayed below, let \(D=\operatorname{diag}(1,1,1,-1,-1)\), and set \(H_-=D H_+D\). For each sufficiently small \(t>0\), on the event \(\{L>M-t\}\), there is a unique sign \(\sigma_t\in\{+,-\}\) naming the nearby maximizing configuration. Using locally unwrapped angle differences, set
\[
Z_t=(2t)^{-1/2}H_{\sigma_t}^{1/2}(Y-y_{\sigma_t}).
\]
Then
\[
\boxed{(\sigma_t,Z_t)\mid\{L>M-t\}\ \xrightarrow{\ \mathrm{TV}\ }\
(\operatorname{Bernoulli}(\tfrac12),\operatorname{Unif}(B_5)),}
\]
where \(B_5\) is the closed five-dimensional Euclidean unit ball, and the two limiting coordinates are independent. This is a distributional statement on the *marked coordinate system*, not on an unaligned labeled tetrahedron.

## Assumptions and scope

All four vertices are i.i.d. with respect to normalized two-dimensional Hausdorff measure on the sphere; edges are Euclidean chords, not great-circle arcs. The cutoff is the **absolute** (not relative) deficit \(t>0\). The angle-coordinate map is defined almost everywhere; its pole/branch-cut exceptions are probability zero. Positive square roots of symmetric positive-definite matrices are intended. No finite-threshold equality or error rate beyond \(o(t^{5/2})\) is claimed.

## Proof

**Step 1: Deterministic maximum and isolated configurations.** For any four unit vectors,
\[
\sum_{i<j}\|X_i-X_j\|_2^2=16-\Big\|\sum_i X_i\Big\|_2^2.
\]
Cauchy–Schwarz therefore gives \(L\le\sqrt{6(16-\|\sum_iX_i\|^2)}\le4\sqrt6\). Equality entails both zero vector sum and six equal chord lengths, hence \(X_i\cdot X_j=-1/3\) for every \(i\ne j\). The resulting Gram matrix has rank three and gives a labeled regular tetrahedron, unique up to orthogonal transformation. The gauge fixing above leaves precisely the two isolated maxima \(y_+\) and \(y_-\).

**Step 2: Exact probability measure.** If \(z\) is the cosine of polar angle, the normalized spherical-area density is \(\tfrac12\,dz\,d\theta/(2\pi)\). Rotational invariance lets us fix \(X_1\) to the pole and \(X_2\)'s azimuth to zero. The five remaining coordinates \((u,v,w,p,q)\) have the constant joint density
\[
\rho=\frac1{32\pi^2}\quad\text{on }(-1,1)^3\times[0,2\pi)^2.
\]
There is no remaining rotation volume or unordered-label factor.

**Step 3: Explicit Hessian.** The six inner products are
\[
\begin{aligned}
g_1&=u,&g_2&=v,&g_3&=w,\\
g_4&=uv+\sqrt{(1-u^2)(1-v^2)}\cos p,\\
g_5&=uw+\sqrt{(1-u^2)(1-w^2)}\cos q,\\
g_6&=vw+\sqrt{(1-v^2)(1-w^2)}\cos(p-q).
\end{aligned}
\]
Define \(F(Y)=M-\sum_{j=1}^6\sqrt{2-2g_j(Y)}\). At either maximum each \(g_j=-1/3\). With \(a=\sqrt{3/8}\), the chain rule yields the exact finite expression
\[
D^2F=a^3 J^{\mathsf T}J+a\sum_{j=1}^6D^2g_j,
\]
where the \(j\)th row of \(J\) is \(\nabla g_j\). Substituting \(y_+\) gives
\[
H_+=\begin{pmatrix}
\frac{27\sqrt6}{64}&\frac{33\sqrt6}{128}&\frac{33\sqrt6}{128}&-\frac{\sqrt2}{16}&\frac{\sqrt2}{16}\\
\frac{33\sqrt6}{128}&\frac{27\sqrt6}{64}&\frac{33\sqrt6}{128}&0&-\frac{\sqrt2}{16}\\
\frac{33\sqrt6}{128}&\frac{33\sqrt6}{128}&\frac{27\sqrt6}{64}&\frac{\sqrt2}{16}&0\\
-\frac{\sqrt2}{16}&0&\frac{\sqrt2}{16}&\frac{\sqrt6}{3}&-\frac{\sqrt6}{6}\\
\frac{\sqrt2}{16}&-\frac{\sqrt2}{16}&0&-\frac{\sqrt6}{6}&\frac{\sqrt6}{3}
\end{pmatrix}.
\]
The five leading principal minors are
\[
\frac{27\sqrt6}{64},\quad\frac{5481}{8192},\quad
\frac{19845\sqrt6}{131072},\quad\frac{4725}{16384},\quad
\boxed{\det H_+=\frac{1125\sqrt6}{16384}}.
\]
All are strictly positive, so the Hessian is positive definite. Reflecting both azimuths maps the two critical points, hence \(H_-=D H_+D\) and \(\det H_-=\det H_+\).

**Step 4: Local volume with global justification.** Analyticity of \(F\) near each maximum and vanishing of its first derivative give
\[
F(y_s+h)=\tfrac12h^{\mathsf T}H_sh+O(\|h\|^3),\qquad s\in\{+,-\}.
\]
Choose disjoint compact local neighborhoods of the two maxima. The previous sharp maximum argument and compactness of the spherical configuration space imply that for sufficiently small \(t\), the entire event \(F<t\) lies inside these neighborhoods. Positivity of \(H_s\) bounds \(\|h\|=O(\sqrt t)\) there. Under \(z=(2t)^{-1/2}H_s^{1/2}h\), the event indicators converge a.e. to \(\mathbf1_{\|z\|<1}\), with a common bounded support. Their integrals thus converge by dominated convergence. Since \(\operatorname{vol}(B_5)=8\pi^2/15\),
\[
\Pr(F<t)\sim
2\rho\,(2t)^{5/2}\frac{8\pi^2/15}{\sqrt{\det H_+}}
=\frac{2\sqrt2}{15\sqrt{\det H_+}}t^{5/2}.
\]
Direct simplification of the determinant gives the displayed radical formula for \(K\).

**Step 5: Total-variation marked limit.** The exact preconditioning Jacobian in each branch is \((2t)^{5/2}/\sqrt{\det H_s}\). Both Jacobians and original densities match, so both branches have asymptotic probability \(1/2\). The rescaled conditional densities converge pointwise a.e. and in \(L^1\), again by dominated convergence after localization. Hence their total-variation distance to the equally weighted uniform laws on \(B_5\) tends to zero. This proves the full stated joint limit, not only weak convergence.

## Verification

The accompanying `CHECK.py` symbolically rebuilds the six inner products, evaluates the 5-by-5 Hessian using independently differentiated expressions, and confirms all entries, every positive leading principal minor, the exact determinant, and the exact simplified coefficient. It then tests the local-volume asymptotic using reproducibly seeded uniform five-ball samples at \(t=0.002\) and \(t=0.0002\); the observed ratios to the limiting coefficient were approximately \(1.00606\) and \(1.00530\). Numerical checks support but do not replace the global uniqueness, Taylor, and dominated-convergence proof steps. Run `python CHECK.py` with Python, NumPy and SymPy.

## Relationship to prior work

Einar Hille (1966), especially Section 4, establishes deterministic regular-simplex extremality of the sum of chord distances; that classical extremum is fully subsumed and excluded from the new claim. Glyn Harman (1982) develops discrepancy-based bounds for sums of distances on spheres, without stating this four-point fixed-sample tail or its marked conditional law in the inspected full text. József Beck (1984) discusses maximizing sphere distance sums; its accessible abstract does not settle whether the complete text contains a related local calculation. Simarova (2021) develops upper extremes for generalized perimeters of *cyclic planar polygons*, and not for the six-edge energy of four points on a two-sphere. Akopyan–Edelsbrunner–Nikitenko (2021) give expectations for total edge length of random spherical polytopes and large-sample comparisons; their inspected Sections 6–7 do not establish the local four-point upper-tail law. Existing related research records address cubic moments of spherical chord energy or rare spherical-cap coverage near tetrahedral geometry, not the five-half-power energy endpoint or marked ellipsoid.

## Limitations

The result treats exactly four i.i.d. uniform points on the unit two-sphere and the unweighted sum of all six **Euclidean** edge lengths. It does not establish the full distribution, rates of convergence, higher-order coefficients, or analogous results for other dimensions and energies. The original full text of Beck (1984) was inaccessible after open-access attempts and institutional-access connection was unavailable; unindexed prior art remains possible. A self-review and computational reproduction are not independent mathematical validation, and historical priority is provisional.

## References

1. E. Hille, *Some geometric extremal problems*, Journal of the Australian Mathematical Society **6** (1966), 122–128. DOI: 10.1017/S1446788700004067. [Full text inspected, especially pp. 122–124 and 127.]
2. G. Harman, *Sums of distances between points of a sphere*, International Journal of Mathematics and Mathematical Sciences **5** (1982), 707–714. DOI: 10.1155/S0161171282000647. [Public full text inspected.]
3. J. Beck, *Sums of distances between points on a sphere—an application of the theory of irregularities of distribution to discrete geometry*, Mathematika **31** (1984), 33–41. DOI: 10.1112/S0025579300010639. [Metadata and abstract inspected; full text inaccessible.]
4. E. N. Simarova, *Limit theorems for generalized perimeters of random inscribed polygons. II*, Vestnik of Saint Petersburg University **8** (2021), 101–110. DOI: 10.21638/spbu01.2021.109. [Full original text inspected.]
5. A. Akopyan, H. Edelsbrunner, A. Nikitenko, *The beauty of random polytopes inscribed in the 2-sphere*, Experimental Mathematics (first public 2020 preprint; journal 2021). DOI: 10.1080/10586458.2021.1980459; arXiv:2007.07783. [Full text inspected, Sections 6–7.]
