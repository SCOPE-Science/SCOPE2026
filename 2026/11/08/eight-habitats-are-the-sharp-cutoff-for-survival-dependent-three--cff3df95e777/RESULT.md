# Eight habitats are the sharp cutoff for survival-dependent three-terminal corridor augmentation

## Finding

Let \(G=(V,E)\) be a connected finite simple undirected graph; designate exactly three permanently present terminals \(T\subseteq V\). Every other vertex survives independently with the same probability \(p\in(0,1)\); an edge is usable exactly when its two endpoints survive. Given a choice of one absent edge \(e\in\binom V2\setminus E\), maximize the probability \(R_e(p)\) that all three terminals are connected in the surviving induced subgraph after adding \(e\).

**Sharp result.** For every connected \(G\) with at most seven vertices and at least one absent edge, there is an absent edge that maximizes \(R_e(p)\) for **every** \(p\in(0,1)\). This remains true coefficientwise conditional on any fixed number of surviving nonterminal vertices. Eight is sharp: take \(V=\{0,1,\ldots,7\}\), \(T=\{0,1,2\}\), and
\[
E=\{(0,4),(0,5),(1,5),(1,6),(2,3),(2,4),(2,7),(3,6),(5,7)\}.
\]
The unique optimal new corridor is \(e_B=(1,2)\) when \(0<p<(\sqrt5-1)/2\), and \(e_A=(0,1)\) when \((\sqrt5-1)/2<p<1\). Exactly these two tie at the threshold. Their reliability difference is
\[
R_{e_A}(p)-R_{e_B}(p)=p(1-p)^2(p^2+p-1).
\]

## Assumptions and scope

The three terminals never fail; all other sites fail independently with identical probabilities; corridors have no additional independent failure, delays, capacity limits or direction. Every endpoint pair not already adjacent is eligible. No geometry, budget distinctions beyond exactly one new edge, or selection of terminal positions is imposed. A complete graph has no eligible corridor and is excluded from the optimization statement. All graph sizes include the three terminals. This is a *site*-failure model, not bond percolation.

## Proof

Write \(m=|V|-3\) and \(U=V\setminus T\). For each absent edge \(e\), define the nonnegative integers \(c_e(k)\) to count subsets \(S\subseteq U\) of cardinality \(k\) such that the terminals are not all connected in \(G[T\cup S]\), but become connected in \((G+e)[T\cup S]\). The gain has the exact Bernstein expansion
\[
R_e(p)-R_0(p)=\sum_{k=0}^m c_e(k)p^k(1-p)^{m-k},\qquad 0<p<1,
\]
where \(R_0\) is the reliability before augmentation. There are exactly two terminal-containing components in such an eligible state, because one new edge cannot connect three initially distinct terminal components. Both endpoints of \(e\) must be alive and belong to the two different terminal-containing components. Conversely that condition suffices. This proves that `gain_vectors` in the bundled `verify.py` computes each \(c_e(k)\) by exact finite subset enumeration.

For the lower bound, `atlas.tsv` supplies the 1,253 unlabelled undirected graphs on 0–7 vertices, in the standard graph-atlas encoding (order counts \(1,1,2,4,11,34,156,1044\)). Completeness of this recognized atlas, rather than the checker alone, is the external combinatorial catalogue input [5]. Connected graphs are examined; for every choice of three labelled positions for terminals and each absent pair, `verify.py` constructs its entire coefficient vector. Cases with at most one absent pair are immediate; in the remaining **32,191** graph–terminal instances, the checker exhibits an eligible \(e_*\) satisfying
\[
c_{e_*}(k)\ge c_e(k)\qquad\text{for every eligible }e\text{ and each }k=0,\ldots,m.
\]
The exact case counts for orders four, five, six, and seven are respectively \(16,190,2200,29785\). Since every Bernstein basis term is strictly positive for \(0<p<1\), coefficientwise domination implies universal probability optimality. Relabellings preserve the coefficients, so an unlabeled atlas suffices for all finite labelled graphs. This proves the cutoff through seven vertices, conditional on the stated atlas completeness.

For the displayed eight-vertex witness, the graph is connected, has nine existing edges and 19 eligible new edges. Enumerating the \(2^5=32\) surviving nonterminal subsets produces
\[
(c_{e_A}(0),\ldots,c_{e_A}(5))=(0,1,4,3,0,0),
\]
\[
(c_{e_B}(0),\ldots,c_{e_B}(5))=(0,2,5,2,0,0).
\]
Every other eligible new edge has a vector strictly componentwise dominated by at least one of these two; neither winner vector is duplicated. Because all \(p^k(1-p)^{5-k}>0\) on \(0<p<1\), no other edge can tie the larger gain. Subtraction gives
\[
R_{e_A}-R_{e_B}=-p(1-p)^4-p^2(1-p)^3+p^3(1-p)^2
=p(1-p)^2(p^2+p-1).
\]
The quadratic has exactly one zero in \((0,1)\), namely \((\sqrt5-1)/2\); its sign proves the announced unique switch. Together with the exhaustive lower bound this proves eight is minimal.

## Verification

The standalone standard-Python checker is `verify.py`; `atlas.tsv` is its only non-code dependency. From the directory containing both files run `python3 verify.py`. It checks all 1,253 atlas entries and their expected order counts, all 32,191 nontrivial graph–terminal cases, the 19 witness interventions and both gain vectors; it also independently recomputes the witness's augmented and unaugmented terminal connectivity by explicit breadth-first search on every survivor subset (rather than relying on the two-terminal-component gain criterion). Its complete replay printed both `ATLAS PASS` and `WITNESS PASS`, with the exact counts above. Checks use integer arithmetic, not floating-point sampling. The catalogue itself is not reproved by code; its unlabelled completeness is cited from [5].

## Relationship to prior work

Hock and Mumby [1] motivate uncertain dispersal connections through single-path reliability in ecological patch networks, rather than one-edge augmentation optimizing *joint connectivity of three permanently present sites under independent node failures*. Xie et al. [2,3] treat three-terminal **edge**-failure reliability and global comparisons of fixed-size graphs rather than site failure after adding one edge to the same network. Romero's survey [4] explicitly distinguishes node versus edge failure and terminal objectives. The related iterative augmentation literature [6] is an important priority risk: only its abstract, not its full paper, was available for comparison. These are substantive differences in probability space and design action, not title-only novelty claims.

## Limitations

The proof of the seven-vertex cutoff is finite and exhaustive **conditional on completeness and correct transcription of the published graph atlas**; it is not a structural graph-theoretic classification of all orders. The eight-vertex witness is exact. The result applies to independent, identical-probability failures of nonterminal sites with protected terminals and perfectly functioning edges; it does not cover edge failures, general dependent patch loss, more than one new edge, geographical corridor costs, or observed ecological outcomes. Historical priority in specialized site-reliability and network-augmentation literature is not conclusively established, particularly for inaccessible complete texts of [6] and other vertex-reliability design studies. Independent review has not been performed.

## References

[1] Hock, K., and Mumby, P. J. (2015), “Quantifying the reliability of dispersal paths in connectivity networks,” Journal of the Royal Society Interface 12, 20150013. https://doi.org/10.1098/rsif.2015.0013 (first publicly indexed 2015-02-26).
[2] Xie, S., Zhao, H., Dai, L., and Yin, J. (2021), “On locally most reliable three-terminal graphs of sparse graphs,” AIMS Mathematics 6, 7518–7531. https://doi.org/10.3934/math.2021439.
[3] Xie, S., Zhao, H., and Yin, J. (2021), “Uniformly Most Reliable Three-Terminal Graph of Dense Graphs,” Mathematical Problems in Engineering, 6664959. https://doi.org/10.1155/2021/6664959.
[4] Romero, P. (2022), “Uniformly optimally reliable graphs: A survey,” Networks 80, 466–481. https://doi.org/10.1002/net.22085 (online 2021-12-06).
[5] Read, R. C., and Wilson, R. J. (1998), An Atlas of Graphs, Oxford University Press. Atlas generation documented at https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html.
[6] Romero, P. (2017), “Building uniformly most-reliable networks by iterative augmentation,” RNDM, doi:10.1109/RNDM.2017.8093016 (abstract only inspected).
