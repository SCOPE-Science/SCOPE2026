# Two nested critical windows for near-brightest projections of circular cones

## Finding
Fix a solid right circular cone of base radius \(r>0\) and height \(h=kr\), with \(k>0\). For a Haar-uniform unoriented projection plane let \(A_k\) be the ordinary area of its orthogonal shadow divided by \(r^2\), and put \(M(k)=\max A_k\) over all planes. The following exact threshold and both nested probability windows describe almost-maximal views.

Define, for \(0<\alpha<\pi/2\),
\[
D(\alpha)=\pi/2+\alpha,\quad F(\alpha)=\cos\alpha+D(\alpha)\sin\alpha,\quad
H(\alpha)=\sqrt{D(\alpha)/(\sin\alpha\cos\alpha)}.
\]
Let \(\alpha_s\in(0,\pi/4)\) be the unique solution of \(\tan(2\alpha_s)=\pi+2\alpha_s\), and let \(\alpha_c\in(0,\alpha_s)\) be the unique solution of
\[
D(\alpha_c)[D(\alpha_c)+\cot\alpha_c]=\pi^2.
\]
Set \(k_c=H(\alpha_c)\), \(T=1+k_c^2\sin^2\alpha_c\), and
\[
\begin{aligned}
z_c&=k_c\sin\alpha_c/\sqrt T,\\
d&=F(\alpha_c)/T^{3/2},\\
\kappa&=(k_c^2\cos(2\alpha_c)-1)T^{3/2}/(k_c\cos\alpha_c),\\
C&=2\sqrt{2/\kappa}.
\end{aligned}
\]
These constants are strictly positive except that \(z_c\) is a latitude in \((0,1)\). Numerically \(k_c=2.641402552064\ldots\), \(z_c=0.588981076349\ldots\), \(d=0.776776042129\ldots\), \(\kappa=3.667631057865\ldots\), and \(C=1.476903680034\ldots\).

**Fixed aspect.** For every fixed \(0<k<k_c\), the upper probability is **exactly** \(\varepsilon/\pi\) for all sufficiently small \(\varepsilon>0\):
\[
\Pr(A_k>M(k)-\varepsilon)=\varepsilon/\pi.
\]
At the critical aspect a second, nonaxial maximizing latitude produces the two-term law
\[
\boxed{\Pr(A_{k_c}>\pi-\varepsilon)=C\sqrt\varepsilon+\varepsilon/\pi+O(\varepsilon^{3/2}).}
\]
For each fixed \(k>k_c\), the upper tail has square-root order \(C(k)\sqrt\varepsilon+O_k(\varepsilon^{3/2})\), with \(C(k)=2\sqrt{2/\kappa(k)}\) and \(\kappa(k)=-\partial_z^2 A_k(z(k))>0\) at its unique maximizing absolute axial cosine \(z(k)\in(0,1)\).

**Outer critical window.** Fix \(\lambda\in\mathbb R\), and vary \(k=k_c+\lambda\varepsilon\). With \(x_+=\max(x,0)\), one has for every \(\lambda\ne-1/d\)
\[
\boxed{
\Pr\{A_k>M(k)-\varepsilon\}
=C\sqrt{[1+d\min(\lambda,0)]_+}\,\sqrt\varepsilon
+\frac{[1-d\max(\lambda,0)]_+}{\pi}\varepsilon
+O_\lambda(\varepsilon^{3/2}).
}
\]
For \(\lambda<-1/d\) the equality \(\Pr\{A_k>M(k)-\varepsilon\}=\varepsilon/\pi\) holds for all sufficiently small \(\varepsilon\). The leading square-root contribution disappears precisely at \(\lambda=-1/d\); the formula at that point requires the finer scale below.

**Inner critical window.** Define at \((k_c,\alpha_c)\) the derivatives of \(G(k,\alpha)=kF(\alpha)/(1+k^2\sin^2\alpha)^{1/2}\), and set
\[
q=G_{kk}-\frac{G_{k\alpha}^2}{G_{\alpha\alpha}},\qquad
\beta=\frac{q}{2d^2}.
\]
Here \(G_{\alpha\alpha}<0\), and \(q\) and \(\beta\) are unambiguously specified real constants (numerically \(q\approx0.229144595\), \(\beta\approx0.189883827\)). For any fixed \(\mu\in\mathbb R\), take
\[
k=k_c-\varepsilon/d+\mu\varepsilon^2.
\]
Then the polar and oblique contributions are *both* of order \(\varepsilon\), and the exact crossover limit is
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr\{A_k>M(k)-\varepsilon\}}{\varepsilon}
=\frac1\pi+C\sqrt{[d\mu+\beta]_+}.}
\]
For \(d\mu+\beta>0\), conditioned on the event from this inner window and on the oblique component, \((Z-z(k))/\varepsilon\) converges in total variation to the uniform law on
\[
\left[-\sqrt{2[d\mu+\beta]/\kappa},\ \sqrt{2[d\mu+\beta]/\kappa}\right],
\]
where \(Z\) is the absolute axial cosine of the viewing normal. The asymptotic probability of this oblique component, under conditioning on a near-maximum view, tends to
\[
\frac{C\sqrt{[d\mu+\beta]_+}}{1/\pi+C\sqrt{[d\mu+\beta]_+}}.
\]
The complementary conditional component is polar and has \((1-Z)/\varepsilon\) asymptotically uniform on \([0,1/\pi]\). When \(d\mu+\beta\le0\), only the polar component has positive limiting conditional mass.

## Assumptions and scope
The cone is the convex hull of \(\{(x,y,0):x^2+y^2\le r^2\}\) and \((0,0,kr)\). The direction has the rotation-invariant probability law on \(S^2\), with opposite normals identified, so its absolute vertical component \(Z\) is uniform on \([0,1]\). The event is the strict area inequality, and all limit statements hold as \(\varepsilon\to0^+\) with \(\lambda\) or \(\mu\) fixed. Areas and deficits are normalized by \(r^2\); multiplying \(r\) does not affect the result. Conditional statements refer only to directions, not to random points sampled in the cone.

## Proof
**1. Exact normalized brightness.** Cauchy's projection formula, applied to the base and lateral surface-area measure, gives for \(z\in[0,1]\)
\[
B_k(z)=\frac{\pi z}2+\frac14\int_0^{2\pi}
\left|k\sqrt{1-z^2}\cos\phi+z\right|d\phi.
\]
The lateral surface contributes half the integral of the absolute normal times its local area; the base contributes \(\pi z/2\). Consequently
\[
B_k(z)=\begin{cases}
\pi z,&z\ge k/\sqrt{1+k^2},\\
\displaystyle \frac{\pi z}2+\sqrt{k^2-(1+k^2)z^2}
+z\arcsin\frac{z}{k\sqrt{1-z^2}},&z<k/\sqrt{1+k^2}.
\end{cases}
\]
Writing \(z=k\sin\alpha/\sqrt{1+k^2\sin^2\alpha}\) on the second branch gives \(B_k(z)=G(k,\alpha)\), with \(G\) as stated.

**2. The competing maximizing configurations.** Differentiation yields
\[
G_\alpha(k,\alpha)=\frac{k\cos\alpha}{(1+k^2\sin^2\alpha)^{3/2}}
\bigl[D(\alpha)-k^2\sin\alpha\cos\alpha\bigr].
\]
Thus the nonaxial stationary points satisfy \(k=H(\alpha)\). Since the sign of \((H^2)'\) is the sign of \(\sin2\alpha-(\pi+2\alpha)\cos2\alpha\), \(H\) decreases to one minimum at \(\alpha_s\) and thereafter increases. For \(k>H(\alpha_s)\), the smaller root \(\alpha_-(k)\) is a strict local maximum and the larger root a strict local minimum. The remaining axial branch has its unique maximum \(\pi\) at \(z=1\). The oblique local maximum \(m(k)=G(k,\alpha_-(k))\) strictly increases through \(\pi\) exactly once, because \(G_k=F(\alpha)/(1+k^2\sin^2\alpha)^{3/2}>0\). At stationarity,
\[
m(k)^2=D(\alpha)[D(\alpha)+\cot\alpha],
\]
so its tie with \(\pi\) is exactly the displayed equation for \(\alpha_c\). In a neighborhood of \(k_c\), all almost-maximizing directions therefore lie in disjoint neighborhoods of \(z=1\) or \(z(k)=k\sin\alpha_-(k)/\sqrt{1+k^2\sin^2\alpha_-(k)}\). Outside these neighborhoods compactness gives a positive area gap, uniformly in nearby \(k\).

**3. Polar and oblique local laws.** The polar branch is **exactly linear**, \(B_k(z)=\pi z\), and hence contributes the probability \([\pi+\varepsilon-M(k)]_+/\pi\), provided that expression is small. The nonaxial branch has nonzero negative curvature at \(z(k)\). At \(k_c\), differentiation through \(z(\alpha)\) gives
\[
-\partial_z^2 B_{k_c}(z_c)
=(k_c^2\cos2\alpha_c-1)T^{3/2}/(k_c\cos\alpha_c)=\kappa>0.
\]
In a smooth family of one-dimensional nondegenerate maxima, the measure of the superlevel interval within an area deficit \(t\) is
\[
2\sqrt{2/\kappa(k)}\sqrt t+O(t^{3/2}),
\]
uniformly for \(k\) near \(k_c\). The missing order-\(t\) term follows by the one-dimensional analytic Morse coordinate and cancellation of its odd Jacobian term across the symmetric interval. Both endpoint intervals carry exactly their lengths as probabilities, because \(Z\) is uniform.

**4. Parameter derivatives.** The envelope theorem at the nonaxial maximizer gives
\[
m'(k_c)=G_k(k_c,\alpha_c)=d>0,\qquad
m''(k_c)=G_{kk}-G_{k\alpha}^2/G_{\alpha\alpha}=q.
\]
The derivatives are explicit. With \(s=\sin\alpha_c\), \(c=\cos\alpha_c\) and \(T=1+k_c^2s^2\),
\[
\begin{aligned}
G_{kk}&=-3k_cs^2F(\alpha_c)/T^{5/2},\\
G_{k\alpha}&=D(\alpha_c)c/T^{3/2}-3k_c^2scF(\alpha_c)/T^{5/2},\\
G_{\alpha\alpha}&=k_cc[1-k_c^2\cos(2\alpha_c)]/T^{3/2}<0.
\end{aligned}
\]
The last inequality follows from \(\alpha_c<\alpha_s\), for which \(H'(\alpha_c)<0\).

**5. Fixed parameter and outer window.** For fixed \(k<k_c\), the oblique branch is separated below the unique polar maximum, giving the exact \(\varepsilon/\pi\) law for small deficits. For fixed \(k>k_c\), only the smooth oblique maximum contributes, giving the square-root law. At \(k_c\), disjoint interval lengths sum to \(C\sqrt\varepsilon+\varepsilon/\pi+O(\varepsilon^{3/2})\). For \(k=k_c+\lambda\varepsilon\), Taylor's theorem gives
\[
m(k)-\pi=d\lambda\varepsilon+O_\lambda(\varepsilon^2).
\]
The global maximum is \(M(k)=\max\{\pi,m(k)\}\). Substituting the resulting local level deficits into the two interval laws proves the outer formula. When \(\lambda<-1/d\), the oblique local maximum is strictly below the threshold \(\pi-\varepsilon\), leaving only the exact polar contribution. At \(\lambda=-1/d\), the first-order oblique deficit vanishes and a finer Taylor term is necessary.

**6. Inner window and conditional shapes.** Take \(k=k_c-\varepsilon/d+\mu\varepsilon^2\). Then \(k<k_c\) for small \(\varepsilon\), \(M(k)=\pi\), and
\[
m(k)-(\pi-\varepsilon)=\left(d\mu+\frac{q}{2d^2}\right)\varepsilon^2+O_\mu(\varepsilon^3).
\]
The polar probability is exactly \(\varepsilon/\pi\), while the oblique interval is of length \(C\varepsilon\sqrt{[d\mu+\beta]_+}+o_\mu(\varepsilon)\), including the boundary case where its length is \(o(\varepsilon)\). This proves the inner crossover and weights. On the positive oblique branch, rescaling \(z-z(k)\) by \(\varepsilon\) transforms the quadratic superlevel interval into the asserted deterministic interval; since the original density in \(z\) is constant and the endpoints converge, conditional total variation follows. The polar rescaled interval is exactly uniform on \([0,1/\pi]\) for sufficiently small deficits. No unproved claim is made about higher-order laws exactly on the inner threshold.

## Verification
The standalone `verify.py` evaluates the isolated critical roots with bracketed solvers, compares the exact area formula to independently generated convex-hull projections of 4,096-gon approximations to a disk, checks the differentiated curvature formula, and computes exact near-upper-tail probabilities by bracketing all roots between stationary latitudes. It tests the polar identity, the ordinary square-root law, the first critical window, and the inner crossover for several parameter values and decreasing deficits. The actual executed output was `CONE_RANDOM_BRIGHTNESS_CRITICAL_TAILS_OK`. The computations corroborate but do not replace the analytic interval and Taylor arguments. Python 3, NumPy and SciPy suffice.

## Relationship to prior work
Vickers and Brown [1], in their circular-cone section and Appendix A, establish the all-direction projected-area formula and describe its orientation-induced probability density; they identify the smaller aspect \(2.145539\ldots\) at which interior stationary directions appear and discuss qualitative density singularities. The formula for the distribution is implicit and is evaluated numerically, not as a uniform double-scaling limit near the global-maximizer switch. Pennell and Deignan [2] derive the oriented cone-shadow area, a fact not claimed new. Finch [3] studies surface-area and mean-width optimization of cones, not this random-shadow statistic. A published sharp brightness-direction theorem [4] identifies \(k_c\), the tied maximizing directions, and the exact stationary-root parametrization; these deterministic facts are acknowledged, not claimed here. What is added is the two-term probability asymptotic at the tied maxima, the explicit \(\varepsilon\)-scale moving-aspect crossover, the finer \(\varepsilon^2\)-scale polar/oblique competition, and the conditional limiting viewing-angle configurations. This is a singular *joint-parameter probability* statement, not a fixed-aspect numerical evaluation of an already known density.

## Limitations
The result concerns right **circular** solid cones, Haar viewing directions, ordinary orthogonal projection area and deficit normalized by \(r^2\). The aspect parameters in the windows vary at the specified rates; it does not assert uniformity for unbounded \(\lambda\) or \(\mu\). The outer two-term expansion is intentionally not claimed at \(\lambda=-1/d\), which requires the separately proved inner window. The first-public day for the earlier 2001 Vickers–Brown journal paper was not verified; the precisely dated 2012 supporting preprint [3] is used for cohort dating and the earlier work is explicitly credited. The historical novelty assessment remains provisional, especially because the earlier general implicit PDF could allow other derivations of these limits. Numerical constants are explanatory approximations, not independent interval certificates. No independent mathematical audit has been conducted.

## References
[1] G. T. Vickers and D. J. Brown, "The distribution of projected area and perimeter of convex, solid particles," *Proceedings of the Royal Society A* 457 (2001), 283–306, DOI: 10.1098/rspa.2000.0667, https://doi.org/10.1098/rspa.2000.0667 (full section 3(c) and Appendix A read in an accessible text transcription).

[2] S. Pennell and J. Deignan, "Computing the Projected Area of a Cone," *SIAM Review* 31 (1989), 299–302, DOI: 10.1137/1031052 (abstract verified; full text not obtained).

[3] S. R. Finch, "Oblique Circular Cones and Cylinders," arXiv:1212.5946v1, first public 2012-12-24, https://arxiv.org/abs/1212.5946 (full HTML article inspected).

[4] "A sharp global brightness-direction switch for right circular cones," publicly accessible geometry note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-global-brightness-direction-switch-for-right-circular-co--19c34891a8b8 (full `RESULT.md` inspected).
