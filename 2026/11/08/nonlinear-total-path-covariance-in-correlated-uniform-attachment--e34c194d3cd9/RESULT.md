# Nonlinear total-path covariance in correlated uniform-attachment trees

## Finding

Consider two coupled, rooted uniform-attachment trees on the same arrival labels, whose parent selections at each insertion are copied with probability \(\alpha\in[0,1]\), and otherwise are made independently. If \(S_n^{(a)}\) is the sum of distances from the initial root in tree \(a\in\{1,2\}\), then the centered averages
\[
M_n^{(a)}=\frac{S_n^{(a)}-n(H_n-1)}{n}
\]
converge jointly almost surely and in \(L^2\), as coordinates, to \((M_\infty^{(1)},M_\infty^{(2)})\). Here \(H_n=\sum_{j=1}^n1/j\). Their limiting covariance is the **exact nonlinear response**
\[
\boxed{\operatorname{Cov}(M_\infty^{(1)},M_\infty^{(2)})
=C(\alpha)=\sum_{j=2}^{\infty}\frac{\alpha}{j^2(j-\alpha)}
=\sum_{k=1}^{\infty}\alpha^k\bigl(\zeta(k+2)-1\bigr).}
\]
In particular, \(C(0)=0\), \(C(1)=2-\zeta(2)\), and \(C\) is strictly increasing and strictly convex on \([0,1]\). Since each marginal limit has variance \(2-\zeta(2)\), the limiting correlation is
\[
\rho(\alpha)=\frac{C(\alpha)}{2-\zeta(2)},\qquad
0<\rho(\alpha)<\alpha\quad(0<\alpha<1).
\]
For example, \(\rho(1/2)\approx0.3595238052\). The initial slope is \(C'(0)=\zeta(3)-1\), so the macroscopic response is not merely the microscopic copying parameter multiplied by the usual single-tree variance.

The exact finite-size form is as follows. Write
\[
Q_n=\frac1n\sum_{i=1}^nD_i^{(1)}D_i^{(2)}
-\frac{S_n^{(1)}S_n^{(2)}}{n^2},\quad
q_n=\mathbb E Q_n,\quad
c_n=\operatorname{Cov}(M_n^{(1)},M_n^{(2)}).
\]
Starting from \(q_1=c_1=0\), for **every** integer \(n\ge1\) and \(\alpha\in[0,1]\),
\[
\boxed{q_{n+1}=\frac{n(n+1+\alpha)}{(n+1)^2}q_n+\frac{n}{(n+1)^2},\qquad
c_{n+1}=c_n+\frac{\alpha q_n}{(n+1)^2}.}
\]
For \(0<\alpha<1\), these recurrences have the explicit solution
\[
nq_n=\frac{1+\alpha n-\prod_{j=1}^n(1+\alpha/j)}{\alpha(1-\alpha)},
\]
with the endpoint solutions \(nq_n=n-H_n\) at \(\alpha=0\) and \(nq_n=(n+1)H_{n+1}-2n-1\) at \(\alpha=1\).

## Assumptions and scope

There is one root, label \(1\), with depth zero in both trees. Independently for each arrival \(m\ge2\), with probability \(\alpha\) choose one uniform parent label in \(\{1,\ldots,m-1\}\) and use it in both trees; with probability \(1-\alpha\) choose two independent uniform parent labels. Each new vertex has depth one plus its chosen parent's depth. Choices at distinct arrival times are independent, and \(\alpha\) is fixed as \(n\to\infty\).

The theorem concerns **root-to-vertex total path length with a specified initial root**. This is an intrinsic statistic of a rooted tree but not, without identifying the ancestral root, a statistic of the completely unrooted and unlabeled observation model used for graph matching. It is not a claim of a consistent parameter estimator from one unrooted tree pair, nor a joint Gaussian limit.

The pair is defined on a common infinite probability space, giving the almost-sure assertion coordinatewise. Joint \(L^2\) convergence means convergence in the sum of the two squared coordinate norms.

## Proof

**1. Martingale normalization.** Let \(\mathcal F_n\) record both trees through insertion \(n\), and let \(U,V\) be the coupled parent labels at insertion \(n+1\). Write \(\overline D_n^{(a)}=S_n^{(a)}/n\). The new depth is \(1+D_U^{(1)}\) or \(1+D_V^{(2)}\), and each marginal parent is uniform. Thus
\[
\mathbb E[S_{n+1}^{(a)}\mid\mathcal F_n]
=\frac{n+1}{n}S_n^{(a)}+1.
\]
The deterministic means \(m_n=n(H_n-1)\) obey the same recurrence. Therefore \(M_n^{(a)}\) is a centered martingale with increment
\[
\Delta M_{n+1}^{(1)}
=\frac{D_U^{(1)}-\overline D_n^{(1)}}{n+1},\qquad
\Delta M_{n+1}^{(2)}
=\frac{D_V^{(2)}-\overline D_n^{(2)}}{n+1}.
\]
For the aligned-parent component, the conditional centered product of the parent depths equals \(Q_n\); for the independent component it equals zero. Hence
\[
\mathbb E[\Delta M_{n+1}^{(1)}\Delta M_{n+1}^{(2)}\mid\mathcal F_n]
=\frac{\alpha Q_n}{(n+1)^2}.
\]
Orthogonality of martingale increments across different times yields \(c_{n+1}-c_n=\alpha q_n/(n+1)^2\).

**2. The cross-sectional recursion.** The usual centered-sample covariance update is valid for any two numerical vectors, without a positivity assumption:
\[
Q_{n+1}=\frac n{n+1}Q_n+
\frac n{(n+1)^2}(D_{n+1}^{(1)}-\overline D_n^{(1)})
(D_{n+1}^{(2)}-\overline D_n^{(2)}).
\]
Set \(X=D_U^{(1)}-\overline D_n^{(1)}\) and \(Y=D_V^{(2)}-\overline D_n^{(2)}\). Conditional means of \(X,Y\) are zero and \(\mathbb E[XY\mid\mathcal F_n]=\alpha Q_n\). Thus the last product is \((1+X)(1+Y)\) with conditional mean \(1+\alpha Q_n\). This proves the displayed recurrence for \(q_{n+1}\) without assuming independence of the two existing trees.

**3. Exact solution and existence of the limiting pair.** Put \(r_n=nq_n\). The recursion reduces to
\[
r_1=0,\qquad r_{n+1}=\left(1+\frac{\alpha}{n+1}\right)r_n+\frac n{n+1}.
\]
For \(0<\alpha<1\), direct substitution with \(B_n=\prod_{j=1}^n(1+\alpha/j)\) gives
\[
r_n=\frac{1+\alpha n-B_n}{\alpha(1-\alpha)}.
\]
Taking continuous limits in this finite formula gives the endpoint cases stated above. In particular \(q_n(1)=O(\log(n+1))\). The scalar recurrence has nonnegative coefficients and its solution is nondecreasing in \(\alpha\in[0,1]\), so \(0\le q_n(\alpha)\le q_n(1)\).

When the two trees coincide (\(\alpha=1\)), \(q_n(1)\) is precisely the expected within-tree empirical variance of the depths. The conditional squared martingale increment in either marginal, whatever the coupling parameter, is this empirical variance divided by \((n+1)^2\). Consequently
\[
\sup_n\mathbb E[(M_n^{(a)})^2]
\le\sum_{n=1}^{\infty}\frac{q_n(1)}{(n+1)^2}<\infty.
\]
The \(L^2\)-bounded martingale convergence theorem gives almost-sure and \(L^2\) limits in each coordinate. Their covariance is therefore the limit of \(c_n\).

**4. Exact evaluation of the covariance series.** For \(0<\alpha<1\), insert the solution for \(r_n\) to obtain
\[
C(\alpha)=\frac1{1-\alpha}
\sum_{n=1}^{\infty}\frac{1+\alpha n-B_n}{n(n+1)^2}.
\]
The two elementary sums are
\[
\sum_{n\ge1}\frac1{n(n+1)^2}=2-\zeta(2),\qquad
\sum_{n\ge1}\frac1{(n+1)^2}=\zeta(2)-1.
\]
For the third sum, the generalized binomial identity \(\sum_{n\ge0}B_nx^n=(1-x)^{-1-\alpha}\) and the integral
\[
\frac1{n(n+1)^2}=\int_0^1x^{n-1}(1-x+x\log x)\,dx
\]
show, by nonnegative summation and integration, that
\[
\begin{aligned}
\sum_{n\ge1}\frac{B_n}{n(n+1)^2}
&=\int_0^1\left(\frac y{1-y}+\log(1-y)\right)(y^{-1-\alpha}-1)\,dy\\
&=\sum_{j\ge2}\frac{j-1}{j}
\left(\frac1{j-\alpha}-\frac1{j+1}\right),
\end{aligned}
\]
where \(y=1-x\) and \(y/(1-y)+\log(1-y)=\sum_{j\ge2}(j-1)y^j/j\). The summand has the exact partial-fraction decomposition
\[
\frac{j-1}{j}\left(\frac1{j-\alpha}-\frac1{j+1}\right)
=\frac2{j(j+1)}-\frac{1-\alpha}{\alpha}
\left(\frac1{j-\alpha}-\frac1j\right).
\]
Since \(\sum_{j\ge2}2/[j(j+1)]=1\), this evaluates the third sum as
\[
1-\frac{1-\alpha}{\alpha}\sum_{j\ge2}
\left(\frac1{j-\alpha}-\frac1j\right).
\]
Substitution and simplification give
\[
C(\alpha)=1-\zeta(2)+\sum_{j\ge2}\frac1{j(j-\alpha)}
=\sum_{j\ge2}\frac{\alpha}{j^2(j-\alpha)}.
\]
All interchanges are justified for \(0<\alpha<1\): the binomial-integral integrand is nonnegative and integrable, and the final sums are absolutely convergent. The endpoint values follow by dominated convergence, using the proven bound \(q_n(\alpha)\le q_n(1)\); for \(\alpha=1\) the last series telescopes by partial fractions to \(2-\zeta(2)\).

**5. Strict attenuation.** For \(0\le\alpha\le1\), the geometric expansion \(1/(j-\alpha)=\sum_{k\ge0}\alpha^k/j^{k+1}\) is absolutely summable after multiplication by \(\alpha/j^2\), giving the zeta expansion. Every coefficient \(\zeta(k+2)-1\) is strictly positive. Thus \(C\) is strictly increasing and strictly convex. By strict convexity and the endpoint values, \(C(\alpha)<\alpha C(1)\) for each \(0<\alpha<1\). This proves the claimed exact strict suppression of macroscopic correlation.

## Verification

The standalone `check.py` uses exact rational arithmetic to enumerate every coupled sequence of parent-pair choices for up to six vertices at \(\alpha\in\{0,1/3,1/2,2/3,1\}\). It independently compares the enumerated normalized total-path covariance and cross-sectional depth covariance against the finite recurrences and checks the closed-form \(r_n\) at additional sizes. It also compares the convergent series with long recurrence evaluations using explicit non-asymptotic tail allowances. Execute with `python3 check.py`. In the prepared package it reports `CHECKS_OK exact_exhaustive_and_numerical=273; max_enumerated_vertices=6`. These finite computations are corroboration only: the infinite claim is justified by the martingale, recurrence and series arguments above.

## Relationship to prior work

Bäumler, Rácz, Ross and Sridhar (2026, arXiv:2606.02472v1) introduced exactly the aligned-or-independent coupled uniform-attachment model. Their principal results concern detection and estimation from **unrooted, unlabeled** trees; their Appendix A derives leaf-count fluctuation results. Their statements do not supply the two-tree root-path covariance response here.

Dobrow and Fill (1999) studied the total path length of **one** uniform recursive tree and its non-Gaussian martingale limit. Gałązka and Wdowicka (2026, arXiv:2610.00614v1) give general single-tree weighted-recursive path-length martingales and recover the uniform variance constant \(2-\zeta(2)\). This work credits that marginal value and instead calculates the full dependence transfer function of **two** coupled trees. A univariate variance identity, even when exact, does not determine the covariance of differently coupled copies.

## Limitations

The exact formula is specific to uniform attachment, fixed \(\alpha\), independent coupling coins at successive arrival times, and the designated growth root. It does not cover hidden-root reconstruction, unrooted-only observability, nonuniform attachment weights, finite-horizon time-changing coupling probabilities, or the joint limiting distribution beyond its covariance. Historical priority has not been independently certified; general stochastic-noise decompositions may yield other formulations of the result. The finite checker is not a proof of infinite statements.

## References

1. J. Bäumler, M. Z. Rácz, N. Ross and A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472v1, first public posting 2026-06-01, https://arxiv.org/abs/2606.02472.
2. M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1, first public posting 2026-09-30, https://arxiv.org/abs/2610.00614.
3. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, DOI:10.1017/S0963548399003855.
