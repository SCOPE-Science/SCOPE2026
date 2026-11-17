# Cassini-oval crossover for nearly circular shadows of nearly oblate ellipsoids

## Finding

Let \(B>\Delta>0\) be fixed. For \(\eta>0\), let
\[
E_\eta=\left\{x\in\mathbb R^3:\frac{x_1^2}{B+\eta}+\frac{x_2^2}{B}+\frac{x_3^2}{B-\Delta}\le1\right\}.
\]
Choose an oriented viewing normal \(N\) uniformly on \(S^2\). The orthogonal shadow of \(E_\eta\) on \(N^\perp\) is an ellipse; write \(\lambda_+(N)\ge\lambda_-(N)>0\) for its *squared* semiaxis lengths, and put \(G_\eta=\lambda_+-\lambda_-\). For every fixed \(t>0\),
\[
\boxed{\lim_{\eta\downarrow0}\frac{\Delta}{\eta}\Pr(G_\eta<t\eta)=\Phi(t)}
\]
where, with complete elliptic integrals of the first and second kinds,
\[
\Phi(t)=\begin{cases}
\bigl(E(t)-(1-t^2)K(t)\bigr)/\pi,&0<t<1,\\
1/\pi,&t=1,\\
tE(1/t)/\pi,&t>1.
\end{cases}
\]
Here \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\) and \(E(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{1/2}\,d\theta\).

Conditionally on the event \(G_\eta<t\eta\) and on \(N_3>0\), the rescaled viewing direction
\[
Z_\eta=\sqrt{\Delta/\eta}(N_1+iN_2)
\]
converges weakly to **normalized planar area measure** on the Cassini region
\[
\boxed{\mathcal C_t=\{z\in\mathbb C:|1-z^2|<t\}.}
\]
For \(0<t<1\) this region has two connected components; at \(t=1\) its two boundary lobes touch at the origin; for \(t>1\) the region is connected. Its area is \(2\pi\Phi(t)\). The crossover is continuous but has an infinite logarithmic slope:
\[
\Phi'(t)=\begin{cases}tK(t)/\pi,&0<t<1,\\K(1/t)/\pi,&t>1,\end{cases}
\quad\text{and}\quad
\Phi'(t)=\frac{1}{2\pi}\log\frac1{|t-1|}+O(1)\quad(t\to1,\ t\ne1).
\]
Thus the quadratic small-window behavior \(\Phi(t)\sim t^2/4\) passes, through a singular Cassini topology transition, to linear large-window behavior \(\Phi(t)\sim t/2\). The statement concerns the **joint** limit in which the departure from axial symmetry and the roundness tolerance decrease together.

## Assumptions and scope

The body is a solid centered Euclidean ellipsoid with positive squared semiaxes \(B+\eta,B,B-\Delta\). The viewing normal uses normalized spherical surface area, equivalently Haar-uniform unoriented planes. The roundness statistic is the difference of squared semiaxis lengths, not their ordinary ratio. All limits keep \(B,\Delta,t\) fixed while \(\eta\downarrow0\). The conditional law assumes the north-hemisphere representative \(N_3>0\); an unoriented plane has the same representative almost surely. The strict/weak event distinction is immaterial because the level sets have zero spherical area for every fixed positive parameter.

For comparison with standard apparent axis ratios, let \(q_\eta=\sqrt{\lambda_-/\lambda_+}\). On the near-round event, \(\lambda_\pm\to B\), so replacing \(G_\eta<t\eta\) by \(1-q_\eta<t\eta/(2B)\) has the same leading probability and the same conditional rescaled-direction limit.

## Proof

**1. Exact spectral identity.** Put \(Q_\eta=\operatorname{diag}(B+\eta,B,B-\Delta)\). The support function of the ellipsoid is \(h(v)=\sqrt{v^TQ_\eta v}\); restricting this support function to \(N^\perp\) shows that the squared shadow semiaxes are the eigenvalues of the compression of \(Q_\eta\) to that plane. Adding a multiple of the identity does not change their difference, so use \(R=Q_\eta-BI=\operatorname{diag}(\eta,0,-\Delta)\). For a symmetric three-by-three matrix \(R\), the trace of its compression is \(\operatorname{tr}R-N^TRN\), and its two-by-two determinant is \(N^T\operatorname{adj}(R)N\). Hence, writing \(N=(x,y,z)\),
\[
G_\eta^2=\bigl(\eta-(\eta+\Delta)x^2-\Delta y^2\bigr)^2+4\eta\Delta y^2.\tag{1}
\]
This equality is exact, without small-parameter approximations.

**2. Localization and the Cassini polynomial.** The event \(G_\eta<t\eta\) forces
\[
(\eta+\Delta)x^2+\Delta y^2<(1+t)\eta,
\]
so both relevant spherical caps shrink to the north and south poles at transverse scale \(\sqrt\eta\). Set \(u=\sqrt{\Delta/\eta}\,x\), \(v=\sqrt{\Delta/\eta}\,y\), and \(z=u+iv\). Dividing (1) by \(\eta^2\) gives the exact expression
\[
\left(1-u^2-v^2-\frac\eta\Delta u^2\right)^2+4v^2.
\]
As \(\eta\downarrow0\) this tends locally uniformly to
\[
(1-u^2-v^2)^2+4v^2=|1-(u+iv)^2|^2.\tag{2}
\]
The localization bound puts all relevant rescaled coordinates inside the fixed disk \(|z|^2\le1+t\). The limiting boundary \(|1-z^2|=t\) is an algebraic curve of planar area zero. Its interior \(\mathcal C_t\) therefore obtains from dominated convergence, even at the touching threshold \(t=1\).

**3. Spherical normalization and the conditional limit.** In coordinates \((x,y)\) on each hemisphere, spherical area is \(dx\,dy/\sqrt{1-x^2-y^2}\). Combining the two hemispheres and normalizing by \(4\pi\),
\[
\Pr(G_\eta<t\eta)=\frac\eta{2\pi\Delta}\int_{\mathbb R^2}
\frac{\mathbf1\{G_\eta(u,v)<t\eta\}}{\sqrt{1-(\eta/\Delta)(u^2+v^2)}}\,du\,dv.
\]
The integral is confined to a compact disk for sufficiently small \(\eta\). Therefore
\[
\lim_{\eta\downarrow0}\frac\Delta\eta\Pr(G_\eta<t\eta)=\frac{|\mathcal C_t|}{2\pi}.
\]
In the north-hemisphere conditional density the prefactor and spherical Jacobian cancel after normalization. The same dominated-convergence argument proves convergence to normalized area measure on \(\mathcal C_t\).

**4. Exact Cassini area.** The holomorphic map \(w=z^2\) is two-to-one away from the origin and has Jacobian modulus \(4|z|^2\). Consequently
\[
|\mathcal C_t|=\frac12\int_{|w-1|<t}\frac{dA(w)}{|w|}.
\]
For \(0<t<1\), integrate in polar coordinates \(w=\rho e^{i\theta}\) to obtain
\[
\int_{|w-1|<t}\frac{dA(w)}{|w|}
=4\int_0^{\arcsin t}\sqrt{t^2-\sin^2\theta}\,d\theta
=4\bigl(E(t)-(1-t^2)K(t)\bigr).
\]
For \(t>1\), the radial segment starts at the origin for every angle, and the same integral equals \(4tE(1/t)\). At \(t=1\) it is \(4\). Division by \(4\pi\) yields \(\Phi\) as stated.

**5. Critical regularity and topology.** Differentiating the complete elliptic integral formulas gives \(\Phi'(t)=tK(t)/\pi\) below one and \(\Phi'(t)=K(1/t)/\pi\) above one. The classical integral behavior \(K(k)=\log(4/\sqrt{1-k^2})+o(1)\) as \(k\uparrow1\) proves the logarithmic divergence. The map \(z\mapsto z^2\) takes \(\mathcal C_t\) to the disk centered at one with radius \(t\). Below one that disk avoids the branch point zero and has two disjoint inverse images; above one it contains the branch point and has one connected inverse image. At one the two open lobes share a boundary point but not an interior point. Standard series at modulus zero give \(\Phi(t)\sim t^2/4\) as \(t\downarrow0\) and \(\Phi(t)\sim t/2\) as \(t\to\infty\).

## Verification

A standalone numerical checker (`check_projection.py`) compares the exact squared-axis gap (1) against direct, independently assembled plane-compression eigenvalues for \(16{,}384\) Haar-uniform directions at each of three sets of parameters. It also checks Cassini areas against the elliptic-integral expression by Sobol quadrature and tests the crossover ratios for several \(\eta\) values and tolerances, including the critical \(t=1\). Successful completion prints `ELLIPSOID_CASSINI_CROSSOVER_CHECKS_OK`.

These finite numerical comparisons test the derivation but are not a substitute for the dominated-convergence, Jacobian, or topology arguments above.

## Relationship to prior work

Binney (1985), following Stark (1977), derived the general projected-axis-ratio formula for triaxial ellipsoidal galaxies and plotted its viewing-direction contours. Jones, Basu and Dubinski (2001) applied the formula to observed cloud cores and emphasized the vanishing apparent-axis-ratio density at the round endpoint for fixed triaxial shapes. Those works cover the underlying projection geometry, not a uniform near-axisymmetric scaling law or its conditional Cassini-region geometry.

An earlier result on Haar-random **central sections** of fixed triaxial ellipsoids gives a quartic small-eccentricity tail. By planar polarity, shadows of an ellipsoid correspond to sections of its polar. Consequently the **fixed-shape quadratic tail in the squared-semiaxis gap is already covered** by that prior result and is not asserted here as new. The present result concerns the singular two-parameter regime where that fixed-shape asymptotic is nonuniform and cannot be substituted directly: it determines the complete crossover function, the logarithmic merger transition, and the conditional viewing-direction geometry.

Cassini ovals and their two-lobed/one-lobed transition are classical plane curves. Their occurrence here is a geometric limiting law, not a claim of discovery of Cassini ovals or complete elliptic integrals.

## Limitations

This theorem requires a near-oblate approach with the smallest squared semiaxis separated by a fixed \(\Delta>0\). It does not address simultaneous collapse of both gaps, arbitrary nonellipsoidal bodies, perspective projections, or nonuniform viewing directions. It determines first-order double-scaling probabilities and weak conditional limits, not a uniform error bound over all \(t\), nor finite-\(\eta\) closed probability distributions. Historical priority of the specific crossover law remains subject to broader literature checking; the classical general projection formula is acknowledged, and independent mathematical validation has not been carried out.

## References

1. J. Binney, *Testing for triaxiality with kinematic data*, Mon. Not. R. Astron. Soc. **212** (1985), 767–781; equations (10)–(12), Figure 1. https://articles.adsabs.harvard.edu/pdf/1985MNRAS.212..767B
2. C. E. Jones, S. Basu, J. Dubinski, *Intrinsic Shapes of Molecular Cloud Cores*, arXiv:astro-ph/0101106, initially public 2001-01-08; Sections 2 and 5. https://arxiv.org/abs/astro-ph/0101106
3. *Cassini oval*, Encyclopedia of Mathematics, mathematical background on the classical plane curve and lemniscate transition. https://encyclopediaofmath.org/wiki/Cassini_oval
