# A golden-ratio mesh-grading threshold for the total variation of natural cubic step interpolants

## Finding

Fix any real number \(R>0\) and integer \(N\ge2\). Set \(x_0=0\) and \(x_{i+1}-x_i=R^i\) for \(0\le i<N\), and interpolate \(y_0=0\), \(y_i=1\) for \(1\le i\le N\) by the unique natural \(C^2\) cubic spline \(S_{N,R}\) (zero second derivatives at both outer knots). The sampled total variation is exactly \(1\). Define
\[
 s=\sqrt{R^2+R+1},\qquad a=\frac1{1+R+s},\qquad q=Ra^2,\qquad \beta=R^2a,
\]
and
\[
 F(k)=\frac13\max_{0\le t\le1}t(1-t)\big[(2-t)-k(1+t)\big],\qquad 0\le k\le a.
\]
The variation of the spline is exactly
\[
 \boxed{\operatorname{Var}(S_{N,R})=1+\frac6{1-q^N}\sum_{i=1}^{N-1}\beta^i(1-q^{N-i})F\left(a\frac{1-q^{N-i-1}}{1-q^{N-i}}\right).}
\]
Here \(0<a<1/2\), \(0<q<1\), and the scalar maximum is attained at
\[
 t_*(k)=\frac{3-\sqrt{3(1-k+k^2)}}{3(1+k)}\in(0,1).
\]
There is a sharp growth transition at \(R_*=\frac{3+\sqrt5}{2}\), characterized by \(\beta=1\):

For \(0<R<R_*\), the variations converge to the finite value
\[
 \lim_{N\to\infty}\operatorname{Var}(S_{N,R})
 =1+\frac{6\beta F(a)}{1-\beta}.
\]
At \(R=R_*\), the variations grow linearly:
\[
 \operatorname{Var}(S_{N,R_*})=6F(R_*^{-2})N+O(1),\qquad 6F(R_*^{-2})=0.669961782255888\ldots.
\]
For \(R>R_*\), they grow exponentially and have the strictly positive finite asymptotic coefficient
\[
 \lim_{N\to\infty}\beta^{-N}\operatorname{Var}(S_{N,R})
 =6\sum_{j=1}^{\infty}\beta^{-j}(1-q^j)
 F\left(a\frac{1-q^{j-1}}{1-q^j}\right)\in(0,\infty).
\]
Thus a fixed geometric growth ratio exceeding \(R_*\) generates exponential variation amplification from a monotone datum with a single jump, while ratios below \(R_*\) give bounded variation for this datum as the number of cells increases.

## Assumptions and scope

All knots and data are real. The interval is the finite interval \([x_0,x_N]\), with classical continuous total variation \(\operatorname{Var}_{[x_0,x_N]}(S)=\int_{x_0}^{x_N}|S'(x)|\,dx\). The knots are strictly increasing because each width \(R^i\) is positive. Natural cubic interpolation means the unique piecewise polynomial of degree at most three that interpolates the specified values, is globally \(C^2\), and satisfies \(S''(x_0)=S''(x_N)=0\). The limit holds at fixed \(R\) with \(N\to\infty\). No assertion about a sharp full-data operator norm or uniformity as \(R\) depends on \(N\) is made.

## Proof

Let \(h_i=R^i\), \(\delta_i=(y_{i+1}-y_i)/h_i\), and \(M_i=S''(x_i)\). The natural spline equations for \(1\le i<N\) are
\[
 h_{i-1}M_{i-1}+2(h_{i-1}+h_i)M_i+h_iM_{i+1}
 =6(\delta_i-\delta_{i-1}),\qquad M_0=M_N=0.
\]
Here \(\delta_0=1\) and \(\delta_i=0\) for \(i\ge1\); the forcing is \(-6\) at \(i=1\) and zero elsewhere. After dividing the homogeneous recurrence by \(R^{i-1}\), its characteristic polynomial is \(Rz^2+2(1+R)z+1\), with two distinct negative roots \(-a\) and \(-b\), where \(b=(1+R+s)/R\). Since \(a/b=Ra^2=q\), imposing the right boundary condition and the first forcing yields the **exact** curvatures
\[
 M_0=M_N=0,\qquad
 M_i=\frac{6(-a)^i(1-q^{N-i})}{1-q^N},\quad1\le i<N.
\]
Direct substitution into the first equation gives \(-6\), using \(Ra^2-2(1+R)a+1=0\); the remaining equations and the right boundary follow from the characteristic equation. The strict diagonal dominance of the spline system gives uniqueness.

On the first cell, writing \(x=x_0+t\), \(0\le t\le1\), the standard cubic-spline cell formula yields
\[
 S(x)=t+\frac{M_1}{6}(t^3-t),\qquad
 S'(x)=1+\frac{M_1}{6}(3t^2-1).
\]
Because \(M_1<0\) and \(|M_1|<6a<3\), this derivative is everywhere strictly positive, so the first cell contributes exactly \(1\) to variation.

For a later cell \(1\le i<N\), put \(t=(x-x_i)/h_i\) and
\[
 k_i=-M_{i+1}/M_i=a\frac{1-q^{N-i-1}}{1-q^{N-i}}\in[0,a].
\]
Both endpoint values are one, and substitution into the spline cell formula gives
\[
 S(x_i+h_it)-1=-\frac{h_i^2M_i}{6}t(1-t)\big[(2-t)-k_i(1+t)\big].
\]
For \(0\le t\le1\), the bracket is strictly positive because \((2-t)-k_i(1+t)\ge1-2a>0\). The cubic has a single nonzero-signed excursion between its equal endpoints: differentiating the bracketed cubic gives \((2-k_i)-6t+3(1+k_i)t^2\), whose smaller root is \(t_*(k_i)\in(0,1)\), while the larger root exceeds one. Hence its cell variation is twice the absolute excursion:
\[
 \operatorname{Var}_{[x_i,x_{i+1}]}(S)
 =h_i^2|M_i|F(k_i)
 =\frac{6\beta^i(1-q^{N-i})}{1-q^N}F(k_i).
\]
Adding the first and all remaining cells proves the exact finite-size formula.

The map \(R\mapsto\beta=R^2/(1+R+s)\) is strictly increasing: if \(D=1+R+s\), then \(D'=1+(2R+1)/(2s)<2\), so \(\beta'=(2RD-R^2D')/D^2>0\). Solving \(\beta=1\), with its required positive square-root sign, gives precisely \(R_*=(3+\sqrt5)/2\) (the second algebraic root does not satisfy the unsquared equation).

If \(\beta<1\), dominated convergence applies to the finite sum with \(i\) held fixed: \(k_i\to a\) and \((1-q^{N-i})/(1-q^N)\to1\), while every summand is uniformly bounded by a fixed multiple of \(\beta^i\); summing the geometric series gives the subcritical limit. At \(\beta=1\), \(F\) is Lipschitz on \([0,a]\), being the maximum of affine functions of \(k\) with uniformly bounded slopes. The difference between the \(i\)-th summand and \(F(a)\) is \(O(q^{N-i-1})\); the total difference is \(O(1)\) after including the bounded correction from \((1-q^N)^{-1}\). This proves the linear law. For \(\beta>1\), substitute \(j=N-i\), divide by \(\beta^N\), and dominate the terms by a constant times \(\beta^{-j}\). Dominated convergence gives the stated series. Every summand is positive, so its sum is finite and strictly positive. This completes the proof.

## Verification

The accompanying `CHECK.py` implements an independent tridiagonal solve of the natural spline curvature equations, explicitly determines extrema of every cubic cell from its derivative quadratic, and compares the resulting total variation against the closed formula for multiple grading ratios and mesh lengths. It also tests the subcritical limiting value, the critical linear slope, and the supercritical normalized constant. Run `python CHECK.py` using a standard Python 3 installation. These finite numerical checks supplement, but do not replace, the preceding proof. A separate comparison against SciPy's independently implemented natural `CubicSpline` was also performed on representative meshes.

## Relationship to prior work

Natural cubic splines and their basis systems are classical. Dermoune and Preda (2014, arXiv:1403.1388v1) construct natural-spline bases and study noisy-data estimation; the inspected account does not supply this fixed-ratio, increasing-grid variation phase law. Shape-preserving weighted cubic splines provide a different mechanism for controlling overshoot, not the same natural \(C^2\) construction. A published three-knot natural cubic positivity-defect calculation examines one pair of intervals and quantifies its overshoot; the current result instead holds at each fixed \(R\) for every \(N\) and determines a large-\(N\) phase transition. Classical convergence/error research typically concerns smooth data and approximation errors; here the monotone input is a discontinuous step in the expanding-grid limit, and the functional is total variation. These comparisons establish no assertion of exhaustive historical priority.

## Limitations

The statement is specific to a one-sided single-jump nodal dataset, natural boundary conditions, and exactly geometric positive mesh widths. It is not a bound for arbitrary datasets, not an exact full interpolation-operator norm, and not a theorem for free-end or periodic splines. The coefficients are asymptotic with fixed \(R\), without mesh-independent uniformity. Historical priority remains subject to additional full-text review of some older nonuniform-spline literature.

## References

- A. Dermoune and C. Preda, *Estimation of noisy cubic spline using a natural basis*, arXiv:1403.1388v1, first posted 2014-03-06. https://arxiv.org/abs/1403.1388
- *A shape-preserving approximation by weighted cubic splines*, *Journal of Computational and Applied Mathematics* (2012), https://doi.org/10.1016/j.cam.2012.04.001.
- C. A. Hall, *Natural Cubic and Bicubic Spline Interpolation*, *SIAM Journal on Numerical Analysis* (1973), https://doi.org/10.1137/0710088.
- R. K. Beatson, *On the Convergence of Some Cubic Spline Interpolation Schemes* (1986), https://doi.org/10.1137/0723058 (abstract consulted; full text not inspected).
- *A sharp three-knot positivity defect for natural cubic interpolation*, archived mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-sharp-three-knot-positivity-defect-for-natural-cubic-interpola--0b51d8330304 (published summary consulted; complete archived text unavailable in this execution).
