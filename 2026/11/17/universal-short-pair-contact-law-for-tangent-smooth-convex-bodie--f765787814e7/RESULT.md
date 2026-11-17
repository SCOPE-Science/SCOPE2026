# Universal short-pair contact law for tangent smooth convex bodies

## Finding

Let \(K_-\) and \(K_+\) be two compact planar convex bodies with disjoint interiors and a unique common point, both with \(C^3\) boundary and strictly positive curvature at that point. Take independent points \(X\) and \(Y\) uniformly in their respective bodies, whose areas are \(A_-\) and \(A_+\). Write their contact curvatures as \(\kappa_->0\) and \(\kappa_+>0\), and put \(k=(\kappa_-+\kappa_+)/2\).

The small cross-body distance probability is

\[
\mathbb P(\|X-Y\|\le r)
=\frac{4\,B(5/4,3/2)}{3A_-A_+\sqrt{k}}\,r^{7/2}+o(r^{7/2}),\qquad r\downarrow0.
\]

This constant depends only on the two areas and the *sum* of contact curvatures. The theorem also determines the entire conditional contact configuration: after the local rescaling in the next section, the four scaled coordinates converge in total variation to uniform measure on

\[
\mathcal D_k=\{(t,u,w,v)\in\mathbb R\times[0,\infty)^2\times\mathbb R:\ (kt^2+u+w)^2+v^2<1\}.
\]

In this limit, with \(H=kt^2+u+w\),

\[
H^2\sim\operatorname{Beta}(5/4,3/2),\qquad
(kt^2/H,u/H,w/H)\sim\operatorname{Dirichlet}(1/2,1,1).
\]

The Dirichlet vector is independent of \(H\) and \(v\). The sign of \(t\) is an independent fair sign; conditionally on \(H=h\), the variable \(v\) is uniform on \((-\sqrt{1-h^2},\sqrt{1-h^2})\).

There is also a sharp near-contact crossover. If \(K_+\) is translated away from \(K_-\) along the common outward normal by \(\lambda r\), with fixed \(\lambda\ge0\), and its uniform point is translated with it, then

\[
\lim_{r\downarrow0}r^{-7/2}\mathbb P(\|X-Y_{\lambda,r}\|\le r)
=\frac{1}{A_-A_+}\,F_k(\lambda),
\]

where

\[
F_k(\lambda)=\frac{8}{3\sqrt k}\int_{\lambda}^{1}(h-\lambda)^{3/2}\sqrt{1-h^2}\,dh\quad(0\le\lambda<1),
\qquad F_k(\lambda)=0\quad(\lambda\ge1).
\]

As the normalized gap approaches its maximum allowable value,

\[
F_k(\lambda)\sim\frac{\pi\sqrt2}{6\sqrt k}(1-\lambda)^3\qquad(\lambda\uparrow1).
\]

## Assumptions and scope

Apply a Euclidean rigid motion sending the unique contact to \((0,0)\), its common tangent to the vertical axis, and \(K_-\) to \(x\le0\), \(K_+\) to \(x\ge0\). Write the boundaries in a neighborhood of the contact as \(x=-g_-(y)\) and \(x=g_+(y)\), respectively. Convexity, smoothness and positive contact curvature imply

\[
g_\pm(y)=\frac{\kappa_\pm}{2}y^2+O(|y|^3),\qquad g_\pm(y)\ge c y^2
\]

for sufficiently small \(|y|\) and some \(c>0\). For the zero-gap contact marks, set

\[
t_r=\frac{X_y+Y_y}{2\sqrt r},\quad v_r=\frac{Y_y-X_y}{r},\quad
u_r=\frac{-X_x-g_-(X_y)}r,\quad
w_r=\frac{Y_x-g_+(Y_y)}r.
\]

The normal-depth coordinates \(u_r,w_r\) are nonnegative. All convergence statements for marks are conditional on \(\|X-Y\|\le r\), and refer to the natural Lebesgue densities in these four scaled coordinates. This theorem concerns *two different positive-area bodies*, not two points sampled from the same body, and assumes positive quadratic contact. It does not cover corner contacts, shared boundary arcs, zero-curvature contacts, higher dimensions, or arbitrary nonuniform sampling.

## Proof

**Localization.** The bodies are compact, on opposite sides of their common supporting line, and meet only at the origin. Thus as \(r\to0\), pairs at mutual distance at most \(r\) lie in the neighborhoods where the boundary graphs above apply. Their horizontal separation is at least \(g_-(X_y)+g_+(Y_y)\), so \(|X_y|+|Y_y|\le C\sqrt r\). Their vertical separation is at most \(r\), and their interior normal depths each at most \(r\). Consequently \((t_r,u_r,w_r,v_r)\) remains in a fixed compact box whenever the rare event holds.

**Jacobian and tangent domain.** Put \(X_y=\sqrt r\,t-rv/2\), \(Y_y=\sqrt r\,t+rv/2\), \(X_x=-g_-(X_y)-ru\), and \(Y_x=g_+(Y_y)+rw\). The absolute four-dimensional Jacobian of this triangular transformation is exactly \(r^{7/2}\). Uniformly on the compact localization box,

\[
\frac{g_-(X_y)+g_+(Y_y)}r=kt^2+O(\sqrt r).
\]

For the translated right body, the difference vector divided by \(r\) tends to \((\lambda+kt^2+u+w,v)\). The indicator of the distance event therefore tends almost everywhere to the indicator of

\[
\mathcal D_{k,\lambda}=\{(t,u,w,v):u,w\ge0,\ (\lambda+kt^2+u+w)^2+v^2<1\}.
\]

Because all prelimit indicators are bounded and supported in a common compact box, dominated convergence gives convergence of their integrals and convergence in \(L^1\) of the rescaled unnormalized densities. Normalizing by their positive limiting mass gives total-variation convergence for \(0\le\lambda<1\), in particular the stated zero-gap marked limit. For \(\lambda\ge1\), the translated bodies are at distance at least \(\lambda r\), making the event empty up to a null set.

**Domain volume and sharp constant.** Let \(h=\lambda+kt^2+u+w\). Combining the two signs of \(t\), replace \(kt^2\) by \(q\ge0\), with \(dt=dq/(\sqrt{kq})\). The integral over \(q,u,w\ge0\), subject to \(q+u+w=h-\lambda\), is

\[
\frac1{\sqrt{k}}\int_0^{h-\lambda}q^{-1/2}(h-\lambda-q)\,dq
=\frac{4}{3\sqrt k}(h-\lambda)^{3/2}.
\]

The allowed \(v\) interval has length \(2\sqrt{1-h^2}\). Integrating \(h\) over \((\lambda,1)\) proves the crossover formula, including the tangent constant

\[
|\mathcal D_k|=F_k(0)=\frac{4}{3\sqrt k}B(5/4,3/2).
\]

The original joint density of \((X,Y)\) equals \(1/(A_-A_+)\) on the two bodies, yielding the prefactor in the finding. At \(\lambda\uparrow1\), substitute \(h=\lambda+(1-\lambda)s\), use \(1-h^2\sim2(1-\lambda)(1-s)\), and evaluate \(B(5/2,3/2)=\pi/16\) to obtain the stated cubic endpoint.

**Conditional marks.** On \(\mathcal D_k\), the change to \((q,u,w,v)\), with the independent fair sign of \(t\), has density proportional to \(q^{-1/2}\). Conditioning on \(H=q+u+w=h\) gives Dirichlet parameters \((1/2,1,1)\), independent of \((H,v)\). Integrating \(v\) gives marginal density for \(H\) proportional to \(h^{3/2}\sqrt{1-h^2}\), so substitution \(z=h^2\) yields \(\operatorname{Beta}(5/4,3/2)\). The conditional \(v\) law is uniform on its stated interval. These transformations exhaust the nondegenerate limiting contact configuration.

## Verification

The independent executable script `check_contact.py` integrates the **exact overlap area** of two unit disks whose centers are two units apart, rather than the tangent-domain derivation. It compares the resulting near-zero point-pair probabilities to the predicted coefficient \(4B(5/4,3/2)/(3\pi^2)\). At thresholds \(r=0.30,0.15,0.07,0.03\), the ratios of exact probability to leading approximation were \(0.93745625,0.96877509,0.98543840,0.99376128\). It also quadratures the contact-domain mass and verifies the beta moments and the monotonicity of the gap crossover. Output ends in `TANGENT_CONTACT_QUADRATURE_AND_BETA_CHECKS_OK`. Run from the extracted artifact directory with `python check_contact.py` after installing `requirements.txt`.

These are finite numerical consistency tests; the proof is the localization, Jacobian, \(L^1\) convergence, and beta-integral calculation above.

## Relationship to prior work

General overlap-integral and convolution techniques for point-pair distances are classical, including Ehlers–Enns (1981), Sheng (1985) and Lellouche–Souris (2019). Those generic identities are used as established background and are not claimed as new. Tong–Ahmadi–Pan (first submitted November 29, 2013) derive distance distributions across adjacent polygons, including triangles with a common edge; this differs from the point-contact geometry and positive curvatures here. The contribution assessed here is the **joint** sharp \(7/2\)-power coefficient for two smooth tangent bodies, the local-gap crossover, and the full beta–Dirichlet conditional contact limit. Prior general convolution formulations can provide an alternative starting point but do not by themselves state this quantitative local theorem. Historical priority for more specialized curved-contact calculations is not definitive; see the scientific review.

## Limitations

The boundaries must have nonzero finite curvature and a unique point of contact. The two points are uniform by **area**, not boundary arclength; a boundary-sampling model has different scaling. The limiting marked law is proved in total variation after conditioning and rescaling, but no explicit general rate is proved. The crossover assumes normal translations by \(\lambda r\), with \(\lambda\) fixed as \(r\to0\). No independent external audit or complete historical-priority certification has occurred.

## References

- P. F. Ehlers and E. G. Enns, “Random secants of a convex body generated by surface randomness,” *Journal of Applied Probability* 18 (1981), 157–166, DOI: `10.2307/3213176` (general overlap formulation; abstract available).
- T. K. Sheng, “The distance between two random points in plane regions,” *Advances in Applied Probability* 17 (1985), 748–773, DOI: `10.2307/1427086` (general cross-region distance integrals; abstract available).
- F. Tong, M. Ahmadi, and J. Pan, “Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points,” arXiv:`1312.2498`, first public posting November 29, 2013, https://arxiv.org/abs/1312.2498 (shared-edge polygon models).
- S. Lellouche and M. Souris, “Distribution of Distances between Elements in a Compact Set,” *Stats* 3 (2020), 1–15; online December 26, 2019, DOI: `10.3390/stats3010001` (full-text convolution and examples).
