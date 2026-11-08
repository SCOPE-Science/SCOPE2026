# A strict-majority Lyapunov law for cyclic graph automata

## Finding

**Theorem (finite-graph fixation with an explicit Lyapunov budget).** Let \(G=(V,E)\) be any finite nonempty simple undirected graph, let \(\kappa\ge3\) be an integer, and let each vertex \(v\) have an integer contact threshold \(\theta_v\ge1\), satisfying \(2\theta_v>d_v\), where \(d_v\) is its graph degree. Each vertex has a state in \(\mathbb Z/\kappa\mathbb Z\). A vertex is *eligible* when at least \(\theta_v\) of its neighbors currently have its successor state. In a round, any subset \(S\) of eligible vertices advances simultaneously by one state; all other vertices remain unchanged.

Define the monochromatic-edge potential and uniform local margin by
\[
\Phi(c)=\#\{\{u,v\}\in E:c_u=c_v\},\qquad
\eta=\min_{v\in V}(2\theta_v-d_v)\ge1.
\]
For every round, including rounds with simultaneous updating, the **quantitative Lyapunov inequality** is
\[
\boxed{\Phi(c')-\Phi(c)\ge\sum_{v\in S}(2\theta_v-d_v)\ge\eta|S|.}
\]
Consequently the total number of vertex updates in any sequence of nonempty eligible batches is at most
\[
\boxed{\left\lfloor\frac{|E|-\Phi(c_0)}{\eta}\right\rfloor.}
\]
For the usual fully synchronous cyclic cellular automaton, every orbit reaches a fixed point by at most this many rounds. In particular, there are no nonconstant periodic orbits.

The strict inequality \(2\theta_v>d_v\) is sharp as a **universal** graph criterion: for each \(m\ge1\), the three-color rule at \(\theta=m\) on the complete tripartite graph \(K_{m,m,m}\), with colors constant and distinct on its three parts in cyclic order, is a genuine three-cycle, while \(d_v=2m\). The restriction \(\kappa\ge3\) is essential: on \(K_{m,m}\), two opposite colors alternate forever even when the threshold equals the full degree.

For the three-color Moore-neighborhood automaton on an \(L\times L\) torus with \(L\ge3\), every contact threshold \(\theta\ge5\) is covered. At the nontrivial first case \(\theta=5\), \(|E|=4L^2\) and \(\eta=2\), so every initial configuration fixates after at most \(2L^2\) nonstationary rounds, with no more than \(2L^2\) individual site changes.

## Assumptions and scope

The graph is finite and undirected with no loops or repeated edges; it need not be connected or regular. The local thresholds may differ from vertex to vertex, but are fixed in time, and all colors advance by exactly one modulo \(\kappa\). There is no stochastic averaging and no restriction on the initial coloring. For the synchronous map, *fixed point* means no vertex is eligible. The stronger batching formulation refers to arbitrary chosen subsets of eligible vertices; it never requires that ineligible vertices move. If the batching rule always chooses at least one eligible vertex whenever any exists, it too reaches a fixed point within the same update budget.

The torus corollary uses the eight **distinct** Moore neighbors on periodic square grids with \(L\ge3\). It does **not** establish fixation at the borderline Moore threshold \(\theta=4\), nor claim that \(\theta=5\) is sharp for that special graph family.

## Proof

Fix one round and let \(S\subseteq V\) be the moved vertices. Let \(I\) be the set of edges whose endpoints are both in \(S\), and let \(B\) be the set of edges with exactly one endpoint in \(S\). Partition \(B\) into: \(P\), the edges on which the unmoved endpoint had the moving endpoint's *successor* color; \(Q\), those on which both endpoints originally had the *same* color; and the remaining boundary edges \(R\). The cardinalities satisfy \(|B|=|P|+|Q|+|R|\).

Let \(a_v\) count the neighbors originally in vertex \(v\)'s successor state. Eligibility says \(a_v\ge\theta_v\) for every \(v\in S\). Every edge in \(P\) contributes exactly once to \(\sum_{v\in S}a_v\), and no other boundary edge contributes. Each edge of \(I\) contributes **at most once**: mutual successor relationships would require \(1\equiv-1\pmod\kappa\), impossible for \(\kappa\ge3\). Therefore
\[
\sum_{v\in S}\theta_v\le\sum_{v\in S}a_v\le|I|+|P|,
\quad\text{so}\quad |P|\ge\sum_{v\in S}\theta_v-|I|.
\]
Edges in \(I\) retain their equality/inequality because both endpoints advance, and edges with no endpoint in \(S\) are unchanged. On \(B\), an edge enters the monochromatic set exactly when it belongs to \(P\), and leaves exactly when it belongs to \(Q\). Thus
\[
\begin{aligned}
\Phi(c')-\Phi(c)
&=|P|-|Q|\\
&\ge2|P|-|B|\\
&\ge2\sum_{v\in S}\theta_v-2|I|-|B|\\
&=\sum_{v\in S}(2\theta_v-d_v),
\end{aligned}
\]
where the final equality is the degree-sum identity \(\sum_{v\in S}d_v=2|I|+|B|\). This proves the main inequality, with equality allowed in intermediate estimates.

If \(S\ne\varnothing\), the potential grows by at least \(\eta|S|\); since \(0\le\Phi\le|E|\), summing over all rounds gives the stated bound on total vertex advances. Each nonempty round contains at least one advance, so there are no more nonempty rounds than advances. The fully synchronous rule has a nonempty update exactly when the state is not fixed; it therefore terminates at a fixed configuration and cannot have a nontrivial cycle.

For sharpness, partition \(K_{m,m,m}\) into three equal parts and assign them colors \(0,1,2\). Each vertex has degree \(2m\) and exactly \(m\) successor-colored neighbors, so all vertices advance at threshold \(\theta=m\), repeatedly, giving a primitive three-cycle. For \(\kappa=2\), assign opposite colors to the parts of \(K_{m,m}\); every neighbor is the successor at threshold \(m=d_v\), and the two configurations alternate. Finally, for the Moore torus \(|E|=4L^2\), \(d_v=8\), and \(\theta=5\) yields \(\eta=2\); substitution completes the corollary.

## Verification

The included standalone standard-library program `verify_majority.py` checks exact update inequalities, total-update bounds, and extremal cycles. It exhaustively enumerates all labeled simple graphs with two through five vertices and every three- and four-color initial configuration, totaling **1,098 graphs and 1,319,754 trajectories**. It separately checks every nonempty eligible update subset for each three-color configuration on every labeled graph with two through four vertices (**5,001 batch checks**), random graphs of sizes 8, 12, 18 and 30, Moore tori of side lengths 3, 4, 5 and 7, and the complete multipartite examples. All tests succeeded. Exhaustive small systems and finite sampling are supplementary; the proof above establishes the statement for arbitrary finite graphs and sizes.

Reproduce with `python3 verify_majority.py` from a standard Python 3 installation. No dependencies outside the standard library are required.

## Relationship to prior work

Muñoz and Nuño [1] study periodicity and lattice-symmetry reduction for the three-color Moore cyclic automaton. Their threshold sweep reports no observed oscillating attractors at high thresholds but does not provide this all-initial-state, all-finite-graph Lyapunov inequality or worst-case update count. Fisch, Gravner and Griffeath [2] introduced the threshold-range family and describe high-threshold fixation phenomena for lattice rules. Bello and Sivakoff [3] give probability-one fixation and fluctuation regimes on infinite regular trees from random initial states; the present deterministic finite-graph statement has different quantifiers.

Matamala and Goles [4] investigate cyclic automata on finite graphs and transient/period bounds, and Goles and Martínez [5] establish potential-function methods for a distinct class of cyclically monotone automata networks. Both are relevant historical comparisons. The full text of [4] was not accessible during this comparison, so priority relative to that work remains a concrete limitation; no exhaustive historical novelty claim is made.

## Limitations

The global convergence theorem assumes strict local successor majorities, finite undirected graphs, and \(\kappa\ge3\). It does not imply fixation for \(\theta=4\) on the eight-neighbor Moore torus, extend to infinite graphs through an infinite edge budget, or classify stationary configurations. The update bound is a rigorous universal bound, not an assertion of optimality for a particular lattice. Historical priority is not established for inaccessible specialized earlier sources.

## References

[1] F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990v1 (first posted 27 October 2026), https://arxiv.org/abs/2610.37990.

[2] R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39, https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf.

[3] J. Bello and D. Sivakoff, *Cyclic cellular automata and Greenberg–Hastings models on regular trees*, arXiv:2108.06404 (2021), https://arxiv.org/abs/2108.06404.

[4] M. Matamala and E. Goles, *Dynamic behavior of cyclic automata networks*, Discrete Applied Mathematics **77** (1997), 161–184, https://doi.org/10.1016/S0166-218X(97)84104-2.

[5] E. Goles and S. Martínez, *Lyapunov functionals for automata networks defined by cyclically monotone functions*, SIAM Journal on Discrete Mathematics **4** (1991), 200–206, https://doi.org/10.1137/0404020.
