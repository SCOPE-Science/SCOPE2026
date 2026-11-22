# Three coordinates are minimal for reentrant support under nonnegative ridge regularization

## Finding
For every real symmetric positive-definite \(A\in\mathbb R^{n\times n}\), \(b\in\mathbb R^n\), and \(t\ge0\), define the unique nonnegative ridge solution
\[
x(t)=\arg\min_{x\in\mathbb R^n,\ x\ge0}\left\{\frac12 x^{\mathsf T}(A+tI)x-b^{\mathsf T}x\right\}.
\]
For \(n\le2\), the zero set of every coordinate \(\{t\ge0:x_i(t)=0\}\) is either empty, all of \([0,\infty)\), or an interval adjoining an endpoint of \([0,\infty)\). Thus no coordinate can be positive, vanish, and later become positive again. If \(b\) is componentwise strictly positive, the support for \(n\le2\) is nondecreasing in \(t\).

This dimension barrier is sharp even when \(b>0\) componentwise. Set
\[
A=\begin{pmatrix}3&-1&\frac32\\-1&1&0\\\frac32&0&4\end{pmatrix},
\qquad b=\begin{pmatrix}1\\1\\5\end{pmatrix}.
\]
The unique optimizer has full support exactly for \(0\le t<\frac12\) and \(t>1\), but support \(\{2,3\}\) for \(\frac12\le t\le1\). This loss and reentry occur as the spectral condition number of \(A+tI\) decreases strictly. Moreover, the pattern persists, at three witness parameter values, on an open neighborhood of the stated matrix and vector.

## Assumptions and scope
The parameter \(t\) ranges over all finite real numbers \(t\ge0\). Matrix \(A\) is symmetric positive definite; no sign pattern is assumed for its off-diagonals. The feasible set is the closed nonnegative orthant, and \(b\) may have arbitrary signs in the dimension-two barrier. All equality cases at \(t=\frac12\) and \(t=1\) are included as zeros. Support means strictly positive coordinates of the unique constrained minimizer. The regularization is the isotropic Tikhonov penalty \(\frac t2\|x\|_2^2\), with \(b\) fixed. No claims are made about active-set iterates at a single parameter value.

## Proof
**Two-dimensional obstruction.** For \(n=1\), \(x_1(t)=\max\{b_1,0\}/(a+t)\), so its zero status is independent of \(t\). For \(n=2\), write
\[
A=\begin{pmatrix}a&c\\c&d\end{pmatrix},\qquad a>0,\ d>0,\ ad>c^2.
\]
Fix coordinate one at the boundary. Its unique restricted minimizer has \(x_2=\max(b_2,0)/(d+t)\). The KKT conditions for this restricted minimizer to be the global optimum are exactly
\[
F_1(t):=\frac{c\max(b_2,0)}{d+t}-b_1\ge0.
\]
By strict convexity, this is equivalent to \(x_1(t)=0\), including equality and the case when both coordinates vanish. The function \(F_1\) is monotone (or constant) on \([0,\infty)\), since
\[
F_1'(t)=-\frac{c\max(b_2,0)}{(d+t)^2}.
\]
Its superlevel set is an endpoint interval, empty, or the entire half-line. Interchanging indices proves the same result for coordinate two. When \(b_1,b_2>0\), the eventual sign \(\lim_{t\to\infty} F_i(t)=-b_i<0\) excludes terminal zero rays: coordinates can only enter support as \(t\) grows, never leave.

**Three-dimensional construction.** The leading principal minors of the displayed \(A\) are \(3\), \(2\), and \(23/4\); by Sylvester's criterion, \(A\succ0\). Define
\[
q(t)=(t-\tfrac12)(t-1),\qquad
D(t)=\det(A+tI)=t^3+8t^2+\tfrac{63}{4}t+\tfrac{23}{4}>0.
\]
The unconstrained stationary solution \(u(t)=(A+tI)^{-1}b\) satisfies the exact identities
\[
u_1(t)=\frac{q(t)}{D(t)},\qquad
u_2(t)=\frac{1+u_1(t)}{t+1},\qquad
u_3(t)=\frac{5-\tfrac32 u_1(t)}{t+4}.
\]
Both \(D(t)+q(t)\) and \(D(t)-q(t)\) have strictly positive coefficients as polynomials in \(t\), hence \(-1<u_1(t)<1\) for every \(t\ge0\). Therefore \(u_2(t),u_3(t)>0\) for all such \(t\). For \(t\in[0,\frac12)\cup(1,\infty)\), \(q(t)>0\), so \(u(t)>0\), satisfies the KKT conditions and is the unique constrained minimizer.

For \(\frac12\le t\le1\), set
\[
v(t)=\begin{pmatrix}0\\1/(t+1)\\5/(t+4)\end{pmatrix}.
\]
A direct multiplication yields the reduced gradient
\[
(A+tI)v(t)-b=\begin{pmatrix}-q(t)/[(t+1)(t+4)]\\0\\0\end{pmatrix}\ge0.
\]
Because \(q(t)\le0\) precisely on this interval, \(v(t)\ge0\), the gradient is nonnegative, and complementary slackness holds. Strict convexity again proves unique global optimality. In particular, \(x_1(\frac12)=x_1(1)=0\) with the other coordinates strictly positive.

**Decreasing conditioning and robustness.** The smallest and largest eigenvalues of \(A\) obey \(0<\lambda_{\min}<\lambda_{\max}\), and
\[
\kappa_2(A+tI)=\frac{\lambda_{\max}+t}{\lambda_{\min}+t},\qquad
\kappa_2'(A+tI)=\frac{\lambda_{\min}-\lambda_{\max}}{(\lambda_{\min}+t)^2}<0.
\]
At the three fixed parameters \(t=0,3/4,2\), the KKT solutions are strictly interior, strictly complementary with coordinate one at zero, and strictly interior, respectively. Positive definiteness, the restricted solutions and the strict KKT signs persist under sufficiently small perturbations of \((A,b)\). Thus the same three-point support loss and regain occur throughout an open set. This proves dimension minimality and robustness.

## Verification
The standalone Python/SymPy script `verify_ridge.py` reconstructs the exact matrix inverse and determinant, checks Sylvester minors, positivity of the coefficients of \(D\pm q\), the boundary KKT gradient, and the two-dimensional threshold derivative. It also independently enumerates every possible active set at nine rational values of \(t\), including both transition points. Running `python verify_ridge.py` returns an explicit `VERIFY_OK` result. Exact algebra, rather than finite samples, proves the all-parameter assertions.

## Relationship to prior work
Schmelzer and Stoll (2026, Section 5.1) describe positive-definite regularization and reduced spectral conditioning for nonnegative-conjugate-gradient solvers, and an active-set method at a fixed matrix. Their finite-termination and condition-number results do not imply nested support as the regularization parameter varies. Rojas and Steihaug (2002) and Calvetti et al. (2004) give nonnegative Tikhonov solution methods, not the present sharp dimension-two no-reentry classification and dimension-three exact counterexample. The well-studied variable-entry and exit behavior for \(\ell_1\)-penalized Lasso paths is a different regularization problem and does not entail the quadratic ridge conclusion. The result is a structural diagnostic, not a new implementation of these solvers.

## Limitations
The construction concerns a three-dimensional convex quadratic with mixed-sign off-diagonal entries; matrices with additional positivity or \(M\)-matrix restrictions may behave differently. The theorem does not characterize all regularization paths in dimensions three or higher. It gives an exact counterexample to support nesting and does not assert that any specific numerical algorithm will follow the wrong active set. Possible earlier equivalent examples outside the compared literature remain a priority risk.

## References
1. T. Schmelzer and M. Stoll, *Non-Negative Conjugate Gradients* (2026), first public version July 24, 2026. https://arxiv.org/abs/2607.22121
2. M. L. Rojas and T. Steihaug, *An interior-point trust-region-based method for large-scale non-negative regularization*, Inverse Problems 18 (2002), 1291–1307. https://www.marielbarojas.com/Academic/Docs/rojas-steihaug.pdf
3. D. Calvetti, B. Lewis, L. Reichel, and F. Sgallari, *Tikhonov regularization with nonnegativity constraint*, Electronic Transactions on Numerical Analysis 18 (2004), 153–173. https://www.math.kent.edu/~reichel/publications/tik.constr.pdf
