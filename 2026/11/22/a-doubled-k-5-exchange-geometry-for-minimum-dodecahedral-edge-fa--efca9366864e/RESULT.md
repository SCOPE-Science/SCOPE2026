# A doubled-\(K_5\) exchange geometry for minimum dodecahedral edge-failure monitors

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph. A vertex subset \(S\) is a *monitoring edge-geodetic set* if every graph edge lies on every shortest path between some pair of distinct vertices in \(S\). Among its minimum such sets, form the \(r\)-exchange graph by joining distinct \(S,T\) when \(1\le |S\setminus T|=|T\setminus S|\le r\). Then:

1. The minimum cardinality is \(8\), and there are exactly \(25\) minimum sets. Five induce an edgeless subgraph of \(D\); the other twenty induce precisely three pairwise disjoint edges and two isolated vertices.
2. The \(r\)-exchange graph has no edges for \(r=1\) or \(r=2\). At the first nontrivial threshold, \(r=3\), it is isomorphic to the simple graph obtained by subdividing every edge of the doubled complete multigraph \(2K_5\) once. This is a connected \(25\)-vertex, \(40\)-edge graph with five vertices of degree \(8\) and twenty of degree \(2\), radius \(3\), and diameter \(4\).

Here \(2K_5\) means five vertices with two parallel edges connecting each unordered pair. Its full edge-subdivision is a simple bipartite incidence graph. The theorem is about simultaneous replacement of at most \(r\) sensors, not movement constrained to edges of \(D\).

## Assumptions and scope

All graphs are finite, simple, undirected and unweighted, except the auxiliary multigraph \(2K_5\). The original graph \(D\) has vertices \(u_i,v_i\), with \(i\in\{0,\ldots,9\}\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), with indices modulo \(10\). In `verify_deletion.py`, \(u_i=i\), \(v_i=10+i\).

For two original vertices \(x,y\) and original edge \(e\), the pair *monitors* \(e\) exactly if \(d_{D-e}(x,y)>d_D(x,y)\). This is equivalent to requiring \(e\) on **all**, not merely one, shortest \(x\)-to-\(y\) paths. The sensor budget is always the minimum possible cardinality, \(8\); exchanges do not temporarily use additional sensors or nonoptimal configurations.

## Proof

The following is a complete finite exhaustive proof with two separately implemented, standard-library-only programs. The equality checks in the attached programs are part of the proof and do not rely on sampled instances.

**Coverage reduction.** Number the \(30\) edges of \(D\) and, for every unordered vertex pair \(\{x,y\}\), form the \(30\)-bit witness mask
\[
W(x,y)=\{e\in E(D): d_{D-e}(x,y)>d_D(x,y)\}.
\]
A vertex set \(S\) is a monitoring edge-geodetic set if and only if the union of the witness masks for all unordered pairs in \(S\) equals \(E(D)\). This follows immediately by expanding the definition of monitoring separately for every edge; therefore the mask test has no omitted cases.

**Finite minimization and classification.** The deletion-distance verifier computes all \(30\) single-edge deletions using breadth-first search, and tests every one of the \(\binom{20}{7}=77520\) seven-sets and every one of the \(\binom{20}{8}=125970\) eight-sets. None of the seven-sets monitors every edge, while exactly \(25\) eight-sets do. As monitoring is upward closed under adding vertices, the seven-set failure also excludes all smaller sets. It computes the induced-edge count of every optimum, obtaining five with zero induced edges and twenty with three mutually disjoint induced edges.

The independent shortest-path verifier constructs an explicitly isomorphic differently labelled dodecahedron. For endpoints \(x,y\), let \(\sigma(x,y)\) count shortest paths. For an edge \(ab\), it counts shortest \(x\)-to-\(y\) paths using that edge by summing \(\sigma(x,a)\sigma(b,y)\) when \(d(x,a)+1+d(b,y)=d(x,y)\), and the reverse-oriented term when its distance equality holds. An edge belongs to every shortest path precisely when this total equals \(\sigma(x,y)\). This independently reconstructs every witness mask and repeats the exhaustive seven- and eight-set census.

**Exchange threshold.** The full unordered intersection profile of the \(25\) optima is
\[
\begin{array}{c|rrrrrrrrr}
|S\cap T|&0&1&2&3&4&5&6&7&8\\\hline
\#\{\{S,T\}:S\ne T\}&30&0&80&60&90&40&0&0&0.
\end{array}
\]
No distinct pair shares more than five of its eight vertices, hence there are no exchanges of one or two sensors. Every one of the forty three-exchange edges joins an independent optimum to one of the twenty other optima. Each of the latter is adjacent to exactly two independent optima, and each unordered pair of the five independent optima has **exactly two** such common adjacent nonindependent optima. These statements are exhausted and asserted by both programs. Consequently the exchange graph is exactly the edge-subdivision of \(2K_5\). In the subdivided doubled complete graph, each original vertex is at most three steps from any vertex, while two subdividing vertices with disjoint endpoint pairs can be four steps apart. Therefore the radius is \(3\) and the diameter is \(4\), as also independently verified by breadth-first search from every optimum.

## Verification

The package includes `verify_deletion.py`, `verify_geodesics.py`, and `optima.json`. Use Python \(3\) with only its standard library:

```
python3 verify_deletion.py
python3 verify_geodesics.py
```

Each program terminates with assertions for the complete minimality test, all optimum configurations, the intersection profile, the first connected exchange graph and its eccentricities, then prints `PASS`. The second program contains a concrete twenty-vertex permutation verifying the equivalence of its planar edge list and \(GP(10,2)\). The JSON file lists the exact \(25\) optimum configurations in the first labeling; it is a convenient certificate, not a substitute for the exhaustive verification. The two verifiers use independent edge-monitoring methods: edge-deletion distances versus exact shortest-path counts.

## Relationship to prior work

Dev, Dey, Foucaud, Narayanan and Ramasubramony Sulochana introduced monitoring edge-geodetic sets and established basic graph classes and complexity results; their initial public preprint appeared in October 2022. Haslegrave studied hardness and graph products in another October 2022 preprint. Foucaud and collaborators' March 2024 work proves general bounds and sufficient conditions, including vertex-cover monitoring in girth-at-least-five graphs. Those general statements do not entail the exact \(25\)-configuration census or the doubled-\(K_5\) exchange graph.

Tan, Li, Wang and Li's June 2023 study, *Monitoring edge-geodetic numbers of convex polytopes and four networks*, is especially relevant because it might include the dodecahedron's minimum monitoring number. Its accessible abstract emphasizes the minimum *number*, not the complete optimum-family intersection geometry. Its full text was not accessible during the comparison. Accordingly, priority is **not** claimed for the bare numerical minimum \(8\), and possible historical coverage of part of the classification remains an explicit unresolved risk. The identified contribution is the simultaneous-exchange threshold and exact optimal-configuration geometry, together with its reproducible finite proof.

## Limitations

The finding concerns a single canonical graph, not an all-order family or directed/weighted networks. Its proof is exhaustive computation over the finite, explicitly defined twenty-vertex graph, rather than a symbolic structural classification of an infinite family. Literature searches and accessible full-text inspections do not prove historical uniqueness. The closely relevant 2023 convex-polytope paper could not be materially compared in full; any overlapping theorem there would narrow the originality claim. No claim is made about independent mathematical verification.

## References

- S. R. Dev, S. Dey, F. Foucaud, K. Narayanan, and L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, first posted 2022-10-07, arXiv:2210.03774, https://arxiv.org/abs/2210.03774 .
- J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, first posted 2022-10-17, arXiv:2210.08955, https://arxiv.org/abs/2210.08955 .
- A. Tan, W. Li, X. Wang, and X. Li, *Monitoring edge-geodetic numbers of convex polytopes and four networks*, published online 2023-06-05, https://doi.org/10.1080/17445760.2023.2220143 .
- F. Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, first posted 2024-03-14, arXiv:2403.09122, https://arxiv.org/abs/2403.09122 .
