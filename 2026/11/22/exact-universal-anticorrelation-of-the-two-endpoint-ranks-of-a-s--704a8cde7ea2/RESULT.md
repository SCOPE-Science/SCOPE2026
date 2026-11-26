# Exact universal anticorrelation of the two endpoint ranks of a symmetric random walk

## Finding

Consider the consecutive levels \(S_0,\ldots,S_m\) of a symmetric random walk. Let \(R_0\) and \(R_m\) be the increasing ranks of its initial and final levels among **all** \(m+1\) levels, with rank one assigned to the lowest level. Each endpoint has a discrete-arcsine rank law, which is uniform for \(m=1\) and nonuniform for \(m\ge2\). Their *joint* second-order dependence has the following exact distribution-free form: for every integer \(m\ge1\),

\[
\operatorname{Cov}(R_0,R_m)=-\frac{(m+1)(m+2)}{24},\qquad
\operatorname{Corr}(R_0,R_m)=-\frac{m+2}{3m}.
\]

The marginal variance is \(\operatorname{Var}(R_0)=\operatorname{Var}(R_m)=m(m+1)/8\), and both marginal expectations are \((m+2)/2\). Consequently the endpoint-rank correlation increases strictly from \(-1\) to the limiting value \(-1/3\). The formulas require **no finite mean, variance or other moment assumption** on the steps; Cauchy increments are included.

## Assumptions and scope

Fix an integer \(m\ge1\). Let \(\xi_1,\ldots,\xi_m\) be independent and identically distributed real random variables with a symmetric, atomless law: \(\xi_i\) and \(-\xi_i\) have the same distribution, and \(\Pr(\xi_i=t)=0\) for every real \(t\). Put \(S_0=0\) and \(S_k=\xi_1+\cdots+\xi_k\). The levels are pairwise distinct almost surely, because every nonempty increment block has an atomless distribution. Define

\[
R_0=1+\sum_{j=1}^m \mathbf1\{S_j<S_0\},\qquad
R_m=1+\sum_{j=0}^{m-1}\mathbf1\{S_j<S_m\}.
\]

These are **ranks at fixed time endpoints**, not times at which the minimum and maximum occur, and not rank statistics from two independent walks. The conclusion concerns the ordinary covariance across repeated independent realizations of the same \(m\)-step random walk. It does not assert independence or the complete bivariate rank distribution.

## Proof

Write \(\operatorname{sgn}(0)=0\), and set

\[
 A=R_0-1=\sum_{j=1}^{m}\mathbf1\{\xi_1+\cdots+\xi_j<0\},\qquad
 B=R_m-1=\sum_{\ell=1}^{m}\mathbf1\{\xi_{m-\ell+1}+\cdots+\xi_m>0\}.
\]

Every nonempty block sum is symmetrically distributed without atoms. Thus \(\mathbb EA=\mathbb EB=m/2\). For centered indicators, symmetry gives

\[
 \operatorname{Cov}(A,B)=-\frac14\sum_{j=1}^m\sum_{\ell=1}^m
 \mathbb E\left[\operatorname{sgn}(\xi_1+\cdots+\xi_j)
 \operatorname{sgn}(\xi_{m-\ell+1}+\cdots+\xi_m)\right].\tag{1}
\]

**Three-block sign identity.** For independent symmetric atomless random variables \(X,Y,Z\), with an individual variable also allowed to be identically zero, provided not all three are zero, put

\[
 P=\operatorname{sgn}(X+Y),\quad Q=\operatorname{sgn}(Y+Z),\quad T=\operatorname{sgn}(X+Z).
\]

Then \(\mathbb E(PQ+PT+QT)=1\), provided the nonzero variables are independent and atomless. Indeed, condition on their absolute magnitudes. The nonzero signs remain independent fair signs; ties between distinct nonzero magnitudes occur with probability zero. If all three variables are nonzero, two of the three pair sums include the variable of largest magnitude and have that variable's sign, while the third pair sum has the sign of the variable of middle magnitude. Their three pairwise products sum to \(1+2\varepsilon_{\rm largest}\varepsilon_{\rm middle}\), whose conditional mean is one. With one zero variable, the same average is one (one pair-sum sign is repeated); with two zero variables, the three pair-sum signs are one zero and two identical signs, again giving one. The zero-variable case with no nonzero variables is excluded.

For nonnegative integers \(a,b,c\) with \(a+b+c=m\), let \(X_a,Y_b,Z_c\) be independent sums of \(a,b,c\) successive increments, taking a zero-length sum to be zero. Define

\[
 F(a,b,c)=\mathbb E[\operatorname{sgn}(X_a+Y_b)\operatorname{sgn}(Y_b+Z_c)].
\]

The three-block identity implies

\[
 F(a,b,c)+F(b,a,c)+F(a,c,b)=1.\tag{2}
\]

When the two blocks in a term of (1) do not overlap, their sign product has expectation zero. Otherwise set \(a=m-\ell\), \(b=j+\ell-m\) and \(c=m-j\): these are nonnegative, sum to \(m\), and \(b>0\); the expected sign product is \(F(a,b,c)\). For \(b=0\) the two sign arguments use independent blocks, so \(F(a,0,c)=0\). Hence the double sum in (1) equals

\[
 U_m=\sum_{a+b+c=m}F(a,b,c).
\]

Summing (2) over every ordered triple of nonnegative integers of total \(m\), and reindexing each of the three permutations, yields \(3U_m=\binom{m+2}{2}\). Therefore

\[
\operatorname{Cov}(R_0,R_m)=\operatorname{Cov}(A,B)
=-\frac{U_m}{4}=-\frac{(m+1)(m+2)}{24}.\tag{3}
\]

**Marginal variances.** If \(a,b\) are positive, let \(U_a,V_b\) be independent symmetric atomless block sums and put \(G(a,b)=\mathbb E[\operatorname{sgn}(U_a)\operatorname{sgn}(U_a+V_b)]\). Conditional on the absolute values of the two blocks, the sign of their sum agrees with the sign of the larger-magnitude block. Averaging over the two independent fair signs gives the two-block identity

\[
G(a,b)+G(b,a)=1.\tag{4}
\]

Since the \(\xi_i\) are identically distributed, \(G(a,b)\) depends on block lengths, not their positions. The variance of \(A\), expressed through centered sign indicators, is

\[
\begin{aligned}
\operatorname{Var}(A)
&=\frac14\left(m+2\sum_{k=2}^m\sum_{j=1}^{k-1}G(j,k-j)\right)\\
&=\frac14\left(m+2\sum_{k=2}^m\frac{k-1}{2}\right)
=\frac{m(m+1)}8.
\end{aligned}
\]

By reversal of the i.i.d. increment sequence and sign symmetry, \(B\) has the same variance. Dividing (3) by the common variance gives \(\operatorname{Corr}(R_0,R_m)=-(m+2)/(3m)\), completing the proof. All exchanges involve finite sums of bounded signs, so no moment assumptions are needed.

## Verification

The self-contained Python 3 script `check_endpoint_ranks.py` exhaustively enumerates, for each \(1\le m\le6\), every ordering and sign assignment of step magnitudes \(1,2,4,\ldots,2^{m-1}\). Every nonempty partial sum is then nonzero, and the script computes rank means, both variances, covariance and correlation with exact rational arithmetic. It verifies 36 displayed moment identities across 50,362 such finite paths in total, plus 92 additional two- and three-block sign-identity magnitude cases. Run with `python3 check_endpoint_ranks.py`; standard-library only. These checks are consistency tests, **not** a replacement for the all-\(m\) argument above. The enumerated magnitude-permutation model is a deliberately finite sign-exchangeable test, not the exact continuous i.i.d. model of the theorem.

## Relationship to prior work

The individual occupation-rank marginal is governed by the classical Sparre Andersen fluctuation/arcsine theory. Ivanovs (2015/2016) discusses time-reversal identities and equality in distribution of occupation counts and extrema times; these statements do not provide their joint initial/final rank covariance. Pitman and Tang (2023) study extreme **values** of the random-walk order statistics and Feller-chain descriptions, not the covariance of fixed-time endpoint **rank indices**. Zhu and Xie (2026) analyze nonlinear **distance correlation between two independent walks** via a Brownian occupation measure, with finite-variance assumptions; that result does not imply this exact finite-horizon, one-walk rank identity and motivates closer attention to ordinal dependence along a single trajectory. The present theorem distinguishes these objects and supplies an explicit full-covariance calculation.

## Limitations

Symmetry, identically distributed steps, and an atomless law are assumed; no claim is made for drifted, nonidentical, or tied-increment walks. The identities determine only second moments, not the full joint law. Historical coverage could exist in classical fluctuation/order-statistic work. In particular, Aneja and Sen (1972) study rank-order distributions through Dwass's random-walk method, but accessible abstract information does not establish whether a more general theorem there implies the result; its full text was unavailable for inspection.

## References

1. L. Zhu and Z. Xie, *Nonsense nonlinear correlations between independent random walks*, arXiv:2611.16614v1, first posted 12 November 2026. https://arxiv.org/abs/2611.16614
2. J. Ivanovs, *Sparre-Andersen identity and the last passage time*, arXiv:1501.04542; *Journal of Applied Probability* **53** (2016). https://arxiv.org/abs/1501.04542
3. J. Pitman and W. Tang, *Extreme order statistics of random walks*, *Annales de l'Institut Henri Poincaré – Probabilités et Statistiques* **59** (2023), 97–116. https://doi.org/10.1214/22-AIHP1254
4. K. G. Aneja and K. Sen, *Random Walk and Distributions of Rank Order Statistics*, *SIAM Journal on Applied Mathematics* **23** (1972), 276–287. https://doi.org/10.1137/0123029
