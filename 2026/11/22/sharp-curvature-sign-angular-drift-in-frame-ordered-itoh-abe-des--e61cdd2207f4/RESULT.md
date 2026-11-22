# Sharp curvature-sign angular drift in frame-ordered Itoh–Abe descent

## Finding
For the squared geodesic distance objective on a two-dimensional constant-curvature space, the frame-ordered Itoh–Abe step produces an explicit, sharp and signed first-order global *angular* error that depends on the frame orientation. At fixed physical time \(T>0\), with \(N\) steps of length \(h=T/N\), the azimuth of the numerical point obeys
\[
\lim_{N\to\infty}\frac{\phi_N-\phi_0}{h}
=\frac{\sin(2\theta)}4\left(\frac{r_0}{S_K(r_0)}-\frac{r_0e^{-T}}{S_K(r_0e^{-T})}\right).
\tag{1}
\]
For nonzero curvature, the maximum absolute coefficient over frame angle \(\theta\) occurs exactly at \(|\sin(2\theta)|=1\); at zero curvature every frame has zero coefficient. For the same positively oriented frame this signed error is positive in spherical curvature, negative in hyperbolic curvature, and zero in Euclidean curvature. Averaging the two coordinate orders, which is the established fixed-center symmetrized Itoh–Abe discrete gradient, cancels the leading transverse error. At a bisector-aligned frame it furthermore admits an *exact radial midpoint branch* in every constant curvature:
\[
r_{n+1}=\frac{2-h}{2+h}r_n,\qquad \phi_{n+1}=\phi_n,\quad 0<h<2.
\tag{2}
\]
The novelty asserted here is the explicit sharp curvature/orientation error law and its exact radial bisector consequence, not the pre-existing Itoh–Abe or symmetrized constructions.

## Assumptions and scope
Fix a real Gaussian curvature \(K\), and let \(M_K\) be the simply connected complete two-dimensional space form with curvature \(K\). Fix \(p\in M_K\). Define \(f(x)=\tfrac12d(p,x)^2\), and choose \(z_0\) with \(r_0=d(p,z_0)>0\). If \(K>0\), assume \(r_0<\pi/(2\sqrt K)\); otherwise \(r_0>0\) is arbitrary. Work in the normal polar chart centered at \(p\). Set
\[
S_K(r)=\begin{cases}
\sin(\sqrt K r)/\sqrt K,&K>0,\\
r,&K=0,\\
\sinh(\sqrt{-K}r)/\sqrt{-K},&K<0,
\end{cases}
\qquad q_K(r)=\frac{r S_K'(r)}{S_K(r)}.
\tag{3}
\]
At an iterate \(z\), let \(e_r\) point along the unit inward radial geodesic toward \(p\), and let \(e_\phi\) point toward increasing polar angle; these are orthonormal. Choose the *ordered* orthonormal frame
\[
E_1=\cos\theta\,e_r+\sin\theta\,e_\phi,\qquad
E_2=-\sin\theta\,e_r+\cos\theta\,e_\phi,
\tag{4}
\]
where \(\theta\) is kept fixed as a frame-relative angle at every iterate (not a fixed ambient direction). The polar-angle coordinate \(\phi\) is lifted continuously along the numerical path, so no angular-wrap ambiguity enters the limit.

For \(u=aE_1+bE_2\) in the injectivity domain, put \(F_z(a,b)=f(\operatorname{Exp}_z(aE_1+bE_2))\), and define the forward-coordinate Itoh–Abe quotient
\[
G_{12}(u;z)=E_1\frac{F_z(a,0)-F_z(0,0)}a
+E_2\frac{F_z(a,b)-F_z(a,0)}b.
\tag{5}
\]
All zero-denominator cases use continuous partial-derivative limits. Define \(G_{21}\) analogously by visiting \((0,b)\) before \((a,b)\): the \(E_2\) quotient is \([F_z(0,b)-F_z(0,0)]/b\), and the \(E_1\) quotient is \([F_z(a,b)-F_z(0,b)]/a\). A forward Itoh–Abe step is the local branch of \(u=-hG_{12}(u;z)\), \(z^+=\operatorname{Exp}_z(u)\). The order-averaged step uses \(G_{\mathrm{sym}}=(G_{12}+G_{21})/2\) in the same equation. The branch is the one continuously approaching \(u=0\) as \(h\downarrow0\), unique locally by the implicit function theorem. The fixed-time assertion takes \(N\to\infty\) along positive integer \(N\); consequently all local steps lie in the stated smooth convex neighborhood.

## Proof
**Hessian and coordinate increments.** For the squared-distance function on a space form, the polar warped metric is \(dr^2+S_K(r)^2d\phi^2\), and its Riemannian Hessian has eigenvalues \(1\) in the radial direction and \(q_K(r)\) in the azimuthal direction. Because \(e_r\) points inward, \(\nabla f(z)=-r e_r\). With \(c=\cos\theta\), \(s=\sin\theta\), the normal-coordinate gradient and Hessian are
\[
g=(-rc,rs),\quad
H_{11}=c^2+q_K(r)s^2,\quad H_{22}=s^2+q_K(r)c^2,\quad
H_{12}=(q_K(r)-1)sc.
\tag{6}
\]
Normal-coordinate Hessians at the origin equal Riemannian Hessians, so Taylor expansion of the two finite differences gives, uniformly on compact subannuli,
\[
G_{12}(u;z)=g+Bu+O(\|u\|^2),\qquad
B=\begin{pmatrix}H_{11}/2&0\\H_{12}&H_{22}/2\end{pmatrix}.
\tag{7}
\]
The implicit equation then has the unique smooth local expansion
\[
u=-hg+h^2Bg+O(h^3).
\tag{8}
\]
Multiplying by the azimuthal unit vector, whose frame coordinates are \((s,c)\), and simplifying with \(c^2+s^2=1\), yields the *exact leading transverse coefficient*
\[
\langle Bg,e_\phi\rangle=\frac{r}{2}(1-q_K(r))sc
=\frac r4(1-q_K(r))\sin(2\theta).
\tag{9}
\]
Thus \(u_\phi=h^2r(1-q_K(r))\sin(2\theta)/4+O(h^3)\), while \(u_r=hr+O(h^2)\).

**From local error to a fixed-time law.** In the warped polar chart, a short exponential displacement with \(u_r=O(h)\) and \(u_\phi=O(h^2)\) changes the angle by \(\Delta\phi=u_\phi/S_K(r)+O(h^3)\); the mixed geometric error is of order \(u_ru_\phi=O(h^3)\). Its radius changes by \(\Delta r=-hr+O(h^2)\), with the sign arising because \(u_r\) is inward. Standard elementary discrete Gronwall estimates on the compact annulus between radii \(r_0e^{-T}\) and \(r_0\) give \(r_n=r_0e^{-nh}+O(h)\), uniformly for \(0\le nh\le T\). Summing \(N=T/h\) azimuthal increments therefore gives
\[
\frac{\phi_N-\phi_0}{h}\longrightarrow
\frac{\sin(2\theta)}4\int_0^T
\frac{r(t)(1-q_K(r(t)))}{S_K(r(t))}\,dt,
\qquad r(t)=r_0e^{-t}.
\tag{10}
\]
Since \(\frac{d}{dr}(r/S_K(r))=(1-q_K(r))/S_K(r)\) and \(\dot r=-r\), the integral is \(r_0/S_K(r_0)-r_0e^{-T}/S_K(r_0e^{-T})\), proving (1). On \((0,\pi/(2\sqrt K))\) when \(K>0\), \(r/S_K(r)\) is strictly increasing; it is strictly decreasing when \(K<0\) and constant when \(K=0\). For nonzero curvature, this proves the signs and the uniquely characterized maximizing frame orientations; when \(K=0\), every orientation has zero coefficient. In particular its small-radius expansion is
\[
\frac{\phi_N-\phi_0}{h}\longrightarrow
\frac{Kr_0^2}{24}(1-e^{-2T})\sin(2\theta)+O_K(r_0^4),
\tag{11}
\]
where the \(O_K\) remainder is uniform with fixed \(T\) and \(K\) as \(r_0\downarrow0\).

**Established order symmetrization and a bisector exactness identity.** The backward-coordinate discrete gradient satisfies
\[
G_{21}(u;z)=g+B_{21}u+O(\|u\|^2),\quad
B_{21}=\begin{pmatrix}H_{11}/2&H_{12}\\0&H_{22}/2\end{pmatrix}.
\tag{12}
\]
Thus \((B+B_{21})/2=H/2\). As \(g=-r e_r\) is an eigenvector of \(H\), the symmetric step has transverse displacement \(u_\phi=O(h^3)\), yielding a global \(O(h^2)\) angular error on any fixed horizon. For either coordinate order the discrete chain identity is \(f(z^+)-f(z)=\langle G(u;z),u\rangle\); it survives averaging and gives \(f(z^+)-f(z)=-\|u\|^2/h\) on an implicit step. The symmetrization itself is an established discrete-gradient construction, not claimed new.

At \(\theta=\pi/4\), take the candidate radial displacement \(u=\delta e_r\). Its two coordinates are \(a=\delta/\sqrt2\), \(b=-\delta/\sqrt2\). The two intermediate exponential images corresponding to \((a,0)\) and \((0,b)\) are mirror images across the radial meridian through \(p,z\), and hence have the same value of \(f\). Consequently the two-order average is purely radial, with radial coefficient exactly \([f(\operatorname{Exp}_z(\delta e_r))-f(z)]/\delta=-r+\delta/2\) as long as \(0\le\delta<r\). The symmetric implicit equation reduces to \(\delta=h(r-\delta/2)\), giving \(\delta=2hr/(2+h)\) and the radial recurrence (2). For every \(0<h<2\) this defines a valid radial solution in the convex polar chart; for sufficiently small \(h\), the implicit function theorem identifies it with the unique local branch. It is exactly the scalar implicit-midpoint contraction for the radius, despite using the curved manifold exponential and coordinate quotients.

## Verification
The standalone scientific diagnostic script `verify.py` uses exact symbolic algebra to check (9) and the derivative identity used in (10). It constructs the sphere and hyperbolic-plane exponential distances explicitly and solves the two-coordinate implicit step; convergence diagnostics at \(N=32,64,128,256\) check the signed coefficients for \(K=1\) and \(K=-1\), their vanishing for \(K=0\), cancellation of the first-order angular error by order averaging, and the exact bisector radial recurrence. Run `python3 verify.py` with Python 3, NumPy, SciPy and SymPy. Finite diagnostics corroborate the theorem but do not replace the analytic Taylor/limit proof above.

## Relationship to prior work
Zhou (2026), arXiv:2608.21862, defines the centered Itoh–Abe coordinate quotients in equations (20)–(21) and their implicit update in equation (27), and establishes general curvature-dependent convergence guarantees. Celledoni, Eidnes, Owren and Ringholm (2018), arXiv:1804.08104, Section 3.1, already formulate Itoh–Abe Riemannian discrete gradient optimization. The same authors' arXiv:1805.07578, Section 3.2, equation (3.6), explicitly construct endpoint-reversal symmetrization: with the *same fixed center* this is exactly the coordinate-order average used above. Neither existing symmetrization nor its general convergence-order statements are claimed new. The distinct asserted claim is the sharp signed coefficient (1), its curvature and frame sign reversal, and the exact bisector radial identity (2) in one geometrically canonical test problem. The examined primary texts did not state or imply these coefficients or identity; historical priority beyond the examined literature remains uncertain.

## Limitations
The theorem concerns a squared-distance objective on smooth two-dimensional simply connected *constant-curvature* manifolds and the local implicit branch. It does not establish analogous sign laws for variable curvature, globally nonsmooth distance functions, arbitrary frame selections, large steps with multiple implicit roots, or general convex objectives. The sphere restriction stays strictly inside the convex hemisphere. Exact energy dissipation does not mean exact physical flow; the bisector symmetric step follows the scalar midpoint law rather than the exponential radial law. The \(O(h^2)\) cancellation of the symmetrized method is not presented as a newly invented symmetrization. The script is a reproducibility diagnostic, not an infinite formal certificate or independent audit.

## References
- D. Zhou, *Centered Weak Discrete Riemannian Gradients: A Unified Framework for Riemannian Optimization*, arXiv:2608.21862v1, first public 2026-08-22. https://arxiv.org/abs/2608.21862
- E. Celledoni, S. Eidnes, B. Owren and T. Ringholm, *Dissipative numerical schemes on Riemannian manifolds with applications to gradient flows*, arXiv:1804.08104, 2018. https://arxiv.org/abs/1804.08104
- E. Celledoni, S. Eidnes, B. Owren and T. Ringholm, *Energy preserving methods on Riemannian manifolds*, arXiv:1805.07578, 2018. https://arxiv.org/abs/1805.07578
- J. G. H. Riis and collaborators, *A Geometric Integration Approach to Nonsmooth, Nonconvex Optimisation*, *Foundations of Computational Mathematics*, DOI:10.1007/s10208-020-09489-2. https://doi.org/10.1007/s10208-020-09489-2
