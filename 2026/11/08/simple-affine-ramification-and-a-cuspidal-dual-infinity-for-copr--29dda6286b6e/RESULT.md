# Simple affine ramification and a cuspidal dual infinity for coprime Chebyshev curves

## Finding

For coprime integers \(2\le a<b\), put \(C_{a,b}\subset\mathbb P^2_{\mathbb C}\) for the projective closure of \(T_b(x)-T_a(y)=0\), where \(T_m(\cos\theta)=\cos(m\theta)\). Its normalization is \(t\mapsto[1:T_a(t):T_b(t)]\) in coordinates \([Z:X:Y]\). The following statements hold simultaneously:

1. The dual curve has degree \(\deg(C_{a,b}^{\vee})=a+b-1\).
2. The ramification divisor of the base-point-free linear series \(\langle1,T_a,T_b\rangle\subset H^0(\mathbb P^1,\mathcal O(b))\) has \(a+b-3\) distinct simple points on \(\mathbb A^1\), the roots of \(W_{a,b}=T_a'T_b''-T_b'T_a''\), and has remaining weight exactly \(2b-a-3\) at \(t=\infty\).
3. The dual's point corresponding to the tangent line at \(t=\infty\) has exactly one analytic branch, with Puiseux pair \((a,b)\), and local delta invariant \((a-1)(b-1)/2\). Each finite root of \(W_{a,b}\) gives an ordinary cuspidal *branch* of the dual; distinct parameters need not have distinct dual images.

## Assumptions and scope

Work over \(\mathbb C\) with integers \(a,b\) satisfying \(2\le a<b\) and \(\gcd(a,b)=1\). Derivatives and roots are taken over \(\mathbb C\). The term ramification divisor means the Wronskian/inflection divisor of the three-dimensional space of sections \(\langle1,T_a,T_b\rangle\) on the normalization, not the branch divisor of the normalization map. The dual is the closure of lines tangent to smooth points of the original curve.

## Proof

**Normalization and immersion on the affine line.** The homogeneous map is
\[
\nu([u:v])=[v^b:v^{b-a}T_a^{h}(u,v):T_b^{h}(u,v)],
\quad T_m^{h}(u,v)=v^mT_m(u/v).
\]
It has no base points. Its generic degree divides both \(a\) and \(b\): a generic value of the first nonconstant coordinate has \(a\) parameter preimages and a generic value of the second has \(b\). Coprimality makes the degree one. Thus \(\nu\) is the normalization, and its image has degree \(b\). Let \(P=T_a'\) and \(Q=T_b'\). Their roots are respectively \(\cos(k\pi/a)\) and \(\cos(l\pi/b)\) with the internal integer ranges. They are simple and disjoint: coincidence would imply \(k/a=l/b\), contradicting coprimality. Hence \(P,Q\) never vanish simultaneously; \(\nu\) is immersed at every finite parameter.

**Dual degree.** The affine tangent line has homogeneous line coordinates
\[
\gamma(t)=[P(t)T_b(t)-Q(t)T_a(t):Q(t):-P(t)].
\]
The leading coefficients of \(T_a,T_b\) are \(2^{a-1},2^{b-1}\); therefore the first coordinate of \(\gamma\) has degree \(a+b-1\), leading coefficient \(ab(a-b)2^{a+b-2}\ne0\). The other two coordinates have degrees \(b-1\) and \(a-1\). There are no common zeros at finite parameters, by \(\gcd(P,Q)=1\), and none at infinity because the first coordinate has full degree. Thus the homogenized Gauss map has \(\gamma^*\mathcal O_{(\mathbb P^2)^\vee}(1)=\mathcal O_{\mathbb P^1}(a+b-1)\). In characteristic zero, reflexivity/biduality makes the Gauss map of an irreducible plane curve birational onto the dual. Consequently \(\deg C_{a,b}^{\vee}=a+b-1\).

**Simple finite Wronskian roots.** In affine parameter the Wronskian of \(1,T_a,T_b\) is exactly
\[
W=P Q'-Q P'.
\]
Its leading coefficient is \(ab(b-a)2^{a+b-2}\), so \(\deg W=a+b-3\). Differentiating the Chebyshev differential equation gives, for \(R=T_m'\),
\[
(1-t^2)R''-3tR'+(m^2-1)R=0.
\]
Subtracting for \(P,Q\) yields
\[
(1-t^2)W'=3tW-(b^2-a^2)PQ.
\]
At \(t=\pm1\), the value of \(W\) is nonzero, since \(W(1)=a^2b^2(b^2-a^2)/3\) and \(W(-1)\ne0\) follows by parity. At any other common root of \(W,W'\), the displayed identity would force \(PQ=0\). But if \(P=0\), then \(W=-QP'\ne0\) because \(P\) has a simple zero and \(Q\ne0\); the \(Q=0\) case is symmetric. Thus \(\gcd(W,W')=1\) and all \(a+b-3\) finite roots are distinct and simple.

**Weight at infinity.** For the degree-\(b\) linear series on \(\mathbb P^1\), its Wronskian divisor has degree \(3(b-2)\). Subtracting the just-computed finite weight gives infinity weight \(3b-6-(a+b-3)=2b-a-3\). Equivalently, in the local parameter \(s=v/u\) at infinity, the vanishing sequence of the three homogeneous sections is \((0,b-a,b)\), whose ramification weight is \(0+(b-a-1)+(b-2)=2b-a-3\).

**Unique branch of the dual at infinity.** Set \(s=1/t\). Divide the homogeneous tangent coordinates by their first coordinate. Their last two ratios have respective nonzero leading terms \(c_as^a\) and \(c_bs^b\) (the order of these two coordinates is \(a,b\)). As \(\gcd(a,b)=1\), this is a plane branch with sole Puiseux pair \((a,b)\) and delta invariant \((a-1)(b-1)/2\). The target point is \([1:0:0]\); a finite parameter could map there only if \(P=Q=0\), impossible. Birationality of the Gauss map therefore shows the dual has exactly one branch there. At a finite simple zero of \(W\), choose a local coordinate along the immersed original branch, in which its tangent graph has nonzero cubic term and vanishing quadratic term. Its slope and intercept vary as terms of respective orders \(2\) and \(3\), proving the corresponding *dual branch* is an ordinary cusp. This statement does not rule out coincidences of the images of distinct parameters.

## Verification

The bundled standalone script `verify_chebyshev_dual.py` uses exact symbolic arithmetic (SymPy). It checks \(73\) coprime pairs with \(2\le a\le12\) and \(a<b\le18\): derivative coprimality, Wronskian degree and squarefreeness, nonvanishing at the endpoints, leading coefficients, and infinity weight. Run with `python verify_chebyshev_dual.py`. This is a finite regression test; the universal statement follows from the preceding Chebyshev ODE, root separation, and Gauss-map proof.

## Relationship to prior work

Yoshinaga [1, §7.2, Proposition 7.2] gives the coprime Chebyshev normalization, degree, affine nodes, and topology of real complementary regions. Freudenburg and Freudenburg [2, §3] study the Chebyshev plane parametrization and its nodes. Fomin and Shustin [3] study expressive curves including Chebyshev examples. Dimca and Sticlaru [4] study a different, typically reducible equal-degree Chebyshev curve arrangement. The asserted addition is the exact dual degree together with squarefree normalized finite ramification and the dual's unique Puiseux branch at infinity; it does not reassert previously known nodal or region counts. The general Wronskian and biduality principles are classical inputs, not new results.

## Limitations

The formulas are over characteristic zero and for coprime \(a,b\) in the indicated range. They classify ramification on the normalization and one distinguished singular branch of the dual; they do not classify all intersections between different dual branches, enumerate distinct singular points of the dual, or treat positive characteristic. Exhaustive historical priority, especially under terminology for Chebyshev knots, expressive curves, or rational plane duals, is not guaranteed by keyword searches. Independent mathematical validation has not been performed.

## References

[1] M. Yoshinaga, *Regions of totally real arrangements of rational curves* (2026), arXiv:2611.00861, §7.2. https://arxiv.org/html/2611.00861v1

[2] G. Freudenburg and J. Freudenburg, *Curves defined by Chebyshev polynomials* (2009), arXiv:0902.3440, §3. https://arxiv.org/abs/0902.3440

[3] S. Fomin and E. Shustin, *Expressive curves*, Communications of the American Mathematical Society 3 (2023), 669–743; arXiv:2006.14066. https://arxiv.org/abs/2006.14066

[4] A. Dimca and G. Sticlaru, *Chebyshev curves, free resolutions and rational curve arrangements* (2011), arXiv:1108.0798. https://arxiv.org/abs/1108.0798
