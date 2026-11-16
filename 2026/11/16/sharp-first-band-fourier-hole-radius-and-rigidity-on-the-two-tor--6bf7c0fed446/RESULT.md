# Sharp first-band Fourier hole radius and rigidity on the two-torus

## Finding
Let \(\mu\) be any positive Borel probability measure on \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\) with vanishing nonconstant Fourier moments throughout the first rectangular band:
\[
\widehat\mu(k,\ell)=\int_{\mathbb T^2}e^{-2\pi i(kx+\ell y)}\,d\mu(x,y)=0
\quad ((k,\ell)\in\{-1,0,1\}^2\setminus\{(0,0)\}).
\]
For the wrap-around supremum metric \(d_\infty\), define the covering radius of its support by
\[
\delta(\mu)=\max_{u\in\mathbb T^2}\min_{z\in\operatorname{supp}\mu}d_\infty(u,z).
\]
Then, with \(r_*=(2\pi)^{-1}\arccos(-1/3)=0.3040867239846964\ldots\),
\[
\boxed{\delta(\mu)\le r_*}.
\]
Equality holds **if and only if**, for some translation \(u\in\mathbb T^2\), \(\mu\) is the translate by \(u\) of the following unique five-point measure:
\[
\boxed{
\mu_* =\frac14\delta_{(1/2,1/2)}+
 \frac{3}{16}\bigl(\delta_{(r_*,0)}+\delta_{(-r_*,0)}+
                    \delta_{(0,r_*)}+\delta_{(0,-r_*)}\bigr).}
\]
The support of \(\mu_*\) has covering radius exactly \(r_*\); its centered open square of side \(2r_*\) contains no support point. The rigidity conclusion does not require \(\mu\) to have finitely many atoms or an a priori bound on its support size.

## Assumptions and scope
The torus is represented by \([-1/2,1/2]^2\) with opposite sides identified. For \(t\in\mathbb T\), let \(d_\mathbb T(t,0)=\min_{j\in\mathbb Z}|t-j|\), and let \(d_\infty((x,y),(a,b))=\max\{d_\mathbb T(x,a),d_\mathbb T(y,b)\}\). All measures are positive, have total mass one, and are regular Borel measures. Compactness makes the minimum and maximum in the definition of \(\delta\) attained. Fourier exactness at the nine first-band frequencies, including the constant, is exactly the condition of positive quadrature for the rectangular first-frequency trigonometric space.

The assertion concerns the maximal **empty square**, not Euclidean covering distance, minimal cubature node count, or the higher-degree rectangular Fourier bands. Positivity is essential to the support rigidity argument.

## Proof
**1. A sharp sign-localized first-band witness.** Set \(X=\cos(2\pi x)\) and \(Y=\cos(2\pi y)\). Consider
\[
H(x,y)=XY+\tfrac12(X+Y)
 =\tfrac12\bigl[\cos(2\pi(x+y))+\cos(2\pi(x-y))+
                        \cos(2\pi x)+\cos(2\pi y)\bigr].
\]
Every frequency of \(H\) is nonzero and belongs to the first rectangular band. Therefore \(\int H\,d\mu=0\).

Write \(c=-1/3=\cos(2\pi r_*)\). A torus point lies outside the centered open \(d_\infty\)-square of radius \(r_*\) precisely when \(X\le c\) or \(Y\le c\). We claim that
\[
H\le0\quad\text{on }\{X\le c\}\cup\{Y\le c\},
\]
and equality occurs there exactly for the three cosine pairs
\[
(X,Y)=(-1,-1),\quad(c,1),\quad(1,c).
\]
Indeed, for \(-1\le X\le-1/2\), \(H=(X+1/2)Y+X/2\) decreases in \(Y\), so its maximum on \([-1,1]\) equals \(H(X,-1)=-(X+1)/2\le0\), with equality exactly at \(X=-1,Y=-1\). For \(-1/2\le X\le c\), it increases in \(Y\), so its maximum is \(H(X,1)=(3X+1)/2\le0\), with equality precisely at \(X=c,Y=1\). The symmetric argument applies when \(Y\le c\). This establishes both the sign and the complete equality set.

**2. Rigidity at an extremal hole.** Suppose \(\delta(\mu)\ge r_*\). Take a center realizing that covering radius and translate it to \((0,0)\). Every point in the support then satisfies \(X\le c\) or \(Y\le c\). By step 1, \(H\le0\) on that support, yet its \(\mu\)-integral is zero. Positivity and continuity force \(H=0\) throughout the support. The support is therefore contained in the five sites
\[
(1/2,1/2),\ (r_*,0),\ (-r_*,0),\ (0,r_*),\ (0,-r_*).
\]
Write \(a\) for the first site's mass, \(b_+,b_-\) for the next two, and \(c_+,c_-\) for the last two; allow zero masses initially. Since \(\sin(2\pi r_*)=2\sqrt2/3\ne0\), the vanishing sine moments imply \(b_+=b_-\) and \(c_+=c_-\). Let \(b=b_++b_-\), \(c'=c_++c_-\). The constant and the two cosine moments give
\[
a+b+c'=1,\qquad -a-\tfrac13 b+c'=0,\qquad
-a+b-\tfrac13 c'=0.
\]
Subtracting yields \(b=c'\), and then \(a=2b/3\). Hence \(a=1/4\), \(b=c'=3/8\), and all four side-node weights are \(3/16\). Thus \(\mu\) must equal the displayed translate of \(\mu_*\).

**3. Exactness and attainment.** For \(\mu_*\), reflection in each coordinate eliminates all first-band sine-containing moments. Its two single-coordinate cosine moments are both
\[
-\tfrac14-\tfrac13\cdot\tfrac38+\tfrac38=0,
\]
and its mixed cosine moment is
\[
\tfrac14-\tfrac13\bigl(\tfrac38+\tfrac38\bigr)=0.
\]
Together with mass one, these are exactly all nine rectangular first-band moment equations. Every side node is at \(d_\infty\)-distance \(r_*\) from the origin, while the corner is at distance \(1/2\), so \(\delta(\mu_*)\ge r_*\).

Finally, if any admissible \(\mu\) had \(\delta(\mu)>r_*\), step 2 would force it to be a translate of \(\mu_*\) centered at its deepest hole. But that hole's nearest side node would then be exactly \(r_*\) away, a contradiction. Hence \(\delta(\mu)\le r_*\) universally. The explicit measure attains the bound, and step 2 proves all equality cases.

## Verification
The accompanying dependency-free `CHECK.py` uses exact rational arithmetic in \(\mathbb Q(i\sqrt2)\) to evaluate all nine complex Fourier moments of the proposed five-node measure, its total mass, its zero-contact identities, and the endpoint inequalities underlying the sign certificate. It passed all 29 assertions at construction. This finite arithmetic verification confirms the explicit coefficient identities, but the universal result and full equality classification follow from the analytical sign-and-support proof above, not a search over measures.

## Relationship to prior work
Kunis (2026) studies positive quadrature for multivariate trigonometric polynomial spaces, obtaining general covering-radius bounds through sign-localized test polynomials; the relevant theorem is not a sharp degree-one two-torus equality classification. The present result solves precisely that natural first rectangular band, with an extremal contact polynomial and a unique five-atom extremizer. Noskov and Schmid (2002) study minimal *node counts* for even-total-degree trigonometric cubature on the two-torus. Their exactness space includes pure second frequencies not required here; neither their node-count bounds nor their example formulae imply the sharp empty-square radius or rigidity above.

The Fourier-moment and covering formulations are equivalent under positive quadrature for the first rectangular band. The result is not claimed to be a statement about higher bands, arbitrary signed measures, or optimal Euclidean-radius designs. An older equivalent result using moment-polytopes or cubature terminology cannot be categorically excluded by literature search alone.

## Limitations
The theorem determines only the exact first rectangular band in dimension two and wrap-around supremum covering radius. It does not determine an optimal radius for higher frequencies, nonrectangular bands, or other metrics. It does not claim minimality of five nodes among all first-band rules; it asserts five-node *rigidity among maximal-hole rules*. The proof has been checked in the same analytical setting, without independent expert review. Publication priority remains provisional, particularly against older cubature and trigonometric-moment literature.

## References
1. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, first public version August 12, 2026. https://arxiv.org/abs/2608.11915 . Relevant: Introduction, Theorem 3.3, Remark 3.4 and §4.
2. M. V. Noskov and H. J. Schmid, *Minimal cubature formulae of an even degree for the 2-torus*, Siberian Journal of Numerical Mathematics 5 (2002), 267–274. https://www.mathnet.ru/eng/sjvm254 . Relevant: definitions of total-degree exactness and minimal cubature formulae.
