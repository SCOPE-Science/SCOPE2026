# A four-knot boundary layer forces greater-than-two variation amplification in curvature-capped projection

## Finding
For integers \(n\ge2\), let \((H_nz)_i=z_i-2z_{i+1}+z_{i+2}\) for \(1\le i\le n-2\), and let \(P_{n,R}\) be Euclidean projection onto
\[
K_{n,R}=\{z\in\mathbb R^n: |(H_nz)_i|\le R\text{ for all }1\le i\le n-2\},\qquad R>0.
\]
Measure two-input perturbations by \(V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|\), and define
\[
C_n=\sup_{V_n(x-y)>0}\frac{V_n(P_{n,R}x-P_{n,R}y)}{V_n(x-y)}.
\]
The following strict twofold-instability witness and stronger asymptotic lower bound hold:
\[
\boxed{C_{30}\ge\frac{197}{98}>2,\qquad \liminf_{n\to\infty}C_n\ge\frac{16}{7}>2.}
\]
The 30-site inequality is attained as a perturbation ratio by **two explicit finite real inputs** at every positive radius. The asymptotic bound comes from a single geometrically specified four-knot family of affine-spline faces on even-length paths; it is not an assertion that \(C_n\) has a limit or that \(16/7\) is the exact limiting value.

## Assumptions and scope
All sites are equally spaced, all observations have equal Euclidean mass, and each absolute second difference has the same positive cap. The path has free, nonperiodic endpoints. Only the two-input variation seminorm is measured; constant perturbations are excluded from the quotient. The result concerns hard curvature caps, not a penalty on the sum of absolute second differences. The same four-knot tangent face also supplies a lower bound for second-difference \(\ell^1\)-penalized trend filtering, but that operator's previously known active-set formula and its low-dimensional constants are not asserted as new here.

## Proof
**1. All selected curvature faces are realized.** Let \(S\) be any subset of second-difference row indices, and let \(H_S\) be the corresponding matrix. Its rows are independent. Choose \(z\) with \((H_nz)_i=R\) on \(S\) and zero elsewhere, and choose \(u=z+H_S^\top\lambda\) for a vector \(\lambda\) with all components strictly positive. The Euclidean normal-cone condition gives \(P_{n,R}(u)=z\), with inactive constraints strictly slack. In a neighborhood of \(u\), the projector's linear part is
\[
\Pi_S=I-H_S^\top(H_SH_S^\top)^{-1}H_S.
\]
Consequently, for each step vector \(h^{(j)}\), zero through site \(j\) and one thereafter, \(V_n(\Pi_Sh^{(j)})\) is a finitely attainable two-input variation ratio, since \(V_n(h^{(j)})=1\). This observation does not by itself assert any new formula for the all-face maximum.

**2. The four-knot subspace.** For even \(n\ge 12\), leave exactly the curvature rows \(1,4,n-5,n-2\) inactive, and make every other row active. The tangent space \(\ker H_S\) is six-dimensional, spanned by the functions of site \(t\)
\[
1,\quad t,\quad (t-2)_+,\quad (t-5)_+,\quad (t-(n-4))_+,\quad (t-(n-1))_+.
\]
Thus its orthogonal projector can be calculated with only the six-by-six Gram matrix of these functions. It consists of an affine interior segment between sites \(5\) and \(n-4\), with a short three-increment affine boundary layer on each side and unconstrained endpoint values. Take the step \(h^{(n/2)}\). The finite witness from step 1 shows that the variation of its orthogonal projection lower-bounds \(C_n\).

**3. An exact 30-site certificate.** For \(n=30\), the six-dimensional Gram calculation gives consecutive increments of \(\Pi_Sh^{(15)}\) equal to
\[
\underbrace{\frac{11}{196}}_{1\text{ increment}},\quad
\underbrace{-\frac{33}{392},-\frac{33}{392},-\frac{33}{392}}_{3\text{ increments}},\quad
\underbrace{\frac{13}{196},\ldots,\frac{13}{196}}_{21\text{ increments}},\quad
\underbrace{-\frac{33}{392},-\frac{33}{392},-\frac{33}{392}}_{3\text{ increments}},\quad
\underbrace{\frac{11}{196}}_{1\text{ increment}}.
\]
Their absolute sum is \(197/98\). For \(R=1\), define \(z_1=z_2=0\), then recursively \(z_{i+2}=2z_{i+1}-z_i+d_i\), where \(d_i=0\) at \(i\in\{1,4,25,28\}\) and \(d_i=1\) otherwise. Put \(u=z+H_S^\top\mathbf1\), \(v=u+10^{-3}h^{(15)}\). The exact-rational program `four_knot.py` verifies the strict positive KKT multipliers and all inactive slack inequalities for both outputs: \(P_{30,1}(u)=z\) and \(P_{30,1}(v)=z+10^{-3}\Pi_Sh^{(15)}\). Hence the ratio is exactly \(197/98\) for these finite distinct inputs. Scaling by \(R\) establishes the same assertion for any \(R>0\).

**4. The asymptotic four-knot boundary layer.** Let even \(n\to\infty\), and write \(p^{(n)}=\Pi_Sh^{(n/2)}\). On the long central interval \(5\le t\le n-4\), the fit is affine, \(p^{(n)}_t=a_n+b_n(t/n)\). The least-squares objective divided by \(n\) converges, uniformly for bounded \((a_n,b_n)\), to
\[
\int_0^1\bigl(a+bs-\mathbf1_{(1/2,1]}(s)\bigr)^2\,ds.
\]
Only finitely many endpoint observations lie outside this interval; their optimum residual sum remains bounded when the central endpoints remain bounded. Coercivity and strict convexity of the limiting two-parameter quadratic imply that the central coefficients converge to its unique minimizer \((a,b)=(-1/4,3/2)\). Therefore \(p^{(n)}_5\to-1/4\), \(p^{(n)}_{n-4}\to5/4\), and central variation converges to \(3/2\).

At the left boundary, the first fitted value is exactly zero, while sites \(2,3,4,5\) lie on a line pinned at the fifth value. Given that pinned value \(c\), minimizing the three squared residuals at sites \(2,3,4\) gives line slope \(3c/7\). As \(c\to-1/4\), the five fitted values tend to
\[
(0,\,1/14,\,-1/28,\,-1/7,\,-1/4),
\]
whose variation is \(11/28\). Reflection combined with complementation gives the matching right-edge variation \(11/28\). Hence
\[
\lim_{\substack{n\to\infty\\ n\text{ even}}}V_n(p^{(n)})
=\frac{11}{28}+\frac32+\frac{11}{28}=\frac{16}{7}.
\]
The step has unit variation, so the limit yields \(\liminf_{n\to\infty} C_n\ge16/7\) only if the odd indices are also controlled. For each odd dimension \(n\), use the same construction with its central step after \(\lfloor n/2\rfloor\), the same symmetric four-knot pattern, and the Riemann-sum limit; left and right endpoint layers converge to the same values. Therefore the full-sequence lower limit is at least \(16/7\). This is a constructed lower bound, not an equality claim for the supremum.

## Verification
Run `python3 four_knot.py`. It performs exact-rational six-dimensional Gram projection, checks all 29 rational increments, and verifies a finite primal-dual witness with strict multiplier positivity and strict slack. It also verifies the exact limiting boundary-layer arithmetic. The asymptotic convergence is proved in step 4 analytically, not extrapolated from numerical experiments.

## Relationship to prior work
Kim–Koh–Boyd–Gorinevsky and Tibshirani–Taylor develop second-difference penalization and piecewise affine trend fitting. Existing finite-face methods already give the same face derivatives for related second-difference denoisers; therefore we do **not** claim the generic tangent formula, the initial small-dimensional coefficients, or their commonality as novel. The new observation is that just four free curvature rows create an exact finite gain above \(2\) and a boundary-layer lower envelope of \(16/7\). Unlike the established small-dimensional formula, this excludes a plausible uniform twofold stability bound on arbitrarily long signals. Agarwal–Phillips–Sadri treat first-difference Lipschitz regression and do not cover this curvature perturbation question. The relevant inspected primary sources and retrieved mathematical records did not yield this explicit boundary-layer amplification; historical priority is nevertheless provisional.

## Limitations
No global upper bound or exact asymptotic value of \(C_n\) is proved. The 30-site witness is not claimed to be the first dimension with amplification above two. The tangent-space family does not characterize all maximizing faces. Weighted observations, periodic boundaries, nonuniform curvature caps, and other norms are not treated. Independent mathematical review and exhaustive historical-source comparison have not been performed.

## References
1. S.-J. Kim, K. Koh, S. Boyd, D. Gorinevsky, *\(\ell^1\) Trend Filtering*, SIAM Review **51** (2009), 339–360, first verified online date 2009-05-04. https://doi.org/10.1137/070690274 ; https://web.stanford.edu/~boyd/papers/pdf/l1_trend_filter.pdf
2. R. J. Tibshirani, J. Taylor, *The Solution Path of the Generalized Lasso*, arXiv:1005.1971, initial submission 2010-05-11; Annals of Statistics **39** (2011), 1335–1371. https://arxiv.org/abs/1005.1971
3. P. K. Agarwal, J. M. Phillips, B. Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, arXiv:0912.5182, initial submission 2009-12-28. https://arxiv.org/abs/0912.5182
