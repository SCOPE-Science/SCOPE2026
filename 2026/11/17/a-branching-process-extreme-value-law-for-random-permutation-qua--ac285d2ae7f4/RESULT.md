# A branching-process extreme-value law for random permutation quadratic population equilibria

## Finding

Fix any \(\alpha\in(0,1)\). For each integer \(n\ge1\), independently choose a uniformly random permutation \(\pi\) of \(\{1,\ldots,n\}\) and a uniformly random point \(x^{(0)}\) of the \(n\)-dimensional probability simplex on \(n+1\) species. Iterate the polynomial stochastic map
\[
(V_{\alpha,\pi}(x))_i=2x_{n+1}\bigl(\alpha x_i+(1-\alpha)x_{\pi(i)}\bigr)\quad (1\le i\le n),
\qquad
(V_{\alpha,\pi}(x))_{n+1}=x_{n+1}^2+\left(\sum_{i=1}^n x_i\right)^2.
\]
All initial coordinates are positive almost surely. The limit \(x^{(\infty)}\) exists almost surely, and its distinguished coordinate is \(1/2\). Define the maximum equilibrium fraction among the other species, rescaled by its uniform baseline,
\[
M_n=2n\max_{1\le i\le n}x_i^{(\infty)}.
\]
Then \(M_n\) converges in distribution to a continuous random variable \(M\) supported on \([1,\infty)\). Its exact distribution is
\[
\boxed{\quad \Pr\{M\le t\}=\begin{cases}0,&t\le1,\\ 1-\rho(t),&t>1,\end{cases}\quad}
\]
where \(\rho(t)\in(0,1)\) is the smallest solution of \(\rho=\exp[-t(1-\rho)]\), equivalently the extinction probability of a Galton--Watson branching process with Poisson\((t)\) offspring. Its density for \(t>1\) is
\[
f_M(t)=\frac{\rho(t)(1-\rho(t))}{1-t\rho(t)}.
\]
In particular,
\[
\Pr\{M\le1+\varepsilon\}=2\varepsilon+O(\varepsilon^2)\quad (\varepsilon\downarrow0),
\qquad \Pr\{M>t\}=e^{-t}+O(te^{-2t})\quad (t\to\infty).
\]
The law is independent of the fixed mixing parameter \(\alpha\). At every finite \(n\), \(M_n\ge1\) deterministically.

There is also an **exact finite-size cycle-index formula** for the auxiliary unnormalized maximum \(U_n\), defined in the proof: with \(U_0\) defined vacuously and \(a_0(t)=1\),
\[
\sum_{n\ge0}a_n(t)z^n
=\exp\left(\sum_{k\ge1}\frac{p_k(t)}kz^k\right),\qquad
 a_n(t)=\Pr\{U_n\le t\},\qquad
 p_k(t)=\Pr\{\operatorname{Gamma}(k,1)\le kt\}.
\]
For each fixed \(t>1\), this auxiliary distribution approaches \(1-\rho(t)\) exponentially fast in \(n\). The claimed limiting distribution for \(M_n\) follows by a random normalization and does not assert the same finite-size rate for \(M_n\).

## Assumptions and scope

The simplex is \(\Delta_n=\{x\in\mathbb R_{\ge0}^{n+1}:\sum_{i=1}^{n+1}x_i=1\}\). Uniform sampling means normalized \(n\)-dimensional Lebesgue measure, equivalently Dirichlet\((1,\ldots,1)\). Permutations are uniform on the full symmetric group and independent of initial conditions; a new permutation and initial sample are used for each dimension. The iteration is deterministic after these choices. The parameter \(\alpha\in(0,1)\) is fixed independently of \(n\). The limit is taken in iteration time first, then in species count \(n\).

A \(\pi\)-cycle \(C\) is a set of coordinates permuted transitively by \(\pi\), including singleton fixed points. For independent mean-one exponential variables \(E_1,\dots,E_n\), write \(S_n=\sum_{i=1}^n E_i\) and
\[
U_n=\max_{C\text{ cycle of }\pi}\frac{1}{|C|}\sum_{i\in C}E_i.
\]
The law of \(U_n\) is used only as an intermediate exactly enumerable model, not as the population statistic itself. No assertion is made for \(\alpha=0\) or \(\alpha=1\), different initial Dirichlet parameters, nonuniform permutations, or simultaneous dimension-dependent mixing approaching an endpoint.

## Proof

**1. Exact deterministic equilibrium projection.** Put \(z_j=x_{n+1}^{(j)}\), \(y_i^{(j)}=x_i^{(j)}/(1-z_j)\), with the latter defined while \(z_j<1\). The map preserves the strict interior. Direct calculation gives
\[
2z_{j+1}-1=(2z_j-1)^2,
\qquad y^{(j+1)}=(\alpha I+(1-\alpha)P_\pi)y^{(j)},
\]
where \((P_\pi y)_i=y_{\pi(i)}\). Because \(|2z_0-1|<1\), the first recursion implies \(z_j\to1/2\). The second matrix is doubly stochastic. On each cycle of length \(k\), its eigenvalues are \(\alpha+(1-\alpha)\omega\), where \(\omega\) ranges over \(k\)th roots of unity. For \(\omega\ne1\), strict convexity gives \(|\alpha+(1-\alpha)\omega|<1\); the eigenvalue one has the one-dimensional space of constants on that cycle. Hence \(y^{(j)}\) converges to the vector of initial cycle averages. For every \(i\in C\),
\[
x_i^{(\infty)}=\frac{1}{2|C|}\sum_{j\in C}\frac{x_j^{(0)}}{\sum_{h=1}^n x_h^{(0)}}.
\]
This identity also covers singleton cycles and all interior initial data. In particular the limiting equilibrium is independent of the fixed interior mixing coefficient.

**2. Exponential representation and the correct scaling.** A Dirichlet\((1,\ldots,1)\) vector equals \((E_1,\ldots,E_{n+1})/\sum_{j=1}^{n+1}E_j\) in law, with independent \(\operatorname{Exp}(1)\) variables. Thus the preceding deterministic identity yields the *exact distributional equality*
\[
M_n\overset d=\frac{n}{S_n}U_n.
\]
The independent \(E_{n+1}\) cancels entirely. The normalized species coordinates sum to \(1/2\), so their maximum is at least \(1/(2n)\): \(M_n\ge1\). Since \(S_n/n\to1\) in probability, it remains to identify the law of \(U_n\).

**3. Exact finite permutation cycle index.** Conditional on the cycle lengths \(k_1,\ldots,k_r\), the disjoint exponential sums are independent Gamma\((k_h,1)\) random variables. Hence
\[
\Pr\{U_n\le t\mid\pi\}=\prod_{h=1}^r p_{k_h}(t),\qquad
p_k(t)=1-q_k(t),\qquad
q_k(t)=e^{-kt}\sum_{j=0}^{k-1}\frac{(kt)^j}{j!}.
\]
A uniform permutation with \(c_k\) cycles of length \(k\) has probability mass \(\prod_k(k^{c_k}c_k!)^{-1}\) on that cycle-count pattern, provided \(\sum_k kc_k=n\). Summing the conditional probabilities over all patterns gives, as an identity of formal power series,
\[
\sum_{n=0}^\infty a_n(t)z^n
=\prod_{k=1}^\infty\sum_{c=0}^\infty\frac{1}{c!}\left(\frac{p_k(t)z^k}{k}\right)^c
=\exp\left(\sum_{k\ge1}\frac{p_k(t)}kz^k\right).
\]
Equivalently,
\[
\sum_{n\ge0} a_n(t)z^n=\frac{A_t(z)}{1-z},\qquad
A_t(z)=\exp\left(-\sum_{k\ge1}\frac{q_k(t)}kz^k\right).
\]
For every fixed \(t>1\), the Gamma Chernoff bound implies
\[
q_k(t)\le\exp[-k I(t)],\qquad I(t)=t-1-\log t>0.
\]
Therefore \(A_t\) is analytic on the disk \(|z|<e^{I(t)}\), including at \(z=1\). Its coefficients decay exponentially and the coefficients of \(A_t(z)/(1-z)\) converge, with an exponentially small error, to
\[
\lim_{n\to\infty}\Pr\{U_n\le t\}=A_t(1)=\exp[-S(t)],\qquad
S(t)=\sum_{k\ge1}\frac{q_k(t)}k.
\]
More precisely, for each \(1<r<e^{I(t)}\) the error is \(O_{t,r}(r^{-n})\), by Cauchy's estimate on the coefficients of \(A_t\).

**4. Identification with branching extinction.** For \(t>1\), let \(\rho(t)\in(0,1)\) be the smaller solution to \(\rho=e^{-t(1-\rho)}\). The total finite-progeny probability generating function \(B_t(z)\) of a Poisson\((t)\) Galton--Watson process is the minimal solution of
\[
B_t(z)=z\exp\{t(B_t(z)-1)\},\qquad B_t(1)=\rho(t).
\]
Lagrange inversion gives the coefficients (including in the supercritical case, where their total mass is \(\rho<1\)):
\[
[z^k]B_t(z)=b_k(t)=e^{-kt}\frac{(kt)^{k-1}}{k!},\qquad k\ge1.
\]
Differentiating the generating-function identity at \(z=1\) yields
\[
B_t'(1)=\sum_{k\ge1}k b_k(t)=\frac{\rho(t)}{1-t\rho(t)}.
\]
The denominator is positive: at the smaller fixed point the offspring generating function intersects the diagonal with derivative \(t\rho(t)<1\). Termwise differentiation in \(S(t)\), justified locally uniformly for \(t>1\) by the same Chernoff bound, gives
\[
S'(t)=-\sum_{k\ge1}e^{-kt}\frac{(kt)^{k-1}}{(k-1)!}=-B_t'(1)=-\frac{\rho(t)}{1-t\rho(t)}.
\]
Implicit differentiation of the extinction equation gives
\[
\rho'(t)=-\frac{\rho(t)(1-\rho(t))}{1-t\rho(t)},\qquad
\frac{d}{dt}[-\log(1-\rho(t))]=-\frac{\rho(t)}{1-t\rho(t)}.
\]
Both \(S(t)\) and \(-\log(1-\rho(t))\) tend to zero as \(t\to\infty\). Therefore they coincide on \((1,\infty)\), proving the exact identity
\[
\exp[-S(t)]=1-\rho(t).
\]
The right side is precisely the survival probability of the Poisson\((t)\) branching process, although its complement \(\rho(t)\) is the extinction probability.

**5. Threshold, density, tails, and original statistic.** By the arithmetic mean bound \(U_n\ge S_n/n\), every subsequential law of \(U_n\) is supported on \([1,\infty)\). The identity above is continuous as \(t\downarrow1\), with \(1-\rho(t)\downarrow0\); hence the limiting distribution has no atom at one. Its derivative on \((1,\infty)\) follows from the displayed formula for \(\rho'\). Writing \(s=1-\rho\), the extinction relation becomes \(-\log(1-s)=ts\), so \(t=1+s/2+O(s^2)\), giving \(s=2(t-1)+O((t-1)^2)\). For large \(t\), \(\rho=e^{-t(1-\rho)}\) gives \(\rho=e^{-t}+O(te^{-2t})\). Thus the limiting CDF is continuous everywhere. Finally \(n/S_n\to1\) in probability, and Slutsky's theorem transfers convergence from \(U_n\) to \(M_n\), completing the proof.

## Verification

The accompanying standalone `verify_cycle_maximum.py` uses only Python's standard library. It checks the exact equilibrium projection for two interior coefficients, compares the cycle-index coefficient formula with direct enumeration of every permutation for all \(1\le n\le6\), tests the Gamma-tail/branching identity and finite-size convergence numerically, and compares seeded Monte Carlo samples of the correctly normalized population maximum against the limiting CDF. Successful execution prints `PERMUTATION_QSO_MAXIMUM_BRANCHING_CHECK_OK`. Numerical checks support, but do not replace, the preceding infinite-dimensional limiting argument; the exact proof does not require the checker.

## Relationship to prior work

Jamilov's work [1] introduced the non-Volterra quadratic stochastic family and established deterministic fixed points, cycle-invariant masses, and convergence for an interior mixing coefficient. The present finding treats a distinct question: after **independently randomizing both the permutation and the initial population, with dimension tending to infinity**, what is the scale and full law of the *largest* selected equilibrium species fraction? The cycle projection is based on the published deterministic structure; the new result is the extreme-value law, its exact finite cycle-index representation, and its explicit Poisson-branching identity.

Galganov and Ilienko [2] develop Poisson point-process limits for short cycles in random permutations and several cycle statistics. Their results motivate the short-cycle viewpoint but do not state the maximum of independent exponential *cycle averages* across all cycle lengths or its translation to an equilibrium fraction. Standard permutation cycle-index enumeration and Lagrange inversion are acknowledged classical tools; neither is presented as a new general theorem. The earlier random Volterra QSO study [3] concerns randomly switched *different* operators and vertex selection, not this one-time random-permutation, interior-mixing equilibrium law.

The 2023/2024 Jamilov--Khudoyberdiev article [4] addresses fixed and periodic points in a related permutation family. Its abstract was accessible but the complete article was not; direct full-text priority comparison with that article remains open.

## Limitations

The theorem is asymptotic in the number of ordinary species and requires both independent uniform permutation sampling and a uniform initial simplex law. It is not a universality theorem for other mark distributions, nonuniform cycle weights, random updates of the permutation at each iteration, or mixing parameters approaching zero or one with dimension. Its finite-size exponential rate pertains only to \(U_n\), not to the denominator-normalized \(M_n\). Prior literature on random permutation extremes and branching processes is extensive; unindexed statements or inaccessible full texts could contain equivalent formulations. An independent mathematical audit has not been performed.

## References

[1] U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107v1 (first submitted 2022-10-11); Communications in Mathematics 31 (2023), 31--41. https://arxiv.org/abs/2210.05107 ; https://doi.org/10.46298/cm.10135 .

[2] O. Galganov and A. Ilienko, *Short cycles of random permutations with cycle weights: point processes approach*, arXiv:2309.10721v1 (2023); Statistics & Probability Letters 213 (2024), 110169. https://arxiv.org/abs/2309.10721 .

[3] U. U. Jamilov, M. Scheutzow, M. Wilke-Berenguer, *On the random dynamics of Volterra quadratic operators*, arXiv:1401.7840 (2014); Ergodic Theory and Dynamical Systems. https://arxiv.org/abs/1401.7840 .

[4] U. U. Jamilov and Kh. O. Khudoyberdiev, *On the dynamics of non-Volterra quadratic operators corresponding to permutations*, Journal of Difference Equations and Applications 30 (2024), 336--360, online 2023-11-23, DOI 10.1080/10236198.2023.2284827. https://doi.org/10.1080/10236198.2023.2284827 .
