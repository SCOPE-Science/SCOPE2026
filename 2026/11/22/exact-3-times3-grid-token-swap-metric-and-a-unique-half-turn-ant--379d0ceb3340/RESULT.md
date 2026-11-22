# Exact \(3\times3\) grid token-swap metric and a unique half-turn antipode

## Finding
Let \(G=P_3\square P_3\) be the nine-vertex square grid, with vertices indexed \(v=3r+c\) for \(r,c\in\{0,1,2\}\). A configuration is a bijection from vertex indices to the nine distinguishable token labels \(0,1,\ldots,8\). A move exchanges the tokens at two edge-adjacent vertices; no blank square is present. Write \(\mathcal T(G)\) for the complete configuration graph and \(d_{\mathcal T}\) for its shortest-swap distance.

The graph \(\mathcal T(G)\) is connected, bipartite, regular of degree \(12\), and vertex-transitive on \(9!=362{,}880\) vertices. Its radius and diameter are both **\(16\)**. **Every configuration has exactly one antipode at distance \(16\)**: rotate the *positions* of all nine tokens by \(180^\circ\) around the central grid vertex. Thus there are exactly \(9!/2=181{,}440\) unordered diameter-achieving pairs.

The exact counts of configurations at respective distances \(0,1,\ldots,16\) from *any* given configuration are
\[
(1,12,88,470,1978,6658,18081,38936,65246,83000,76688,48316,18975,4024,382,24,1).
\]
Let \(L(p)=\lceil\frac12\sum_{v=0}^8 \operatorname{dist}_G(v,p(v))\rceil\), the standard half-total-token-distance lower bound relative to the identity target, where token labels also denote their target vertices. The maximum excess \(d_{\mathcal T}(p,\mathrm{id})-L(p)\) is exactly \(5\), attained by exactly \(20\) configurations. The complete excess multiplicities for excess \(0,1,\ldots,5\) are
\[
(98647,167522,84339,11850,502,20).
\]

## Assumptions and scope
The configuration graph is **sequential distinct-token swapping**, not the classical sliding-tile puzzle with one empty square, not simultaneous swaps on matchings, and not swaps between arbitrary positions. The grid has exactly nine fixed *labelled* sites \(0,\ldots,8\), row-major, and exactly twelve undirected edges, obtained by changing one coordinate by one. The theorem is **finite**, specific to this grid. No asymptotic formula for larger meshes is asserted.

## Proof
**1. Reduction to the identity.** For a configuration \(p\), let \(p(v)\) be the label at site \(v\). Any relabeling of tokens \(p\mapsto\sigma\circ p\), for \(\sigma\in S_9\), preserves exactly the allowed site-edge swaps, giving a transitive action on the configurations. Accordingly all reference configurations have the same distance-layer counts. There are twelve possible site-edge swaps from each configuration, all distinct. A swap changes permutation parity, so the graph is bipartite. The twelve transpositions correspond to edges of the connected base grid; these transpositions generate \(S_9\), so the graph is connected. In addition the exhaustive traversal below visits every one of the \(9!\) possible configurations without relying on that general generation argument.

**2. Exhaustive finite lemma (exact BFS certificate).** Set \(p_0=(0,1,\ldots,8)\). The supporting program `verify_grid.py` represents permutations by nine-byte sequences and builds a queue starting with \(p_0\). When a sequence \(p\) is removed from the queue, it swaps the two entries for each of the twelve site edges and inserts any previously unseen neighbor at distance \(d(p)+1\). Standard breadth-first-search induction proves the assigned value is the exact minimum number of swaps: every length-\(j\) walk is discovered by layer \(j\), and no shorter walk exists for a vertex first discovered at layer \(j\). Each dequeued vertex is processed exactly once and all twelve neighbors are generated; the traversal stops only on an empty queue. This tests the entire graph, not a sampled subset. The program asserts that exactly \(362{,}880=9!\) different configurations were discovered and that the complete distance-layer histogram is exactly the displayed 17-term tuple, ending in \(24,1\). Its assertion that the sole state at distance \(16\) is the reversed row-major sequence \((8,7,6,5,4,3,2,1,0)\) proves both the diameter and uniqueness of the antipode at the identity.

For independent implementation redundancy, the included `verify_grid_factoradic.cpp` uses a separate factorial-rank state representation, a dense BFS array and its own rank/unrank functions. It asserts the same complete distance census and sole antipode; the two programs use independently implemented state encodings and edge generators.

**3. Antipodes of arbitrary configurations.** Define \(\rho(v)=8-v\), the site permutation induced by half-turn rotation of the grid. The sole antipode to the identity is \(\rho\). Under the label-relabeling automorphism \(\sigma=p\), the identity configuration becomes \(p\), and \(\rho\) becomes \(p\circ\rho\). Thus \(p\circ\rho\), obtained by a physical half-turn of the contents of the board, is the **unique** antipode to \(p\). Because \(\rho\ne\mathrm{id}\) and \(\rho^2=\mathrm{id}\), this pairs the \(9!\) states into exactly \(9!/2\) unordered diametral pairs. Vertex transitivity gives \(\operatorname{rad}=\operatorname{diam}=16\).

**4. Exact transportation-deficit census.** Any edge swap moves exactly two tokens one grid edge; therefore the total Manhattan distance to the identity decreases by at most two at each move, proving \(L(p)\le d_{\mathcal T}(p,p_0)\). The independent programs iterate through all \(9!\) labelled states, calculate their actual shortest distances and the integer lower bound \(L(p)\), and count each possible difference. Both find the exact six-term excess histogram displayed above, with maximum \(5\) reached by \(20\) placements.

## Verification
To reproduce the proof on a Python 3 standard-library installation, run `python3 verify_grid.py` from the directory holding the accompanying code. It uses no external data or libraries, asserts all counts, exits on disagreement and prints an explicit summary on success. For an independent representation, compile `c++ -O2 -std=c++17 verify_grid_factoradic.cpp -o grid_check` and execute `./grid_check`; the program has built-in exact assertions. All displayed values are generated from enumerating **all** labelled configurations and every legal edge swap. The two programs were run successfully from these packaged source files.

## Relationship to prior work
Aichholzer et al., *Hardness of Token Swapping on Trees* (arXiv:2103.06707, first public 2021-03-11), addresses computational complexity and approximation on trees. Bonnet, Miltzow and Rzążewski, *Complexity of Token Swapping and Its Variants* (Algorithmica, 2017 online), establishes complexity results, general exact algorithms and easy/hard graph classes. Their results furnish motivation and a standard lower bound but do **not** state the exact seventeen-layer \(3\times3\) grid census, unique half-turn antipodes or the twenty maximally deficient configurations. Other exact token-swapping computations for different host graphs and classical blank-tile \(3\times3\) puzzles are distinct problems. Searches for synonyms such as the Cayley graph of \(S_9\) generated by grid-edge transpositions did not locate covering published tables; this non-identification is **not** proof of absolute novelty.

## Limitations
The theorem does not give a symbolic short proof of the numerical BFS layers, nor any claim for \(P_m\square P_n\) with larger parameters. Its exact computations require the explicit executable finite enumeration supplied here, not an inference from a finite sample to an infinite family. The calculation concerns sequential swaps between two occupied sites, which must not be confused with the eight-puzzle. Literature and indexing gaps remain possible; independent audit has not been performed.

## References
1. O. Aichholzer et al., *Hardness of Token Swapping on Trees*, arXiv:2103.06707, version 1 first public 2021-03-11. https://arxiv.org/abs/2103.06707
2. É. Bonnet, T. Miltzow and P. Rzążewski, *Complexity of Token Swapping and Its Variants*, Algorithmica, online 2017-10-20, DOI 10.1007/s00453-017-0387-0. https://link.springer.com/article/10.1007/s00453-017-0387-0
3. T. Miltzow et al., *Approximation and Hardness of Token Swapping*, ESA 2016, DOI 10.4230/LIPIcs.ESA.2016.66 (general problem background only). https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2016.66
