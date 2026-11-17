# A unique covariance sign reversal for the longest circular gap and long-gap counts

## Finding

Place \(n\ge 2\) independent uniform points on a unit-circumference circle and let \(X_1,\ldots,X_n\) be their clockwise successive spacings. Define the maximal gap \(M_n=\max_i X_i\) and the threshold-exceedance count \(N_n(t)=\sum_{i=1}^n\mathbf 1_{\{X_i>t\}}\), for \(0<t<1\). Write \(H_n=\sum_{r=1}^n1/r\) and \((u)_+=\max\{u,0\}\).

**Theorem.** For every integer \(n\ge2\) and every \(0<t<1\),
\[
\operatorname{Cov}(M_n,N_n(t))
=(1-t)^{n-1}\bigl((n-1)t-H_n+1\bigr)
+\sum_{j=1}^{n-1}\frac{(-1)^{j+1}}{j(j+1)}\binom{n-1}{j}\bigl(1-(j+1)t\bigr)_+^n.
\]
There exists exactly one threshold \(t_n\in(0,1)\) at which this covariance vanishes. The covariance is strictly negative for \(0<t<t_n\), and strictly positive for \(t_n<t<1\). Moreover, \(t_2=1/2\), while \(0<t_n<1/2\) for every \(n\ge3\). The endpoint covariances at \(t=0\) and \(t=1\) vanish trivially because the exceedance count is deterministic.

For illustration, \(t_3=0.407701380217632\ldots\) is the unique root in \((1/3,1/2)\) of \(36t^3-43t^2+14t-1=0\). The sign reversal is an all-\(n\) theorem, not a numerical conjecture.

## Assumptions and scope

The sampling points are independent and atomlessly uniform on the circle. Spacings are positive almost surely and sum to one; their joint distribution is \(\operatorname{Dirichlet}(1,\ldots,1)\). The strict threshold convention causes no ambiguity for \(0<t<1\), since all individual gaps have continuous distributions. The law applies equally to the \(n\) pieces of a unit stick broken at \(n-1\) independent uniform points. No independence between the individual gaps is assumed.

In the standard equal-length clockwise arc-coverage model, \(N_n(t)\) is the number of uncovered inter-arc gaps after extending an arc of length \(t\) from each sampled point. \(M_n>t\) characterizes failure of complete coverage, so the covariance connects the obstruction size with the number of remaining holes.

## Proof

**Step 1: Exact law and moment.** The circular spacing vector is uniform on the simplex. For any distinct \(r\) indices and \(0\le s_1,\ldots,s_r\) with \(\sum s_i\le1\), simple translation of the simplex gives
\[
\Pr(X_{i_1}>s_1,\ldots,X_{i_r}>s_r)
=\bigl(1-\textstyle\sum_{\ell=1}^r s_\ell\bigr)^{n-1}.
\]
When the sum exceeds one the probability is zero, as encoded by the positive part. Inclusion-exclusion then yields
\[
\Pr(M_n>x)=\sum_{r=1}^n(-1)^{r+1}\binom nr(1-rx)_+^{n-1}.
\]
Integrating from zero to one gives
\[
\mu_n:=\mathbb E M_n=\frac1n\sum_{r=1}^n\frac{(-1)^{r+1}}r\binom nr
=\frac{H_n}{n}.
\]
Similarly \(\Pr(X_1>t)=(1-t)^{n-1}\), so \(\mathbb E N_n(t)=n(1-t)^{n-1}\).

**Step 2: Conditional maximal gap.** Given \(X_1=x\), the remaining normalized gaps are \(\operatorname{Dirichlet}_{n-1}(1,\ldots,1)\), independently of \(x\). If \(Z_{n-1}\) denotes the maximum of such a vector, then
\[
g_n(x):=\mathbb E[M_n\mid X_1=x]
=\mathbb E\max\{x,(1-x)Z_{n-1}\}.
\]
Every integrand is the maximum of two affine functions of \(x\); hence \(g_n\) is continuous and convex on \([0,1]\). The mean of a maximum of \(m\) uniform simplex coordinates, calculated in Step 1, is \(H_m/m\). Consequently,
\[
g_n(0)=\frac{H_{n-1}}{n-1}
=\mu_n+\frac{H_n-1}{n(n-1)}>\mu_n,
\qquad g_n(1)=1>\mu_n.
\]
Yet the tower property gives \(\mathbb E[g_n(X_1)]=\mu_n\), and \(X_1\) has density \(f_n(x)=(n-1)(1-x)^{n-2}>0\) on \((0,1)\). Thus the sublevel set \(\{x:g_n(x)<\mu_n\}\) is a nonempty open interval \((a_n,b_n)\) with \(0<a_n<b_n<1\). Convexity ensures \(g_n(x)\ge\mu_n\) outside this interval and \(g_n(x)<\mu_n\) within it.

**Step 3: One and only one sign change.** Exchangeability and conditioning give
\[
\frac1n\operatorname{Cov}(M_n,N_n(t))
=h_n(t):=\int_t^1(g_n(x)-\mu_n)f_n(x)\,dx.
\]
The integral over \([0,1]\) vanishes. Hence \(h_n(0)=h_n(1)=0\), and
\(h_n'(t)=-(g_n(t)-\mu_n)f_n(t)\). On \((a_n,b_n)\), this derivative is strictly positive. Moreover,
\[
h_n(a_n)=-\int_0^{a_n}(g_n(x)-\mu_n)f_n(x)\,dx<0,
\quad
h_n(b_n)=\int_{b_n}^1(g_n(x)-\mu_n)f_n(x)\,dx>0.
\]
Both inequalities are strict because the integrands are strictly positive near the endpoints zero and one, respectively. Thus a unique zero \(t_n\in(a_n,b_n)\) exists, with strictly negative covariance before it and strictly positive covariance afterward. Outside \((a_n,b_n)\) the derivative sign prevents any further zero.

For \(t\ge1/2\), at most one spacing can exceed \(t\), and so \(N_n(t)=\mathbf1_{\{M_n>t\}}\). When \(n\ge3\), the event \(\{M_n>1/2\}\) is nondegenerate and its indicator has strictly positive covariance with \(M_n\), proving \(t_n<1/2\). For \(n=2\), the explicit formula in Step 4 yields \(t_2=1/2\).

**Step 4: Finite exact covariance.** Let \(t\le s\le1\). Inclusion-exclusion on the events \(\{X_i>s\}\), separating \(i=1\) from the others, gives
\[
\begin{aligned}
\Pr(M_n>s, X_1>t)
={}&(1-s)^{n-1}\\
&+\sum_{j=1}^{n-1}(-1)^{j+1}\binom{n-1}{j}
\left[(1-t-js)_+^{n-1}-(1-(j+1)s)_+^{n-1}\right].
\end{aligned}
\]
The layer-cake representation for \(M_n\mathbf1_{\{X_1>t\}}\) implies
\[
\begin{aligned}
\mathbb E[M_n\mathbf1_{\{X_1>t\}}]
&=t(1-t)^{n-1}+\int_t^1\Pr(M_n>s,X_1>t)\,ds\\
&=t(1-t)^{n-1}+\frac{(1-t)^n}{n}
+\frac1n\sum_{j=1}^{n-1}\frac{(-1)^{j+1}}{j(j+1)}\binom{n-1}{j}(1-(j+1)t)_+^n.
\end{aligned}
\]
Subtract \(\mu_n\Pr(X_1>t)\), multiply by \(n\), and simplify the first two terms to obtain the stated exact finite formula. At \(n=2\), this formula is negative on \((0,1/2)\), zero at \(1/2\), and positive on \((1/2,1)\), as claimed.

## Verification

The standalone standard-Python verifier `verify.py` independently computes the covariance through exact rational integration of joint simplex tails in the layer-cake identity and compares it with the closed formula. It performed 2,635 exact Fraction comparisons for \(2\le n\le18\) and rational cutoffs (including boundaries). A separate conditional-regression quadrature calculation using SciPy passed 48 additional floating-point comparisons with tolerance \(4\cdot10^{-9}\). Numerically bracketed roots were obtained for \(n\in\{2,3,4,5,8,10,20,30,50\}\), illustrating but not proving the all-size result. The proof above establishes existence, uniqueness and strict signs for every admissible integer \(n\).

Run `python verify.py` with Python 3 and SciPy available. The rational identity routines use only the Python standard library; SciPy is required for the separate numerical quadrature and root computations.

## Relationship to prior work

Holst (1980) develops exact and asymptotic distributions and moments of broken-stick spacings. Schlemm (2014) studies the same maximal circular spacing using a uniform Dirichlet representation and derives maximal-spacing moments. Those results imply the underlying marginal formulas but do not in their inspected statements give the cross-statistic sign reversal proved here. Hüsler (1982) and Holst–Hüsler (1984) study random circle coverage and joint *limit* distributions involving numbers of gaps and largest gaps. Their accessible abstracts do not establish an all-finite-size, one-threshold covariance phase classification. The full text of the especially close 1984 article was not accessible for a decisive line-by-line comparison, so independent historical-priority checking remains important. The finite mixed-moment formula is derivable from classical simplex inclusion-exclusion; the primary structural assertion is its unique sign reversal at every sample size.

## Limitations

The result is for independent uniform sample points, equal coverage-arc lengths and the strict exceedance count. It does not assert a sign phase diagram under nonuniform sampling or arbitrary Dirichlet concentration vectors. The threshold \(t_n\) is specified uniquely and can be computed from the finite formula, but an explicit elementary expression for general \(n\) and an asymptotic expansion of \(t_n\) are not proved. The scientific comparison is not an independent audit and does not establish global priority beyond the inspected literature.

## References

- L. Holst, *On the Lengths of the Pieces of a Stick Broken at Random*, Journal of Applied Probability 17 (1980), 623–634, https://www.jstor.org/stable/3212956 (open copy: https://imprs-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf).
- E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114v1, first posted 2014-05-23, https://arxiv.org/abs/1405.6114.
- J. Hüsler, *Random coverage of the circle and asymptotic distributions*, Journal of Applied Probability 19 (1982), 578–587, https://doi.org/10.2307/3213515.
- L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability 21 (1984), 558–566, https://doi.org/10.2307/3213617.
