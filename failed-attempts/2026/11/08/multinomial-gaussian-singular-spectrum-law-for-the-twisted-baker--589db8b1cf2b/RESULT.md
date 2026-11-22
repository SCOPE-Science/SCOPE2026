# Multinomial Gaussian singular-spectrum law for the twisted baker map

## Finding

For every fixed integer \(m\ge2\), the finite-time singular-value spectrum of the \(m\)-dimensional twisted baker map has an exact representation by occupation counts of a half-lazy directed random walk on the cyclic group \(\mathbb Z/m\mathbb Z\). Under normalized Lebesgue initial data, the centered occupation vector has the same *limiting covariance matrix* as \(n\) independent uniform allocations to \(m\) boxes, even though its increments are not independent:
\[
\frac{C(n)-(n/m)\mathbf1}{\sqrt n}\ \Longrightarrow\ G,
\qquad \operatorname{Cov}(G)=\frac1m I_m-\frac1{m^2}\mathbf1\mathbf1^\top.
\]
If \(\sigma_1(n)\ge\cdots\ge\sigma_m(n)\) are the singular values of the \(n\)-step Jacobian, then jointly
\[
\left(\frac{\log\sigma_j(n)-(n/m)\log2}{\sqrt n}\right)_{j=1}^m
\Longrightarrow (\log2)(G_{(j)})_{j=1}^m,
\]
where \(G_{(1)}\ge\cdots\ge G_{(m)}\) are the ordered Gaussian coordinates. In particular, almost every orbit has all \(m\) Lyapunov exponents equal to \((\log2)/m\), but the maximal finite-time expansion has the non-Gaussian, positive order-statistic bias
\[
\mathbb E\log\|DF^n\|=\frac{n\log2}{m}+c_m(\log2)\sqrt n+o(\sqrt n),
\quad c_m=\frac1{\sqrt m}\,\mathbb E\max_{1\le j\le m}Z_j,
\]
for independent standard normal \(Z_j\). Moreover, \(\log\kappa(DF^n)/\sqrt n\) converges to \((\log2)(\max_jG_j-\min_jG_j)\), where \(\kappa\) denotes the Euclidean condition number. In dimension two, an exact finite-time binomial law holds: \(C_1(n)\overset d=1+\operatorname{Bin}(n-1,1/2)\), and \(\log\kappa(DF^n)/((\log2)\sqrt n)\Longrightarrow |Z|\) for standard normal \(Z\).

## Assumptions and scope

Fix \(m\ge2\) and the box \(X=[-1,1]\times[0,1]^{m-1}\). On \(X_L=\{x\in X:x_1<0\}\) and \(X_R=\{x\in X:x_1\ge0\}\), respectively, define
\[
F(x_1,\ldots,x_m)=\begin{cases}
(1+2x_1,x_2,\ldots,x_m), &x_1<0,\\
(1-2x_m,x_1,\ldots,x_{m-1}),&x_1\ge0.
\end{cases}
\]
The initial point is sampled from normalized \(m\)-dimensional Lebesgue measure on \(X\). The Jacobian \(DF^n(x)\) is considered away from the finite union of branch-discontinuity preimages, a set of measure zero. All limits below take \(n\to\infty\) with \(m\) fixed. No assertion is made about joint limits in which \(m\) grows with \(n\), or about eigenvalues of return Jacobians on periodic orbits.

Write \(b_t\in\{0,1\}\) for the branch visited at time \(t\), with zero for \(X_L\) and one for \(X_R\). For \(n\ge1\), define the integer vector \(C(n)=(C_0(n),\dots,C_{m-1}(n))\) by counting, for each \(j\in\mathbb Z/m\mathbb Z\), the number of indices \(k\in\{0,\dots,n-1\}\) satisfying
\[
\sum_{r=k+1}^{n-1}b_r\equiv j\pmod m.
\]
Thus \(\sum_j C_j(n)=n\). The order of the coordinates of \(C(n)\) is immaterial to the singular spectrum, but is fixed by this formula for its stated vector limit.

## Proof

**1. Exact monomial factorization.** Define the diagonal matrix \(D=\operatorname{diag}(2,1,\ldots,1)\) and the orthogonal signed cyclic permutation \(Q\) by \(Qe_j=e_{j+1}\) for \(j<m\) and \(Qe_m=-e_1\). Its conjugation acts as a cyclic permutation on diagonal matrices. The two branch Jacobians are \(A_L=D\) and \(A_R=DQ\). For each binary word, move the factors \(Q\) to the right in the product \(A_{b_{n-1}}\cdots A_{b_0}\). The resulting left factor is diagonal, with one copy of \(2\) on coordinate \(1+\sum_{r=k+1}^{n-1}b_r\pmod m\) for each \(k\). The remaining right factor is an orthogonal signed permutation. Consequently, exactly and without approximation,
\[
\{\sigma_1(n),\ldots,\sigma_m(n)\}
=\{2^{C_0(n)},\ldots,2^{C_{m-1}(n)}\}
\]
as multisets for every admissible orbit segment. Thus the full singular spectrum reduces to the integer occupation vector.

**2. Distribution as a cyclic-walk local-time vector.** Each branch is almost everywhere an affine bijection onto \(X\) with absolute Jacobian determinant \(2\); hence every \(n\)-branch cylinder has normalized Lebesgue measure \(2^{-n}\). This exact Bernoulli coding is also established in the originating paper. Thus \((b_0,\dots,b_{n-1})\) is uniformly distributed on \(\{0,1\}^n\). Reading a uniform word backwards does not change its distribution. It follows that \(C(n)\) has exactly the distribution of the occupation vector \((\sum_{t=0}^{n-1}\mathbf1_{\{W_t=j\}})_{j=0}^{m-1}\) of the Markov chain
\[
W_0=0,\qquad W_{t+1}\equiv W_t+\xi_t\pmod m,
\qquad \mathbb P(\xi_t=0)=\mathbb P(\xi_t=1)=1/2,
\]
where the \(\xi_t\) are independent. Its transition matrix is \(P=(I+S)/2\), with \((Sh)(j)=h(j+1)\). The chain is irreducible and aperiodic, and its unique invariant distribution is uniform on \(\mathbb Z/m\mathbb Z\).

**3. Exact Gaussian covariance.** For any real vector \(v=(v_j)\), put \(\bar v=m^{-1}\sum_jv_j\) and \(g(j)=v_j-\bar v\). Because \(\sum_jg(j)=0\), there is a bounded periodic function \(h\) satisfying
\[
h(j)-h(j+1)=2g(j),\qquad (I-P)h=g.
\]
Set \(\mathcal D_{t+1}=h(W_{t+1})-(Ph)(W_t)\). These are bounded martingale differences, and the exact telescoping identity is
\[
\sum_{t=0}^{n-1}g(W_t)
=h(W_0)-h(W_n)+\sum_{t=0}^{n-1}\mathcal D_{t+1}.
\]
Conditional on \(W_t=j\), the increment \(\mathcal D_{t+1}\) equals \(g(j)\) or \(-g(j)\), each with probability \(1/2\). Thus its predictable conditional variance is *exactly* \(g(W_t)^2\). By the finite irreducible aperiodic-chain ergodic theorem,
\[
\frac1n\sum_{t=0}^{n-1}g(W_t)^2\ \longrightarrow\ \frac1m\sum_{j=0}^{m-1}g(j)^2
\quad\text{almost surely}.
\]
The martingale Lindeberg condition holds because the increments are bounded. The scalar martingale central limit theorem, followed by Cramér–Wold, therefore gives
\[
\frac{v\cdot(C(n)-(n/m)\mathbf1)}{\sqrt n}
\Longrightarrow N\!\left(0,\frac1m\sum_j(v_j-\bar v)^2\right).
\]
The quadratic form on the right is \(v^\top[(1/m)I_m-(1/m^2)\mathbf1\mathbf1^\top]v\), proving the joint Gaussian law. The cancellation of all extra long-run covariance is specific to the half-lazy *directed* step rule; it is not an assertion that the occupancy indicators are independent.

**4. Singular-value laws and almost-sure exponents.** Because sorting is a continuous map on \(\mathbb R^m\), the continuous-mapping theorem applied to the exact factors \(2^{C_j(n)}\) proves the joint sorted log-singular-value limit and condition-number limit. For almost-sure exponents, let \(U_t=\sum_{r=0}^{t-1}b_r\pmod m\). The occupation counts for suffix residues at length \(n\) are a cyclic permutation of the counts of \(U_1,\ldots,U_n\). The ordinary finite-state ergodic theorem makes all their proportions converge to \(1/m\), almost surely. This proves that every singular-value exponential rate, and hence every Lyapunov exponent, equals \((\log2)/m\).

For expected maximal expansion, bounded \(h\) and martingale orthogonality in step 3 give, for each coordinate, \(\mathbb E[(C_j(n)-n/m)^2]=O_m(n)\). Consequently the scaled maximum has a bounded second moment and is uniformly integrable. Its expectation therefore converges to \(\mathbb E\max_j G_j\). Taking independent standard normal \(Z_j\) and \(G_j=(Z_j-\bar Z)/\sqrt m\), with \(\bar Z=m^{-1}\sum_j Z_j\), yields \(c_m=m^{-1/2}\mathbb E\max_j Z_j\), which can also be evaluated as
\[
c_m=\sqrt m\int_{-\infty}^{\infty}z\varphi(z)\Phi(z)^{m-1}\,dz,
\]
where \(\varphi\) and \(\Phi\) denote the standard normal density and distribution function. This proves the stated mean expansion asymptotic.

**5. Exact dimension-two law.** When \(m=2\), every row of \(P\) is \((1/2,1/2)\). Thus \(W_1,\ldots,W_{n-1}\) are independent fair two-state variables, while \(W_0=0\). The exact representation gives \(C_0(n)\overset d=1+\operatorname{Bin}(n-1,1/2)\), \(C_1(n)=n-C_0(n)\). Hence \(\log\kappa(DF^n)=(\log2)|2C_0(n)-n|\), and the ordinary binomial central limit theorem gives the folded-normal limit claimed above.

## Verification

Run `python3 checker.py` using the standard Python library. The checker multiplies the exact integer Jacobian matrices and verifies the occupation-factorization identity for **all 5,110 binary words** of lengths one through nine in dimensions two through six. It also verifies the exact dimension-two binomial counts through length eleven. Seeded Monte Carlo checks in dimensions three and five compare the measured occupation covariance against \((1/m)I_m-(1/m^2)\mathbf1\mathbf1^\top\); these are finite illustrations only. The continuum and asymptotic assertions follow from the foregoing proof, not from finite enumeration or simulation.

## Relationship to prior work

Saiki, Takahasi and Yorke introduce the twisted baker map and establish simultaneous density and equidistribution of periodic points of real and nonreal multiplier type, Bernoulli coding, and nonuniform expansion among periodic points. Those results supply the dynamical setting and symbolic cylinder formula but do not state the joint finite-time *singular-value* law for normalized Lebesgue sampled orbit segments, its all-dimensional covariance, or the mean top-singular-value correction. An earlier three-dimensional calculation of weakest expansion under *uniform periodic-point counting* has the same Gaussian covariance pattern, but concerns a different ensemble, a single weakest eigenvalue statistic, and one dimension. It neither implies almost-sure typical-orbit exponents nor the joint all-dimensional singular-value order-statistic law. Finite-state Markov-chain martingale central limit methods are classical and are used as tools rather than claimed as new.

## Limitations

All results are for a fixed finite dimension and normalized Lebesgue initialization. They concern singular values of finite-time derivatives and not the possibly complex eigenvalues of periodic return matrices. No uniform-in-dimension central limit rate, large-deviation law, or phase-space-specific orbitwise central limit theorem beyond Lebesgue-a.e. exponents is asserted. The limit variance identity can also be recognized as an application of established Markov-additive techniques; publication priority for the specific application should be checked against potentially unindexed literature. Numerical tests are only consistency checks.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first version 2022-02-09; *Nonlinearity* 36 (2023), 1776–1788. Full text: https://arxiv.org/html/2202.04304 ; submission record: https://arxiv.org/abs/2202.04304 .
2. M. Gordin and M. Peligrad, *On the functional central limit theorem via martingale approximation*, arXiv:0910.3448 (2009). https://arxiv.org/abs/0910.3448 . Classical martingale-approximation background, not a claim of specific twisted-baker results.
3. G. L. Jones, *On the Markov chain central limit theorem*, arXiv:math/0409112 (2004). https://arxiv.org/abs/math/0409112 . General Markov-additive central limit theory.
