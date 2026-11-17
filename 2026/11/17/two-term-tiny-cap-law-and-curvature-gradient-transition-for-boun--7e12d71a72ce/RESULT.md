# Two-term tiny-cap law and curvature-gradient transition for boundary-random chords

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body whose boundary \(\Gamma\) is a positively oriented \(C^8\) closed curve of perimeter \(P\), with strictly positive curvature \(\kappa(s)\) in Euclidean arclength \(s\in\mathbb R/P\mathbb Z\). Choose independent \(X,Y\) uniformly from \(\Gamma\) by arclength, and let \(M\) be the area of the smaller of the two pieces of \(K\) cut by the line segment \([X,Y]\). Then, as \(t\downarrow0\),
\[
\boxed{\Pr(M\le t)=\frac{2(12t)^{1/3}}{P^2}\int_0^P\kappa(s)^{-1/3}\,ds+\frac{2t}{5P^2}\left(2\pi-\int_0^P\frac{\kappa'(s)^2}{\kappa(s)^3}\,ds\right)+O_K(t^{5/3}).}
\]
Here the derivative in the second integral is with respect to Euclidean arclength. The leading coefficient is minimized at fixed perimeter uniquely by the circle:
\[
\frac{2\,12^{1/3}}{P^2}\int_0^P\kappa^{-1/3}ds\ \ge\ 2(6/\pi)^{1/3}P^{-2/3}.
\]
The coefficient of \(t\) is **maximized** uniquely by the circle at fixed perimeter and is unbounded below among smooth positively curved curves of fixed perimeter. More precisely, for every integer \(m\ge2\), the analytic oval with radius of curvature \(\rho(\theta)=P(1+\varepsilon\cos(m\theta))/(2\pi)\), where \(0<\varepsilon<1\), has second coefficient
\[
\boxed{B_m(\varepsilon)=\frac{4\pi}{5P^2}\left[1-m^2\left(\frac1{\sqrt{1-\varepsilon^2}}-1\right)\right].}
\]
It changes sign exactly at \(\varepsilon_m=\sqrt{2m^2+1}/(m^2+1)\); for example \(\varepsilon_2=3/5\).

There is also an inverse marked law. Let \(S\) be the arclength midpoint of the **short** boundary arc between \(X,Y\), let \(\sigma\in\{-1,+1\}\) record its orientation relative to the labels, and put \(Z=M/t\). Conditional on \(M\le t\), the marked triple \((S,Z,\sigma)\) converges in total variation to independent factors: \(S\) has arclength density
\[
q(s)=\frac{\kappa(s)^{-1/3}}{\int_0^P\kappa(u)^{-1/3}\,du},
\]
\(Z\) has density \(z^{-2/3}/3\) on \((0,1)\), and \(\sigma\) is fair. Knowing \(q(s)\) on an arclength-labelled boundary recovers the curvature and therefore the curve up to a Euclidean rigid motion:
\[
\boxed{\kappa(s)=\frac{2\pi q(s)^{-3}}{\int_0^P q(u)^{-3}\,du}.}
\]

## Assumptions and scope
The body is fixed as \(t\downarrow0\), with \(C^8\) embedded boundary and \(\inf\kappa>0\). Both endpoints are independent and uniformly distributed with respect to the curve's Euclidean arclength; they are not sampled by invariant random lines or inside the body. For the small event, \(M\) equals the area of the locally short boundary cap. The small-\(t\) error bound depends on the fixed curve and is not uniform over the harmonic family as \(m\to\infty\). Labels for \(S\) mean a chosen arclength origin and orientation; without those labels its marginal law need not reconstruct the ordering of curvature values. Total variation is on \((\mathbb R/P\mathbb Z)\times[0,1]\times\{-1,+1\}\).

## Proof
**1. Exact local area representation.** Write \(\gamma(s)\) for the unit-speed counterclockwise boundary, with unit tangent \(T(s)\), and use signed midpoint coordinates \(X=\gamma(s-h/2)\), \(Y=\gamma(s+h/2)\). For \(h>0\) sufficiently small, the area of the cap between the short boundary arc and the chord is exactly
\[
A(s,h)=\frac12\int_{-h/2}^{h/2}\!du\int_u^{h/2}\!dv\;\det(T(s+u),T(s+v)).
\]
The tangent's turning angle satisfies \(\det(T(s+u),T(s+v))=\sin(\int_u^v\kappa(s+w)\,dw)\). The curvature is positive and bounded, so this cap area increases strictly with small \(h>0\), uniformly in \(s\). Symmetry of midpoint coordinates eliminates even powers in the expansion. Taylor's formula, uniformly in \(s\), gives
\[
\boxed{A(s,h)=\frac{\kappa(s)}{12}h^3+\left(\frac{\kappa''(s)}{480}-\frac{\kappa(s)^3}{240}\right)h^5+O_K(h^7).}
\]
For example, the coefficient of \(\kappa''\) is the integral of \((v^3-u^3)/12\), while the cubic term comes from \(-\kappa^3(v-u)^3/12\). Both are elementary integrals over \(-h/2\le u\le v\le h/2\). The exact unit-circle area \((h-\sin h)/2\) independently gives \(h^3/12-h^5/240+O(h^7)\).

**2. Invert the cap area.** Uniform positive curvature permits a unique small positive solution \(H(s,t)\) of \(A(s,H)=t\), uniformly for all \(s\). Inverting the previous expansion yields
\[
H(s,t)=\left(\frac{12t}{\kappa(s)}\right)^{1/3}
+\frac{12t}{\kappa(s)}\left(\frac{\kappa(s)^2}{60}-\frac{\kappa''(s)}{120\kappa(s)}\right)+O_K(t^{5/3}).
\]
Since distinct points of a compact strictly convex curve have a positive smaller cut area away from the diagonal, every sufficiently small cut comes from a unique short arc; no distant-endpoint events are omitted. The map from labelled endpoints to \((s,h)\) has Jacobian one, and both signs of \(h\) are allowed. Thus **exactly** for sufficiently small \(t\),
\[
\Pr(M\le t)=\frac{2}{P^2}\int_0^P H(s,t)\,ds.
\]
The contribution of order \(t\) simplifies using \(\int\kappa ds=2\pi\) and periodic integration by parts,
\[
\int_0^P\frac{\kappa''}{\kappa^2}ds=2\int_0^P\frac{(\kappa')^2}{\kappa^3}ds.
\]
Substitution proves the two-term probability formula including the stated remainder.

**3. Extremal coefficients.** The turning-tangent identity and strict convexity of \(x\mapsto x^{-1/3}\) imply by Jensen
\[
\int_0^P\kappa^{-1/3}ds\ge P\left(\frac{2\pi}{P}\right)^{-1/3}.
\]
Equality requires constant positive curvature and hence a circle. The integral \(J(K)=\int(\kappa')^2/\kappa^3ds\) is nonnegative, and vanishes only for circles, proving the unique maximal second coefficient.

**4. Exact sign transition and unboundedness.** For \(m\ge2\), \(\rho_m(\theta)=P(1+\varepsilon\cos m\theta)/(2\pi)\) is positive; integration of \(\rho_m(\theta)(\cos\theta,\sin\theta)\) closes by Fourier orthogonality and gives a smooth embedded strictly convex oval with perimeter \(P\). In normal-angle coordinates \(ds=\rho_m d\theta\) and \(\kappa=1/\rho_m\), so
\[
J(K)=\int_0^{2\pi}\left(\frac{d}{d\theta}\log\rho_m(\theta)\right)^2d\theta
=2\pi m^2\left((1-\varepsilon^2)^{-1/2}-1\right).
\]
The last equality follows by integrating \(\varepsilon^2\sin^2u/(1+\varepsilon\cos u)^2\) over one period. Substitution gives \(B_m\). Its bracket decreases strictly from \(1\) to \(-\infty\) as \(\varepsilon\uparrow1\), with the unique specified zero. At any fixed \(0<\varepsilon<1\), letting \(m\to\infty\) sends the second coefficient to \(-\infty\), each oval separately satisfying the theorem.

**5. Marked limit and inverse rigidity.** Conditional on \(M\le t\), \(s\) has density proportional to \(H(s,t)\), which converges uniformly after normalization to \(q(s)\). Conditional on any \(s\), the sign of \(h\) is fair and \(V=|h|/H(s,t)\) is **exactly** independent uniform on \((0,1)\). The local area expansion gives \(M/t=V^3+O_K(t^{2/3})\) uniformly in \(s,V\), and its monotone change-of-variable density converges pointwise to \(z^{-2/3}/3\); probability densities integrate to one, so Scheffé's lemma yields joint total-variation convergence. Solving the identity for \(q\) gives \(\kappa(s)=c q(s)^{-3}\); the turning-tangent identity forces \(c=2\pi/\int_0^P q^{-3}\). The fundamental theorem of plane curves then reconstructs the curve up to a rigid motion from this arclength-labelled curvature. This completes the proof.

## Verification
The standalone `cap_checker.py` independently computes cap areas on normal-angle-parametrized analytic ovals by high-precision Green-theorem integration, checks the \(h^3\)/\(h^5\) coefficients and the \(h^7\) residual decay, checks the closed-form curvature-gradient integral for multiple Fourier modes, and tests the two-term circle probability against an exact inverse-sine relation. Running `python cap_checker.py` with Python 3 and `mpmath` produced `SMOOTH_CAP_AREA_CHECKS_OK`. Computation corroborates but does not replace the analytic proof. The specific oval parameters and exact-circle comparisons are recorded in the standalone code.

## Relationship to prior work
Bárány, Fodor and Vígh (arXiv:0906.0309, public 2009-06-01) develop cap techniques and intrinsic-volume asymptotics for convex hulls of **interior-uniform** samples; their results do not give this two-endpoint boundary-chord cap-area distribution. Pardon (arXiv:1003.4209, public 2010-03-22) treats many-point interior random polygons, a distinct asymptotic model. Craizer, Teixeira and da Silva (arXiv:1103.2722, public 2011-03-14) study equal-area polygons and affine arclength, not the present random-chord distribution. Bäsel (arXiv:1204.2707, public 2012-04-12) gives chord lengths for random **lines** in regular polygons and interior-point distances, not smooth-boundary area cuts.

Related published results concern the small area of a **three-point** inscribed triangle on a smooth curve, and the fifth-order small **Euclidean chord distance** law for two boundary points. These establish important curvature-dependent comparators but neither is a formula for the two-term area of the *smaller chord-cut cap*, its inverse marked law or its harmonic sign threshold. The known polygonal-boundary smaller-cut law has a nonzero atom and positive \(t\log(1/t)\) tail instead of the smooth \(t^{1/3}\) regime; it is likewise not a specialization or a dominating theorem. No claim is made that the circle cap probability or the Frenet local expansion, separately, is historically new.

## Limitations
The theorem is for independent uniform-arclength endpoints on a fixed positive-curvature \(C^8\) convex oval. It gives no uniform remainder under degenerating curvature or increasing harmonic frequency. The conditional inverse uses known arclength labels, not an unordered scalar area distribution. Classical and unindexed area-cap literature could contain equivalent expansions; priority remains provisional. No independent mathematical audit has been performed.

## References
1. I. Bárány, F. Fodor, V. Vígh, *Intrinsic volumes of inscribed random polytopes in smooth convex bodies*, arXiv:0906.0309 (2009-06-01). https://arxiv.org/abs/0906.0309
2. J. Pardon, *Central limit theorems for random polygons in an arbitrary convex set*, arXiv:1003.4209 (2010-03-22). https://arxiv.org/abs/1003.4209
3. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Affine Properties of Convex Equal-Area Polygons*, arXiv:1103.2722 (2011-03-14). https://arxiv.org/abs/1103.2722
4. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707 (2012-04-12). https://arxiv.org/abs/1204.2707
5. D. Ren, *Random chord distributions and containment functions*, *Advances in Applied Mathematics* 58 (2014), 1–20, DOI:10.1016/j.aam.2014.05.003 (different invariant-line sampling; complete text not inspected).
