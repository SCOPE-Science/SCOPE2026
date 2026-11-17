# An exact conditional coplanarity law and a sharp nonanalytic correction for sphere-inscribed tetrahedra

## Finding

Let \(X_1,X_2,X_3,X_4\) be independent, normalized-area-uniform points of the unit sphere \(\mathbb S^2\subset\mathbb R^3\), and put
\[
 V=\frac16\left|\det(X_2-X_1,X_3-X_1,X_4-X_1)\right|.
\]
For every \(t>0\), the **entire conditional geometry** given \(V<t\) admits the exact rejection representation described below. Its proposal distribution is a uniform oriented plane normal, a uniform signed plane height, four independent uniform angular marks on its circular section, and a uniform rescaled signed volume. The proposal acceptance probability tends to one as \(t\downarrow0\), with sharp rate
\[
 \left\|\mathcal L(\mathcal M_t\mid V<t)-\mu_0\right\|_{\mathrm{TV}}
 = c_*\sqrt t+o(\sqrt t),\qquad
 c_*=\frac{\sqrt6}{3}\frac{\Gamma(1/4)}{\Gamma(3/4)^3}.
\]
Consequently,
\[
 \Pr(V<t)=3\pi t-\pi\sqrt6\frac{\Gamma(1/4)}{\Gamma(3/4)^3}\,t^{3/2}+o(t^{3/2}).
\]
The unmarked joint weak limit for near-coplanar tetrahedra was previously obtained; it is not claimed as new. The present contribution is the **exact finite-threshold uniformly generated marked law**, the independent uniform signed-volume mark, and the sharp explicit square-root total-variation convergence rate. The scalar volume moment formula is classical.

## Assumptions and scope

The sphere has Euclidean radius one. Null events of coincident or collinear first three points are ignored. Choose independently an unbiased sign for the normal to the affine plane through \(X_1,X_2,X_3\), obtaining an oriented unit normal \(N\). Set \(H=N\cdot X_1\), \(\rho=\sqrt{1-H^2}\), and choose any measurable oriented orthonormal frame of \(N^\perp\). Let \(\Theta_i\in[0,2\pi)\) be the polar angle of the orthogonal projection of \(X_i\) onto \(N^\perp\), for \(i=1,2,3,4\). Write
\[
 T(\theta_1,\theta_2,\theta_3)=\frac12\left|\det_2(u_2-u_1,u_3-u_1)\right|,
 \quad u_i=(\cos\theta_i,\sin\theta_i), \quad A=(1-H^2)T.
\]
Here \(A\) is the Euclidean area of \(X_1X_2X_3\). For each \(t>0\) define the signed mark \(Z_t=A(N\cdot X_4-H)/(3t)\). On \(V<t\), it lies in \((-1,1)\). Denote the marked vector by \(\mathcal M_t=(N,H,\Theta_1,\Theta_2,\Theta_3,\Theta_4,Z_t)\).

Let \(\mu_0\) be the product of normalized Haar surface measure on \(N\in\mathbb S^2\), independent uniform \(H\in[-1,1]\), four independent uniform \(\Theta_i\in[0,2\pi)\), and independent uniform \(Z\in[-1,1]\). Under this proposal define
\[
 E_t=\left\{\left|H+\frac{3tZ}{(1-H^2)T(\Theta_1,\Theta_2,\Theta_3)}\right|\le1\right\};
\]
points with zero denominator have proposal measure zero. The exact identity is
\[
 \boxed{\Pr(V<t)=3\pi t\,\mu_0(E_t),\qquad
 \mathcal L(\mathcal M_t\mid V<t)=\mu_0(\,\cdot\mid E_t).}
\]
It also provides a rejection sampler for the conditional geometric marks without first generating a small-volume tetrahedron by naive rejection.

## Proof

**1. Three-point change of variables.** For three sphere-uniform points, the affine Blaschke–Petkantschin change of variables into an oriented plane and three positions on its intersection circle has a Jacobian proportional to their planar triangle area \(A\). The surface delta-functions remove the three radial Jacobians. Since \(A=(1-h^2)T\), after normalizing (and randomizing the normal's orientation) the joint distribution is
\[
 d\Pr_{N,H,\Theta_{1:3}}=d\sigma(N)\,
 \frac34(1-h^2)\,dh\,
 \frac{T(\theta_1,\theta_2,\theta_3)}{\mathbb E_0 T}
 \prod_{i=1}^3\frac{d\theta_i}{2\pi}.
\]
The expectation \(\mathbb E_0\) refers to three independent uniform circle angles. To normalize this identity, sort the three angles and use their three cyclic gaps, whose normalized vector is \(\operatorname{Dirichlet}(1,1,1)\). The oriented circle-triangle area is one half the sum of the sines of these gaps; each sine has expectation \(1/\pi\). Hence \(\mathbb E_0T=3/(2\pi)\). The height density integrates to one and gives \(\mathbb E H^2=1/5\) before rare-event conditioning.

**2. Exact conditional uniform-proposal identity.** Conditional on the first three vertices, \(U=N\cdot X_4\) is uniform on \([-1,1]\), and \(\Theta_4\) is independently uniform. The tetrahedral volume is \(V=A|U-H|/3\). Make the substitution \(U=H+3tz/A\). In the joint density the factor \((1-h^2)T\) cancels against the Jacobian \(3t/A\). Dividing the resulting unnormalized measure by the fully uniform product measure \(\mu_0\) leaves the constant \(3\pi t\), restricted exactly by \(|z|<1\) and the physical sphere constraint \(|H+3tz/A|\le1\). Therefore, for every Borel set \(B\) of marks,
\[
 \Pr(\mathcal M_t\in B,\ V<t)=3\pi t\,\mu_0(B\cap E_t).
\]
Integration and conditioning prove both exact identities.

**3. Conditional total-variation convergence.** For almost every proposal mark \((N,H,\Theta_i,Z)\), one has \(|H|<1\) and \(T>0\). Thus \(\mathbf1_{E_t}\to1\) as \(t\downarrow0\). Dominated convergence gives \(a(t):=\mu_0(E_t)\to1\). Since the conditional law has density \(\mathbf1_{E_t}/a(t)\) relative to \(\mu_0\), its total-variation distance from \(\mu_0\) is **exactly** \(1-a(t)\).

**4. Sharp first rejection correction.** Condition on \(T>0\) and put \(w=3t/T\). For \(H>0\), write \(\delta=1-H\). An outward-pointing signed mark rejects when \(\delta^2(2-\delta)<w|Z|\); an inward-pointing mark that crosses the opposite pole rejects when \(\delta(2-\delta)^2<w|Z|\). By sign symmetry their combined rejection probability is
\[
 1-a(t\mid T)=\frac12\int_0^1
 \bigl[R_{\mathrm{out}}(wq)+R_{\mathrm{in}}(wq)\bigr]dq,
\]
where \(R_{\mathrm{out}}(y)\) and \(R_{\mathrm{in}}(y)\) are the Lebesgue measures of \(\delta\in[0,1]\) satisfying the respective inequalities. As \(y\downarrow0\),
\[
 R_{\mathrm{out}}(y)=\sqrt{y/2}+O(y),\qquad
 R_{\mathrm{in}}(y)=y/4+O(y^2).
\]
For all \(y>0\), both measures are at most \(\min(1,\sqrt y)\): use \(\delta^2(2-\delta)\ge\delta^2\) and \(\delta(2-\delta)^2\ge\delta\). Hence
\[
 \lim_{t\downarrow0}\frac{1-a(t\mid T)}{\sqrt t}
 =\frac13\sqrt{\frac{3}{2T}},\qquad
 \frac{1-a(t\mid T)}{\sqrt t}\le\sqrt{3/T}.
\]
The last bound permits integration over the independent circle angles once \(\mathbb E_0T^{-1/2}<\infty\).

**5. Exact circle-triangle negative moment.** For independent circle angles, the chord-area identity gives \(T=\frac14\prod_{i<j}|e^{i\Theta_i}-e^{i\Theta_j}|\). The three-variable circular Selberg (Dyson) integral, valid at exponent \(-1/2\), yields
\[
 \mathbb E_0T^{-1/2}=2\frac{\Gamma(1/4)}{\Gamma(3/4)^3}<\infty.
\]
Dominated convergence in Step 4 therefore gives
\[
 1-a(t)=\frac{\sqrt6}{3}\frac{\Gamma(1/4)}{\Gamma(3/4)^3}\sqrt t+o(\sqrt t).
\]
Substitute into the exact probability identity of Step 2 to obtain the displayed two-term small-volume law. The exact total-variation formula from Step 3 gives the sharp conditional convergence rate simultaneously. No use is made of numerical sampling to justify any infinite limit.

## Verification

The standalone script `verification/check.py` requires only the dependencies stated in `verification/requirements.txt`. Run from the artifact root using `python verification/check.py`. It draws 2,500,000 directly sampled sphere-tetrahedra and 1,500,000 independent uniform-product proposals, comparing the exact change-of-variables probability at three thresholds. It tests the plane-height second moment before and after conditioning, and uses 2,000,000 circle-angle triples to check the circle-area and negative-half-moment normalizations. Numerical Mellin-residue checks against the classical spherical-simplex moment formula independently corroborate both scalar constants. The observed result is `SPHERE_TETRA_COPLANAR_CONDITIONAL_LAW_OK`. Monte Carlo and finite precision are corroboration only; the proof is analytic.

## Relationship to prior work

Miles, *Isotropic Random Simplices* (1971), gives a classical exact general moment formula for spherical random simplex volumes, which determines the scalar volume distribution and whose Mellin poles are consistent with the two displayed coefficients. **The scalar marginal is not claimed as a wholly independent distribution theory.** Ruben and Miles (1980) give a canonical decomposition of isotropic random-point configurations; that and the affine Blaschke–Petkantschin identity supply foundational changes of variables. Brauchart and collaborators (arXiv:1512.07470, initial public version December 23, 2015), in their Section 4, use the circle-section simplex-area Jacobian for expected facet-hole radii at large sample size. A previously published conditional uniform-chord law already establishes the unmarked joint weak limit of four points at small volume, including the leading \(3\pi t\) coefficient. Those conclusions are not asserted here as new. The present distinct claim is the exact **all-positive-threshold uniform-proposal rejection representation of the marked volume**, the asymptotically independent signed rescaled volume mark, and the explicit sharp \(\sqrt t\) total-variation correction for the entire marked law. None is implied by the earlier weak convergence alone or established by the inspected spherical hole-radius results or the available scalar moment formula. Prior joint marked treatments remain a residual historical-priority risk.

## Limitations

The points are independent and uniform on the **surface** of a unit sphere, and the volume is Euclidean. An auxiliary fair sign is required to avoid the spurious orientation constraint on the first three circular angles. The mark \(Z_t\) depends on the cutoff \(t\), so the theorem states convergence of these *marked conditional distributions*, not convergence of unconditioned Euclidean vertices. It does not give a uniform theorem over other dimensions, sampling laws, or ellipsoids. Complete original texts of the 1971 and 1980 classical sources were inaccessible in the present comparison; their published formulas and abstracts were inspected where available, and unrecognized stronger historical conditional results cannot be excluded. Independent review has not been performed.

## References

1. R. E. Miles, *Isotropic Random Simplices*, Advances in Applied Probability 3 (1971), 353–382, DOI: 10.2307/1426176.
2. H. Ruben and R. E. Miles, *A canonical decomposition of the probability measure of sets of isotropic random points in Rn*, Journal of Multivariate Analysis 10 (1980), 1–18, DOI: 10.1016/0047-259X(80)90077-9.
3. J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang and R. S. Womersley, *Random Point Sets on the Sphere — Hole Radii, Covering, and Separation*, arXiv:1512.07470, first public version 2015-12-23; particularly Section 4.
4. The circular Dyson integral (a specialization of the Selberg integral), used only to evaluate the negative circle-triangle area moment; original theory of Dyson and Selberg.
