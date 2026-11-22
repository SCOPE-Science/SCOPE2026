# Exact positivity probability and Pareto noise instability of three-knot natural-spline quadrature

## Finding

Let three independent uniform points in \([0,1]\) have order statistics \(X_0<X_1<X_2\). For arbitrary real sampled values \(y_0,y_1,y_2\), let \(S_y\) be the ordinary \(C^2\) natural cubic spline on \([X_0,X_2]\), interpolating the data and satisfying \(S_y''(X_0)=S_y''(X_2)=0\). Consider the **normalized spline-integral quadrature**
\[
 Q_X(y)=\frac1{X_2-X_0}\int_{X_0}^{X_2}S_y(x)\,dx=\sum_{i=0}^2W_i y_i.
\]
The following statements hold exactly.

1. All three weights are nonnegative with probability \(4-\sqrt{13}\), approximately \(0.3944487245\). Almost surely, strict positivity and nonnegativity have the same probability.
2. Put \(A_X=\sum_i|W_i|\), the sharp operator norm from the three sampled values with the maximum norm to the averaged integral. For **every real** \(z\ge1\),
\[
 \mathbb P(A_X>z)=\sqrt{(4z-1)^2+4}-(4z-1).
\]
In particular \(\mathbb P(A_X>z)\sim(2z)^{-1}\), and for \(s\ge0\), \(\mathbb E[A_X^s]<\infty\) if and only if \(s<1\).
3. If the three observed values also have independent, centered Gaussian measurement errors of variance \(\sigma^2>0\), independent of the locations, then the induced error in \(Q_X\) has **infinite unconditional mean absolute magnitude and infinite second moment**. These statements concern the random-hull average, not the integral over all of \([0,1]\).

## Assumptions and scope

The knots are three independent continuous uniform samples, sorted, so ties occur with probability zero. The interpolant is the conventional natural cubic with zero second derivatives at the two extreme sampled knots (not a B-spline basis with independent nonnegative coefficients, a not-a-knot cubic, or a spline constrained to be positive). The average is taken over the observed hull \([X_0,X_2]\) and normalized by its positive length. The quadrature weights are coefficients of the original nodal ordinates, not Gaussian spline quadrature nodes optimized to integrate an entire spline space. All probabilities integrate over the random knots; the final noise conclusion integrates over independent Gaussian observation errors as well.

## Proof

Write \(a=X_1-X_0>0\), \(b=X_2-X_1>0\), and \(L=a+b\). The only nonzero interior knot second derivative is
\[
 M_1=\frac3{a+b}\left(\frac{y_2-y_1}{b}-\frac{y_1-y_0}{a}\right).
\]
On a cell of width \(h\), the integral of the cubic spline equals the trapezoidal contribution minus \(h^3\) times the sum of its endpoint second derivatives divided by \(24\). Because \(M_0=M_2=0\),
\[
 \int_{X_0}^{X_2} S_y(x)\,dx
 =\frac{a(y_0+y_1)+b(y_1+y_2)}2
 -\frac{a^3+b^3}{24}M_1.
\]
Collecting the three coefficients and dividing by \(L\) yields
\[
 W_0=\frac{3a^2+ab-b^2}{8aL},\quad
 W_1=\frac{a^2+3ab+b^2}{8ab},\quad
 W_2=\frac{3b^2+ab-a^2}{8bL}.
\]
They sum to one. In particular \(W_1>0\). Set \(T=a/L\in(0,1)\); then
\[
 W_0=\frac{T+3-T^{-1}}8,\qquad
 W_1=\frac{1+T-T^2}{8T(1-T)},\qquad
 W_2=\frac{4-T-(1-T)^{-1}}8.
\]
Let \(c=(\sqrt{13}-3)/2\in(0,1/2)\). Since \(T^2+3T-1\) increases strictly on \((0,1)\), \(W_0<0\) precisely when \(T<c\); by reflection, \(W_2<0\) precisely when \(T>1-c\). The negative-weight regions are disjoint.

The joint ordered-point density is \(6\) on \(0<X_0<X_1<X_2<1\). With \(X_0=u\), \(X_2=u+L\), \(X_1=u+TL\), the Jacobian is \(L\); integration over \(0<L<1\) and \(0<u<1-L\) shows that \(T\) is exactly uniform on \((0,1)\). Hence all coefficients are nonnegative with probability \(1-2c=4-\sqrt{13}\).

Since the weights sum to one, \(A_X=1+2\sum_{i:W_i<0}(-W_i)\). For \(0<T<c\), it is exactly
\[
 A_X=1-2W_0=\frac{1-T+T^{-1}}4,
\]
with the reflected expression on \(1-c<T<1\) and \(A_X=1\) otherwise. This left-tail expression decreases strictly in \(T\). For \(z\ge1\), its unique positive inverse is
\[
 t_z=\frac{\sqrt{(4z-1)^2+4}-(4z-1)}2,
\]
which lies in \((0,c]\). Uniformity and reflection imply \(\mathbb P(A_X>z)=2t_z\), including \(z=1\) because the boundary has zero probability. Rationalizing the expression shows \(z\mathbb P(A_X>z)\to1/2\). Integrating the survival function proves the claimed moment criterion.

For independent centered errors \(\epsilon_i\sim N(0,\sigma^2)\), the conditional noise error is \(\sum_i W_i\epsilon_i\), normally distributed with standard deviation \(\sigma(\sum_iW_i^2)^{1/2}\). As \(T\downarrow0\),
\[
 T W_0\to-\frac18,\qquad T W_1\to\frac18,\qquad T W_2\to0,
\]
so \(\sum_i W_i^2\sim1/(32T^2)\). Consequently the conditional absolute first moment is asymptotic to a positive constant times \(1/T\); its expectation over the uniform \(T\) diverges logarithmically. Likewise the conditional variance is asymptotic to \(\sigma^2/(32T^2)\), whose expectation diverges. Tonelli's theorem applies to both nonnegative conditional moments and completes the assertions.

## Verification

Run `python verify.py` with SymPy 1.14.0. The script independently reconstructs the spline integral from its second-derivative equation, verifies the three symbolic weight identities, affine exactness, the two positivity boundaries, inversion of the exact amplification tail, the asymptotic Pareto coefficient, and the asymptotic squared-noise coefficient. It also performs 360 exact-rational independent checks of the spline integral and normalized nodal-weight representation. The printed success message is supplementary; the identities and probability argument above establish the continuum theorem, not the finite checks.

## Relationship to prior work

The general motivation to enforce positive quadrature weights and to control the sum of their absolute values occurs in Karvonen, Kanagawa and Särkkä (2018) and van den Bos and Sanderse (2019). The former treats Gaussian-process Bayesian quadrature and the latter polynomial-exact interpolatory rules and node extension. Neither establishes the present three-knot **natural cubic spline** cardinal-integral weights or their random-hull distribution. Aràndiga, Baeza and Yáñez (2021) study shape-preserving cubic Hermite interpolants rather than the distribution of integrated natural-spline weights. Ait-Haddou, Bartoň and Calo (2014) develop Gaussian quadrature rules for a \(C^1\) spline space with different nodes, continuity, and exactness requirements. The pointwise overshoot of natural cubic interpolation and the integrated nodal weights are different functionals: pointwise failure alone does not determine the sign probability or exact norm tail of the integrated rule. The present result is specific to three sorted uniform knots and is not a generic statement about all randomly sampled quadrature schemes.

## Limitations

No statement is made about positivity of the interpolating spline between knots, about integration over the fixed interval \([0,1]\), about knot counts other than three, or about other boundary conditions. Infinite expected noise amplification need not imply infinite error for a noiseless smooth integrand, where cancellations may occur. Uniformity of the knot distribution is essential to the exact probability and survival formula; arbitrary node densities would alter it. Earlier equivalent spline-integration distributions may have escaped the targeted literature comparison, so historical priority is not independently established. The algebraic and numerical checks are not an external audit.

## References

- T. Karvonen, M. Kanagawa, S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, first public 2018-12-20, https://arxiv.org/abs/1812.08509.
- L. M. M. van den Bos, B. Sanderse, *A geometrical interpretation of the addition of nodes to an interpolatory quadrature rule while preserving positive weights*, first public 2019-02-20, https://arxiv.org/abs/1902.07477.
- F. Aràndiga, A. Baeza, D. F. Yáñez, *Monotone cubic spline interpolation for functions with a strong gradient*, first public 2021-02-23, https://arxiv.org/abs/2102.11564.
- R. Ait-Haddou, M. Bartoň, V. M. Calo, *Explicit Gaussian quadrature rules for cubic splines with non-uniform knot sequences*, first public 2014-10-27, https://arxiv.org/abs/1410.7196 (supporting comparison for different spline quadrature).
