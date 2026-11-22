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
The sharp critical rate is \(\alpha_*=1-\log2\). If \(\alpha\ge\alpha_*\), then \(s_\alpha=\alpha+\log2\ge1\); if \(0<\alpha<\alpha_*\), then \(s_\alpha\in(1/2,1)\) is the unique root of \(2s-1-\log(2s)=\alpha\). Equivalently, the critical minus-domain length is \(n\sim\log(m)/(1-\log2)\). The function \(\alpha\mapsto s_\alpha\) is continuously differentiable but not twice differentiable at \(\alpha_*\): its second derivative tends to \(-1\) from the left and equals zero to the right.

There is a pathwise mechanism statement, not merely a crossover of means. For each initial domain \(j\), let \(G_j\) be the time taken to remove its first \(n-1\) minus spins and \(E_j\) the additional waiting time of its final, isolated minus spin. Let \(J_n\) be the index of the domain that completes last (unique almost surely). Then
\[
\boxed{\left(\frac{G_{J_n}}n,\frac{E_{J_n}}n\right)
\xrightarrow{\mathsf P}\left(\min(s_\alpha,1),(s_\alpha-1)_+\right).}
\]
Thus at \(\alpha>\alpha_*\) a positive fraction \(s_\alpha-1\) of the winning domain's extinction time is a single final-spin wait of macroscopic order \(n\), whereas at \(0<\alpha\le\alpha_*\) the final-spin wait is \(o_{\mathsf P}(n)\), and the rare slow event is collective domain erosion. This is one joint theorem for the extinction time and its dominant microscopic mechanism.

## Assumptions and scope

Place \(N=m(n+1)\) spins on a periodic nearest-neighbor chain, \(m,n\ge2\). The initial cyclic word consists of exactly \(m\) repetitions of \(n\) consecutive minus spins followed by one plus spin. Independently at each site a rate-one Poisson clock rings. A plus spin never changes; a minus spin changes irreversibly to plus at its clock ring exactly when at least one neighboring site is plus. This is the continuous-time single-site-clock realization of the sector \(Q^{(1)}(0,2)\) of Cao, Jiang and Zhang (2026). Time units are one mean site-update attempt per site (sweeps). There is no reverse flip, spontaneous bulk flip or disorder in the initial pattern. No assertion is made for other kinetic sectors, random initial-domain laws or a different update rule.

## Proof

**1. Exact independent-domain law.** The permanent plus sites separate independent rate-one site clocks. If a minus block has length \(r\ge2\), only its two end spins are flippable; the total departure rate is exactly \(2\). Upon the next flip the block has length \(r-1\). At length one its departure rate is \(1\). By the strong Markov property and independence of Poisson clocks, for each block
\[
T_j\stackrel d=G_j+E_j,\qquad
G_j\sim\operatorname{Gamma}(n-1,\text{rate }2),\quad
E_j\sim\operatorname{Exp}(1),
\]
with all terms and blocks mutually independent. Consequently \(T_{m,n}=\max_{1\le j\le m}(G_j+E_j)\). The exact one-block Laplace transform and survival law are
\[
\mathbb E e^{-zT_j}=\left(\frac2{2+z}\right)^{n-1}\frac1{1+z},\quad z\ge0,
\]
\[
\Pr(T_j>t)=\Pr\{\operatorname{Pois}(2t)\le n-2\}
+2^{n-1}e^{-t}\Pr\{\operatorname{Pois}(t)\ge n-1\},\quad t\ge0.
\]
The second identity follows by conditioning on \(G_j\), integrating the truncated exponential moment, and the integer-gamma/Poisson correspondence; it is used for reproducible finite-size checks.

**2. Rare tail of a single domain.** Cramér's theorem for independent rate-two exponential stages gives the good rate function
\[
j(g)=2g-1-\log(2g),\quad g>0,
\]
for \(G_j/n\); define \(j(0)=+\infty\). Independently, \(E_j/n\) has good large-deviation rate \(e\) for \(e\ge0\). Their joint rate is \(J(g,e)=j(g)+e\). For every \(s>1/2\), contraction to the half-space \(g+e\ge s\) yields
\[
-\lim_{n\to\infty}\frac1n\log\Pr(T_j\ge ns)
=\inf_{g>0,\ e\ge0,\ g+e\ge s}\{j(g)+e\}=I(s).
\]
For completeness, the minimizer is unique: since \(j\) is strictly convex, \(j'(g)=2-1/g\), and the objective is increasing in \(e\), its minimizer is \((g_s,e_s)=(s,0)\) when \(1/2<s\le1\), and \((1,s-1)\) when \(s\ge1\). One may independently derive the upper tail bound by the moment generating function for \(\theta<1\): \(\lim n^{-1}\log\mathbb E e^{\theta T_j}=\log[2/(2-\theta)]\). For the lower bound on \(s>1\), require \(G_j/n\) close to \(1\) and \(E_j/n\) above \(s-1\), obtaining exponent \((1-\log2)+(s-1)=s-\log2\). For \(s\le1\), the gamma tail alone realizes the bound. At \(s=1\), these formulas coincide.

**3. Extreme-domain threshold.** Let \(p_n(s)=\Pr(T_j>ns)\). Independence gives \(\Pr(T_{m,n}\le ns)=[1-p_n(s)]^m\). As \(m=\exp[(\alpha+o(1))n]\), the previous logarithmic tail shows that this probability tends to \(1\) whenever \(I(s)>\alpha\) and tends to \(0\) whenever \(I(s)<\alpha\). For \(s\le1/2\), the ordinary law of large numbers gives a nonvanishing single-domain survival probability and the same lower conclusion. Monotonicity and strict increase of \(I\) on \((1/2,\infty)\) imply convergence in probability to its unique solution \(s_\alpha\). The change of analytic expression at \(s=1\) occurs exactly at \(\alpha_*=I(1)=1-\log2\). Differentiating the inverse rate shows \(s_\alpha'\to1\) from either side, \(s_\alpha''\to-1\) from the left, and \(s_\alpha''=0\) on the right.

**4. Mechanism of the last surviving domain.** The good joint large-deviation rate \(J\) has a unique minimizer \((g_{s_\alpha},e_{s_\alpha})\) over \(\{g+e\ge s_\alpha\}\), with value \(\alpha\). For every fixed \(\varepsilon>0\), choose a sufficiently small \(\delta>0\). By strict uniqueness and compact level sets, the infimum of \(J\) over
\[
\bigl\{(g,e):s_\alpha-\delta\le g+e\le s_\alpha+\delta,\ \|(g,e)-(g_{s_\alpha},e_{s_\alpha})\|\ge\varepsilon\bigr\}
\]
is strictly greater than \(\alpha\). The joint large-deviation upper bound, multiplied by \(m_n=\exp[(\alpha+o(1))n]\), proves that with probability tending to one no domain ending within this small time window has a decomposition far from the unique minimizer. Step 3 puts the last domain inside the window with probability tending to one. This proves the stated convergence for \((G_{J_n}/n,E_{J_n}/n)\).

**5. Discrete-sweep normalization.** If instead each attempt selects one of the \(N\) sites uniformly and \(K\) attempts are needed for absorption, the clock superposition is a rate-\(N\) Poisson process with identical selected-site sequence. Its independent interattempt gaps give \(T_{m,n}=N^{-1}\sum_{i=1}^K Z_i\), where \(Z_i\) are independent \(\operatorname{Exp}(1)\). The union Chernoff bound at any fixed parameter \(0<\theta<1\) shows \(\mathbb ET_{m,n}=O(n+\log m)=O(n)\). Since the gap sequence is independent of \(K\), the exact mean-square difference is \(\mathbb E[(T_{m,n}-K/N)^2]=\mathbb EK/N^2=\mathbb ET_{m,n}/N=O(n/N)\). Thus \((K/N-T_{m,n})/n\to0\) in \(L^2\), and the extinction-time conclusion holds equally for discrete attempts measured in sweeps. The decomposition into \(G_j,E_j\) is defined in the continuous-clock realization.

## Verification

Run `python3 check.py` from the directory containing this document. The self-contained script uses the Python standard library and verifies the exact finite-state Laplace transform by rational recursion for several finite rings; it checks the survival identity, rate-function asymptotics and piecewise critical optimizer and compares finite-domain simulations with exact probabilities. On the delivered package the script completed 76 checks. Numerical tests corroborate algebra and normalization but do not replace the infinite large-deviation and extreme-value proof above.

## Relationship to prior work

Cao, Jiang and Zhang (2026) introduced the kinetic-sector dynamics and proved exact mean absorption times for a fully exposed spin preparation and one macroscopic minus block; their Appendix C gives finite-block waiting-time transforms and general first-step recursions. Those formulas and the domain-erosion mechanism are credited here. The present result instead studies \(m\) independent *deterministically equally sized*, logarithmically growing minus domains; its sharp joint large-domain/large-count transition, the nondifferentiability of the second derivative, and the last-domain decomposition require nonuniform large-deviation and extreme-value analysis. They are not stated as such in that source. An earlier exact arbitrary-initial-domain analysis already establishes the complete finite-time absorption CDF, including the independent gamma-plus-exponential factors used here; the finite-time formula and its specialization to equally long runs are **not** claimed as new. That analysis establishes Gumbel and Gaussian limits for its fastest and slowest configurations but not the exponentially many, simultaneously growing equal-length domain transition or the conditional two-stage structure of the last surviving domain. Separate work on Bernoulli-prepared domains treats random domain lengths and a different Gumbel regime; this does not state the selected-domain mechanism identified here. General Cramér large deviations and extreme-value techniques are standard tools and are not claimed as new.

## Limitations

The theorem assumes equally spaced permanent plus seeds, independent rate-one site clocks, irreversible boundary flips, and a positive finite limit of \(\log m/n\). It proves first-order scaling in probability, not a centered Gumbel theorem, convergence of expectations, or robustness to random domain lengths or reverse flips. The threshold is a feature of this microscopic two-stage hazard structure and need not persist in other kinetic models. An exact finite-size generating function in existing literature may imply further properties through separate asymptotic analysis; prior implicit coverage is a residual originality risk. No independent scientific audit is claimed.

## References

1. D. Cao, W. Jiang, and Y. Zhang, *Kinetic Sectors and Nonequilibrium Dynamics in the \(\delta\)-Ising Model*, arXiv:2610.36829v1 (first submitted 2026-10-27), especially Section IV.B and Appendix C. https://arxiv.org/abs/2610.36829
2. H. Cramér, *Sur un nouveau théorème-limite de la théorie des probabilités*, Actualités Scientifiques et Industrielles **736** (1938). Classical large-deviation principle; the application here is proved explicitly above.
