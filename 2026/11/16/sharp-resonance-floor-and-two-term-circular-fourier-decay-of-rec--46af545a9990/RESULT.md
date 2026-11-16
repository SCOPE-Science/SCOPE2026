# Sharp resonance floor and two-term circular Fourier decay of rectangles

## Finding

For an axis-aligned rectangle \(Q_{a,b}=[-a,a]\times[-b,b]\) with arbitrary fixed \(a,b>0\), the complete first two orders of its circular squared Fourier energy admit a uniform asymptotic formula, including the oscillations at radii where the leading order vanishes:

\[
\begin{aligned}
E_{a,b}(R)={}&\frac{32\pi}{R^3}\bigl(b\sin^2(aR)+a\sin^2(bR)\bigr)\\
&+\frac{8\sqrt{2\pi}}{R^{7/2}}\bigl[\sqrt a(\cos(2aR)-\sin(2aR))
+\sqrt b(\cos(2bR)-\sin(2bR))\bigr]
+o_{a,b}(R^{-7/2}).
\end{aligned}
\]

As a sharp consequence, irrespective of the arithmetic type of the aspect ratio,
\[
\boxed{\liminf_{R\to\infty}R^{7/2}E_{a,b}(R)=8\sqrt{2\pi}(\sqrt a+\sqrt b).}
\]
In particular, the improvement of the generic \(R^{-3}\) energy scale to \(R^{-7/2}\) along simultaneous near-resonant radii has a strictly positive, explicit optimal coefficient.

## Assumptions and scope

The Fourier convention is \(\widehat f(\xi)=\int_{\mathbb R^2}f(x)e^{-i x\cdot\xi}\,dx\), with no \(2\pi\) in the phase. The angular measure is unnormalized arclength, \(d\theta\), on the unit circle. Precisely,
\[
E_{a,b}(R)=\int_0^{2\pi}\left|\widehat{\mathbf1}_{[-a,a]\times[-b,b]}(R\cos\theta,R\sin\theta)\right|^2\,d\theta.
\]
The parameters \(a,b\) are any fixed positive real numbers, while \(R\) tends to positive infinity through arbitrary real values. No uniformity as \(a\) or \(b\) tends to zero or infinity is asserted. A rotation of the rectangle changes neither the angular average nor the conclusion.

## Proof

**Step 1: exact reduction.** By the product Fourier transform and quadrant symmetry, with the axis values understood continuously,
\[
E_{a,b}(R)=\frac{64}{R^4}\int_0^{\pi/2}
\frac{\sin^2(aR\cos\theta)\sin^2(bR\sin\theta)}{\cos^2\theta\sin^2\theta}\,d\theta.\tag{1}
\]
Fix \(0<\delta<\pi/4\) independently of \(R\). The integral over \([\delta,\pi/2-\delta]\) is \(O_{a,b,\delta}(1)\), contributing \(O(R^{-4})\) to (1). It remains to expand the two disjoint endpoint pieces.

**Step 2: axial contribution.** At the endpoint \(\theta=0\), write the integral as \(\sin^2(aR)S_R+T_R\), where
\[
S_R=\int_0^\delta\frac{\sin^2(bR\sin\theta)}{\cos^2\theta\sin^2\theta}\,d\theta,
\]
\[
T_R=\int_0^\delta\frac{[\sin^2(aR\cos\theta)-\sin^2(aR)]\sin^2(bR\sin\theta)}{\cos^2\theta\sin^2\theta}\,d\theta.
\]
Substitute \(u=\sin\theta\). The density of \(S_R\) is \(u^{-2}(1-u^2)^{-3/2}\sin^2(bRu)\). On the fixed interval \(0\le u\le\sin\delta\), \((1-u^2)^{-3/2}-1=O_\delta(u^2)\). After restoring the bounded tail, the standard integral \(\int_0^\infty\sin^2(cu)u^{-2}\,du=\pi|c|/2\) yields
\[
S_R=\frac{\pi bR}{2}+O_{b,\delta}(1).\tag{2}
\]
The error in (2), multiplied by \(\sin^2(aR)\), is uniformly \(O(1)\).

**Step 3: the oscillatory boundary layer.** Put \(x=\sqrt R\,\theta\) and \(\phi=aR\). In \(T_R/\sqrt R\), the nonoscillatory factor is
\[
\frac{\sin^2\bigl(\phi+aR(\cos(x/\sqrt R)-1)\bigr)-\sin^2\phi}{x^2}
\frac{(x/\sqrt R)^2}{\cos^2(x/\sqrt R)\sin^2(x/\sqrt R)}.
\]
It converges for every fixed positive \(x\) to \([\sin^2(\phi-a x^2/2)-\sin^2\phi]/x^2\) in the following uniform-in-\(\phi\) sense: express each difference as a linear combination of \(\cos(2\phi)\) and \(\sin(2\phi)\). The coefficient functions converge pointwise and are bounded by an integrable majorant \(C_{a,\delta}\min(1,x^{-2})\), because \(|R(\cos(x/\sqrt R)-1)|\le x^2/2\). Dominated convergence gives uniform \(L^1\)-convergence of the coefficient functions on the extended interval \([0,\infty)\) (extended by zero beyond \(\delta\sqrt R\)).

The remaining multiplier \(\sin^2(bR\sin(x/\sqrt R))\) converges weakly to \(1/2\) on every bounded \(x\)-interval: its cosine phase has derivative \(2b\sqrt R\cos(x/\sqrt R)\), bounded below by a positive multiple of \(\sqrt R\) for fixed \(x\)-intervals. Integration by parts after smooth \(L^1\) approximation proves the nonstationary-phase assertion; the integrable tail bound makes the replacement valid on the half-line. Uniformly for \(\phi=aR\), therefore,
\[
T_R=\frac{\sqrt R}{2}F_a(\phi)+o_{a,b,\delta}(\sqrt R),\qquad
F_a(\phi)=\int_0^\infty\frac{\sin^2(\phi-a x^2/2)-\sin^2\phi}{x^2}\,dx.\tag{3}
\]
By the identity \(2[\sin^2(\phi-t)-\sin^2\phi]=\cos(2\phi)-\cos(2\phi-2t)\),
\[
F_a(\phi)=\frac12\cos(2\phi)\int_0^\infty\frac{1-\cos(a x^2)}{x^2}\,dx
-\frac12\sin(2\phi)\int_0^\infty\frac{\sin(a x^2)}{x^2}\,dx.
\]
Both convergent Fresnel integrals equal \(\sqrt{\pi a/2}\), by integration by parts (first truncate at large \(x\)) and the classical Fresnel integrals \(\int_0^\infty\cos(a x^2)\,dx=\int_0^\infty\sin(a x^2)\,dx=\sqrt{\pi/(8a)}\). Consequently
\[
F_a(\phi)=\sqrt{\frac{\pi a}{8}}\bigl(\cos(2\phi)-\sin(2\phi)\bigr).\tag{4}
\]
Combining (2)–(4), the first endpoint of (1), *before* the prefactor \(64/R^4\), equals
\[
\frac{\pi bR}{2}\sin^2(aR)
+\frac{\sqrt R}{2}\sqrt{\frac{\pi a}{8}}
[\cos(2aR)-\sin(2aR)]+o(\sqrt R).
\]
The bounded error from (2) is absorbed in the latter little-o term.

**Step 4: the other endpoint.** Replacing \(\theta\) by \(\pi/2-\theta\) and interchanging \(a,b\) yields the corresponding term
\[
\frac{\pi aR}{2}\sin^2(bR)
+\frac{\sqrt R}{2}\sqrt{\frac{\pi b}{8}}
[\cos(2bR)-\sin(2bR)]+o(\sqrt R).
\]
Multiplying the sum by \(64/R^4\) proves the claimed two-term expansion and its uniformity in the real radius \(R\).

**Step 5: exact global lower envelope.** Multiply the expansion by \(R^{7/2}\). The result is
\[
32\pi\sqrt R\bigl[b\sin^2(aR)+a\sin^2(bR)\bigr]
+8\sqrt{2\pi}\bigl[\sqrt a(\cos(2aR)-\sin(2aR))
+\sqrt b(\cos(2bR)-\sin(2bR))\bigr]+o(1).\tag{5}
\]
Consider any sequence \(R_j\to\infty\) on which the left side of (5) remains bounded. Since the second bracket is uniformly bounded, the nonnegative leading term in (5) is bounded, forcing \(\sin(aR_j),\sin(bR_j)=O(R_j^{-1/4})\). Thus both phases approach integer multiples of \(\pi\), so every cosine of a doubled phase tends to \(1\) and every corresponding sine tends to \(0\). The second bracket in (5) tends to \(\sqrt a+\sqrt b\); the first is nonnegative. Any bounded subsequential lower limit is therefore at least \(8\sqrt{2\pi}(\sqrt a+\sqrt b)\).

For the reverse inequality, put \(\rho=b/a\). If \(\rho\) is rational, choose arbitrarily large integers \(m\) such that \(m\rho\in\mathbb Z\); set \(R_m=m\pi/a\). If \(\rho\) is irrational, choose the infinitely many denominators \(m\) of its continued-fraction convergents, for which there exist integers \(n\) with \(|m\rho-n|<1/m\), and again set \(R_m=m\pi/a\). In either case \(\sin(aR_m)=0\), \(\sin(bR_m)=O(1/m)\); hence the first term of (5) tends to zero and the second tends to the stated constant. Combining both inequalities proves the exact liminf for all positive \(a,b\).

## Verification

A standalone standard-Python numerical checker evaluates the exact trigonometric integral using composite Simpson quadrature at increasing resonant radii for three distinct aspect ratios, and compares against the proved lower-envelope constant. It also checks the two-term approximation for a generic nonresonant rectangle. The numerical checks are finite sanity tests, not proof of the real-radius asymptotic or of the infinite liminf; these follow from Steps 1–5.

## Relationship to prior work

Brandolini–Colzani–Travaglini (1997), §1, formula for the square and the subsequent polyhedral decay estimates, supplies the Fourier product formula and coarse upper estimates but not the all-radius two-term asymptotic or the sharp liminf coefficient. Brandolini–Rigoli–Travaglini (1998), Lemma 3.12(ii), treats enhanced square decay on an integer-radius sequence by upper bounds, without identifying the exact \(R^{-7/2}\) constant for arbitrary rectangles. Brandolini–Hofmann–Iosevich (2003) gives universal mean-square convex-body decay of order \(R^{-3}\) in the plane. Iosevich–Merlo–Mourgoglou (2026) gives sharp boundary-regularity criteria for the generic spherical average decay; its object is general domains rather than rectangular exact oscillatory profiles. None of those inspected statements implies the sharp all-aspect-ratio resonance floor. The present result is consistent with all these bounds.

## Limitations

The result applies to rectangles in the plane, not general polygons or higher-dimensional boxes. Its little-o estimate is for each fixed positive \(a,b\); no estimate uniform in an unbounded family of aspect ratios is claimed. The proof does not quantify the speed of convergence along the irrational continued-fraction sequence or assert that every sequence of near-minima is of that precise form. Earlier equivalent formulations in diffraction or convex Fourier-analysis literature have not been exhaustively ruled out; the precise historical priority remains provisional.

## References

- L. Brandolini, L. Colzani, G. Travaglini, *Average decay of Fourier transforms and integer points in polyhedra*, Arkiv för Matematik 35 (1997), 253–275, DOI: 10.1007/BF02559969. Open PDF: https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7682-11512_2007_Article_BF02559969.pdf
- L. Brandolini, M. Rigoli, G. Travaglini, *Average decay of Fourier transforms and geometry of convex sets*, Revista Matemática Iberoamericana 14 (1998), 519–560, DOI: 10.4171/RMI/244.
- L. Brandolini, S. Hofmann, A. Iosevich, *Sharp rate of average decay of the Fourier transform of a bounded set*, Geometric and Functional Analysis 13 (2003), 671–680, arXiv:math/0303188.
- A. Iosevich, A. Merlo, M. Mourgoglou, *Sharp decay of the spherical averages of the Fourier transform of open sets*, arXiv:2611.04426v1, first posted 2026-11-03.
