# Sharp finite-jet Fourier phase retrieval for two intervals

## Finding

For every two-interval indicator \(f=\mathbf 1_{E}\), with \(E\subset\mathbb R\) a union of exactly two bounded, nonempty intervals separated by a strictly positive gap, the three real numbers \(I(0)\), \(I''(0)\), and \(I^{(4)}(0)\), where
\[
\widehat f(t)=\int_{\mathbb R} f(x)e^{-itx}\,dx,\qquad I(t)=|\widehat f(t)|^2,
\]
determine \(E\) uniquely up to translation and reflection. Explicit radical inverse formulas are given below. The claim holds for unequal as well as equal interval lengths and with no restrictions on the gap.

These data are minimal among consecutive even Taylor jets at the origin: \(I(0)\) and \(I''(0)\) alone admit a continuum of geometrically inequivalent two-interval sets. Furthermore, the realizable jets satisfy a sharp fourth-order inequality, with equality precisely when the two intervals have equal length.

## Assumptions and scope

Write, after translation,
\[
E=[0,a]\cup[a+g,a+g+b],\qquad a,b,g>0,
\]
with endpoint overlap irrelevant to the indicator. Put \(s=a+b\), \(r=ab\), and \(d=g+s/2\). Define the Taylor coefficients \(c_2=I''(0)/2\) and \(c_4=I^{(4)}(0)/24\), so \(I(t)=s^2+c_2t^2+c_4t^4+O(t^6)\).

Then set
\[
s=\sqrt{I(0)},\qquad q=-c_2-\frac{s^4}{12},\qquad y=12c_4-\frac{s^6}{30}-qs^2.
\]
One always has \(q>0\), and the complete explicit recovery is
\[
r=\frac{\sqrt{y^2+4q^3}-y}{2q},\qquad
\{a,b\}=\left\{\frac{s+\sqrt{s^2-4r}}2,\frac{s-\sqrt{s^2-4r}}2\right\},\qquad
g=\sqrt{\frac{s^2}{4}+\frac qr}-\frac s2.
\]
The two choices of ordering for the recovered lengths differ by reflection, not by an additional ambiguity.

For a proposed triple \((I(0),c_2,c_4)\) with \(s=\sqrt{I(0)}>0\), there exists such a genuine two-interval indicator if and only if
\[
q>0,\qquad c_4\geq\frac{s^6}{360}+\frac{qs^2}{16}+\frac{q^2}{3s^2}.
\]
Equality holds exactly when \(a=b\).

## Proof

**1. Exact intensity factorization.** Let \(\operatorname{sinc}(u)=\sin(u)/u\), with its value at zero equal to one. The centers of the two intervals are separated by \(d=g+s/2\), hence translation invariance gives
\[
I(t)=a^2\operatorname{sinc}^2(at/2)+b^2\operatorname{sinc}^2(bt/2)
+2ab\operatorname{sinc}(at/2)\operatorname{sinc}(bt/2)\cos(dt).
\]
Taylor expansion through degree four and collection of symmetric polynomials in \(a,b\) yield exactly
\[
 c_2=-\frac{s^4}{12}+\frac{rs^2}{4}-rd^2,
\]
\[
 c_4=\frac{s^6}{360}-\frac{s^4r}{64}+\frac{s^2r^2}{48}
 +\frac{d^2s^2r}{24}-\frac{d^2r^2}{12}+\frac{d^4r}{12}.
\]
These identities also follow directly by integrating \((x-y)^2\) and \((x-y)^4\) on \(E\times E\).

**2. Reconstruction.** The second-order identity simplifies to
\[
q=r(d^2-s^2/4)=ab\,g(g+s)>0,
\]
so \(d^2=s^2/4+q/r\). Substitution into the fourth-order identity gives
\[
c_4=\frac{s^6}{360}+\frac{qs^2}{12}+\frac{q^2}{12r}-\frac{qr}{12}.
\]
Consequently \(y=q^2/r-qr\), equivalently \(qr^2+yr-q^2=0\). Because \(q>0\), this quadratic has precisely one positive root, namely the asserted expression for \(r\). The length pair consists of the roots of \(z^2-sz+r=0\). Since \(d>s/2\), the positive gap is recovered uniquely from \(d^2\). Only exchanging \(a,b\), geometrically a reflection, remains.

**3. Sharp range.** For fixed \(s>0\) and \(q>0\), any \(r\) in \((0,s^2/4]\) produces positive \(a,b\) and the strictly positive gap specified above. The function
\[
F_{s,q}(r)=\frac{s^6}{360}+\frac{qs^2}{12}+\frac{q^2}{12r}-\frac{qr}{12}
\]
is continuous and strictly decreasing on this interval because \(F'_{s,q}(r)=-q^2/(12r^2)-q/12<0\). Its value at \(r=s^2/4\) is exactly the claimed lower bound, and it diverges to infinity as \(r\downarrow0\). Thus the inequality is both necessary and sufficient, and equality means \(r=s^2/4\), or \(a=b\).

**4. Minimality.** For any prescribed \(s,q>0\), changing \(r\) continuously through \((0,s^2/4]\), with \(d^2=s^2/4+q/r\), leaves \(I(0)=s^2\) and \(c_2=-s^4/12-q\) unchanged. The resulting length pairs and gaps are different, so the order-two data do not identify the set. All odd intensity derivatives vanish, hence the fourth derivative is the first additional Taylor datum capable of identification.

## Verification

The independent-expressions checker `CHECK.py` evaluates the intensity coefficients by exact rational integration of even powers of the coordinate difference over the product set, independently of the sinc expansion. It compares the resulting coefficients to the closed identities for multiple rational interval configurations, verifies algebraic inversion and the sharp range inequality, and tests the direct Fourier identity numerically. Run with `python3 CHECK.py` using the Python standard library. No computation is used to prove the universal statements.

## Relationship to prior work

Xia and Xu [1, Theorems 1.2 and 1.3] establish that the *entire* Fourier magnitude determines indicators of one or two intervals up to translation/reflection, and derive stability from entire-magnitude data. The proof for two intervals first identifies an outer endpoint from equality of whole trigonometric polynomials and only then uses Taylor coefficients; it does not yield a three-number, order-four finite-jet inverse or the sharp jet-feasibility inequality above. The present result addresses a strictly smaller measurement set and proves its minimality.

The broad review by Grohs, Koppensteiner and Rathmair [2] discusses general Fourier phase-retrieval uniqueness and stability. General uniqueness given the whole magnitude does not imply sufficiency of any fixed finite Taylor jet. The interval-specific radical reconstruction and exact attainable-jet boundary are the distinguishing statements here.

## Limitations

Only indicators of one-dimensional unions of **exactly two** disjoint positive-length intervals with a positive gap are covered. Translation and reflection cannot be recovered from intensity. As the gap or one length tends to zero, the inverse degenerates; this theorem claims no uniform stability there. Recovering unordered lengths via a square root also loses Lipschitz regularity at equal lengths, although the symmetric invariant \(r\) is a smooth inverse function when \(q>0\). Exact infinitesimal derivatives are mathematical data; estimating them from noisy finite-band samples is not analyzed. Literature overlap outside the inspected sources remains possible; independent audit has not been performed.

## References

[1] Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first submitted 2026-06-18. https://arxiv.org/abs/2606.19855

[2] Philipp Grohs, Sarah Koppensteiner and Martin Rathmair, *Phase Retrieval: Uniqueness and Stability*, SIAM Review 62 (2020), 301–350. https://doi.org/10.1137/19M1256865
