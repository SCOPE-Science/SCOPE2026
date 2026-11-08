# Local-sign parity and exact mobile distances in Petersen four-edge recolouring

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), and two vertices are adjacent exactly when the subsets are disjoint. Use the four **named** edge colours \(\{0,1,2,3\}\). In the reconfiguration graph \(\mathcal R\), vertices are all proper edge-colourings \(c:E(P)\to\{0,1,2,3\}\), and two vertices are adjacent when they differ at exactly one edge and both assignments are proper. In particular, a simultaneous exchange along a multiedge alternating path is **not** one move.

**Theorem (exact single-edge reconfiguration).** The graph \(\mathcal R\) has \(49\,920\) vertices and \(109\,440\) edges. It has exactly \(962\) connected components: \(960\) singletons and precisely two components of order \(24\,480\). Each nonsingleton component has radius \(24\) and diameter \(25\). There are \(38\,880\) nonsingleton colourings of eccentricity \(24\) and \(10\,080\) of eccentricity \(25\), summed over both components. The complete degree counts are

\[
\begin{array}{c|rrrrrrrr}
\text{degree}&0&1&2&3&4&5&6&7\\
\hline
\text{count}&960&1440&2880&10560&8640&12960&6720&5760.
\end{array}
\]

The two nonsingleton components are distinguished **completely** by a local-sign parity invariant. In each vertex of \(P\), put its three incident edges into the order induced by the lexicographic ordering of \(E(P)\), and let \(m_c(v)\) denote the unique colour absent from those edges. Let \(\sigma_v(c)\in\{+1,-1\}\) be the sign of the permutation
\[
(c(e_{v,1}),c(e_{v,2}),c(e_{v,3}),m_c(v))
\]
of \((0,1,2,3)\), and write \(\varepsilon(c)=\prod_{v\in V(P)}\sigma_v(c)\). The sign is invariant under every legal one-edge recolouring, and, among nonisolated colourings, equality of signs is **equivalent** to being in the same connected component. Each nonsingleton component contains \(24\,480\) colourings, one sign each; \(480\) frozen colourings of each sign are also present.

An edge \(uv\) can be recoloured if and only if \(m_c(u)=m_c(v)\). Hence a colouring is frozen precisely when the missing-colour map \(m_c\) is a proper vertex-colouring of \(P\). Every frozen colouring has missing-colour multiplicity pattern \((4,2,2,2)\), and the four vertices missing the distinguished colour are a maximum independent-set star of \(\operatorname{KG}(5,2)\). There are exactly \(960\) frozen colourings.

## Assumptions and scope

The graph and all colour labels are fixed, with no quotient by graph automorphisms or colour permutations. All edges are undirected and simple. All distances, radii and diameters concern the two nonsingleton connected components separately. Isolated vertices have no distance to colourings in other components. The computational classification is finite and exact; no uniform theorem about all cubic graphs' component structures is asserted.

## Proof

**1. Sign invariance (structural).** At a cubic vertex the three incident edge colours are distinct, so the fourth colour is unique. If a legal move changes edge \(uv\) from \(a\) to \(b\), then \(b\) must have been missing at both \(u\) and \(v\). At each endpoint the ordered four-tuple is changed by exchanging the entries \(a\) and \(b\); hence each endpoint sign is multiplied by \(-1\). Every other local tuple is unchanged, so \(\varepsilon\) is preserved. Conversely, the only possible alternative colour at edge \(uv\) is the unique colour missing at both endpoints, so it exists if and only if \(m_c(u)=m_c(v)\).

**2. Form of the frozen missing maps (structural).** For every colour \(a\), the number of vertices missing \(a\) equals \(10-2s_a\), where \(s_a\) counts edges currently coloured \(a\); therefore each multiplicity is even. If the colouring is frozen, each missing-colour class is an independent set of \(P\). Every independent set of \(\operatorname{KG}(5,2)\) has order at most four; the independent sets of order four are precisely the five stars of two-subsets containing one fixed symbol. No two such stars are disjoint. The four even multiplicities sum to ten, and each is at most four. The only ways to express ten as the sum of four even integers between zero and four are the multisets \(4,2,2,2\) and \(4,4,2,0\). The latter is impossible because the two four-vertex independent-set stars would have to be disjoint. Therefore the multiplicity pattern is \(4,2,2,2\). The six remaining vertices after removing a star induce three disjoint edges. Assigning three named missing colours twice each so that endpoints of those three edges disagree gives \(90-3\cdot18+3\cdot6-6=48\) maps for each chosen star and chosen distinguished colour. There are four choices of distinguished colour and five stars, so precisely \(4\cdot5\cdot48=960\) candidate frozen missing maps. The exhaustive reconstruction below establishes that each has exactly one realising proper four-edge-colouring, giving exactly 960 frozen states.

**3. Exhaustive state enumeration (computational proof).** In `verify_local.py`, construct the ten vertices as lexicographic two-subsets and the 15 graph edges as lexicographically ordered disjoint pairs. Depth-first search assigns a colour in \(\{0,1,2,3\}\) to each edge, rejecting a colour already present at either endpoint. This visits every proper assignment once and finds exactly \(49\,920\) assignments. For every assignment and each edge, test each of the other three labels against the colours at the four other incident edges. These are **all** possible one-edge moves, by their definition. The resulting symmetric adjacency has \(218\,880\) directed incidences, hence \(109\,440\) undirected edges; its breadth-first connected-component enumeration gives exactly \(960\) singleton components and two components of size \(24\,480\). Direct evaluation of \(\varepsilon\) is constant on each large component and opposite across them. Since the large components cover all nonfrozen configurations, the parity obstruction is complete there. The degree counts and the frozen-missing-map bijection are checked exhaustively.

**4. Exact distances (computational proof with justified symmetry reduction).** The alternating group \(A_5\) acts on the underlying five symbols, inducing Petersen graph automorphisms. The symmetric group \(S_4\) independently permutes colour labels. These actions are graph automorphisms of \(\mathcal R\) and therefore preserve eccentricities. The first program generates the action using a 3-cycle and a 5-cycle on the symbols and three adjacent transpositions on colours, and exhaustively enumerates exactly 42 state orbits; two are frozen orbits, and 40 meet nonsingleton components. Run ordinary breadth-first search from one representative of each of the 40 nonsingleton orbits. Each search reaches exactly \(24\,480\) vertices. The resulting weighted eccentricity census is \(38\,880\) at eccentricity \(24\), and \(10\,080\) at eccentricity \(25\). A transposition of two underlying symbols swaps the two parity sectors, proving that they have the same radius and diameter; the census shows radius \(24\) and diameter \(25\).

**5. Independent complete reconstruction (computational proof).** `verify_matching.py` independently enumerates all matching masks of the 15-edge graph, recursively partitions the edge set into exactly four disjoint matchings, and finds \(2080\) unlabelled four-matching partitions. Giving four colours to the classes in all \(24\) orders recovers \(49\,920\) assignments. Independent move generation moves a single edge from one matching class to a different class only when neither endpoint acquires a repeated colour. It reproduces all \(109\,440\) edges, components, degrees and parity sectors. The different encoding avoids relying on the first program's recursive colouring algorithm. The first program, rather than the second, establishes all-pairs eccentricities via the symmetry-reduced complete BFS construction.

## Verification

Reproduce with standard Python 3.10 or later (no external libraries) using `python3 verify_local.py` and `python3 verify_matching.py`. Both scripts are complete, included alongside this file, and terminate by assertions failing on any mismatch. Both were run from the packaged source contents. No random sampling or time-limited heuristic is involved. The BFS computation is exhaustive over symmetry orbits because every orbit is explicitly generated by graph automorphisms; ordinary breadth-first search computes exact shortest-path distances in an unweighted finite graph.

## Relationship to prior work

OEIS A159233 already gives the count of \(49\,920\) proper four-edge-colourings of the Petersen graph, credited to Alois P. Heinz (2009). That count is background, not the new assertion. Ito, Kamiński and Demaine (2009) introduced and studied exactly the single-edge recolouring move for list edge-colourings, proving general complexity results and tree-specific connectivity statements, but do not classify this graph. McDonald, Mohar and Scheide (2010, arXiv:1005.2248) proved that all four-edge-colourings of any subcubic graph are **Kempe equivalent**. Their Kempe move can exchange colours along an entire alternating path or cycle, and is fundamentally stronger than the single-edge move here; their theorem therefore does not imply connectivity, components, or diameter under single-edge changes. The line-graph formulation is equivalently single-vertex recolouring of \(L(P)\) with four colours. The present exact sign-class and metric classification is additional to the known colouring count and known Kempe connectivity.

## Limitations

This is a complete exact finite result for one explicitly specified graph, not a general bound for all cubic graphs. Exact eccentricities rely on independent executable enumeration and the first program's complete symmetry-reduced BFS, rather than a short closed-form structural argument. The local sign is a proven obstruction for all cubic graphs with four edge colours, but completeness of its two nonfrozen level sets is asserted only for the Petersen graph. The historically known count of 49,920 is not claimed original. Exhaustive priority in old, unpublished, or unindexed literature is not claimed; independent audit has not been performed.

## References

1. Alois P. Heinz, *Number of edge colorings of the Petersen graph*, OEIS A159233, 2009-04-06: https://oeis.org/A159233 (known count).
2. Takehiro Ito, Marcin Kamiński and Erik D. Demaine, *Reconfiguration of List Edge-Colorings in a Graph*, Algorithms and Data Structures (WADS), 2009, DOI 10.1007/978-3-642-03367-4_33, author's manuscript https://dspace.mit.edu/entities/publication/bb785ce8-54b8-410f-9221-e28f5a647d36 (single-edge move and general complexity).
3. Jessica McDonald, Bojan Mohar and Diego Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248, 2010-05-13, https://arxiv.org/abs/1005.2248 (stronger Kempe-move connectivity).
