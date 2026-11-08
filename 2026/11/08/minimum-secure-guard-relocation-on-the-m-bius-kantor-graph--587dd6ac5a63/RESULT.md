# Minimum secure-guard relocation on the Möbius–Kantor graph

## Finding

Let \(G=GP(8,3)\) be the sixteen-vertex Möbius–Kantor graph. A secure dominating set is a dominating set \(S\subseteq V(G)\) such that, for each \(v\notin S\), at least one selected neighbor \(u\in S\cap N(v)\) can be replaced by \(v\) while retaining ordinary domination. Then \(\gamma_s(G)=7\) and there are exactly \(336\) minimum secure dominating sets.

Let \(\mathcal T_J\) join two such minimum sets when one selected vertex is replaced by any unselected vertex, with secure domination retained. Let \(\mathcal T_S\) impose the additional condition that the removed and inserted vertices are adjacent in \(G\). Both are simple undirected graphs. The exact relocation structure is:

\[
|V(\mathcal T_J)|=|V(\mathcal T_S)|=336,\qquad |E(\mathcal T_J)|=1392,\qquad |E(\mathcal T_S)|=528.
\]

The jumping graph is connected; its radius is \(7\), its diameter is \(8\), and its vertex eccentricities are \(7\) (\(288\) vertices) and \(8\) (\(48\) vertices). Its degree counts are \(48\) of degree \(5\), \(96\) of degree \(6\), \(48\) of degree \(8\), and \(144\) of degree \(11\).

The sliding graph has \(25\) components: one of order \(288\) and twenty-four copies of \(K_2\). The large component has radius \(8\), diameter \(9\), and eccentricities \(8\) (\(192\) vertices) and \(9\) (\(96\) vertices); all \(48\) vertices of the isolated edges have eccentricity \(1\) within their components. Sliding degrees are \(1\) (\(48\) vertices), \(3\) (\(240\) vertices), and \(6\) (\(48\) vertices).

In particular the \(48\) minimum configurations belonging to isolated sliding edges can move only to their unique partner by an adjacent exchange, but each can reach every other minimum configuration when unrestricted guard replacement is permitted.

## Assumptions and scope

Vertices are \(u_i,v_i\) with \(i\in\mathbb Z/8\mathbb Z\); edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), interpreted as unordered pairs. There are sixteen vertices and twenty-four edges, with no loops or repeated edges. In the first verifier, vertices \(u_i\) are integers \(i\) and \(v_i\) are integers \(8+i\).

The *domination* condition used inside the definition of security is ordinary closed-neighborhood domination, not secure domination of every defense-replacement set. In contrast, every vertex of the two relocation graphs is itself a minimum **secure** dominating set; reconfiguration retains that stronger property. Each relocation replaces exactly one selected vertex, and the resulting set has the same cardinality. Radius and diameter are taken inside the connected graph or the stated connected component; the disconnected sliding graph has no global finite diameter under the conventional definition.

## Proof

The following exhaustive finite argument establishes the theorem. It is complete because the vertex universe has sixteen explicitly specified vertices and every relevant candidate is visited; it uses no probabilistic sampling.

For every bitmask \(m\in\{0,\ldots,2^{16}-1\}\), define the closed-neighborhood union
\[
R(0)=\varnothing,\qquad R(m)=R(m\setminus\{a\})\cup N[a],
\]
where \(a\) is the least numbered selected vertex. The recursion computes the exact set of dominated vertices. Therefore \(m\) dominates if and only if \(R(m)=V(G)\). For each dominating candidate \(m\), check every \(v\notin m\) and all defenders \(u\in m\cap N(v)\) against the exact precomputed ordinary-domination predicate on \((m\setminus\{u\})\cup\{v\}\). This Boolean condition is exactly the definition of secure domination.

Enumerate the \(\binom{16}{k}\) subsets separately for every \(k=0,\ldots,7\). The secure-set counts for \(k=0,1,\ldots,6\) are all zero; for \(k=7\) the count is precisely \(336\). This proves both the lower bound and attainment, without assuming a previously reported minimum number.

For each of those \(336\) seven-sets \(S\), enumerate every ordered pair \((u,v)\) with \(u\in S\), \(v\notin S\). Retain the neighbor \(T=(S\setminus\{u\})\cup\{v\}\) exactly when \(T\) belongs to the enumerated family; additionally retain it as a slide exactly when \(uv\in E(G)\). This exhausts every possible undirected relocation, each edge appearing in both endpoint searches. The resulting exact adjacency lists have \(1392\) jump edges and \(528\) slide edges and the stated degree distributions. A depth-first component traversal yields one jump component of order \(336\), one slide component of order \(288\), and twenty-four slide components of order two.

Finally breadth-first search from **every** state of **every** component gives exact shortest-path lengths and the eccentricity histograms quoted in the finding. In particular, the computed diameters are finite maximum distances of explicitly enumerated finite graphs; they are not estimates inferred from a sample.

The second verifier uses the independent eight-point/eight-line incidence model: points \(p_i\) and lines \(\ell_j\) are incident when \(i-j\equiv0,1,3\pmod8\). It independently enumerates subsets as Python immutable sets, checks domination and each defense without the bitmask recurrence, constructs relocations through shared six-vertex intersections, and computes components and all eccentricities. It contains an explicit sixteen-vertex bijection to the generalized Petersen indexing and checks the equality of all twenty-four edge images. Its results coincide with the first verifier's outputs.

## Verification

Both included standalone scripts require Python 3 and no third-party packages. From a directory containing the files, run:

```sh
python3 verify_gp.py
python3 verify_incidence.py
```

The exact standard output is included as `gp_output.txt` and `incidence_output.txt`. Each script has internal assertions for the minimum-cardinality count and every claimed component, edge, degree, and eccentricity count; the independent incidence verifier additionally checks the graph isomorphism. The scripts enumerate respectively \(\sum_{k=0}^7\binom{16}{k}\) candidates and all feasible optimum-to-optimum exchanges. The computation finishes normally under ordinary desktop conditions, so the output is not a timeout-dependent upper bound.

## Relationship to prior work

Secure domination and exact-search algorithms are developed by Burger, de Villiers and van Vuuren (2013), and edge-removal sensitivity by the same authors (2015). The latter paper studies a different graph transformation—deletion of *edges from the host graph*—rather than guard exchanges within a fixed host. Suzuki, Mouawad and Nishimura (2014) study reconfiguration of *ordinary* dominating sets of size at most a bound by additions/deletions, rather than fixed-size secure dominating sets joined by swaps. None of these results implies the enumerated twenty-five-component sliding network or the connected \(336\)-configuration jumping network. The Möbius–Kantor graph is also the Levi graph of the classical \(8_3\) configuration, giving the independent incidence-model check.

## Limitations

This is an exact statement for the specified sixteen-vertex graph only, not a formula for all generalized Petersen graphs. The computations certify the claimed finite facts in the fully specified models; they do not establish uniqueness of these invariants among larger cubic graphs, and they do not establish absolute historical novelty. No independent scholarly audit has been performed. Specialized unindexed computations and the general graph-protection literature remain historical-priority risks.

## References

1. A. P. Burger, A. P. de Villiers and J. H. van Vuuren, “Two Algorithms for Secure Graph Domination,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **85** (2013), 321–339. Public article date 2013-05-31. https://combinatorialpress.com/jcmcc-articles/volume-085/two-algorithms-for-secure-graph-domination/
2. A. P. Burger, A. P. de Villiers and J. H. van Vuuren, “Edge stability in secure graph domination,” *Discrete Mathematics & Theoretical Computer Science* **17** (2015), 103–122. DOI 10.46298/dmtcs.2120. https://dmtcs.episciences.org/en/articles/2120
3. A. Suzuki, A. E. Mouawad and N. Nishimura, “Reconfiguration of Dominating Sets,” arXiv:1401.5714, initial posting 2014-01-22. https://arxiv.org/abs/1401.5714
4. E. W. Weisstein, “Möbius–Kantor Configuration,” *MathWorld*, https://mathworld.wolfram.com/Moebius-KantorConfiguration.html. Graph-identity background only; no initial public date claimed.
