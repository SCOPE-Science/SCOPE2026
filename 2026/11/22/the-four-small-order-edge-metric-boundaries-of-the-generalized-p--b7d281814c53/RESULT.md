# Counting the minimum edge-resolving sets of \(P(n,3)\) at orders seven through ten

## Finding

For the generalized Petersen graphs \(P(n,3)\) at \(n=7,8,9,10\), the respective numbers of minimum edge-resolving vertex subsets are **469, 368, 18, and 160**. These are labelled subset counts, not counts up to automorphism. The corresponding minimum sizes \(4,4,3,3\) are already stated in the concluding remarks of Wang, Wang and Zhang [1]; their Theorem 1.1 proves size four for every \(n\ge 11\). The contribution here is the four multiplicities, not the dimension classification or the two exceptional orders.

## Assumptions and scope

For \(n\ge7\), write the vertices as \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\). The \(3n\) distinct undirected edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\). The distance from a landmark vertex \(w\) to an edge \(\{a,b\}\) is \(\min(d(w,a),d(w,b))\) for shortest-path graph distance \(d\). A landmark set resolves the edges when each pair of distinct edges is distinguished by at least one landmark. Only orders seven through ten are counted.

## Proof

For each order, compute all vertex distances by breadth-first search in the specified graph and form the vertex-by-edge matrix \(M[w,\{a,b\}]=\min(d(w,a),d(w,b))\). The graph is connected since the outer cycle meets every inner vertex by a spoke. A set of rows resolves if and only if restriction to those rows leaves the \(3n\) columns pairwise distinct. Enumerating all unordered row subsets of sizes two, three and four gives:

| \(n\) | Resolving pairs | Resolving triples | Resolving four-sets | Number at minimum size |
|---:|---:|---:|---:|---:|
| 7 | 0 | 0 | 469 | 469 |
| 8 | 0 | 0 | 368 | 368 |
| 9 | 0 | 18 | 1,359 | 18 |
| 10 | 0 | 160 | 3,200 | 160 |

The enumeration independently recovers the known minima: resolving is preserved under adding vertices, so in each case the absence of resolving sets of the previous size rules out all smaller sets. With \(u_i\) represented by \(i\) and \(v_i\) by \(n+i\), the first minimum witnesses in lexicographic order are \(\{0,1,2,7\}\), \(\{0,1,2,11\}\), \(\{0,12,13\}\), and \(\{0,2,13\}\), respectively.

## Reproduction

From the record directory, compile `verify_exhaustive.cpp` using `g++ -O2 -std=c++17 verify_exhaustive.cpp -o verify_gp3` and run `./verify_gp3`; `cpp_results.txt` records the output across sizes two through four. Running `python3 verify_networkx.py` with NetworkX enumerates through the first successful size for each order; `python_results.txt` records its reported minimum counts and first witnesses. Both tests enumerate every subset at each size they report; neither estimates counts by sampling or checks other orders.

## Relationship to prior work and limitations

Wang, Wang and Zhang [1, §6] explicitly state all four dimensions. At order seven, they use the isomorphism \(P(7,3)\cong P(7,2)\) and Filipović, Kartelj and Kratica [2, §2.3 and Table 5]. An explicit isomorphism swaps the layers and sends index \(i\) to \(2i\) modulo seven: a step of one becomes an inner step of two, and a step of three becomes an outer step of minus one. The scalar at order eight and the two order-nine and order-ten exceptions also appear in [1, §6]. Neither that passage nor [2, Table 5], which gives a single representative basis for \(P(7,2)\), is a census of all optimal landmark subsets.

The counts distinguish the number of optimal choices even at orders with the same dimension. The cutoff is the four orders preceding the published stable-range theorem, not an arbitrary sample of the stable range. No counts outside these four orders or up to symmetry are claimed. Historical priority for the multiplicities is qualified by the sources inspected.

## References

1. D. G. L. Wang, M. M. Y. Wang, and S. Zhang, *The edge metric dimension of the generalized Petersen graph \(P(n,3)\) is 4*, Theorem 1.1 and §6, [arXiv:2005.08038](https://arxiv.org/abs/2005.08038), Journal of Combinatorial Optimization 43 (2022), 460–496, [DOI](https://doi.org/10.1007/s10878-021-00780-8).
2. V. Filipović, A. Kartelj, and J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, §2.3 and Table 5, [arXiv:1807.00580](https://arxiv.org/abs/1807.00580).
