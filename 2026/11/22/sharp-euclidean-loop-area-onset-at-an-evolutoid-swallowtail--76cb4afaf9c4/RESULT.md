# Sharp Euclidean loop-area onset at an evolutoid swallowtail

## Finding
Let a strictly positively curved closed oval have support function \(h\in C^7(\mathbb R/2\pi\mathbb Z)\). Set \(\rho=h+h''>0\), \(g=\rho'/\rho\), and \(m=-\min g>0\). Suppose the global minima of \(g\) consist of finitely many points \(\phi_1,\ldots,\phi_k\), each nondegenerate, with \(g(\phi_j)=-m\) and \(q_j=g''(\phi_j)>0\). For its positive-angle evolutoids let \(\alpha_c=\arctan(1/m)\). Denote by \(\mathcal L(\delta)\) the sum of the ordinary, nonnegative Euclidean areas of all small self-intersection loops born when the evolutoid angle is \(\alpha_c+\delta\), for \(\delta>0\) sufficiently small. Then exactly one small two-cusped loop is born per minimum and

\[
\boxed{\mathcal L(\delta)=\frac{16\sqrt6}{35}(1+m^2)^{5/2}\left(\sum_{j=1}^{k}\frac{\rho(\phi_j)^2}{q_j^{3/2}}\right)\delta^{7/2}+o(\delta^{7/2}).}
\]

For every noncircular ellipse of semiaxes \(a>b>0\), there are two such loops. With \(D=a^2-b^2\) and \(H=\sqrt{4a^2b^2+9D^2}\), their *total* area has the explicit asymptotic

\[
\boxed{\mathcal L_{a,b}(\delta)=\frac{H^5}{210(ab)^{5/2}D^{3/2}}\,\delta^{7/2}+o(\delta^{7/2}),\qquad \alpha_c=\arctan\!\frac{2ab}{3D}.}
\]

At fixed ellipse area, the coefficient divided by \(ab\) has a **unique global minimum** among noncircular ellipses at the semiaxis ratio
\[
\boxed{\frac ab=\frac{1+\sqrt{22}}{\sqrt{21}}=1.241750521674\ldots.}
\]
This is an optimization of the *infinitesimal newborn-loop area coefficient*, not an assertion about loop areas at one fixed nonzero angle increment across different ellipses.

## Assumptions and scope
The oval is the strictly convex body with boundary \(\gamma(\theta)=h(\theta)n(\theta)+h'(\theta)T(\theta)\), where \(n(\theta)=(\cos\theta,\sin\theta)\) and \(T(\theta)=(-\sin\theta,\cos\theta)\). Its positive-angle evolutoid is the envelope of tangent lines rotated counterclockwise through \(\alpha\), expressed by the ordinary (not necessarily convex) support parametrization
\[
h_\alpha(\theta)=h(\theta-\alpha)\cos\alpha+h'(\theta-\alpha)\sin\alpha,\qquad
\gamma_\alpha=h_\alpha n+h_\alpha' T.
\]
Here the angular parameter runs over one turn, and loop area is ordinary nonnegative Lebesgue area, not globally signed/oriented area of a possibly self-intersecting curve. The positive parameter \(\delta\to0\) is taken with the oval (or, in the ellipse case, the semiaxes) held fixed. No uniform asymptotic is asserted as the oval tends to a circle or any minimum becomes degenerate. The global-minimum hypothesis is essential: other local minima can give later loop births but are not counted in this first threshold.

## Proof
1. **Curvature-radius crossing.** With \(\phi=\theta-\alpha\), differentiation gives
\[
\gamma_\alpha'(\theta)=r_\alpha(\theta)T(\theta),\qquad
r_\alpha(\theta)=\rho(\phi)[\cos\alpha+g(\phi)\sin\alpha].
\]
Because \(g\) has zero integral, is nonconstant, and has minimum \(-m\), the factor is positive for \(0\le\alpha<\alpha_c\), nonnegative with isolated zeros at \(\alpha=\alpha_c\), and strictly negative on exactly one short interval near each \(\phi_j\) when \(\alpha=\alpha_c+\delta\) is just above threshold. The evolutoid at criticality is a convex, injectively parametrized oval except for its finitely many isolated zero-speed parameters; hence any new intersections for small positive \(\delta\) must lie near these parameters. Each negative interval is bounded by two simple zeros of \(r_\alpha\), giving ordinary cusps (at a simple zero, \(\det(\gamma_\alpha'',\gamma_\alpha''')=2(r_\alpha')^2\ne0\)).

2. **Metric normal form with coefficients.** Fix one minimum and write \(s=\theta-(\phi_j+\alpha)\), moving the origin to \(\gamma_\alpha(\phi_j+\alpha)\) and taking orthonormal coordinate axes along \(T(\phi_j+\alpha)\) and \(n(\phi_j+\alpha)\). Uniform Taylor expansion gives
\[
r_\alpha(s)=-A_j\delta+B_js^2+O(\delta^2+\delta|s|+|s|^3),\quad
A_j=\rho_j\sqrt{1+m^2},\quad
B_j=\frac{\rho_jq_j}{2\sqrt{1+m^2}}.
\]
Integrating \(\gamma_\alpha'=r_\alpha T\) and using \(T(\theta_0+s)=T(\theta_0)\cos s-n(\theta_0)\sin s\), the local coordinates satisfy
\[
X(s)=-A_j\delta s+\frac{B_j}{3}s^3+O(\delta^2|s|+\delta s^2+|s|^4),\qquad
Y(s)=\frac{A_j}{2}\delta s^2-\frac{B_j}{4}s^4+O(\delta^2s^2+\delta|s|^3+|s|^5).
\]
With \(s=\sqrt\delta\,t\), the rescaled coordinates \((X/\delta^{3/2},Y/\delta^2)\) converge in \(C^1\) on compact intervals to the polynomial pair \((-A_jt+B_jt^3/3,A_jt^2/2-B_jt^4/4)\). This is a *Euclidean* normal form: its scale factors retain geometric units and cannot be discarded by arbitrary diffeomorphisms.

3. **Closing the loop and evaluating its area.** The limiting polynomial pair has a transverse double point at \(t_\pm=\pm\sqrt{3A_j/B_j}\); the two ordinary cusps are at \(t=\pm\sqrt{A_j/B_j}\). The Jacobian of the two-point coincidence equations is nonsingular, so the implicit-function theorem gives a genuine nearby transverse double point for each small \(\delta>0\). Away from the finitely many degeneracy neighborhoods, the limiting convex curve is embedded; within each neighborhood the two cusp intervals and monotonicity of the tangential coordinate outside them exclude any further double points. Green's formula applied between the crossing parameters, after the above anisotropic rescaling, yields
\[
\begin{split}
\lim_{\delta\downarrow0}\frac{\mathcal L_j(\delta)}{\delta^{7/2}}
&=\frac12\int_{-\sqrt{3A_j/B_j}}^{\sqrt{3A_j/B_j}}\left(X_0(t)Y_0'(t)-Y_0(t)X_0'(t)\right)dt\\
&=\frac{8\sqrt3}{35}\frac{A_j^{7/2}}{B_j^{3/2}}=\frac{16\sqrt6}{35}\frac{\rho_j^2(1+m^2)^{5/2}}{q_j^{3/2}}.
\end{split}
\]
The first equality is a signed Green integral in the orthonormal but orientation-reversing \(T,n\) frame; its positive absolute value equals ordinary loop area, since the polynomial integral is positive. Summing finitely many disjoint loops proves the general statement. The \(7/2\) power is the product of the tangential \(\delta^{3/2}\) and normal \(\delta^2\) scales; the exact metric coefficient is the added content.

4. **Ellipse and sharp optimal eccentricity.** For the ellipse, its support function and curvature radius are
\[
p(\phi)=\sqrt{a^2\cos^2\phi+b^2\sin^2\phi},\quad
\rho(\phi)=\frac{a^2b^2}{(a^2\cos^2\phi+b^2\sin^2\phi)^{3/2}},\quad
g(\phi)=\frac{3(a^2-b^2)\sin\phi\cos\phi}{a^2\cos^2\phi+b^2\sin^2\phi}.
\]
The two minima obey \(\tan\phi=-a/b\) modulo \(\pi\), with
\[
m=\frac{3D}{2ab},\quad
\rho_j=\frac{(a^2+b^2)^{3/2}}{2^{3/2}ab},\quad
q_j=\frac{3D(a^2+b^2)^2}{2a^3b^3}.
\]
Substitution gives the stated two-loop coefficient. With fixed \(ab\), rewrite it as
\[
\frac{1}{ab}\lim_{\delta\downarrow0}\frac{\mathcal L_{a,b}(\delta)}{\delta^{7/2}}
=\frac{16}{105}\left(\frac32\right)^{3/2}\frac{(1+m^2)^{5/2}}{m^{3/2}}.
\]
The logarithmic derivative with respect to \(m>0\) is \((7m^2-3)/[2m(1+m^2)]\). Thus the expression decreases to its unique minimum at \(m=\sqrt{3/7}\), then increases to infinity. Since \(a/b- b/a=2m/3\), the unique minimizing aspect ratio is \((1+\sqrt{22})/\sqrt{21}\). This completes the sharp ellipse classification.

## Verification
An accompanying `CHECKER.py` computes the coefficient in both equivalent forms, evaluates the model signed-area integral analytically, locates two exact geometric double-point parameters numerically for several ellipses using the actual evolutoid support parametrization, integrates their enclosed area, and verifies convergence of the area ratios to one as \(\delta\downarrow0\). It also verifies the predicted eccentricity optimum. The checker uses Python with NumPy/SciPy/SymPy; these are only numerical and algebraic checks, not a substitute for the global analytic proof. All independent-audit or external certification channels remain unperformed.

## Relationship to prior work
Giblin and Warder (2014) already give the ellipse's critical angle, the cusp-birth classification, and the swallowtail transition. Jerónimo-Castro (first public online 18 June 2013) gives the support-function formalism and a *convex-regime* area inequality, not the new positive small-loop area. Aguilar-Arteaga and colleagues (2015) give an exact evolutoid curvature-radius identity, used above. Eggers and Fontelos (2012) give the canonical swallowtail and its \(3/2\)-by-\(2\) anisotropic scaling in a much wider context, which predicts the \(7/2\) exponent but not this Euclidean evolutoid coefficient or its ellipse optimizer. These inherited results are explicitly excluded from novelty claims. The present claim concerns the **metric leading coefficient**, its dependence on the original curvature-radius jet, and a sharp fixed-area optimal eccentricity.

## Limitations
The proof assumes finitely many nondegenerate global minima of \(\rho'/\rho\); it does not cover flat minima, coincident higher-order singularities, arbitrary later-angle evolutoid transitions, or the double limit of near-circular ellipses and vanishing angle increments. The loop area differs from the conventional oriented area of a whole hedgehog, so known support-integral formulas do not directly compute the coefficient. Historical priority remains provisional, especially regarding Wunderlich's short 1955 German article on ellipse evolutoids, for which no full text was reliably retrieved, and Zwierzyński's later extended-evolutoid-front work. The claimed value is quantitative geometry at an already known transition, not discovery of the transition itself.

## References
- J. Jerónimo-Castro, *On evolutoids of planar convex curves*, Aequationes mathematicae 88 (2014), 97–103, first published online 2013-06-18. https://doi.org/10.1007/s00010-013-0213-y (complete author-posted text inspected)
- P. J. Giblin and J. P. Warder, *Evolving Evolutoids*, American Mathematical Monthly 121 (2014), 871–889. https://www.liverpool.ac.uk/~pjgiblin/papers/giblin-warder-revised.pdf (complete accessible article, particularly Sec. 3–5)
- V. A. Aguilar-Arteaga, R. Ayala-Figueroa, I. González-García, and J. Jerónimo-Castro, *On evolutoids of planar convex curves II*, Aequationes mathematicae 89 (2015), 1433–1447, published online 2015-04-22. https://doi.org/10.1007/s00010-015-0352-4 (accessible author-posted full text, Remark 2)
- J. Eggers and M. A. Fontelos, *Cusps in interfacial problems*, Panoramas & Synthèses 38 (2012), 69–90. https://people.maths.bris.ac.uk/~majge/Eggers_Fontelos_cusp_review.pdf (Sec. 1 normal forms and scaling)
- W. Wunderlich, *Über die Evolutoiden der Ellipse*, Elemente der Mathematik 10 (1955), 37–40 (bibliographic identification only; full-text priority risk)
- M. Zwierzyński, *The singular evolutoids set and the extended evolutoids front*, arXiv:2107.08605 (2021) and Aequationes mathematicae 96 (2022), 849–866. https://arxiv.org/abs/2107.08605 (abstract/bibliography only)
