# Sharp bounded-variation norm of whole-line \(C^2\) cardinal cubic-spline interpolation

## Finding

Let \(\mathcal B\) be the real sequences \(y=(y_j)_{j\in\mathbb Z}\) of finite discrete total variation
\[
V_d(y):=\sum_{j\in\mathbb Z}|y_{j+1}-y_j|<\infty.
\]
For \(y\in\mathcal B\), let \(Iy\) be its bounded, twice continuously differentiable cubic cardinal interpolant: \(Iy(j)=y_j\) for all integers and \(Iy\) is a polynomial of degree at most three on each closed interval \([j,j+1]\). Then
\[
\boxed{\operatorname{Var}_{\mathbb R}(Iy)\le K V_d(y),\qquad
K=\frac{2+\sqrt3+2\sqrt{2-\sqrt3}}3=1.5891089959929867\ldots.}
\]
The coefficient is **sharp**, attained by the single step \(y_j=0\) for \(j<0\) and \(y_j=1\) for \(j\ge0\). Consequently for all \(y,z\in\mathcal B\),
\[
\operatorname{Var}_{\mathbb R}(Iy-Iz)\le K V_d(y-z),
\]
with the same sharp coefficient. This is an operator norm on the space modulo additive constants, where total variation is a norm.

## Assumptions and scope

The grid is the **entire uniform integer lattice**; signals are real and have absolutely summable adjacent differences. The boundedness condition is imposed on the interpolant globally, not as natural boundary conditions at finite endpoints. Every such input is bounded because it has finite variation, and both limits at \(\pm\infty\) exist. The variation of a continuous function is the total variation over the whole real line, equal here to the integral of the absolute derivative.

## Proof

**1. Existence and uniqueness.** Put \(m_j=(Iy)''(j)\). Continuity of the first derivative across integer knots for cubic pieces gives the standard tridiagonal relations
\[
m_{j-1}+4m_j+m_{j+1}=6(y_{j+1}-2y_j+y_{j-1})=6(\Delta^2y)_j.
\]
Set \(r=2-\sqrt3\in(0,1)\), \(q=-r=\sqrt3-2\), and \(G_j=q^{|j|}/(2\sqrt3)\). Direct substitution gives \(G_{j-1}+4G_j+G_{j+1}=\mathbf1_{\{j=0\}}\). Because \(G\in\ell^1(\mathbb Z)\) and \(\Delta^2y\in\ell^1\),
\[
m_j=6\sum_{k\in\mathbb Z}G_{j-k}(\Delta^2y)_k
\]
is well defined, bounded and summable. Any bounded cubic on a unit cell has second derivatives bounded by a constant times its supremum, by the fixed-degree polynomial Markov inequality. Therefore a bounded global cubic spline has uniformly bounded nodal curvatures. The homogeneous recurrence has characteristic roots \(q\) and \(q^{-1}\); no nonzero bi-infinite bounded solution exists. On an interval with local coordinate \(u\in[0,1]\), the unique cubic with given nodal values and second derivatives is
\[
(Iy)(j+u)=(1-u)y_j+u y_{j+1}
+\frac{m_j}{6}\big((1-u)^3-(1-u)\big)
+\frac{m_{j+1}}6(u^3-u).
\]
Its derivative is
\[
(Iy)'(j+u)=y_{j+1}-y_j
+\frac{m_j}{6}(-2+6u-3u^2)
+\frac{m_{j+1}}6(-1+3u^2).
\]
These pieces satisfy the required matching conditions; the interpolation is bounded because \(y\) and \(m\) are bounded. Uniqueness follows from the bounded homogeneous recurrence.

**2. Reduction to a single step.** Each \(y\in\mathcal B\) has an absolutely convergent jump decomposition
\[
y_j=y_{-\infty}+\sum_{k\in\mathbb Z}(y_{k+1}-y_k)\mathbf1_{\{j\ge k+1\}}.
\]
The cardinal spline map is linear, commutes with integer translations, and reproduces constants. Its Green formula ensures uniform convergence under the above \(\ell^1\) sum, including derivatives on compact sets. If \(S=I(\mathbf1_{\{j\ge0\}})\) and \(\operatorname{Var}_{\mathbb R}(S)<\infty\), integrating the derivative series or passing through finite sums gives
\[
\operatorname{Var}_{\mathbb R}(Iy)\le \operatorname{Var}_{\mathbb R}(S)\sum_k|y_{k+1}-y_k|.
\]
The step itself proves that this bound is best possible. Thus it remains to calculate its variation exactly.

**3. Step curvature and central cell.** The step satisfies \((\Delta^2y)_{-1}=1\), \((\Delta^2y)_0=-1\) and all other second differences vanish. Therefore
\[
m_j=\sqrt3\big(q^{|j+1|}-q^{|j|}\big).
\]
In particular, \(m_{-1}=\sqrt3(1+r)\) and \(m_0=-m_{-1}\). On the only interval with a unit secant, \([-1,0]\), putting \(u=x+1\) gives
\[
S'(x)=1+\frac{\sqrt3(1+r)}6(-1+6u-6u^2)>0,
\]
because its endpoint minimum is \((3-\sqrt3)/2>0\). Its total variation contribution is exactly one.

**4. All tails and the radical.** On every right interval \([j,j+1]\) with \(j\ge0\), the secant vanishes and \(m_{j+1}=q m_j\), so
\[
S'(j+u)=\frac{m_j}{6}A(u),\qquad
A(u)=-\sqrt3+6u-3(3-\sqrt3)u^2.
\]
The quadratic has exactly one root in \((0,1)\), namely
\[
\alpha=\frac{1-\sqrt{2-\sqrt3}}{3-\sqrt3};
\]
it is negative before \(\alpha\) and positive after. Its integral over \([0,1]\) is zero. With
\[
P(u)=-\sqrt3\,u+3u^2-(3-\sqrt3)u^3,
\]
we consequently have \(\int_0^1|A(u)|\,du=-2P(\alpha)\). The left tail is the reflection of the right tail because \(S(-1-x)=1-S(x)\). Moreover \(\sum_{j\ge0}|m_j|=\sqrt3(1+r)/(1-r)=3\). Hence the two tails contribute
\[
2\sum_{j\ge0}\frac{|m_j|}6\int_0^1|A(u)|\,du
=\int_0^1|A(u)|\,du=-2P(\alpha).
\]
An exact algebraic simplification yields
\[
1-2P(\alpha)=\frac{2+\sqrt3+2\sqrt{2-\sqrt3}}3.
\]
This proves the asserted sharp constant and the equality case. □

## Verification

The self-contained checker `verify_cardinal_cubic.py` uses exact symbolic arithmetic to verify the Green recurrence, the step moments, the turning point and the radical identity. Independently it solves a long finite tridiagonal spline system and integrates each cell's absolute quadratic derivative, recovering the sharp step value to numerical precision. It also tests 1,200 finite-support random perturbations against the proven bound. These tests corroborate, but do not replace, the all-input analytical proof above. Run using `python verify_cardinal_cubic.py`; it requires Python, SymPy, NumPy and SciPy.

## Relationship to prior work

Schoenberg's classical cardinal-spline interpolation theory and de Boor's treatment provide the established operator and the tridiagonal inverse. This finding computes a different quantitative object: the **exact global total-variation operator norm** from sampled \(BV\) to continuous \(BV\), and a sharp jump extremizer. The variation-diminishing property of *positive B-spline approximation* does not transfer to *interpolatory* cardinal cubics. Published finite-knot natural-cubic results, orthogonal piecewise-linear spline projection norms and Shannon total-variation regularization concern different boundary conditions, operators or norms, so their reported statements do not yield the displayed coefficient. No claim is made that mathematical literature has been exhaustively searched; the complete original Schoenberg chapter was not accessible for full-text priority comparison.

## Limitations

The constant concerns real-valued sequences, bi-infinite equally spaced knots and bounded \(C^2\) cardinal cubic interpolation. It need not hold for finite natural/not-a-knot splines, nonuniform grids, periodic splines, local Hermite splines or higher-order cardinal splines. No optimality is claimed among other spline schemes. Exact first historical circulation of the 1973 Schoenberg text is not day-verified; the bibliographic 2012 online release date identifies a verifiable reissued source record, not the original invention date.

## References

- I. J. Schoenberg, *Cardinal Spline Interpolation*, original edition 1973, SIAM online reissue (2012-03-28), Chapter 4. https://epubs.siam.org/doi/10.1137/1.9781611970555.ch4
- Carl de Boor, *A Practical Guide to Splines*, revised edition, Chapters IV and XVI (uniform/cardinal interpolation and decay). https://djvu.online/file/W5YE3VGOgt1Ml
- A. Dermoune and C. Preda, *Estimation of noisy cubic spline using a natural basis*, first arXiv version 2014-03-06. https://arxiv.org/abs/1403.1388
- R. Abergel and L. Moisan, *The Shannon Total Variation*, especially discussion of cardinal spline interpolation in imaging. https://helios2.mi.parisdescartes.fr/~rabergel/papers/shannon-tv_r2.pdf
