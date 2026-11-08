# Stationary Ornstein–Uhlenbeck fluctuations in the critical careless coupon collector

## Finding

For fixed \(c>0\), let \(n\to\infty\) through integers \(n>c\), and put \(p_n=c/n\). In the *post-loss careless coupon collector* with \(n\) equally likely types, each step draws one uniformly chosen type, adds it to the present set, and then independently removes every present type with probability \(p_n\). Write \(K^{(n)}_j\) for the number of present types after step \(j\), started in the unique stationary law, and put
\[
q_n=1-p_n,\qquad a_n=q_n(1-1/n),\qquad
\mu_n=\frac{nq_n}{np_n+q_n},\qquad
Y_n(t)=\frac{K^{(n)}_{\lfloor nt\rfloor}-\mu_n}{\sqrt n}.
\]
For every fixed \(T<\infty\), \(Y_n\) converges in distribution in \(D([0,T],\mathbb R)\) (Skorokhod \(J_1\) topology) to the **stationary** Ornstein–Uhlenbeck process
\[
 dY(t)=-(1+c)Y(t)\,dt+\frac{\sqrt{c(c+2)}}{1+c}\,dB(t),
 \qquad Y(0)\sim \mathcal N\left(0,\frac{c(c+2)}{2(1+c)^3}\right),
\]
where \(Y(0)\) and the standard Brownian motion \(B\) are independent. In particular, for \(s,t\ge0\),
\[
 \operatorname{Cov}(Y(s),Y(t))
 =\frac{c(c+2)}{2(1+c)^3}e^{-(1+c)|t-s|}.
\]
Thus the exact stationary fluctuation variance is lower than the independent-Bernoulli approximation by the factor \((c+2)/(2(1+c))\), strictly between \(1/2\) and \(1\). The result concerns typical equilibrium fluctuations, **not** exponentially rare full-collection times.

## Assumptions and scope

The number of types is an integer \(n\ge2\). Drawing is uniform and independent over steps; losses occur *after* each draw, independently across currently held types and time steps. For the finite identities below, any \(0<p<1\) is permitted, with \(q=1-p\). For the functional limit, \(c>0\) is fixed and \(p=c/n<1\), and the **initial set has the stationary distribution**. The count chain is irreducible and aperiodic on \(\{0,\ldots,n\}\), so stationarity is unambiguous. At every scale, the threshold \(K=n\) is not absorbing.

## Proof

**1. Conditional dynamics.** Given \(K_j=k\), the next draw adds a new type with probability \(b=(n-k)/n\). With \(J\sim\operatorname{Bernoulli}(b)\), the next count, conditional on \(J\), is \(\operatorname{Binomial}(k+J,q)\). Consequently,
\[
\mathbb E[K_{j+1}\mid K_j=k]=q(k+b)=ak+q,
\qquad a=q(1-1/n),
\]
\[
\operatorname{Var}(K_{j+1}\mid K_j=k)
=pq(k+b)+q^2b(1-b)=:V_{n,p}(k).
\]
The exact stationary mean is \(\mu=q/(1-a)=nq/(np+q)\). Also, for every integer \(h\ge0\), iterated conditional expectation implies
\[
\mathbb E[K_{j+h}-\mu\mid K_j]=a^h(K_j-\mu),\qquad
\operatorname{Cov}(K_j,K_{j+h})=a^h\operatorname{Var}(K_j)
\]
when the chain is stationary.

**2. Exact stationary second moments.** Let \(X_i\) indicate presence of type \(i\) in the stationary set, and write \(m_r=\mathbb E\prod_{i=1}^r X_i\), with \(m_0=1\). Exchangeability and independent post-draw thinning give, for \(1\le r\le n\),
\[
 m_r=q^r\left[\left(1-\frac rn\right)m_r+\frac rn m_{r-1}\right],\qquad
 m_r=\frac{r q^r}{n(1-q^r)+r q^r}\,m_{r-1}.
\]
This stationary fixed-subset recursion is an auxiliary identity already used in earlier analysis of the same collector; it is **not** asserted to be novel here. With \(\alpha=m_1=q/(np+q)\), it yields
\[
 m_2=\frac{2q^2\alpha}{np(1+q)+2q^2},\quad
 \operatorname{Cov}(X_1,X_2)
 =-\frac{np^2q^2}{(np+q)^2\bigl(np(1+q)+2q^2\bigr)}.
\]
Hence for \(K=\sum_iX_i\),
\[
 \operatorname{Var}(K)=n\alpha(1-\alpha)
 -\frac{n^2(n-1)p^2q^2}{(np+q)^2\bigl(np(1+q)+2q^2\bigr)}.
\]
Substitution of \(p=c/n\) proves
\[
 \frac{\mu_n}{n}\longrightarrow x_c:=\frac1{1+c},\qquad
 \frac{\operatorname{Var}(K^{(n)}_0)}n\longrightarrow
 v_c:=\frac{c(c+2)}{2(1+c)^3}.
\]
In particular \(\sup_n\mathbb E[Y_n(0)^2]<\infty\), after ignoring the finitely many \(n\le c\).

**3. Martingale and quadratic variation.** Set \(\lambda_n=n(1-a_n)=1+c-c/n\) and
\[
 \xi_{j+1}=K_{j+1}-\mathbb E[K_{j+1}\mid K_j],\qquad
 M_n(t)=\frac1{\sqrt n}\sum_{j<\lfloor nt\rfloor}\xi_{j+1}.
\]
Then the centered count has the exact discrete semimartingale equation
\[
 Y_n(t)=Y_n(0)-\frac{\lambda_n}{n}
 \sum_{j<\lfloor nt\rfloor}Y_n(j/n)+M_n(t).
\]
The conditional quadratic variation is
\[
 \langle M_n\rangle(t)=\frac1n\sum_{j<\lfloor nt\rfloor}V_{n,p_n}(K_j).
\]
For \(k/n\to x_c\), the conditional variance converges to
\[
 H_c=c x_c+(1-x_c)x_c=\frac{c(c+2)}{(1+c)^2}.
\]
The map \(k/n\mapsto V_{n,p_n}(k)\) is uniformly bounded and uniformly Lipschitz for fixed \(c\). Stationarity and the second-moment formula imply \(\mathbb E|K_j/n-x_c|=O(n^{-1/2})\), uniformly in \(j\). Therefore, for each \(T<\infty\),
\[
 \mathbb E\sup_{t\le T}|\langle M_n\rangle(t)-H_ct|\longrightarrow0.
\]
Indeed, the absolute error is bounded by the sum of the absolute conditional-variance errors divided by \(n\), plus a single Riemann-step error.

Write the actual number of post-draw losses as \(R_{j+1}\). Conditional on \(K_j=k\) and the new-type indicator \(J\), it has law \(\operatorname{Binomial}(k+J,c/n)\) and is stochastically bounded by \(\operatorname{Binomial}(n,c/n)\). Since \(K_{j+1}-k=J-R_{j+1}\), all fourth moments of \(\xi_{j+1}\) are bounded uniformly in \(n,j,k\). Thus the scaled martingale jumps satisfy Lindeberg's condition:
\[
 \frac1n\sum_{j<nT}\mathbb E\bigl[\xi_{j+1}^2
 \mathbf1\{|\xi_{j+1}|>\varepsilon\sqrt n\}\bigr]
 \le \frac{C_{c,T}}{\varepsilon^2n}\longrightarrow0.
\]
The martingale functional central limit theorem, or equivalently the continuous martingale-problem limit, gives diffusion coefficient \(\sqrt{H_c}\).

**4. Tightness and stationary identification.** The variance bound in Step 2, Doob's \(L^2\) inequality applied to \(M_n\), and the linear semimartingale equation followed by the discrete Gronwall inequality give \(\sup_n\mathbb E\sup_{t\le T}|Y_n(t)|^2<\infty\). The drift over an interval of scaled length \(\delta\) is bounded in probability by \(O(\delta)\) times this compact-interval supremum, while the martingale increment has second moment \(O(\delta+1/n)\); the fourth-moment bound makes the largest scaled jump vanish in probability. Aldous' criterion establishes tightness in \(D([0,T])\).

Every subsequential limit therefore solves the well-posed continuous martingale problem with generator
\[
 \mathcal L f(y)=-(1+c)y f'(y)+\frac{H_c}{2}f''(y),
 \qquad f\in C_c^\infty(\mathbb R).
\]
It is an Ornstein–Uhlenbeck process driven by Brownian motion independent of the limiting initial state. Because the finite count chains start stationary, every fixed-time marginal of the limit equals its time-zero law. The Ornstein–Uhlenbeck transition converges, from any initial law, to its unique Gaussian invariant law \(\mathcal N(0,H_c/[2(1+c)])\). Thus the limiting initial law is necessarily this Gaussian, and the limit process is uniquely the stationary Ornstein–Uhlenbeck process. Uniqueness removes the need to select a subsequence and proves the stated functional convergence.

**5. Correlation and variance reduction.** Step 1 gives the exact finite-lag covariance. Because \(a_n^{\lfloor nt\rfloor}\to e^{-(1+c)t}\), Step 2 yields the limiting covariance kernel. Under a falsely independent occupancy model with marginal \(x_c\), the variance coefficient would be \(x_c(1-x_c)=c/(1+c)^2\), whereas the proved coefficient is \(v_c\). Their ratio is \((c+2)/(2(1+c))\), concluding the comparison.

## Verification

The accompanying `checker.py` independently constructs the exact \((n+1)\)-state transition matrix, solves the stationary linear system with rational arithmetic, and compares all fixed-subset inclusion probabilities, first and second moments, and lag-regression formulas. Running `python checker.py` gives **945 exact-rational assertions passed**, for \(2\le n\le8\), three different rational loss probabilities, and four lags. No simulation, finite-state check, or numerical limit substitutes for Steps 3–4 of the analytic proof.

## Relationship to prior work

Cruciani and Dudeja (2026, arXiv:2602.20705v1) define the same post-loss dynamics, compute the marginal equilibrium fraction and prove negative association and metastable concentration. Long (2026, arXiv:2605.14511v1) analyzes its count-chain stationary high tail and full-collection entry flux for fixed \(p\). An earlier exact stationary fixed-subset inclusion recursion and all-present product also occur in an accessible research record (opaque identifier `247b3755-9956-49bd-acb8-294ff8cf2826`); they are treated here as established inputs, not as new claims. General density-dependent-process diffusion methods, going back to Kurtz, motivate the martingale approach but do not by themselves specify this model's **stationary critical-window variance and two-time covariance**. The new result is the functional equilibrium fluctuation law at \(p=c/n\), with its explicit non-binomial variance and relaxation parameter.

## Limitations

The functional convergence is for fixed \(c>0\), stationary initialization and bounded rescaled time horizons. It does not cover growing \(c\), nonuniform draw probabilities, type-dependent losses, pre-loss observation, nonstationary initial fluctuations, or rare completion-time tail asymptotics. The exact finite-state identities are proved for \(0<p<1\) but the functional theorem is only asserted on \(p=c/n\). The novelty comparison is based on the identified sources and accessible prior claims, not an exhaustive proof of historical priority. No independent audit has been performed.

## References

1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, first posted 2026-02-24, arXiv:2602.20705v1. https://arxiv.org/abs/2602.20705
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, first posted 2026-05-14, arXiv:2605.14511v1. https://arxiv.org/abs/2605.14511
3. A. D. Barbour, K. Hamza, H. Kaspi and F. Klebaner, *Escape from the boundary in Markov population processes*, arXiv:1312.5788v1 (2013), discussing classical density-dependent diffusion approximation. https://arxiv.org/abs/1312.5788
