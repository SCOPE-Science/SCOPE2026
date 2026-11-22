# Fractional cut covers are the exact minimax law for two correlated sign trace probes

## Finding

Let \(G=(V,E)\) be any finite nonempty simple undirected graph, with vertices \(V=\{1,\ldots,n\}\). Let \(\mathcal A_G\) contain all real symmetric matrices \(A\) whose off-diagonal entries vanish outside \(E\) and satisfy
\[
\sum_{\{i,j\}\in E} A_{ij}^{2}=1.
\]
There is no restriction on their diagonal. Choose a joint law of \(Z,W\in\{-1,1\}^{n}\) **before** the entries of \(A\) are known, requiring each marginal separately to be uniform on the full sign cube; dependence between the two vectors is otherwise unrestricted. The two-matrix-product estimator is
\[
\widehat T_A=\tfrac12\bigl(Z^{\mathsf T}AZ+W^{\mathsf T}AW\bigr).
\]

For a cut \(S\subseteq V\), let \(\delta(S)\subseteq E\) be the edges with exactly one endpoint in \(S\). Define the established *fractional cut-covering number*
\[
\operatorname{fcc}(G)=\min\left\{\sum_{S\subseteq V} y_S:\ y_S\ge0,\quad
\sum_{S:\,e\in\delta(S)}y_S\ge1\ \text{for every }e\in E\right\}.
\]
The **exact graph-uniform, all-couplings minimax variance** is
\[
\boxed{\inf_{\mathcal L(Z,W)}\ \sup_{A\in\mathcal A_G}
 \operatorname{Var}(\widehat T_A)=4\left(1-\frac1{\operatorname{fcc}(G)}\right).}
\]
The infimum is attained by a simple, matrix-independent construction: independently draw \(Z\) as a uniform sign vector and a random cut whose law maximizes the smallest edge-cut probability; define \(W_i=Z_i\) on one side and \(W_i=-Z_i\) on the other.

In particular, **zero minimax variance occurs exactly for bipartite graphs**. On every nonbipartite graph, each *deterministic* coordinatewise sign-flip coupling has worst-case variance \(4\), whereas the optimal randomized-cut coupling has worst-case variance at most \(2\). Thus randomizing the cut improves the sharp robust variance by at least a factor of two whenever the graph is nonbipartite.

For an edge-transitive graph, the value simplifies to
\[
\boxed{\operatorname{Var}_{\min\max}(G)=4\left(1-\frac{\operatorname{MaxCut}(G)}{|E|}\right).}
\]
Hence for every odd cycle \(C_{2k+1}\), \(k\ge1\), it is exactly \(4/(2k+1)\). For the complete graph on \(n\ge2\) vertices it equals
\[
\boxed{\operatorname{Var}_{\min\max}(K_n)=
\begin{cases}
\dfrac{2(n-2)}{n-1},&n\ \text{even},\\[2pt]
\dfrac{2(n-1)}{n},&n\ \text{odd}.
\end{cases}}
\]
The fractional rather than ordinary maximum-cut formulation is essential for arbitrary graphs. On a triangle with one pendant edge, the minimax variance is \(4/3\), although \(4(1-\operatorname{MaxCut}(G)/|E|)=1\).

## Assumptions and scope

All graphs are finite, simple, undirected and have at least one edge; isolated vertices are allowed. The matrix class normalizes the **unordered** off-diagonal edge coefficients, not the full Frobenius norm (which counts them twice). Every probe is individually a vector of mutually independent fair signs; only dependence *between* the two probes is optimized. The method consumes two full-dimensional quadratic-form or matrix-vector-product queries, with equal weights \(1/2\). The probe law depends on the known graph \(G\), not on unknown numerical entries of \(A\). The objective is worst-case *variance*, not worst-case realized error, tail risk, or runtime. Adding a sufficiently large multiple of the identity to any admissible off-diagonal matrix makes it positive definite without changing the variance, so the same minimax value holds when the matrix adversary is further required to use positive-definite matrices with unrestricted diagonal.

## Proof

**1. Expansion and an all-couplings lower bound.** For any admissible joint law, let \(D_i=Z_iW_i\in\{-1,1\}\). This is a random vertex signing and hence defines a random cut; \(D\) may depend arbitrarily on \(Z\). For each edge \(e=\{i,j\}\) define \(H_e=(Z_iZ_j+W_iW_j)/2\). The two marginal uniformity assumptions imply \(\mathbb E H_e=0\), while
\[
H_e^2=\tfrac12(1+D_iD_j)=\mathbf1_{\{D_i=D_j\}}.
\]
For the symmetric matrix with its only nonzero off-diagonal edge coefficient equal to one at \(e\), the estimator error is \(2H_e\). Its variance is therefore \(4\Pr(D_i=D_j)\). Because each such matrix belongs to \(\mathcal A_G\), *every* permissible coupling satisfies
\[
\sup_{A\in\mathcal A_G}\operatorname{Var}(\widehat T_A)
\ge4\max_{e=\{i,j\}\in E}\Pr(D_i=D_j).
\]
Taking the infimum over all couplings cannot improve on the minimum over all probability distributions of cuts:
\[
\rho_G\ge4\theta_G,
\qquad\theta_G:=\min_{\pi}\max_{e\in E}\Pr_{D\sim\pi}(D_i=D_j).
\]
This uses no assumption of coordinatewise or linear coupling between the two probes.

**2. An exactly matching law.** Let \(\pi\) minimize the finite-dimensional cut problem defining \(\theta_G\). Draw \(D\sim\pi\) and, independently, a uniform vector \(Z\) of fair independent signs. Put \(W_i=D_iZ_i\). Conditional on any \(D\), \(W\) is uniform on the full cube, so both required marginals are uniform. For each edge,
\[
H_e=Z_iZ_j\,\mathbf1_{\{D_i=D_j\}}.
\]
For distinct edges \(e\ne f\), \(\mathbb E_Z[(Z_iZ_j)(Z_kZ_l)]=0\), even if the edges share one vertex. Thus the covariance matrix of the vector \((H_e)_{e\in E}\) is *diagonal* with diagonal entries \(p_e=\Pr_\pi(D_i=D_j)\). Since
\[
\widehat T_A-\operatorname{tr}(A)=2\sum_{e\in E}A_eH_e,
\]
we have the exact variance identity
\[
\operatorname{Var}(\widehat T_A)=4\sum_{e\in E} A_e^2p_e.
\]
Maximizing over the normalized edge coefficients gives \(4\max_e p_e=4\theta_G\), matching the lower bound. A worst-case matrix is obtained by concentrating its unit edge-energy on an edge with maximal \(p_e\).

**3. Identification with the established fractional cut-covering parameter.** Set
\[
\alpha_G=\max_{\pi}\min_{e\in E}\Pr_{D\sim\pi}(D_i\ne D_j).
\]
Because the complement of a crossing edge is an uncut edge, \(\theta_G=1-\alpha_G\). For any cut distribution with minimum crossing probability \(\alpha>0\), assigning cover weights \(y_S=\pi(S)/\alpha\) is feasible with total weight \(1/\alpha\), so \(\operatorname{fcc}(G)\le1/\alpha_G\). Conversely, any feasible fractional cover \(y\) of total mass \(L\) gives a cut distribution \(\pi(S)=y_S/L\) whose every edge has crossing probability at least \(1/L\). Therefore \(\alpha_G\ge1/\operatorname{fcc}(G)\). The two inequalities establish \(\alpha_G=1/\operatorname{fcc}(G)\), and hence the main formula. Finite cut sets ensure that the minimizers and maximizing distributions exist. Equivalently, finite-game minimax gives the already standard graph-theoretic dual
\[
\theta_G=1-\min_{q\in\Delta(E)}\max_{S\subseteq V}\sum_{e\in\delta(S)}q_e.
\]
No novelty is attributed to the fractional cut-cover invariant or this LP duality.

**4. Bipartiteness and deterministic sign flips.** The value \(\theta_G=0\) if and only if some cut distribution crosses every edge with probability one. Since there are finitely many edges, that requires one cut crossing every edge, which is equivalent to bipartiteness. For any deterministic signing \(D\), the construction in Step 2 has variance \(4\) times the largest indicator of an uncut edge, hence either zero if \(D\) crosses every edge or exactly \(4\) otherwise. A nonbipartite graph leaves at least one edge uncut under every signing, while taking an independent uniform signing gives every edge uncut probability \(1/2\) and hence \(\theta_G\le1/2\). Therefore its best deterministic sign-flip robust variance is \(4\) and its optimal randomized robust variance is at most \(2\).

**5. Edge transitivity and exact examples.** Every cut has at most \(\operatorname{MaxCut}(G)\) edges, so averaging the number of uncut edges under any distribution shows \(\theta_G\ge1-\operatorname{MaxCut}(G)/|E|\). If graph automorphisms act transitively on edges, apply a uniformly random automorphism to one maximum cut. All edges then have the same probability of being uncut and the average bound is attained. The maximum cut of an odd cycle of size \(2k+1\) has \(2k\) edges. The maximum cut of \(K_n\) has \(\lfloor n^2/4\rfloor\) edges. Substituting these counts and simplifying gives the asserted formulas for odd cycles and both parities of complete graphs. For a triangle with a pendant edge, some triangle edge must remain uncut under every cut, so \(\theta_G\ge1/3\). Randomizing equally over the three cuts that leave, respectively, one triangle edge uncut while always cutting the pendant edge gives \(\theta_G\le1/3\); thus its exact value is \(4/3\). Its ordinary maximum cut has three of its four edges, explaining why the uniform-edge average formula incorrectly predicts \(1\) outside edge-transitive families.

## Verification

Run `python verify.py` in this directory after installing the packages in `requirements.txt`. The verifier independently constructs the primal cut-distribution and dual edge-weight linear programs, checks their numerical agreement on graph families and nontransitive examples, enumerates exact-rational sign-product covariances for explicit optimal-cut ensembles, tests random non-linear fully-uniform probe couplings against the lower bound, and checks the complete-graph parity formulas with exact fractions. Its completed invocation reports `PASS 594 finite LP, covariance, and exact combinatorial assertions`. Numerical LP duality and randomly sampled couplings are finite corroboration only; the all-graphs optimality and the all-couplings lower bound are proved analytically above.

## Relationship to prior work

Frommer, Rinelli and Schweitzer [1] establish the Rademacher variance of *independent color-restricted* stochastic-probing vectors in their Section 3 and address colorings and optimal allocation after a partition is chosen. That identity is the background for variance minimization, but their estimator differs from two *fully uniform* correlated probes and does not establish a minimax over all couplings before the edge coefficients are known. Neto and Ben-Ameur [2], and Proença, de Carli Silva, Sato and Tunçel [3], study the **already known fractional cut-covering graph parameter**, including its primal/dual properties; the graph-theoretic LP and the closed forms implied by it are not claimed as new. The contribution is the sharp equality between that pre-existing invariant and the unrestricted two-uniform-probe **minimax variance**, with a universally attaining coupling and a proof that nonlocal couplings cannot lower its worst-case risk.

Previously reported fixed-matrix coupling results [4,5] optimize the joint law with *numerical matrix entries held fixed*. Those quantifiers are not interchangeable with the present matrix-blind minimax problem: in particular, for the unscaled complete-graph adjacency matrix on four vertices the best matrix-specific nonlinear coupling has variance \(6\), whereas the graph-robust randomized-cut construction has variance \(8\) on that same matrix and guarantees \(4/3\) over all unit-edge-energy coefficient choices. A known shared-sign Hadamard-row construction [6] gives the same coefficient as the even-complete-graph formula at dyadic sizes; the coefficient in that subfamily is therefore **not** attributed new priority. The new statement is the all-graph, all-couplings sharp minimax identification and the nonbipartite necessity of randomizing an otherwise deterministic sign-flip robust design. A more direct older derivation of this minimax identity cannot be ruled out.

## Limitations

The optimization is strictly for a two-query, equally weighted average whose two *individual* marginals are completely uniform Rademacher vectors. Matrix-dependent probe distributions, arbitrary non-Rademacher marginals, deterministic graph-color-supported vectors, pilot/adaptive products, more than two queries and alternate unbiased estimators are excluded. The matrix adversary is restricted to a known sparsity graph with a fixed sum of squared unordered edge coefficients; other uncertainty sets have different optima. The fractional cut-cover LP may be expensive to solve on large graphs, so this is not a universal computational-speedup claim. Variance optimality does not imply dominance in individual trials or in all tail probabilities. Only finite numerical experiments supplement the proof; historical priority and mathematical review have not been independently validated.

## References

1. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, first public arXiv version 2023-08-15, https://arxiv.org/abs/2308.07722 (especially Sections 2.2 and 3.1–3.2).
2. J. Neto and W. Ben-Ameur, *On fractional cut covers*, Discrete Applied Mathematics **265** (2019), 168–181, https://doi.org/10.1016/j.dam.2019.03.020. The publisher metadata and abstract were examined; its full text was not available for this comparison.
3. N. B. Proença, M. K. de Carli Silva, C. M. Sato and L. Tunçel, *A primal-dual extension of the Goemans–Williamson algorithm for the weighted fractional cut-covering problem*, https://arxiv.org/abs/2311.15346 (original arXiv preprint 2023, updated later; introduction, definitions and duality discussion inspected).
4. *The four-vertex threshold for nonlinear two-probe trace coupling*, public mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-four-vertex-threshold-for-nonlinear-two-probe-trace-coupling--e737dedee370.
5. *A sharp nonlinear-coupling window for two-probe trace estimation on a weighted five-cycle*, public mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-nonlinear-coupling-window-for-two-probe-trace-estimation--627202544eed.
6. *Sharp worst-case variance inflation of unmodified Hadamard trace probes*, public mathematical note (the shared-random-sign Hadamard construction is identified there as earlier work), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-worst-case-variance-inflation-of-unmodified-hadamard-trace--a170715967ec.
