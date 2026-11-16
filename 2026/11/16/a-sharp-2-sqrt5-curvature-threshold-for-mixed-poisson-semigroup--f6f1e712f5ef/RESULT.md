# A sharp \(2+\sqrt5\) curvature threshold for mixed Poisson semigroup Fourier kernels

## Finding

Write \(P_s(x)=s/[\pi(x^2+s^2)]\) for the one-dimensional Poisson kernel and, for \(0<a<b\), \(0<w<1\), put
\[
K_{a,b,w}(x)=wP_a(x)+(1-w)P_b(x).
\]
With the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx\), its multiplier is the strictly positive mixture
\[
\widehat K_{a,b,w}(\xi)=w e^{-a|\xi|}+(1-w)e^{-b|\xi|}.
\]
Although every such density is even and strictly decreasing on the positive half-line, its second derivative can have six distinct sign-changing real zeros instead of two. The following is the complete sharp phase diagram, including the transition weights.

Put \(t=(b/a)^2>1\), \(W=(b/a)(1-w)/w>0\), and
\[
R_t(u)=\frac{(3u-1)(u+t)^3}{(t-3u)(u+1)^3},\qquad \frac13<u<\frac t3.
\]
The critical squared scale ratio is \(t_*=9+4\sqrt5=(2+\sqrt5)^2\).

* If \(1<t<t_*\), then \(K_{a,b,w}''\) has exactly two real zeros, both simple, for every \(w\). The same is true at \(t=t_*\) except for the unique weight for which \(W=R_{t_*}((t_*+1)/10)\); at that weight the two distinct zeros each have multiplicity three.
* If \(t>t_*\), define
\[
u_\pm=\frac{t+1\pm\sqrt{t^2-18t+1}}{10},\quad W_{\max}=R_t(u_-),\quad W_{\min}=R_t(u_+).
\]
Then \(0<W_{\min}<W_{\max}\). There are exactly **six distinct simple real zeros**, three positive and three negative, if and only if
\[
W_{\min}<W<W_{\max}.
\]
At either boundary \(W=W_{\min}\) or \(W=W_{\max}\), the second derivative has four distinct real zeros (a simple pair and a double pair). Outside the closed interval it has exactly two distinct simple real zeros.

Consequently, **some positive mixture has six curvature sign changes if and only if \(b/a>2+\sqrt5\)**. This threshold is attained sharply as an infimum but not at equality. In terms of the original mixture weight, the six-zero chamber is
\[
\frac{b/a}{b/a+W_{\max}}<w<\frac{b/a}{b/a+W_{\min}}.
\]

For example, \(a=1\), \(b=5\), \(w=1/37\) gives \(W=180\) and six simple second-derivative zeros, while the kernel remains strictly unimodal.

## Assumptions and scope

All kernels are functions on \(\mathbb R\), and all scales and weights are exactly as above. Zeros refer to distinct real roots of the classical smooth second derivative; root multiplicities are stated separately. "Inflection points" refers to zeros at which the second derivative changes sign; the tangency roots at the two weight boundaries are not inflection points. This is a result about a **convex average of two Poisson semigroup kernels**, not an assertion that this average is the Poisson kernel of any one of the restricted elliptic operators considered in earlier bell-shape theorems. No assertion about the sign changes of derivatives of orders three and higher is made.

## Proof

**1. Reduction to a single rational level equation.** Rescaling \(x= a\sqrt u\) yields
\[
K_{a,b,w}''(x)=\frac{2w}{\pi a^3}\left[\frac{3u-1}{(u+1)^3}+W\frac{3u-t}{(u+t)^3}\right].
\]
For \(0\le u\le1/3\) the bracket is strictly negative, and for \(u\ge t/3\) it is strictly positive. All possible zeros therefore satisfy \(1/3<u<t/3\). On that open interval, multiplying by strictly positive denominators gives the equivalent equation \(R_t(u)=W\). Each positive solution \(u\) corresponds to the two real zeros \(x=\pm a\sqrt u\), with the same multiplicity because the change of variable is locally invertible at these points.

**2. Critical points.** Direct differentiation (or the quotient rule followed by cancellation) gives the exact identity
\[
R_t'(u)=\frac{6(t-1)(u+t)^2\,[5u^2-(t+1)u+t]}{(t-3u)^2(u+1)^4}.
\]
The denominator and all prefactors are strictly positive on the interval. The quadratic
\[
Q_t(u)=5u^2-(t+1)u+t
\]
has discriminant \(\Delta=t^2-18t+1\). For \(1<t<t_*\) this discriminant is negative; hence \(R_t\) is strictly increasing. At \(t=t_*\), \(Q_t\) is a perfect square with one root \(u_0=(t_*+1)/10\) in the interval, so \(R_t\) is still strictly increasing, but its derivative vanishes to order two at \(u_0\).

For \(t>t_*\), both real roots \(u_-<u_+\) of \(Q_t\) lie strictly between \(1/3\) and \(t/3\). Indeed the vertex \((t+1)/10\) is interior, \(Q_t\) is negative at its vertex, and \(Q_t(1/3)=2t/3+2/9>0\), \(Q_t(t/3)=2t^2/9+2t/3>0\). Hence \(R_t\) increases to \(W_{\max}\) at \(u_-\), decreases to \(W_{\min}\) at \(u_+\), and then increases again. The endpoint limits are \(R_t(1/3+)=0\) and \(R_t(t/3-)=+\infty\). The two extremal values are positive and strictly ordered. Horizontal-line intersections give exactly the root census asserted above. At either nondegenerate extremum the repeated level intersection has multiplicity two. At the critical merger, the level intersection at \(u_0\) has multiplicity three because \(Q_{t_*}(u)=5(u-u_0)^2\) and all other factors in \(R'\) are nonzero there.

**3. Sharp threshold and unimodality.** Since \(t_*=(2+\sqrt5)^2\), the three-intersection chamber exists precisely when \(b/a>2+\sqrt5\). On the other hand, \(P_s'(x)=-2sx/[\pi(x^2+s^2)^2]<0\) for all \(x>0\); a positive convex mixture preserves this strict monotonicity. Thus the six-inflection regime occurs without any additional mode.

**4. Exact witness.** For \(a=1,b=5,w=1/37\), after removing a positive rational factor and positive denominator, the sign of \(K''(x)\), with \(u=x^2\), is the sign of
\[
543u^4-2656u^3-6330u^2+32040u-20125.
\]
Its values at \(u=1/2,1,2,3,5,6\) have signs \(-,+,+,-,-,+\), respectively. Hence it has positive roots in each of \((1/2,1)\), \((2,3)\), and \((5,6)\). Descartes' sign rule bounds its number of positive roots by three, so these are all simple. Each produces two distinct real inflection points. This independently certifies strictness of the existence statement.

## Verification

The accompanying standalone `check.py` uses only Python's standard library. It checks the exact rational identity for \(R_t'\) at 239 rational evaluation pairs away from poles, reconstructs the quartic witness coefficients by integer polynomial arithmetic, evaluates its six rational sign brackets, and checks the critical discriminant and its sign on rational examples on both sides of the threshold. The universal theorem follows from the symbolic proof above; the finite checks are independent reproducibility checks and cannot certify all real parameters.

## Relationship to prior work

The 2025 preprint *Poisson kernels on the half-plane are bell-shaped* (arXiv:2501.16068), published in 2026, proves bell shape for individual eligible Poisson kernels. The October 1, 2026 preprint *Bell-shaped functions are Poisson kernels* (arXiv:2610.01717) provides a converse representation using intransitive diffusions. Neither result asserts closure under positive **arithmetic mixtures of different heights**, and neither provides the threshold above. A different, earlier literature on Cauchy *density mixtures*, exemplified by Došlá (2009), studies the emergence of multiple **modes** under shifts of the centers, not the emergence of six curvature changes at a common center. The criterion here is therefore not implied by its bimodality formulas. The general 2019/2022 characterization by Kwaśnicki and Simon supplies a broad class-theoretic framework for bell-shaped functions, but does not state the present explicit curvature phase diagram.

## Limitations

Only the second derivative is classified. A mixture with two curvature sign changes need not be bell-shaped at all higher orders; no equivalence with full bell shape is claimed. The two-kernel formula concerns centered, positive, real, same-location Poisson densities; shifted, signed or three-or-more-component mixtures are outside scope. Generic results about bell shape and mixture modality are not alleged to be new. Although the exact scale threshold and chamber were not located in the inspected sources and searches, unpublished or differently indexed calculations of Cauchy-mixture inflection counts remain possible; no independent priority review has been conducted.

## References

1. M. Kwaśnicki, *Bell-shaped functions are Poisson kernels*, arXiv:2610.01717, first submitted 2026-10-01, https://arxiv.org/abs/2610.01717.
2. M. Kwaśnicki, *Poisson kernels on the half-plane are bell-shaped*, arXiv:2501.16068 (first submitted 2025-01-27); *Bull. London Math. Soc.* 58 (2026), e70303, https://arxiv.org/abs/2501.16068.
3. Š. Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, *Kybernetika* 45 (2009), 279–292, https://www.dml.cz/handle/10338.dmlcz/140075.
4. M. Kwaśnicki and T. Simon, *Characterisation of the class of bell-shaped functions*, arXiv:1910.07752 (first submitted 2019-10-17), *Math. Z.* 301 (2022), 2659–2683, https://arxiv.org/abs/1910.07752.
