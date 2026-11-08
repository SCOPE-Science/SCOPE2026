# A sharp self-averaging criterion for noisy voting on complete bipartite networks

## Finding

**Theorem.** Let \(a,b\ge1\) be integers and \(\mu>0\). On the unweighted complete bipartite contact graph \(K_{a,b}\), assign each vertex a spin \(\sigma_v\in\{-1,+1\}\). Each vertex, independently, copies a uniformly selected neighbor at rate one, and resets to an independent fair spin at rate \(\mu\). Let \(N=a+b\), and in the unique stationary distribution write \(M=N^{-1}\sum_v\sigma_v\) for **unweighted** population magnetization. Then

\[
\operatorname{Var}(M)=\frac{N^2+2\mu(3+\mu)ab}{N\{N+2\mu(2+\mu)ab\}}.
\]

For two distinct vertices in the **same** part and two vertices in **opposite** parts respectively, their stationary spin correlations (whenever the pair exists) are

\[
C_{\mathrm{same}}=\frac{a+b}{a+b+2\mu(2+\mu)ab},\qquad
C_{\mathrm{cross}}=(1+\mu)C_{\mathrm{same}}.
\]

Thus an opposite-part pair is strictly more correlated than a distinct same-part pair whenever both exist. For fixed \(N\ge3\) and \(\mu>0\), variance is strictly decreasing in the product \(ab\); balancing the part sizes uniquely minimizes variance up to exchanging the parts, and the star maximizes it.

For **any** sequence of such graphs with \(N\to\infty\), and the same fixed \(\mu>0\), stationary \(M\to0\) in probability if and only if \(\min(a,b)\to\infty\). In contrast, for each fixed integer \(m\ge1\), along \(K_{m,b}\) as \(b\to\infty\),

\[
\lim_{b\to\infty}\operatorname{Var}(M)=\frac1{1+2\mu(2+\mu)m}>0.
\]

This is a sharp **non-self-averaging** law at fixed noise strength: growing a population around a bounded intermediary core cannot suppress global stationary opinion fluctuations.

## Assumptions and scope

The graph is finite, simple, undirected and complete bipartite, with two nonempty parts. The two per-vertex Poisson mechanisms are independent across vertices. Copying selects uniformly among the neighbors of the copying vertex, not among all edges globally. The reset clock rate \(\mu\) means resampling a fair spin (equivalent to a rate \(\mu/2\) flip). All statements are stationary, for a fixed positive \(\mu\). They concern the **unweighted** average of all vertex spins, not the degree-stationary-weighted voter density. They do not assert a limiting magnetization *distribution* when one part is bounded, or that the stationary law is bimodal.

## Proof

**1. Existence and symmetry.** At positive reset rate each individual spin can change to either sign with positive probability. The continuous-time chain on \(2^N\) configurations is irreducible and has a unique stationary law. It is invariant under global spin inversion and under permutations inside each part. Consequently \(\mathbb E\sigma_v=0\) and the three pair-correlation types below suffice.

**2. Exact stationary pair equations.** Set \(u=\mathbb E[\sigma_i\sigma_j]\) for distinct first-part vertices, \(v\) for distinct second-part vertices and \(w\) for opposite-part vertices. Empty correlation classes at part size one are handled by considering only their coefficients multiplied by zero. For any vertex \(i\), the generator satisfies

\[
L\sigma_i=-(1+\mu)\sigma_i+\frac1{\deg(i)}\sum_{j\sim i}\sigma_j.
\]

As distinct vertices do not jump simultaneously, \(L(\sigma_i\sigma_j)=\sigma_jL\sigma_i+\sigma_iL\sigma_j\). At stationarity this gives, when corresponding pairs exist,

\[
0=-2(1+\mu)u+2w,\qquad 0=-2(1+\mu)v+2w.
\]

For an opposite-part pair, copying can select its partner with probabilities \(1/b\) and \(1/a\); that contribution is exactly one rather than an unknown covariance. Hence

\[
0=-2(1+\mu)w+\frac1a+\frac1b
 +\left(1-\frac1b\right)v+\left(1-\frac1a\right)u.
\]

If a part has size one, its unused correlation may be formally set to \(w/(1+\mu)\), without affecting this last equation. Set \(s=1/a+1/b\), \(t=2\mu(2+\mu)>0\). Substitution yields the unique solution

\[
u=v=\frac{s}{s+t},\qquad w=\frac{(1+\mu)s}{s+t}.
\]

The strict cross-part excess is \(w-u=\mu s/(s+t)>0\). No mean-field approximation is used.

**3. Population variance.** Since spins square to one and have zero means,

\[
N^2\operatorname{Var}(M)=N+\bigl[a(a-1)+b(b-1)\bigr]u+2ab\,w.
\]

Using \(a(a-1)+b(b-1)=N^2-N-2ab\) and \(s=N/(ab)\) gives the displayed exact rational formula.

**4. Finite-size extremizers.** For fixed \(N,\mu\), regard the rational variance as a function of \(P=ab\). Its derivative equals

\[
\frac{\partial\operatorname{Var}(M)}{\partial P}=
\frac{2\mu\{3+\mu-N(2+\mu)\}}{\{N+2\mu(2+\mu)P\}^2}<0
\]

for every \(N\ge2\). Among integers \(a+b=N\), the product \(ab\) is maximal at the most balanced split and minimal at a star; both statements are strict, apart from swapping parts.

**5. Sharp asymptotic criterion.** Write \(H=ab/(a+b)\), so

\[
\operatorname{Var}(M)=\frac{1+2\mu(3+\mu)H/N}{1+2\mu(2+\mu)H}.
\]

For all positive \(a,b\), \(\min(a,b)/2\le H\le\min(a,b)\) and \(H/N\le1/4\). The numerator therefore lies between one and \(1+\mu(3+\mu)/2\), uniformly over all graph sizes. With fixed \(\mu>0\), variance tends to zero **exactly** when \(H\to\infty\), equivalently \(\min(a,b)\to\infty\). Because \(|M|\le1\) and \(\mathbb EM=0\), convergence in probability to zero is equivalent to convergence of the second moment to zero. When \(a=m\) is fixed and \(b\to\infty\), \(H\to m\) and \(H/N\to0\), proving the positive limiting variance. No assertion of Gaussian or other distributional convergence is needed.

## Verification

Run `python3 verify.py` from this directory. The standard-library checker constructs the *independent count-process generator* on state pairs \((i,j)\), where \(i\) and \(j\) are the plus-spin counts in the two parts. It solves the exact stationary master equation with rational Gaussian elimination, then independently computes group means, pair correlations and unweighted magnetization variance from the solved distribution. It checks every pair \(1\le a,b\le4\) at noise rates \(\mu\in\{1/4,1,5/2\}\), and independently checks fixed-order monotonicity for \(3\le N\le29\). It reports 48 finite exact stationary laws and 714 rational assertions. These finite checks support the algebra; the proof of all-size and infinite-sequence statements is analytic above.

## Relationship to prior work

The noisy-voter mechanism and the interest in opinion-noise fluctuations are motivated by Caligiuri and Galla (arXiv:2305.19096, first public May 30, 2023), whose full accessible preprint treats **all-to-all** contact graphs under switching environments and influencers rather than exact stationary second moments on a fixed bipartite contact graph. Carro, Toral and San Miguel (arXiv:1602.06935) derive general first- and second-moment equations, an important known ingredient; for heterogeneous random networks they use an **annealed approximation** and do not state the exact bipartite formula or the sharp smaller-part self-averaging criterion. Peralta et al. (arXiv:1807.04615) study stochastic **pair approximations**, not an exact stationary bipartite census. Ben-Ari et al. (arXiv:2004.10187) investigate the **noise-free quasi-stationary** voter law on complete bipartite graphs, a different stochastic question. Pymar and Rivera (arXiv:2112.01478) investigate the **degree-weighted** stationary density and asymptotic results, rather than the unweighted average here. The exact all-size formula and the if-and-only-if criterion were not located in inspected material; a presently unindexed equivalent could exist. Merely having generic second-moment equations is not represented as a new contribution.

## Limitations

The conclusions apply only to homogeneous positive reset rates and unit-rate copying on unweighted complete bipartite graphs. When noise vanishes, irreducibility fails, so the stationary uniqueness argument does not apply. Asymptotic self-averaging assumes noise is held fixed rather than scaled with network size. Positive variance does not by itself identify the limiting distribution or its number of modes. Priority against inaccessible or unindexed literature is not independently certified.

## References

1. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (first posted 2023-05-30), https://arxiv.org/abs/2305.19096.
2. A. Carro, R. Toral and M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (2016), https://arxiv.org/abs/1602.06935.
3. A. F. Peralta, A. Carro, M. San Miguel and R. Toral, *Stochastic pair approximation treatment of the noisy voter model*, arXiv:1807.04615 (2018), https://arxiv.org/abs/1807.04615.
4. I. Ben-Ari, H. Panzo, P. Speegle and R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (2020), https://arxiv.org/abs/2004.10187.
5. R. Pymar and N. Rivera, *On the stationary distribution of the noisy voter model*, arXiv:2112.01478 (2021), https://arxiv.org/abs/2112.01478.
