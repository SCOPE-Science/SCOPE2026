# Exact five-orbit dimer-jamming law on the Heawood graph

## Finding

In irreversible random sequential dimer adsorption on the Heawood graph, the final number \(X\) of deposited dimers has the **exact** law
\[
\Pr(X=5)=\frac{19}{330},\qquad
\Pr(X=6)=\frac{497}{792},\qquad
\Pr(X=7)=\frac{1247}{3960}.
\]
No other terminal count is possible. Thus the mean is \(\mathbb EX=24779/3960\), the expected vertex coverage is \(24779/27720\), and perfect occupancy has probability \(1247/3960\). The possible terminal matchings number \(42\), \(168\), and \(24\), respectively. Under the full graph automorphism group, these \(234\) matchings split into **five** orbits with the following exact per-matching probabilities:

| Dimers | Orbit cardinality | Probability of each labelled matching | Total orbit probability |
|---|---:|---:|---:|
| \(5\) | \(42\) | \(19/13860\) | \(19/330\) |
| \(6\) | \(28\) | \(261/98560\) | \(261/3520\) |
| \(6\) | \(56\) | \(8257/1995840\) | \(8257/35640\) |
| \(6\) | \(84\) | \(91723/23950080\) | \(91723/285120\) |
| \(7\) | \(24\) | \(1247/95040\) | \(1247/3960\) |

In particular, terminal matchings with the *same cardinality* can have different deposition probabilities; the three distinct size-six orbit probabilities are not recoverable from the static matching-size census.

## Assumptions and scope

The Heawood graph \(G\) has point vertices \(P_i\) and line vertices \(L_j\), indexed modulo seven, with an edge \(P_iL_j\) exactly when \(i-j\in\{0,1,3\}\pmod7\). It is the point–line incidence graph of the Fano projective plane, with fourteen vertices, twenty-one edges, and degree three. Initially all sites are empty. Every edge receives one independent, identically distributed continuous arrival priority. Processing the edges in increasing order, an arrival occupies its two endpoints if and only if both are vacant; rejected arrivals have no further effect. Accepted edges form a matching, which is inclusion-maximal when the process ends. Independent rate-one exponential arrival clocks give the same terminal law. Results are for a *single irreversible deposition round*, not equilibrium monomer–dimer fugacity sampling or repeated desorption.

## Proof

**First-arrival recursion.** For any set \(U\subseteq V(G)\) of occupied sites, put \(A(U)=\{uv\in E(G):u,v\notin U\}\). Let \(F_U(z)\) be the probability generating polynomial of the number of *future* accepted edges. Conditioning on the earliest arrival among currently feasible edges gives the finite identity
\[
F_U(z)=\begin{cases}
1,&A(U)=\varnothing,\\[3pt]
\displaystyle\frac{z}{|A(U)|}\sum_{uv\in A(U)}F_{U\cup\{u,v\}}(z),&A(U)\ne\varnothing.
\end{cases}
\]
The recurrence terminates because each transition occupies two previously empty vertices. The conditioning is valid even though some rejected priorities may have occurred: the remaining feasible priorities retain exchangeable relative order. This also follows directly by ordering all twenty-one i.i.d. continuous priorities.

**Two-step reduction.** Edge transitivity lets the first accepted edge be \(P_0L_0\). Sixteen disjoint edges remain eligible for the second accepted dimer. Exactly eight second-edge choices leave twelve feasible edges and eight leave eleven; within each class the residual graph is isomorphic. The distribution of the number \(Y\) of *additional* dimers after the first two is:

| Feasible edges after second dimer | Number of second-edge choices | \(\Pr(Y=3)\) | \(\Pr(Y=4)\) | \(\Pr(Y=5)\) |
|---|---:|---:|---:|---:|
| \(12\) | \(8\) | \(4/105\) | \(731/1260\) | \(481/1260\) |
| \(11\) | \(8\) | \(89/1155\) | \(1559/2310\) | \(191/770\) |

These entries are obtained by repeated application of the displayed exact finite recurrence; the complete edge list and replay code appear in the standalone verifiers. Averaging the two equally likely rows and adding the first two dimers gives precisely the stated \(5,6,7\) law. This is an *exhaustive finite proof*, not a Monte Carlo estimate.

**Terminal configurations and symmetry.** A final matching \(M\) is possible if and only if it is inclusion-maximal, equivalently every graph edge touches an endpoint of an edge of \(M\). The include/exclude enumeration over all twenty-one labelled graph edges, with the no-common-endpoint restriction, gives exactly \(42\), \(168\), and \(24\) maximal matchings at sizes five, six, and seven. A complete enumeration of the Fano-plane point permutations preserving its seven line triples yields \(168\) incidence-preserving collineations. The explicit duality \(P_i\mapsto L_{-i}\), \(L_j\mapsto P_{-j}\) doubles this to the full group of \(336\) graph automorphisms. Their induced actions on the maximal matchings have orbit cardinalities \(42,28,56,84,24\).

For a fixed maximal matching \(M\) of size \(k\), its exact probability is obtained by summing over the \(k!\) orders of its edges, or equivalently by dynamic programming over its subsets:
\[
H_M(S)=\begin{cases}
1,&S=M,\\[2pt]
\displaystyle\frac{1}{|A(V(S))|}\sum_{e\in M\setminus S}H_M(S\cup\{e\}),&S\subsetneq M,
\end{cases}
\]
where \(V(S)\) is the union of endpoints in \(S\). For every intermediate \(S\subsetneq M\), the denominator is positive. Evaluating \(H_M(\varnothing)\) for a representative of each of the five computed orbits gives the five per-matching probabilities in the table. Since graph automorphisms preserve the arrival-priority law, the value is constant within each orbit. The individual class masses sum to one and recover the size distribution.

## Verification

Three standalone standard-library Python checkers are included: `check_vertex.py` executes the occupied-vertex-mask recurrence with exact rational arithmetic; `check_edge.py` independently constructs the seven Fano lines by nonzero binary vectors and executes an edge-conflict-mask recurrence; `check_orbits.py` enumerates all \(234\) terminal matchings, all \(336\) symmetries, their five orbits, and the exact probability of every terminal matching by edge-order subset recursion. All programs contain assertions of the full stated outputs; running `python3 check_vertex.py`, `python3 check_edge.py`, and `python3 check_orbits.py` requires only the Python standard library. A second-edge partition into two eight-member classes supplies an intermediate cross-check independent of the orbit census.

## Relationship to prior work

Penrose and Sudbury (2005) defined dimer random sequential adsorption on general graphs and developed occupation equations and results for Bethe lattices, with large-graph limit theory. Gamarnik and Goldberg (2008) gave randomized greedy matching bounds and finite-girth corrections for regular graphs. Those frameworks justify the model and general algorithm but their examined results do not state the exact five-orbit Heawood terminal measure. The classical count of twenty-four perfect matchings on the Heawood graph is background information, not claimed as new. The contribution assessed here is the full rational terminal distribution and its finer symmetry-orbit splitting for this canonical cubic cage.

## Limitations

The result concerns the labelled fourteen-site Fano incidence graph and equal, independent, continuous edge-priority laws. It does not provide a limiting jamming law for growing projective-plane incidence graphs, unequal edge rates, desorption, finite-time coverage, or adsorption on arbitrary cubic graphs. Historical novelty is assessed only against the examined literature and research records; inaccessible or unlocated equivalent computations remain possible. The computations are exact and finite and do not imply a general theorem for infinite networks.

## References

- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889. Earliest arXiv preprint 24 March 2005, `arxiv:math/0503519v1`, https://arxiv.org/pdf/math/0503519.
- D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, `arxiv:0807.1277v1`, first submitted 8 July 2008, https://arxiv.org/html/0807.1277v1.
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
- Standard Heawood-graph combinatorial data, including the twenty-four perfect matchings: https://jaanos.github.io/tables/graphs/Heawood.html.
