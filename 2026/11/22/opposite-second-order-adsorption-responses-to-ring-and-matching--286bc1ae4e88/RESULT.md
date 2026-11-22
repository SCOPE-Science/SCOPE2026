# Opposite second-order adsorption responses to ring and matching biases on the Möbius–Kantor graph

## Finding
Let \(G=\mathrm{GP}(8,3)\) be the 16-vertex Möbius–Kantor graph, and perform irreversible edge-dimer random sequential adsorption from an entirely vacant substrate. Each available edge receives independent Poisson attempts at its specified constant rate; an attempt succeeds if and only if both endpoints are still vacant. Denote by \(Q_B(t)\) the probability of a perfect eight-dimer terminal covering when edges in a designated eight-edge subset \(B\) have rate \(t>0\) and the other sixteen edges have rate one.

For the eight outer-ring edges \(R\) and for the eight spokes \(M\) (a perfect matching), the exact homogeneous probability and first two responses are
\[
\begin{aligned}
Q_R(1)=Q_M(1)&=\frac{903422}{3840375},\\
Q_R'(1)=Q_M'(1)&=0,\\
Q_R''(1)&=\frac{276830066540632837}{4793798789772300000}>0,\\
Q_M''(1)&=-\frac{561926341371011}{43579988997930000}<0.
\end{aligned}
\]
Consequently, **homogeneous rates are a strict local minimum of perfect-covering probability under an outer-ring bias but a strict local maximum under a spoke-matching bias**. Both perturbations affect exactly eight edges in the same edge-transitive cubic graph. Thus the sign of the second-order response depends on the geometry of the marked edge set, not its cardinality or a distinction between edge orbits.

At the homogeneous point the complete terminal-size distribution is
\[
\Pr(X=6)=\frac{868823}{6912675},\qquad
\Pr(X=7)=\frac{2008042}{3142125},\qquad
\Pr(X=8)=\frac{903422}{3840375},
\]
where \(X\) is the number of deposited dimers. These are exact probabilities, not simulation estimates.

## Assumptions and scope
Write the vertex set as \(\{u_i,v_i: i\in\mathbb Z/8\mathbb Z\}\). The undirected edge set consists of the outer ring \(\{u_i,u_{i+1}\}\), the inner step-three ring \(\{v_i,v_{i+3}\}\), and the spokes \(\{u_i,v_i\}\), each for the eight values of \(i\), with indices taken modulo eight. These 24 distinct edges give the standard simple cubic graph \(\mathrm{GP}(8,3)\). The marked set \(R\) comprises the eight outer-ring edges; \(M\) comprises the eight spokes. Only one marked family is biased at a time.

For every \(t>0\), the first successful attempt on an active edge set occurs on edge \(e\) with probability proportional to its rate. Rejected attempts cannot change the vacant set. Each accepted dimer irreversibly occupies its two endpoints. The process stops when no edge joins two vacant vertices. A perfect covering means all sixteen vertices have been occupied by exactly eight dimers. All graph vertices and edges are labeled; there are no desorption, diffusion, or cooperative deposition moves.

## Proof
For an occupied-vertex set \(S\subseteq V\), let \(A(S)\) be the edges with both endpoints outside \(S\), let \(k(S)=|A(S)|\), and let \(a_B(S)=|A(S)\cap B|\). Define \(F_S(t)\) to be the conditional probability of reaching perfect covering from \(S\) under the rate assignment just specified. For a terminal state \(A(S)=\varnothing\), set \(F_S(t)=1\) when \(S=V\), and zero otherwise. For every nonterminal state, the exponential-race identity gives the exact finite recursion
\[
F_S(t)=\frac{\displaystyle\sum_{e\in A(S)}
\bigl(1+(t-1)\mathbf1_{e\in B}\bigr)F_{S\cup e}(t)}
{k(S)+(t-1)a_B(S)},
\]
where \(S\cup e\) denotes adding both endpoints of \(e\). Every term on the right has exactly two more occupied vertices, so this recurrence terminates after at most eight successful depositions, with no approximation or infinite-limit argument. All its denominators are positive for \(t>0\); hence every \(F_S\) is analytic in a neighborhood of \(t=1\).

For compact exact evaluation, write \(p_S=F_S(1)\), \(d_S=F_S'(1)\), and \(c_S=F_S''(1)\). Differentiating the recursion twice gives, with \(k=k(S)\) and \(a=a_B(S)\),
\[
\begin{aligned}
p_S&=\frac1k\sum_{e\in A(S)}p_{S\cup e},\\
d_S&=\frac1k\left[\sum_{e\in A(S)}\left(d_{S\cup e}+\mathbf1_{e\in B}p_{S\cup e}\right)-a p_S\right],\\
c_S&=\frac1k\left[\sum_{e\in A(S)}\left(c_{S\cup e}+2\mathbf1_{e\in B}d_{S\cup e}\right)-2a d_S\right].
\end{aligned}
\]
For terminal states the derivative entries vanish. Therefore all values are determined by finite rational additions and divisions by positive integers. `verify_vertices.py` implements these formulas over **all 7,314 reachable occupied-vertex masks**, obtaining at \(S=\varnothing\) exactly the four displayed derivatives and the terminal-size distribution.

To rule out dependence on the vertex-state representation, `verify_matchings.py` independently constructs the 24 edges in interleaved type order and tracks the **set of already deposited edges** as a 24-bit mask. It exhausts **11,068 reachable partial matching masks**, reconstructs the active edges, and applies the separately implemented rational jet recursion. The two independently constructed state spaces yield exactly the same rational values for both marked sets.

Since \(Q_R'(1)=Q_M'(1)=0\), both curvature signs displayed in the finding are strict. Taylor's formula then gives a strict local minimum for \(Q_R\) and a strict local maximum for \(Q_M\) at \(t=1\). This conclusion is local: no global extremum or uniqueness away from the homogeneous point has been established. The vanishing first derivatives are also consistent with edge transitivity and invariance of terminal probabilities under uniform rescaling of all edge rates, but their exact vanishing is certified independently by both recurrences.

## Verification
Run `python3 verify_vertices.py` and `python3 verify_matchings.py` with Python 3 and its standard library only. Both exit nonzero if a graph invariant, visited-state count, exact rational curvature, or first-derivative identity fails. The required completion markers are `VERTEX_STATE_EXACT_OK` and `MATCHING_STATE_EXACT_OK`. The former also checks that the complete terminal-size distribution sums to one. Both verifiers use exact `fractions.Fraction` arithmetic; no floating-point fitting, random sampling, external tables, or implicit graph-library conventions enter the proof.

## Relationship to prior work
Pippenger (1989) established the graph random-sequential-adsorption/greedy-matching setting and obtained adsorption results on regular and locally tree-like graphs. Penrose and Sudbury (2005) gave the general finite-graph dimer-adsorption construction and analyzed infinite-tree occupation and correlation functions. Gamarnik and Goldberg (first public preprint 2008) established performance and concentration bounds for random greedy matchings on regular graphs, also treating independently and identically weighted variants. These frameworks motivate the present finite-cage question, but the materials inspected do not give the two rate-derivative signs for \(\mathrm{GP}(8,3)\).

An existing exact calculation of uniform-rate dimer jamming on the Petersen graph concerns a different ten-vertex cubic graph and has no heterogeneous-rate response. Results comparing uniform monomer adsorption on two cospectral 16-vertex graphs concern a different adsorption rule and do not imply the curvature signs. The Möbius–Kantor graph and its edge-transitivity are standard graph-theoretic facts and are not claimed as discoveries. The novelty assessed here is the **opposite, exactly determined second-order perfect-covering response for two equally large, structurally different marked edge sets on the same graph**.

## Limitations
The result is an exact finite-graph statement on this labeled 16-site substrate, not a general theorem for cubic graphs, larger generalized Petersen graphs, other adsorption protocols, or all positive rates. A local extremum need not be a global extremum. The exact rational computations constitute a complete finite proof but have not undergone independent external mathematical validation. Historical priority remains subject to further unindexed literature; full text of Pippenger (1989) was unavailable through the examined routes, so no whole-document noncoverage claim is made about that source.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, arXiv:math/0503519v1 (2005-03-24), https://arxiv.org/abs/math/0503519.
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1 (2008-07-08), https://arxiv.org/abs/0807.1277.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, https://doi.org/10.1137/0402034 (abstract and bibliographic record examined; full text unavailable).
4. E. W. Weisstein, *Möbius–Kantor Graph*, MathWorld, https://mathworld.wolfram.com/Moebius-KantorGraph.html.
5. *Exact dimer-jamming kinetics on the Petersen graph*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dimer-jamming-kinetics-on-the-petersen-graph--e4a3af5b8d37.
6. *Strict kinetic separation of two cospectral graphs under hard-core monomer adsorption*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-strict-kinetic-separation-of-two-cospectral-graphs-under-hard-co--0f9e5993c6ec.
