# Simple affine ramification and a cuspidal dual infinity for coprime Chebyshev curves

## Finding

Let \(2\le a<b\) be coprime integers. Over \(\mathbb C\), let \(C_{a,b}\subset\mathbb P^2\) be the projective closure of \(T_b(x)-T_a(y)=0\), where \(T_m(\cos\theta)=\cos(m\theta)\). In coordinates \([Z:X:Y]\) its normalization is \(t\mapsto[1:T_a(t):T_b(t)]\). Then:

1. The projective dual has degree \(a+b-1\).
2. The ramification divisor of the linear series \(\langle1,T_a,T_b\rangle\subset H^0(\mathbb P^1,\mathcal O(b))\) has \(a+b-3\) distinct simple finite points, namely the roots of \(W=T_a'T_b''-T_b'T_a''\), and weight \(2b-a-3\) at \(t=\infty\).
3. The dual point representing the original tangent at \(t=\infty\) has exactly one analytic branch, with Puiseux pair \((a,b)\) and delta invariant \((a-1)(b-1)/2\). Every finite root of \(W\) gives an ordinary cuspidal **branch** of the dual; distinct parameters need not give distinct points.

Ramification here means the Wronskian divisor of the hyperplane linear series on the normalization, not the branch divisor of the normalization map. The dual is the closure of tangents to smooth points of the curve.

## Proof

**Normalization.** In homogeneous coordinates \([u:v]\) on \(\mathbb P^1\), write \(T_m^h=v^mT_m(u/v)\). The map \([v^b:v^{b-a}T_a^h:T_b^h]\) is base-point-free. If its degree onto its image is \(d\), then \(d\) divides both \(a\) and \(b\) by the degrees of the two affine coordinate functions; thus \(d=1\). Its image has degree \(b\) by pullback of a line. The identity \(T_b\circ T_a=T_a\circ T_b\) places the image in the projective degree-\(b\) equation in the statement, so the image is that curve. Write \(P=T_a'\) and \(Q=T_b'\). The roots of \(T_m'\) are the simple roots \(\cos(k\pi/m)\), \(1\le k<m\), by differentiating the defining cosine identity. No root is shared by \(P\) and \(Q\): cosine is injective on \((0,\pi)\), and \(k/a=\ell/b\) would contradict coprimality for these internal indices. Thus the normalization is immersed at all finite parameters.

**Dual degree.** Its tangent line map is
\[
\gamma(t)=[P(t)T_b(t)-Q(t)T_a(t):Q(t):-P(t)].
\]
In fact, these coefficients annihilate the point \([1:T_a:T_b]\) and the velocity \([0:P:Q]\). Since \(T_m\) has leading coefficient \(2^{m-1}\), the first coordinate has degree \(a+b-1\) and leading coefficient
\[
(a-b)2^{a+b-2}\ne0.
\]
The other coordinates have degrees \(b-1,a-1\). There is no common zero at finite parameters by derivative coprimality, and none after homogenization at infinity because the first coordinate has full degree. Therefore \(\gamma^*\mathcal O(1)\) has degree \(a+b-1\). Characteristic-zero biduality makes the tangent map generically one-to-one: at a generic smooth dual point the tangent to the dual recovers the original smooth point. It follows that the dual curve has degree \(a+b-1\), and \(\gamma\) from \(\mathbb P^1\) is its normalization.

**Simple finite Wronskian roots.** The affine Wronskian of the three sections is \(W=P Q'-Q P'\). Its leading coefficient is \(ab(b-a)2^{a+b-2}\), so \(\deg W=a+b-3\). Differentiating the Chebyshev differential equation shows that \(R=T_m'\) solves
\[
(1-t^2)R''-3tR'+(m^2-1)R=0.
\]
Taking the difference of the equations for \(Q\) and \(P\) after multiplication by \(P\) and \(Q\), respectively, gives
\[
(1-t^2)W'=3tW-(b^2-a^2)PQ.
\]
At \(\pm1\), both \(P\) and \(Q\) are nonzero by their explicit roots, so evaluating this polynomial identity there gives \(W(\pm1)\ne0\). At any zero of \(P\), one has \(W=-QP'\ne0\) by simplicity and disjointness; likewise \(W\ne0\) at any zero of \(Q\). Thus at any finite root of \(W\) the displayed identity forces \(W'\ne0\). Each root contributes ramification weight one.

**Infinity weight.** In the chart \(u=1\) with local parameter \(s=v/u\), the three homogeneous coordinate sections have successive orders \(0,b-a,b\) when ordered by increasing vanishing. Their orders are distinct, so they give the vanishing sequence. Subtracting \(0,1,2\) gives weight \(2b-a-3\). This also agrees with the total degree \(3(b-2)\) of the Wronskian divisor minus its finite degree.

**Branches of the dual.** As \(t\to\infty\), divide the tangent coordinates by their first component. The two affine ratios have leading orders \(s^a,s^b\) in \(s=1/t\), with nonzero coefficients. Taking an analytic \(a\)-th root of the unit in the order-\(a\) ratio makes it an exact \(a\)-th power of a new parameter; the order-\(b\) ratio then has first nonzero term of degree \(b\). Since \(\gcd(a,b)=1\), this gives the single Puiseux pair \((a,b)\) and the usual one-pair delta invariant \((a-1)(b-1)/2\). No finite parameter maps to \([1:0:0]\), since that would require \(P=Q=0\). The dual normalization therefore has exactly one point over this dual point, and there is exactly one branch there.

At a finite root of \(W\), \(P\ne0\), so write the original branch as a graph in the \(x\) coordinate. Its second derivative is \(W/P^3\), with a simple zero. In affine coordinates translated to the point with the tangent made horizontal, the graph is \(y=h(x)=c x^3+O(x^4)\), \(c\ne0\). The slope and intercept coordinates of its tangent have leading orders two and three, since they are \(h'(x)\) and \(h(x)-xh'(x)\). This is an ordinary cuspidal branch of the dual, regardless of whether there are other branches at its image point.

## Verification and scope

The optional SymPy checker `verify_chebyshev_dual.py` is a finite exact regression on \(2\le a\le12\), \(a<b\le18\), \(\gcd(a,b)=1\). It tests derivative coprimality, the derivative ODE identity, squarefreeness and degree of the Wronskian, endpoint values and the Gauss-coordinate leading coefficient. The proof above, not this bounded computation, establishes the unrestricted theorem. The result does not enumerate singular points of the dual or classify coincidences between branches and does not treat positive characteristic.

## Relationship to prior work

Yoshinaga, [*Regions of totally real arrangements of rational curves*](https://arxiv.org/abs/2611.00861), §7.2, and Freudenburg and Freudenburg, [*Curves defined by Chebyshev polynomials*](https://arxiv.org/abs/0902.3440), §3, give the known coprime Chebyshev curve geometry, including normalization and affine nodes. The degree and infinity computations here are direct consequences of the Gauss parametrization once the normalization and derivative root separation are known. The substantive addition is the uniform simplicity of every finite root of the normalized Wronskian, and hence the ordinary nature of the finite dual cuspidal branches. The general theory of Wronskians, biduality and Puiseux pairs is classical. Fomin and Shustin's [*Expressive curves*](https://arxiv.org/abs/2006.14066) is relevant broader context; the comparison with this work is not exhaustive. The equal-degree arrangements in Dimca and Sticlaru, [*Chebyshev curves, free resolutions and rational curve arrangements*](https://arxiv.org/abs/1108.0798), do not have the coprime hypotheses here.
