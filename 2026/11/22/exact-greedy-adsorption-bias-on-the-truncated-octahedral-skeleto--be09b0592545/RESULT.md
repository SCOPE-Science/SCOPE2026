# Exact greedy adsorption bias on the truncated octahedral skeleton

## Finding

Let \(G\) be the 24-vertex graph of a regular truncated octahedron, formed from all signed coordinate permutations of \((0,1,2)\) and joining pairs at squared distance \(2\). In nearest-neighbor-exclusion random sequential adsorption, examine all vertices in a uniformly random order and accept a vertex only when no adjacent vertex has already been accepted. Write \(J\) for the final number of occupied vertices.

The **complete exact jamming law** is

| \(k\) | \(\Pr(J=k)\) | Number of maximal independent sets of size \(k\) |
|---|---:|---:|
| 8 | \(7666301/62208000\) | 117 |
| 9 | \(926336912/1915538625\) | 208 |
| 10 | \(51963221287/178319232000\) | 36 |
| 12 | \(57033471421/560431872000\) | 2 |

All other probabilities are zero; notably, **size 11 is impossible**. The mean is \(\mathbb E J=1161395055131/122594472000\).

Let \(U\) be the size of a uniformly chosen maximal independent set of the same graph. Then \(\Pr(U=k)\) equals the third-column count divided by \(363\). The law of \(J\) strictly first-order stochastically dominates the law of \(U\): \(\Pr(J\ge t)\ge\Pr(U\ge t)\) for every real \(t\), with strict inequality for thresholds \(t\) satisfying \(8<t\le12\). In particular the probability of a maximum packing is amplified by precisely
\[
\frac{\Pr(J=12)}{\Pr(U=12)}=\frac{627368185631}{33965568000}>18.
\]

## Assumptions and scope

The underlying graph is fixed, simple and undirected. Vertices are exactly the 24 distinct signed permutations of \((0,1,2)\). Edges are those pairs whose squared Euclidean distance is exactly \(2\); this yields a connected cubic graph with 36 edges. All \(24!\) vertex orders are equiprobable. A vertex is permanently admitted if none of its neighbors was previously admitted. The final admitted set is necessarily independent and inclusion-maximal. The comparison law samples uniformly *among distinct maximal independent sets*, not among vertex permutations.

## Proof

For a finite residual vertex set \(S\subseteq V(G)\), let \(F_S(z)\) be the probability-generating polynomial of additional occupied vertices when a uniformly random order is applied to its induced subgraph. Conditioning on the first inspected residual vertex gives the exact recursion
\[
F_{\varnothing}(z)=1,\qquad
F_S(z)=\frac{z}{|S|}\sum_{v\in S}F_{S\setminus N[v]}(z),
\]
where \(N[v]\) is the closed neighborhood of \(v\) in the *original* graph and the deletion is intersected with \(S\). The discarded neighbors would be blocked by the first accepted vertex; conditional on its position, the relative order of every surviving vertex remains uniform. Induction on \(|S|\) proves the recursion for the entire distribution, not only for its mean.

Represent subsets by 24-bit masks. Evaluating this rational recursion from the full mask explores exactly 23,123 distinct residual masks and yields the four probabilities in the displayed table; the checker asserts the coefficients individually and their sum is one.

Independently enumerate all independent subsets by including or excluding the least remaining vertex, deleting its neighbors on inclusion. Retain a leaf subset if its closed neighborhood covers all 24 vertices. This visits every independent set once and keeps exactly the 363 inclusion-maximal independent sets, partitioned by size as shown. In particular the independence number is 12, attained twice, and no maximal independent set has size 11.

For each of the only three nontrivial support thresholds \(t=9,10,12\), subtract the uniform-maximal-set tail from the greedy tail. Exact arithmetic yields positive differences, respectively
\[
\frac{1498489579}{7527168000},\qquad
\frac{12449256306871}{43153254144000},\qquad
\frac{593402617631}{6164750592000}.
\]
The remaining thresholds have equal zero or unit tails or reduce to these. This proves strict stochastic dominance as stated. The mean and maximum-packing amplification follow by rational arithmetic from the probability table.

## Verification

Run the accompanying standalone Python 3 script `check_truncated_octahedral_adsorption.py`. It uses only the standard library, constructs the graph from integer coordinates, checks degrees and edges, computes the complete rational distribution, independently enumerates maximal independent sets, and verifies stochastic dominance, expectation, and the exact amplification factor. No floating-point numbers, Monte Carlo approximations or external data files are required. A complete rational calculation, rather than finite sampling, is a proof for this finite graph.

## Relationship to prior work

The random-order greedy exclusion rule is standard random sequential adsorption. Pippenger (1989) analyzed such adsorption on regular graphs and high-girth limits; Dhara, van Leeuwaarden and Mukherjee (2016, arXiv initial version) rigorously treat greedy activation on random graphs in a large-size regime. Neither of those inspected statements supplies the complete finite law on this specific highly symmetric cubic graph. The truncated octahedral graph is the skeleton of a space-filling Archimedean solid (the Kelvin cell), with 24 vertices and 36 edges. The independent-complex homotopy type studied separately in the literature does not give the random-order selection probabilities. The distinction between random-greedy and uniform-maximal-set sampling is important: they use the same support but assign markedly different weights to maximal packings.

## Limitations

This is an exact result for one naturally distinguished 24-vertex graph; it does not assert a universal stochastic-dominance theorem for all cubic graphs, and the particular positive inequalities need not persist on other graphs. The independence and jamming recursions are finite enumerations; no infinite-size asymptotic law is claimed. Earlier work on the general adsorption process is substantial, and bibliographic coverage does not prove historical uniqueness of the exact numerical values. Pippenger's 1989 text was not freely accessible in full during comparison; its inspected abstract discusses different structural and asymptotic questions.

## References

- S. Dhara, J. S. H. van Leeuwaarden and D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, arXiv:1604.03918, initial version 2016-04-13. https://arxiv.org/abs/1604.03918
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401, doi:10.1137/0402034. Public abstract: https://epubs.siam.org/doi/10.1137/0402034
- *Truncated octahedron*, Polyhedra Viewer, solid description (24 vertices, 36 edges and face structure): https://polyhedra.tessera.li/truncated-octahedron/info
