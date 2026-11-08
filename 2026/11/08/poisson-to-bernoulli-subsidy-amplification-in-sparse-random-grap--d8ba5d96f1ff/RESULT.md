# Poisson-to-Bernoulli subsidy amplification in sparse random graphical fair division

## Finding

A random graph can have an enormous number of agents with no goods but only a bounded random number of small tree components. One such tree component forces every isolated agent to receive a unit payment. Hence an isolated-edge Poisson event is amplified into a macroscopic random total subsidy.

**Theorem.** Fix \(c\in\mathbb R\). For all sufficiently large integers \(n\), draw a simple graph \(G_n\sim G(n,p_n)\), independently retaining each unordered edge with probability
\[
p_n=\frac{\log n+\log\log n+c}{2n}.
\]
Make each vertex an agent and each edge a good valued at one by both endpoints and zero by all other agents. Every good must be allocated to one of its endpoints. External, freely divisible money is valued at face value by every agent. Let \(S_n\) be the least nonnegative total payment compatible with **global envy-freeness** across all pairs of agents. Define
\[
a_n=e^{-c/2}\sqrt{\frac{n}{\log n}},\qquad \lambda=\frac{e^{-c}}4.
\]
Then the exact zero-subsidy probability and scaled subsidy distribution satisfy
\[
\Pr\{S_n=0\}\longrightarrow e^{-\lambda},\qquad
\frac{S_n}{a_n}\xrightarrow{\,d\,}\operatorname{Bernoulli}(1-e^{-\lambda}),
\qquad \frac{\mathbb E S_n}{a_n}\longrightarrow1-e^{-\lambda}.
\]
Thus the limiting scaled payment is exactly zero with probability \(e^{-\lambda}\) and exactly one otherwise. The underlying count of two-vertex tree components has a Poisson limit; no other nontrivial trees survive in this window.

## Assumptions and scope

For a finite simple undirected graph \(G=(V,E)\), an *orientation allocation* sends each good \(\{i,j\}\in E\) to exactly one of \(i,j\). Write \(A_j\) for the goods assigned to agent \(j\), and define binary additive values \(v_i(A)=\lvert\{e\in A:i\in e\}\rvert\). For subsidies \(s_i\ge0\), global envy-freeness means
\[
v_i(A_i)+s_i\ge v_i(A_j)+s_j \quad\text{for every }i,j\in V.
\]
The subsidies come from an external budget rather than transfers. Let \(S(G)\) be the minimum of \(\sum_i s_i\) over all allocations and real nonnegative subsidies. An isolated vertex remains an agent and values all goods at zero. Let \(I(G)\) be its count and \(T(G)\) be the number of connected components that are trees with at least two vertices. A connected component with a cycle is called cyclic; neither bipartiteness nor connectedness is assumed. The random theorem assumes one fixed \(c\), independent random edges, symmetric unit endpoint values and all agents participating in envy comparisons.

## Proof

**Step 1: an exact finite-graph subsidy identity.** For every finite simple graph,
\[
S(G)=\begin{cases}0,&T(G)=0,\\T(G)+I(G),&T(G)>0.\end{cases}
\]
For a lower bound, every orientation of a nontrivial tree component has a vertex \(u\) with no incoming edge: the sum of indegrees is one less than the component order. There is a neighboring vertex \(v\) receiving the edge \(\{u,v\}\), and the envy inequality for \(u\) against \(v\) forces \(s_u\ge1+s_v\ge1\). Distinct tree components supply distinct such vertices, yielding at least \(T(G)\) total payments. If a nontrivial tree exists, choose any of its indegree-zero vertices \(u\). Every isolated vertex \(w\) has empty allocation and values \(A_u\) at zero, so its envy inequality against \(u\) forces \(s_w\ge s_u\ge1\). This adds \(I(G)\) disjoint payments.

For an upper bound, in every cyclic connected component choose a simple cycle, orient it consistently around the cycle, and orient edges of a spanning forest away from the cycle; orient any remaining edges arbitrarily. Every vertex in such a component receives at least one edge. In each nontrivial tree choose a root and orient edges away from it: precisely the root receives no edges. If there are any nontrivial trees, give one unit of money to each such root and to every isolated vertex, and zero to every other agent. Otherwise give no money. Every agent's final own utility is at least one when at least one tree exists, and each other bundle has subjective value at most one because the graph is simple. More specifically, a *paid* agent's bundle is empty, so any other agent values it at zero and adds at most the unit payment; an *unpaid* agent's bundle has monetary payment zero and contains at most one good incident to any given different agent. Thus all pairwise envy inequalities hold. If there is no nontrivial tree, all non-isolated agents receive at least one good, each isolated agent receives and values no good, and no subsidies are necessary. Equality follows. The argument covers the edgeless graph and disconnected graphs and shows that an optimum exists with integral unit payments.

**Step 2: surviving tree components.** Put \(L_n=np_n\), let \(Z_n\) count isolated edges (connected components with exactly two vertices), and let \(N_{k,n}\) count tree components on exactly \(k\) vertices. For all \(2\le k\le n\), Cayley's tree count and independence give the exact expectation
\[
\mathbb E N_{k,n}
=\binom nk k^{k-2}p_n^{k-1}
 (1-p_n)^{k(n-k)+\binom k2-k+1}.
\]
In particular,
\[
\mathbb E Z_n=\binom n2 p_n(1-p_n)^{2(n-2)}\longrightarrow\lambda.
\]
For each fixed positive integer \(r\), the factorial moment of \(Z_n\) counts ordered collections of \(r\) vertex-disjoint isolated edges:
\[
\mathbb E(Z_n)_r=
\frac{(n)_{2r}}{2^r}p_n^r
(1-p_n)^{2r(n-2r)+\binom{2r}{2}-r}
\longrightarrow \lambda^r.
\]
Factorial-moment convergence yields \(Z_n\Rightarrow\operatorname{Pois}(\lambda)\).

We show that \(\sum_{k=3}^{n}N_{k,n}\to0\) in probability and in mean, not merely for fixed \(k\). For \(3\le k\le n/2\), use \(k!\ge(k/e)^k\), \(\binom nk\le n^k/k!\), and \(1-p\le e^{-p}\) to obtain
\[
\mathbb E N_{k,n}\le\frac1{p_n k^2}
 \left(e L_n e^{-p_n(n-k)}\right)^k.
\]
For \(3\le k\le n/4\), the parenthesis is \(O(n^{-3/8}(\log n)^{5/8})\), and the whole expectation sum is at most
\[
O\!\left(p_n^{-1}n^{-9/8}(\log n)^{15/8}\right)=o(1).
\]
For \(n/4<k\le n/2\), the parenthesis is \(O(n^{-1/4}(\log n)^{3/4})\), so the remaining geometric tail is also \(o(1)\). For \(k>n/2\), ignoring external absent edges and using \(\binom nk\le2^n\),
\[
\mathbb E N_{k,n}\le 2^n (np_n)^n
\exp\!\left[-\frac{p_n(k-1)(k-2)}{2}\right].
\]
Its sum over these \(k\) is \(o(1)\): the logarithm of the positive prefactor is \(O(n\log\log n)\), while the negative exponent is \(-\Omega(n\log n)\). Thus \(\mathbb E\sum_{k\ge3}N_{k,n}\to0\), giving \(T_n-Z_n\to0\) in \(L^1\), \(T_n\Rightarrow\operatorname{Pois}(\lambda)\), and \(\mathbb ET_n\to\lambda\).

**Step 3: concentration of isolated agents.** With \(I_n=I(G_n)\), independence gives
\[
\mathbb E I_n=n(1-p_n)^{n-1}\sim a_n,
\quad
\mathbb E(I_n)_2=n(n-1)(1-p_n)^{2n-3}.
\]
Since \(\mathbb E I_n\to\infty\) and \(p_n\to0\), these imply \(\operatorname{Var}(I_n)/(\mathbb E I_n)^2\to0\), and hence \(I_n/a_n\to1\) in \(L^2\).

**Step 4: the amplified limit.** The exact identity in Step 1 gives
\[
\frac{S_n}{a_n}=\left(\frac{I_n}{a_n}+\frac{T_n}{a_n}\right)
\mathbf1_{\{T_n>0\}}.
\]
The first fraction converges to one in \(L^2\); the second converges to zero in \(L^1\), because \(\mathbb ET_n\to\lambda\) and \(a_n\to\infty\). Meanwhile \(\Pr(T_n=0)\to e^{-\lambda}\) by the Poisson limit on the integer-valued support. The distributional limit follows by Slutsky's theorem and the expectation limit follows from the \(L^1\) bounds. Finally, \(S_n=0\) holds *exactly* when \(T_n=0\) for every finite graph, proving the zero-payment probability assertion.

## Verification

The standalone standard-library program `verify_graph_subsidy.py` enumerates all simple graphs on at most four vertices, all orientations of each graph, and all zero-one subsidy assignments in increasing total cost. It also tests six five-vertex archetypes, for 81 exact finite checks. These independently corroborate the finite-graph identity's constructive optimality in the specified finite cases. The program additionally checks direct numerical values of \(\mathbb E I_n/a_n\), \(\mathbb E Z_n\), and expected higher-order tree counts at two finite orders. Its expected output ends in `PASS`. None of the finite checks establishes the infinite Poisson or mean limit; those follow from the proof above.

## Relationship to prior work

Li, Sun, Suzuki and Xing (2025) study minimum subsidies for envy-free orientations, including a polynomial-time characterization for binary additive values. Their deterministic component argument is close background for Step 1, but does not state the random-graph window, its Poisson defect law, or a Bernoulli amplified subsidy limit. Li, Sun and Xing (2026) explicitly observe that an isolated good amid many isolated agents can force payment to every goodless agent; this illustrates the propagation mechanism and is not a new observation here. Wu (2026) studies asymptotic subsidies with *dense i.i.d. agent-good values* and no endpoint-only orientation restriction; its limiting compensation scales do not imply the sparse random-graph law above. Classical Erdős–Rényi component-count techniques motivate Step 2; isolated-edge Poisson convergence itself is not claimed as a new random-graph principle. The contribution is the exact combination of rare structural obstructions and the divergent population of zero-valuation agents into the limiting subsidy distribution, in a natural graph-orientation fair-division model.

## Limitations

The result requires symmetric unit values on a simple independent-edge graph, positive constant \(c\) not required, unrestricted external nonnegative monetary subsidies, global pairwise envy comparisons, and all isolated agents remaining eligible. It does not cover arbitrary binary or weighted edge valuations, multidigraphs, graph models without independent edges, budget-balanced transfers or approximate envy. The limiting distribution is under the particular double-logarithmic window, not a uniform bound for varying \(c\). Finite enumerations are not completeness certificates for other models, and publication priority against unindexed literature remains uncertain. No independent audit was performed.

## References

1. B. Li, A. Sun, M. Suzuki and S. Xing, *On the Subsidy of Envy-Free Orientations in Graphs* (2025), arXiv:2502.13671, https://arxiv.org/abs/2502.13671 . First public version: 19 February 2025.
2. B. Li, A. Sun and S. Xing, *Eliminating Envy in Multigraphs Through Subsidy*, IJCAI 2026, https://doi.org/10.24963/ijcai.2026/387 .
3. Z. Wu, *Asymptotic Subsidies for Envy-Free Allocation* (2026), arXiv:2610.10272, https://arxiv.org/abs/2610.10272 . First public version: 7 October 2026.
4. Classical Cayley tree enumeration, binomial random-graph component formulas and factorial-moment Poisson convergence are used as standard mathematical tools; complete details relevant to this theorem are given above.
