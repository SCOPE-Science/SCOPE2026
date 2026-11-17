# Sharp bounded-variation amplification and jump localization for quadratic least-squares projection

## Finding
For every integer \(n\ge3\), let \(P_n:\mathbb R^n\to\mathbb R^n\) be the ordinary Euclidean orthogonal projection onto sampled polynomials of degree at most two at \(n\) equally spaced real sites. Equip the data with the adjacent total-variation seminorm
\[
V_n(y)=\sum_{j=0}^{n-2}|y_{j+1}-y_j|.
\]
The sharp quotient-space norm \(C_n=\sup_{V_n(y)>0}V_n(P_ny)/V_n(y)\) is **exactly**, using only rational arithmetic,
\[
\boxed{C_n=\max_{1\le k<n}\frac{6k(n-k)}{n(n^2-1)}
\sum_{j=0}^{n-2}\left|1+\frac{5(2k-n)(2j-n+2)}{n^2-4}\right|.}\tag{1}
\]
Every finite-grid maximum is attained by a one-jump vector \(y_j=\mathbf1_{\{j\ge k\}}\), and formula (1) costs \(O(n^2)\) rational arithmetic operations. In particular, \(C_3=1\), \(C_4=13/10\), \(C_5=44/35\), \(C_6=9/7\), \(C_7=55/42\), and \(C_8=29/21\).

As the number of observations increases, these sharp coefficients converge to the explicitly algebraic number
\[
\boxed{\lim_{n\to\infty}C_n=\Lambda
=\frac{6t_*(t_*-1)(50t_*^2-50t_*+13)}{5(2t_*-1)}
=1.63318209583481\ldots,}\tag{2}
\]
where
\[
\boxed{t_*=\frac12-\frac{\sqrt3}{30}\sqrt{12+\sqrt{69}}
=0.239829390188425\ldots.}\tag{3}
\]
If \(k_n\) is **any** sequence of maximizing jump indices for formula (1), then
\[
\boxed{\operatorname{dist}\!\left(k_n/n,\{t_*,1-t_*\}\right)\longrightarrow0.}\tag{4}
\]
Thus quadratic least-squares smoothing amplifies variation by a factor exceeding \(1.63\) in large samples; its asymptotically worst single jumps occur strictly inside the observation interval, not at its endpoints or midpoint.

## Assumptions and scope
All inputs and outputs are real, node weights are equal, the sites are ordered and equally spaced, and the fitted space consists of all polynomials of degree at most two. There is no positivity or monotonicity constraint on the fitted polynomial. The seminorm annihilates constants, and the projection reproduces constants, so the operator norm on the quotient by constants is well-defined. The supremum is over distinct input pairs equivalently over a single nonconstant difference, since the projection is linear. Formula (1) requires \(n\ge3\); for \(n=3\) the projector is the identity. Formula (2) concerns the limit as the number of observation nodes grows with fixed polynomial degree.

## Proof
**1. Reduction to jumps.** Write \(H^{(k)}_j=\mathbf1_{\{j\ge k\}}\), \(1\le k<n\). Every vector \(y\) has the exact decomposition
\[
y=y_0\mathbf1+\sum_{k=1}^{n-1}(y_k-y_{k-1})H^{(k)},
\qquad V_n(y)=\sum_{k=1}^{n-1}|y_k-y_{k-1}|.
\]
Since \(P_n\mathbf1=\mathbf1\), the triangle inequality implies \(V_n(P_ny)\le\max_k V_n(P_nH^{(k)})V_n(y)\). Each jump has unit variation; hence equality holds in the operator norm and some one-jump input attains it.

**2. Closed finite-grid formula.** Index the nodes by \(j=0,\ldots,n-1\), set \(u_j=j-(n-1)/2\), and \(q_j=u_j^2-(n^2-1)/12\). The mutually orthogonal sampled polynomials \(1,u,q\) have squared Euclidean norms
\[
\|1\|_2^2=n,\quad \|u\|_2^2=\frac{n(n^2-1)}{12},\quad
\|q\|_2^2=\frac{n(n^2-1)(n^2-4)}{180}.
\]
For the step \(H^{(k)}\), direct summation yields
\[
\langle H^{(k)},u\rangle=\frac{k(n-k)}2,\qquad
\langle H^{(k)},q\rangle=\frac{k(n-k)(2k-n)}6.
\]
The successive differences of its projected polynomial are consequently
\[
(P_nH^{(k)})_{j+1}-(P_nH^{(k)})_j
=\frac{6k(n-k)}{n(n^2-1)}\left[1+
\frac{5(2k-n)(2j-n+2)}{n^2-4}\right].
\]
Taking absolute values, summing and maximizing over the unit jumps proves (1), with no unverified combinatorial enumeration.

**3. Continuum limiting problem.** Map nodes affinely to \(x_j=j/(n-1)\). For each \(t\in[0,1]\), write \(h_t(x)=\mathbf1_{\{x\ge t\}}\) and let \(Qh_t\) be its \(L^2([0,1],dx)\)-orthogonal projection onto \(\operatorname{span}\{1,x,x^2\}\). Direct integration of the three moments gives
\[
q_t(x)=(Qh_t)(x)
=(1-t)\big[(10t^2-8t+1)+12t(3-5t)x+30t(2t-1)x^2\big].\tag{5}
\]
Reflection gives \(\operatorname{TV}(q_t)=\operatorname{TV}(q_{1-t})\). For \(0\le t\le2/5\), the quadratic has its maximum at \(x=(5t-3)/(5(2t-1))\in[0,1]\), so its variation equals \(2q_t(x)-q_t(0)-q_t(1)\). For \(2/5\le t\le1/2\), it is increasing on \([0,1]\). The resulting exact function is
\[
\operatorname{TV}(q_t)=
\begin{cases}
\displaystyle \frac{6t(t-1)(50t^2-50t+13)}{5(2t-1)},&0\le t\le2/5,\\[4pt]
6t(1-t),&2/5\le t\le1/2,
\end{cases}\tag{6}
\]
extended to \(1/2\le t\le1\) by reflection. At \(t=0\), use the continuous limiting value zero.

**4. Exact maximum and uniqueness.** On \([0,2/5]\), differentiating the first expression in (6) yields
\[
\frac{6(300t^4-600t^3+426t^2-126t+13)}{5(2t-1)^2}.
\]
Its only two zeros in that interval are
\[
t_*=\frac12-\frac{\sqrt3}{30}\sqrt{12+\sqrt{69}},\qquad
s_*=\frac12-\frac{\sqrt3}{30}\sqrt{12-\sqrt{69}}.
\]
The first is a strict local maximum, the second a strict local minimum. The endpoint values of this branch are \(0\) and \(36/25\); the remaining branch is at most \(3/2\). But the first branch at \(t=1/4\) already equals \(261/160>3/2\). Thus the *only* global maximizers are \(t_*\) and \(1-t_*\), establishing the exact value \(\Lambda\).

**5. Uniform passage from grids to the limit.** Let \(t=k/n\). The empirical moment matrix for the polynomial basis \((1,x,x^2)\) at \(x_j=j/(n-1)\) differs by \(O(n^{-1})\) from the invertible continuous Hilbert moment matrix \((1/(a+b+1))_{a,b=0}^2\). The corresponding three step moments differ by \(O(n^{-1})\), *uniformly* over \(1\le k<n\), from \(((1-t^{a+1})/(a+1))_{a=0}^2\). Matrix inversion is uniformly stable near that limiting positive-definite matrix, so the coefficients of the discrete fitted step polynomial differ by \(O(n^{-1})\) from (5), uniformly in \(k\). The variation of a degree-two polynomial on the sampled grid differs from its interval variation by \(O(n^{-1})\), uniformly for bounded coefficients: integrate its affine derivative on each cell and use the derivative's uniform Lipschitz bound. Therefore
\[
\sup_{1\le k<n}\big|V_n(P_nH^{(k)})-\operatorname{TV}(q_{k/n})\big|=O(n^{-1}).
\]
The grid \(\{k/n\}\) becomes dense in \([0,1]\), so (2) follows. The uniqueness of the continuum maximizers, continuity of (6), and this uniform estimate force every maximizing sequence to satisfy (4).

## Verification
Execute `python3 verify_quadratic_bv.py` from this package. It independently computes the fitted vectors by exact inversion of the three-by-three monomial Gram matrix, comparing 464 step cases with (1); checks the stated small dimensions, exact inequalities on arbitrary rational inputs, and exact continuous step moment identities. Floating-point diagnostics check the algebraic maximizer and sample-size convergence only. The infinite-dimensional limit, uniqueness, and all-grid norm identity follow from the analytic proof above, not from the finite checker.

## Relationship to prior work
Classical work on discrete least-squares approximation establishes the polynomial projection and its sampling stability in Euclidean and reconstruction norms. In particular, Bos–Calvi–Levenberg–Sommariva–Vianello (2009) discuss discrete least-squares schemes and weakly admissible meshes, and Cohen–Davenport–Leviatan (2011) study stable and accurate polynomial reconstruction and equispaced sampling; neither inspected full text asserts a sharp adjacent-variation operator norm at fixed quadratic degree. Nochetto–Salgado (2012) construct a different, specially designed finite-element interpolant that *does* diminish total variation; its result does not cover the ordinary quadratic least-squares projector.

The closest indexed quadratic-projector comparisons concern sharp *pointwise* range overshoot for monotone inputs under Jacobi weighting, and sharp *endpoint evaluation* sensitivity on uniform grids. Their theorems do not imply (1)–(4), because the output quantity here is the sum of absolute adjacent changes, and the worst output quadratic can reverse direction within the interval; neither pointwise nor endpoint bounds yield the attained sharp variation constant. The continuum extremizers are interior jumps, rather than the boundary-evaluation kernel sign inputs. This distinction does not establish exhaustive historical priority.

## Limitations
Only real, equally weighted, nonperiodic uniform grids and quadratic least squares are analyzed. Formula (1) is an exact finite optimization, not a single closed rational expression in \(n\). The limit and localization concern growing sample count, not increasing polynomial degree, nonuniform weights, or arbitrary multidimensional designs. No assertion of independent validation or exhaustive priority verification is made. An unindexed older calculation of this particular variation norm remains possible.

## References
- L. Bos, J.-P. Calvi, N. Levenberg, A. Sommariva and M. Vianello, *Geometric Weakly Admissible Meshes, Discrete Least Squares Approximations and Approximate Fekete Points*, arXiv:0902.0215, first public version 2009-02-02. https://arxiv.org/abs/0902.0215
- A. Cohen, M. A. Davenport and D. Leviatan, *On the Stability and Accuracy of Least Squares Approximations*, arXiv:1111.4422, first public version 2011-11-18. https://arxiv.org/abs/1111.4422
- K. A. Kopotun, D. Leviatan, A. Prymak and I. A. Shevchuk, *Uniform and Pointwise Shape Preserving Approximation by Algebraic Polynomials*, arXiv:1109.0968, first public version 2011-09-05. https://arxiv.org/abs/1109.0968
- R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069, first public version 2012-11-05. https://arxiv.org/abs/1211.1069
- *Sharp two-branch monotone range envelope for quadratic symmetric Jacobi projection*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-two-branch-monotone-range-envelope-for-quadratic-symmetric--68d5f845db4a
- *Arithmetic second-order boundary amplification in discrete quadratic least squares*, publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-arithmetic-second-order-boundary-amplification-in-discrete-quadr--90f86b115858
