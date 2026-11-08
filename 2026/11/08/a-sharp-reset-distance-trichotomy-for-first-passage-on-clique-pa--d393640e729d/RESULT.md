# A sharp reset-distance trichotomy for first passage on clique–path networks

## Finding
Let \(G_{m,\ell}\) be a clique \(K_m\), \(m\ge2\), with a path of \(\ell\ge1\) edges attached to one clique vertex \(o\). A continuous-time walker jumps along **each** incident edge at rate one, starts at \(o\), and is reset independently to \(o\) at rate \(r\ge0\). Its target is the far end of the attached path. Write \(M_{m,\ell}(r)\) for the mean first-passage time. Define polynomials
\[
 E_\ell(r)=\sum_{j=0}^{\ell}\binom{\ell+j}{2j}r^j,\qquad
 H_{\ell-1}(r)=\sum_{j=0}^{\ell-1}\binom{\ell+j}{2j+1}r^j.
\]
Then for \(r>0\), with continuous extension at zero,
\[
 \boxed{M_{m,\ell}(r)=\frac{E_\ell(r)-1}{r}+\frac{(m-1)H_{\ell-1}(r)}{1+r}},\qquad
 M_{m,\ell}(0)=m\ell+\frac{\ell(\ell-1)}2.
\]
The global optimum has a sharp three-way classification:

* \(\ell=1\): \(M_{m,1}(r)=1+(m-1)/(1+r)\) is strictly decreasing and has infimum \(1\), never attained at finite \(r\).
* \(\ell=2\): \(M_{m,2}(r)=m+2+r+(m-1)/(1+r)\). Its unique minimizer on \([0,\infty)\) is \(r_*=\sqrt{m-1}-1\), which is positive precisely when \(m\ge3\). The minimum is \(m+1+2\sqrt{m-1}\); the gain over no resetting is exactly \((\sqrt{m-1}-1)^2\).
* \(\ell\ge3\): \(M_{m,\ell}(r)\) is **strictly increasing** throughout \([0,\infty)\) for every \(m\ge2\); the unique optimum is no resetting.

Thus attaching only one extra path edge beyond the two-edge case destroys all possible mean first-passage advantage of resetting to the gateway, even for arbitrarily large clique traps. In contrast, for a two-edge target the optimal rate is positive once the clique has at least three vertices.

## Assumptions and scope
The network is finite, simple, undirected and unweighted. The path vertices \(x_1,\ldots,x_\ell\) are disjoint from the clique, with edges \(o=x_0\!\sim x_1\sim\cdots\sim x_\ell\). Every undirected edge supplies two independent directed transition clocks of rate one. Hence the total escape rate at a vertex equals its degree: the model is **not** the discrete-time uniform-neighbor walk or a continuous-time walk normalized to total rate one. Resets have a homogeneous independent Poisson clock of rate \(r\), send the walker to \(o\), and do not stop or change the target. At the source, a reset leaves the state unchanged. First passage stops on first reaching \(x_\ell\). All assertions cover integers \(m\ge2\), \(\ell\ge1\) and real \(r\ge0\), with no thermodynamic limit required.

## Proof
**1. Hitting-time transform without resetting.** For \(s\ge0\), let \(T\) be the target hitting time with no resetting and let \(f_v(s)=\mathbb E_v[e^{-sT}]\). The common transform at the \(m-1\) non-gateway clique vertices, denoted \(f_b\), satisfies \((s+m-1)f_b=(m-2)f_b+f_o\), hence \(f_b=f_o/(s+1)\). The gateway equation is
\[
 (s+m)f_o=(m-1)f_b+f_{x_1},\quad
 \frac{f_{x_1}}{f_o}=s+m-\frac{m-1}{s+1}.
\]
For the interior path vertices, \((s+2)f_{x_j}=f_{x_{j-1}}+f_{x_{j+1}}\). Define the ratios \(F_j=f_{x_j}/f_o\), so \(F_0=1\), \(F_1=s+m-(m-1)/(s+1)\), and \(F_{j+1}=(s+2)F_j-F_{j-1}\). Since \(f_{x_\ell}=1\), \(f_o(s)=1/F_\ell(s)\).

**2. Polynomial solution.** Set \(E_0=1\), \(E_1=1+s\) and \(H_{-1}=0\), \(H_0=1\), with each sequence satisfying \(Y_{j+1}=(s+2)Y_j-Y_{j-1}\). Direct substitution and induction give
\[
 F_\ell(s)=E_\ell(s)+(m-1)\frac{sH_{\ell-1}(s)}{s+1}.
\]
The binomial expressions in the finding satisfy exactly these initial conditions and recurrences: for \(j\ge0\),
\[
 E_j(s)=\sum_{k=0}^j\binom{j+k}{2k}s^k,
 \qquad H_j(s)=\sum_{k=0}^j\binom{j+k+1}{2k+1}s^k,
\]
as follows by Pascal's identity (with missing coefficients interpreted as zero). In particular \(E_\ell(0)=1\), \(E_\ell'(0)=\ell(\ell+1)/2\), and \(H_{\ell-1}(0)=\ell\).

**3. Renewal with Poisson resetting.** If \(\phi(s)=\mathbb E_o[e^{-sT}]=1/F_\ell(s)\), the exponential reset clock \(R\) satisfies \(\mathbb P(T<R)=\phi(r)\) and \(\mathbb E[\min(T,R)]=(1-\phi(r))/r\). Following each unsuccessful attempt the process starts anew at \(o\), independently. Thus for \(r>0\),
\[
 M_{m,\ell}(r)=\frac{1-\phi(r)}{r\phi(r)}=\frac{F_\ell(r)-1}{r},
\]
which is precisely the displayed rational formula. Analytic continuation to \(r=0\) gives \(\ell(\ell+1)/2+(m-1)\ell=m\ell+\ell(\ell-1)/2\).

**4. Global optimization.** For \(\ell=1,2\), the formulas above follow immediately. At \(\ell=2\), differentiation gives \(M'_{m,2}(r)=1-(m-1)/(1+r)^2\) and \(M''_{m,2}(r)=2(m-1)/(1+r)^3>0\); hence the stated unique optimum and the exact saving. The \(\ell=1\) derivative is \(-(m-1)/(1+r)^2<0\).

For \(\ell\ge3\), \((E_\ell(r)-1)/r\) is a polynomial with strictly positive coefficients and degree \(\ell-1\), so its derivative is strictly positive for \(r\ge0\). It remains to check the second summand. Write \(H_{\ell-1}(r)=\sum_{j=0}^{\ell-1} c_jr^j\), where \(c_j=\binom{\ell+j}{2j+1}>0\). Then
\[
 (1+r)H'_{\ell-1}(r)-H_{\ell-1}(r)
 = (c_1-c_0)+\sum_{j=1}^{\ell-1}\big((j+1)c_{j+1}+(j-1)c_j\big)r^j,
\]
with \(c_\ell=0\). Its constant coefficient is \(\binom{\ell+1}{3}-\ell>0\) for \(\ell\ge3\). Every displayed nonconstant coefficient is nonnegative, and in fact positive for \(\ell\ge3\). Consequently the derivative of \(H_{\ell-1}(r)/(1+r)\) is strictly positive. Because \(m-1>0\), both summands increase strictly on all \(r\ge0\). This proves the last case, including the boundary \(r=0\), and completes the classification. \(\square\)

## Verification
The accompanying Python 3 script `check.py` separately constructs the full continuous-time transient generator of the actual clique–path network (not the one-dimensional reduced equations), inserts reset transitions, and solves its first-step linear system using exact rational Gaussian elimination. It agrees **exactly** with the formula for \(2\le m\le9\), \(1\le\ell\le7\), and reset rates \(0,1/4,1/2,3/2,5\), comprising 280 full-generator comparisons. Further checks verify coefficient signs for \(1\le\ell\le44\) and compare sample regimes for \(2\le m\le24\), \(1\le\ell\le13\). These finite computations are independent sanity checks; the preceding recurrence and positivity proof establishes the claims for every admissible size and rate.

## Relationship to prior work
The exponential resetting renewal identity is established classical methodology, as in Evans and Majumdar (2011) and Pal and Reuveni (2016). General network studies by Riascos et al. (2019/2020 and 2021) establish spectral and renewal techniques for reset walks, with degree-normalized jump kernels; their 2020 paper also discusses a continuous-time operator obtained from that normalized kernel. Förster et al. (2021) study exact **non-reset** first-passage laws on necklace structures containing cliques. None is asserted as new here. In particular, Zelenkovski et al. (2023) examine a lollipop network under degree-normalized discrete-time neighbor steps with resetting and graph-averaged first-passage statistics. Their dynamics and target observable differ from the rate-one-per-edge continuous-time, single terminal-target setting here. The contribution claimed is the explicit **all-clique-size, all-path-length global optimization trichotomy and its sharp two-edge threshold**, not the graph family, the renewal formula, or general resetting phenomena.

## Limitations
No statement is made for degree-normalized continuous-time random walks, graph-averaged first-passage times, reset locations other than the gateway, nonexponential resetting, nonuniform edge rates, or infinite networks. The decrease for a one-edge target has only an unattained limiting infimum. The uniqueness and novelty assessment concerns the precise joint assumptions and conclusions above, not a proof of priority over every unindexed or inaccessible mathematical source. Independent scientific audit has not been performed.

## References
1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first publicly posted 2011-02-14), https://arxiv.org/abs/1102.2704.
2. A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 (first publicly posted 2016-07-20), https://arxiv.org/abs/1607.06048.
3. A. P. Riascos, D. Boyer and J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437 (2021), https://arxiv.org/abs/2110.15437.
4. A. P. Riascos, D. Boyer, P. Herringer and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568 (2019), https://arxiv.org/abs/1910.13568.
5. Y.-P. Förster, L. Gamberi, E. Tzanis, P. Vivo and A. Annibale, *Exact and Approximate Mean First Passage Times on Trees and other Necklace Structures: a Local Equilibrium Approach*, arXiv:2110.01946 (2021), https://arxiv.org/abs/2110.01946.
6. K. Zelenkovski et al., *Random Walks on Networks with Centrality-Based Stochastic Resetting*, *Entropy* **25** (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC9955709/.
