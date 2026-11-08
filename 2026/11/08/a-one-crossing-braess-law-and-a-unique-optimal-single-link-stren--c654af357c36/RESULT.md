# A one-crossing Braess law and a unique optimal single-link strength for weighted search networks

## Finding

For every finite connected undirected network with at least three vertices, adding one physical transport channel of fixed positive mean travel time produces only two possible global-search responses as its conductance is increased: universal harm at every positive strength, or initial improvement followed by a unique optimum and one exact crossover to permanent harm. In particular, a shortcut harmful at infinitesimal strength can never become beneficial at a larger strength when all original edges remain fixed.

Write \(L\) for the positive weighted graph Laplacian, \(G=L^\dagger\), and \(b=e_u-e_v\) for endpoints of the added channel. Define
\[
A=\operatorname{tr}G,\quad R=b^\top G b,\quad Q=b^\top G^2b,\quad B=AR-Q,
\qquad T_0=2\sum_{\{i,j\}\in E}g_{ij}t_{ij}.
\]
For a new channel of conductance \(w\ge0\) and traversal mean \(t>0\), the all-ordered-pairs mean first-passage time is
\[
\boxed{M(w)=\frac{(T_0+2tw)(A+Bw)}{(N-1)(1+Rw)}}.
\]
The constants \(A,R,Q,B,T_0\) are all strictly positive. Set \(t_*=T_0Q/(2A)\). If \(t\ge t_*\), every addition of positive conductance strictly worsens the mean and \(M\) increases strictly. If \(0<t<t_*\), there is a unique global minimizer
\[
\boxed{w_*=\frac{\sqrt{1+R(T_0Q-2tA)/(2tB)}-1}{R}}
\]
and the link is beneficial against the original network if and only if
\[
\boxed{0<w<w_{\rm return}:=\frac{T_0Q-2tA}{2tB}}.
\]
The return point is strictly larger than the optimal weight; at that point the original global search time is recovered exactly.

## Assumptions and scope

The graph has \(N\ge3\) vertices, is finite, connected, and undirected, with symmetric positive conductances \(g_{ij}\) for every existing edge and symmetric positive mean edge traversal times \(t_{ij}\). Starting at vertex \(i\), the walker chooses an outgoing edge \(ij\) with probability \(g_{ij}/\sum_k g_{ik}\), spends an independent nonnegative traversal time with finite mean \(t_{ij}\), and arrives at \(j\); only means matter for this theorem. For each ordered pair of distinct vertices, the first-passage time is until the first arrival at its target. The mean \(M\) averages the expectations equally over all \(N(N-1)\) ordered source-target pairs. The new channel joins any distinct vertices \(u,v\); it can parallel an existing edge, has independent positive mean transit time \(t\) and nonnegative adjustable conductance \(w\), and leaves all original parameters unchanged. If parallel physical channels are present, transition probabilities are proportional to channel conductances, including both channels. No fixed total-conductance-budget constraint is imposed.

## Proof

**1. A general mean-passage identity.** Let \(\tau_i=\sum_j g_{ij}t_{ij}\) and \(T_0=\sum_i\tau_i\). For a target \(j\), first-step conditioning gives \(\sum_k L_{ik}h_i^{(j)}=\tau_i\) at every \(i\ne j\), with \(h_j^{(j)}=0\), where \(h_i^{(j)}\) denotes the mean hitting time from \(i\). Equivalently, \(Lh^{(j)}=\tau-T_0 e_j\) on all vertices, because the rows of \(L\) sum to zero. Since \(G\mathbf1=0\) and \(LG=I-\mathbf1\mathbf1^\top/N\), the unique target-zero solution is
\[
h_i^{(j)}=\sum_k(G_{ik}-G_{jk})\tau_k+T_0(G_{jj}-G_{ij}).
\]
Sum over all ordered pairs with \(i\ne j\). The first sum cancels by \(\sum_iG_{ik}=0\). For the second, \(\sum_{j}\sum_{i\ne j}(G_{jj}-G_{ij})=N\operatorname{tr}G\). Therefore
\[
M(0)=\frac{T_0\operatorname{tr}G}{N-1}.
\]
This identity is already present in the motivating literature; it is reconstructed here to establish the precise normalization independently.

**2. Exact conductance perturbation.** The added channel changes the Laplacian to \(L_w=L+wbb^\top\) and the total traversal loading to \(T_w=T_0+2wt\). On \(\mathbf1^\perp\), the positive matrix \(L\) is invertible. The Sherman–Morrison identity, extended by zero on \(\operatorname{span}\{\mathbf1\}\), gives
\[
G_w=G-\frac{w}{1+wR}Gbb^\top G,
\qquad \operatorname{tr}G_w=A-\frac{wQ}{1+wR}=\frac{A+Bw}{1+wR}.
\]
Substitution in the mean-passage identity proves the formula for \(M(w)\), including \(w=0\).

**3. Strict positivity of the coefficients.** The connectedness condition makes \(G\) positive definite on the \((N-1)\)-dimensional subspace \(\mathbf1^\perp\). Thus \(A,R,Q>0\). Since \(N\ge3\), this space has dimension at least two, so \(\lambda_{\max}(G)<\operatorname{tr}G=A\). As \(G^2\preceq\lambda_{\max}(G)G\), we have \(Q\le\lambda_{\max}(G)R<AR\), proving \(B>0\). No regularity, vertex transitivity, or equal-weight hypothesis is used.

**4. Exact sign and optimizer classification.** Direct subtraction and differentiation yield
\[
M(w)-M(0)=\frac{w(2tA-T_0Q+2tBw)}{(N-1)(1+Rw)},
\]
\[
(N-1)(1+Rw)^2M'(w)=2tA-T_0Q+4tBw+2tRBw^2.
\]
The right-hand derivative numerator is strictly increasing for \(w\ge0\). If \(t\ge t_*\), it is positive for all \(w>0\), including equality at \(w=0\) in the threshold case; the baseline difference is strictly positive for \(w>0\). If \(t<t_*\), the derivative numerator has precisely one positive zero, obtained by solving \((1+Rw)^2=1+R(T_0Q-2tA)/(2tB)\), hence the displayed \(w_*\). It changes from negative to positive there, and \(M(w)\) grows linearly as \(w\to\infty\) since \(B,t,R>0\), so this zero is the unique global minimum. The exact difference formula has precisely one positive nonzero root \(w_{\rm return}\), and changes sign from negative to positive across it. Therefore \(0<w_*<w_{\rm return}\) and all claims follow.

**5. Sharp four-cycle example.** On the four-cycle with old unit conductances and unit mean transit times, choose opposite vertices for the new link. Exact graph calculations yield
\[
A=\frac54,\quad R=1,\quad Q=\frac12,\quad B=\frac34,\quad T_0=8,
\quad t_*=\frac85.
\]
If the new diagonal has geometric length \(\sqrt2\) and mean traversal time \(t=2^\beta\), as in an anomalous spatial-diffusion flight-time model, beneficial conductances exist exactly for \(\beta<\log_2(8/5)\). With \(\beta=1/2\), the optimum and crossover are, respectively,
\[
w_*=\sqrt{\frac{4\sqrt2-2}{3}}-1,\qquad
w_{\rm return}=\frac{4\sqrt2-5}{3}.
\]
This small graph illustrates the exact universal classification; the theorem itself is for every finite connected weighted topology.

## Verification

The accompanying executable \(\texttt{graph\_checker.py}\) uses exact rational and symbolic arithmetic. It constructs the positive graph Laplacian, pseudoinverse and expected loading independently, then computes each target-hitting-time vector by inverting the grounded Laplacian, without using the claimed global formula. It checks the predicted formula, derivative and sign identities, and optimality equations on five distinct connected graphs with nonuniform edge weights and traversal means. The checker passed 700 exact assertions, including 80 direct finite-weight hitting-time comparisons. These finite diagnostics are corroborations; the proof above establishes the theorem for every graph meeting the hypotheses.

## Relationship to prior work

Gounaris and Katifori, *A Braess' paradox analog in physical networks of optimal exploration* (arXiv:2303.02146, first posted 2023-03-03), supply the general all-target mean-time identity and exhibit paradoxical shortcut effects on structured networks, including numerical/global multi-edge conductivity optimization. This theorem does **not** claim discovery of that model, the mean-time identity, or the existence of Braess effects. It supplies an explicit universal **single-channel** phase classification at fixed original weights, with sharp time threshold, unique finite optimum, and one-crossing obstruction.

Predari, Berner, Kooij, and Meyerhenke, *Greedy optimization of resistance-based graph robustness with global and local edge insertions* (arXiv:2309.08271, first posted 2023-09-15), give the classical rank-one pseudoinverse trace update for pure graph resistance. That exact update is used as an established tool here, not as a new result. Unlike their resistance-only objective, a transport channel here also increases total time loading; its competition with decreasing resistance produces the strict one-crossing and finite-optimum laws.

## Limitations

The results concern means, not higher passage-time moments or pathwise distributions, and finite networks with symmetric channel conductances, not directed, nonreversible or infinite networks. All original conductances and transit means are held fixed as the one channel is strengthened; results are not asserted under global budget redistribution or when the channel traversal mean changes with its conductance. The theorem is a direct but physically meaningful optimization synthesis of known general spectral identities; it does not establish publication priority against every possible unindexed specialization. At \(N=2\), the strict positivity of \(B\) fails, so the claimed two-regime structure is deliberately restricted to \(N\ge3\). Independent external validation has not been performed.

## References

- G. Gounaris and E. Katifori, *A Braess' paradox analog in physical networks of optimal exploration*, arXiv:2303.02146v1 (2023-03-03), https://arxiv.org/pdf/2303.02146. Later journal article: *Physical Review Letters* 133, 067401 (2024).
- M. Predari, L. Berner, R. Kooij, and H. Meyerhenke, *Greedy optimization of resistance-based graph robustness with global and local edge insertions*, arXiv:2309.08271v1 (2023-09-15), https://arxiv.org/pdf/2309.08271.
- J. Sherman and W. J. Morrison, *Adjustment of an inverse matrix corresponding to a change in one element of a given matrix*, *Annals of Mathematical Statistics* 21 (1950), 124–127.
