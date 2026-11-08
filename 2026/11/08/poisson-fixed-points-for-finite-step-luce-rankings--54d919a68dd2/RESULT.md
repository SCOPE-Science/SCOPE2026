# Poisson fixed points for finite-step Luce rankings

## Finding

**Theorem (joint fixed-point limit for finite-step Luce weights).** Fix an integer \(d\ge 1\), proportions \(\alpha_1,\ldots,\alpha_d>0\) with \(\sum_{j=1}^d\alpha_j=1\), and rates \(w_1,\ldots,w_d>0\). For each integer \(n\), partition \(\{1,\ldots,n\}\) into \(d\) consecutive nonempty blocks \(I_{j,n}\) of sizes \(n_{j,n}\), such that \(n_{j,n}/n\to\alpha_j\). Give every label in \(I_{j,n}\) Luce sampling weight \(w_j\). Sequentially draw labels with probabilities proportional to their remaining weights, and write \(\sigma_n(i)\) for the draw position of label \(i\).

Let \(F_{j,n}=\#\{i\in I_{j,n}:\sigma_n(i)=i\}\). Define

\[
G(t)=\sum_{h=1}^{d}\alpha_h(1-e^{-w_h t}),\qquad
s_j=\sum_{h\le j}\alpha_h,\quad s_0=0,
\]

and \(t_0=0\), \(t_d=\infty\), with \(G(t_j)=s_j\) for \(1\le j<d\). Define

\[
\lambda_j=e^{-w_j t_{j-1}}-e^{-w_j t_j}\in(0,1],
\]

Then the entire vector of class-specific fixed-point counts has the joint limit

\[
(F_{1,n},\ldots,F_{d,n})\ \xrightarrow{\mathrm{TV}}\
\bigl(Z_1,\ldots,Z_d\bigr),\qquad
Z_j\ \text{independent},\quad Z_j\sim\mathrm{Poisson}(\lambda_j).
\]

In particular, the total number of fixed points converges in total variation to \(\mathrm{Poisson}(\Lambda)\), where \(\Lambda=\sum_{j=1}^d\lambda_j\). The parameter equals the diagonal intensity \(\Lambda=\int_0^1\rho(x,x)\,dx\) of the corresponding Luce permuton density of Borga, Chatterjee and Diaconis.

**Two-block quantitative corollary.** Let \(d=2\), \(\alpha_1=u\in(0,1)\), and rates \(a,b>0\). Let \(t>0\) uniquely satisfy \(u(1-e^{-at})+(1-u)(1-e^{-bt})=u\). Then

\[
\Lambda=1-e^{-at}+e^{-bt}.
\]

For fixed \(u,b\), this limiting mean is strictly increasing in the ratio \(a/b\), equals \(1\) when \(a=b\), and is above (respectively below) \(1\) when \(a>b\) (respectively \(a<b\)).

## Assumptions and scope

The number of blocks \(d\) and their positive weights are fixed as \(n\to\infty\). Every block proportion tends to a strictly positive limit. Endpoints of the blocks are consecutive in the label order; the draw-rank convention \(\sigma_n(i)\) matches the inverse of the drawn-label sequence. All limits are through integer \(n\) for which the blocks are nonempty. No regularity beyond convergence of block proportions is required. The theorem makes no assertion for a growing number of blocks, vanishing proportions or unbounded/vanishing weight sequences.

## Proof

**1. Exponential race and class word.** Attach mutually independent exponential clocks \(E_i\) of rates \(w_j\) for labels \(i\in I_{j,n}\). The labels sorted by clock time have exactly the Luce draw law by exponential memorylessness. Define the class word \(W_n(k)=j\) if the label at draw position \(k\) belongs to \(I_{j,n}\). Since labels within one class have identically distributed independent clocks, conditional on the class word their arrangement over that class's occupied positions is a uniform bijection. Furthermore, the bijections of different classes are conditionally independent. This is valid even when some of the class rates coincide.

**2. Exact conditional factorial moments.** Let

\[
H_{j,n}=\#\{k\in I_{j,n}: W_n(k)=j\}.
\]

There are \(H_{j,n}\) positions at which a label from class \(j\) could be fixed. For fixed nonnegative integers \(r_j\le n_{j,n}\), using falling factorials \((v)_r=v(v-1)\cdots(v-r+1)\), uniform assignment yields the exact identity

\[
\mathbb E\!\left[\prod_{j=1}^{d}(F_{j,n})_{r_j}\mid W_n\right]
=\prod_{j=1}^{d}\frac{(H_{j,n})_{r_j}}{(n_{j,n})_{r_j}}.
\tag{1}
\]

Indeed, for \(r_j\) distinct fixed labels the probability of all their prescribed draws is \(1/(n_{j,n})_{r_j}\), and there are \((H_{j,n})_{r_j}\) ordered eligible choices. For any fixed multiindex all denominators are defined for sufficiently large \(n\).

**3. Limiting eligible-position proportions.** For each class and every finite \(t\ge0\), the weak law for independent exponential clocks gives

\[
\frac1n\#\{i\in I_{j,n}:E_i\le t\}
\xrightarrow{\mathbb P}\alpha_j(1-e^{-w_jt}).
\]

The full empirical time distribution has the strictly increasing continuous limit \(G\), with \(G(0)=0\) and \(G(\infty)=1\). Its order-statistic time at the end of the \(j\)-th position block converges in probability to \(t_j\) for \(1\le j<d\). Let \(T_{j,n}\) denote that time, \(T_{0,n}=0\), and \(T_{d,n}=\infty\). Since clocks are almost surely distinct, the number \(H_{j,n}\) is the number of class-\(j\) clocks in \((T_{j-1,n},T_{j,n}]\). Sandwiching these random intervals between intervals with deterministic endpoints \(t_h\pm\varepsilon\), and then letting \(\varepsilon\downarrow0\), gives

\[
\frac{H_{j,n}}{n_{j,n}}\xrightarrow{\mathbb P}
\Pr\bigl( t_{j-1}<\mathrm{Exp}(w_j)\le t_j\bigr)=\lambda_j.
\tag{2}
\]

For the final block use a finite left endpoint and the infinite upper endpoint. Every \(\lambda_j\) is positive. For \(d\ge2\) each is strictly below one; for the single uniform-rate block \(d=1\), the intensity is exactly one.

**4. Joint Poisson law.** The factors on the right of (1) are in \([0,1]\) and, by (2), converge in probability to \(\lambda_j^{r_j}\). Bounded convergence in expectation thus gives

\[
\lim_{n\to\infty}\mathbb E\prod_j(F_{j,n})_{r_j}
=\prod_j\lambda_j^{r_j}\qquad\text{for each fixed multiindex }(r_1,\ldots,r_d).
\tag{3}
\]

The factorial moments of the independent Poisson vector on the right are precisely these products. A direct probability-generating-function argument justifies the inference: for \(z_j\in[-1,1]\), the multivariate expansion of \(\mathbb E\prod_j(1+z_j)^{F_{j,n}}\) has terms bounded in absolute value by \(\prod_j1/r_j!\) using (1), hence is uniformly dominated by \(e^{d}\). Termwise convergence yields \(\exp(\sum_j\lambda_j z_j)\), the independent Poisson generating function; uniqueness then gives the weak joint limit. On the countable discrete space \(\mathbb Z_{\ge0}^d\), weak convergence entails convergence in total variation: restrict to a finite box capturing almost all limiting probability, then sum pointwise convergences there. Summing coordinates gives the total-fixed-point assertion.

**5. Diagonal density comparison.** Proposition 2.2 of Borga, Chatterjee and Diaconis gives, for a weight profile constant at \(w_j\) on the \(j\)-th block,

\[
\rho(x,y)=\frac{w_j e^{-w_jG^{-1}(y)}}{G'(G^{-1}(y))}
\quad\text{if }s_{j-1}<x<s_j.
\]

For the diagonal integral on this interval put \(y=x=G(t)\), so \(dx=G'(t)\,dt\); then

\[
\int_{s_{j-1}}^{s_j}\rho(x,x)\,dx
=\int_{t_{j-1}}^{t_j}w_j e^{-w_jt}\,dt=\lambda_j.
\]

Block endpoints form a null set. Summing confirms \(\Lambda=\int_0^1\rho(x,x)\,dx\). This comparison uses only the stated known permuton density, not a claimed implication from permuton convergence to rare fixed-point counts.

**6. Two-block monotonicity.** Rescale both rates by \(b\), set \(c=a/b\) and write \(v=bt\). The quantile equation is \(u(1-e^{-cv})+(1-u)(1-e^{-v})=u\), while \(\Lambda(c)=1-e^{-cv}+e^{-v}\). Implicit differentiation (the derivative of the equation with respect to \(v\) is strictly positive) yields

\[
\frac{d\Lambda}{dc}
=\frac{v e^{-(c+1)v}}{u c e^{-cv}+(1-u)e^{-v}}>0.
\]

At \(c=1\), the expression for \(\Lambda\) equals \(1\), proving the claims.

## Verification

The independent-of-asymptotics conditional factorial-moment identity (1) was checked by exhaustive exact-rational enumeration of Luce draws for six finite parameter configurations, including two and three classes, and factorial multiindices of total degree at most three. The reproducible standard-library script `VERIFY.py` passed \(7{,}126\) exact and boundary assertions. This is supporting finite evidence only: the infinite joint limit is proved by the law of large numbers, order-statistic quantile convergence, exact identity (1), and the generating-function argument above. Run `python3 VERIFY.py` from the directory containing this file and the checker.

## Relationship to prior work

Borga, Chatterjee and Diaconis, *Permuton and local limits for the Luce model* (first posted September 9, 2025), establish the general permuton density and explicitly pose the limiting fixed-point distribution as an open question in their Section 5.2, conjecturing a Poisson law with diagonal-density parameter. The result above establishes that conjectured distribution for any fixed finite-step positive profile, with **joint independence of the per-block fixed-point counts**. Their permuton convergence alone does not imply the fixed-point law; it is a rare, discontinuous statistic. Chatterjee, Diaconis and Kim's earlier Tsetlin-library enumeration treats positions at the top and bottom but lists fixed points among the open counting questions. Clay's 2026 random-to-top work establishes different, finite-time shuffle results and notes the Luce stationary fixed-point question as open. Fulman's 2024 Poisson theorems concern conjugation-invariant permutation distributions, not the generally non-conjugation-invariant Luce measure.

## Limitations

This proof covers only a fixed finite number of macroscopic constant-weight blocks. It does not prove the arbitrary-profile fixed-point conjecture, describe small cycles beyond fixed points, or give quantitative finite-\(n\) total variation error rates. The mathematical argument has not received independent external review; historical priority of special cases may require further literature assessment. The exact verifier checks finite instances, not the analytic limiting step.

## References

1. J. Borga, S. Chatterjee, P. Diaconis, *Permuton and local limits for the Luce model*, arXiv:2509.07729 (first public version 2025-09-09; Section 5.2, Proposition 2.2), https://arxiv.org/html/2509.07729v3.
2. S. Chatterjee, P. Diaconis, G. B. Kim, *Enumerative Theory for the Tsetlin Library*, arXiv:2306.16521 (first public version 2023-06-28; Sections 1 and 2.2), https://arxiv.org/html/2306.16521v1.
3. A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008 (first public version 2026-03-09; Section 8), https://arxiv.org/html/2603.09008v2.
4. J. Fulman, *Fixed points of non-uniform permutations and representation theory of the symmetric group*, arXiv:2406.12139 (2024; Sections 1, 3 and 4), https://arxiv.org/html/2406.12139v2.
