# Vanishing hub-facet area versus half-weight sphere contact in wheel Laplacian simplices

## Finding
For each integer \(m\ge4\), let \(W_m=K_1\vee C_m\) be the unweighted simple wheel graph with a hub \(h\), \(m\) cyclically arranged rim vertices, and \(n=m+1\). Let \(L_m\) be its ordinary combinatorial graph Laplacian. The **canonical Euclidean Laplacian simplex** is
\[
T_m=\operatorname{conv}\{L_me_h,L_me_1,\ldots,L_me_m\}
\subset\mathbf1^\perp\subset\mathbb R^n,
\]
with the Euclidean metric inherited from the original \(n\) orthonormal coordinate axes (not a non-orthogonal lattice reduction). It has dimension \(m\). Let \(V_m\), \(S_m\), \(r_m\), and \(R_m\) denote its intrinsic \(m\)-volume, full Euclidean \((m-1)\)-surface area, largest inscribed-ball radius, and minimum enclosing-ball radius.

Put
\[
 a_m=\frac{\sqrt m}{(m+1)^{3/2}},\qquad
 b_m=\left[\frac{1}{m(m+1)^3}+\frac1m\sum_{k=1}^{m-1}\frac{1}{\left(3-2\cos\frac{2\pi k}{m}\right)^2}\right]^{1/2}.
\tag{1}
\]
Write \(v_h=L_me_h\). The hub-opposite facet has area \(mV_ma_m\), and **every** rim-opposite facet has area \(mV_mb_m\). The exact intrinsic volume and surface-to-volume ratio are
\[
 V_m=\frac{(m+1)^{3/2}}{m!}\left(\rho^{-m}+\rho^m-2\right),\qquad
 \frac{S_m}{V_m}=m(a_m+mb_m),\qquad
 \rho=\frac{3-\sqrt5}{2}.
\tag{2}
\]
All \(m+1\) facets touch the **unique** largest inscribed sphere, with
\[
 \boxed{r_m=\frac1{a_m+mb_m}},\qquad
 \boxed{c_m^{\mathrm{in}}=\frac{a_m-b_m}{a_m+mb_m}\,v_h}.
\tag{3}
\]
All \(m+1\) vertices touch the **unique** minimum enclosing sphere, with
\[
 \boxed{c_m^{\mathrm{out}}=t_mv_h},\qquad
 t_m=\frac{m(m+1)-12}{2(m+1)^2},
\]
\[
 \boxed{R_m=\sqrt{m(m+1)}(1-t_m)
 =\frac{\sqrt m\,(m^2+3m+14)}{2(m+1)^{3/2}}}.
\tag{4}
\]
The unique barycentric supporting probability measure on its contact vertices assigns mass
\[
 \boxed{p_m=\frac{1+mt_m}{m+1}}
\tag{5}
\]
to the hub vertex \(v_h\), and mass \((1-p_m)/m\) to **each** rim vertex. Thus the same distinguished hub is strongly suppressed in one metric sense and strongly represented in the dual enclosing-sphere support certificate.

Precisely, letting \(\beta=\sqrt{3/(5\sqrt5)}\), the sharp limits along integers \(m\to\infty\) are
\[
 \boxed{\lim_{m\to\infty}m^2\frac{\operatorname{area}(F_h)}{S_m}
       =\frac1\beta=1.930486975480\ldots},
 \qquad
 \boxed{\lim_{m\to\infty}p_m=\frac12},
\tag{6}
\]
\[
 \boxed{\lim_{m\to\infty}m r_m=\frac1\beta},\qquad
 \boxed{\lim_{m\to\infty}\frac{R_m}{m}=\frac12},\qquad
 \boxed{\lim_{m\to\infty}\frac{R_m}{m^2r_m}=\frac\beta2=0.259002006411\ldots}.
\tag{7}
\]
Here \(F_h\) is the facet opposite the hub column. In particular its fraction of boundary area vanishes quadratically, while the hub carries half of the unique positive contact measure for the minimum enclosing sphere. The claim concerns this coupled **facet-area / enclosing-contact asymptotic**, together with its exact finite-size geometry; no new general formula for arbitrary graph simplices is asserted.

## Assumptions and scope
The graph is finite, connected, simple, unweighted, and has \(m\ge4\) rim vertices. The tetrahedral case \(m=3\) is excluded because it is the complete graph and already belongs to the vertex-transitive theory. Graph coordinates are ordered as hub and rim. All distances, face areas, and volume use the intrinsic Euclidean metric on the zero-sum hyperplane, without deleting a coordinate and pretending the remaining basis is orthonormal.

A "supporting probability measure" means nonnegative weights on the vertices lying on the minimum enclosing sphere, summing to one and having barycenter equal to its center. The weights in (5) are unique because the Laplacian columns are affinely independent. They are not uniform boundary-area weights, so (6) compares two genuinely different geometric measurements.

## Proof
**1. Full Euclidean simplex and exact facet normalization.** Connectedness gives \(\ker L_m=\operatorname{span}\{\mathbf1\}\), so the \(n\) columns \(v_i=L_me_i\) are affinely independent in \(\mathbf1^\perp\) and sum to zero. Let \(L_m^+\) be the Moore--Penrose pseudoinverse. Every \(x\in\mathbf1^\perp\) has the unique barycentric coordinates
\[
 \lambda_i(x)=\frac1n+\langle L_m^+e_i,x\rangle,
 \quad \sum_i\lambda_i(x)=1,\quad x=\sum_i\lambda_i(x)v_i.
\tag{8}
\]
The facet opposite \(v_i\) is \(\lambda_i(x)=0\) and its intrinsic normal is \(z_i=L_m^+e_i\). As \(\lambda_i(v_i)=1\), its opposite-vertex altitude is \(1/\|z_i\|\). Thus, since the dimension is \(m\),
\[
\operatorname{area}(F_i)=m V_m\|z_i\|.
\tag{9}
\]
This standard general-simplex/pseudoinverse step is included only as an ingredient, not claimed original.

**2. Two pseudoinverse norms.** The vector \(w=(m,-1,\ldots,-1)\) is an eigenvector of \(L_m\) with eigenvalue \(n\). Its squared norm is \(mn\). The remaining \(m-1\) orthogonal Fourier eigenvectors have hub coordinate zero, sum-zero rim coordinates, and eigenvalues
\[
 \mu_k=3-2\cos(2\pi k/m),\quad 1\le k\le m-1.
\tag{10}
\]
The squared projection of \(e_h\) on the unit vector \(w/\sqrt{mn}\) is \(m/n\), while for any rim coordinate it is \(1/(mn)\). For a fixed rim coordinate, the squared projection on each normalized nonconstant rim Fourier frequency is \(1/m\) (with the usual conjugate-pair real interpretation). Applying \((L_m^+)^2\) therefore yields
\[
 \|z_h\|^2=\frac{m}{n^3}=a_m^2,\qquad
 \|z_i\|^2=\frac1{mn^3}+\frac1m\sum_{k=1}^{m-1}\mu_k^{-2}=b_m^2.
\tag{11}
\]
Substitution into (9) gives the two facet-area classes and \(S_m/V_m=m(a_m+mb_m)\).

**3. Intrinsic volume.** The restriction of \(L_m\) to \(\mathbf1^\perp\) has determinant \(\prod_{\lambda>0}\lambda=n\tau(W_m)\), by the matrix-tree theorem, where \(\tau\) is the number of spanning trees. The standard simplex \(\operatorname{conv}(e_1,\ldots,e_n)\) inside \(\mathbf1^\perp\) has intrinsic volume \(\sqrt n/m!\). Therefore \(V_m=n^{3/2}\tau(W_m)/m!\). Deleting the hub row and column from \(L_m\) gives the cyclic matrix \(3I-A(C_m)\), whose determinant is
\[
 \tau(W_m)=\prod_{k=0}^{m-1}\left(3-2\cos\frac{2\pi k}{m}\right)
 =\rho^{-m}+\rho^m-2.
\tag{12}
\]
The final identity follows either from the cyclic tridiagonal determinant recurrence or \(2T_m(3/2)-2\), where \(T_m\) is the Chebyshev polynomial of the first kind. This proves (2).

**4. Unique insphere.** An intrinsic Euclidean ball \(B(c,r)\) is contained in the simplex exactly when \(\lambda_i(c)\ge r\|z_i\|\) for every \(i\). Summing the inequalities gives \(1\ge r(a_m+mb_m)\). At equality all barycentric coordinates are fixed, with \(\lambda_h(c)=a_m/(a_m+mb_m)\) and each rim coordinate \(\lambda_i(c)=b_m/(a_m+mb_m)\). Such a center exists and equals
\[
 c=\frac{a_m v_h+b_m\sum_i v_i}{a_m+mb_m}
  =\frac{a_m-b_m}{a_m+mb_m}v_h,
\]
because \(\sum_i v_i=-v_h\). Equality forces all barycentric coordinates, hence the center, uniquely. This proves (3), including tangency of every facet.

**5. Unique minimum enclosing sphere and its positive contact certificate.** Directly from the wheel graph Laplacian, the hub column has squared length \(\|v_h\|^2=m(m+1)\), every rim column has squared length \(12\), and \(\langle v_h,v_i\rangle=-(m+1)\). A candidate center \(tv_h\) consequently has squared distances
\[
 d_h(t)^2=m(m+1)(1-t)^2,
 \quad d_r(t)^2=12+2(m+1)t+m(m+1)t^2.
\tag{13}
\]
They are equal exactly at \(t=t_m\) in (4). For \(m\ge4\), \(0<t_m<1\), so their common value has radius \(R_m\) in (4). Every vertex is a contact, not merely a vertex inside the ball.

Set \(p_m=(1+mt_m)/(m+1)\). Then \(0<p_m<1\) and the weights \(p_m\) at the hub and \((1-p_m)/m\) on the rim have center
\[
 p_m v_h+\frac{1-p_m}{m}\sum_i v_i
 =\frac{(m+1)p_m-1}{m}v_h=t_mv_h=c_m^{\mathrm{out}}.
\tag{14}
\]
For any other center \(z\) in the ambient space, weighted variance decomposition gives
\[
 \sum_i w_i\|v_i-z\|^2
 =R_m^2+\|z-c_m^{\mathrm{out}}\|^2.
\tag{15}
\]
Thus some vertex lies at squared distance at least the right-hand side; no smaller enclosing ball exists, and equality of the optimal radius forces \(z=c_m^{\mathrm{out}}\). The unique barycentric contact weights are those in (14), by affine independence. This proves (4)--(5) without assuming in advance that a symmetric center is globally optimal.

**6. Sharp two-scale asymptotics.** The expression \(b_m^2\) in (1) is a periodic Riemann sum with its zero-frequency term omitted. Consequently
\[
 b_m^2\longrightarrow
 \frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{(3-2\cos\theta)^2}
 =\frac{3}{5\sqrt5}=\beta^2.
\tag{16}
\]
For the integral, differentiate \((2\pi)^{-1}\int_0^{2\pi}(s-2\cos\theta)^{-1}d\theta=(s^2-4)^{-1/2}\) with respect to \(s\) and set \(s=3\). Meanwhile \(m a_m\to1\), \(t_m\to1/2\), and \(p_m\to1/2\). Equations (3)--(5) now give \(m r_m\to1/\beta\), \(R_m/m\to1/2\) and \(R_m/(m^2r_m)\to\beta/2\). Finally the hub-facet surface fraction is \(a_m/(a_m+mb_m)\), and
\[
 m^2\frac{a_m}{a_m+mb_m}
 =\frac{m a_m}{b_m+a_m/m}\longrightarrow\frac1\beta.
\]
This establishes (6)--(7) and the claimed geometric contrast for the entire infinite family.

## Verification
The standalone `verify.py` reconstructs wheel Laplacian matrices directly from graph edges and checks \(3\le m\le10\) (the smaller tetrahedral case is included only as a computational boundary test). It independently computes full and opposite-facet Euclidean Gram determinants with exact integer arithmetic, verifies the spanning-tree volume, checks the incenter by direct pseudoinverse halfspace clearances, and checks the circumball distances and positive weighted-center identity. It also compares perturbed minimax centers and the asymptotic formulas at four larger sizes up to \(m=20000\). The script reports `WHEEL_LAPLACIAN_METRIC_PASS checks=132`. The proof, not these finite checks, establishes the all-integer assertions.

## Relationship to prior work
Braun and Meyer [1] introduced Laplacian simplices, their spanning-tree normalized volume and lattice-theoretic properties; Meyer and Pllaha [2] developed their coding-theoretic connections. Neither primary source states the metric two-contact asymptotic (6). A published result [3] gives pseudoinverse facet normals and spectral Euclidean radii for **vertex-transitive** graph Laplacian simplices, while the wheel with at least four rim vertices is not vertex-transitive. That work's general barycentric-normal identity is reused and credited here, and no novelty is claimed for it. A published prism--Möbius result [4] compares inradii of two distinct vertex-transitive cubic graph families and neither addresses wheel columns nor hub-facet area. A published wheel **edge-polytope** result [5] concerns the convex hull of \(e_i+e_j\) over graph edges, not the present convex hull of Laplacian columns; the vertices, facets and metrics differ. Published complete-multipartite Laplacian-ball formulas [6] concern a different graph family and do not cover \(K_1\vee C_m\) for \(m\ge4\).

The current distinctive claim is the **exact and sharp surface-area suppression at the hub-opposite facet alongside the macroscopic half-weight minimum-sphere contact at the hub vertex**, including explicit finite-size in-/enclosing spheres. A general formula for simplex radii alone does not state that discrepancy, its order, or its constants. The literature comparison is a best-knowledge priority assessment, not a mathematical proof that no equivalent unpublished or unindexed work exists.

## Limitations
The asymptotic assertion concerns only the standard unweighted wheels \(W_m\) and the canonical Euclidean Laplacian-column realization. Non-orthogonal lattice coordinate changes generally alter all metric quantities. The result does not determine John or Löwner ellipsoids or extend to arbitrary sparse graph families. Its general-simplex ingredients and matrix-tree and Fourier identities are classical. Priority for the particular coupled boundary/contact law is provisional, and no independent mathematical audit has been performed.

## References
1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085 (first public 2017-06-21), https://arxiv.org/abs/1706.07085.
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960 (first public 2018-09-09), https://arxiv.org/abs/1809.02960.
3. *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, public research note, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-vertex-transitive-laplacian-simplices-have-spectral-inradii-and--841b23980b76/RESULT.md.
4. *An exponentially small inradius gap between prism and Möbius Laplacian simplices*, public research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-exponentially-small-inradius-gap-between-prism-and-m-bius-lap--fce010f93d91/RESULT.md.
5. *An exceptional rectangle of incenters for ordinary wheel edge polytopes*, public research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-an-exceptional-rectangle-of-incenters-for-ordinary-wheel-edge-po--13f88e3d79e2/RESULT.md.
6. *Water-filling contact strata of complete multipartite Laplacian simplices*, public research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-water-filling-contact-strata-of-complete-multipartite-laplacian--e213ee1cfdd8/RESULT.md.
