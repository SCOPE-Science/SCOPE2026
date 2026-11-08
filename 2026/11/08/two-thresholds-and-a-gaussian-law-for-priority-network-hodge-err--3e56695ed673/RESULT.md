# Two thresholds and a Gaussian law for priority-network Hodge error

## Finding

Let \(G_n\sim G(n,p_n)\) be an undirected simple Erdős–Rényi conflict graph. For the linear rank-payoff priority-coordination game on \(G_n\) with any integer number \(K_n\ge2\) of priority levels and any deterministic edgewise tie-breaking orientations, let \(R_n\) be the fraction of squared unilateral-incentive energy not representable by a potential game. Define \(R_n=0\) when the graph has no edges. For any sequence \(p_n\in[0,1]\), the following statements hold:

1. If \(n^2p_n\to t\in[0,\infty)\), then
   \[
   R_n\ \Longrightarrow\ \tfrac12 B_t,
   \qquad\mathbb P(B_t=1)=1-e^{-t/2}.
   \]
2. If \(n^2p_n\to\infty\) and \(np_n\to0\), then \(R_n\to1/2\) in probability.
3. If \(np_n\to\lambda\in(0,\infty)\), then \(R_n\to1/(\lambda+2)\) in probability and in \(L^1\). At the exact sparse scale \(p_n=\lambda/n\),
   \[
   \sqrt n\left(R_n-\frac1{\lambda+2}\right)
   \ \Longrightarrow\
   N\!\left(0,\frac{2(1+\lambda)}{(\lambda+2)^4}\right).
   \]
4. If \(np_n\to\infty\), then \((np_n)R_n\to1\) in probability.

The two distinct thresholds are the appearance of the first conflict at density of order \(n^{-2}\), and the onset of appreciable conflicts sharing an agent at density of order \(n^{-1}\). On each nonempty graph, the answer is independent of the number of priority levels and the tie-breaking orientations. The Gaussian variance is strictly positive for every \(\lambda>0\).

## Assumptions and scope

The vertex set is \(\{1,\dots,n\}\), edges are independent with common probability \(p_n\), and a conflict contributes one unit of linear rank cost to whichever endpoint is served later. Agents select priority levels in \(\{0,\dots,K_n-1\}\); higher levels are served first, and tied endpoints are ordered deterministically. As in Lin–Lan–Nguyen–Kawahara (2026), every unilateral change has equal weight in the discrete game-flow inner product. The potential part is the orthogonal projection onto gradients of common potentials; the residual is the harmonic part. No assertion is made here for nonlinear payoff functions, heterogeneous graph edges, weighted move distributions, or conditional errors at a particular state.

For degrees \(d_1,\dots,d_n\), define the integer graph statistics
\[
X_n=\sum_i d_i=2|E(G_n)|,\qquad
Y_n=\sum_i d_i(d_i-1)=2\sum_i\binom{d_i}{2}.
\]
The exact finite-graph energy identity of Lin et al., Proposition 2, is
\[
\mathcal E_{\rm harm}=c_{K_n}X_n,\qquad
\mathcal E_{\rm pot}=c_{K_n}(X_n+Y_n),\qquad
c_K=\frac{K^{n-1}(K^2-1)}{12}.
\]
Consequently, for every nonempty graph,
\[
R_n=\frac{X_n}{2X_n+Y_n}.
\]
The new assertions concern the random-network laws of this ratio, not the original deterministic energy formula. The empty graph is given the stated zero convention because otherwise its total incentive energy is zero and the ratio is undefined.

## Proof

**Exact joint moments.** Write \(M_n=|E(G_n)|\) and \(H_n=n\binom{n-1}{2}\) for the number of unordered edge pairs sharing a vertex. Thus \(X_n=2M_n\) and \(Y_n=2W_n\), where \(W_n\) is the number of such present pairs. Set \(N_n=\binom n2\), \(q_n=2(n-2)\); every possible edge belongs to \(q_n\) possible wedges. Elementary covariance counting over independent edge indicators gives the following **exact** formulas for every integer \(n\ge2\) and \(p=p_n\):
\[
\begin{aligned}
\mathbb EX_n&=2N_np,& \mathbb EY_n&=2H_np^2,\\
\operatorname{Var}(X_n)&=4N_np(1-p),&
\operatorname{Cov}(X_n,Y_n)&=8H_np^2(1-p),\\
\operatorname{Var}(Y_n)&=4\left[H_n(p^2-p^4)+N_nq_n(q_n-1)(p^3-p^4)\right].
\end{aligned}
\]
For the final variance, pairs of wedges with no common graph edge are independent; diagonal pairs contribute \(H_n(p^2-p^4)\), and ordered distinct pairs sharing one edge contribute \(N_nq_n(q_n-1)(p^3-p^4)\). The covariance formula follows by counting each of the two constituent edges of each wedge. In particular,
\[
\frac{\mathbb EY_n}{\mathbb EX_n}=(n-2)p
\]
whenever \(p>0\).

**First-conflict regime.** If \(n^2p_n\to t<\infty\), then \(M_n\sim\operatorname{Bin}(N_n,p_n)\) converges in distribution to \(\operatorname{Pois}(t/2)\); if \(t=0\), this is the constant zero. Since \(\mathbb EW_n=H_np_n^2=O(n^{-1})\), the graph is a matching with probability tending to one. On a nonempty matching, \(Y_n=0\) and \(R_n=1/2\). On an empty graph, \(R_n=0\). This yields the first claim.

**Many disjoint conflicts.** If \(n^2p_n\to\infty\), binomial concentration gives \(X_n/(\mathbb EX_n)\to1\) in probability. If also \(np_n\to0\), then \(\mathbb EY_n/(\mathbb EX_n)\to0\). By Markov's inequality and concentration of \(X_n\), \(Y_n/X_n\to0\) in probability. Thus \(R_n\to1/2\).

**Positive mean-degree regime.** Suppose \(np_n\to\lambda>0\). The displayed moments give \(X_n/n\to\lambda\) and \(Y_n/n\to\lambda^2\) in \(L^2\): both expectations have those limits and both variances are \(O(n)\). The continuous mapping theorem then gives the limit \(1/(2+\lambda)\). Because \(0\le R_n\le1/2\), boundedness also gives convergence in \(L^1\).

To obtain the sharp Gaussian law for \(p_n=\lambda/n\), the moment formulas yield the covariance limit
\[
\frac1n\operatorname{Cov}\binom{X_n}{Y_n}\longrightarrow
\Sigma_\lambda=
\begin{pmatrix}
2\lambda&4\lambda^2\\
4\lambda^2&2\lambda^2+8\lambda^3
\end{pmatrix}.
\]
Here is a self-contained joint central-limit argument, including the dependence between wedges. Express \(X_n\) as a sum of single-edge indicator monomials and \(Y_n\) as a sum of ordered two-edge wedge monomials. In any mixed joint cumulant of fixed order \(r\ge3\), a summand vanishes unless the selected edge and wedge monomials form a connected *dependency* family, meaning their sets of primitive edge indicators overlap through a chain. The union graph of such a family is connected. If it has \(e\) distinct primitive edges and \(v\) vertices, then \(v\le e+1\). For a fixed \(r\), finitely many patterns exist, each admitting \(O(n^v)\) labeled embeddings. The moment–cumulant formula bounds the cumulant of a pattern by \(O(p_n^e)\): every term is a product of expectations of indicator monomials, with total exponent at least the number of distinct primitive edges. Hence each connected pattern contributes \(O(n^{v-e})=O(n)\). Consequently every fixed mixed cumulant of order \(r\ge3\) of \((X_n,Y_n)\) is \(O(n)\). After division by \(n^{r/2}\) it tends to zero, while the centered second cumulants converge to \(\Sigma_\lambda\). The moment–cumulant identities and moment determinacy of a normal law yield the joint convergence
\[
\frac1{\sqrt n}\left(\binom{X_n}{Y_n}-\mathbb E\binom{X_n}{Y_n}\right)
\Longrightarrow N_2(0,\Sigma_\lambda).
\]
The moment means differ from \(n(\lambda,\lambda^2)\) by \(O(1)\). Apply the delta method to \(g(x,y)=x/(2x+y)\) at \((\lambda,\lambda^2)\). Its gradient there is
\[
\nabla g(\lambda,\lambda^2)=\frac1{(\lambda+2)^2}(1,-1/\lambda).
\]
Direct matrix multiplication gives
\[
\nabla g^\top\Sigma_\lambda\nabla g
=\frac{2(1+\lambda)}{(\lambda+2)^4},
\]
which proves the Gaussian statement. Because \(\lambda>0\), the zero-edge event has negligible probability at this scale.

**Dense mean-degree regime.** Finally suppose \(np_n\to\infty\). The exact variances above show \(X_n/\mathbb EX_n\to1\) and \(Y_n/\mathbb EY_n\to1\) in probability. Indeed, \(\operatorname{Var}(X_n)/(\mathbb EX_n)^2=O((n^2p_n)^{-1})\), whereas
\[
\frac{\operatorname{Var}(Y_n)}{(\mathbb EY_n)^2}
=O\!\left(\frac1{n^3p_n^2}+\frac1{n^2p_n}\right)\longrightarrow0.
\]
Thus \(Y_n/X_n=(n-2)p_n(1+o_{\mathbb P}(1))\), and the identity \(R_n=(2+Y_n/X_n)^{-1}\) yields \((np_n)R_n\to1\). This completes all cases.

## Verification

The accompanying standalone `verify.py` recomputes all five moment identities by rational exhaustive enumeration of graph edge sets for orders \(2\) through \(5\), checks the finite-game Hodge identity separately by solving the profile-gradient least-squares problem for every graph through order \(4\) with two priority levels, and performs seeded Monte Carlo checks of the Gaussian variance coefficient. It reports 40 exact moment equalities, 74 direct Hodge projection graph cases, and two scale-variance diagnostics, ending with `PASS`. Numerical checks only support finite identities and the plausibility of asymptotics; the infinite statements are proved above.

## Relationship to prior work

Lin, Lan, Nguyen and Kawahara (2026), Proposition 2 and Remark 1, derive the deterministic graphwise Hodge energy ratio and its invariance under the number of priority levels and deterministic tie-breaking. Those identities are an explicitly credited premise, not claimed here as new. Ruciński (1988) establishes classical normal-limit conditions for fixed-subgraph counts in independent-edge random graphs, and Sturm–Wemheuer (2024) develop broader normal approximation tools for locally defined sparse-graph functionals. Neither inspected statement supplies the combined two-threshold random *priority-game* error law, its precise Bernoulli window, or the explicit joint-wedge covariance and ratio variance \(2(1+\lambda)/(\lambda+2)^4\). The new contribution is the stochastic network classification and sharp finite-size fluctuation law. Related historical results on complete-graph priority-payoff extremality concern nonlinear payoff design rather than this random graph limit.

## Limitations

This is a mathematical conclusion for the precisely normalized, equally weighted Hodge squared-error criterion, not an experimental estimate of realized driving delays, safety or welfare. The original finite-graph result is essential to the reduction. The Gaussian conclusion assumes exact \(p_n=\lambda/n\); for arbitrary sequences with \(np_n\to\lambda\), the deterministic centering at \(1/(\lambda+2)\) need not be accurate at the \(n^{-1/2}\) scale. A zero graph has no canonical relative error, so its value is a declared convention. The claims have not undergone independent scientific validation. Relevant unindexed or inaccessible literature may contain equivalent probabilistic consequences.

## References

- Z. Lin, J. Lan, A.-T. Nguyen, and Y. Kawahara, *Priority Coordination Games: Hodge Decomposition and a Sharp Design Limit*, arXiv:2610.05832v1, first posted October 5, 2026. https://arxiv.org/html/2610.05832v1 . Proposition 2, Remark 1 and Corollary 1.
- A. Ruciński, *When Are Small Subgraphs of a Random Graph Normally Distributed?*, Probability Theory and Related Fields **78** (1988), 1–10. https://www.math.uci.edu/~rvershyn/teaching/probability-PhD/rucinski-subgraph-count.pdf .
- M. Sturm and M. Wemheuer, *A Central Limit Theorem for Functions on Weighted Sparse Inhomogeneous Random Graphs*, arXiv:2404.12740 (2024). https://arxiv.org/abs/2404.12740 .
