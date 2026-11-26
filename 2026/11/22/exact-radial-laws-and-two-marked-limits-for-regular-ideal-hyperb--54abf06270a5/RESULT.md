# Two marked radial limits for regular ideal hyperbolic polygons

## Finding

Let \(P_n\) be the regular ideal \(n\)-gon of the complete curvature-\(-1\) hyperbolic plane, where \(n\ge3\), and let \(O\) be its symmetry center. Sample \(X_n\) by normalized hyperbolic area (the polygon has finite area \(A_n=(n-2)\pi\)). Set \(D_n=d_{\mathbb H}(O,X_n)\), \(\alpha=\pi/n\), and \(r_n=\operatorname{artanh}(\cos\alpha)\).

**Fixed-side cusp law with marks.** For every fixed \(n\ge3\), the scalar survival probability used to normalize the conditional law is
\[
\boxed{\Pr(D_n>t)\sim c_n e^{-t},\qquad
c_n=\frac{2n\cot\alpha}{(n-2)\pi}.}
\]
Inside the event \(D_n>t\) for \(t>r_n\), choose the unique side-normal fan containing the polar angle \(\phi\in(-\alpha,\alpha)\), and let \(J\) denote its limiting cusp vertex and \(B\) the side of that vertex, determined by the sign of \(\phi\). Put \(\theta_n(t)=\arccos(\cos\alpha/\tanh t)\), \(\delta_t=\alpha-\theta_n(t)\), \(Z_t=(\alpha-|\phi|)/\delta_t\), and \(S_t=D_n-t\). As \(t\to\infty\), the joint conditional law of \((J,B,Z_t,S_t)\) converges in total variation to a uniform label among the \(2n\) directed cusp-side sectors, independent of the continuous law
\[
\boxed{f(z,s)=e^s\,\mathbf1_{\{0<z<1,\ 0<s<-\frac12\log z\}}.}
\]
Equivalently, \(S\sim\operatorname{Exp}(1)\) and \(Z e^{2S}\sim\operatorname{Uniform}(0,1)\) are independent, as is the discrete sector label. This records the *position* of an unusually distant point rather than only its scalar radial distance.

**Many-side arcsine–exponential law.** Let \(\phi_n\in(-\alpha,\alpha)\) be the signed polar angle from its nearest side normal, define \(U_n=\phi_n/\alpha\), and let \(R_n(\phi_n)\) be the radial distance from \(O\) to the ideal polygon's boundary in that direction. Put \(E_n=R_n(\phi_n)-D_n\ge0\). As \(n\to\infty\),
\[
\boxed{\mathcal L(U_n,E_n)\xrightarrow{\mathrm{TV}}
\operatorname{Arcsine}(-1,1)\otimes\operatorname{Exp}(1),}
\]
where the arcsine variable has density \(1/(\pi\sqrt{1-u^2})\). In particular,
\[
\boxed{D_n-r_n\ \Longrightarrow\ -\tfrac12\log(1-U^2)-E,}
\]
with independent \(U\) arcsine and \(E\) standard exponential. Its complete limiting survival function is
\[
\boxed{S_\infty(y)=\begin{cases}
1-\frac{2}{\pi}e^y,&y\le0,\\
\frac{2}{\pi}\left[\arcsin(e^{-y})-
\frac{e^{-y}}{1+\sqrt{1-e^{-2y}}}\right],&y>0.
\end{cases}}
\]
The centered scalar limit and its survival function are included as consequences and for comparison with the scalar radial law. The claim here concerns the two joint marked limits.

## Assumptions and scope

The polygons are geodesically convex ideal polygons with exactly \(n\) equally spaced vertices at infinity, in the standard complete hyperbolic plane of constant sectional curvature \(-1\). The random point is sampled with normalized *hyperbolic area*, not Euclidean disk area or boundary arclength. Distance means hyperbolic geodesic distance from the fixed symmetry center, not distance to the closest side, distance between two random points, or distance to a random triangle's incenter. In the fixed-\(n\) marked statement, the label is the angular cusp-side sector, not the (infinite) distance to an ideal vertex. All zero-probability boundary ambiguity is arbitrary. Asymptotic coefficients in the fixed-\(n\) statements need not be uniform as \(n\) grows.

## Proof

### 1. Exact geometry and normalization

Work in polar geodesic coordinates around \(O\). A geodesic disk has area element \(\sinh\rho\,d\rho\,d\phi\). In the Klein disk coordinates of radial radius \(k=\tanh\rho\), the supporting geodesic of an ideal side with endpoints at polar angles \(\pm\alpha\) is the Euclidean line \(k\cos\phi=\cos\alpha\). Hence within its normal fan \(-\alpha<\phi<\alpha\) the polygon has exact radial boundary
\[
R_n(\phi)=\operatorname{artanh}\!\left(\frac{\cos\alpha}{\cos\phi}\right),
\qquad
\cosh R_n(\phi)=\frac{\cos\phi}{\sqrt{\sin^2\alpha-\sin^2\phi}}.
\]
Its minimum is attained at \(\phi=0\) and equals \(r_n\); the radius diverges at each fan endpoint, an ideal vertex. There are \(n\) disjoint such fans, up to null boundaries. The identity
\[
\int_0^{\phi}\cosh R_n(v)\,dv
=\arcsin\!\left(\frac{\sin\phi}{\sin\alpha}\right)
\]
shows, independently of Gauss–Bonnet, that their total area is
\[
2n\int_0^\alpha(\cosh R_n(\phi)-1)\,d\phi
=2n(\pi/2-\alpha)=(n-2)\pi=A_n.
\]

### 2. Scalar radial law and tangency, for reference

Radial area integration gives the exact identity for every \(t\ge0\),
\[
\Pr(D_n>t)=\frac{n}{A_n}\int_{-\alpha}^{\alpha}
[\cosh R_n(\phi)-\cosh t]_+\,d\phi.
\]
If \(0\le t\le r_n\), this equals one minus the area of a full radius-\(t\) disk divided by \(A_n\), giving \(1-2(\cosh t-1)/(n-2)\). If \(t>r_n\), only the two portions \(|\phi|>\theta_n(t)\) survive. The primitive in Step 1 evaluates the resulting integral to
\[
\Pr(D_n>t)=\frac{2n}{A_n}\left[\arccos\!\left(\frac{\sin\theta_n(t)}{\sin\alpha}\right)-\cosh t\,(\alpha-\theta_n(t))\right].
\]
By differentiating the radial integral at regular \(t\), or differentiating the branches, the density is
\[
f_{D_n}(t)=\frac{2n\sinh t}{A_n}\begin{cases}
\alpha,&0<t<r_n,\\
\alpha-\theta_n(t),&t>r_n.
\end{cases}
\]
Since \(\tanh r_n=\cos\alpha\), Taylor expansion gives
\[
\theta_n(r_n+h)=\frac{\sqrt2\sin\alpha}{\sqrt{\cos\alpha}}\sqrt h+O_n(h^{3/2}).
\]
Using \(\sinh r_n=\cos\alpha/\sin\alpha\), the density has a continuous extension at \(r_n\) and satisfies
\[
f_{D_n}(r_n+h)-\frac{2\pi}{A_n}\sinh(r_n+h)=-\frac{2n\sqrt{2\cos\alpha}}{A_n}\sqrt h+O_n(h^{3/2}).
\]

### 3. Exponential cusp tail and the marked distribution

For fixed \(n\), \(\tanh t=1-2e^{-2t}+O(e^{-4t})\) implies
\[
\delta_t=\alpha-\theta_n(t)=2\cot\alpha\,e^{-2t}+O_n(e^{-4t}).
\]
At one corner of a side-normal fan write \(\phi=\alpha-\delta_t z\), \(0<z<1\). For every fixed \(z\in(0,1)\), the exact Klein radial equation yields
\[
R_n(\alpha-\delta_t z)-t\longrightarrow -\tfrac12\log z.
\]
In the event \(D_n>t\), put \(s=D_n-t\). The original area element, summed over \(2n\) congruent corner sectors, is
\[
\frac{2n\delta_t}{A_n}\sinh(t+s)\,
\mathbf1_{\{0<s<R_n(\alpha-\delta_t z)-t\}}\,dz\,ds.
\]
Its integral over \((z,s)\) is \(\Pr(D_n>t)\). Dividing by \(e^{-t}\), the density tends pointwise almost everywhere to \(c_n e^s\mathbf1_{0<z<1,\,0<s<-\frac12\log z}\), where
\(c_n=2n\cot\alpha/A_n\). Integrating the limit gives
\[
\int_0^1\!\int_0^{-\frac12\log z} e^s\,ds\,dz
=\int_0^1(z^{-1/2}-1)\,dz=1.
\]
For the normalizing probability, the density in Step 2 and the expansion of \(\delta_t\) give \(f_{D_n}(t)\sim c_n e^{-t}\). Integrating from \(t\) to infinity gives \(\Pr(D_n>t)\sim c_n e^{-t}\), since the relative density error is uniformly small beyond any sufficiently large threshold. Thus the normalized conditional densities converge pointwise almost everywhere to a probability density, and Scheffé's lemma gives total variation convergence. Symmetry makes each of the \(2n\) corner labels exactly uniform at every such \(t\), with identical conditional mark laws. The substitution \(w=ze^{2s}\) transforms the limiting density into \(e^{-s}\,dw\,ds\) on \(w\in(0,1), s>0\), proving the independent uniform and exponential marks.

### 4. Growing-side arcsine–exponential factorization

For each fan let \(u=\phi/\alpha\in(-1,1)\), and set the inward radial slack \(e=R_n(\alpha u)-\rho\). The *exact normalized joint density* with respect to \(du\,de\) is
\[
p_n(u,e)=\frac{n\alpha}{A_n}
\sinh(R_n(\alpha u)-e)\,
\mathbf1_{\{-1<u<1,\ 0<e<R_n(\alpha u)\}}.
\]
The factor \(n\) accounts for the disjoint fans and the factor \(\alpha\) for their angular rescaling. For each fixed \(-1<u<1\), Taylor expansion of the Klein boundary relation as \(\alpha\downarrow0\) gives
\[
R_n(\alpha u)-r_n\longrightarrow-\tfrac12\log(1-u^2),\qquad
\alpha\sinh R_n(\alpha u)\longrightarrow(1-u^2)^{-1/2}.
\]
Since \(n/(n-2)\to1\), for each fixed \(e>0\),
\[
p_n(u,e)\longrightarrow\frac{e^{-e}}{\pi\sqrt{1-u^2}},
\qquad -1<u<1.
\]
The limiting function integrates to one: its factors are the normalized arcsine and exponential densities. Each \(p_n\) also integrates to one by Step 1. Consequently Scheffé's lemma proves the asserted total variation convergence without a separate endpoint-uniform Taylor estimate. Applying the continuous mapping theorem to \(D_n-r_n=R_n(\alpha U_n)-r_n-E_n\) requires a small qualification: the deterministic radial functions converge uniformly on every compact subset of \((-1,1)\), while the arcsine limiting measure gives arbitrarily small probability to the excluded endpoint neighborhoods; this proves the displayed weak limit.

For its CDF, conditional on \(U=u\), let \(H(u)=-\tfrac12\log(1-u^2)\ge0\) and recall \(E\sim\operatorname{Exp}(1)\). For \(y\le0\),
\[
\Pr(H(U)-E\le y)=e^y\,\mathbb E[e^{-H(U)}]
=\frac2\pi e^y.
\]
For \(y>0\), only \(|U|>\sqrt{1-e^{-2y}}\) contributes to the survival event, whose arcsine integral gives the second branch in the statement. Its two expressions meet continuously at \(y=0\); as \(y\to\infty\), the survival is asymptotic to \(e^{-y}/\pi\).

## Verification

A standalone standard-library Python checker is supplied at `checks/check_radial.py`. It independently integrates the polar survival region using a square-root endpoint substitution, without using the stated inverse-trigonometric primitive, and compares the result with the exact law for four polygon sizes and three thresholds above each inradius. It tests the fixed-side exponential tail coefficients, the inradius branch junction, and four centered thresholds in the growing-side limit at two large polygon sizes. The maximum discrepancy in the direct quadrature comparisons was \(4.05\times10^{-12}\). Execution of `python3 checks/check_radial.py` ends with `ALL_CHECKS_PASSED`. The mathematical limits are established by the proof, not by numerical tests or sampling.

## Relationship to prior work

*Radial distance in regular ideal hyperbolic polygons: an exact law and a logarithmic many-side limit* gives the scalar radial CDF and density for the same sampling model, the fixed-side scalar tail, and the weak limit centered at \(\log n\). Its scalar limit is equivalent to the one centered at \(r_n\) above, since \(r_n-\log n\to\log(2/\pi)\). The scalar formulas are not claimed as distinct contributions here. The joint distributions in the two marked limits, rather than radial marginals alone, are the subject of this result. For general hyperbolic polygon area formulas, see Abrosimov and Mednykh. The Gauss–Bonnet area formula, Klein disk geometry and hyperbolic polar Jacobian are classical premises.

The publicly available result *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons* evaluates the distance of one area-uniform point to the **nearest side**, and for ideal triangles gives the global side-clearance distribution. That is not the radial distance to a fixed incenter; the two distributions even have different support (bounded versus unbounded). *Cusp-pair tails for random distances in ideal hyperbolic polygons* and *Marked cusp-pair and midpoint laws for distant points in ideal hyperbolic polygons* concern the distance between **two** area-uniform points, with \(t e^{-t}\) scaling and two-cusp depth splits. Their probabilistic geometry does not imply the one-point \(e^{-t}\) tail, exact radial CDF, or many-side arcsine factorization.

*Exact incenter and phase laws for boundary-uniform ideal hyperbolic triangles* instead randomizes the **ideal vertices** and studies the resulting random incenter; here the polygon is fixed and an interior point is area-uniform. The Euclidean theorem *Radial-distance laws classify tangential polygons up to cyclic ordering* uses related polar integration but a different metric, finite vertices, and different normalized sampling.

## Limitations

The theorem concerns regular ideal polygons in curvature \(-1\), with each fixed \(n\ge3\) and a separate \(n\to\infty\) regime; it does not assert bounds uniform in \(n\) for the fixed-polygon cusp tail, nor results for irregular ideal polygons, compact polygons, nonconstant curvature, or alternative sampling schemes. The total-variation conclusions concern the specified two-dimensional rescaled marks and sector label; only weak convergence is asserted here for the centered scalar radial distance.

## References

- N. Abrosimov and A. Mednykh, *Volumes of polytopes in spaces of constant curvature*, arXiv:1302.4919, first public 2013-02-20; https://arxiv.org/abs/1302.4919 ; full HTML https://arxiv.org/html/1302.4919v2 . Primary classification 51M20.
- *Radial distance in regular ideal hyperbolic polygons: an exact law and a logarithmic many-side limit*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-radial-distance-in-regular-ideal-hyperbolic-polygons-an-exact-la--7af837d2c4e2/RESULT.md .
- *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-the-logarithmic-boundary-distance-law-and-a-renormalized-shape-i--1d7379fbdbb6/RESULT.md .
- *Cusp-pair tails for random distances in ideal hyperbolic polygons*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-cusp-pair-tails-for-random-distances-in-ideal-hyperbolic-polygon--102d92c50bd6/RESULT.md .
- *Marked cusp-pair and midpoint laws for distant points in ideal hyperbolic polygons*, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-marked-cusp-pair-and-midpoint-laws-for-distant-points-in-ideal-h--520ae1386677/RESULT.md .
- *Exact incenter and phase laws for boundary-uniform ideal hyperbolic triangles* (2026).
- *Radial-distance laws classify tangential polygons up to cyclic ordering* (2026).
