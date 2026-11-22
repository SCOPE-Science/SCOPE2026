# A singular disk–lens crossover for near-maximal random inscribed parallelograms

## Finding
Let \(0\le c<1\) and let
\[
K_c=\{(x,y)\in\mathbb R^2:(|x|+c)^2+y^2\le1\}
\]
be the intersection of unit disks centered at \((\pm c,0)\). Its radial function is
\[
\rho_c(\theta)=\sqrt{1-c^2\sin^2\theta}-c|\cos\theta|.
\]
Independently choose two directions \(\Theta,\Phi\) uniformly on \([0,\pi)\), and form the centered inscribed parallelogram with vertices \(\pm\rho_c(\Theta)(\cos\Theta,\sin\Theta)\) and \(\pm\rho_c(\Phi)(\cos\Phi,\sin\Phi)\). Its area is
\[
Q_c=2\rho_c(\Theta)\rho_c(\Phi)|\sin(\Phi-\Theta)|.
\]
Write \(a=1-c\), \(b=\sqrt{1-c^2}\) and \(M_c=2ab\). Then \(Q_c\le M_c\); for \(0<c<1\), equality is possible only for the two ordered direction pairs \((0,\pi/2)\) and \((\pi/2,0)\) modulo \(\pi\), while for \(c=0\) every orthogonal pair maximizes.

For each fixed \(0<c<1\), the *sharp upper-end area probability* is
\[
\boxed{\Pr(M_c-Q_c\le\varepsilon)
\sim\frac{8}{3\pi^2(1-c)^2c\sqrt{\sqrt{1-c^2}}}\,\varepsilon^{3/2}}
\qquad(\varepsilon\downarrow0).
\]
In contrast, when \(c=0\), for \(0\le\varepsilon\le2\) the distribution is exactly
\[
\boxed{\Pr(M_0-Q_0\le\varepsilon)
=\frac2\pi\arccos(1-\varepsilon/2)
\sim\frac2\pi\sqrt\varepsilon.}
\]
The apparent discontinuity of exponent has a sharp boundary layer. If \(c=c(\varepsilon)\ge0\) and \(c/\varepsilon\to\lambda\in[0,\infty)\), then
\[
\boxed{\lim_{\varepsilon\downarrow0}
\frac{\Pr(M_c-Q_c\le\varepsilon)}{\sqrt\varepsilon}
=G(\lambda)
=\frac4{\pi^2}\int_0^{\pi/2}
\sqrt{\left[1-2\lambda(\sin t+\cos t-1)\right]_+}\,dt.}
\]
This strictly positive continuous crossover satisfies \(G(0)=2/\pi\) and \(G(\lambda)\sim8/(3\pi^2\lambda)\) as \(\lambda\to\infty\).

The rare directions carry a further *marked limit law*: for a fixed \(0<c<1\), conditional on \(M_c-Q_c\le\varepsilon\), the two maximizing ordered pairs have limiting probability \(1/2\) each. At the first pair write \(\alpha=\Theta\) modulo \(\pi\), choosing the signed representative near \(0\), and \(\delta=\Phi-\pi/2\). Then
\[
\left(\frac{a\sqrt b\,\alpha}{\sqrt\varepsilon},
\frac{2ac\,\delta}{\varepsilon}\right)
\quad\Longrightarrow\quad
\operatorname{Unif}\{(x,y):x^2+|y|\le1\},
\]
whose planar density is \(3/8\) on that region. At the other ordered pair exchange the labels \(\Theta\) and \(\Phi\).

## Assumptions and scope
The disks are Euclidean, of common unit radius and have center half-separation \(c\). Choosing angles uniformly is *not* the same as sampling points by arclength along the lens boundary. Both direction samples are independent and considered modulo sign; the parallelogram has its center fixed at the lens center. The included equality classification is for this centered class. All asymptotic statements with fixed \(c\) have constants depending on \(c\); the boundary-layer limit only assumes \(c/\varepsilon\to\lambda<\infty\). The notation \([z]_+=\max\{z,0\}\) is used in the crossover integral.

## Proof
**1. Sharp area envelope and equality set.** The lens is contained in the ellipse
\[
E_c=\{(x,y):x^2/a^2+y^2/b^2\le1\}.
\]
To verify this, it suffices to use \(x\ge0\), put \(x=au\) with \(0\le u\le1\), and take the largest permitted \(y^2=1-(x+c)^2\). Direct subtraction gives
\[
1-\frac{x^2}{a^2}-\frac{y^2}{b^2}
=\frac{2cx(a-x)}{ab^2}\ge0.
\]
For \(c>0\), equality on the lens boundary occurs precisely when \(x=0\) or \(|x|=a\), namely at the four points \((\pm a,0)\), \((0,\pm b)\). Applying the linear map \((x,y)\mapsto(x/a,y/b)\), any two vectors from the ellipse have determinant of absolute value at most one, with equality only for two orthogonal unit vectors. Therefore the area of their symmetric parallelogram is at most \(2ab\), and for \(c>0\) equality forces the four stated axial contacts. This establishes the exact maximizing angle pairs. When \(c=0\), the ellipse is a disk and every pair of orthogonal boundary radii attains equality.

**2. Local contact normal form.** Fix \(0<c<1\). At the maximizing ordered pair near \((0,\pi/2)\), use signed deviations \(\alpha\) and \(\delta\). The exact radial formula and elementary Taylor expansions give
\[
\rho_c(\alpha)=a+\frac{ca}{2}\alpha^2+O_c(\alpha^4),
\qquad
\rho_c(\pi/2+\delta)=b-c|\delta|+O_c(\delta^2),
\]
\[
|\sin(\pi/2+\delta-\alpha)|
=1-\frac12(\delta-\alpha)^2+O((\delta-\alpha)^4).
\]
Multiplying, and using \(M_c=2ab\), gives
\[
M_c-Q_c=a^2b\,\alpha^2+2ac|\delta|
+O_c(|\alpha|^3+|\alpha\delta|+\delta^2).
\]
The same expression with labels interchanged holds at the second maximizing pair. Compactness, the already classified equality set, and positivity of the leading coefficients ensure that the event \(M_c-Q_c\le\varepsilon\) is eventually confined to these two neighborhoods and has local scales \(|\alpha|=O_c(\sqrt\varepsilon)\), \(|\delta|=O_c(\varepsilon)\). Indeed the remainder divided by \(\alpha^2+|\delta|\) tends uniformly to zero near the origin, giving matching local lower and upper bounds.

Set \(X=a\sqrt b\,\alpha/\sqrt\varepsilon\) and \(Y=2ac\,\delta/\varepsilon\). The limiting event is \(X^2+|Y|\le1\), a region of area
\[
\int_{-1}^1 2(1-X^2)\,dX=\frac83.
\]
The angular probability density is constant \(1/\pi^2\); the Jacobian of the inverse scaled coordinates is \(\varepsilon^{3/2}/(2a^2c\sqrt b)\). Each ordered pair therefore contributes \(4\varepsilon^{3/2}/(3\pi^2a^2c\sqrt b)\), proving the stated factor two and coefficient. The same rescaling and dominated convergence on the bounded limiting region give the uniform conditional law, its density \(3/8\), and the equally weighted ordered pair.

**3. Circle law.** At \(c=0\), \(Q_0=2|\sin(\Phi-\Theta)|\). The direction difference modulo \(\pi\) is uniform on \([0,\pi)\). Consequently
\[
\Pr(Q_0\ge2-\varepsilon)=\frac2\pi\arccos(1-\varepsilon/2),
\]
with the asserted square-root expansion.

**4. Critical crossover.** Let \(c/\varepsilon\to\lambda\in[0,\infty)\). Uniformly for angles away from the immaterial sign-representation endpoints, the radial function has the first-order expansion
\[
\rho_c(t)=1-c|\cos t|+O(c^2),\qquad
M_c=2-2c+O(c^2).
\]
A nearly maximal event must satisfy \(\Phi=\Theta+\pi/2+O(\sqrt\varepsilon)\) modulo \(\pi\). Write \(\Phi=\Theta+\pi/2+\sqrt\varepsilon\,z\); for bounded \(z\) the normalized deficit converges to
\[
\frac{M_c-Q_c}{\varepsilon}
\longrightarrow z^2+2\lambda(|\cos\Theta|+|\sin\Theta|-1).
\]
This convergence is uniform on compact sets after noting that the absolute cosine is Lipschitz; a global bound from the disk-area sine factor confines \(z\) to a fixed bounded interval for sufficiently small \(\varepsilon\) when \(c=O(\varepsilon)\). The angular density and Jacobian contribute \(\sqrt\varepsilon/\pi^2\). Thus the conditional admissible \(z\)-length at \(\Theta=t\) is twice the displayed square root, and integrating \(t\in[0,\pi)\) by its quadrant symmetry yields the formula for \(G\). Dominated convergence proves continuity and \(G(0)=2/\pi\).

As \(\lambda\to\infty\), the integral has contributions only near the endpoints \(t=0,\pi/2\), where \(\sin t+\cos t-1=t+O(t^2)\) (or the reflected equivalent). Each endpoint has leading integral \(1/(3\lambda)\), so \(G(\lambda)\sim8/(3\pi^2\lambda)\), as claimed.

## Verification
Run the standalone `verify.py` with Python 3 from the same directory; it requires no third-party packages. It checks the exact radial and ellipse-containment identities, the deterministic maximal parallelogram, both local coefficients through progressively shrinking numerical increments, the disk distribution formula, the exact geometric density normalization, and independently quadrature-evaluated crossover values and its large-parameter scaling. These are finite deterministic diagnostics. The proof above, not the numerical tests, establishes the continuum statements and the limits.

## Relationship to prior work
Kratky (1978) gives classical intersection-area calculations for multiple congruent circular disks, including the symmetric two-disk geometry. Kallus (2013) treats maximal inscribed triangles in centrally symmetric domains, a different polygon optimization. Barba and collaborators (2015) study extremal areas of polygons with vertices constrained to circles. A separately published result *Exact John and Löwner ellipsoids of equal-ball lenses in every dimension* (2026) supplies the enclosing ellipse \(E_c\) and its axial contact set; therefore the deterministic area envelope used in step 1 is not claimed as original. A separately published *Exact maximal triangle area and equality configurations in every symmetric circular lens* (2026) resolves a different deterministic area invariant. Neither comparison supplies the near-optimal random **centered parallelogram** probability, its mixed quadratic/absolute-value angular normal form, the singular disk-to-lens crossover, or the marked conditional law. Related random-polygon results with independent area-uniform vertices in disks concern another sampling rule and polygon class.

The asserted contribution is the combined sharp random-area endpoint theorem, the angle-scaled crossover, and its conditional directional geometry, rather than the known optimal ellipse, the classical lens geometry, or the disk sine distribution taken in isolation. Older mathematically equivalent random-parallelogram calculations may exist outside the examined literature; priority is not asserted beyond the comparisons described.

## Limitations
The two selected directions are independent and uniform in angle, not arclength or uniform interior samples. The result concerns a centered parallelogram in a symmetric lens, not arbitrary polygons or unequal disk radii. Fixed-positive-separation asymptotics are not uniform as \(c\downarrow0\), which is precisely why the crossover is stated separately. The crossover does not cover \(c/\varepsilon\to\infty\) with \(c\downarrow0\) under arbitrary relative rates. It is an analytic same-study derivation without an independent mathematical audit or exhaustive historical-priority certification.

## References
1. K. W. Kratky, *The area of intersection of n equal circular disks*, Journal of Physics A: Mathematical and General **11** (1978), 1017–1024, https://doi.org/10.1088/0305-4470/11/6/006 (journal public record dated 1978-06-01).
2. Y. Kallus, *Inextensible domains*, arXiv:1301.5880v1, first posted 2013-01-24, https://arxiv.org/abs/1301.5880 .
3. L. Barba et al., *Asymmetric polygons with maximum area*, arXiv:1501.07721v1, first posted 2015-01-30, https://arxiv.org/abs/1501.07721 .
4. *Exact John and Löwner ellipsoids of equal-ball lenses in every dimension*, publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-john-and-l-wner-ellipsoids-of-equal-ball-lenses-in-every-d--a1fa5399323a .
5. *Exact maximal triangle area and equality configurations in every symmetric circular lens*, publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-maximal-triangle-area-and-equality-configurations-in-every--c8fb931a71de .
