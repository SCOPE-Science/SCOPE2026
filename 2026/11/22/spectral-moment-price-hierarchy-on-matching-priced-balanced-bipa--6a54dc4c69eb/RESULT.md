# Spectral-moment price hierarchy on matching-priced balanced bipartite networks

## Finding
Let \(m\ge3\) be an integer. On the complete bipartite network \(K_{m,m}\), mark the perfect matching \(\{\{u_i,v_i\}:1\le i\le m\}\). The marked edges cost \(c>0\) per unit conductance, all other edges cost one, and their combined budget is \(B>0\). Every edge conductance is independently adjustable and nonnegative; the resulting network must remain connected. Let \(L\) be its weighted combinatorial Laplacian and \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_{2m}\) its eigenvalues.

For a real spectral order \(p>0\), minimize
\[
J_p(L)=\sum_{j=2}^{2m}\lambda_j^{-p}.
\]
For \(p=0\), minimize \(J_0(L)=-\sum_{j=2}^{2m}\log\lambda_j\), equivalently maximize the weighted spanning-tree determinant. Put
\[
A_{m,p}=\frac{1}{2^p(m-1)^{p+1}},\qquad
D_{m,p}=\frac{1}{m^p},\qquad
C_{m,p}=\frac{1}{(m-2)^p},\qquad
T_m=\frac{2(m-1)}{m-2},
\]
with the usual convention that positive bases to power zero equal one. Define
\[
\boxed{\quad c_{m,p}=\frac{A_{m,p}+T_m C_{m,p}}{A_{m,p}+D_{m,p}+C_{m,p}}.\quad}
\]
**Theorem.** For every \(m\ge3\), \(B>0\), \(c>0\), and real \(p\ge0\), there is exactly one global optimum among all individual edge-weight allocations. It assigns one common conductance \(a_{m,p}\) to marked edges and another common strictly positive conductance \(b_{m,p}\) to unmarked edges. The optimum deletes every marked edge exactly when \(c\ge c_{m,p}\); otherwise both conductances are positive and their ratio is the unique positive stationary solution of the explicit one-variable objective in the proof.

At each fixed \(m\ge3\), \(c_{m,p}\) is *strictly increasing* in \(p\ge0\), with
\[
\boxed{\quad c_{m,0}=\frac{m(2m-3)}{(m-2)(2m-1)},\qquad
\lim_{p\to\infty}c_{m,p}=T_m.\quad}
\]
Thus the entire continuum of inverse-moment objectives has strictly nested price-triggered matching support. In particular, for every \(m\ge3\), the determinant, first-order coherence and second-order coherence thresholds satisfy \(c_{m,0}<c_{m,1}<c_{m,2}<T_m\).

For each fixed real \(p\ge0\),
\[
\boxed{\quad c_{m,p}=1+\frac{p+1}{m}+O_p(m^{-2}).\quad}
\]
If \(p\) is fixed and \(c=1+\gamma/m\) for a fixed real \(\gamma\), then the optimal edge-conductance ratio has the sharp limit
\[
\boxed{\quad\lim_{m\to\infty}\frac{a_{m,p}}{b_{m,p}}=\max\!\left\{0,1-\frac{\gamma}{p+1}\right\}.\quad}
\]
For *varying* orders \(p_m\ge0\) such that \(p_m/m\to\alpha\in[0,\infty]\), the threshold instead has the logistic crossover
\[
\boxed{\quad\lim_{m\to\infty}c_{m,p_m}=\frac{2}{1+e^{-2\alpha}}\quad}
\]
(the value at \(\alpha=\infty\) is two). Hence the large-network and high-spectral-order limits do not commute:
\[
\lim_{p\to\infty}\lim_{m\to\infty}c_{m,p}=1,
\qquad
\lim_{m\to\infty}\lim_{p\to\infty}c_{m,p}=2.
\]
The normalizations here use **unnormalized** Laplacian eigenvalues and total *priced conductance* \(B\), not a stochastic transition matrix. Multiplying \(J_p\) by a constant independent of the conductances does not change the optimizer.

## Assumptions and scope
The graph is \(K_{m,m}\) for an integer \(m\ge3\), with precisely one designated perfect matching. The cost ratio \(c\), budget \(B\), and order \(p\) are arbitrary within the domains above. Edges can be removed by assigning zero conductance as long as connectivity remains; this convention is essential because the pseudoinverse formula alone, without a connectivity constraint, would give misleading values at disconnected networks. For all orders, no constraint is imposed on the relative magnitudes of distinct original edge weights. At \(p=0\), the log determinant is over the \(2m-1\) positive eigenvalues only.

## Proof
**1. Strict global convexity and forced symmetry.** Let \(P\) be orthogonal projection onto \(\mathbf 1^\perp\). For any connected conductance assignment, the compressed Laplacian \(X=L|_{\mathbf 1^\perp}\) is positive definite. For real \(p>0\), the map \(X\mapsto\operatorname{tr}(X^{-p})\) is strictly convex on the positive-definite cone. Indeed, in an eigenbasis of \(X\), its Hessian along any nonzero symmetric perturbation \(H\) is
\[
\sum_{i,j}\frac{f'(\lambda_i)-f'(\lambda_j)}{\lambda_i-\lambda_j}\lvert H_{ij}\rvert^2>0,\qquad f(x)=x^{-p};
\]
where diagonal terms are interpreted as \(f''(\lambda_i)>0\), and off-diagonal terms are positive because \(f'\) is strictly increasing. The same argument applies to \(f(x)=-\log x\) for \(p=0\). The linear map from independent edge conductances to the weighted Laplacian is injective because each edge is an off-diagonal entry of \(L\). Thus the objective is strictly convex in all individual edge conductances whenever the weighted graph is connected.

The feasible cost simplex is compact; near disconnected boundary points at least one nonzero eigenvalue tends to zero, making \(J_p\) divergent for \(p>0\) and \(J_0\) divergent upward. There exists a positive-conductance feasible assignment, so a unique connected minimizer exists. Permutations of the \(m\) matched vertex pairs and the interchange of bipartition sides preserve the problem, and act transitively on marked edges and separately transitively on unmarked edges. By uniqueness, its conductances are constant on these two edge orbits. Write them \(a\ge0\) and \(b>0\), with
\[
mc a+m(m-1)b=B.
\]
The unmarked-edge subgraph is the connected crown graph for \(m\ge3\), so \(a=0\) is admissible.

**2. The three positive Laplacian spectral classes.** The cross-part adjacency block is \(Q=(a-b)I+b\mathbf1\mathbf1^\top\). Its singular/eigenvalue classes are \(d=a+(m-1)b\) on constants and \(a-b\) on zero-sum vectors. Consequently the full Laplacian \(\begin{pmatrix}dI&-Q\\-Q&dI\end{pmatrix}\) has nonzero eigenvalues
\[
2d\quad (\text{multiplicity }1),\qquad
mb\quad (\text{multiplicity }m-1),\qquad
2a+(m-2)b\quad (\text{multiplicity }m-1).
\]
The reduced objectives therefore are
\[
J_p(a,b)=[2(a+(m-1)b)]^{-p}+(m-1)(mb)^{-p}+(m-1)(2a+(m-2)b)^{-p}
\]
for \(p>0\), and the negative sum of corresponding multiplicity-weighted logarithms for \(p=0\).

**3. Exact support frontier and characterization of the interior optimum.** Eliminate \(b=(B/m-ca)/(m-1)\), for \(0\le a<B/(mc)\). Differentiate along this budget line. For \(p>0\) the derivative is
\[
\frac{dJ_p}{da}=-p b^{-p-1}G_{m,p}(r,c),\qquad r=\frac ab,
\]
where
\[
G_{m,p}(r,c)=\frac{1-c}{2^p(r+m-1)^{p+1}}-\frac{c}{m^p}+\frac{2(m-1)-(m-2)c}{(2r+m-2)^{p+1}}.
\]
For \(p=0\), the same sign rule applies with \(dJ_0/da=-b^{-1}G_{m,0}(r,c)\). In particular, at \(a=0\),
\[
G_{m,p}(0,c)=(A_{m,p}+T_m C_{m,p})-c(A_{m,p}+D_{m,p}+C_{m,p}).
\]
Since the one-variable objective is strictly convex and tends to infinity as \(b\downarrow0\), its one-sided derivative at \(a=0\) completely determines the support: the minimum is \(a=0\) exactly for \(c\ge c_{m,p}\); for \(c<c_{m,p}\), the unique positive critical point satisfies \(G_{m,p}(r,c)=0\), with
\[
b=\frac{B}{m(m-1+cr)},\qquad a=rb.
\]
This supplies a unique, reproducibly computable exact one-variable characterization for every real order. No unsupported radical expression is asserted for general \(p\).

**4. Strict monotonicity across *all* orders.** Factor the threshold weights by setting \(U=A_{m,p}\), \(V=D_{m,p}\), \(W=C_{m,p}\), and \(T=T_m>2\). Then \(c_{m,p}=(U+TW)/(U+V+W)\). Write
\[
x=\frac1{2(m-1)},\qquad y=\frac1m,\qquad z=\frac1{m-2},
\]
so \(U=x^p/(m-1)\), \(V=y^p\), \(W=z^p\), with \(0<x<y<z\). Differentiation gives
\[
(U+V+W)^2\frac{dc_{m,p}}{dp}=
VW T\log(z/y)+UW(T-1)\log(z/x)-UV\log(y/x).
\]
The last negative term cannot overcome the first positive term: \(W/U=(m-1)(z/x)^p\ge m-1\) for \(p\ge0\), while
\[
(m-1)T\log(z/y)>\frac{4(m-1)^2}{m(m-2)}>4>\log(y/x).
\]
Here the first inequality follows from \(\log(m/(m-2))>2/m\), and \(\log(y/x)=\log(2(m-1)/m)<\log2<1\). Thus the derivative is strictly positive for every \(p\ge0\). Substituting \(p=0\) gives the displayed determinant threshold. Since \(W/V=(m/(m-2))^p\to\infty\) and \(W/U\to\infty\), its high-order limit is \(T_m\).

**5. Sharp large-network laws.** Dividing the exact threshold numerator and denominator by \(C_{m,p}\) yields the numerically stable identity
\[
c_{m,p}=\frac{T_m+\frac1{m-1}\left(\frac{m-2}{2(m-1)}\right)^p}{1+\left(\frac{m-2}{m}\right)^p+\frac1{m-1}\left(\frac{m-2}{2(m-1)}\right)^p}.
\]
For fixed real \(p\ge0\), expand both sides in powers of \(m^{-1}\) to obtain \(c_{m,p}=1+(p+1)/m+O_p(m^{-2})\). For \(p_m/m\to\alpha\), the second denominator term tends to \(e^{-2\alpha}\), the final term vanishes, and \(T_m\to2\); this proves the logistic formula, including \(\alpha=\infty\).

To obtain the critical-window conductance ratio, put \(c=1+\gamma/m\). At any fixed \(r\ge0\), direct expansion of the exact stationarity expression gives
\[
m^{p+1}G_{m,p}(r,1+\gamma/m)\longrightarrow 2\bigl[(p+1)(1-r)-\gamma\bigr]
\]
for every fixed real \(p\ge0\). The strictly convex budget-line objective has derivative of sign \(-G\), and the ratio \(r=a/b\) grows strictly with \(a\). For \(\gamma<p+1\), the derivative is negative at zero and becomes positive at any fixed \(r>1-\gamma/(p+1)\), so its unique zero converges to \(1-\gamma/(p+1)\). For \(\gamma>p+1\), the exact boundary threshold forces \(r=0\) for all large \(m\). At equality, the derivative at every fixed \(r>0\) is eventually positive and \(r\to0\). This proves the stated positive-part limit, including \(p=0\).

## Verification
The standalone script `verify.py` reconstructs the three spectral multiplicities, compares the formula with direct symmetric-matrix eigenvalues for small graphs, checks scalar optima and support boundaries at real orders, checks exact-rational thresholds at \(p=0,1,2\), and probes the critical-price and logistic crossover limits. Run from the extracted package directory using `python verify.py` with NumPy and SciPy installed. It printed `PASS 852 assertions` in the documented execution. The rigorous claims rely on the analytic proof above, not on the finite numerical tests.

## Relationship to prior work
Ghosh, Boyd and Saberi develop convex effective-resistance (first inverse spectral moment) network design; their full accessible paper explains symmetry reduction and specific graph examples, but does not give this continuum-of-orders matching-price hierarchy. Patterson and Bamieh identify first- and second-order noisy-consensus coherence as first and second inverse Laplacian moments and analyze fractal graph families, not conductance-price support transitions in the marked bipartite family. Closely related public mathematical records separately determine the determinant, first-inverse-moment and spectral-gap matching-price boundaries on \(K_{m,m}\); those individual endpoints are **not** claimed new here. The assertion that *every* finite real spectral order has the displayed threshold, that the threshold is *strictly increasing throughout the continuum*, and that its joint high-order/large-graph scaling is logistic is a distinct comparison requiring the proof above. Some relevant record text was only available as public summaries, so an unindexed stronger theorem remains a publication-priority risk.

## Limitations
The conclusion applies to a complete balanced bipartite graph with one designated perfect matching and equal prices within each of its two edge classes; it does not address arbitrary graph topology, unequal individual prices, directed networks, or normalized random-walk Laplacians. The relative conductance limit is for fixed \(p\); the logistic threshold permits varying \(p\), but no analogous varying-order conductance-ratio formula is claimed. The result does not assert a unique optimizer in the nonsmooth limiting spectral-gap problem, and no numerical experiment is treated as proof of the all-parameter statements. Priority is qualified by limited accessibility of some related public full texts. 

## References
1. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1 (first publicly posted 2013-10-09), https://arxiv.org/abs/1310.2592 ; especially Section II and equation (6) for the squared-inverse coherence metric.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf ; especially the convex design framework and symmetry examples.
3. *An A-versus-D support gap for a priced perfect matching in complete bipartite networks*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-a-versus-d-support-gap-for-a-priced-perfect-matching-in-compl--b65b2ff40797 (public summary available; full record not accessed).
4. *Exact spectral-gap price transition and all optimal allocations for matching-priced complete bipartite networks*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-spectral-gap-price-transition-and-all-optimal-allocations--efaad5dd81d4 (public summary available; full record not accessed).
