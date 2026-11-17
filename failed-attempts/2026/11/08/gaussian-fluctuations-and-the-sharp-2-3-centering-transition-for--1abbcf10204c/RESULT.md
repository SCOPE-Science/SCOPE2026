# Gaussian fluctuations and the sharp \(2/3\) centering transition for harmonic Zipf quorum times

## Finding

For each integer \(n\ge2\), let \(H_n=\sum_{j=1}^n j^{-1}\), take independent exponential first-discovery times \(T_{j,n}\) of rates \(\lambda/(jH_n)\), and define the strictly positive-weight quorum time
\[
\tau_{n,\theta}=\inf\left\{t\ge0:\sum_{j=1}^n\frac{\mathbf1_{\{T_{j,n}\le t\}}}{jH_n}>\theta\right\},\qquad 0<\theta<1,\quad\lambda>0.
\]
Let \(A_n=\lambda\tau_{n,\theta}/H_n\), let \(a_n\) be the unique positive solution of
\[
S_n(a_n)=\theta H_n,\qquad S_n(a)=\sum_{j=1}^n\frac{1-e^{-a/j}}j,
\]
and set \(B_n=\exp(\theta H_n-2\gamma)\) and \(c_\theta=\exp((\theta-2)\gamma)\), where \(\gamma\) is Euler's constant.

**Theorem.** For every fixed \(\theta\in(0,1)\),
\[
\frac{A_n-a_n}{\sqrt{a_n}}\ \Longrightarrow\ \mathcal N(0,1/2),\qquad
 a_n=B_n+\frac{B_n^2}{n}(1+o(1)).
\]
Consequently, the explicit first-order centering exhibits a sharp second-order phase transition:
\[
\frac{A_n-B_n}{\sqrt{B_n}}\Longrightarrow
\begin{cases}
\mathcal N(0,1/2),&0<\theta<2/3,\\
\mathcal N(e^{-2\gamma},1/2),&\theta=2/3,
\end{cases}
\]
and \((A_n-B_n)/\sqrt{B_n}\to+\infty\) in probability when \(2/3<\theta<1\).
Here the convergences are along integer \(n\to\infty\); no moment convergence or rate of weak convergence is asserted.

## Assumptions and scope

All weights and discovery rates are aligned harmonic Zipf weights: \(p_{j,n}=w_{j,n}=(jH_n)^{-1}\). The exponent of the Zipf distribution is exactly one. Both \(\theta\in(0,1)\) and \(\lambda>0\) are fixed independently of \(n\). The threshold uses strict crossing (\(>\theta\)); this agrees with the first-crossing distributional limit, including at any finite-level subset-sum equality. The result is a probability limit theorem (primary MSC2020 60F05), not an algorithmic reliability theorem.

## Proof

**1. Exact Poisson representation and deterministic crossing.** Independent exponentials \(E_j\sim\operatorname{Exp}(1)\) allow \(T_{j,n}=jH_n E_j/\lambda\). At scaled time \(a\), the unnormalized discovered mass is \(Y_n(a)=\sum_{j=1}^n j^{-1}\mathbf1_{\{E_j\le a/j\}}\). The summands are independent Bernoulli variables with success probabilities \(q_j(a)=1-e^{-a/j}\). Since \(Y_n(a)\) is increasing, \(\{A_n\le a\}=\{Y_n(a)>\theta H_n\}\). Its expectation is exactly \(S_n(a)\) and its variance is
\[
V_n(a)=\sum_{j=1}^n\frac{e^{-a/j}(1-e^{-a/j})}{j^2}.
\]
Because \(S_n(0)=0\), \(S_n(+\infty)=H_n\) and \(S_n'(a)>0\), the root \(a_n\) is uniquely defined.

**2. A sufficiently precise harmonic mean expansion.** Define the infinite sum \(F(a)=\sum_{j\ge1}(1-e^{-a/j})/j\) for \(a>0\). Termwise differentiation (locally uniform absolute convergence) gives
\[
F'(a)=\sum_{j\ge1}j^{-2}e^{-a/j}.
\]
The integral of \(g_a(x)=x^{-2}e^{-a/x}\) over \((0,\infty)\) equals \(1/a\). Writing \(g_a(x)=a^{-2}g_1(x/a)\), the derivatives of \(g_1\) of every order are integrable and vanish at both endpoints. Euler--Maclaurin summation with arbitrarily many integrations by parts therefore gives, for every fixed integer \(m\ge1\),
\[
F'(a)=a^{-1}+O_m(a^{-m-1}),\qquad
F(a)=\log a+C+O_m(a^{-m}),\quad a\to\infty.
\]
To determine \(C\), insert \(1-e^{-a/j}=\int_0^{a/j}e^{-u}\,du\), and interchange sum and integral:
\[
F(a)=\int_0^a e^{-u} H_{\lfloor a/u\rfloor}\,du.
\]
The harmonic estimate \(H_k=\log k+\gamma+O(1/k)\), with exponential tail control and dominated convergence, gives \(F(a)-\log a\to\gamma-\int_0^\infty e^{-u}\log u\,du=2\gamma\). Thus \(C=2\gamma\).

When \(a\to\infty\) and \(a/n\to0\), Taylor expansion in the omitted tail yields
\[
F(a)-S_n(a)=\sum_{j>n}\frac{1-e^{-a/j}}j
=\frac an+O\left(\frac a{n^2}+\frac{a^2}{n^2}\right),
\]
and hence, for any fixed \(m\),
\[
S_n(a)=\log a+2\gamma-\frac an
+O_m\left(a^{-m}+\frac a{n^2}+\frac{a^2}{n^2}\right). \tag{1}
\]
The identity \(B_n=e^{\theta H_n-2\gamma}\sim c_\theta n^\theta\), and (1) evaluated at fixed multiples of \(B_n\), imply \(a_n/B_n\to1\); in particular \(a_n\to\infty\), \(a_n/n\to0\). Using (1) at \(a=a_n\) and choosing \(m\) sufficiently large (depending on fixed \(\theta\)),
\[
0=\log(a_n/B_n)-a_n/n+o(a_n/n),
\]
which implies \(a_n/B_n=1+(B_n/n)(1+o(1))\), as claimed. The arbitrarily high-order Euler--Maclaurin remainder is essential here: a mere \(o(1)\) mean approximation cannot identify this second-order shift for every \(\theta\).

**3. Gaussian fluctuations of the weighted Bernoulli mass.** Fix a sequence \(a\asymp n^\theta\). Because \(a/n\to0\), Riemann-sum convergence, with the rapidly decaying integrand at zero, gives
\[
aV_n(a)\longrightarrow \int_0^\infty\frac{e^{-1/x}(1-e^{-1/x})}{x^2}\,dx
=\int_0^\infty(e^{-u}-e^{-2u})\,du=\frac12. \tag{2}
\]
For centered Bernoulli summands \(Z_{j,a}=j^{-1}(\mathbf1_{\{E_j\le a/j\}}-q_j(a))\), the absolute third moment satisfies
\[
\sum_{j=1}^n\mathbb E|Z_{j,a}|^3
\le\sum_{j=1}^n j^{-3}e^{-a/j}=O(a^{-2}).
\]
By (2), the Lyapunov ratio is \(O(a^{-1/2})\to0\). Thus, uniformly for any deterministic sequence \(a\sim a_n\),
\[
\sqrt{a_n}\big(Y_n(a)-S_n(a)\big)\Longrightarrow\mathcal N(0,1/2). \tag{3}
\]
Also \(S_n'(a)=a^{-1}(1+o(1))\) uniformly for \(a=a_n+O(\sqrt{a_n})\): this follows from the infinite-sum derivative expansion and \(\sum_{j>n}j^{-2}e^{-a/j}=O(1/n)=o(1/a_n)\). For fixed \(x\in\mathbb R\), put \(a=a_n+x\sqrt{a_n}\). Then
\[
\sqrt{a_n}\big(S_n(a)-\theta H_n\big)\to x.
\]
The identity for \(\{A_n\le a\}\), equation (3), and continuity of the Gaussian distribution give
\[
\Pr\left\{\frac{A_n-a_n}{\sqrt{a_n}}\le x\right\}\to
\Pr\{\mathcal N(0,1/2)+x>0\}=\Phi(\sqrt2 x).
\]
This also takes care of any exact equalities in finite subset sums: their limiting probability at the local scale vanishes by the continuous Gaussian limit.

**4. The centering transition.** Since \(B_n\sim c_\theta n^\theta\),
\[
\frac{a_n-B_n}{\sqrt{B_n}}
=\frac{B_n^{3/2}}{n}(1+o(1))
=c_\theta^{3/2}n^{3\theta/2-1}(1+o(1)).
\]
Slutsky's theorem gives zero shift below \(2/3\), the finite shift \(c_{2/3}^{3/2}=e^{-2\gamma}\) at \(2/3\), and positive divergence above \(2/3\). This completes the proof.

## Verification

`verify.py` provides a standalone Python 3 standard-library checker. It enumerates all discovery subsets for sizes \(2\) through \(8\) at specified times and thresholds, compares their exact event probabilities with the Bernoulli mean and variance identities, solves deterministic finite roots, checks the second-order root bias and sampled harmonic/variance asymptotics. Run it in the directory containing this file and `verify.py` as `python3 verify.py`.

These finite checks are reproducibility aids, not an infinite proof. The decisive infinite steps are the Euler--Maclaurin control in (1), the Lyapunov condition behind (3), and the local threshold inversion. No computational output is used as a substitute for those arguments.

## Relationship to prior work

Müller and Šebek (2026, arXiv:2607.08551) introduce the weighted quorum model and prove, in Section 6, the first-order critical harmonic-Zipf scaling \(A_n/n^\theta\to c_\theta\) in probability (their Theorem 6.3), supported by their mean asymptotics and a variance upper bound (Lemmas 6.1--6.2). The present claim is the exact-root centered Gaussian law, its variance \(1/2\), the sharp second-order deterministic correction, and the \(2/3\) explicit-centering transition. None follows from a first-order limit alone.

Chebunin and Zuyev (2020, DOI 10.1007/s10959-020-01053-6) prove functional central limit theorems for infinite occupancy and missing-mass models with fixed infinite probability vectors. Garza and Wang (2024, arXiv:2412.02160) study weighted *occupancy-count* processes under an infinite-urn regularly varying tail. Neither theorem, as stated, covers this triangular finite-array harmonic Zipf normalization with quorum-weighted first passage or determines its centering phase. The triangular-array Lyapunov CLT is a classical proof ingredient; no claim of a new general CLT principle is made.

## Limitations

The threshold is fixed and strictly between zero and one, the exponent is exactly harmonic Zipf \(s=1\), and first-discovery clocks are independent exponentials. The result does not treat non-Poisson input, arbitrary nonaligned weights, varying thresholds, quantitative convergence rates, expected stopping-time corrections, or moment convergence. Literature priority beyond inspected primary texts remains subject to independent comparison, especially possible general empirical-quantile or occupancy theorems whose hypotheses could imply some portions of the claim after additional work.

## References

1. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551 (first posted July 9, 2026), https://arxiv.org/abs/2607.08551. Sections 2, 3 and 6.
2. M. Chebunin and S. Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, *Journal of Theoretical Probability* 35 (2022), initially online November 23, 2020, https://doi.org/10.1007/s10959-020-01053-6. Introduction and Theorem 1.
3. J. Garza and Y. Wang, *A functional central limit theorem for weighted occupancy processes of the Karlin model*, arXiv:2412.02160 (first posted December 3, 2024), https://arxiv.org/abs/2412.02160. Introduction and principal theorem.
