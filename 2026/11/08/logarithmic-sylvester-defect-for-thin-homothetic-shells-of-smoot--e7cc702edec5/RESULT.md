# Logarithmic Sylvester defect for thin homothetic shells of smooth convex bodies

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body with \(C^3\) boundary and everywhere positive Euclidean curvature, with the origin in its interior. Put \(A=\operatorname{area}(K)\), let \(n(x)\) be its outer unit normal, \(h(x)=\langle x,n(x)\rangle>0\), and let \(\kappa(x)>0\) be its curvature. For \(0<\delta<1\), sample four independent, area-uniform points from the homothetic shell \(K_\delta=K\setminus(1-\delta)K\), and let \(Q_K(\delta)\) be the probability that all four are vertices of their convex hull. Then
\[
\boxed{\lim_{\delta\downarrow0}\frac{1-Q_K(\delta)}{\delta\log(1/\delta)}
=\mathcal C(K):=\frac1{A^3}\int_{\partial K}\frac{h(x)^4}{\kappa(x)}\,ds(x).}
\]
The coefficient is positive, finite, and invariant under every invertible linear change of coordinates. For every ellipse centered at the origin, \(\mathcal C(K)=2/\pi^2\). It is not constant over smooth bodies: for the strictly convex family with support function \(h_\varepsilon(\theta)=1+\varepsilon\cos(3\theta)\), \(|\varepsilon|<1/8\),
\[
\mathcal C(K_\varepsilon)=\frac{8+24\varepsilon^2+963\varepsilon^4+160\varepsilon^6}{4\pi^2(1-4\varepsilon^2)^3}
=\frac2{\pi^2}\bigl(1+15\varepsilon^2+O(\varepsilon^4)\bigr).
\]
Thus a classical four-point convex-position question develops a singular \(\delta\log(1/\delta)\) boundary layer whose leading coefficient records centro-affine shape.

## Assumptions and scope
All convexity refers to ordinary Euclidean convexity, and the four points have an absolutely continuous joint law. The shell is the region between the stated homothetic copies, rather than an arclength-thickened normal neighborhood. The support \(h\) is measured relative to the specified homothety center, not an arbitrarily translated origin. Smoothness and strictly positive curvature are used uniformly; the theorem does not include polygons, zero-curvature points, nonsmooth bodies, or dimensions above two. The asserted asymptotic is a limit, with no uniform error bound over all eligible bodies.

## Proof
**1. Exact sampling coordinates.** Parameterize \(\partial K\) by counterclockwise arclength \(s\in\mathbb R/L\mathbb Z\), writing \(p(s)\), tangent \(T(s)\), inward normal \(N(s)=-n(s)\), and \(\kappa(s)>0\). The map \((s,\lambda)\mapsto\lambda p(s)\) parametrizes the shell, with Jacobian \(\lambda h(s)\). Consequently the boundary parameter and radial factor are independent, with densities
\[
f(s)=\frac{h(s)}{2A},\qquad
\frac{2\lambda}{1-(1-\delta)^2}\,1_{[1-\delta,1]}(\lambda).
\]
The first density integrates to one by \(\int_{\partial K}h\,ds=2A\). Equivalently each sampled point is \((1-\delta U)p(s)\), where \(U\in[0,1]\) has density \(2(1-\delta U)/(2-\delta)\), converging uniformly to the uniform density on \([0,1]\).

**2. Localization to three consecutive boundary parameters.** Except on a null set, failure of four-point convex position means that exactly one sample lies inside the triangle formed by the other three. Order the four projected boundary parameters cyclically. If the interior point has parameter \(s\), denote its immediate cyclic predecessor and successor by \(s-u\) and \(s+v\), and the remaining sample by \(s_*\). The event for fixed \(s\) requires the signed turn of these consecutive three shell points to be negative. On the unperturbed strictly convex boundary the turn is strictly positive. Uniform curvature bounds and compactness imply the following localization facts as \(\delta\to0\):

(a) If either adjacent gap is bounded below by a fixed \(\eta>0\), the probability of a negative turn is \(O_\eta(\delta)\), after integrating the other gap; the same applies to configurations in which the fourth point falls within a fixed \(\eta\)-neighborhood of \(s\), up to an \(O(\eta)\) fraction of the leading localized integral.

(b) For \(0<u,v<\eta\), a negative turn requires \(uv=O(\delta)\), with the implicit constant independent of the three radial parameters. The part with \(u\leq C\delta\), \(v\leq C\delta\), or with \(u/v\) in a fixed compact subinterval of \((0,\infty)\), contributes only \(O_\eta(\delta)\) after the integration. The two unbalanced scale sectors in which both gaps tend to zero, each much larger than \(\delta\), carry the full \(\delta\log(1/\delta)\) coefficient.

For completeness, these statements follow by expanding the cross product of the three consecutive difference vectors and using the strict positivity of the curvature. On \(u,v\leq\eta\), the unperturbed turn is \(\kappa(s)uv(u+v)/2+O(uv(u+v)^2)\); the radial perturbation has absolute size \(O(\delta(u+v))\) (plus a smaller quadratic perturbation). Hence any negative turn with both gaps small forces \(uv\lesssim\delta\), apart from a region of \(O(\delta^2)\) measure. When one gap stays above \(\eta\), the unperturbed turn is bounded below by a positive constant times the other gap, and the same first-order perturbation bound gives an \(O_\eta(\delta)\) event. Finally, when both gaps are \(o(1)\) but \(\gg\delta\), and \(s_*\) stays a positive distance from \(s\), the two non-base sides of the triangle meet the near-vertex region at inward depth comparable to \(\min(u,v)\), whereas the tested point lies at depth \(O(\delta+uv)=o(\min(u,v))\). Thus negative turn is then equivalent to membership inside the triangle. To remove the fixed-separation restriction on \(s_*\), note that its conditional density is bounded and its probability of falling within distance \(\eta\) of \(s\) is \(O(\eta)\); take \(\delta\downarrow0\) before \(\eta\downarrow0\). This proves the claimed leading-order replacement without claiming global equality of turn and containment events.

**3. Local turn expansion.** Write \(U_0,U_-,U_+\) for the three independent radial-depth variables at parameters \(s,s-u,s+v\). Taylor expansion in the tangent/normal frame gives, uniformly as \(u,v\to0\) with \(\delta/\min(u,v)\to0\),
\[
\frac{\det(X_0-X_-,X_+-X_0)}{u+v}
=\frac{\kappa(s)}2uv
-\delta h(s)\left(U_0-\frac{vU_-+uU_+}{u+v}\right)
+o(uv+\delta).
\]
The unperturbed part follows from \(p(s+t)=p(s)+tT(s)+\kappa(s)t^2N(s)/2+O(t^3)\); the radial perturbation contributes the stated weighted depth difference. Uniformity holds on the multiscale sectors used below. In particular, the leading negative-turn condition is
\[
uv<\frac{2\delta h(s)}{\kappa(s)}
\left(U_0-\frac{vU_-+uU_+}{u+v}\right)_+.
\]

**4. The logarithmic gap integral.** Conditional on the distinguished point's boundary parameter \(s\), the joint density of the immediate predecessor and successor gaps near \((u,v)=(0,0)\) is \(6f(s-u)f(s+v)(1+O(u+v))=6f(s)^2(1+O(u+v))\). The factor six chooses and orders two of the other three points; the last lies outside the intervening short arc.

The elementary kernel limit used here is, for independent \(U_0,U_-,U_+\sim\mathrm{Unif}[0,1]\), any fixed \(c>0\) and \(\eta>0\),
\[
\lim_{\delta\downarrow0}\frac{1}{\delta\log(1/\delta)}
\int_0^\eta\!\int_0^\eta
\Pr\!\left(uv<c\delta\left(U_0-\frac{vU_-+uU_+}{u+v}\right)_+\right)du\,dv
=\frac c6.
\]
To prove it, change variables to \(t=uv\), \(z=\log(u/v)\), with \(du\,dv=dt\,dz/2\). For each \(t\in(0,\eta^2)\), the allowed \(z\)-interval has length \(2\log(\eta^2/t)\). Except for a bounded-length central \(z\)-interval, the weighted depth of the neighbors approaches one of \(U_-\) or \(U_+\) as \(|z|\to\infty\); either limit has the same law. Integrating \(t\) up to \(c\delta\), and dividing by \(\delta\log(1/\delta)\), therefore leaves \(c\int_0^1\Pr(U_0-U_->w)\,dw=c\mathbb E(U_0-U_-)_+=c/6\). The central interval and the logarithmic factor \(\log(1/w)\) have only \(O(\delta)\) total cost; bounded convergence applies to the remaining terms. Restricting to \(\delta^{1-a}\leq u,v\leq\delta^a\) for fixed \(0<a<1/2\) captures a fraction \(1-2a\) of the coefficient and makes the Taylor replacement uniform; the omitted coefficient is bounded by \(O(a)\), and \(a\downarrow0\) completes the comparison.

**5. Assemble the coefficient.** The kernel has \(c=2h(s)/\kappa(s)\). Multiply its limit by the sixfold neighbor-gap density, the boundary density \(f(s)\) of the distinguished point, and the four choices of interior point. By the localization in step 2, no other configuration contributes at this scale. Thus
\[
1-Q_K(\delta)\sim 4\int_{\partial K}f(s)\,6f(s)^2
\frac{2h(s)}{6\kappa(s)}\,ds\,\delta\log(1/\delta)
=8\int_{\partial K}\frac{f(s)^3h(s)}{\kappa(s)}\,ds\,\delta\log(1/\delta).
\]
Substitute \(f=h/(2A)\) to obtain the formula in the Finding.

**6. Affine invariance and examples.** An invertible linear map takes the shell to the matching shell and preserves the area-uniform law and convex position; therefore its limit coefficient is unchanged. This reduces every origin-centered ellipse to a disk, where \(h=R\), \(\kappa=1/R\), \(ds=R\,d\theta\) and \(A=\pi R^2\), yielding \(2/\pi^2\). For \(h_\varepsilon(\theta)=1+\varepsilon\cos3\theta\), the radius of curvature is \(\rho=h+h''=1-8\varepsilon\cos3\theta>0\), \(ds=\rho\,d\theta\), and
\[
A=\frac12\int_0^{2\pi}h\rho\,d\theta=\pi(1-4\varepsilon^2),\qquad
\int_{\partial K}\frac{h^4}{\kappa}\,ds
=\int_0^{2\pi}h^4\rho^2\,d\theta
=\frac\pi4(8+24\varepsilon^2+963\varepsilon^4+160\varepsilon^6).
\]
This proves the explicit family formula and the strict nonconstant shape response.

## Verification
The standalone `thin_shell_check.py` evaluates the support-function integral by exact rational polynomial arithmetic, samples points by the exact uniform area law on the shell, and detects triangle containment directly using oriented cross products (not the local turn approximation). It tests both the circular annulus and a threefold perturbation, for three shell thicknesses. The normalized empirical defects trend toward the predicted coefficients but converge slowly; finite simulation cannot establish the limit. The analytic steps above are the proof.

## Relationship to prior work
Marckert's 2014 paper *Probability that n random points in a disk are in convex position* (arXiv:1402.3512) gives disk-interior convex-position probabilities and recursive formulas. Marckert's 2015 paper *Around Sylvester's question in the plane* (arXiv:1511.03658) treats convex-body extrema for four and five area-uniform points. Both concern sampling from a convex body, whereas the present sampling domain is a **nonconvex homothetic shell** and the quantity is its singular fixed-four-point thin-shell limit. The older Sylvester/Blaschke results motivate the question, but no stated result in those inspected papers gives the formula here. Related work on the convex hull of boundary-sampled points and published finite/polytope thin-shell calculations treats other asymptotic parameters or outcomes.

## Limitations
The statement makes no claim for nonsmooth or weakly curved boundaries, for a normal-offset shell, or for more than four points. The coefficient is not claimed to be an optimal isoperimetric functional or to uniquely determine shape. The proof gives an asymptotic equivalence, not a numerically effective bound on the remainder for a fixed thickness. Historical priority has not been independently certified; the literature search is not a uniqueness proof. The cited full-text works cover closely related but different sampling models.

## References
- J.-F. Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512, first public 2014-02-14; https://arxiv.org/abs/1402.3512.
- J.-F. Marckert, *Around Sylvester's question in the plane*, arXiv:1511.03658, first public 2015-11-11; https://arxiv.org/abs/1511.03658.
- I. Bárány, *Sylvester's question: The probability that n points are in convex position*, Ann. Probab. 27 (1999), 2020–2034; cited in the Marckert papers.
- H. Carnal and J. Hüsler, *On the convex hull of n random points on a circle*, J. Appl. Probab. 28 (1991), 235–240; abstract accessible at https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/on-the-convex-hull-of-n-random-points-on-a-circle/CBBA8C382423C9839F5B92B2A1201874.
