# A sharp sampling-exponent reversal for acute triangles on nearly circular ellipses

## Finding

Let \(-1<q<1\) and consider the ellipse parametrization
\[
X_q(t)=(\sqrt{1+q}\cos t,\sqrt{1-q}\sin t),\qquad 0\le t<2\pi.
\]
For every fixed real \(\alpha\), take three independent parameters with density
\[
 f_{q,\alpha}(t)=\frac{(1-q\cos 2t)^{\alpha/2}}{\int_0^{2\pi}(1-q\cos 2v)^{\alpha/2}\,dv},
\]
and let \(P_\alpha(q)\) be the probability that the corresponding Euclidean triangle is strictly acute. Then, as \(q\to0\) with \(\alpha\) fixed,
\[
\boxed{P_\alpha(q)=\frac14-\frac{3(1-\alpha)}{2\pi^2}q^2+O_\alpha(q^4).}
\]
The coefficient is exact. Consequently the circle is a strict local maximum of this acuteness probability for every \(\alpha<1\), a strict local minimum for every \(\alpha>1\), and has vanishing quadratic response for the unique exponent \(\alpha=1\). For \(\alpha=1\), the density is precisely uniform Euclidean arclength; \(\alpha=0\) is uniform eccentric angle. The theorem asserts no sign for the quartic term at \(\alpha=1\).

## Assumptions and scope

Acuteness refers to ordinary Euclidean angles, not angles in an affine metric. Any fixed \(\alpha\in\mathbb R\) is permitted, and the expansion is local at \(q=0\) with its remainder allowed to depend on that fixed exponent. For \(|q|<1\) all parameter densities are strictly positive and smooth. The arcs are full ellipses, not proper subarcs. Degenerate or right triangles have probability zero. The parameter \(q=(a^2-b^2)/(a^2+b^2)\) describes anisotropy after a common similarity, so exchanging axes replaces \(q\) by \(-q\).

## Proof

**1. Reduction to a single obtuse vertex.** At a designated vertex with eccentric angle \(t\), write the other two angles as \(t+2s\), \(t+2r\) modulo \(2\pi\), with \(s,r\in(0,\pi)\). The chord factorization
\[
X_q(t+2s)-X_q(t)=2\sin s\,(-\sqrt{1+q}\sin(t+s),\sqrt{1-q}\cos(t+s))
\]
shows that the angle at the designated vertex is obtuse exactly on
\[
B_q=\{(t,s,r):\cos(s-r)-q\cos(2t+s+r)<0\}.
\]
Write \(B_0=\{|s-r|>\pi/2\}\). A nondegenerate Euclidean triangle has at most one obtuse vertex. Exchangeability therefore gives \(P_\alpha(q)=1-3Q_\alpha(q)\), where
\[
Q_\alpha(q)=\int_0^{2\pi}\!\int_0^\pi\!\int_0^\pi
 f_{q,\alpha}(t)\,2f_{q,\alpha}(t+2s)\,2f_{q,\alpha}(t+2r)
\,\boldsymbol 1_{B_q}\,dr\,ds\,dt.
\]
Here \(Q_\alpha\) is the probability of an obtuse angle at one fixed label.

**2. The uniform-angle geometric contribution.** At \(\alpha=0\), the phase \(2t+s+r\) is uniform modulo \(2\pi\) independently of the triangular difference \(s-r\). Integrating over the phase, or expanding the elementary arcsine-square integral, yields
\[
 Q_0(q)=\frac14+\frac{1}{2\pi^2}\operatorname{Li}_2(q^2)
 =\frac14+\frac{q^2}{2\pi^2}+O(q^4),
\]
where \(\operatorname{Li}_2(z)=\sum_{j\ge1}z^j/j^2\). For completeness, the phase average leads to
\[
Q_0(q)=\frac14+\frac{1}{2\pi^3}\int_0^{2\pi}\arcsin^2(q\cos v)\,dv;
\]
then \(\arcsin^2 z=\frac12\sum_{j\ge1}4^j z^{2j}/(j^2\binom{2j}{j})\) and the usual even-cosine integral prove the displayed dilogarithm identity.

**3. Expansion of the sampling density.** Uniformly in the parameter angle,
\[
2\pi f_{q,\alpha}(t)
=1-\frac\alpha2 q\cos2t
+\frac{\alpha(\alpha-2)}{16}q^2\cos4t+O_\alpha(q^3).
\]
The product of the three normalized density factors therefore has first coefficient
\[
W_1=-\frac\alpha2\bigl(\cos2t+\cos(2t+4s)+\cos(2t+4r)\bigr).
\]
Its second coefficient is a sum of three single-angle fourth harmonics, which vanish on averaging over the common rotation, and the pair part
\[
\frac{\alpha^2}{4}\sum_{i<j}\cos2t_i\cos2t_j.
\]
Averaging this pair part over common rotation leaves
\[
\frac{\alpha^2}{8}\bigl(\cos4s+\cos4r+\cos4(s-r)\bigr).
\]
Each term has integral zero over \(B_0\) in the square \((0,\pi)^2\). Indeed the first two follow by reducing to \(\int_0^\pi|s-\pi/2|\cos4s\,ds=0\), and the last to \(2\int_{\pi/2}^\pi(\pi-d)\cos4d\,dd=0\).

**4. Mixed boundary contribution.** The first displacement of the obtuse indicator is the distributional identity
\[
\left.\frac{d}{dq}\boldsymbol1_{B_q}\right|_{q=0}
=\cos(2t+s+r)\,\delta(\cos(s-r)).
\]
This identity can equivalently be obtained by differentiating the unique moving right-angle boundary on each half of the parameter square; hence no probabilistic delta-function assumption is required. Averaging \(W_1\cos(2t+s+r)\) over the common angle \(t\) gives
\[
-\frac\alpha4\cos(s+r)\bigl(1+2\cos2(s-r)\bigr).
\]
On either boundary \(s-r=\pm\pi/2\), it equals \(\alpha\cos(s+r)/4\). The two resulting segment integrals of \(\cos(s+r)\) are both \(-1\); thus the mixed term contributes exactly \(-\alpha/(2\pi^2)\) to the coefficient of \(q^2\) in \(Q_\alpha\). Combining with step 2 and the zero pure-density contribution in step 3 gives
\[
Q_\alpha(q)=\frac14+\frac{1-\alpha}{2\pi^2}q^2+o(q^2).
\]
The probability is an even analytic function of \(q\) near zero: the density is analytic for \(|q|<1\), the right-angle boundary has a unique nonvanishing normal derivative and analytic endpoints after splitting the parameter square, and rotating the ellipse by \(\pi/2\) changes \(q\) to \(-q\) without changing the probability. Therefore \(o(q^2)\) strengthens to \(O_\alpha(q^4)\). Substitution into \(P_\alpha=1-3Q_\alpha\) proves the claim and all strict local sign conclusions for \(\alpha\ne1\).

## Verification

Run `python checker.py` with Python 3.11 or newer, NumPy and SciPy. The checker independently verifies Euclidean chord-dot signs and uses a fixed-domain two-dimensional Gaussian quadrature with an elliptic right-angle boundary to evaluate the probability for several positive and negative anisotropies and sampling exponents. It compares these values with the theorem to fourth-order tolerance, tests axis-exchange symmetry and tests the exact circular probability. These finite numerical checks corroborate, but do not replace, the preceding analytic proof. The checker does not certify a quartic coefficient or any global aspect-ratio ordering.

## Relationship to prior work

Edelman and Strang's *Random Triangle Theory with Geometry and Applications* (arXiv:1501.03053, originally posted 2015-01-09) gives the classical random-triangle framework and highlights the dependence of the acute probability on sampling models. The later exact affine-uniform ellipse law (published-finding corpus, 2026-10-25 and 2026-11-02) is the \(\alpha=0\) case above; its full dilogarithm formula is expressly acknowledged as prior work. The public 2025 calculation of arclength-uniform ellipse acuteness gives a triple-integral expression for the \(\alpha=1\) case, without evaluating its near-circle quadratic response. The present claim is the new exact coefficient for the complete speed-power family and the unique reversal threshold at Euclidean arclength, not a new formula at \(\alpha=0\), not a full distribution, and not an evaluation of the 2025 integral at arbitrary anisotropy.

## Limitations

The result is local in the ellipse eccentricity and fixed in the exponent. It does not assert global monotonicity in anisotropy. In particular, zero quadratic response at \(\alpha=1\) does not imply exact constancy or a proved fourth-order sign. A publicly posted integral for the arclength case could, after additional differentiation, imply the isolated cancellation; novelty is claimed for the explicit power-family response and its sign reversal, subject to independent historical-priority assessment. Independent mathematical validation has not been performed.

## References

1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053v1, first posted 2015-01-09, https://arxiv.org/abs/1501.03053 .
2. *Probability that Triangle on Ellipse is Acute*, Mathematics Stack Exchange question 5014676 (asked 2024-12-22), with C. Boilley's arclength-integral answer dated 2025-01-24, https://math.stackexchange.com/questions/5014676/probability-that-triangle-on-ellipse-is-acute .
3. *Dilogarithmic acuteness law for uniform-angle triangles on an ellipse*, publicly accessible result dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-dilogarithmic-acuteness-law-for-uniform-angle-triangles-on-an-el--72d4f16967d8 .
4. *Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles*, publicly accessible result dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-dilogarithmic-acuteness-law-for-affine-uniform-ellipse-tri--a5911e351b92 .
