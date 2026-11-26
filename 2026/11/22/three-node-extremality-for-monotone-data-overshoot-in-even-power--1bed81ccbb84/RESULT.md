# Three-node extremality for monotone-data overshoot in even-powered generalized Floater–Hormann interpolation

## Finding
For every even integer \(\gamma\ge2\), every \(n\ge1\), and every nondecreasing real dataset \(m\le y_0\le\cdots\le y_n\le M\) on equally spaced nodes, the degree-one generalized Floater–Hormann interpolant \(R_{n,\gamma}y\) satisfies the **sharp all-grid range enclosure**
\[
m-\delta_\gamma(M-m)\ \le\ (R_{n,\gamma}y)(x)\ \le\ M+\delta_\gamma(M-m),\qquad x\in[x_0,x_n],
\]
where
\[
\delta_\gamma=\max_{0\le t\le1}\frac{(1-t)t^\gamma}{t^\gamma+(2-t)^\gamma}.
\]
The same constant works simultaneously for *every* finite equispaced grid and is attained for three nodes with step data. If \(m<M\), both inequalities are strict on any fixed grid having at least four nodes. When \(m=M\), the data and interpolant are identically \(m\). Thus the maximal monotone-data overshoot of the entire even-power degree-one family is controlled by its first nontrivial three-node instance.

The three-node constant may equivalently be expressed through the unique \(r_\gamma\in(0,1)\) solving
\[
\gamma(1-r_\gamma^2)=2r_\gamma(1+r_\gamma^\gamma),\qquad
\delta_\gamma=\frac{(1-r_\gamma)r_\gamma^\gamma}{(1+r_\gamma)(1+r_\gamma^\gamma)}.
\]
For \(\gamma=2\), \(\delta_2=0.06744224886812295\ldots\). For positive nondecreasing samples with minimum \(m\) and maximum \(M\), the sharp universal guarantee is strict positivity for \(M/m<1+1/\delta_\gamma\) and nonnegativity for \(M/m\le1+1/\delta_\gamma\). Three-node data can attain zero at the threshold and a negative value above it.

## Assumptions and scope
We use nodes \(x_j=a+jh\), \(0\le j\le n\), with \(h>0\), integer \(n\ge1\), and even integer \(\gamma\ge2\). By an affine change of abscissa let \(x_j=j\). For each interval let
\[
 p_i(x)=(i+1-x)y_i+(x-i)y_{i+1},\qquad
 w_i(x)=\frac1{(x-i)^\gamma(x-i-1)^\gamma},\quad 0\le i<n.
\]
Away from the nodes, \(w_i(x)>0\) and
\[
(R_{n,\gamma}y)(x)=\frac{\sum_{i=0}^{n-1}w_i(x)p_i(x)}{\sum_{i=0}^{n-1}w_i(x)}.
\]
At nodes take the continuous interpolating limit. This is the \(d=1\) member of the generalized Floater–Hormann family of Themistoclakis and Van Barel, not the classical \(\gamma=1\) method. We consider the range of real, nondecreasing sampled data; no assertion is made for arbitrary nonmonotone data, nonequispaced nodes, higher polynomial blending degree, or odd \(\gamma\).

## Proof
**Step 1 (reduce monotone data to jumps).** Affine normalization of values reduces to \(0\le y_0\le\cdots\le y_n\le1\). Write \(e^{(k)}_i=\mathbf1_{\{i\ge k\}}\) for \(1\le k\le n\). Then
\[
y=y_0\mathbf1+\sum_{k=1}^n(y_k-y_{k-1})e^{(k)};
\]
the displayed nonnegative coefficients have sum \(y_n\le1\). Linearity and constant reproduction reduce the range assertion to the step functions \(F_k(x):=(R_{n,\gamma}e^{(k)})(x)\).

**Step 2 (a local two-weight bound).** Fix a nonnodal point \(x=j+t\) with \(0\le j<n\) and \(0<t<1\), and denote \(W=\sum_{i=0}^{n-1}w_i(x)\). If \(k=j+1\), then
\[
F_k(x)=\frac{t w_j+\sum_{i=j+1}^{n-1}w_i}{W}\in[0,1].
\]
If \(k\ge j+2\), only the interval \(i=k-1\) contributes a negative extrapolation from its local interpolating line; intervals \(i\ge k\) contribute \(1\), and all earlier intervals contribute zero. Therefore, with \(s=k-1-x\ge1-t\),
\[
F_k(x)=\frac{-s w_{k-1}+\sum_{i=k}^{n-1}w_i}{W}\ge -\frac{s w_{k-1}}{W}\ge-\frac{s}{1+w_j s^\gamma(s+1)^\gamma}.
\]
The last inequality uses \(W\ge w_j+w_{k-1}\), with distinct indices, and \(w_{k-1}=1/[s^\gamma(s+1)^\gamma]\).

**Step 3 (the distant jump cannot be worse).** Put \(A=[t^\gamma(1-t)^\gamma]^{-1}\) and \(H(s)=s/[1+A s^\gamma(s+1)^\gamma]\). Direct differentiation gives
\[
\operatorname{sgn}H'(s)=\operatorname{sgn}\Big(1-A s^\gamma(s+1)^{\gamma-1}\big((2\gamma-1)s+\gamma-1\big)\Big).
\]
For \(s\ge1-t\), the subtracted positive expression is nondecreasing in \(s\) and at \(s=1-t\) equals
\[
\frac{(2-t)^{\gamma-1}\big((2\gamma-1)(1-t)+\gamma-1\big)}{t^\gamma}\ge1
\]
because \(\gamma\ge2\), \(0<t<1\). Hence \(H\) is decreasing on \([1-t,\infty)\), and
\[
F_k(x)\ge-H(1-t)=-\frac{(1-t)t^\gamma}{t^\gamma+(2-t)^\gamma}\ge-\delta_\gamma.
\]
For \(k\le j\), the step function is a pointwise nonnegative blend of local extrapolants, so \(F_k\ge0\). Reflection \(x\mapsto n-x\), together with complementing and reversing the step data, gives \(1-F_k(x)=F_{n-k+1}(n-x)\); the latter is bounded below by \(-\delta_\gamma\). Thus \(F_k(x)\le1+\delta_\gamma\). All three cases imply \(-\delta_\gamma\le F_k(x)\le1+\delta_\gamma\), and Step 1 concludes the range enclosure.

**Step 4 (sharpness and finite-grid rigidity).** For \(n=2\), data \((0,0,1)\) and \(0<x=t<1\), the formula reduces exactly to
\[
(R_{2,\gamma}y)(t)=-\frac{(1-t)t^\gamma}{t^\gamma+(2-t)^\gamma}.
\]
At its unique maximizer in absolute value this equals \(-\delta_\gamma\); reversal and complementation of the data produces \(1+\delta_\gamma\) at the reflected abscissa. If \(n\ge3\), then in the negative-jump case \(W>w_j+w_{k-1}\) because at least one further positive blending weight is present. Every step interpolant lies strictly between \(-\delta_\gamma\) and \(1+\delta_\gamma\), by this observation, reflection, and the nodal values. The normalized dataset is a convex combination of these step datasets and the constant datasets 0 and 1, so its interpolant satisfies the same strict inequalities. Compactness in the abscissa and the finitely many step datasets gives a strict improvement of the defect on each fixed grid with \(n\ge3\). Normalization uses \(m<M\); when \(m=M\), constant reproduction applies directly.

The interior maximizer is unique: substituting \(r=t/(2-t)\in(0,1)\) in the derivative equation gives \(\gamma(1-r^2)=2r(1+r^\gamma)\), whose left side is strictly decreasing and right side strictly increasing. For positive monotone samples with extrema \(m,M\), the lower bound is \(m-\delta_\gamma(M-m)\). This is positive below the stated threshold, zero at it, and negative above it. The three-node data \((m,m,M)\) make the lower bound exact, proving the two guarantees and their sharpness.

## Verification
The attached `verify.py` reproduces the original blend formula using rational arithmetic for all jump datasets on grid lengths \(2\le n\le12\), even powers \(\gamma=2,4,6,8\), and 28 distinct interior rational points per cell. It also checks symbolic differentiation of the three-node extremizer and high-precision root values. Output from the packaged verifier: `Exact rational ... PASS` and `Exact three-node step extremal profile: PASS`. The **proof of the all-grid theorem is Steps 1–4**, not these finite tests.

## Relationship to prior work
Themistoclakis–Van Barel (2023, arXiv:2307.05345) introduce generalized Floater–Hormann interpolation and prove uniformly bounded Lebesgue constants for \(\gamma>1\) on quasi-uniform meshes. Their follow-up (first published September 17, 2024) develops error estimates on arbitrary meshes. These results do not give the exact monotone-data range constant or establish three-node extremality over all equispaced grid lengths. A separate exact [three-site analysis](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-three-site-stability-and-a-mesh-power-boundary-layer-for-g--885bf8a5c599/RESULT.md) gives the same \(\delta_\gamma\) and the centered three-site extremizer; neither fact is claimed as new here. The added mathematical content is the global \(n\)-independent inequality and strict nonattainment of the normalized defect on every grid of four or more nodes. Classical degree-one Floater–Hormann interpolation (\(\gamma=1\)) and Berrut interpolation are different operators; their known sharp monotone overshoot results do not imply the even-power bound.

## Limitations
The bound is only for nondecreasing real data on equally spaced knots and even integer power with blending degree one. The all-grid constant is attained by a three-node step dataset; on larger finite grids only a smaller (not computed here) defect is possible. The result is a precise shape-boundary guarantee, **not** a proof that the interpolated function is monotone. It does not establish novel values for the three-site constants, which are prior. External historical priority of the all-grid extension has not been independently certified.

## References
1. W. Themistoclakis and M. Van Barel, *A generalization of Floater–Hormann interpolants*, arXiv:2307.05345, first submitted July 11, 2023, https://arxiv.org/abs/2307.05345.
2. W. Themistoclakis and M. Van Barel, *A note on generalized Floater–Hormann interpolation at arbitrary distributions of nodes*, *Numerical Algorithms*, first published September 17, 2024, https://doi.org/10.1007/s11075-024-01933-6.
3. M. S. Floater and K. Hormann, *Barycentric rational interpolation with no poles and high rates of approximation*, *Numerische Mathematik* 107 (2007), https://doi.org/10.1007/s00211-007-0093-y.
