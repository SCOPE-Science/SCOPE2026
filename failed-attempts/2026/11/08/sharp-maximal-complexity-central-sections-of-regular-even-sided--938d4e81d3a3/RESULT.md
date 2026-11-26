# Sharp maximal-complexity central sections of regular even-sided prisms

## Finding
For every even integer \(n\ge4\), the probability that a Haar-uniform plane through the center of a right regular \(n\)-gonal prism cuts the maximum possible \(n+2\) vertices is
\[
 p_n(h)=\frac n\pi\left[2\arcsin\left(\frac{\sin(\pi/n)}{\sqrt{1+h^2}}\right)-\arcsin\left(\frac{\sin(2\pi/n)}{\sqrt{1+h^2}}\right)\right],
\]
when the base circumradius is one and the two bases are at heights \(\pm h\). For every even \(n\ge4\), the unique maximizing half-height is
\[
 h_n^*=\sqrt{3\cos^2(\pi/n)-1}.
\]
The sharp maximum is
\[
 p_n^*=\frac n\pi\left[2\arcsin\left(\frac{\tan(\pi/n)}{\sqrt3}\right)-\arcsin\left(\frac{2\sin(\pi/n)}{\sqrt3}\right)\right],
\]
and \(p_n^*=2\pi^2/(3\sqrt3\,n^2)+O(n^{-4})\) as even \(n\to\infty\). At \(n=4\), the optimal prism is a cube. At \(n=6\), the unique optimal full height is \(\sqrt5\) times its base radius, and the octagon probability is \(6[2\arcsin(1/3)-\arcsin(1/\sqrt3)]/\pi\approx0.122601719541\).

## Assumptions and scope
Let \(n=2m\) be even with \(m\ge2\), and \(h>0\). Define the compact, three-dimensional convex prism
\[
 K_{n,h}=\operatorname{conv}\left\{\left(\cos\frac{2\pi j}{n},\sin\frac{2\pi j}{n},\pm h\right):0\le j<n\right\}.
\]
Its base circumradius is one; the full height is \(2h\). The orientation \(U\in S^2\) has normalized rotation-invariant (Haar) distribution; the plane is \(U^\perp\), passing through the origin. Apart from a null set of planes containing a prism vertex, the intersection is a nondegenerate convex polygon whose vertices lie in relative interiors of prism edges. Denote its side count by \(N_{n,h}\). This theorem does not address random-offset planes, surface-point-chosen planes, or odd-sided prisms. All trigonometric functions use radians and standard principal real branches.

## Proof
**1. Edge-crossing enumeration and maximality.** A generic plane meets a prism edge if and only if its two endpoints have opposite signed dot products with its normal. Since the prism has \(n\) vertical edges and two cycles of \(n\) horizontal edges, no other section vertices occur. By reflection, assume \(U=(r\cos\phi,r\sin\phi,q)\) with \(r=\sqrt{1-q^2}>0\) and \(q=|U_z|>0\). Let \(t=hq/r\). The horizontal vertex dot products, divided by \(r\), are \(\cos(\phi-2\pi j/n)\); because \(n\) is even these values occur in opposite pairs. Put \(b_j=|\cos(\phi-2\pi j/n)|\), \(0\le j<m\), and assume their generic values are distinct. Let \(b_{(1)}<\cdots<b_{(m)}\) be the order statistics.

For \(t<b_{(m)}\), each of the two base faces is met in a nondegenerate segment, yielding two intersected edges from each base (four total). Exactly \(2k\) vertical edges are crossed, where \(k=\#\{j:b_j<t\}\). Thus \(N_{n,h}=4+2k\). For \(t>b_{(m)}\), both horizontal base faces are missed and every vertical edge is crossed, giving \(N_{n,h}=n\). In particular, \(N_{n,h}\le n+2\) almost surely, and \(N_{n,h}=n+2\) occurs precisely when \(b_{(m-1)}<t<b_{(m)}\).

**2. Two extreme projections.** The opposite-pair directions form a uniform grid of spacing \(2\pi/n\) modulo \(\pi\). Rotation/reflection symmetry folds the uniform azimuth into \(0<\phi<\pi/n\), with probability density \(n/\pi\) there. On this interval the largest two values of the \(b_j\) are exactly \(\cos\phi\) and \(\cos(2\pi/n-\phi)\), respectively (an endpoint tie has probability zero). Thus the maximal-complexity event is
\[
 \cos(2\pi/n-\phi)<\frac{h q}{\sqrt{1-q^2}}<\cos\phi.
\]

**3. Haar integration.** For uniform \(U\in S^2\), the variables \(q=|U_z|\) and the azimuth are independent, with \(q\) uniform on \((0,1)\). For \(b>0\),
\[
 \Pr\!\left\{\frac{h q}{\sqrt{1-q^2}}<b\right\}=\frac{b}{\sqrt{h^2+b^2}}.
\]
Consequently,
\[
 p_n(h)=\frac n\pi\int_0^{\pi/n}\left[\frac{\cos\phi}{\sqrt{h^2+\cos^2\phi}}-\frac{\cos(2\pi/n-\phi)}{\sqrt{h^2+\cos^2(2\pi/n-\phi)}}\right]d\phi.
\]
The antiderivative \(\arcsin(\sin x/\sqrt{1+h^2})\) evaluates both terms, giving the formula in the finding. All denominators are strictly positive for \(h>0\).

**4. Sharp height optimum.** Set \(a=\sin(\pi/n)>0\), \(c=\cos(\pi/n)\in[1/\sqrt2,1)\) and \(z=(1+h^2)^{-1/2}\in(0,1)\). Then
\[
 p_n(h)=\frac n\pi\bigl(2\arcsin(a z)-\arcsin(2ac z)\bigr).
\]
Its derivative with respect to \(z\) has the sign of
\[
 \frac1{\sqrt{1-a^2z^2}}-\frac{c}{\sqrt{1-4a^2c^2z^2}}.
\]
Both terms are positive. Squaring their comparison and clearing positive denominators shows that the sign is exactly the sign of \(a^2(1-3c^2z^2)\). Since \(c\ge1/\sqrt2\), the unique zero \(z^*=1/(\sqrt3c)\) lies strictly in \((0,1)\). The derivative is positive below and negative above this zero; hence \(z^*\) is the unique global maximum. Since \(z\) decreases strictly as \(h\) increases, the maximizing half-height is \(h_n^*=\sqrt{3c^2-1}\), and strict monotonicity on either side follows. The limits at \(h\downarrow0\) and \(h\to\infty\) both vanish; for the former, use \(\arcsin(\sin(2\pi/n))=2\pi/n\), valid for \(n\ge4\).

Substituting \(z^*\) yields the sharp maximum. With \(x=\pi/n\downarrow0\), the elementary series
\[
 2\arcsin(\tan x/\sqrt3)-\arcsin(2\sin x/\sqrt3)=\frac{2x^3}{3\sqrt3}+O(x^5)
\]
gives \(p_n^*=2\pi^2/(3\sqrt3\,n^2)+O(n^{-4})\). For \(n=4\), \(h_4^*=1/\sqrt2\), which exactly makes the square prism a cube. For \(n=6\), \(h_6^*=\sqrt5/2\), giving the explicit octagon probability stated above.

## Verification
The standalone file `check_even_prism.py` evaluates the closed form and an independent one-dimensional numerical integral, and counts directly the signs of plane intersections with all \(3n\) prism edges. Execute `python3 check_even_prism.py` with Python, NumPy, and SciPy. It tests five even orders and three half-heights per order, using 190,000 shared random unit directions for each of 15 configurations, i.e. 2,850,000 section classifications. Checks include the known cube probability and the exact \(n=6\) optimizer. The observed probabilities agree within stated Monte Carlo tolerances and numerical quadrature agrees to \(3\times10^{-13}\). These finite numerical checks corroborate, but are not substitutes for, the preceding proof for every even \(n\).

## Relationship to prior work
Padrol–Pfeifle (2014) concerns which polygons can be represented as sections of low-complexity polytopes, not Haar probabilities of a fixed regular prism family. Kim–Yaskin–Zvavitch (2015) studies distributions of section **areas**, not the combinatorial vertex count. De Loera–Lopez-Campos–Torres (2024) studies maximum vertex counts and possible slice counts but does not give the orientation probability or the optimum aspect ratio for all even regular prisms. An older study by Ohser–Mücklich (1995) investigates stereological size–shape distributions of random polyhedral sections by simulation; its full text was not accessible for this comparison, so historical priority in related stereological formulae is not fully resolved. The \(n=4\) cube probability is already known and is included as a consistency check, not separately claimed as original.

## Limitations
The theorem is specific to central planes and regular even-sided right prisms. It gives the exact probability of **maximal** section complexity, not all lower section-type probabilities. The asymptotic formula is for the maximizing probability as even \(n\to\infty\). No inference is made about noncentral stereological sampling, odd bases or arbitrary convex prisms. The 1995 prism-stereology source could not be inspected in full; a historical-priority risk remains. Independent validation has not been performed.

## References
1. Padrol, A., and Pfeifle, J. *Polygons as sections of higher-dimensional polytopes* (2014), arXiv:1404.2443v1, https://arxiv.org/abs/1404.2443.
2. Kim, J., Yaskin, V., and Zvavitch, A. *Distribution functions of sections and projections of convex bodies* (2015), arXiv:1512.07289v1, https://arxiv.org/html/1512.07289v1.
3. De Loera, J. A., Lopez-Campos, G., and Torres, A. J. *On the Number of Vertices in a Hyperplane Section of a Polytope* (2024), arXiv:2412.12419v1, https://arxiv.org/abs/2412.12419.
4. Ohser, J., and Mücklich, F. *Stereology for some classes of polyhedrons* (1995), Advances in Applied Probability 27, 384–396, DOI:10.2307/1427832, https://doi.org/10.2307/1427832 (abstract inspected; full text not available).
