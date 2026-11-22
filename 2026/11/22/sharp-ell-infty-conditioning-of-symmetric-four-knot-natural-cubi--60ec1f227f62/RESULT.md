# Sharp \(\ell^\infty\) conditioning of symmetric four-knot natural cubic interpolation

## Finding
Let \(r>0\) and let \(S_r:\mathbb R^4\to C([0,2+r])\) be the natural cubic interpolant at the four sites \(0,1,1+r,2+r\): it interpolates all four nodal data, is piecewise cubic and \(C^2\), and has zero second derivative at both endpoints. Its sharp sup-norm noise amplification, or Lebesgue constant, is
\[
\boxed{\Lambda(r)=\sup_{\|y\|_{\ell^\infty}\le1}\|S_ry\|_{L^\infty}
=\max\left\{1+\frac{4(r+1)}{3\sqrt3\,r(3r+2)},\quad 1+\frac{3r^2}{2(3r+2)}\right\}.}
\]
Among **all reflected-symmetric four-knot meshes**, up to translation and positive scaling, there is exactly one optimal middle-to-outer gap ratio \(r_*\), the unique positive solution of
\[
\boxed{9\sqrt3\,r_*^3=8(r_*+1).}
\]
Numerically \(r_*=1.01048320579748\ldots\), and \(\Lambda(r_*)=1.30440818854744\ldots\), strictly less than the equally spaced value \(\Lambda(1)=1+8/(15\sqrt3)=1.30792014356780\ldots\). The maximal amplification on the outer cells and on the middle cell is equal exactly at \(r=r_*\). The corresponding sharp worst-case overshoot of the range \([0,1]\), for arbitrary nodal data in that range, is \((\Lambda(r)-1)/2\).

## Assumptions and scope
Every mesh in the optimization class has successive positive gap lengths proportional to \((1,r,1)\). The four measurements are arbitrary independent real nodal values; there is no constraint of monotonicity or differentiability on the underlying measured signal. The norm compares the continuous interpolated output on the **closed knot interval** with the \(\ell^\infty\) magnitude of the four inputs. The theorem makes no claim of global optimality among asymmetric meshes or among other spline boundary conditions. No extrapolation beyond the knot interval is included.

## Proof
Write the nodal data as \(y_0,y_1,y_2,y_3\), and let \(M_i=S_r''(x_i)\). Natural boundary conditions give \(M_0=M_3=0\), and the \(C^2\) matching equations are
\[
\begin{pmatrix}2(1+r)&r\\r&2(1+r)\end{pmatrix}
\begin{pmatrix}M_1\\M_2\end{pmatrix}
=6\begin{pmatrix}(y_2-y_1)/r-(y_1-y_0)\\(y_3-y_2)-(y_2-y_1)/r\end{pmatrix}.
\]
The determinant is \((r+2)(3r+2)>0\). On cell \([x_j,x_{j+1}]\), with local coordinate \(t=(x-x_j)/(x_{j+1}-x_j)\) and length \(h_j\), the natural spline is exactly
\[
(1-t)y_j+ty_{j+1}+\frac{h_j^2}{6}\left[M_j((1-t)^3-(1-t))+M_{j+1}(t^3-t)\right].
\]
Let \(\ell_i(x)=S_re_i(x)\) denote the four cardinal splines; they sum to one at every \(x\). On the left cell, direct substitution gives
\[
\begin{aligned}
\ell_0&=\frac{(1-t)[3r^2+8r+4-2(r+1)(t+t^2)]}{(r+2)(3r+2)},\\
\ell_1&=\frac{t[3r^2+4r+1-(2r+1)t^2]}{r(3r+2)},\\
\ell_2&=\frac{(r+1)t(t^2-1)}{r(3r+2)},\\
\ell_3&=\frac{rt(1-t^2)}{(r+2)(3r+2)}.
\end{aligned}
\]
For every \(r>0\), \(0\le t\le1\), the signs are respectively nonnegative, nonnegative, nonpositive, nonnegative. Indeed the first bracket is at least \(3r^2+4r\), and the second at least \(3r^2+2r\). Consequently the left-cell Lebesgue function is \(1-2\ell_2\), maximized at \(t=1/\sqrt3\). Its maximum is
\[
O(r)=1+\frac{4(r+1)}{3\sqrt3\,r(3r+2)}.
\]
The right cell has the same maximum by reflection.

On the middle cell, with \(0\le t\le1\), direct substitution shows \(\ell_0,\ell_3\le0\), \(\ell_1,\ell_2\ge0\), and
\[
\ell_0+\ell_3=-\frac{3r^2t(1-t)}{3r+2}.
\]
To verify the signs: the factors of \(\ell_0\) and \(\ell_3\) have the forms
\[
\ell_0=\frac{r^2t(1-t)[(3r+4)-(3r+2)t]}{-(r+2)(3r+2)},\qquad
\ell_3=-\frac{r^2t(1-t)[(3r+2)t+2]}{(r+2)(3r+2)};
\]
the square bracket in the first expression is at least \(2\). The other cardinal coefficients equal
\[
\ell_1=\frac{(t-1)[3r^2t(t-1)+r(2t^2-t-3)-2]}{3r+2},\quad
\ell_2=\frac{-t[3r^2t(t-1)+r(2t^2-3t-2)-2]}{3r+2},
\]
whose brackets are strictly negative. Thus the middle-cell Lebesgue function is
\[
1-2(\ell_0+\ell_3)=1+\frac{6r^2t(1-t)}{3r+2},
\]
with unique interior maximum at \(t=1/2\), giving
\[
C(r)=1+\frac{3r^2}{2(3r+2)}.
\]
This proves the exact formula \(\Lambda(r)=\max\{O(r),C(r)\}\).

The function \(O(r)\) decreases strictly from infinity to one, while \(C(r)\) increases strictly from one to infinity. Their unique crossing is the global and unique minimizer of their maximum. Clearing their positive denominators gives exactly \(9\sqrt3r^3=8(r+1)\). Thus the stated sharp minimum and its location follow; no numerical argument is used for uniqueness.

For fixed \(x\), maximizing \(|\sum_i\ell_i(x)y_i|\) over \(|y_i|\le1\) yields \(\sum_i|\ell_i(x)|\) by choosing the four data signs. Since \(\sum_i\ell_i(x)=1\), maximizing \(S_ry(x)-1\) over \(0\le y_i\le1\) gives \(\sum_{\ell_i(x)>0}\ell_i(x)-1=(\sum_i|\ell_i(x)|-1)/2\). This proves both the sharp operator norm interpretation and the range-escape statement.

## Verification
The accompanying `verify.py` reconstructs the natural-spline second-derivative system and all cardinal pieces symbolically; verifies the crucial identities, root equation and strictly monotone branch derivatives; and checks the alternative direct spline formula over an exact rational sample grid. Running `python verify.py` with Python 3 and SymPy 1.14 or compatible is sufficient; its recorded output is in `verification_output.txt`. The infinite-dimensional quantifiers and global minimax are justified by the analytic sign and monotonicity argument above, not by finite tests. Numerical values are only approximations to exactly defined algebraic quantities.

## Relationship to prior work
Saeidian, Sarfraz, Azizi and Jalilian (2021) investigate constrained shape-preserving cubic Hermite interpolation, motivating control of range escape, but their adjustable derivatives and constrained constructions differ from a fixed natural cubic interpolant. Amat, Levin, Ruiz-Álvarez, Trillo and Yáñez (2022) analyze nonlinear \(C^2\) quasi-interpolating splines for Gibbs suppression, rather than sharp \(\ell^\infty\) operator norms of a four-knot natural interpolant. Beatson and Chacko (1990/1992) calculate and compare norms of eight cubic spline schemes, including the natural end condition, on uniform and randomized meshes; their inspected formulation and tables do not supply this symbolic four-knot minimax ratio. Related published mathematical records derive sharp **total-variation** stability for the same four-knot spline family, but that seminorm acts on *increments* and is not equivalent to the present \(\ell^\infty\)-to-\(L^\infty\) operator norm. In particular the reported variation-optimal middle-gap ratio \(1.4288255\ldots\) has present Lebesgue factor \(1.4871271\ldots\), far above \(1.3044081\ldots\). Polynomial four-node interpolation and three-knot natural cubic interpolation also define different operators. These comparisons are evidence of distinction, not a proof of bibliographic uniqueness.

## Limitations
The result is a closed-form solution only within the symmetric four-knot natural cubic family, not an all-knot global optimum. The improvement over equal spacing is small (about \(0.27\%\) in the norm) but the exact minimax geometry is stable and differs markedly from variation-optimal geometry. The unconditional range bound is sharp but does not guarantee the spline preserves positivity or monotonicity for every datum. The related published mathematical record was available in summary form rather than full text, so historical priority is provisional; independent scientific review has not been performed.

## References
- J. Saeidian, M. Sarfraz, A. Azizi and S. Jalilian, *A New Approach of Constrained Interpolation Based on Cubic Hermite Splines*, Journal of Mathematics (2021), DOI: [10.1155/2021/5925163](https://doi.org/10.1155/2021/5925163), first public 2021-08-31.
- S. Amat, D. Levin, J. Ruiz-Álvarez, J. C. Trillo and D. F. Yáñez, *A class of \(C^2\) quasi-interpolating splines free of Gibbs phenomenon*, Numerical Algorithms 91 (2022), 51–79, DOI: [10.1007/s11075-022-01254-6](https://doi.org/10.1007/s11075-022-01254-6), first public 2022-02-25.
- R. K. Beatson and E. Chacko, *Which Cubic Spline Should One Use?*, preprint 1990, SIAM Journal on Scientific and Statistical Computing 13 (1992), 1009–1024, DOI: [10.1137/0913059](https://doi.org/10.1137/0913059), [open full text](https://files01.core.ac.uk/download/pdf/35472972.pdf).
- H.-J. Rack and R. Vajda, *Optimal cubic Lagrange interpolation: Extremal node systems with minimal Lebesgue constant*, Studia Universitatis Babeș-Bolyai Mathematica (2015), [journal page](https://studia.reviste.ubbcluj.ro/index.php/subbmathematica/article/view/5710).
- Published mathematical record: *Unique variation-optimal symmetric four-knot natural cubic interpolation*, [record](https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-unique-variation-optimal-symmetric-four-knot-natural-cubic-inter--a68c76ffcd7c) (2026).
