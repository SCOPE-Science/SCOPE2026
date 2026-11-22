# Sharp boundary-chord mean-distance profile of Euclidean rectangles

## Finding

Let \(K_{a,b}=[0,a]\times[0,b]\) with \(a\ge b>0\). Let \(X,Y\) be independent points uniformly distributed with respect to arclength on its boundary. Write \(t=b/a\in(0,1]\), \(\theta(K)=\mathbb E\|X-Y\|_2\), and \(\mathcal R(t)=\theta(K_{a,b})/\operatorname{per}(K_{a,b})\). Define
\[
S=\sqrt{1+t^2},\qquad A=\operatorname{arsinh}(1/t),\qquad B=\operatorname{arsinh}(t).
\]
Then the **entire exact profile** is
\[
\mathcal R(t)=\frac{2(1+t^3)+\frac23S(-t^2+4t-1)+\frac23[(2+3t)B+t^2(2t+3)A]}{8(1+t)^3}.
\]
It is strictly increasing for \(0<t<1\). Consequently, among all positive-sided rectangles of a given perimeter, the unique maximum up to congruence is the square, and the best lower limit is obtained only through degeneration:
\[
\frac16<\mathcal R(t)\le\frac1{16}+\frac{\sqrt2}{48}+\frac5{48}\log(1+\sqrt2)=0.1837725311973085\ldots,
\]
with equality on the right exactly for \(t=1\). The lower endpoint is not attained by a nondegenerate rectangle.

Both endpoint approaches are sharp:
\[
\mathcal R(t)=\frac16+t^2\left(\frac14\log\frac{2}{t}-\frac38\right)+O\!\left(t^3\log\frac1t\right)\quad(t\downarrow0),
\]
\[
\mathcal R(1)-\mathcal R(t)=\frac{3\sqrt2-3-\log(1+\sqrt2)}{64}(1-t)^2+O((1-t)^3)\quad(t\uparrow1).
\]

## Assumptions and scope

The ambient space is the Euclidean plane with Euclidean distance; both random endpoints are sampled independently under normalized arclength measure on the entire boundary. The rectangle has positive side lengths and is otherwise arbitrary. The theorem concerns rectangles, not every planar convex body; the square's numerical mean distance alone is not claimed as new.

## Proof

**1. Decompose the ordered boundary integral.** Put \(P=2(a+b)\) and
\[
I(a,b)=\int_{\partial K_{a,b}}\int_{\partial K_{a,b}}\|x-y\|_2\,ds(y)\,ds(x).
\]
A pair of points on the same side contributes \(2(a^3+b^3)/3\), summed over all four sides. For opposite horizontal sides the sum of the two oriented integrals equals \(2J(a,b)\), with the analogous vertical contribution \(2J(b,a)\), where
\[
J(a,b)=2\int_0^a(a-u)\sqrt{u^2+b^2}\,du
=a^2\sqrt{a^2+b^2}+ab^2\operatorname{arsinh}(a/b)-\frac23((a^2+b^2)^{3/2}-b^3).
\]
Each adjacent pair of sides contributes twice the corner integral \(K(a,b)\), and there are four corners, hence \(8K(a,b)\), where
\[
K(a,b)=\int_0^a\int_0^b\sqrt{x^2+y^2}\,dy\,dx
=\frac{2ab\sqrt{a^2+b^2}+a^3\operatorname{arsinh}(b/a)+b^3\operatorname{arsinh}(a/b)}6.
\]
Thus \(I(a,b)=2(a^3+b^3)/3+2J(a,b)+2J(b,a)+8K(a,b)\). Elementary collection gives
\[
I(a,b)=2(a^3+b^3)+\frac23\sqrt{a^2+b^2}\,(4ab-a^2-b^2)
+\frac23\Big[a^2(2a+3b)\operatorname{arsinh}(b/a)+b^2(2b+3a)\operatorname{arsinh}(a/b)\Big].
\]
Because \(\theta=I/P^2\), the quotient \(\theta/P\) is \(I/P^3\). Divide by \(a^3\) and put \(t=b/a\) to obtain the displayed formula.

**2. Strict monotonicity (an analytic certificate).** Define
\[
F(t)=t(t+2)A-(2t+1)B-3(1-t)(1+t-S).
\]
Direct differentiation of the closed expression, using \(A'=-1/(tS)\) and \(B'=1/S\), gives the exact identities
\[
4(1+t)^4\mathcal R'(t)=F(t),\qquad
F'(t)=2\big[(t+1)A-B+3(t-S)\big],
\]
\[
F''(t)=2\left[A+3-\frac{1/t+2+3t}{S}\right].
\]
Set \(z=1/t\ge1\), and define
\[
H(z)=\frac{z^2+2z+3}{\sqrt{z^2+1}}-3-\operatorname{arsinh}z.
\]
Then \(F''(t)=-2H(1/t)\), while exact differentiation factors as
\[
H'(z)=\frac{(z-1)^2(z+1)}{(z^2+1)^{3/2}}\ge0.
\]
Also \(H(1)=3\sqrt2-3-\log(1+\sqrt2)>0\): indeed \(\operatorname{arsinh}1<1<3(\sqrt2-1)\). Therefore \(F''(t)<0\) throughout \((0,1]\). Both endpoint values vanish, \(\lim_{t\downarrow0}F(t)=F(1)=0\); strict concavity forces \(F(t)>0\) for every \(0<t<1\), proving \(\mathcal R'(t)>0\).

**3. Endpoints and exact coefficients.** Substituting \(t=1\) yields the square constant. At the thin limit,
\(A=\log(2/t)+O(t^2)\), \(B=t+O(t^3)\), and \(S=1+t^2/2+O(t^4)\). Substitution and cancellation through first order yield the displayed \(t^2\log(1/t)\) law with its constant term. At the square, the first derivative vanishes and \(\mathcal R''(1)=-H(1)/32\), giving the stated Taylor coefficient. Both positive coefficients show optimality of the endpoint exponents.

## Verification

The standalone `checker.py` numerically reconstructs the ordered boundary integral from all sixteen ordered side pairs, compares it with the analytic expression at six aspect ratios, checks the derivative and curvature identities, verifies positivity of the concavity certificate, and checks both endpoint limits. This is corroborating finite computation, not the proof of universal monotonicity. The exact derivative identities and factorization were also separately simplified symbolically; the argument above establishes them without dependence on a computer algebra system.

## Relationship to prior work

Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances* (arXiv:2608.06470, first public version 6 August 2026; Section 5 of version 3) and *A Sharp Perimeter Inequality for Mean Distances on Convex Curves* (arXiv:2611.21661, Section 1 and sharpness discussion) prove the universal planar lower bound \(\theta(K)/\operatorname{per}K>1/6\), approached by thin rectangles. Neither inspected treatment states a strict aspect-ratio classification with the two exact endpoint stability coefficients above. Tokmachev's earlier boundary-mean-distance theorem yields the universal **disk** upper extremum among convex bodies, not the square extremum within rectangles. The standard square mean-distance value itself is not asserted to be new. Interior-point mean-distance inequalities and boundary-to-interior mean-distance gaps concern different statistics and do not imply this exact rectangle profile.

## Limitations

The classification holds only for Euclidean rectangles under independent normalized arclength endpoint sampling. It does not assert that the square maximizes this ratio among all quadrilaterals, and does not sharpen either universal planar convex-body bound. The first-public source date refers to the motivating research topic, not a publication date for this result. The historical-priority comparison is substantive but not exhaustive: earlier unindexed rectangular integration notes may exist. Independent audit remains to be performed.

## References

1. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470v3 (2026), https://arxiv.org/html/2608.06470v3 .
2. E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1 (2026), https://arxiv.org/html/2611.21661v1 .
3. A. S. Tokmachev, *Mean distance between random points on the boundary of a convex body*, Zap. Nauchn. Sem. POMI 510 (2022), 248–261; English translation J. Math. Sci. 286 (2024), 798–806, https://www.mathnet.ru/znsl7205 .
4. G. Bonnet, A. Gusakova, C. Thäle, D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, Adv. Math. 386 (2021), 107813, https://doi.org/10.1016/j.aim.2021.107813 .
