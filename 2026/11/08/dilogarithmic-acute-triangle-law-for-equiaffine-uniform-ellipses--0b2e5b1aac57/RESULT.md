# Dilogarithmic acute-triangle law for equiaffine-uniform ellipses

## Finding
Let \(a,b>0\) and let three independent boundary points of the ellipse
\[E_{a,b}=\{(a\cos t,b\sin t):0\le t<2\pi\}\]
be sampled with the normalized equiaffine arclength law. Write \(p(a,b)\) for the probability their ordinary Euclidean triangle has three strictly acute angles, and set
\[\eta=\frac{|a^2-b^2|}{a^2+b^2}.\]
Then
\[\boxed{p(a,b)=\frac14-\frac{3}{2\pi^2}\operatorname{Li}_2(\eta^2)},\qquad
\operatorname{Li}_2(z)=\sum_{m=1}^\infty\frac{z^m}{m^2}.\]
The circle uniquely maximizes \(p\) among ellipses; as the semiaxis ratio \(q=\max(a,b)/\min(a,b)\) rises from \(1\) to infinity, \(p\) strictly falls from \(1/4\) toward \(0\). Hence a single acute-triangle probability recovers \(q\) uniquely. The sharp, globally valid deficit bounds are
\[\frac{3}{2\pi^2}\eta^2\le\frac14-p(a,b)\le\frac14\eta^2.\]
The left coefficient is optimal as \(\eta\downarrow0\); the right is optimal as \(\eta\uparrow1\), though every noncircular nondegenerate ellipse satisfies both strictly. With \(\delta=4q^2/(q^2+1)^2\),
\[p(a,b)=\frac{3}{2\pi^2}\delta(1-\log\delta)+O(\delta^2|\log\delta|),\qquad q\to\infty.\]
The same numerical function is known from a *different* experiment: the probability that three independently uniform points on a unit circle enclose a preassigned interior point at distance \(\eta\) from its center. The circular-enclosure formula is prior work; the equality with the equiaffine-ellipse acute probability is the new comparison.

## Assumptions and scope
The ellipse has \(a,b>0\); triangle vertices are sampled independently using normalized affine arclength, not Euclidean arclength. For a Euclidean unit-speed curve with curvature \(\kappa>0\), the equiaffine line element is \(\kappa^{1/3}ds\). For \(x(t)=(a\cos t,b\sin t)\),
\[|\det(x'(t),x''(t))|^{1/3}dt=(ab)^{1/3}dt.\]
Therefore affine-arclength sampling corresponds **exactly** to independent uniform parameters \(t_i\in[0,2\pi)\). By symmetry we may assume \(a\ge b\); the isotropic case follows by continuity. Right-angle and repeated-point events have probability zero.

## Proof
Fix \(t_1=t\), put \(u=(t_2-t_1)\bmod 2\pi\), \(v=(t_3-t_1)\bmod 2\pi\), and set \(w=|u-v|\). These variables have \(t\) independent uniform on \([0,2\pi)\), \(u,v\) independent uniform there, and
\[f_W(w)=\frac{2\pi-w}{2\pi^2},\qquad 0<w<2\pi.\]
The chord identity
\[x(t+u)-x(t)=2\sin(u/2)\,(-a\sin(t+u/2),b\cos(t+u/2))\]
shows that the Euclidean angle at the first vertex is obtuse precisely when
\[\cos(w/2)-\eta\cos\bigl(2t+(u+v)/2\bigr)<0.\]
The phase \(2t+(u+v)/2\) is uniform modulo \(2\pi\) conditionally on \(u,v\). Let \(q_\eta(w)\) be this conditional obtuse probability. For \(0<\eta<1\),
\[q_\eta(w)=\begin{cases}
0,&\cos(w/2)\ge\eta,\\
\pi^{-1}\arccos(\cos(w/2)/\eta),&|\cos(w/2)|<\eta,\\
1,&\cos(w/2)\le-\eta.
\end{cases}\]
Because \(q_\eta(2\pi-w)=1-q_\eta(w)\), pairing the two halves of the integral against \(f_W\) gives
\[\Pr(\text{obtuse at vertex }1)=\frac14+
\frac1{\pi^2}\int_0^\pi(\pi-w)q_\eta(w)\,dw.\]
Only the interval \(2\arccos\eta<w<\pi\) contributes. Set \(z=\pi-w\), integrate by parts after substituting \(z=2y\), and then set \(\sin y=\eta\sin s\). The result is
\[\Pr(\text{obtuse at vertex }1)=\frac14+
\frac2{\pi^3}\int_0^{\pi/2}\arcsin^2(\eta\sin s)\,ds.\]
A Euclidean triangle has at most one obtuse angle. Symmetry among three sampled vertices therefore yields
\[p(a,b)=1-3\Pr(\text{obtuse at vertex }1)
=\frac14-\frac6{\pi^3}\int_0^{\pi/2}\arcsin^2(\eta\sin s)\,ds.\]
For \(0\le\eta<1\), the classical absolutely convergent series
\[\arcsin^2 z=\frac12\sum_{m=1}^\infty
\frac{(2z)^{2m}}{m^2\binom{2m}{m}}\]
and
\[\int_0^{\pi/2}\sin^{2m}s\,ds=\frac\pi2\frac{\binom{2m}{m}}{4^m}\]
combine to give
\[\int_0^{\pi/2}\arcsin^2(\eta\sin s)\,ds
=\frac\pi4\operatorname{Li}_2(\eta^2).\]
This proves the exact law; the limiting endpoint follows by dominated convergence. Since \(\operatorname{Li}_2\) is strictly increasing on \((0,1)\) and \(\eta=(q^2-1)/(q^2+1)\) increases strictly with \(q\ge1\), the circle is the unique maximizer and the inverse ratio is unique. The series gives \(1\le\operatorname{Li}_2(z)/z\le\pi^2/6\) on \(0<z<1\), with sharp endpoint limits, proving the inequalities. Finally, integration of \(-\log(1-z)/z\) at \(z=1\) yields
\[\operatorname{Li}_2(1)-\operatorname{Li}_2(1-\delta)
=\delta(1-\log\delta)+O(\delta^2|\log\delta|),\]
which gives the stated degeneration rate.

## Verification
The accompanying `verify.py` independently evaluates the angularly conditioned obtuse probability, the arcsine-squared integral, and the dilogarithm series using standard-library arithmetic. It also independently samples vertices in the ellipse, tests the three Euclidean dot products, and checks the trigonometric integrals for several integer exponents. Successful replay produces `ELLIPSE_ACUTE_CHECK_OK formulas=5 direct_samples=800000`. Numerical experiments are supplementary; the exact derivation above is the proof.

## Relationship to prior work
Hall's 1982 paper treats acute triangles chosen **inside** Euclidean balls rather than equiaffine boundary sampling. Dendrinos–Laghi–Wright (first arXiv version 2008-05-28) establish the significance of affine arclength measures on curves but do not study acute triangles. A 2024/2025 mathematical discussion of acute triangles on an ellipse assumes **ordinary Euclidean perimeter-uniform sampling** and gives a triple-integral approach, not the present probability law. Tan's 2018 circle-point enclosure solution and Ismailov's 2026 exposition establish the *same dilogarithm function for circular enclosure*, a distinct event. The exact coincidence is acknowledged and not misrepresented as a new dilogarithm evaluation. It takes the nontrivial chord-angle conditioning above to link it to this ellipsoidal sampling model.

## Limitations
No result is asserted for the Euclidean-arclength law, generic smooth convex curves, or arbitrary non-equi-affine sampling. The identity concerns the scalar acute probability only, not equality of the full triangle-shape distributions or a samplewise bijection. Priority among unindexed historical geometric-probability sources is not independently certified.

## References
- G. R. Hall, *Acute triangles in the n-ball*, Journal of Applied Probability 19 (1982), DOI: `10.2307/3213533`.
- S. Dendrinos, N. Laghi, J. Wright, *Universal Lp improving for averages along polynomial curves in low dimensions*, arXiv:0805.4344, first posted 2008-05-28.
- J. Tan Jie Rui, solution to *Probability that a random triangle with vertices on a circle contains an arbitrary point inside said circle*, Mathematics Stack Exchange, 2018-02-10, question 2641793.
- A. Ismailov, *With what probability does an inscribed triangle contain a given point?*, arXiv:2601.02929, first posted 2026-01-06.
- C. Boilley, answer to *Probability that Triangle on Ellipse is Acute*, Mathematics Stack Exchange, 2025-01-24, question 5014676.
