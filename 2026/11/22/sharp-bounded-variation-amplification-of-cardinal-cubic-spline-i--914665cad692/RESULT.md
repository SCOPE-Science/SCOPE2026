# Sharp bounded-variation amplification of cardinal cubic spline interpolation

## Finding

Let \(S\) denote classical cardinal \(C^2\) cubic-spline interpolation at all integer knots on \(\mathbb R\), defined by bounded nodal second derivatives. For every bilateral real sequence of finite discrete variation,
\[
\operatorname{TV}_{\mathbb R}(S y)\le K\,\operatorname{Var}_d(y),
\qquad K=\frac{2+\sqrt3+2\sqrt{2-\sqrt3}}{3}=1.589108995992986\ldots .
\]
The coefficient is optimal and **attained** by every nonzero translated or scaled unit step. Because interpolation is linear and preserves constants, \(K\) also is its exact two-input Lipschitz factor from discrete bounded variation modulo constants to continuous bounded variation modulo constants. A monotone nodal step can therefore acquire about \(58.91\%\) extra total variation from the smooth interpolant.

## Assumptions and scope

Sequences \(y=(y_i)_{i\in\mathbb Z}\) are real, defined at every integer, and satisfy \(\operatorname{Var}_d(y):=\sum_{i\in\mathbb Z}|y_{i+1}-y_i|<\infty\). Such sequences are bounded and have finite limits at both ends. Continuous variation is \(\operatorname{TV}_{\mathbb R}(f)=\sup_{x_0<\cdots<x_m}\sum_{j=1}^m|f(x_j)-f(x_{j-1})|\), over arbitrary finite ordered partitions. The interpolant \(S y\) is \(C^2(\mathbb R)\), cubic on every \([i,i+1]\), takes the values \(y_i\), and has a bounded second derivative. It is the standard cardinal cubic B-spline prefilter interpolant; it is **not** a finite-interval natural or clamped spline. There are no mesh-width or dimensional truncations in the theorem.

## Proof

Write \(\Delta_i=y_{i+1}-y_i\), \(M_i=(S y)''(i)\), and \(q=2-\sqrt3\). Cubic-spline continuity gives the bilateral recurrence
\[
M_{i-1}+4M_i+M_{i+1}=6(\Delta_i-\Delta_{i-1}). \tag{1}
\]
The inverse convolution kernel of the operator on the left is \(g_j=(-q)^{|j|}/(2\sqrt3)\), as verified using \(q^2-4q+1=0\) and \(4-2q=2\sqrt3\). Hence \(M=6g*(\Delta-\operatorname{shift}\Delta)\in\ell^1(\mathbb Z)\). The unique bounded solution of (1) has this form, since the homogeneous roots \(-q\) and \(-q^{-1}\) permit no nonzero bilateral bounded solution. On each cell, with \(0\le t\le1\),
\[
(S y)(i+t)=(1-t)y_i+t y_{i+1}
+\frac{M_i}{6}\big((1-t)^3-(1-t)\big)
+\frac{M_{i+1}}6(t^3-t). \tag{2}
\]
This constructs the unique specified spline; (1) ensures continuous first derivatives at each knot. It is also the standard cardinal cubic B-spline interpolant: the integer samples of the centered cubic B-spline have mask \((1,4,1)/6\), whose bilateral inverse is \(6g\).

**Sharp unit-step calculation.** Let \(u_i=0\) for \(i<0\) and \(u_i=1\) for \(i\ge0\). Only \(\Delta_{-1}=1\). Put \(A=3(1-q)\); solving (1) gives
\[
M_{-1-k}=A(-q)^k,\quad M_k=-A(-q)^k\qquad(k\ge0). \tag{3}
\]
The transition cell \([-1,0]\) is strictly increasing: substituting (3) into (2) yields derivative \(1+(A/6)(-1+6t-6t^2)>0\), so its total variation is one. For each right-hand constant-data cell \([k,k+1]\),
\[
(Su)(k+t)-1=\frac A6(-q)^k F(t),\quad
F(t)=t(1-t)\big((2-q)-(1+q)t\big). \tag{4}
\]
Here \(F\ge0\) on \([0,1]\), vanishes only at the ends, and has a unique interior maximum at
\[
t_* =\frac{1-\sqrt q}{1+q},\qquad H=F(t_*)=\frac{\sqrt3-1+2\sqrt q}{6}. \tag{5}
\]
Thus each such cell contributes \((A/3)q^k H\) to the continuous total variation. Reflection \((Su)(x)+(Su)(-1-x)=1\) makes the left tail identical. Summing both tails and using \(A=3(1-q)\),
\[
\operatorname{TV}_{\mathbb R}(Su)
=1+2\sum_{k=0}^\infty\frac A3q^k H
=1+2H=\frac{2+\sqrt3+2\sqrt{2-\sqrt3}}3. \tag{6}
\]
The geometric series converges absolutely, giving an actual infinite-domain extremizer rather than a finite-window approximation.

**Universal bound.** Every finite-variation sequence has the uniformly absolutely convergent representation
\[
y_i=y_{-\infty}+\sum_{j\in\mathbb Z}\Delta_j\,\mathbf1_{\{i>j\}}.
\]
Cardinal interpolation is linear, translation equivariant and preserves constants. By (1)-(2) the associated series of interpolated steps converges locally in \(C^1\), and for every finite sum the total-variation triangle inequality and (6) give variation at most \(K\sum_j|\Delta_j|\). Taking limits through finite partitions yields \(\operatorname{TV}_{\mathbb R}(Sy)\le K\operatorname{Var}_d(y)\). Equality for the single step (6) proves sharpness. Applying this to the sequence \(x-y\) proves the two-input formulation.

## Verification

The self-contained standard-library script `check_cardinal_bv.py` checks the inverse recurrence for translated steps, algebraic peak and constant identities at high decimal precision, exact-form cubic-cell variation using its derivative roots, and deterministic finite-step superpositions. Its finite-cell and random-data tests supplement the analytical bilateral proof; they do not certify its infinite quantifiers. Run: `python3 check_cardinal_bv.py`.

## Relationship to prior work

The cubic B-spline sample mask and prefiltering construction appear in Percan, Zellmann and Lang (2014), *Asymptotic error of cubic B-spline interpolation using prefiltering*. Their object matches the cardinal interpolation construction, but their results treat asymptotic reconstruction errors, not a sharp BV operator norm or all-input attaining steps. Zhang and Martin (1997), *Convergence and Gibbs' phenomenon in cubic spline interpolation of discontinuous functions*, study step-like nodal data, overshoot, and ringing for finite-interval complete cubic splines with clamped endpoint conditions. Their sharp overshoot is not the sum of all oscillation contributions on the bilateral cardinal spline, and no equivalence to the present global BV norm is asserted. Searches of relevant published mathematical records and nearby spline results identified no statement implying the present formula; this absence is not proof of historical uniqueness.

## Limitations

The result concerns unit-spaced, real, bi-infinite, bounded-second-derivative \(C^2\) cardinal cubic interpolation. It does not state the sharp BV norm for a finite interval with natural/not-a-knot/clamped boundary conditions, nonuniform meshes, other spline orders or nonlinear shape-preserving reconstructions. The proof is analytic, with independent mathematical audit not performed. Relevant earlier unpublished or unindexed equivalent formulas might remain undiscovered.

## References

- E. Percan, S. Zellmann and S. Lang, *Asymptotic error of cubic B-spline interpolation using prefiltering*, published online November 30, 2014, DOI: https://doi.org/10.1007/s11075-014-9941-x. The public PDF contains the prefilter equations.
- R. Zhang and K. Martin, *Convergence and Gibbs' phenomenon in cubic spline interpolation of discontinuous functions*, Journal of Computational and Applied Mathematics 87 (1997), 359–371, DOI: https://doi.org/10.1016/S0377-0427(97)00199-4.
