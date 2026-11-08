# Strict convex-order polarization under heterogeneous cross-topic averaging

## Finding

For a directed strongly connected social network, heterogeneous person-specific weights on already-consensual source topics can sustain disagreement on a derived topic. If the total weight on the source topics is increased uniformly from \(a\) to \(b\), with \(0<a<b\le1\), the derived-topic equilibrium at the smaller weight is an **explicit strictly positive Markov average** of the equilibrium at the larger weight. In particular, the distribution of derived-topic opinions, weighted by the social network's stationary influence measure, increases in **convex order** with the source-topic weight: for every continuous convex \(\varphi:[0,1]\to\mathbb R\),

\[
\sum_{i=1}^{n}\pi_i\varphi(h_{a,i})\le \sum_{i=1}^{n}\pi_i\varphi(h_{b,i}).
\]

Every strictly convex test gives a strict inequality if and only if the individuals' mixtures of source consensus values are not all equal. The stationary weights are essential: an explicit three-person strongly connected example shows that ordinary unweighted cross-sectional variance can **decrease** over the same parameter increase.

## Assumptions and scope

Fix integers \(n\ge2\) and \(r\ge2\). Let \(T_j\), for \(1\le j\le r\), be primitive nonnegative row-stochastic \(n\times n\) matrices; source-topic opinions \(y^{(j)}(t)\in[0,1]^n\) evolve by \(y^{(j)}(t+1)=T_jy^{(j)}(t)\). Each converges to \(c_j\mathbf1\) for some \(c_j\in[0,1]\). Let \(S\) be any **irreducible** nonnegative row-stochastic \(n\times n\) matrix, possibly nonsymmetric, nonreversible, or periodic. Its unique invariant probability vector is \(\pi>0\), with \(\pi^\top S=\pi^\top\), \(\sum_i\pi_i=1\).

Each individual \(i\) has a row of nonnegative topic weights \(\theta_{ij}\ge0\) with \(\sum_{j=1}^r\theta_{ij}=1\). The derived topic starts at an arbitrary \(x(0)\in[0,1]^n\), and for a fixed \(\varepsilon\in(0,1]\) obeys

\[
x_i(t+1)=(1-\varepsilon)\sum_{k=1}^{n}S_{ik}x_k(t)
 +\varepsilon\sum_{j=1}^{r}\theta_{ij}y_i^{(j)}(t).
\]

This is an acyclic source-to-derived-topic multiplex update with individual-dependent interlayer mixtures and a **shared total coupling strength** \(\varepsilon\). Define \(w_i=\sum_j\theta_{ij}c_j\), \(\mu=\pi^\top w\), and

\[
F_\varepsilon=\varepsilon[I-(1-\varepsilon)S]^{-1},\qquad
h_\varepsilon=F_\varepsilon w.
\]

The order comparison concerns the same \(S\), topic-weight matrix \((\theta_{ij})\), source initial states, and source consensus vector while varying only the positive total coupling strength. It does not assume a reversible graph or that the per-person source weights are identical.

## Proof

**Existence and normalization.** Since \(\|(1-\varepsilon)S\|_\infty=1-\varepsilon<1\), its powers decay. Each source tends to \(c_j\mathbf1\); writing the sink recurrence as a geometric convolution and splitting the summation into its bounded recent tail and decaying remote tail shows that
\[
\lim_{t\to\infty}x(t)=\varepsilon\sum_{k=0}^\infty (1-\varepsilon)^kS^kw=F_\varepsilon w.
\]
The nonnegative matrix \(F_\varepsilon\) is row-stochastic, and \(\pi^\top F_\varepsilon=\pi^\top\). Thus \(h_\varepsilon\in[0,1]^n\) and \(\pi^\top h_\varepsilon=\mu\) for every \(\varepsilon>0\).

**Exact comparison kernel.** For \(0<a<b\le1\), the rational matrix functions of \(S\) commute, so
\[
\begin{aligned}
K_{a,b}&=F_aF_b^{-1}\\
&=\frac ab\left[I+(b-a)S[I-(1-a)S]^{-1}\right]\\
&=\frac ab I+\frac{a(b-a)}b\sum_{k=1}^\infty(1-a)^{k-1}S^k.
\end{aligned}
\]
Every coefficient is nonnegative. For each ordered pair of vertices, irreducibility supplies a positive entry of some positive power \(S^k\), and \(a<1\); therefore \((K_{a,b})_{ij}>0\) for all \(i,j\). From \(S\mathbf1=\mathbf1\) and \(\pi^\top S=\pi^\top\), the displayed series gives \(K_{a,b}\mathbf1=\mathbf1\) and \(\pi^\top K_{a,b}=\pi^\top\). Crucially, \(h_a=K_{a,b}h_b\).

**Convex order and equality.** Jensen's inequality in every row of the strictly positive stochastic matrix \(K_{a,b}\) yields
\[
\varphi(h_{a,i})\le\sum_j(K_{a,b})_{ij}\varphi(h_{b,j}).
\]
Multiply by \(\pi_i\) and sum, using \(\pi^\top K_{a,b}=\pi^\top\), to get the stated inequality. When \(\varphi\) is strictly convex, equality in one row would force all entries of \(h_b\) equal. Because \(F_b\) is invertible and fixes \(\mathbf1\), \(h_b\) is constant if and only if \(w\) is constant. Thus if \(w\) is nonconstant every row has a strict Jensen gap, and strictness holds in the total sum; conversely a constant \(w\) gives equality for every \(\varphi\). For \(\varphi(u)=(u-\mu)^2\) this gives a strict increase in \(\pi\)-weighted variance. If \(S\) is doubly stochastic, \(\pi\) is uniform, so the result is the usual finite-vector majorization \(h_a\prec h_b\).

**Consensus boundary and small-coupling asymptotics.** At any fixed \(\varepsilon>0\), the derived topic reaches consensus precisely when \(w\) is constant. It reaches consensus for **every** source consensus vector \((c_j)\in[0,1]^r\) precisely when all rows of \((\theta_{ij})\) coincide. Put \(\Pi=\mathbf1\pi^\top\). On the invariant mean-zero subspace \(I-S\) is invertible, giving
\[
h_\varepsilon=\mu\mathbf1+\varepsilon g+O(\varepsilon^2),\quad
g=(I-S+\Pi)^{-1}(w-\mu\mathbf1),\quad \pi^\top g=0.
\]
Consequently
\[
\sum_i\pi_i(h_{\varepsilon,i}-\mu)^2
=\varepsilon^2\sum_i\pi_i g_i^2+O(\varepsilon^3),
\]
with positive leading coefficient exactly when \(w\) is nonconstant. The limit at \(\varepsilon\downarrow0\) does **not** identify the actual \(\varepsilon=0\) evolution, which can retain dependence on the sink's initial opinions.

**Stationary weights cannot generally be replaced by equal weights.** Consider
\[
S=\frac1{100}\begin{pmatrix}1&98&1\\1&99&0\\1&0&99\end{pmatrix},\quad
\pi=\frac1{100}(1,98,1)^\top,\quad w=(1/2,1,0)^\top.
\]
This \(S\) is strongly connected and has positive diagonal. It is realized by two source consensus values \(c_1=1\), \(c_2=0\) with \(\theta_{i1}=w_i\), \(\theta_{i2}=1-w_i\). For \(a=1/5\) and \(b=4/5\), direct exact-rational inversion gives **uniformly centered** unweighted variances
\[
\frac13\sum_i(h_{a,i}-\overline h_a)^2
=\frac{14071}{76050}
>\frac{6075272}{36180225}
=\frac13\sum_i(h_{b,i}-\overline h_b)^2,
\quad \overline h_\varepsilon=\frac13\sum_i h_{\varepsilon,i}.
\]
Nevertheless the theorem gives the strict opposite ordering for the corresponding \(\pi\)-weighted variances, so this counterexample identifies the appropriate weighting, not an exception to the theorem.

## Verification

Run `python verify.py` with Python 3 and `sympy`. The exact-rational checker compares the resolvent and the comparison kernel, row sums and invariant stationary weights, three convex hinge functionals, and strict stationary-weighted variance inequalities on 48 directed positive-matrix cases of sizes \(2\)–\(5\). It also checks the explicit two-person disagreement example and the exact three-person unweighted-variance reversal above. All assertions passed. The finite computations are **sanity checks only**; generality and strictness follow from the analytic argument.

## Relationship to prior work

Zender, Shi, Hickok, Chu and Porter (2026), Section 5.4 and Section 7.2.1, study acyclic multiplex DeGroot dynamics with node-*homogeneous* interlayer weights, derive equilibrium block expressions and consensus from strongly connected source layers, and explicitly identify heterogeneous interlayer weights as a further direction. Their results do not state a parameter-wise Markov comparison across heterogeneous mixtures. Ye, Liu, Wang, Anderson and Cao (2020) already provide broad consensus/disagreement criteria for heterogeneous belief systems: **heterogeneity-induced disagreement is not claimed as new here**. Standard Friedkin–Johnsen and personalized-PageRank literature supplies resolvent expressions; neither the resolvent representation nor elementary Jensen's inequality is claimed as new. The specific combination of an explicit strictly positive **inter-parameter** kernel, sharp strict \(\pi\)-convex-order comparison for all directed irreducible networks, and an exact failure of uniform-node variance under the same model is the proposition assessed here.

## Limitations

The result concerns one derived topic driven by consensus-forming source topics, nonnegative person-specific source weights, and a scalar **shared** total coupling parameter; it does not cover agent-dependent total coupling rates, endogenous interlayer cycles, antagonistic signed influence, nonlinear opinion updates or changing networks. It asserts deterministic equilibrium convex order, not an empirical polarization law. Uniform-weighted variance need not be monotone on non-doubly-stochastic networks. The consensus classification for heterogeneous belief systems and the basic resolvent are pre-existing; novelty of the full ordered comparison remains conditional on the completeness of accessible literature, and no independent audit is claimed.

## References

1. M. Zender, K. Shi, A. Hickok, W. Chu, M. A. Porter, *DeGroot Dynamics on Multiplex Networks with Directed and Acyclic Interlayer Connectivities*, arXiv:2610.27198v1, first public 2026-10-19, https://arxiv.org/html/2610.27198v1 . Sections 4, 5.4.1, 5.4.3, 7.2.1 and Appendix A.
2. M. Ye, J. Liu, L. Wang, B. D. O. Anderson, M. Cao, *Consensus and Disagreement of Heterogeneous Belief Systems in Influence Networks*, IEEE Transactions on Automatic Control **65** (2020), 4679–4694, DOI:10.1109/TAC.2019.2961998, https://research.rug.nl/files/137419308/08941271.pdf . Sections III–IV.
3. S. Neumann, Y. Dong, P. Peng, *Sublinear-Time Opinion Estimation in the Friedkin–Johnsen Model*, arXiv:2404.16464, 2024, https://arxiv.org/abs/2404.16464 .
4. K. Avrachenkov, R. van der Hofstad, M. Sokol, *Personalized PageRank with Node-dependent Restart*, arXiv:1408.0719, 2014, https://arxiv.org/abs/1408.0719 .
