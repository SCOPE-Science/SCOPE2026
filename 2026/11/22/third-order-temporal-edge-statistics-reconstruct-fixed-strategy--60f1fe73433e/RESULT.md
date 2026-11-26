# Third-order temporal edge statistics reconstruct labelled fixed-strategy interaction networks

## Finding

In the unanimous-strategy restriction of the vertex-update environmental game of Betz, Fu and Masuda [1], the stationary lag-one statistics of products involving at most three distinct, labelled edges determine the full incidence structure of every finite simple graph without isolated vertices, up to a vertex permutation preserving every edge label. The formulas hold everywhere in the nondegenerate parameter regime below. Three is the smallest universal observation order even on **connected** graphs with known vertex count: two assignments of the same six edge labels to the edges of the complete graph on four vertices have identical stationary trajectories on every set of one or two observed edges, but differ on a labelled triple.

## Model and scope

Let \(G=(V,E)\) be simple and undirected, with \(N\ge2\) known and no isolated vertices. Edge IDs and the step clock are observed; vertex names and incidences are not. Strategies are fixed at unanimous cooperation or defection, so an attempted strategy update leaves the environment unchanged. With probability \(0<\omega<1\), choose a vertex uniformly and independently apply the two-state kernel
\[
K=\begin{pmatrix}1-p&p\\q&1-q\end{pmatrix},\qquad 0<p,q<1,
\]
to each incident edge, holding the other edges fixed. The appropriate source rates are \((p_0,q_0)\) under all cooperation and \((p_2,q_2)\) under all defection. Put \(\pi=p/(p+q)\), \(r=1-p-q\), and \(H_S(t)=\prod_{e\in S}(M_e(t)-\pi)\) for a set \(S\) of distinct observed edge IDs. The statistic of order \(|S|\) is
\[
C_S=\frac{\mathbb E_{\mathrm{stat}}[H_S(0)H_S(1)]}{[\pi(1-\pi)]^{|S|}},\qquad C_\varnothing=1.
\]
Order counts edge IDs, not time-indexed factors. The rates and \(N\) are taken as known.

## Proof

**Stationary law and lag-one formula.** The kernel \(K\) preserves Bernoulli\((\pi)\) and multiplies the centered coordinate by \(r\) in conditional expectation. Every update at a specified vertex preserves the product Bernoulli law, and their mixture with holding steps does too. Any one edge can flip with positive probability while every other edge holds, by selecting one of its endpoints and using the positive single-edge hold probabilities. Hence the finite chain is irreducible and its product stationary law is unique. Let \(d_S(v)\) be the number of edges of \(S\) incident at \(v\). The independence of updates conditional on the selected vertex gives the eigenfunction identity
\[
\mathbb E[H_S(t+1)\mid M(t)]
= \lambda_S H_S(t),\qquad
\lambda_S=1-\omega+\frac\omega N\sum_{v\in V}r^{d_S(v)}.
\]
The stationary second moment of \(H_S\) is \([\pi(1-\pi)]^{|S|}\), so \(C_S=\lambda_S\).

**Recovering common endpoints.** For a nonempty edge set \(T\), define \(a_T=|\bigcap_{e\in T}\partial e|\), where \(\partial e\) is the two-element endpoint set of \(e\). Expanding \(r^{d_S(v)}=\prod_{e\in S}(1+(r-1)\mathbf1_{v\in\partial e})\) gives
\[
C_S-1=\frac\omega N\sum_{\varnothing\ne T\subseteq S}(r-1)^{|T|}a_T.
\]
For \(|S|\le3\) every term needed for inversion is observed:
\[
a_S=\frac{N}{\omega(r-1)^{|S|}}
\sum_{T\subseteq S}(-1)^{|S|-|T|}(C_T-1).
\]
The denominator is nonzero. For two distinct edges \(a_S=1\) if they meet and \(0\) otherwise. The incident-minus-disjoint lag gap is \(\omega(1-r)^2/N\). For three mutually incident edges the triangle has \(a_S=0\) and the three-edge star has \(a_S=1\). Their lower-order terms are identical, so the triangle-minus-star lag gap is \(\omega(1-r)^3/N>0\). This distinction applies to a triple anywhere in the graph, not just to triples forming components.

**Recovering all labelled incidences.** For each pair \(e,f\) with \(a_{\{e,f\}}=1\), form
\[
U(e,f)=\{e,f\}\cup\{g\in E\setminus\{e,f\}:a_{\{e,f,g\}}=1\}.
\]
By simplicity, \(e,f\) have a unique common endpoint \(v\), and \(U(e,f)\) is exactly the full set of edges incident at \(v\). Every vertex of degree at least two occurs this way. Two different such vertices cannot give the same set, because then two distinct edges would have the same two endpoints. Deduplicate these sets and create one reconstructed vertex for each. An edge occurring in \(d\) of the sets is assigned \(2-d\) new private degree-one endpoints. In particular a component consisting of a single edge gives two private endpoints. Every original vertex is represented, since there are no isolates. This constructs the unique edge-label-preserving incidence structure.

**Why two edge IDs do not suffice, even on connected graphs.** Put labels \(0,1,2,3,4,5\) on the edges \(01,02,03,23,13,12\) of \(K_4\), respectively. In the second assignment move each label to the complementary edge (the unique disjoint edge). The pair relation is unchanged: two distinct edges are disjoint exactly when they are complementary, and complementing both preserves this relation. But labels \(0,1,2\) are incident at a common vertex in the first assignment and form a triangle in the second. No vertex permutation preserving the observed IDs can match the two. For a fixed set of at most two observed edges, which of them receive \(K\) at the next step depends only on \(N\) and on whether the two have a common endpoint. The projected transition matrix therefore agrees in the two assignments on each such fixed set; its transition law does not depend on hidden edges. The projected stationary laws are also identical. This proves equality of all trajectory distributions on each fixed set of at most two edge IDs, not just equality of lag-one moments. The third-order gap on labels \(0,1,2\) distinguishes the assignments.

## Reproducibility

Run `python3 check.py` with the Python standard library. The checker builds projected transition matrices in exact fractions, verifies the stationary probabilities, computes the normalized lag numerically in exact rational arithmetic, checks it against the eigenvalue formula, and reconstructs labelled incidence sets and leaf multiplicities. At \(p=1/2,q=1/4,\omega=2/3\), the connected four-vertex witness has gap \(9/128\). A second witness on seven vertices exchanges which of two disjoint triples of edge IDs forms a claw and which forms a triangle, with gap \(9/224\). For both witnesses the test checks equality of all one- and two-edge projected transition matrices. It also checks the incidence reconstruction from the lag formula on all simple graphs without isolated vertices on fixed labelled vertex sets of orders two through five (814 graphs total), using a negative \(r\). The universal claims follow from the algebraic proof, not these finite checks.

## Relationship to prior work and limitations

The vertex-clock rule is from [1]. The tensor-product eigenfunctions of the update kernels and the line-graph viewpoint on pairwise incidence are standard. Whitney's graph-isomorphism uniqueness theorem [2] for connected roots does not identify a particular edge-labelled line-graph isomorphism with a vertex permutation; complementing the six edges of \(K_4\) illustrates the difference. The specific contribution is an exact observation-order criterion for this stochastic model, including how its third-order statistic supplies common-endpoint information and why even the full order-two projected trajectories do not suffice. The sharpness witness is about labelled incidence and does not constitute an unlabelled nonidentifiability result. The theorem is population-law identifiability, not a noisy finite-sample guarantee, and does not treat unobserved edges, isolated vertices, unknown rates or mixed-strategy dynamics.

## References

1. K. Betz, F. Fu, and N. Masuda, *Evolutionary games on networks with negative edge-based environmental feedback*, arXiv:2611.11029v1 (2026), https://arxiv.org/html/2611.11029v1.
2. H. Whitney, *Congruent graphs and the connectivity of graphs*, American Journal of Mathematics 54 (1932), 150–168, https://doi.org/10.2307/2371086.
