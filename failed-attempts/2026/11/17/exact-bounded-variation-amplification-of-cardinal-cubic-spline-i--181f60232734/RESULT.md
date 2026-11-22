# Exact bounded-variation amplification of cardinal cubic spline interpolation

## Finding

For the canonical bounded real cubic cardinal interpolant \(I_3\) on the uniform integer grid, the sharp operator gain from *discrete first-difference total variation* to *continuous total variation* is
\[
C_3=\sup_{V_{\mathbb Z}(y)>0}
\frac{\operatorname{Var}_{\mathbb R}(I_3y)}{V_{\mathbb Z}(y)}
=1+\frac{4h}{1-q}=1.589108995992987\ldots,
\]
with
\[
q=2-\sqrt3,\qquad E=\sqrt3(1+q),\qquad
 t_* =\frac{1-\sqrt q}{1+q},\qquad
h=\frac E6t_*(1-t_*)\bigl((2-q)-(1+q)t_*\bigr).
\]
The constant is the unique root in \((1.58,1.60)\) of
\[
81z^4-216z^3+18z^2+312z-191=0.
\]
A single-jump sequence attains equality. Cubic interpolation may therefore increase the total variation of sampled data by approximately 58.91 percent, even though it interpolates all samples exactly.

## Assumptions and scope

Let \(y=(y_j)_{j\in\mathbb Z}\) be any **real** sequence for which
\[
V_{\mathbb Z}(y)=\sum_{j\in\mathbb Z}|y_{j+1}-y_j|<\infty.
\]
This assumption implies boundedness and limits at both ends of the grid. Let \(I_3y=s\) denote the unique *bounded* function on \(\mathbb R\) which is twice continuously differentiable, a polynomial of degree at most three on each unit cell \([j,j+1]\), and satisfies \(s(j)=y_j\) for every integer \(j\). Its continuous variation is \(\operatorname{Var}_{\mathbb R}(s)=\int_{\mathbb R}|s'(x)|\,dx\), which is finite for the stated data. No periodic identification, finite-interval boundary convention, or compact-support restriction is imposed.

## Proof

**1. Bounded Green solution.** Write \(M_j=s''(j)\). Cubic matching gives the three-term difference equation
\[
M_{j-1}+4M_j+M_{j+1}=6(y_{j+1}-2y_j+y_{j-1}).\tag{1}
\]
The inverse of the left operator on bounded sequences is convolution with
\[
G_k=\frac{(-q)^{|k|}}{2\sqrt3},\qquad q=2-\sqrt3,
\]
since \(q^2-4q+1=0\) and \(4G_0+2G_1=1\). Thus
\[
M_j=6\sum_{k\in\mathbb Z}G_{j-k}(y_{k+1}-2y_k+y_{k-1}).\tag{2}
\]
The sum is absolutely convergent. The cell polynomial is
\[
s(j+t)=(1-t)y_j+ty_{j+1}
 +\frac{M_j((1-t)^3-(1-t))+M_{j+1}(t^3-t)}6,
\quad 0\le t\le1.\tag{3}
\]
Equations (1)–(3) give existence, boundedness, interpolation and \(C^2\) matching. Uniqueness follows because the homogeneous recurrence has no nonzero bi-infinite bounded solution; boundedness of the spline forces boundedness of its knot second derivatives by finite-dimensional norm equivalence on each cell.

**2. Exact step response.** Take \(u_j=0\) for \(j\le0\) and \(u_j=1\) for \(j\ge1\). The second differences of \(u\) are \(+1\) at zero and \(-1\) at one. Consequently
\[
M_j=6(G_j-G_{j-1}),\qquad
M_0=E,\quad M_1=-E,\quad M_{1+k}=(-q)^k(-E)\ (k\ge0),
\]
where \(E=\sqrt3(1+q)\). Also \(M_{1-j}=-M_j\), giving the reflection \(s(1-x)=1-s(x)\).

On the central cell, (3) becomes
\[
s(t)=t-\frac E6t(1-t)(1-2t),\qquad0\le t\le1.
\]
Its derivative \(1-E(1-6t+6t^2)/6\) is strictly positive because \(E<6\); its total variation on the central cell is exactly one.

For the first right-hand plateau cell,
\[
s(1+t)-1=F(t):=\frac E6t(1-t)\bigl((2-q)-(1+q)t\bigr),\qquad0\le t\le1.
\]
Here \(F(t)>0\) in the open cell and \(F(0)=F(1)=0\). The derivative has one zero in \((0,1)\), namely
\[
t_* =\frac{1-\sqrt q}{1+q},
\]
as verified by substituting \(q^2-4q+1=0\); its maximum is \(h=F(t_*)\). Every subsequent plateau cell has deviation \((-q)^{j-1}F(t)\) on \([j,j+1]\) for \(j\ge1\), so each contributes exactly \(2hq^{j-1}\) to variation. The geometric total on the right is \(2h/(1-q)\), and the reflected left tail contributes the same. Therefore
\[
\operatorname{Var}_{\mathbb R}(I_3u)=1+\frac{4h}{1-q}=C_3,\qquad V_{\mathbb Z}(u)=1.\tag{4}
\]
A symbolic elimination yields the displayed quartic, and direct root isolation on \((1.58,1.60)\) selects the stated real value.

**3. Universal upper bound and equality.** For general \(y\), the summable increments \(d_k=y_k-y_{k-1}\) yield
\[
y_j=y_{-\infty}+\sum_{k\in\mathbb Z}d_k\mathbf1_{\{j\ge k\}},
\qquad \sum_k|d_k|=V_{\mathbb Z}(y).
\]
The bounded cardinal interpolation operator preserves constants and commutes with translations. The corresponding series of step-interpolant derivatives converges absolutely in \(L^1(\mathbb R)\), by (4), and represents the derivative of the interpolant (equivalently, pass to the uniform limit using (2)–(3)). Hence
\[
\operatorname{Var}_{\mathbb R}(I_3y)
\le\sum_k|d_k|\operatorname{Var}_{\mathbb R}(I_3u)
=C_3 V_{\mathbb Z}(y).
\]
The step \(u\) already attains equality, as do all its integer translations and nonzero affine rescalings. This proves the sharp norm and its attainment for the stated infinite family of inputs.

## Verification

The standalone `verify.py` checks the Green recurrence identity, the exact critical-point equation, the quartic polynomial, and the geometric tail profile using symbolic algebra. It also integrates the absolute derivative of finite natural cubic interpolants by enumerating *all derivative critical points*, for increasing interval sizes, and tests additional finitely supported random jump inputs. The numeric finite-interval experiments are diagnostics; the preceding steps establish the unrestricted theorem.

To reproduce: install Python 3 with `sympy`, `numpy` and `scipy`, then run `python verify.py`. The final success marker is `ALL_CARDINAL_CUBIC_VARIATION_CHECKS_PASS`.

## Relationship to prior work

The standard cardinal cubic interpolation operator is classical. Madani–Ayremlou–Amini–Marvasti study reconstruction and optimal compact interpolation filters in an \(\ell^2\)-frequency-error setting [1]. Tzimbalario studies Lebesgue constants for cardinal interpolation from bounded sequences into the supremum norm [2]. Abergel–Moisan introduce Shannon total variation and discuss spline reconstructions but do not formulate the present sharp discrete-first-difference to continuous-total-variation norm [3]. These different normed problems neither imply nor directly contradict the stated exact constant. Classical monotone cubic interpolators impose altered shape constraints and are not the same global linear \(C^2\) cubic operator [4].

## Limitations

The theorem is specific to unweighted bi-infinite, uniformly spaced, real, \(C^2\) cardinal **cubic** interpolation. No finite-grid boundary-independent coefficient, nonuniform-mesh bound, higher-degree generalization, or multivariate statement is asserted. Related historical work on cardinal interpolation operator norms may contain unindexed equivalents; a definitive historical-priority determination remains open. In particular, older works on cardinal spline interpolation-operator norms and \(\ell^p\) stability were not all available in full text.

## References

[1] R. Madani, A. Ayremlou, A. Amini, F. Marvasti, *Optimized Spline Interpolation*, arXiv:1105.0011v1, first public version 29 April 2011. https://arxiv.org/abs/1105.0011

[2] J. Tzimbalario, *Lebesgue Constants for Cardinal L-Spline Interpolation*, Canadian Journal of Mathematics **29** (1977), 441–448. https://doi.org/10.4153/CJM-1977-047-4

[3] R. Abergel, L. Moisan, *The Shannon Total Variation*, preprint (2016). https://helios2.mi.parisdescartes.fr/~rabergel/papers/shannon-tv_2016r1.pdf

[4] F. N. Fritsch, R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis **17** (1980), 238–246. https://doi.org/10.1137/0717021
