# Sharp EF1 survival rates for balanced exponential lottery allocations

## Finding

Fix integers \(n\geq2\) and \(r\geq2\). Assign \(nr\) distinct goods **before any values are observed** so that each of the \(n\) agents receives exactly \(r\) goods. All \(n^2r\) agent-good values are independent \(\operatorname{Exp}(1)\) random variables, and utilities are additive. In particular, the fixed allocation is envy-free in expectation.

Let \(P_{n,r}\) be the probability that this fixed allocation is envy-free up to one good (EF1) after realization. Define
\[
\lambda_t=\frac{t+1}{t},\qquad
 a_t=\prod_{\substack{1\le j\le r-1\\ j\ne t}}
 \frac{\lambda_j}{\lambda_j-\lambda_t},\qquad 1\le t\le r-1,
\]
and let \(S\sim\operatorname{Gamma}(r,1)\), with density \(s^{r-1}e^{-s}/(r-1)!\) on \(s>0\). Then the **exact finite probability** is
\[
P_{n,r}=q_{n,r}^{\,n},\quad
q_{n,r}=\frac{1}{(r-1)!}\int_0^\infty
s^{r-1}e^{-s}\left(1-\sum_{t=1}^{r-1}a_t e^{-\lambda_t s}\right)^{n-1}\,ds.
\]
It is a rational number computable from the finite formula
\[
q_{n,r}=\sum_{\substack{k_1,\dots,k_{r-1}\ge0\\K:=\sum_t k_t\le n-1}}
(-1)^K\binom{n-1}{K}\frac{K!}{\prod_t k_t!}
\frac{\prod_t a_t^{k_t}}{(1+\sum_t k_t\lambda_t)^r}.
\]
For each **fixed** \(r\ge2\) as \(n\to\infty\), set
\[
\theta_r=\frac{r-1}{r},\qquad
K_r=\frac{\Gamma(\theta_r)}{(r-1)!}
\left(\frac{r-1}{r}\right)^r
(r-1)^{-(r-1)\theta_r}.
\]
Then \(K_r>0\), and the sharp asymptotic is
\[
\boxed{\quad P_{n,r}^{1/n}=q_{n,r}\sim K_r\,n^{-\theta_r}(\log n)^{r-1}.\quad}
\]
Equivalently,
\[
\log P_{n,r}=-\theta_r n\log n+(r-1)n\log\log n+n\log K_r+o(n).
\]
The statement is **not** a relative \(1+o(1)\) approximation of \(P_{n,r}\) itself. For the same fixed allocation, the ex-post envy-free probability without any deletion is exactly \(n^{-n}\).

In the first nontrivial case of two goods per agent, the finite expression simplifies to
\[
q_{n,2}=\sum_{j=0}^{n-1}\frac{(-1)^j\binom{n-1}{j}}{(2j+1)^2}
=\frac{1}{4}B\left(\frac12,n\right)
\sum_{j=0}^{n-1}\frac{2}{2j+1},
\quad
q_{n,2}\sim \frac{\sqrt\pi}{4}\frac{\log n}{\sqrt n}.
\]
For instance, \(P_{2,2}=64/81\) and \(P_{3,2}=(184/225)^3\).

## Assumptions and scope

The allocation is fixed independently of all valuations, contains exactly \(r\) goods per agent, and does not discard goods. Every agent has her **own independent** exponential valuation for every good, including goods assigned to others. This is not the distinct model in which all agents see a single shared random realized value for each good. Ex-post EF1 means that for every ordered pair of different agents \((i,j)\), there exists at most one good in the recipient \(j\)'s bundle whose removal removes agent \(i\)'s envy. For nonnegative additive values, removing the good that \(i\) values most is optimal. The exponential rate is one by normalization; any common positive exponential scale gives the same probabilities. The asymptotic limit fixes \(r\) before allowing \(n\) to increase; it does not cover growing \(r\), correlated values, other distributions, or allocations conditioned on observed values.

## Proof

**1. Factorization by independent valuation rows.** Fix an agent \(i\). Her utility for her own \(r\)-good bundle is \(S\sim\operatorname{Gamma}(r,1)\). For each other bundle, list its \(r\) values for this agent as \(X_{(1)}\le\cdots\le X_{(r)}\). The least utility remaining after deleting one item is
\[
Y=X_{(1)}+\cdots+X_{(r-1)}.
\]
The \(n-1\) residual values \(Y\) are iid and independent of \(S\). If \(F_r(s)=\Pr(Y\le s)\), the probability that this particular agent is EF1-satisfied is
\[
q_{n,r}=\mathbb E[F_r(S)^{n-1}].
\]
Different agents use disjoint independent valuation rows, hence their EF1-satisfaction events are independent and \(P_{n,r}=q_{n,r}^{n}\). This justifies the complete-allocation probability, not merely a one-agent surrogate.

**2. Exact residual law.** For iid rate-one exponentials, the spacings \(D_h=X_{(h)}-X_{(h-1)}\), with \(X_{(0)}=0\), are independent exponentials of rates \(r-h+1\). Therefore
\[
Y=\sum_{h=1}^{r-1}(r-h)D_h
\ \stackrel{d}{=}\ \sum_{t=1}^{r-1} E_t,
\qquad E_t\sim\operatorname{Exp}(\lambda_t),
\]
with independent \(E_t\) and distinct \(\lambda_t=(t+1)/t\). Partial fractions of
\(\prod_t\lambda_t/(\lambda_t+z)\), the Laplace transform of \(Y\), give
\[
\Pr(Y>s)=\sum_{t=1}^{r-1}a_t e^{-\lambda_t s}
\]
for \(s\ge0\). The product defining \(a_t\) in the finding is the usual residue coefficient. This proves the exact integral. Expanding its finite integer power by the multinomial theorem and using the gamma Laplace transform
\(\mathbb E[e^{-uS}]=(1+u)^{-r}\) gives the rational sum, including all signs and multinomial factors.

**3. Precise upper-tail coefficient.** The smallest rate is
\(\alpha=\lambda_{r-1}=r/(r-1)\), and its coefficient equals
\[
a_{r-1}=\prod_{j=1}^{r-2}\frac{\lambda_j}{\lambda_j-\alpha}
=(r-1)^{r-2}\prod_{j=1}^{r-2}\frac{j+1}{r-1-j}
=(r-1)^{r-1}=:C.
\]
For \(r=2\) the product is empty and \(\Pr(Y>s)=e^{-2s}\) exactly. For \(r>2\), the remaining exponential rates are strictly larger than \(\alpha\), so
\[
1-F_r(s)=Ce^{-\alpha s}\bigl(1+O(e^{-\eta s})\bigr)
\quad (s\to\infty)
\]
for some \(\eta>0\) depending only on \(r\).

**4. Sharp Laplace asymptotics.** Put \(\theta=1/\alpha=(r-1)/r\) and substitute \(z=Cn e^{-\alpha s}\) into the exact integral for \(q_{n,r}\). In the region with \(z\) bounded away from zero and infinity, the preceding tail estimate yields
\(F_r(s)^{n-1}\to e^{-z}\) uniformly on compact \(z\)-intervals, while
\[
s=\alpha^{-1}\log(Cn/z),\quad
s^{r-1}e^{-s}\,|ds|
=\frac{(Cn)^{-\theta}}{\alpha^r}
 z^{\theta-1}[\log(Cn/z)]^{r-1}\,dz.
\]
For completeness, localization is justified as follows. For sufficiently large fixed \(s_0\), the tail \(1-F_r(s)\) lies between two positive constant multiples of \(e^{-\alpha s}\) for \(s\ge s_0\). Hence the transformed integrand is dominated by a constant multiple of
\(z^{\theta-1}e^{-c z}(1+|\log z|^{r-1})\) after division by \((\log n)^{r-1}\), on the region \(s\ge s_0\). That envelope is integrable at zero and infinity. The omitted fixed interval \(0\le s<s_0\) is exponentially small in \(n\), because \(F_r(s_0)<1\). Dominated convergence therefore gives
\[
q_{n,r}\sim \frac{C^{-\theta}\Gamma(\theta)}{(r-1)!\alpha^r}
 n^{-\theta}(\log n)^{r-1}=K_r n^{-\theta}(\log n)^{r-1}.
\]
Taking the logarithm of \(q_{n,r}^n\) gives the asserted \(o(n)\)-accurate log-probability statement.

**5. The two-good identity and exact EF benchmark.** For \(r=2\), \(Y\sim\operatorname{Exp}(2)\) and
\[
q_{n,2}=\int_0^\infty se^{-s}(1-e^{-2s})^{n-1}\,ds.
\]
The substitution \(u=e^{-2s}\) yields one quarter of the logarithmic beta integral, giving the formula involving \(B(1/2,n)\) and the explicit odd-harmonic sum. Standard gamma-ratio and harmonic-sum asymptotics give \(\sqrt\pi\log n/(4\sqrt n)\). Without deleting any item, agent \(i\)'s valuations of all \(n\) bundles are iid continuous gamma variables. Her own bundle is the maximum with probability exactly \(1/n\); independence of the \(n\) valuation rows yields ex-post EF probability \(n^{-n}\).

## Verification

Run the standalone Python 3 program `check.py` with only the standard library. It reconstructs the exponential partial-fraction coefficients and the independent multinomial/gamma exact rational sum, numerically integrates the residual cdf against the own-bundle gamma density, and checks the independent beta/harmonic identity when \(r=2\). Its deterministic seeded Monte Carlo tests are supplementary sanity checks and are not used for the theorem. Verified cases are \(2\le r\le4\) and \(2\le n\le6\), as well as several explicit small rational anchors. The proof is the analytic argument above; numerical checks do not prove an infinite-parameter result.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1 (first submitted October 26, 2026), study ex-post exact envy-freeness of fixed allocations under uncertain valuations. Their Sections 4 and 7 establish optimality statements for ex-ante EF allocations; their conclusion explicitly identifies EF1 as future work. The present statement instead computes and sharply estimates the **probability of EF1 under a fixed balanced allocation** for independent exponential item values. It is neither a corollary of a theorem about exact EF nor an optimality claim among all possible fixed allocations.

Aloisio, Bilò, Caruso, Flammini, and Vinci (AAMAS 2024) study expected maximum envy under random valuations, especially bounded distributions and optimization of allocations. Their three-page proceedings text does not state the exact EF1 probability or the fixed-\(r\) asymptotics above. Cohen, Teh, and Wooldridge, arXiv:2609.28333 (September 23, 2026), study worst-case guarantees of **randomized online allocation algorithms** against adversaries; their abstract does not imply a distribution-specific fixed-allocation exact probability. Relevant published binary/shared-item EF1 results concern different dependence models or parameter regimes. These comparisons are scientific-scope distinctions, not claims of exhaustive publication uniqueness.

## Limitations

This result assumes independent unbounded exponential values, precommitted equal-size bundles, and fixed \(r\). It does not identify an optimal allocation under asymmetric item distributions, measure expected envy, or give a fairness guarantee for a procedure that observes values before allocating. It does not apply to shared-realization item values. For growing \(r\), the displayed fixed-\(r\) asymptotic need not hold uniformly. The results have not undergone independent validation. Literature searches and accessible primary-text inspection cannot exclude all unindexed equivalent work.

## References

1. Ayumi Igarashi and Yeeseok Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1, October 26, 2026. https://arxiv.org/html/2610.34906
2. Alessandro Aloisio, Vittorio Bilò, Antonio Mario Caruso, Michele Flammini, and Cosimo Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS 2024, pp. 2120–2122. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p2120.pdf
3. Saar Cohen, Nicholas Teh, and Michael Wooldridge, *Online Fair Division Against an Oblivious Adversary*, arXiv:2609.28333, September 23, 2026. https://arxiv.org/abs/2609.28333
