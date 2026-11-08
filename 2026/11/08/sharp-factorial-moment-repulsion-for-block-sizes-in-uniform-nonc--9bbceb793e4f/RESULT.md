# Sharp factorial-moment repulsion for block sizes in uniform noncrossing partitions

## Finding

For a uniformly chosen noncrossing partition of \(\{1,\ldots,n\}\), let \(X_j\) count its blocks of size \(j\), and put \(\mu_j=\mathbb E X_j\). For every integer \(n\ge3\), define
\[
\kappa_n=\frac{(2n-1)(n-1)}{(n+1)(2n-3)}=1-\frac{2(n-2)}{(n+1)(2n-3)}<1.
\]
For every integer \(m\ge2\) and all positive integers \(\ell_1,\ldots,\ell_m\), including repeated sizes, write \(r_j=|\{i:\ell_i=j\}|\). Then the *uniform all-order factorial-moment bound* is
\[
\boxed{\quad \mathbb E\!\left[\prod_{j\ge1}(X_j)_{\underline{r_j}}\right]
\le \kappa_n^{m-1}\prod_{i=1}^{m}\mu_{\ell_i}.\quad}
\]
Here \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\) and \((x)_{\underline0}=1\). The constant \(\kappa_n\) is optimal as a uniform *one-step* factor and in the two-block inequality: equality for \(m=2\) occurs precisely for the size pairs \((1,1)\), \((1,2)\) and \((2,1)\). In particular, for distinct \(a,b\),
\[
\operatorname{Cov}(X_a,X_b)\le-(1-\kappa_n)\mu_a\mu_b<0,
\]
with equality only for \(\{a,b\}=\{1,2\}\); while for any \(a\),
\[
\operatorname{Var}(X_a)\le\mu_a-(1-\kappa_n)\mu_a^2<\mu_a.
\]
The finding is an all-order factorial-moment comparison, **not** a claim of full negative association for arbitrary increasing functions.

## Assumptions and scope

A partition is noncrossing when no two distinct blocks contain \(a<c\) and \(b<d\) respectively with \(a<b<c<d\). All \(C_n=\binom{2n}{n}/(n+1)\) noncrossing partitions are equiprobable. The size parameters are positive integers; a falling-factorial product is zero if there are not enough eligible blocks. No asymptotic regime, independent-block assumption or restriction to distinct sizes is imposed.

For \(m\ge1\) put \(s=\sum_i\ell_i\) and
\[
M_{m,s}=\mathbb E\!\left[\prod_{j\ge1}(X_j)_{\underline{r_j}}\right].
\]
Although its notation suppresses the individual sizes, this expectation depends on them only through \(m\) and \(s\). For \(s\le n\), the exact formula is
\[
\boxed{M_{m,s}=\frac{(n)_{\underline{m-1}}}{C_n}\binom{2n-m-s}{n-s}.}
\]
For \(s>n\), \(M_{m,s}=0\). The single-size mean is \(\mu_b=M_{1,b}>0\) for \(1\le b\le n\).

## Proof

**1. Exact multivariate factorial moments.** Let \(F(z;\mathbf w)\) count noncrossing partitions by size and by weights of their blocks, with the empty partition included. Cutting the block containing the first position at successive elements gives the standard formal identity
\[
F=1+\sum_{j\ge1}w_j(zF)^j.
\]
With \(u=zF\), Lagrange inversion gives
\[
[z^n]F=\frac1{n+1}[u^n]\left(1+\sum_{j\ge1}w_ju^j\right)^{n+1}.
\]
Set \(w_j=1+t_j\), so the parenthesis is \((1-u)^{-1}+\sum_jt_ju^j\). Differentiating \(r_j\) times in every \(t_j\), evaluating at zero, dividing by \(C_n\), and extracting the coefficient yields
\[
M_{m,s}=\frac{(n)_{\underline{m-1}}}{C_n}[u^{n-s}](1-u)^{-(n+1-m)}
=\frac{(n)_{\underline{m-1}}}{C_n}\binom{2n-m-s}{n-s}.
\]
This remains valid for \(m=n=s\). There are no selected configurations if \(s>n\).

**2. A sharp bound for adding one distinguished block.** Suppose \(m\ge1\), \(s\ge m\), and \(s+b\le n\). The ratio of the factorial moments before and after adding a block of size \(b\) equals
\[
Q_{m,s}(b)=\frac{M_{m+1,s+b}}{M_{m,s}}
=\frac{(n-m+1)(n-m)(n-s)_{\underline b}}{(2n-m-s)_{\underline{b+1}}}.
\]
Put \(c=n-m\) and \(a=n-s\). Then \(b\le a\le c\) and
\[
Q_{m,s}(b)=h_{c,b}(a):=\frac{c(c+1)(a)_{\underline b}}{(a+c)_{\underline{b+1}}}.
\]
For \(b\le a<c\), the ratio \(h_{c,b}(a+1)/h_{c,b}(a)\) is
\[
\frac{(a+1)(a+c-b)}{(a+1-b)(a+c+1)}.
\]
Its numerator minus denominator is \(bc-a-1\ge0\). Hence \(h_{c,b}(a)\le h_{c,b}(c)=:q_c(b)\).

Now
\[
q_c(b)=\frac{c(c+1)(c)_{\underline b}}{(2c)_{\underline{b+1}}}
=q_c(1)\prod_{j=1}^{b-1}\frac{c-j}{2c-1-j},
\qquad q_c(1)=\frac{c(c+1)}{2(2c-1)}.
\]
The value \(q_c(1)\) is nondecreasing in integer \(c\ge1\):
\[
q_{c+1}(1)-q_c(1)=\frac{(c+1)(c-1)}{(2c+1)(2c-1)}\ge0.
\]
For each \(j\ge1\), the factor \((c-j)/(2c-1-j)\), with \(c>j\), is nondecreasing in \(c\) (the factor for \(j=1\) equals \(1/2\), and the derivative for \(j>1\) has positive numerator \(j-1\)). Consequently \(q_c(b)\le q_{n-1}(b)\).

**3. The universal constant and its equality case.** Since \(q_{n-1}(b)=M_{2,1+b}/M_{1,1}\), define \(R_b=q_{n-1}(b)/\mu_b\) for \(1\le b\le n-1\). Substituting the exact binomial moments gives
\[
R_1=\frac{(2n-1)(n-1)}{(n+1)(2n-3)}=\kappa_n,
\qquad
\frac{R_{b+1}}{R_b}
=\frac{(n-b-1)(2n-b-1)}{(2n-b-3)(n-b)}\quad(1\le b\le n-2).
\]
The numerator minus denominator in the last ratio is \(1-b\), so \(R_2=R_1\), and \(R_{b+1}<R_b\) for \(b\ge2\). Thus every admissible extension satisfies
\[
M_{m+1,s+b}\le\kappa_n M_{m,s}\mu_b.
\]
If \(s+b>n\) its left side is zero. Iteration proves the stated all-order inequality. The pair \((1,1)\) attains \(R_1=\kappa_n\), and \((1,2)\) attains \(R_2=\kappa_n\). Conversely the monotonicities in steps 2 and 3 exclude equality for all other two-size pairs: the only extra tie at fixed \(m=1\) is \(s=1\) or \(s=2\) when \(b=1\), which gives the symmetric pair \((2,1)\). For \(n\ge3\), \(1-\kappa_n=2(n-2)/((n+1)(2n-3))>0\).

**4. Count consequences.** For distinct \(a,b\), \(\mathbb E(X_aX_b)=M_{2,a+b}\), giving the covariance claim. For equal sizes, \(\mathbb E(X_a)_{\underline2}=M_{2,2a}\) and \(\operatorname{Var}X_a=\mu_a+M_{2,2a}-\mu_a^2\), giving the stated strict sub-Poisson bound. All assertions include the case where the selected block sizes cannot fit into \(n\).

## Verification

Run `python3 check.py` with Python 3's standard library. The checker independently generates restricted-growth strings for set partitions, rejects crossings directly, and evaluates the exact factorial-product averages by exhaustive enumeration for \(3\le n\le8\) and all size multisets of up to four blocks that fit. It separately tests the sharp two-block bound for all positive sizes and \(3\le n<100\) using exact rational arithmetic. The packaged replay returned `VERIFY_OK 328671 exact assertions`.

These finite checks are corroboration, not a substitute for the all-order algebraic proof.

## Relationship to prior work

Kargin's 2019 work [1], Theorem 2.2 and equations (3)–(4), already gives the single-size and pairwise block-count generating functions, explicit first and mixed second factorial moments, asymptotic pairwise negative covariance, and Gaussian limits. Those results are **not** claimed as new. Kortchemski and Marzouk [2] provide the earlier simply generated noncrossing-partition framework and weighted tree bijections, giving a broader means of encoding arbitrary block-size laws. Gatea and Huang [3] derive factorial-moment formulas for divisibility-restricted noncrossing partitions and related Gaussian limits; their univariate moment analyses are acknowledged.

The narrowly scoped claim here is the quantitative inequality \(M_{m,s}\le\kappa_n^{m-1}\prod\mu\) **simultaneously for arbitrary finite collections of block sizes**, with the sharp universal one-step constant, pair equality characterization, and finite-size variance/covariance consequences. It requires a separate monotonicity comparison of successive marked-block factorial moments, not just a rewriting of a known asymptotic covariance. The general partition-function identities make these moments calculable, so they remain a significant antecedent and historical-priority risk.

## Limitations

The theorem concerns uniform, type-A noncrossing set partitions only, not all simply generated block weights. It bounds mixed falling-factorial moments and does not imply negative association of arbitrary increasing events or stochastic domination of entire count vectors. The factor \(\kappa_n^{m-1}\) is a uniform valid bound; its optimality is proved for each single extension and for two marked blocks, **not** separately for every fixed order \(m\ge3\). Independent mathematical validation and comprehensive historical-priority confirmation have not been performed.

## References

[1] V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632 (first posted 2019-07-01), https://arxiv.org/html/1907.00632v1 .

[2] I. Kortchemski and C. Marzouk, *Simply generated non-crossing partitions*, arXiv:1503.09174 (first posted 2015-03-31), https://arxiv.org/html/1503.09174v1 .

[3] A. Gatea and S. Huang, *Combinatorial Insights into Asymptotic Normality*, arXiv:2610.34775 (first posted 2026-10-26), https://arxiv.org/html/2610.34775v1 .
