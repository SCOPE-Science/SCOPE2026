# Exact all-contact Löwner ellipsoid of star cosmological polytopes

## Finding

Let \(P_m\) be the canonical Euclidean cosmological polytope of the star \(K_{1,m}\), with \(m\ge1\), as defined below. Its intrinsic minimum-volume containing (Löwner) ellipsoid is unique, is centered at the uniform coordinate vector \(c=(2m+1)^{-1}\mathbf1\), and touches **all and only** its \(3m\) vertices. In its \(2m\)-dimensional affine span the ellipsoid has squared principal semiaxes

\[
\lambda_T=\frac{4m(m+1)}{2m+1}\quad(\text{multiplicity }1),\qquad
\lambda_U=\frac{4m}{2m+1}\quad(\text{multiplicity }m-1),\qquad
\lambda_V=\frac{4(m+1)}{2m+1}\quad(\text{multiplicity }m).
\]

The \(U\) eigenspace is absent when \(m=1\). Consequently the squared-semiaxis condition number is \(m+1\) for \(m\ge2\), while it is \(1\) for \(m=1\). The ratio of intrinsic ellipsoid volume to the minimum enclosing Euclidean ball volume is exactly

\[
\rho_m=\sqrt{m+1}\left(\frac{2\sqrt{m(m+1)}}{3m+1}\right)^m,
\qquad
\rho_m\sim e^{1/6}\sqrt m\left(\frac23\right)^m.
\]

Here the previously identified ball has squared radius \(3-1/(2m+1)\). The formula quantifies the exponential saving obtained by using an ellipsoid instead of that ball, even though the entire vertex set contacts both surfaces.

## Assumptions and scope

All coordinates use the standard orthonormal basis \(h,\ell_1,\ldots,\ell_m,g_1,\ldots,g_m\) of \(\mathbb R^{2m+1}\). The hub is \(h\), the leaves are \(\ell_i\), and \(g_i\) denotes the edge joining the hub to leaf \(i\). The convex body is

\[
P_m=\operatorname{conv}\bigl\{h+\ell_i-g_i,\quad h-\ell_i+g_i,\quad -h+\ell_i+g_i:1\le i\le m\bigr\}.
\]

No projective renormalization, nonorthogonal transformation, edge weighting, or additional vertices are used. Every displayed generator has coordinate sum \(1\), so \(P_m\) lies in the hyperplane \(\mathcal H=\{x:\langle x,\mathbf1\rangle=1\}\). The affine dimension is \(2m\), and all volumes and ellipsoid semiaxes refer to the induced Euclidean metric on \(\mathcal H\). For a positive-definite operator \(Q\) on the direction space of \(\mathcal H\), the ellipsoid \(\mathcal E(c,Q)\) is defined by \(\langle x-c,Q^{-1}(x-c)\rangle\le1\).

## Proof

**1. An orthogonal two-layer decomposition.** Write

\[
s=\sum_{i=1}^m(\ell_i+g_i),\quad w_i=\ell_i-g_i,\quad u_i=\ell_i+g_i-\frac{s}{m},\quad \delta=-2h+\frac{s}{m}.
\]

The vertices are \(A_i^\pm=h\pm w_i\) and \(C_i=h+\delta+u_i\). Their hub coordinates are respectively \(1\) and \(-1\). The first layer is an \(m\)-dimensional crosspolytope, and the second an \((m-1)\)-dimensional simplex; hence all \(3m\) points are genuine vertices. Define the mutually orthogonal subspaces

\[
V=\operatorname{span}\{w_i\},\qquad U=\operatorname{span}\{u_i\},\qquad T=\operatorname{span}\{\delta\}.
\]

Their dimensions are \(m,m-1,1\), respectively, and they span the direction space \(\mathbf1^\perp\) of \(\mathcal H\). We have

\[
\|\delta\|^2=4+\frac2m,\quad \|w_i\|^2=2,\quad \|u_i\|^2=\frac{2(m-1)}m,
\quad \sum_i w_iw_i^{\mathsf T}=2\Pi_V,\quad \sum_i u_iu_i^{\mathsf T}=2\Pi_U.
\]

Here \(\Pi_V,\Pi_U,\Pi_T\) are orthogonal projectors. The \(U\) terms are zero if \(m=1\).

**2. A positive covariance certificate.** Put \(D=2m+1\), \(\alpha=(m+1)/D\), and \(\beta=m/D\). Assign weight \(\alpha/(2m)\) to every \(A_i^\pm\), and \(\beta/m\) to every \(C_i\). All weights are positive and sum to \(1\). Their weighted mean is

\[
c=h+\beta\delta=\frac{h+s}{2m+1}=\frac{\mathbf1}{D}.
\]

The weighted covariance about \(c\) is

\[
\Sigma=\alpha\beta\delta\delta^{\mathsf T}+\frac{2\beta}{m}\Pi_U+\frac{2\alpha}{m}\Pi_V.
\]

Since the affine dimension is \(d=2m\), define \(Q=d\Sigma\). Its spectral values on \(T,U,V\) are precisely \(\lambda_T,\lambda_U,\lambda_V\) stated above, all strictly positive on their respective nonzero spaces.

**3. Exact contact equalities.** For every first-layer vertex, orthogonality gives

\[
\langle A_i^\pm-c,Q^{-1}(A_i^\pm-c)\rangle
=\frac{\beta}{2m\alpha}+\frac1{2\alpha}=1.
\]

For every second-layer vertex,

\[
\langle C_i-c,Q^{-1}(C_i-c)\rangle
=\frac{\alpha}{2m\beta}+\frac{m-1}{2m\beta}=1.
\]

Thus \(\mathcal E(c,Q)\) contains all vertices, hence the full polytope, and every vertex touches its boundary. A strictly convex ellipsoid has no boundary line segment, so no nonvertex point of \(P_m\) lies on its boundary.

**4. Global optimality and uniqueness, without a symmetry assumption.** Let \(\mathcal E(z,B)\) be *any* containing ellipsoid in \(\mathcal H\) with positive-definite shape \(B\). Averaging the vertex containment inequalities with the positive weights from step 2 yields

\[
1\ge\operatorname{tr}(B^{-1}\Sigma)+\langle c-z,B^{-1}(c-z)\rangle,
\quad\text{hence}\quad \operatorname{tr}(B^{-1}Q)\le d.
\]

Applying the arithmetic-geometric mean inequality to the positive eigenvalues of \(B^{-1/2}QB^{-1/2}\) gives

\[
\frac{\det Q}{\det B}\le
\left(\frac{\operatorname{tr}(B^{-1}Q)}d\right)^d\le1.
\]

Thus \(\det B\ge\det Q\), so no containing ellipsoid has lower intrinsic volume. Equality forces \(B=Q\) and \(z=c\), proving uniqueness.

**5. Ball comparison and volume ratio.** Each vertex has squared ambient norm \(3\) and coordinate sum \(1\), giving \(\|v-c\|^2=3-1/D\). Therefore the ball with center \(c\) and squared radius \(R_m^2=3-1/D\) contains \(P_m\). The weighted mean identity also shows that every other possible center \(z\) satisfies

\[
\max_{v\in\operatorname{Vert}(P_m)}\|v-z\|^2
\ge\sum_v p_v\|v-z\|^2=R_m^2+\|z-c\|^2,
\]

so the enclosing ball is unique. The ratio of the ellipsoid and ball volumes equals \(\sqrt{\det Q}/(R_m^2)^m\), which, using the eigenvalue multiplicities, simplifies to

\[
\frac{4^m m^{m/2}(m+1)^{(m+1)/2}}{(2m+1)^m}
\left(\frac{2m+1}{2(3m+1)}\right)^m
=\sqrt{m+1}\left(\frac{2\sqrt{m(m+1)}}{3m+1}\right)^m.
\]

Finally \(\log(2\sqrt{m(m+1)}/(3m+1))=\log(2/3)+1/(6m)+O(m^{-2})\), proving the asymptotic constant \(e^{1/6}\).

## Verification

Run `python3 verify_star_cosmo.py 15` using only the Python standard library. The included exact rational checker directly rebuilds all \(3m\) original integer-coordinate vertices, confirms the affine hyperplane and norms, forms their positive weighted covariance, compares it entrywise to the proposed three-projector shape, and confirms every contact Mahalanobis square equals exactly \(1\) for \(1\le m\le15\). It separately checks the ball radius and numerical sanity of the volume ratio. These finite checks are not used in place of the all-parameter proof above.

## Relationship to prior work

Arkani-Hamed, Benincasa and Postnikov introduced the graph construction and its three vertex generators per edge in 2017. Kühne and Monin proved face descriptions and tree recursions in a 2022 preprint (later published). Their results supply the combinatorial setting, not this metric ellipsoid classification. A previously indexed statement determines the common Euclidean enclosing *ball* of connected cosmological polytopes; that ball radius is an antecedent rather than a newly claimed discovery. A separate indexed statement concerns determinants of covariance from *uniform* vertex sampling, whereas the positive Löwner certificate here uses total first-layer weight \((m+1)/(2m+1)\), not the vertex-uniform first-layer weight \(2/3\) when \(m>1\). Neither antecedent by itself determines this minimum-volume ellipsoid or exponential volume ratio. General Löwner contact optimality is classical and used, not claimed as new.

## Limitations

The theorem concerns the standard orthonormal-coordinate realization of the unweighted star graph and does not assert affine-invariant Euclidean formulas, universality for arbitrary tree shapes, or any physical observable. The underlying minimum enclosing ball is already known. Historical priority of the Löwner spectrum and volume ratio remains subject to discovery of unindexed results or more general ellipsoid theorems that imply this special case. The exact formula does not require and does not purport to provide independent validation.

## References

1. N. Arkani-Hamed, P. Benincasa and A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813, first posted 2017-09-08, Section 3, https://arxiv.org/abs/1709.02813.
2. L. Kühne and L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first posted 2022-09-16, Sections 1, 4 and 5, https://arxiv.org/abs/2209.08069.
3. *Every connected cosmological polytope has graph-independent Euclidean circumradius*, indexed 2026 result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-connected-cosmological-polytope-has-graph-independent-eucl--099bd090b126.
4. *Degree-rooted forests determine the vertex-inertia volume of cosmological polytopes*, indexed 2026 result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-degree-rooted-forests-determine-the-vertex-inertia-volume-of-cos--e97f64c007b7.
