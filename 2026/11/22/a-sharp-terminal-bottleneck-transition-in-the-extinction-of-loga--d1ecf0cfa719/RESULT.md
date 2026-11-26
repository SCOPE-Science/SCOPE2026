# A sharp terminal-bottleneck transition in the extinction of logarithmic Ising domains

## Finding

Consider the irreversible zero-temperature one-dimensional kinetic Ising sector described below. An initially almost-all-minus ring is seeded with equally spaced permanent plus spins, leaving \(m\) independent minus domains, each of length \(n\). Let \(T_{m,n}\) be the first all-plus time. Suppose \(n\to\infty\), \(m=m_n\to\infty\), and
\[
\frac{\log m_n}{n}\longrightarrow\alpha\in(0,\infty).
\]
Define, for \(s>1/2\),
\[
I(s)=\begin{cases}
2s-1-\log(2s),&1/2<s\le1,\\
s-\log2,&s\ge1.
\end{cases}
\]
There is a unique \(s_\alpha>1/2\) such that \(I(s_\alpha)=\alpha\), and
\[
\boxed{\frac{T_{m_n,n}}{n}\xrightarrow{\mathsf P}s_\alpha.}
\]
The critical rate is \(\alpha_*=1-\log2\). If \(\alpha\ge\alpha_*\), then \(s_\alpha=\alpha+\log2\ge1\); if \(0<\alpha<\alpha_*\), then \(s_\alpha\in(1/2,1)\) is the unique root of \(2s-1-\log(2s)=\alpha\). Equivalently, the critical length is \(n\sim \log(m)/(1-\log2)\) in this first-order scaling. The function \(\alpha\mapsto s_\alpha\) is continuously differentiable but not twice differentiable at \(\alpha_*\): its second derivative tends to \(-1\) from the left and equals zero to the right.

For each initial domain \(j\), let \(G_j\) be the time taken to remove its first \(n-1\) minus spins and \(E_j\) the additional waiting time of its final, isolated minus spin. Let \(J_n\) be the index of the domain that completes last (unique almost surely). Then
\[
\boxed{\left(\frac{G_{J_n}}n,\frac{E_{J_n}}n\right)
\xrightarrow{\mathsf P}\left(\min(s_\alpha,1),(s_\alpha-1)_+\right).}
\]
For \(\alpha>\alpha_*\) the final-spin wait is of order \(n\) with limiting coefficient \(s_\alpha-1\). As a **fraction of the last domain's lifetime** it tends to \((s_\alpha-1)/s_\alpha\). For \(0<\alpha\le\alpha_*\), that wait is \(o_{\mathsf P}(n)\), and the macroscopic slowdown is due to erosion before the last spin becomes isolated. These statements concern the selected last domain, not a typical single domain.

## Assumptions and scope

Place \(N=m(n+1)\) spins on a periodic nearest-neighbor chain, \(m,n\ge2\). The initial cyclic word consists of exactly \(m\) repetitions of \(n\) consecutive minus spins followed by one plus spin. Independently at each site a rate-one Poisson clock rings. A plus spin never changes; a minus spin changes irreversibly to plus at its clock ring exactly when at least one neighboring site is plus. This is the continuous-time single-site-clock realization of the sector \(Q^{(1)}(0,2)\) of Cao, Jiang and Zhang (2026). Time units are one mean site-update attempt per site (sweeps). There is no reverse flip, spontaneous bulk flip or disorder in the initial pattern. No assertion is made for other kinetic sectors, random initial-domain laws or a different update rule.

## Proof

**1. Exact independent-domain law.** Permanent plus sites separate independent rate-one clocks on the minus domains. If a minus block has length \(r\ge2\), only its two end spins are flippable, giving total departure rate \(2\); after the flip the block has length \(r-1\). At length one its departure rate is \(1\). The strong Markov property and independent clocks give, for each block,
\[
T_j=G_j+E_j,\qquad
G_j\sim\operatorname{Gamma}(n-1,\text{rate }2),\qquad E_j\sim\operatorname{Exp}(1),
\]
with all terms and blocks mutually independent. Thus \(T_{m,n}=\max_{1\le j\le m}(G_j+E_j)\). Its one-block Laplace transform and survival law are
\[
\mathbb E e^{-zT_j}=\left(\frac2{2+z}\right)^{n-1}\frac1{1+z},\quad z\ge0,
\]
\[
\Pr(T_j>t)=\Pr\{\operatorname{Pois}(2t)\le n-2\}
+2^{n-1}e^{-t}\Pr\{\operatorname{Pois}(t)\ge n-1\},\quad t\ge0.
\]
The second identity follows by conditioning on \(G_j\): the contribution from \(G_j\le t\) is \(e^{-t}\mathbb E[e^{G_j};G_j\le t]\). Tilting its gamma density by \(e^g\) changes the rate from two to one and multiplies by \(2^{n-1}\). The gamma–Poisson identity then gives the expression.

**2. Rare tail of a single domain.** Cramér's theorem for independent rate-two exponential stages gives the good rate function \(j(g)=2g-1-\log(2g)\) for \(g>0\) and \(+\infty\) otherwise for \(G_j/n\) at speed \(n\). The change from \(n-1\) summands and normalization by \(n\) to the conventional sample mean leaves the rate unchanged: the factor tends to one and the sample means are exponentially tight. The independent \(E_j/n\) has good rate \(e\) for \(e\ge0\) and \(+\infty\) otherwise. Their joint rate is \(J(g,e)=j(g)+e\) on its finite domain. For \(s>1/2\), the unique minimizer over \(g+e\ge s\) is \((s,0)\) for \(s\le1\), and \((1,s-1)\) for \(s\ge1\). In fact, minimizing out \(e\) yields \(j(g)+(s-g)_+\); on \(g<s\) its derivative is \(1-1/g\), and on \(g>s\) one has \(j'(g)=2-1/g>0\). The rate at the minimum is \(I(s)\) as in the Finding. The open half-space \(g+e>s\) has the same infimum as the closed half-space by increasing \(e\) by an arbitrarily small positive amount at the minimizer. Therefore the large-deviation upper and lower bounds give
\[
-\lim_{n\to\infty}\frac1n\log\Pr(T_j>ns)=I(s).
\]

**3. Extreme-domain threshold.** For \(s>1/2\), let \(p_n(s)=\Pr(T_j>ns)\). Independence gives \(\Pr(T_{m,n}\le ns)=[1-p_n(s)]^m\). Since \(m=\exp[(\alpha+o(1))n]\), the tail rate gives \(mp_n(s)\to0\) when \(I(s)>\alpha\) and \(mp_n(s)\to\infty\) when \(I(s)<\alpha\). Use the union bound in the first case and \((1-p)^m\le e^{-mp}\) in the second. The latter conclusion for \(s\le1/2\) follows by comparison with a fixed \(s'\in(1/2,s_\alpha)\). Strict increase of \(I\) above \(1/2\) proves convergence in probability to its unique level \(I(s_\alpha)=\alpha\). At \(s=1\) the branches match with \(I'=1\); the left and right limits of \(I''\) there are \(1\) and \(0\). Inverse differentiation gives the stated smoothness and one-sided second derivatives of \(s_\alpha\).

**4. Mechanism of the last surviving domain.** Write \(x_*=(\min(s_\alpha,1),(s_\alpha-1)_+)\). It uniquely minimizes the good joint rate over \(g+e\ge s_\alpha\), with value \(\alpha\). For every \(\varepsilon>0\), choose a sufficiently small \(\delta>0\) so that the infimum of \(J\) over the closed set
\[
\{(g,e):s_\alpha-\delta\le g+e\le s_\alpha+\delta,\ \|(g,e)-x_*\|\ge\varepsilon\}
\]
is strictly greater than \(\alpha\). If no such \(\delta\) existed, compactness of rate sublevel sets and lower semicontinuity would yield a limit with sum \(s_\alpha\), at distance at least \(\varepsilon\) from \(x_*\), with rate at most \(\alpha\), contradicting uniqueness. The joint large-deviation upper bound and a union bound over \(m=\exp[(\alpha+o(1))n]\) domains imply that with high probability no domain completing in that window has its split outside the \(\varepsilon\)-ball. Step 3 places the last domain in the window with high probability. The fraction in the Finding follows by dividing by \(T_{m,n}/n\), which tends to \(s_\alpha>0\).

**5. Discrete-sweep normalization.** If each attempt instead selects a uniform site and \(K\) attempts are needed for absorption, the clock superposition is a rate-\(N\) Poisson process with the same selected-site sequence. Its independent interattempt gaps give \(T_{m,n}=N^{-1}\sum_{i=1}^K Z_i\), with \(Z_i\) independent rate-one exponentials independent of \(K\). The union Chernoff bound at a fixed parameter \(0<\theta<1\) gives \(\mathbb ET_{m,n}=O(n+\log m)=O(n)\): the bound on a time-\(u\) exceedance is \(\min(1,m\mathbb E e^{\theta T_j}e^{-\theta u})\), with \(\log\mathbb E e^{\theta T_j}=O(n)\). The exact mean-square difference is \(\mathbb E[(T_{m,n}-K/N)^2]=\mathbb EK/N^2=\mathbb ET_{m,n}/N=O(n/N)\). Thus \((K/N-T_{m,n})/n\to0\) in \(L^2\), and the extinction-time conclusion also holds in discrete sweeps. The split is stated for the continuous-clock realization.

## Verification

The supplied script `check.py` uses the Python standard library and checks the one-block Laplace transform by rational recursion, the survival identity and selected rate-function values, a grid check of the optimizer, and finite-domain simulations. These finite tests corroborate algebra and normalization but do not replace the large-deviation proof above.

## Relationship to prior work

Cao, Jiang and Zhang (2026) describe the kinetic-sector dynamics and obtain mean absorption times for two specific preparations, one fully exposed and one with a single macroscopic minus block. Their Appendix C gives attempt-count generating functions for those preparations and a mean recursion for general run lengths. The local erosion mechanism is credited to that framework. The finite-time law is not claimed as new: the rate calculation in Step 1 applies to each separated block, and independence gives a product of one-block CDFs even when their deterministic lengths differ. For Bernoulli initial spins, *A density-tuned Gumbel transition in irreversible one-dimensional spin ordering* uses the same per-run law but studies random geometrically distributed run lengths, including a density critical window rather than simultaneous deterministic growth of the common domain length and the number of domains. The contribution here is the sharp boundary in that deterministic equal-length regime and the joint limit for the selected last domain. Cramér large deviations and extreme-value methods are standard tools.

## Limitations

The theorem assumes equally spaced permanent plus seeds, independent rate-one site clocks, irreversible boundary flips, and a positive finite limit of \(\log m/n\). It proves first-order scaling in probability, not a centered Gumbel theorem, convergence of expectations, or robustness to random domain lengths or reverse flips. The threshold is a feature of the two-stage hazard structure and need not persist in other kinetic models. Prior implicit asymptotic coverage and unindexed results remain originality risks.

## References

1. D. Cao, W. Jiang, and Y. Zhang, *Kinetic Sectors and Nonequilibrium Dynamics in the \(\delta\)-Ising Model*, arXiv:2610.36829v1 (first submitted 2026-10-27), especially Section IV.B and Appendix C. https://arxiv.org/abs/2610.36829
2. H. Cramér, *Sur un nouveau théorème-limite de la théorie des probabilités*, Actualités Scientifiques et Industrielles **736** (1938).
3. *A density-tuned Gumbel transition in irreversible one-dimensional spin ordering*, Resultary record `2026/11/22/SCOPE-a-density-tuned-gumbel-transition-in-irreversible-one-dimensiona--7f482632ec5d`.
