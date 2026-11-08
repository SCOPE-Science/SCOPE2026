# Independent endpoint Poisson laws and the sharp singleton-gap scale in uniform set partitions

## Finding

Let \(\Pi_n\) be a uniformly selected set partition of \([n]=\{1,\ldots,n\}\). Put \(\eta_{n,i}=1\) when \(\{i\}\) is a singleton block, and zero otherwise. Let \(B_n\) be the \(n\)-th Bell number and set \(a_n=B_{n-1}/B_n\).

For every integer \(n\geq1\), define two random point measures on \([0,\infty)\):
\[
\Xi_n^-=\sum_{i=1}^{n}\eta_{n,i}\,\delta_{a_n(i-1)},\qquad
\Xi_n^+=\sum_{i=1}^{n}\eta_{n,i}\,\delta_{a_n(n-i)}.
\]
As \(n\to\infty\), the pair \((\Xi_n^-,\Xi_n^+)\) converges jointly in distribution, with the vague topology on locally finite point measures, to two **independent Poisson point processes of unit intensity** on \([0,\infty)\).

Let \(U_n\) be the number of labels preceding the smallest singleton; let \(V_n\) be the number following the largest singleton. Define both as \(n\) when there are no singletons. If \(E_1,E_2\) are independent exponential random variables of mean one, then
\[
(a_n U_n,a_n V_n)\ \Longrightarrow\ (E_1,E_2),\qquad
a_n\mathbb E U_n\longrightarrow1,\quad
a_n\mathbb E V_n\longrightarrow1.
\]
In particular, writing \(W(n)\) for the positive solution of \(W(n)e^{W(n)}=n\),
\[
\mathbb E U_n\sim\mathbb E V_n\sim \frac{n}{W(n)}.
\]
The average smallest singleton label and average largest singleton label (with the above convention when none exists) are therefore respectively \(1+(1+o(1))n/W(n)\) and \(n-(1+o(1))n/W(n)\).

The Bell-ratio mechanism also yields an exact finite-sample contrast: for distinct labels \(i\ne j\) and \(n\ge2\),
\[
\operatorname{Cov}(\eta_{n,i},\eta_{n,j})
=\frac{B_{n-2}}{B_n}-\left(\frac{B_{n-1}}{B_n}\right)^2>0.
\]
Thus distinct singleton indicators are positively correlated at every finite size, while the two separated endpoint point processes have independent limits.

## Assumptions and scope

Each partition of the labeled set \([n]\) has probability \(1/B_n\); there is no parameter, restriction on block sizes, or conditioning on the presence of singletons. Point-process convergence concerns **fixed bounded coordinate windows** after rescaling by \(a_n\), not all labels simultaneously. All limits are as the positive integer \(n\) tends to infinity.

## Proof

**Prescribed singletons and exact factorial moments.** For any fixed set \(J\subseteq[n]\) of \(r\) distinct labels, forcing every \(\{j\}\), \(j\in J\), to be a block leaves precisely \(B_{n-r}\) unrestricted partitions of the other labels. Thus
\[
\Pr(\eta_{n,j}=1\ \text{for all }j\in J)=\frac{B_{n-r}}{B_n}.
\]
For pairwise disjoint deterministic subsets \(A_{1,n},\ldots,A_{k,n}\subseteq[n]\), let \(X_{j,n}=\sum_{i\in A_{j,n}}\eta_{n,i}\) and \(m_{j,n}=|A_{j,n}|\). For all fixed nonnegative integers \(r_1,\ldots,r_k\), with \(r=\sum_jr_j\le n\),
\[
\mathbb E\prod_{j=1}^k(X_{j,n})_{\underline{r_j}}
=\frac{B_{n-r}}{B_n}\prod_{j=1}^{k}(m_{j,n})_{\underline{r_j}}. \tag{1}
\]
Here \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\) and \((x)_{\underline0}=1\).

**Bell-ratio asymptotics.** Define \(N_n=n/W(n)\), so \(N_n\log N_n=n\). The classical Bell-number saddle-point approximation gives
\[
B_n=\frac{N_n^n e^{N_n-n-1}}{\sqrt{1+\log N_n}}
\left(1+O\!\left(\sqrt{\frac{\log n}{n}}\right)\right).
\]
Taking the ratio at \(n-r\) and \(n\), for every fixed integer \(r\ge0\), yields
\[
\frac{B_{n-r}}{B_n}
=N_n^{-r}\left(1+O_r\!\left(\sqrt{\frac{\log n}{n}}\right)\right).
\tag{2}
\]
Indeed the derivative of the logarithm of the displayed saddle-point main factor is \(\log N_x+O(x^{-1})\), and a fixed change in \(x\) changes \(\log N_x\) by \(O_r(x^{-1})\). Consequently
\[
a_n\sim\frac{W(n)}n,\quad
n a_n\sim W(n)\longrightarrow\infty,\quad
\frac{B_{n-r}}{B_n a_n^r}=1+O_r\!\left(\sqrt{\frac{\log n}{n}}\right).
\tag{3}
\]

**Joint endpoint processes.** Fix a finite list of bounded intervals in the left and right rescaled coordinates whose boundaries have zero limiting Lebesgue measure. Subdivide overlapping intervals within each endpoint into disjoint atoms. The corresponding sets of original labels at opposite endpoints are disjoint for all sufficiently large \(n\), because \(n a_n\to\infty\). An atom of length \(t_j\) contains \(m_{j,n}\) labels with \(a_n m_{j,n}\to t_j\). Substituting (3) into (1) gives
\[
\mathbb E\prod_j(X_{j,n})_{\underline{r_j}}
\longrightarrow\prod_j t_j^{r_j}.
\tag{4}
\]
These are all joint factorial moments of independent Poisson variables of means \(t_j\). The Poisson law is moment-determinate; bounded first moments give tightness for each finite vector. The factorial-moment criterion therefore yields convergence of every finite vector of disjoint-atom counts, and the standard locally finite point-process criterion gives the claimed joint convergence.

The event \(a_n U_n>x\) is the absence of a singleton among the first \(\lfloor x/a_n\rfloor+1\) labels, up to an endpoint convention of at most one label; similarly for \(V_n\). Applying the independent Poisson void-probability limits gives joint survival probabilities \(e^{-x-y}\) for all \(x,y\ge0\), and hence joint convergence to \((E_1,E_2)\). The number of all singletons diverges in probability, so the convention when none exists does not affect the limit; this also follows from the next paragraph.

**Convergence of the means.** Set \(S_n=\sum_i\eta_{n,i}\) and \(\lambda_n=n a_n\). Formula (1) gives, for each fixed \(r\le4\),
\[
\mathbb E(S_n)_{\underline r}
=(n)_{\underline r}\frac{B_{n-r}}{B_n}
=\lambda_n^r\left(1+O_r\!\left(\sqrt{\frac{\log n}{n}}\right)\right).
\tag{5}
\]
By expressing ordinary powers using falling factorials and expanding around \(\lambda_n\), (5) implies
\[
\operatorname{Var}(S_n)=\lambda_n+o(\lambda_n^2),\qquad
\mathbb E(S_n-\lambda_n)^4=O(\lambda_n^2).
\tag{6}
\]
More explicitly, the conversion between falling-factorial and ordinary moments gives \(\mathbb E(S_n-\lambda_n)^4=3\lambda_n^2+\lambda_n+O(\lambda_n^4\sqrt{\log n/n})\); the error is \(o(\lambda_n^2)\), since \(\lambda_n=O(\log n)\). Consequently \(S_n/\lambda_n\to1\) in probability and \(\Pr(S_n<\lambda_n/2)=O(\lambda_n^{-2})\).

Conditional on \(S_n=s\), the singleton-label set is a uniformly selected \(s\)-subset of \([n]\). The expected gap preceding its minimum (or \(n\) if \(s=0\)) equals \((n-s)/(s+1)\); the same holds for the gap following its maximum. Therefore, exactly,
\[
\mathbb E U_n=\mathbb E V_n
=(n+1)\,\mathbb E\frac1{S_n+1}-1. \tag{7}
\]
On \(S_n\ge\lambda_n/2\), the quantity \(\lambda_n/(S_n+1)\) is bounded by \(2\) and converges in probability to \(1\). On its complement, its expectation is at most \(\lambda_n\Pr(S_n<\lambda_n/2)=O(\lambda_n^{-1})\). Hence \(\lambda_n\mathbb E[1/(S_n+1)]\to1\). Multiplying (7) by \(a_n=\lambda_n/n\) gives \(a_n\mathbb E U_n\to1\) and the identical assertion for \(V_n\). Also \(\Pr(S_n=0)\le\Pr(S_n<\lambda_n/2)\to0\).

**Finite positive dependence.** The \(r=1,2\) instance of the prescribed-singleton identity gives the covariance formula. Strict positivity follows from Dobinski's representation \(B_m=e^{-1}\sum_{k\ge0}k^m/k!\), which is a nondegenerate positive moment sequence; strict Cauchy–Schwarz yields \(B_{n-1}^2<B_{n-2}B_n\) for \(n\ge2\).

## Verification

Run `python check.py` with Python 3 and no third-party dependencies. The program independently enumerates all 4,140 set partitions at size \(8\), as well as smaller sizes, and tests the prescribed-singleton and joint factorial-moment identities. It checks exact expectation formulas, strict Bell-number log-convexity and finite-size diagnostics through \(n=600\). Its reported successful execution comprises 1,106 checks. These finite computations verify bounded cases and formulas only; the infinite limit and expectation asymptotic rely on the proof above, not on extrapolation from numerical data.

## Relationship to prior work

Sun and Wu, *The largest singletons of set partitions* (arXiv:1007.1341v1, 2010), establish exact recurrences, enumerations and finite expectations for the largest and smallest singleton labels. Their Remark 3.11 explicitly raises asymptotic expressions for these expectations. The present claim adds a joint independent endpoint point-process limit and the precise \(n/W(n)\) expected-gap scale. The finite Bell-number identities are treated as background ingredients, not independently new identities.

Arratia and Tavaré, *Independent Process Approximations for Random Combinatorial Structures* (Advances in Mathematics 104, 1994; arXiv:1308.3279), give component-size-count approximations for random assemblies, including set partitions. Their component process indexes counts by **block size**; it is different from a point process of **singleton labels at the two ends**. The known approximation framework is relevant and could imply related positional results after additional exchangeability and scaling arguments.

The Bell-number asymptotics used here are classical, tabulated in NIST DLMF §26.7(iv), formula 26.7.7. The claimed contribution concerns the derived positional limit and endpoint mean gap; it is not a new Bell-number asymptotic.

## Limitations

No quantitative total-variation bound or convergence rate is established. Point-process convergence is local on fixed rescaled windows, not uniform over windows whose lengths diverge. The independent limiting point processes do not make distinct singleton indicators independent at finite \(n\). Historical priority is not independently certified: an implicit derivation from general exchangeable sparse-point-process results or older random-set-partition theory remains possible. The theorem and checker have not received independent audit.

## References

1. Y. Sun and X. Wu, *The largest singletons of set partitions*, arXiv:1007.1341v1 (first posted 2010-07-08), https://arxiv.org/html/1007.1341v1.
2. R. Arratia and S. Tavaré, *Independent Process Approximations for Random Combinatorial Structures*, Advances in Mathematics 104 (1994), 90–154; arXiv:1308.3279 (open manuscript posted 2013), https://arxiv.org/html/1308.3279v1.
3. NIST Digital Library of Mathematical Functions, §26.7(iv), Bell-number asymptotic approximation, https://dlmf.nist.gov/26.7.
4. J. H. Goh and E. Schmutz, *Random Set Partitions*, SIAM Journal on Discrete Mathematics (1994), https://doi.org/10.1137/S0895480190186974 (only the abstract and bibliographic description were reviewed).
