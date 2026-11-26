# A complete normal-multiplicity phase diagram for Cassini ovals

## Finding
For the full smooth Cassini family, the oriented normal-direction multiplicity has an exact three-phase law. In the connected peanut phase the Gauss map is generically one-to-one or three-to-one on precisely identified normal-angle arcs. The fraction of triple-preimage directions is strictly decreasing and has distinct square-root and three-halves endpoint laws; total absolute curvature is determined exactly by that fraction.

Let the foci be \(\pm a\), with \(a>0\), and let \(s=b^2/a^2>0\). For \(s\ne1\), define
\[
C_s=\{z\in\mathbb C:|z^2-a^2|=a^2s\},\qquad
N:C_s\longrightarrow S^1
\]
by the outward unit normal of the region bounded by each component. For any direction \(\omega\), let \(m_s(\omega)\) be the number of distinct points in its fiber.

* If \(0<s<1\), the two components are strictly convex; \(m_s(\omega)=2\) for all directions and \(K(s)=\int_{C_s}|\kappa|\,d\ell=4\pi\).
* If \(s\ge2\), the connected curve is convex (strictly positively curved for \(s>2\)); \(m_s(\omega)=1\) for all directions and \(K(s)=2\pi\).
* If \(1<s<2\), put
\[
\phi(s)=\arccos\frac{s^2+2}{3s},\quad
\psi(s)=\arccos\sqrt{\frac{s^2-1}{3}},\quad A(s)=\psi(s)-2\phi(s).
\]
Then \(0<A(s)<\pi/2\). The two open normal-direction arcs of half-width \(A(s)/2\) centered at the angles \(\pi/2\) and \(3\pi/2\) have three preimages. Each of their four endpoints has two preimages; directions outside the closed arcs have one preimage. The normalized angular measure of the open arcs and the total absolute curvature are
\[
p_3(s)=\frac{A(s)}{\pi},\qquad K(s)=2\pi+4A(s).
\]
The quantity \(A\) is strictly decreasing, with
\[
A'(s)=-\frac{\sqrt{4-s^2}}{s\sqrt{s^2-1}}.
\]
Consequently, the fraction of oriented normals with three preimages determines the similarity parameter uniquely within the peanut phase. Its endpoint asymptotics are
\[
\begin{aligned}
p_3(s)&=\frac12-\frac{\sqrt6}{\pi}\sqrt{s-1}+O((s-1)^{3/2}) &&(s\downarrow1),\\
p_3(s)&=\frac{2}{3\pi\sqrt3}(2-s)^{3/2}+O((2-s)^{5/2}) &&(s\uparrow2).
\end{aligned}
\]

## Assumptions and scope
The Euclidean metric and standard outward orientation are used. The parameter \(s=b^2/a^2\), rather than the commonly quoted focus ratio \(b/a\), is dimensionless. Similarities leave the normal count and integrated absolute curvature unchanged. The singular Bernoulli lemniscate \(s=1\) is excluded because its central double point has no unique regular normal. The nearly circular limit \(s\to\infty\) is included through the convex phase. The normal map counts points on the *boundary* with a prescribed oriented outward normal, not normal lines passing through an independently chosen point in the plane.

## Proof
Scale \(a\) to one. The inverse image of the complex circle \(1+s e^{it}\) under the square map parametrizes the Cassini curve:
\[
z(t)=\sqrt{1+s e^{it}}.
\]
For \(s>1\), take a continuously continued square root over \(0\le t\le4\pi\); this traces the connected oval once counterclockwise. For \(0<s<1\), the two single-valued branches \(\pm\sqrt{1+s e^{it}}\), each over \(0\le t\le2\pi\), trace the two components once.

Direct differentiation gives \(z'(t)=is e^{it}/(2z(t))\) after normalization. If \(\theta(t)=\arg z'(t)\) is a continuous tangent-angle lift, then
\[
\theta(t)=t+\frac\pi2-\frac12\arg(1+s e^{it}),\qquad
\theta'(t)=\frac{s^2+2+3s\cos t}{2(1+s^2+2s\cos t)}.
\]
The same derivative holds for the oriented outward-normal angle, which differs from \(\theta\) by a constant. Because \(d\ell=|z'(t)|dt\), \(\int|\kappa|\,d\ell=\int|\theta'(t)|dt\). An independent differentiation gives signed curvature
\[
\kappa(t)=\frac{s^2+2+3s\cos t}{a s(1+s^2+2s\cos t)^{3/4}}.
\]
For \(0<s<1\), the numerator is at least \((s-1)(s-2)>0\). Each closed component has one full positive turn, so its normal is bijective and its absolute curvature integral is \(2\pi\). For \(s\ge2\), the numerator is nonnegative and vanishes only at isolated points when \(s=2\); the connected curve has one full turn and strictly increasing normal angle except at those isolated stationary parameters. This proves both endpoint phases, including uniqueness at \(s=2\).

For \(1<s<2\), the only negative-turn intervals on \(0\le t<4\pi\) are \((\pi-\phi,\pi+\phi)\) and its translate by \(2\pi\), where \(\cos\phi=(s^2+2)/(3s)\). Choose the branch starting at \(z(0)>0\) and the argument lift starting at zero. At the endpoints \(t=\pi-\phi,\pi+\phi\), respectively, \(1+s e^{it}\) has real part \(-(s^2-1)/3\) and imaginary parts \(\pm\sqrt{(s^2-1)(4-s^2)}/3\). Since its modulus there is \(\sqrt{(s^2-1)/3}\), its lifted arguments are \(\pi-\psi\) and \(\pi+\psi\). The outward-normal angle \(t-\tfrac12\arg(1+s e^{it})\) at these endpoints is \(\pi/2+A/2\) and \(\pi/2-A/2\), respectively. The drop \(A=\psi-2\phi\) is positive because the derivative is strictly negative between the endpoints, and \(A<\psi<\pi/2\). The translation by \(2\pi\) shifts the outward-normal angle by \(\pi\), giving the disjoint antipodal arc.

Away from the four critical values the normal-angle map has degree one: the number of positive-orientation preimages minus the number of negative-orientation preimages equals one. The latter number is one on the two backward-turn arcs and zero outside their closures, proving the regular multiplicities. Each stationary point at an arc endpoint is a simple fold: the numerator of \(\theta'\) has nonzero derivative there. The four critical values are distinct, so near an endpoint only this fold changes the local count: it contributes two points on the triple side, zero on the single side, and one at the endpoint. The other preimages are regular and persist locally, by compactness and the inverse function theorem. There is exactly one such preimage, as seen on the single side; the endpoint thus has two distinct preimages. The signed total turn is \(2\pi\), and the sum of the negative turns is \(-2A\). Replacing negative increments by their magnitudes adds \(4A\) to the total, giving \(K=2\pi+4A\).

Differentiating the inverse-cosine expression and simplifying yields \(A'=-\sqrt{4-s^2}/(s\sqrt{s^2-1})\). This is strictly negative for \(1<s<2\), with endpoint limits \(A(1+)=\pi/2\) and \(A(2-)=0\). As \(s\downarrow1\), \(-A'\sim\sqrt{3/2}(s-1)^{-1/2}\), giving \(A=\pi/2-\sqrt6\sqrt{s-1}+O((s-1)^{3/2})\). As \(s\uparrow2\), \(-A'\sim(2-s)^{1/2}/\sqrt3\), giving \(A=2(2-s)^{3/2}/(3\sqrt3)+O((2-s)^{5/2})\). Divide by \(\pi\) for the stated asymptotics of \(p_3\).

## Verification
Run the standalone Python 3 standard-library script `geometry_cassini_normal_check.py` using `python3 geometry_cassini_normal_check.py`. It evaluates the curvature in two algebraically independent ways (complex derivatives and the explicit curvature formula), compares numerical total absolute turning with exact integrals across both disconnected and connected phases, independently counts preimages over uniform finite grids of normal directions for four concave shape parameters, and tests both critical exponents. The executed script passed **745 deterministic assertions**. The finite discretizations are checks only: they neither prove the all-parameter assertions nor establish originality, which rest on the analytic argument and literature comparisons, respectively.

## Relationship to prior work
The classical Cassini-oval topology and convexity transition at \(b/a=\sqrt2\) are known, not claimed here. The Mathcurve Cassinian oval entry also records curvature radius and the inflection locus; the present calculation evaluates the angular images of the backward-turn intervals and the two endpoint asymptotics. Boyadzhiev and Boyadzhiev (arXiv:1303.5876) study Cassini ovals from planar harmonic-oscillator foci. Rabinowitz's 2025 geometry survey gives Cassini constructions and classical shape transitions. Lawden (1999) studies orthogonal trajectories. The term *normal multiplicity* is deliberately distinguished from the number of normals through an arbitrary interior point of a different curve such as an ellipse.

## Limitations
The statement covers the explicit Euclidean two-focus Cassini family only, excluding its singular lemniscate at \(s=1\). These results do not classify normal lines through arbitrary interior points or normals of more general polynomial lemniscates. Historical priority is provisional: the literature comparison is not exhaustive.

## References
1. K. N. Boyadzhiev and I. A. Boyadzhiev, *Harmonic motion and Cassini ovals*, initial arXiv submission 2013-03-23, https://arxiv.org/abs/1303.5876 ; accessible journal full text https://www.researchgate.net/publication/258818264_Harmonic_motion_and_Cassini_ovals .
2. S. Rabinowitz, *Geometric Properties of a Cassini Oval*, International Journal of Computer Discovered Mathematics 10 (2025), 325–348, https://www.researchgate.net/publication/395098992_Geometric_Properties_of_a_Cassini_Oval .
3. D. F. Lawden, *Families of ovals and their orthogonal trajectories*, Mathematical Gazette 83 (1999), 410–420, https://doi.org/10.2307/3620950 (abstract only available for this comparison).
4. A. Hirst and K. Lloyd, *Cassini, his ovals and a space probe to Saturn*, Mathematical Gazette 81 (1997), 409–421, https://doi.org/10.2307/3619618 (historical source, complete text not inspected).
5. R. Ferréol, *Cassinian oval*, Mathcurve, https://mathcurve.com/courbes2d.gb/cassini/cassini.shtml (curvature radius and inflection locus).
