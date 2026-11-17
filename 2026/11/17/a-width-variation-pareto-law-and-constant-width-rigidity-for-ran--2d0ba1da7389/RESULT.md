# A width-variation Pareto law and constant-width rigidity for random normal intersections

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body with \(C^3\) support function \(h\), positive radius of curvature \(h+h''>0\), and width \(w(\theta)=h(\theta)+h(\theta+\pi)\). Independently choose two outward-normal angles \(\Theta,\Phi\) with a common strictly positive continuous circular density \(f\). Let \(Z\) be the intersection of the full Euclidean normal lines at the corresponding boundary points, defined almost surely.

Then
\[
\lim_{R\to\infty}R\Pr\{\|Z\|>R\}=C_{K,f}:=2\int_0^{2\pi}f(\theta)f(\theta+\pi)|w'(\theta)|\,d\theta.
\]
The support of the distribution of \(Z\) is bounded if and only if \(K\) has constant width. In the nonconstant-width case \(C_{K,f}>0\), \(\mathbb E\|Z\|^p<\infty\) precisely for \(0<p<1\), and \(\mathbb E\|Z\|^p=\infty\) for \(p\ge1\).

For a marked limit define \(s=\operatorname{wrap}(\Phi-\Theta-\pi)\in(-\pi,\pi]\). If \(C_{K,f}>0\), the conditional law of \((\Theta,Rs)\) given \(\|Z\|>R\) converges in **total variation** to the probability density
\[
G(\theta,q)=\frac{f(\theta)f(\theta+\pi)}{C_{K,f}}\,\mathbf1_{\{|q|<|w'(\theta)|\}}
\quad (0\le\theta<2\pi,\ q\in\mathbb R).
\]
Thus in the limiting conditional law the normal direction has density \(2f(\theta)f(\theta+\pi)|w'(\theta)|/C_{K,f}\), the sign of the near-antipodal angle error is a fair sign, and the absolute error normalized by \(|w'(\Theta)|/R\) is independent uniform on \((0,1)\). In particular \(R/\|Z\|\), conditional on \(\|Z\|>R\), converges **weakly** to a uniform \((0,1)\) variable.

Under uniform normal-angle sampling \(f=1/(2\pi)\),
\[
C_{K,f}=\frac1{2\pi^2}\int_0^{2\pi}|w'(\theta)|\,d\theta.
\]
For an ellipse with semiaxes \(a>b>0\) this equals \(4(a-b)/\pi^2\). Thus the far-field normal-intersection probability exactly measures total variation of directional width, and it vanishes precisely for constant-width ovals.

## Assumptions and scope
The body is planar; \(h\) is real-valued, \(2\pi\)-periodic and \(C^3\); \(h+h''>0\). The origin is arbitrary and fixed; translations change \(Z\) by a bounded vector and do not change the far-field coefficient. The two angles are independent and have the same continuous density \(f>0\), normalized by \(\int_0^{2\pi}f=1\). Sampling uniformly in arc length corresponds to \(f(\theta)=[h(\theta)+h''(\theta)]/L\), \(L=\int_0^{2\pi}[h+h'']\,d\theta\). All normal lines are complete, not rays. Parallel pairs have probability zero, so \(Z\) is defined almost surely. The marked convergence is stated in total variation for the angular mark \((\Theta,Rs)\), not for \(R/\|Z\|\).

## Proof
Write \(n_\theta=(\cos\theta,\sin\theta)\) and \(t_\theta=(-\sin\theta,\cos\theta)\). Standard support-function parametrization gives the contact point \(x_\theta=h(\theta)n_\theta+h'(\theta)t_\theta\). Its normal line has equation \(z\cdot t_\theta=h'(\theta)\). For \(\delta=\Phi-\Theta\notin\pi\mathbb Z\), solve the two line equations in the orthonormal basis \((n_\Theta,t_\Theta)\):
\[
Z=a(\Theta,\delta)n_\Theta+h'(\Theta)t_\Theta,
\quad a(\theta,\delta)=\frac{h'(\theta)\cos\delta-h'(\theta+\delta)}{\sin\delta}.
\tag{1}
\]
This is exact; it is also an independently testable coordinate equation. Because \(h'\) is continuously differentiable, \(a(\theta,\delta)\to-h''(\theta)\) uniformly in \(\theta\) as \(\delta\to0\). Hence the almost-parallel normals at nearby contact points have uniformly bounded intersections. On compact angular regions away from \(0\) and \(\pi\) modulo \(2\pi\), equation (1) is bounded.

Only the opposite-normal diagonal matters. Put \(\delta=\pi+s\) with \(|s|\) small. Equation (1) becomes
\[
a(\theta,\pi+s)=\frac{h'(\theta)\cos s+h'(\theta+\pi+s)}{\sin s}
=\frac{w'(\theta)}s+O_K(1),
\tag{2}
\]
with an error bounded uniformly in \(\theta\) and \(s\) for small nonzero \(s\). The \(t_\Theta\)-component of \(Z\) is uniformly bounded. Equation (2) proves that all normal intersections are uniformly bounded when \(w'\equiv0\); conversely any \(\theta\) with \(w'(\theta)\ne0\) gives unbounded intersections as \(s\to0\). Since \(w\) is periodic, \(w'\equiv0\) if and only if the width is constant.

For the tail, set \(q=Rs\). There is a fixed \(B<\infty\) such that, for all sufficiently large \(R\), the event \(\|Z\|>R\) forces \(|s|<B/R\), and consequently \(|q|<B\). Indeed, outside a small neighborhood of the opposite-normal diagonal intersections are bounded, while (2) gives \(\|Z\|\le \|w'\|_\infty/|s|+O_K(1)\) inside that neighborhood. For each \(\theta\) and nonzero fixed \(q\), equations (1)–(2) give
\[
R^{-1}\|Z(\theta,\theta+\pi+q/R)\|\longrightarrow |w'(\theta)/q|.
\]
Hence for almost every \((\theta,q)\), the tail-event indicator converges to \(\mathbf1_{|q|<|w'(\theta)|}\). The change of variables \(\Phi=\Theta+\pi+q/R\) turns the probability into
\[
R\Pr(\|Z\|>R)=\int_0^{2\pi}\int_{-B}^{B}
 f(\theta)f(\theta+\pi+q/R)
 \mathbf1_{\{\|Z\|>R\}}\,dq\,d\theta.
\]
Bounded convergence proves the coefficient \(C_{K,f}\), including the zero-coefficient constant-width case; the latter was already shown to have bounded support. Because \(f>0\), continuity and nonconstancy of \(w\) imply \(C_{K,f}>0\). The nonnegative unnormalized densities on \((\theta,q)\) converge pointwise almost everywhere, and their total integrals converge to \(C_{K,f}\). Dividing by the actual tail probability and applying Scheffé's lemma proves total-variation convergence to \(G\).

For \(C_{K,f}>0\), the conditional \(q\)-section at a fixed \(\theta\) is uniform on \((-|w'(\theta)|,|w'(\theta)|)\). Therefore its sign and normalized magnitude are independent fair-sign and uniform variables; equation (2) further gives \(R/\|Z\|\Rightarrow U\sim\operatorname{Unif}(0,1)\), jointly with the angle and sign marks. The layer-cake identity \(\mathbb E\|Z\|^p=p\int_0^\infty R^{p-1}\Pr(\|Z\|>R)\,dR\) yields the claimed moment threshold.

For the ellipse, \(h(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}\) and \(w=2h\). The total variation of \(h\) on one full cycle is \(4(a-b)\). Insert this into the uniform-angle coefficient to obtain \(C=4(a-b)/\pi^2\).

## Verification
The exact normal-line equation and small-angle expansion supply the mathematical verification. The standalone `normal_intersection_checks.py` independently calculates line intersections for the positively curved support function \(h=1+0.2\cos(2\theta)\). The predicted coefficient is \(1.6/\pi^2=0.16211389382774044\). Four million independent pairs yielded ratios of \(R\widehat{\Pr}(\|Z\|>R)\) to that coefficient of approximately 0.9999, 1.0040, 1.0082, and 0.9879 at thresholds \(R=20,40,80,160\). For the noncircular constant-width, positively curved support \(h=1+0.1\cos(3\theta)\), a separate 500,000-pair check found bounded intersections. Numerical tests are corroborative and do not prove the limit.

Run with `python normal_intersection_checks.py` (requires Python 3 and NumPy). The code is supplementary; no proof step rests on its output.

## Relationship to prior work
The support-function identity defining constant width, and basic curvature facts, are classical. Bárány and Schneider (2014, first arXiv posting April 28) study curvature behavior of constant-width bodies and use that identity. Giblin and Holtom's *The Centre Symmetry Set* examines the envelope of chords joining opposite parallel-tangent contacts; it observes that for constant-width curves those chords are common normals. Neither source, in the material inspected, gives the distribution of intersections of two independently sampled full normal lines, its \(R^{-1}\) coefficient, or the total-variation conditional angular law. The 2007 characterization paper of Lachand-Robert and Oudet was accessible only at abstract level; it is a residual priority risk concerning the deterministic boundedness characterization, not evidence for the marked probability law. A search of related random-line and normal-multiplicity literature did not establish coverage of the statement.

## Limitations
This is a planar result for \(C^3\), strictly positively curved bodies and strictly positive continuous normal-angle density. It does not address nonsmooth Reuleaux polygons, dependent sampling, normal rays, or higher-dimensional normal-line intersections. No quantitative convergence rate is proved. The deterministic constant-width equivalence has classical ingredients and is not asserted to be historically new in isolation. Although the particular probability and conditional limits were not found in the inspected literature, definitive priority and independent mathematical validation remain unestablished.

## References
- I. Bárány and R. Schneider, *Typical curvature behaviour of bodies of constant width*, arXiv:1404.7019 (first public posting 2014-04-28). https://arxiv.org/abs/1404.7019
- P. Giblin and P. Holtom, *The Centre Symmetry Set*, Banach Center Publications 50 (1999), particularly §§1–2. https://www.liverpool.ac.uk/~pjgiblin/papers/giblin-holtom1999.pdf
- *Oval*, Encyclopedia of Mathematics, support-function and curvature description. https://encyclopediaofmath.org/wiki/Oval
- T. Lachand-Robert and É. Oudet, *Bodies of constant width in arbitrary dimension*, Math. Nachr. 280 (2007), 740–750, https://doi.org/10.1002/mana.200510512 (abstract inspected; full text unavailable).
