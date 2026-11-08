# Pendant conductance orders first-passage fluctuations without changing their mean

## Finding
Let \(G\) be any finite connected undirected graph, with symmetric positive edge jump rates \(c_{ij}=c_{ji}\). Fix distinct vertices \(x,y\) and a vertex \(v\ne y\). Attach one new leaf \(p\) to \(v\) by an edge of rate \(w>0\). A continuous-time walk jumps independently along each incident edge at that edge's rate (the variable-speed, symmetric-rate walk). Denote its first hitting time of \(y\), from \(x\), by \(T_w\). On the original graph let \(T_0\) denote the hitting time of \(y\) and define the pre-hitting occupation time \(L_v=\int_0^{T_0}\mathbf1_{\{X_t=v\}}\,dt\).

For every \(w>0\), \(T_w\) has the conditional compound-Poisson representation
\[
T_w\ \stackrel{d}{=}\ T_0+\sum_{j=1}^{N_w}E_{j,w},\qquad
N_w\mid(X_t)_{0\le t\le T_0}\sim\operatorname{Pois}(wL_v),\qquad
E_{j,w}\sim\operatorname{Exp}(w),
\]
where the exponential variables are conditionally independent of the Poisson count. Equivalently, for \(s\ge0\),
\[
\mathbb E e^{-sT_w}=\mathbb E\exp\!\left(-sT_0-\frac{ws}{w+s}L_v\right).
\]
For any \(0<w_1<w_2\),
\[
\boxed{T_{w_2}\le_{\mathrm{cx}}T_{w_1}},
\]
meaning \(\mathbb E\varphi(T_{w_2})\le\mathbb E\varphi(T_{w_1})\) for every convex function for which both expectations exist. Moreover,
\[
\mathbb E T_w=\mathbb E(T_0+L_v),\qquad
\operatorname{Var}(T_w)=\operatorname{Var}(T_0+L_v)+\frac{2\mathbb E L_v}{w}.
\]
If \(\Pr(L_v>0)>0\), the convex ordering is strict for the test function \(\varphi(t)=t^2\); every pair of different-rate laws is incomparable in first-order stochastic order, and their Laplace transforms are strictly ordered in the reverse direction. In the rare-trap limit \(w\downarrow0\), \(T_w\) converges to \(T_0\) in total variation while its mean stays at \(\mathbb E T_0+\mathbb E L_v\). In the rapid-excursion limit \(w\to\infty\), \(T_w\) converges in \(L^2\) under a suitable coupling to \(T_0+L_v\).

## Assumptions and scope
All vertices and edges are finite in number and all existing edge rates are strictly positive. The random walk has generator \((Qf)(i)=\sum_{j\sim i}c_{ij}(f(j)-f(i))\); it is **not** the rate-one walk that selects a neighbor proportionally to conductance. Both starting vertex \(x\) and absorbing target \(y\) are in the original core, with \(x\ne y\), and the added leaf is not the target. The strict results require positive probability that the original walk spends positive time at \(v\) before reaching \(y\). If this occupation time is zero almost surely, all the laws coincide. At \(w=0\), the isolated leaf is not part of the state space used for the hitting problem; statements at zero are distributional limits, not continuity of the expectation.

## Proof
**1. Excursion decomposition.** Construct the original core walk using independent exponential edge clocks in the elapsed time spent at each core vertex. Along its occupation-time clock at \(v\), add an independent rate-\(w\) Poisson process of departures to \(p\). Each departure is followed by an independent exponential holding time of rate \(w\) at \(p\), then a forced return to \(v\). Pause the core clocks during these excursions. Memorylessness makes the resulting chronological process exactly the rate-\(c_{ij}\) core walk with the new rate-\(w\) edge. Until the original core path first reaches \(y\), the number of inserted excursions is conditionally Poisson with mean \(wL_v\); this proves the representation. Its conditional Laplace transform is
\[
\exp\!\left(wL_v\left(\frac{w}{w+s}-1\right)\right)
=\exp\!\left(-\frac{ws}{w+s}L_v\right).
\]
Conditionally on the core path, the extra time has mean \(L_v\) and variance \(2L_v/w\). Taking conditional expectations and variances proves both moment identities, including the covariance between \(T_0\) and \(L_v\) in the baseline term.

**2. Mean-preserving semigroup and convex order.** For each \(t>0\), define a Markov kernel \(K_t(z,\cdot)\) on \([0,\infty)\) as the distribution of a sum of \(\operatorname{Pois}(z/t)\) independent exponentials of mean \(t\); let \(K_0(z,\cdot)\) be a point mass at \(z\). Its Laplace transform is
\[
\int e^{-s u}\,K_t(z,du)=\exp\!\left(-\frac{zs}{1+ts}\right).
\]
The identity
\[
\frac{\frac{s}{1+ts}}{1+u\frac{s}{1+ts}}=\frac{s}{1+(t+u)s}
\]
and uniqueness of Laplace transforms prove the Chapman–Kolmogorov law \(K_tK_u=K_{t+u}\). Each kernel preserves the mean \(z\), as follows by differentiation at \(s=0\), and its variance is \(2zt\). Therefore if \(t_2>t_1\), the later kernel is obtained from the earlier by a mean-preserving Markov transition, so conditional Jensen gives convex-order growth in \(t\). The inserted excursion time at conductance \(w\), conditional on the core path, has exactly law \(K_{1/w}(L_v,\cdot)\). Adding the fixed conditional offset \(T_0\), then averaging, proves \(T_{w_2}\le_{\mathrm{cx}}T_{w_1}\) when \(w_2>w_1\). This also gives a joint martingale coupling for all reciprocal conductances; no unproved diffusion-existence theorem is needed.

**3. Strictness and stochastic incomparability.** For \(s>0\), the coefficient \(ws/(w+s)\) strictly increases with \(w\). Hence the displayed Laplace transform strictly decreases with \(w\) if \(\Pr(L_v>0)>0\). The variance formula also gives a strictly positive difference \(2\mathbb E L_v(1/w_1-1/w_2)\). Since both laws have identical finite means, first-order stochastic dominance in either direction would force equality in distribution by integrating the difference of survival functions; this contradicts strict variance or Laplace difference.

**4. Singular limits.** In the coupling of step 1, \(\Pr(N_w>0)\le w\mathbb E L_v\). Therefore \(d_{\mathrm{TV}}(\mathcal L(T_w),\mathcal L(T_0))\le w\mathbb E L_v\to0\). Yet \(\mathbb ET_w-\mathbb ET_0=\mathbb EL_v\) at every positive \(w\). Under the kernel coupling of step 2, \(K_{1/w}(L_v,\cdot)\) has conditional mean \(L_v\) and conditional squared deviation \(2L_v/w\). Thus \(\mathbb E[(T_w-(T_0+L_v))^2]=2\mathbb EL_v/w\to0\) as \(w\to\infty\).

**5. Exact diagnostic example.** On a two-vertex core consisting of the unit-rate edge \(a-b\), start at \(a=v\) and hit \(b\). Then \(T_0=L_v\sim\operatorname{Exp}(1)\), and
\[
\mathbb E e^{-sT_w}=\frac{s+w}{s^2+(1+2w)s+w},\quad
\mathbb ET_w=2,\quad
\operatorname{Var}(T_w)=4+\frac2w.
\]
For \(w\downarrow0\) the law converges to \(\operatorname{Exp}(1)\) although its mean stays \(2\); for \(w\to\infty\) it converges to \(2\operatorname{Exp}(1)\).

## Verification
The independent finite-generator inversion in `checker.py` verifies the conditional resolvent identity against the complete augmented continuous-time chain at rational rates. Six nonconstant-rate core configurations and five leaf conductances are checked, with three positive rational Laplace parameters for each configuration. Full-generator first and second moments are compared to the conditional local-time reward formulas. The symbolic three-vertex transform, derivative sign, singular limits, mean-preserving kernel composition and an attachment hidden behind the target are separately checked. Running `python checker.py` with SymPy prints `VERIFY_OK 167 exact rational and symbolic assertions`. All computations use exact rational or symbolic arithmetic; the arbitrary-graph theorem follows from the proof, not from the finite tests.

## Relationship to prior work
Grebenkov and Tupikina's heterogeneous continuous-time random-walk formalism (2017 preprint) provides general Laplace-propagator and first-passage methods for heterogeneous networks, including weighted graphs. Oliveira and Peres (2018) study hitting-time and return-probability bounds for discrete-time lazy graph walks. Zatloukal (2020) gives local-time resolvent calculations for discrete-time graph walks. None of these inspected papers states the mean-preserving reciprocal-conductance convex-order family for a single pendant edge, the exact affine reciprocal-variance law, or the non-uniformly-integrable zero-rate limit. Their general transforms and local-time tools are relevant precursors and may lead to an alternative derivation; the claim is the explicit familywise comparison, not a new general theory of first passage or occupation times.

## Limitations
The conclusions require symmetric edge *jump rates*; they do not automatically extend to unit-total-rate random walks or to destination/initial vertices on the appended leaf. The strict inequalities vanish when the core first-passage path cannot visit the attachment vertex. The result is an explicit specialization of classical Markov excursion machinery; previous unlocated literature may have an equivalent pendant-edge comparison. Historical priority and independent mathematical review remain open.

## References
1. D. S. Grebenkov and L. Tupikina, *Heterogeneous continuous time random walks*, arXiv:1712.01020 (first public 2017-12-04), https://arxiv.org/abs/1712.01020.
2. R. I. Oliveira and Y. Peres, *Random walks on graphs: new bounds on hitting, meeting, coalescing and returning*, arXiv:1807.06858 (first public 2018-07-18), https://arxiv.org/abs/1807.06858.
3. V. Zatloukal, *Local time of random walks on graphs*, arXiv:2012.15399 (first public 2020-12-31), https://arxiv.org/abs/2012.15399.
