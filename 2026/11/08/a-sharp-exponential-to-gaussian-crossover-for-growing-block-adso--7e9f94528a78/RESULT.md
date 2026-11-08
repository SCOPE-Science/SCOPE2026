# A sharp exponential-to-Gaussian crossover for growing-block adsorption near saturation

## Finding

At each integer time, sample uniformly and independently a set of \(k\) distinct sites from a complete substrate of \(kn\) sites. Deposit a \(k\)-mer if and only if all the sampled sites are vacant. For integers \(0\le u<n\), let \(T_{n,k,u}\) be the number of proposals, including rejected ones, until precisely \(n-u\) successful deposits have occurred. Set
\[
r=u+1,\qquad \pi_{n,k,u}=\frac{\binom{kr}{k}}{\binom{kn}{k}}.
\]

**Theorem (joint near-saturation scaling).** Suppose \(n\to\infty\), the integer block size \(k=k_n\to\infty\), and \(u=u_n\ge0\) satisfies \(u_n=o(n)\).

If \(u_n/k_n\to\theta\in[0,\infty)\), put \(q_0=0\) and \(q_\theta=e^{-1/\theta}\) for \(\theta>0\), interpreting \(q_\theta^0=1\) even at \(\theta=0\). With independent unit-rate exponential variables \(E_0,E_1,\ldots\),
\[
\pi_{n,k,u}T_{n,k,u}\ \Longrightarrow\ Z_\theta:=\sum_{j=0}^\infty q_\theta^j E_j.
\]
For each \(\theta\in[0,\infty)\), the first two moments converge as well:
\[
\pi_{n,k,u}\,\mathbb E T_{n,k,u}\to\frac{1}{1-q_\theta},\qquad
\pi_{n,k,u}^{\,2}\operatorname{Var}(T_{n,k,u})\to\frac{1}{1-q_\theta^2}.
\]
For \(0<\theta<\infty\), this non-Gaussian law is characterized by
\[
\mathbb E e^{-s Z_\theta}=\prod_{j=0}^\infty(1+s q_\theta^j)^{-1}\quad(s\ge0),\qquad
\kappa_m(Z_\theta)=\frac{(m-1)!}{1-q_\theta^m}\quad(m\ge1).
\]
Here \(\kappa_m\) denotes the \(m\)-th cumulant. At \(\theta=0\) the limit is a single unit-rate exponential law.

If instead \(u_n/k_n\to\infty\), then
\[
\mathbb E T_{n,k,u}\sim \frac{u}{k\pi_{n,k,u}},\qquad
\operatorname{Var}(T_{n,k,u})\sim\frac{u}{2k\pi_{n,k,u}^{\,2}},
\]
and
\[
\frac{T_{n,k,u}-\mathbb E T_{n,k,u}}
{\sqrt{\operatorname{Var}(T_{n,k,u})}}
\Longrightarrow N(0,1).
\]
In this Gaussian regime, the Kolmogorov distance to \(N(0,1)\) is \(O(\sqrt{k/u})\), with an absolute implicit constant. Thus the ratio \(u/k\) is the transition parameter between domination by the final waiting time, a non-Gaussian geometric-exponential sum, and fluctuations created by many comparable waiting times. The standardized law of \(Z_\theta\) itself approaches \(N(0,1)\) as \(\theta\to\infty\).

## Assumptions and scope

The substrate is a complete graph only in the sense that every \(k\)-subset is equally eligible for a proposal; there is no nearest-neighbor or geometric exclusion rule. Each proposal independently chooses its \(k\)-subset uniformly without replacement within the proposal. Occupation is permanent, and the process starts vacant. Time counts **all** proposals, including failures. The result concerns triangular arrays \((n,k_n,u_n)\) with \(u_n=o(n)\); no bound on \(k_n/n\) is imposed. \(N(0,1)\) denotes the standard normal law.

## Proof

**1. Exact waiting-time factorization.** If \(j\) whole \(k\)-site blocks' worth of vacancies remain, there are exactly \(kj\) vacant sites. The success probability is
\[
p_{n,j}=\frac{\binom{kj}{k}}{\binom{kn}{k}},\qquad 1\le j\le n.
\]
Independence of proposals and the fact that this probability depends only on \(j\) give the exact identity
\[
T_{n,k,u}\ \overset{d}{=}\ \sum_{j=r}^{n}G_{n,j},\qquad
G_{n,j}\ \text{independent with}\quad
\Pr(G_{n,j}=h)=(1-p_{n,j})^{h-1}p_{n,j}\quad(h\ge1).
\]
Define \(\pi=p_{n,r}\) and
\[
a_{n,\ell}=\frac{p_{n,r}}{p_{n,r+\ell}}
=\prod_{i=0}^{k-1}\frac{kr-i}{k(r+\ell)-i},\qquad 0\le\ell\le n-r.
\]
For all \(\ell\ge0\),
\[
0<a_{n,\ell}\le\left(\frac{r}{r+\ell}\right)^k.
\tag{1}
\]
Indeed each numerator/denominator ratio is at most \(r/(r+\ell)\). Also \(\pi\le(r/n)^k\to0\), because \(r=o(n)\) and \(k\to\infty\).

**2. Bounded \(u/k\).** For any fixed nonnegative integer \(\ell\), if \(r/k\to\theta\in(0,\infty)\), the logarithm of the preceding product obeys
\[
\log a_{n,\ell}
=-\sum_{i=0}^{k-1}\log\left(1+\frac{\ell}{r-i/k}\right)
\longrightarrow-\frac{\ell}{\theta}.
\]
If \(r/k\to0\), inequality (1) instead implies \(a_{n,\ell}\to0\) for every \(\ell\ge1\), whereas \(a_{n,0}=1\). In either case, for each fixed \(\ell\) the success probability \(p_{n,r+\ell}\to0\), and so
\[
\pi G_{n,r+\ell}
=a_{n,\ell}\big(p_{n,r+\ell}G_{n,r+\ell}\big)
\Longrightarrow q_\theta^\ell E_\ell,
\]
with joint convergence for any finite number of indices because the waits are independent.

The discarded tail is uniformly controlled using (1): for any integer \(L\ge1\),
\[
\mathbb E\left[\pi\sum_{\ell=L}^{n-r}G_{n,r+\ell}\right]
=\sum_{\ell=L}^{n-r}a_{n,\ell}
\le\left(1+\frac Lr\right)^{-k}
+\frac{r}{k-1}\left(1+\frac Lr\right)^{1-k}.
\tag{2}
\]
When \(r/k\to\theta>0\), the limit superior of the right side is at most \((1+\theta)e^{-L/\theta}\), which vanishes with \(L\). When \(r/k\to0\), taking \(L=1\) already makes the bound vanish. Truncation and Markov's inequality therefore prove the asserted weak convergence, including \(\theta=0\).

**3. Moment convergence.** Let \(R_{m,n}=\sum_{\ell=0}^{n-r}a_{n,\ell}^m\). Exact geometric moments give
\[
\pi\mathbb ET_{n,k,u}=R_{1,n},\qquad
\pi^2\operatorname{Var}(T_{n,k,u})=R_{2,n}-\pi R_{1,n}.
\tag{3}
\]
The same tail estimate (2), with squared weights bounded by unsquared ones, yields \(R_{m,n}\to(1-q_\theta^m)^{-1}\) for \(m=1,2\) in the finite-\(\theta\) regime. Since \(\pi\to0\), (3) yields the stated moments. The independent exponential sum has Laplace product \(\prod_{j\ge0}(1+s q_\theta^j)^{-1}\); differentiation of its cumulant generating function near zero gives \(\kappa_m=(m-1)!/(1-q_\theta^m)\).

**4. Gaussian regime.** Suppose \(r/k\to\infty\), and write \(h=k/r\to0\). Uniformly for \(x\) in compact subsets of \([0,\infty)\), the product defining \(a_{n,\ell}\) satisfies
\[
\log a_{n,\lfloor x/h\rfloor}=-x+o(1).
\]
For every fixed \(m\in\{1,2,3\}\), (1) controls the Riemann-sum tails after \(\ell\ge L/h\):
\[
h\sum_{\ell\ge L/h}\left(1+\frac\ell r\right)^{-mk}
\le h\left(1+\frac{\lceil L/h\rceil}{r}\right)^{-mk}
+\frac{k}{mk-1}\left(1+\frac{\lceil L/h\rceil}{r}\right)^{1-mk}
\longrightarrow \frac{e^{-mL}}m.
\]
Since \((n-r)h\to\infty\), dominated Riemann summation proves
\[
R_{m,n}\sim\frac{r}{mk}\qquad(m=1,2,3).
\tag{4}
\]
Equations (3), (4), \(\pi\to0\), and \(r\sim u\) give the mean and variance asymptotics.

For a geometric \(G\) of parameter \(p\), the third absolute centered moment of \(pG\) is bounded uniformly over \(0<p\le1\), since \(\Pr(pG>t)\le e^{1-t}\) for \(t\ge0\). Thus the third absolute moments of the independent centered summands \(\pi(G_{n,r+\ell}-\mathbb EG_{n,r+\ell})\) sum to at most \(C R_{3,n}\), for an absolute \(C\). By the independent-summand Berry--Esseen inequality and (3)--(4), the distance to normal is at most
\[
C'\frac{R_{3,n}}{(R_{2,n}-\pi R_{1,n})^{3/2}}
=O\left(\sqrt{\frac{k}{r}}\right)
=O\left(\sqrt{\frac{k}{u}}\right).
\]
This proves both the quantitative Gaussian claim and weak convergence. Applying the same bound to the weighted exponential sum defining \(Z_\theta\), as \(q_\theta\uparrow1\), proves its standardized Gaussian limit. \(\square\)

## Verification

The standalone standard-library program `verify.py` independently enumerates finite uniform proposal outcomes, compares a finite-state absorbing-chain distribution to a convolution of geometric waiting times, checks the exact scaled-moment identity (3), and tests numerical convergence of the critical and Gaussian rate profiles. Its recorded execution passed 2,249 exact and diagnostic assertions. The enumeration is finite and is **not** offered as a proof of the asymptotic statements; the derivations above provide the infinite-parameter arguments.

## Relationship to prior work

Turban's 2019 public preprint establishes the complete-graph \(k\)-mer model, exact finite-parameter waiting-time distribution and fixed-\(k\) coverage limits, including a fixed number of remaining vacancies. Those exact formulas are a crucial starting point; the claim here is only the **joint limit when both \(k\) and \(u\) grow**, the non-Gaussian family at \(u/k\to\theta\), and the sharp Gaussian scale \(u/k\to\infty\). It is not a claim to a new finite-time generating function. Vajna, Tóth and Kertész (2012) already obtain the *same abstract geometric-exponential sum law* in a task-priority model. The probability distribution considered in isolation is therefore not asserted to be new; its emergence as this adsorption crossover and the quantitative boundary are the claimed additions.

## Limitations

The proposal sets are uniformly drawn from a complete substrate; no spatial constraints, preferential selection, repeated-site selection within a proposal, or changing rules are covered. The assumption \(u=o(n)\) excludes macroscopic vacancy fractions. The critical regime has weak convergence and moment limits, but no claimed general uniform Kolmogorov rate. The rate bound in the Gaussian regime concerns its centered and variance-standardized *discrete-time* coverage time.

## References

1. Loïc Turban, *Random sequential adsorption of \(k\)-mers on the fully-connected lattice: probability distributions of the covering time and extreme value statistics*, first posted August 2, 2019, arXiv:1908.00940, https://arxiv.org/abs/1908.00940. See especially Section 2.1, Eq. (3.3) and Section 4.4.
2. Szabolcs Vajna, Bálint Tóth and János Kertész, *Modelling bursty time series*, first posted November 6, 2012, arXiv:1211.1175, https://arxiv.org/abs/1211.1175. See Section 3.2 and Appendix A.1 for the geometric-exponential sum appearing in another model.
