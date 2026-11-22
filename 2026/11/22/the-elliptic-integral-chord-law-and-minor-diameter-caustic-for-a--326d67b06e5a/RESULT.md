# The elliptic-integral chord law and minor-diameter caustic for affine-uniform ellipse endpoints

## Finding
Let \(a>b>0\) and sample \(T,U\) independently and uniformly from \([0,2\pi)\). On the ellipse \(X(t)=(a\cos t,b\sin t)\), let \(L=\|X(T)-X(U)\|_2\), and put \(\Delta=a^2-b^2\), \(x=\ell/2\). Write \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\) for the complete elliptic integral of the first kind. The density of \(L\), supported on \((0,2a)\), is precisely
\[
f_L(\ell)=\begin{cases}
\dfrac{2}{\pi^2\sqrt{a^2-x^2}}\,K\!\left(\sqrt{\dfrac{\Delta}{a^2-x^2}}\right),&0<\ell<2b,\\[7pt]
\dfrac{2}{\pi^2\sqrt\Delta}\,K\!\left(\sqrt{\dfrac{a^2-x^2}{\Delta}}\right),&2b<\ell<2a.
\end{cases}
\]
It has exactly one interior singularity: the logarithmic caustic at the minor-axis diameter \(\ell=2b\), with the **full leading logarithmic constant**
\[
f_L(\ell)=\frac{1}{\pi^2\sqrt\Delta}\log\frac{16\Delta}{b|\ell-2b|}+o(1),\qquad \ell\to2b^\pm.
\]
The outer endpoint values are finite and positive:
\[
f_L(0+)=\frac{2}{\pi^2 a}K\left(\frac{\sqrt\Delta}{a}\right),\quad f_L(2a-)=\frac{1}{\pi\sqrt\Delta};\qquad
\Pr(L>2a-\eta)=\frac{\eta}{\pi\sqrt\Delta}+o(\eta).
\]
Moreover, writing \(m_2=\mathbb E L^2\) and \(m_4=\mathbb E L^4\), the two moments recover the entire ellipse, including scale, up to rigid motion:
\[
m_2=a^2+b^2,\quad m_4=\frac94(a^4+b^4)+\frac32 a^2b^2,\quad
\Delta=\sqrt{\frac43m_4-2m_2^2},\quad
a=\sqrt{\frac{m_2+\Delta}{2}},\quad b=\sqrt{\frac{m_2-\Delta}{2}}.
\]
A single continuous scalar moment cannot recover both positive axes even locally on the open two-parameter family, whereas these two specific natural moments do. At the circle limit \(a=b=r\), the density becomes \(2/(\pi\sqrt{4r^2-\ell^2})\); the interior caustic merges with the upper endpoint and its density singularity changes form.

## Assumptions and scope
The sampling law is uniform in **eccentric anomaly**, i.e. the push-forward of uniform circular parameter under the affine map \((\cos t,\sin t)\mapsto(a\cos t,b\sin t)\). It is not uniform in Euclidean arclength, not area-uniform in the filled ellipse, and not the motion-invariant random-line chord law. Endpoints are independent. The main piecewise formula assumes a noncircular ellipse, \(a>b>0\); the circle is separately specified. All density identities hold away from the singular diameter, and the density at that single point is immaterial to the distribution.

## Proof
**Independent chord-factor representation.** Difference-of-trigonometric-functions identities give
\[
L=2\left|\sin\frac{T-U}{2}\right|\left(a^2\sin^2\frac{T+U}{2}+b^2\cos^2\frac{T+U}{2}\right)^{1/2}=2SR.
\]
The map \((T,U)\mapsto(T-U,T+U)\) on the two-torus is a surjective integer homomorphism, so it sends Haar probability to Haar probability. Its output coordinates are independent uniform angles modulo \(2\pi\), hence \(S\) and \(R\) are independent. Their densities are
\[
f_S(s)=\frac{2}{\pi\sqrt{1-s^2}}\;(0<s<1),\qquad
f_R(r)=\frac{2r}{\pi\sqrt{(r^2-b^2)(a^2-r^2)}}\;(b<r<a).
\]
Condition on \(R=r\). Since \(L=2rS\), its conditional density is \(1/(\pi\sqrt{r^2-\ell^2/4})\) for \(0<\ell<2r\). Thus the exact mixture is
\[
f_L(\ell)=\frac2{\pi^2}\int_{\max\{b,\ell/2\}}^a
\frac{r\,dr}{\sqrt{(r^2-b^2)(a^2-r^2)(r^2-\ell^2/4)}}.
\]
For \(x=\ell/2<b\), use \(r^2=b^2+\Delta\sin^2\theta\) to obtain the first elliptic-integral branch. For \(b<x<a\), use \(r^2=x^2+(a^2-x^2)\sin^2\theta\) to obtain the second. These substitutions also establish normalization, since the mixture of normalized conditional densities is normalized.

**Singular and extreme behavior.** For modulus \(k\uparrow1\), the standard expansion \(K(k)=\log(4/\sqrt{1-k^2})+O((1-k^2)|\log(1-k^2)|)\) applies. In the first branch, \(1-k^2=(b^2-x^2)/(a^2-x^2)\); in the second, \(1-k^2=(x^2-b^2)/\Delta\). Since \(|x^2-b^2|=b|\ell-2b|+O((\ell-2b)^2)\), both yield the same displayed logarithmic expansion, including the factor \(16\Delta/b\). Apart from \(2b\), both branches have modulus strictly below one and are finite and continuous. Taking \(\ell\downarrow0\) and \(\ell\uparrow2a\), using \(K(0)=\pi/2\), gives their finite limits and the upper-tail linear law.

**Moments and inverse.** The independent factors satisfy \(\mathbb E S^2=1/2\), \(\mathbb E S^4=3/8\), \(\mathbb E R^2=(a^2+b^2)/2\), and \(\mathbb E R^4=3(a^4+b^4)/8+a^2b^2/4\). Substituting into \(L=2SR\) proves the formulas for \(m_2,m_4\). Elimination gives \(4m_4/3-2m_2^2=(a^2-b^2)^2\), yielding the unique ordered positive axes. Finally, on the circle \(R=r\) deterministically, so \(L=2rS\) and the stated arcsine density follows. One continuous moment map from an open region of \(\mathbb R^2\) into \(\mathbb R\) cannot be injective by dimension (and concretely \(m_2=a^2+b^2\) has one-dimensional level sets).

## Verification
Run the included standalone checker as `python3 verify_ellipse_chords.py` using the Python standard library. It checks three axis pairs: independently integrated density normalization, second and fourth moments, inversion, the two-sided logarithmic constant, 3,600 pointwise chord factorizations, and an independent seeded Monte Carlo sample of 220,000 chords. The reported marker is `ELLIPSE_END_POINT_CHORD_DENSITY_CHECKS_OK`. Computation tests the formulas but does not replace the analytic proof.

## Relationship to prior work
Classical chord distributions depend on the sampling convention. Gečiauskas (1966) considers distances of random **interior** points of an oval; Gečiauskas (1967) discusses random-ray and random-line chord models. Neither gives this independent, uniformly eccentric-anomaly endpoint distribution. Schrempp (2015) studies extremes of distances among numerous **interior** ellipse points. Bäsel (2014) studies chord distributions in regular polygons, not ellipses. Relevant published ellipse-boundary work on arclength-uniform near-diametral distances concerns a different measure, so its asymptotics do not imply the present full law. The new object is distinguished by the independent arcsine product, the interior logarithmic caustic and the exact two-moment inversion. Absence of matching published material in a bounded search is not proof of absolute historical priority.

## Limitations
This is a one-chord law for two independent points sampled by eccentric anomaly on a nondegenerate ellipse; it does not give the law under boundary-arclength, interior, or invariant-line sampling. It does not classify chord distributions for general ovals, nor establish publication priority against all classical sources. The density diverges at \(2b\), but is integrable and does not create an atom. No independent mathematical audit has been performed.

## References
- E. Gečiauskas, “Distribution function of a distance between two random points in an oval,” *Lithuanian Mathematical Journal* 6 (1966), 245–248, https://doi.org/10.15388/LMJ.1966.19722 (interior-point distribution).
- E. Gečiauskas, “The distribution function of the chord length of oval and ovaloid,” *Lithuanian Mathematical Journal* (1967), https://www.zurnalai.vu.lt/LMJ/article/view/19983 (alternative random-chord models).
- M. Schrempp, “The limit distribution of the largest interpoint distance for distributions supported by an ellipse and generalizations,” arXiv:1505.01597 (2015), https://arxiv.org/abs/1505.01597 (interior-point extreme-value sampling).
- U. Bäsel, “Random chords and point distances in regular polygons,” *Acta Mathematica Universitatis Comenianae* (2014), https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/71 (contrasting geometric chord models).
