# Exact identifying-code censuses for the four-, five-, and six-symbol undirected length-two Kautz graphs

## Finding

Let \(U_q\) be the undirected length-two Kautz graph. A radius-one identifying code is a set \(C\) for which the sets \(N[v]\cap C\) over all vertices \(v\) are nonempty and pairwise different, with \(N[v]\) the closed neighborhood. The following table gives the exact minimum size and counts of minimum identifying codes:

| Alphabet size \(q\) | Minimum size | Labeled minimum codes | Orbits under simultaneous alphabet relabeling |
|---:|---:|---:|---:|
| 4 | 4 | 168 | 10 |
| 5 | 5 | 24 | 1 |
| 6 | 7 | 4320 | 6 |

The entries for \(q=4,5,6\) in `verification/orbit_representatives.json` give a representative and exact orbit size for every orbit. The six-symbol graph is the first after the four- and five-symbol cases in which the minimum exceeds the alphabet size. In particular, the equality with alphabet size in those two cases does not extend to the next case.

## Definitions and scope

The vertex set is \(V_q=\{(a,b):0\leq a,b<q,\ a\neq b\}\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent if and only if \(b=c\) or \(d=a\). The graph is undirected and loopless; the closed neighborhood of a vertex includes the vertex itself. Two distinct code subsets on this labeled vertex set count separately. The orbit action uses the same permutation of the alphabet on both coordinates, and is not defined using the full automorphism group. The finding concerns only \(q=4,5,6\).

## Proof

The finite checker `verification/enumerate_codes.cpp` enumerates the size-\(k\) subsets of \(V_q\) by a two-branch inclusion/exclusion recursion keeping track of the number of vertices still to be chosen. Indices are the bit positions in the subset representation. The checker constructs closed-neighborhood masks from the adjacency condition and accepts a candidate mask if and only if all its intersections with those masks are nonzero and pairwise unequal. Thus the recursive leaves counted as accepted subsets are exactly the identifying codes of size \(k\). The relevant full layers are:

| \(q\) | \(k\) | Total candidates \(\binom{q(q-1)}k\) | Accepted |
|---:|---:|---:|---:|
| 4 | 3 | 220 | 0 |
| 4 | 4 | 495 | 168 |
| 5 | 4 | 4845 | 0 |
| 5 | 5 | 15504 | 24 |
| 6 | 6 | 593775 | 0 |
| 6 | 7 | 2035800 | 4320 |

The intersection signatures for a larger code restrict to the corresponding signatures for any smaller code contained in it. Hence extending a code preserves identification. The empty layer immediately below the first positive layer rules out all smaller sizes. Exhaustion of each first positive layer gives the exact labeled counts.

For the orbit claim, the representative table and `verification/orbit_check.py` provide the finite certificate. For each representative, applying every permutation of the alphabet generates its full orbit, and the verifier checks that the representative and its images are identifying codes. For \(q=4\) the sorted orbit sizes are \(6,6,12,12,12,24,24,24,24,24\); for \(q=5\) the single size is \(24\); for \(q=6\) all six sizes are \(720\). The orbit sets for any one \(q\) were checked to be disjoint. Their union in each case is a subset of the minimum identifying codes and has cardinality equal to the exhaustive count, so the classification is complete.

## Reproduction

From the package root, compile and run `c++ -O3 -std=c++17 verification/enumerate_codes.cpp -o codes && ./codes`, then run `python3 verification/orbit_check.py`. With NumPy and SciPy, `python3 verification/crosscheck.py` corroborates the minimum sizes by solving an integer hitting-set model: one constraint hits each closed neighborhood for nonemptiness and one hits each pairwise symmetric difference for separation. The integer model is not used to count codes or certify the orbit census. The unchanged verification artifacts also include the three-symbol case as a comparison instance outside the finding.

## Relationship to prior work

For \(q=3\), the two directed cyclic orientations of the three alphabet symbols give two triangles, joined by the matching that reverses ordered pairs. Thus \(U_3\) is the triangular prism, isomorphic to the line graph of \(K_{2,3}\). The edge-identification result of Foucaud et al. [3, Proposition 11 and the example immediately after it] gives the minimum size four by specializing to \(K_{2,3}\). The three-symbol case is not part of the claimed contribution. For \(q\geq4\), a vertex \((a,b)\) has three pairwise nonadjacent forward neighbors of the form \((b,c)\), giving an induced claw; since line graphs are claw-free, these cases lie outside the line-graph result.

Fan, Xu and Lü [1] use the undirected Kautz graph (the present graph has length parameter two and degree parameter \(q-1\) in their convention) for restricted edge-connectivity, not for identification. Horan [2] studies undirected de Bruijn graphs, which include repeated-letter vertices. Directed Kautz identification with closed outgoing or incoming neighborhoods is also different: symmetrizing the graph alters both domination and the symmetric differences used for separation, so directed optima and counts cannot be carried over as identifying-code censuses.

## Limitations

This is a finite classification, not a formula for larger alphabet sizes. The complete orbit census is only under simultaneous symbol relabeling. The exhaustive checks concern the stated graph and signature predicate; they do not establish historical priority.

## References

1. Y. Fan, J. Xu and X. Lü, *The Restricted Edge-Connectivity of Kautz Undirected Graphs*, Ars Combinatoria (2006), https://combinatorialpress.com/ars-articles/volume-081-ars-articles/the-restricted-edge-connectivity-of-kautz-undirected-graphs/.
2. V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403 (2015), https://arxiv.org/abs/1508.00403.
3. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau and P. Valicov, *Identifying Codes in Line Graphs*, Journal of Graph Theory (2013), Proposition 11 and subsequent \(K_{2,n}\) example, pp. 430–431, https://perso.limos.fr/ffoucaud/Publications/Papers/J06_IDcodes_line_JGT_2013.pdf.
