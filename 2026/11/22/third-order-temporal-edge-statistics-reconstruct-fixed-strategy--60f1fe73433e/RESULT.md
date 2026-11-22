# Third-order temporal edge statistics reconstruct fixed-strategy interaction networks

## Finding
For every finite simple undirected graph without isolated vertices, the stationary temporal statistics of products of at most three **distinct, individually labelled edge-environment variables** determine the complete edge-to-vertex incidence structure, up to renaming the unobserved vertices, in the unanimous-strategy restriction of the stochastic edge-feedback evolutionary game of Betz, Fu and Masuda [1]. Every conclusion holds at every nondegenerate update rate, not just in a weak-selection or large-population limit. Order two suffices for connected graphs except for the triangle/claw ambiguity; a three-edge temporal statistic resolves that exception with an explicit strictly positive gap. Order three is the smallest universal observation order for **edge-label-preserving** reconstruction: two seven-vertex graphs with the same six labelled edges have identical one-edge and two-edge trajectory distributions but distinct edge incidence structures.

## Assumptions and scope
Fix a simple undirected graph \(G=(V,E)\) with \(N=|V|\ge 2\), with no isolated vertices and at least one edge. The number \(N\), an individual identity for each observed edge, the step clock and the parameters below are known; the vertex names and edge endpoints are not observed. Consider the finite agent-based update rule of [1] after the players have reached unanimous cooperation or unanimous defection. The unanimity is absorbing for Fermi imitation, so strategies remain fixed. Each attempted update is a strategy-update (then an environmental holding step) with probability \(1-\omega\), or an environmental update with probability \(\omega\), where \(0<\omega<1\). On an environmental update, select one vertex uniformly and independently update all its incident edge states, conditional on the chosen vertex. Each selected edge switches \(0\to1\) with probability \(p\in(0,1)\), and \(1\to0\) with probability \(q\in(0,1)\). The choices of flips on different edges are conditionally independent. In the source's parameterization take \((p,q)=(p_0,q_0)\) for all cooperators or \((p_2,q_2)\) for all defectors; the remaining source parameters do not influence the restricted dynamics.

Let \(M_e(t)\in\{0,1\}\) be the state of edge \(e\) at integer attempted-update time \(t\). Put \(\pi=p/(p+q)\), \(r=1-p-q\in(-1,1)\), and \(Z_e(t)=M_e(t)-\pi\). For a nonempty subset \(S\subseteq E\), write \(H_S(t)=\prod_{e\in S} Z_e(t)\) and \(d_S(v)=|\{e\in S:v\in e\}|\). The lag-one normalized temporal statistic is
\[
C_S(1)=\frac{\mathbb E_{\mathrm{stat}}[H_S(0)H_S(1)]}{[\pi(1-\pi)]^{|S|}}.
\]
Here expectations are under the unique stationary environmental law, which is not assumed known in advance. The **order** of an observation is the number of distinct edge IDs in \(S\), not the number of individual time-indexed factors.

## Proof
**1. Stationarity and diagonalization.** The single-edge flip kernel
\[
K=\begin{pmatrix}1-p&p\\q&1-q\end{pmatrix}
\]
has invariant Bernoulli law with success probability \(\pi\), and maps \(m-\pi\) to \(r(m-\pi)\) in conditional expectation. The full environmental chain chooses a vertex and applies independent copies of \(K\) on its incident edges, with a holding step of probability \(1-\omega\). Thus its invariant distribution is the product Bernoulli law \(\bigotimes_{e\in E}\mathrm{Bernoulli}(\pi)\). Because every selected edge can flip while all other edges incident to the selected vertex stay unchanged with positive probability, each single-edge flip has positive probability. Consequently the finite environmental chain is irreducible; the positive holding probability makes it aperiodic, so this invariant distribution is unique. Each product \(H_S\) is an eigenfunction for the one-step Markov operator with eigenvalue
\[
\lambda_S=1-\omega+\frac{\omega}{N}\sum_{v\in V}r^{d_S(v)}.
\tag{1}
\]
All products indexed by subsets \(S\subseteq E\), including the constant empty product, form an orthogonal eigenbasis for the product stationary distribution. Consequently, for every integer \(t\ge0\),
\[
\frac{\mathbb E_{\mathrm{stat}}[H_S(0)H_S(t)]}{[\pi(1-\pi)]^{|S|}}=\lambda_S^t.
\tag{2}
\]
No independence between distinct edges at consecutive times is assumed: their dependence arises from the common selected vertex.

**2. Pairwise adjacency is observable.** For two distinct edges \(e,f\), exactly two cases occur. If they share one endpoint, the three affected vertices have selected-edge degrees \((2,1,1)\); otherwise four endpoints have degree one. Equation (1) gives
\[
\lambda_{\mathrm{incident}}=1-\frac{\omega}{N}(1-r)(3+r),\qquad
\lambda_{\mathrm{disjoint}}=1-\frac{4\omega}{N}(1-r).
\]
Therefore
\[
\lambda_{\mathrm{incident}}-\lambda_{\mathrm{disjoint}}
=\frac{\omega}{N}(1-r)^2>0.
\tag{3}
\]
Every edge pair's measured statistic \(C_{\{e,f\}}(1)\) determines whether the two edges are incident. Thus the entire **edge-labelled line graph** \(L(G)\) is recovered. The classical line-graph theorem of Whitney [2] reconstructs the connected components of a simple graph from their line graphs, with the only ambiguity that a three-edge triangle and a three-edge claw have the same three-vertex line graph. This classical theorem is used, not claimed as new.

**3. Third-order resolution of the only ambiguity.** Let \(S\) consist of the three mutually incident edges of an ambiguous line-graph component. For a triangle, \(d_S(v)=2\) at its three vertices; for a claw the central degree is three and three leaves have degree one. Equation (1) becomes
\[
\lambda_{\triangle}=1-\frac{3\omega}{N}(1-r^2),\qquad
\lambda_{\mathrm{claw}}=1-\frac{\omega}{N}[(1-r^3)+3(1-r)].
\]
Hence
\[
\lambda_{\triangle}-\lambda_{\mathrm{claw}}
=\frac{\omega}{N}(1-r)^3>0.
\tag{4}
\]
One lag-one statistic involving these three labelled edges selects the correct component. Applying this to every ambiguous component reconstructs all graph edges' endpoints up to a vertex permutation; the no-isolates condition excludes unobservable isolated vertices. In fact if the graph is connected and its number of vertices is known, triangle and claw also differ by order, but the third-order rule works uniformly for disconnected graphs.

**4. Order-three sharpness without changing the number of vertices.** Take \(N=7\) and six observed edges labelled \(0,1,2,3,4,5\). In graph \(A\), edges \(0,1,2\) form a claw and edges \(3,4,5\) form a disjoint triangle. In graph \(B\), the first three form a triangle and the last three a claw. Every vertex has positive degree. The edge-labelled line graphs agree: each of the two disjoint three-edge sets forms a complete three-clique. For any subset of at most two labelled edges, the **projected environmental transition kernel** depends only on whether those two edges have a common endpoint. It is therefore identical in the two networks, as is the projected stationary distribution; all their finite-dimensional trajectory distributions on one or two observed edge IDs coincide. Nevertheless a vertex permutation preserving each edge label cannot map \(A\) to \(B\): the first three edges form a triangle in one and a claw in the other. Equation (4) distinguishes them with three-edge observations. This proves that observation order two does not universally identify the edge-labelled incidence structure even when \(N\), \(p\), \(q\) and \(\omega\) are given. The two graphs are isomorphic if edge labels are forgotten; the claim is explicitly about reconstruction with persistent observed edge identities.

## Verification
The standalone standard-library script `check.py` constructs the complete stochastic transition matrices over the \(2^6=64\) binary environmental states for both seven-vertex graphs, with
\[
p=\frac12,\qquad q=\frac14,\qquad\omega=\frac23,\qquad r=\frac14.
\]
It verifies exact row sums and product-law stationarity, and the eigenfunction identities for all \(2^6-1=63\) nonempty subsets for **each** graph, using rational arithmetic. It checks equality of every one- and two-edge stationary-lag signature across the graphs, and finds
\[
\lambda_{\mathrm{claw}}=\frac{155}{224},\quad
\lambda_{\triangle}=\frac{41}{56},\quad
\lambda_{\triangle}-\lambda_{\mathrm{claw}}=\frac9{224}.
\]
The finite exact computation illustrates and independently cross-checks the formulas; the proof for arbitrary \(N\) and every admissible parameter is the analytic argument above. Execute `python check.py` with Python 3; no packages are required.

## Relationship to prior work
Betz, Fu and Masuda [1, Secs. 2–6] introduce and analyze the binary edge-feedback evolutionary game, including agent-based trajectories and mean-field/pair approximations. The present finding concerns an exact **post-consensus stochastic inverse problem**, not the coexistence dynamics, mean-field fixed points, or general payoff-dependent evolutionary process. Whitney [2] established the fundamental uniqueness/exception theorem for line graphs, which the present proof applies to observed lag eigenvalues. Shandilya and Timme [3] reconstruct connections from continuous-state ordinary-differential-equation trajectories; their derivation presupposes differential equations and is not a result about stationary stochastic binary edge observations or the order-two/three separation here. The diagonalization of independent two-state kernels and the line-graph theorem themselves are classical; the asserted contribution is their synthesis into an exact observation-order classification for the specified vertex-clock environmental process, including a matched-parameter indistinguishability witness. Existing related general methods may subsume this specialization; originality has not been independently established.

## Limitations
This is an exact population-law identification result, not a finite-sample stability bound or an estimator with an explicit confidence interval. It requires labelled access to individual edge states across time, knowledge of the total number of vertices and positive transition rates, uniform vertex selection, and fixed unanimous strategies. It does not recover vertex names, edge directions, missing isolated vertices, or unknown switching parameters without additional assumptions. The lower bound concerns preserving edge IDs; the explicit witness graphs are unlabelled-isomorphic. No result is asserted about general mixed-strategy evolutionary trajectories or observational noise, and no independent scientific review has been performed.

## References
[1] K. Betz, F. Fu and N. Masuda, *Evolutionary games on networks with negative edge-based environmental feedback*, arXiv:2611.11029v1, first posted 8 November 2026, https://arxiv.org/html/2611.11029v1 .

[2] H. Whitney, *Congruent graphs and the connectivity of graphs*, American Journal of Mathematics 54 (1932), 150–168, https://doi.org/10.2307/2371086 .

[3] S. G. Shandilya and M. Timme, *Inferring network topology from complex dynamics*, New Journal of Physics 13 (2011), 013004, https://doi.org/10.1088/1367-2630/13/1/013004 .
