# Optimal independent clocks for adjacent-cycle rendezvous: an exact time–movement tradeoff

## Finding

Let \(n\geq3\) be an integer and let \(X_t,Y_t\) be independent walks on the same cycle \(C_n=\mathbb Z/n\mathbb Z\). They begin at adjacent vertices, \(X_0=0\), \(Y_0=1\). At each integer tick, each walker independently moves with probability \(p\in(0,1)\), choosing either neighboring vertex with probability \(1/2\), and otherwise stays put. Meetings are checked at tick endpoints, not during edge traversals. Write \(T_{n,p}=\inf\{t\geq1:X_t=Y_t\}\) and \(M_{n,p}\) for the total number of individual moves up to and including that tick.

**Theorem.** For \(a_k=1-\cos(2\pi k/n)\),
\[
H_n(p):=\mathbb E T_{n,p}
=\sum_{k=1}^{n-1}\frac{1}{p(2-pa_k)}.
\]
Writing \(r(p)=(1-\sqrt{1-p})/(1+\sqrt{1-p})\), this has the equivalent finite closed form
\[
H_n(p)=\frac{n}{2p\sqrt{1-p}}
\frac{1+(-r(p))^n}{1-(-r(p))^n}-\frac{1}{2p}.
\]
For every \(n\geq3\), the function \(H_n\) is strictly convex on \((0,1)\) and has exactly one global minimizer \(p_n\in(0,1)\). These minimizers and their optimal clock times satisfy
\[
p_n=\frac23-\frac{2\sqrt3}{27n}+O(n^{-2}),\qquad
H_n(p_n)=\frac{3\sqrt3}{4}n-\frac34+O(n^{-1}).
\]
In contrast,
\[
\mathbb E M_{n,p}=2pH_n(p)
=2\sum_{k=1}^{n-1}\frac{1}{2-pa_k}
\]
is *strictly increasing* in \(p\), and \(\inf_{0<p<1}\mathbb E M_{n,p}=n-1\), attained only as \(p\downarrow0\). Thus the time-optimal independent clock approaches a move probability of \(2/3\), while minimizing the expected number of moves instead favors an arbitrarily slow clock.

At \(p=1\), the expected meeting time is infinite when \(n\) is even, whereas \(H_n(1)=(n^2-1)/2\) for odd \(n\); in particular the optimal interior point is not an artifact of the open parameter interval. For \(n=3\), the elementary special case \(p_3=2/3\) is already consistent with earlier triangle rendezvous calculations and is **not** claimed as a new isolated result.

## Assumptions and scope

The walks are independent, share the same fixed clock parameter, make independent clockwise/counterclockwise choices, and undergo synchronous *observations* at integer times. A tick may contain zero, one or two actual moves. The walkers do not coordinate their clocks and cannot use the other's location. The graph is the undirected unweighted simple cycle on \(n\geq3\) vertices. The first meeting counts equal *vertices after updates*; passing on edges does not count. At \(p\in(0,1)\) the relative chain is irreducible and aperiodic, so \(T_{n,p}\) has finite expectation. All bounds and optimizations are over \(p\) common to both walkers; adaptive, unequal or state-dependent clocks are excluded.

The parameter \(p\) is the probability of moving, **not** the holding probability. In the alternative holding-probability convention, the asymptotically clock-optimal hold probability tends to \(1/3\).

## Proof

**1. Relative chain and exact mean.** Set \(Z_t=X_t-Y_t\pmod n\). Its one-step characteristic value at Fourier angle \(\theta_k=2\pi k/n\) is \(\lambda_k=(1-p+p\cos\theta_k)^2\), because each coordinate's symmetric one-step characteristic function is \(1-p+p\cos\theta_k\). For \(1\leq k\leq n-1\) we have \(0\leq\lambda_k<1\). The function
\[
h(x)=\sum_{k=1}^{n-1}
\frac{1-\cos(\theta_k x)}{1-\lambda_k}
\]
vanishes at \(x=0\) and satisfies \((I-P)h(x)=1\) at each \(x\ne0\): the Fourier sum \(\sum_{k=1}^{n-1}\cos(\theta_k x)=-1\) for nonzero \(x\pmod n\). Uniqueness of the finite killed-chain Poisson equation makes \(h(x)\) the mean first hitting time of zero. With initial separation \(1\), canceling \(1-\cos\theta_k\) in
\[
1-\lambda_k=p(1-\cos\theta_k)(2-p+p\cos\theta_k)
\]
yields the first displayed formula for \(H_n(p)\).

**2. Exact summation.** For \(0<p<1\), put \(s=\sqrt{1-p}\), \(r=(1-s)/(1+s)\). A Poisson-kernel expansion gives
\[
\frac{1}{2-p+p\cos\theta}=
\frac{1}{2s}\left[1+2\sum_{j\geq1}(-r)^j\cos(j\theta)\right].
\]
Sum at \(\theta_k\) over \(0\leq k<n\). Only Fourier frequencies divisible by \(n\) survive, so the bracket sums to \(n[1+(-r)^n]/[1-(-r)^n]\). Subtract the \(k=0\) term \(1/2\), then divide by \(p\), to obtain the stated closed form. Every geometric series converges absolutely because \(0<r<1\).

**3. Strict convexity and finite optimizers.** Each summand is \(f_a(p)=1/g_a(p)\), where \(g_a(p)=2p-ap^2>0\) and \(a=a_k\in(0,2]\). As \(g_a''=-2a<0\),
\[
f_a''(p)=\frac{2(g_a'(p))^2}{g_a(p)^3}+\frac{2a}{g_a(p)^2}>0.
\]
Thus \(H_n\) is strictly convex. Its limit as \(p\downarrow0\) is infinity. If \(n\) is even, \(a_{n/2}=2\), so \(H_n(p)\to\infty\) as \(p\uparrow1\); an interior unique minimum follows. If \(n\) is odd, at \(p=1\) the relative walk has jump \(\pm2\) each with probability \(1/4\) and holds with probability \(1/2\). Multiplication by the inverse of two modulo \(n\) maps it to a half-lazy simple walk started at \((n+1)/2\), so its mean hitting time is \(2[(n+1)/2][(n-1)/2]=(n^2-1)/2\). For odd \(n\ge5\), the finite-sum expression at \(p=2/3\) implies
\[
H_n(2/3)\le\frac94(n-1)<\frac{n^2-1}{2}=H_n(1).
\]
For \(n=3\), \(H_3(p)=4/[p(4-3p)]\), with \(H_3(2/3)=3<H_3(1)=4\). Hence all odd cycles also have an interior minimizer, necessarily unique.

**4. Asymptotic optimum.** For every fixed \(0<p<1\), Riemann summation, including one differentiation with respect to \(p\), gives
\[
\lim_{n\to\infty}\frac{H_n(p)}n=
G(p)=\frac{1}{2p\sqrt{1-p}},\qquad
G'(p)=\frac{3p-2}{4p^2(1-p)^{3/2}}.
\]
For each fixed \(\varepsilon\in(0,1/3)\), \(G'(2/3-\varepsilon)<0<G'(2/3+\varepsilon)\). Differentiated Riemann sums then give the same signs for \(H_n'\) for all sufficiently large \(n\). Strict convexity traps \(p_n\) between these fixed points. Consequently \(p_n\to2/3\). In a fixed compact neighborhood of \(2/3\), the finite geometric correction in Step 2 and its first derivative are respectively \(O(n\rho^n)\) and \(O(n^2\rho^n)\) for some \(\rho<1\). Therefore
\[
H_n'(p)=nG'(p)+\frac{1}{2p^2}+O(n^2\rho^n).
\]
At \(p_0=2/3\), \(G'(p_0)=0\), \(G''(p_0)=81\sqrt3/16\), and \(1/(2p_0^2)=9/8\). A Taylor expansion of the unique equation \(H_n'(p_n)=0\) yields
\[
p_n-p_0=-\frac{9/8}{n(81\sqrt3/16)}+O(n^{-2})
=-\frac{2\sqrt3}{27n}+O(n^{-2}).
\]
Substitution back into \(H_n\) gives \(H_n(p_n)=nG(p_0)-1/(2p_0)+O(n^{-1})=(3\sqrt3/4)n-3/4+O(n^{-1})\).

**5. Move-count comparison.** Let \(V_t\) be the number of walkers making actual moves at tick \(t\). The \(V_t\) are iid, take values \(0,1,2\), and satisfy \(\mathbb EV_t=2p\). The finite-mean stopping time \(T_{n,p}\) is adapted to the update sequence, so Wald's first identity (or direct summation of \(\mathbb E[V_t\mathbf1_{T\ge t}]\)) gives \(\mathbb EM_{n,p}=2pH_n(p)\). Its derivative is
\[
\frac{d}{dp}\mathbb EM_{n,p}=
2\sum_{k=1}^{n-1}\frac{a_k}{(2-pa_k)^2}>0.
\]
Taking \(p\downarrow0\) gives \(\inf\mathbb EM_{n,p}=n-1\), not attained at any positive clock rate.

## Verification

The standalone file `CHECK.py` constructs the exact killed transition matrix for the separation process from independently drawn movement decisions. It solves the finite Poisson equation using exact rational arithmetic for \(3\le n\le14\) and five rational rates per size, comparing with both the spectral and closed-form expressions. It also checks the \(n=3,4\) simplifications and numerical optimizer corrections at five larger sizes. It passed 193 assertions. These finite tests supplement, and do not replace, the all-size analytic proof above. Reproduce with `python CHECK.py` using Python 3, SymPy and SciPy.

## Relationship to prior work

Coelho and Prado, *Reinforced random walks with geometric inter-transition times*, arXiv:2606.05386 (first publicly submitted June 3, 2026), study independent geometric transition clocks in reinforced interacting walks, focusing on occupation laws. Their stochastic-clock motivation prompts a distinct first-meeting question for independent simple random walkers; the present theorem does not claim to extend their reinforcement results.

Classical symmetric Markovian rendezvous search on cycles is *not* new. Alpern, *The Rendezvous Search Problem* (1995), and the full exposition by Alpern and Gal, *The Theory of Search Games and Rendezvous* (2003, Section 15.4.1), treat common movement probabilities, the relative-distance killed chain, mean rendezvous optimization, strict convexity and some finite cycle examples. The latter explicitly studies **random initial locations** and reports finite-size calculations. We credit this structure and do not claim to discover the relative-chain reduction, the generic uniqueness argument, or the three-vertex optimizer. The present statement instead fixes **initial separation exactly one** and quantifies the optimizer over *all* cycle sizes, its sharp first-order large-cycle correction, a closed Poisson-kernel representation, and the opposing total-jump objective. The 1995 article itself could not be read in full, after a lawful full-text search; priority of these sharper conclusions is therefore a residual risk.

Zhang, Tan and Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph* (2014), derive a relative-chain Fourier representation for the **uniform initial distribution** and show the random-start mean on a circle is of quadratic order in its size. Their accessible preprint includes the general spectral method and arbitrary per-walker stay/move probabilities. The adjacent-start mean here is of linear order at fixed interior \(p\), and the minimizer's \(n^{-1}\) correction and move-budget comparison are not established by their uniform-start result. The general Fourier method is credited rather than presented as newly invented.

Alpern and Zeng, *Social Distancing, Gathering, Search Games: Mobile Agents on Simple Networks* (2022), investigate independent lazy walkers and obtain, among other results, the triangle loop-random-walk optimum. That triangle case is credited; their cycle results for larger sizes address dispersion rather than the present adjacent-start time and move count. McAvoy, *Meeting times on graphs in near-cubic time* (2026), considers a pair process where exactly one walker moves per tick, unlike independent simultaneous Bernoulli clocks here.

## Limitations

Novelty is assessed against the examined and searchable literature, not guaranteed against every earlier source. Two-agent cycle rendezvous with symmetric Markovian strategies has been studied since at least 1981, with explicit mean-optimization treatment in 1995 and 2003. An earlier adjacent-start asymptotic optimizer formula, unindexed or contained in the inaccessible 1995 text, remains a material historical-priority risk. The finding assumes a fixed common \(p\), two walkers, adjacent start and vertex-only meetings. It says nothing about unequal clocks, coordinated schedules, arbitrary initial separations, continuously observed edge crossings or adaptive controls. The stronger all-graph or all-starts optimization problem is open here. Independent mathematical validation has not been performed.

## References

1. M. G. Coelho and F. P. A. Prado, *Reinforced random walks with geometric inter-transition times*, arXiv:2606.05386, https://arxiv.org/abs/2606.05386 (first posted 2026-06-03).
2. S. Alpern and L. Zeng, *Social Distancing, Gathering, Search Games: Mobile Agents on Simple Networks*, Dynamic Games and Applications 12 (2022), 288–311, https://doi.org/10.1007/s13235-022-00427-1.
3. A. McAvoy, *Meeting times on graphs in near-cubic time*, arXiv:2604.18872, https://arxiv.org/abs/2604.18872 (first posted 2026-04-20).
4. S. Alpern, *The Rendezvous Search Problem*, SIAM J. Control Optim. 33 (1995), 673–683, https://doi.org/10.1137/S0363012993249195 (full text not accessible in this review).
5. S. Alpern and S. Gal, *The Theory of Search Games and Rendezvous*, Kluwer, 2003, Section 15.4.1, https://doi.org/10.1007/b100809 (relevant chapter text inspected).
6. Y. Zhang, Z. Tan and B. Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph*, arXiv:1408.2005, https://arxiv.org/abs/1408.2005 (full preprint inspected).
7. Standard Fourier solution of the finite-cycle first-hitting Poisson equation and the Poisson kernel identity (both derived explicitly above).
