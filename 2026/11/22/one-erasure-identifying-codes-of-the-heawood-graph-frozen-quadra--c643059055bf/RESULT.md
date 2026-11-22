# One-erasure identifying codes of the Heawood graph: frozen quadrangles and mobile induced matchings

## Finding

**Theorem.** Let \(H\) be the fourteen-vertex Heawood graph, the point-line incidence graph of the binary Fano plane. A radius-one identifying code is a detector subset \(C\subseteq V(H)\) whose closed-neighborhood signatures \(I_C(v)=C\cap N[v]\) are nonempty and pairwise distinct. A *one-erasure identifying code* remains identifying after deletion of any one selected detector. Its exact minimum size is \(10\), attained by exactly \(98\) labelled codes, and its full cardinality polynomial is

\[
R_H(z)=98z^{10}+224z^{11}+91z^{12}+14z^{13}+z^{14}.
\]

Every optimum is the complement of exactly one of the following omitted four-vertex sets: (i) one of the \(14\) quadrangles on a single Fano shore (the complement of one projective line, or its dual); (ii) the four endpoints of one of \(84\) induced two-edge matchings in \(H\). These two classes are disjoint and exhaustive.

Let \(\mathcal R_r\) be the graph on the \(98\) minimum codes whose edges exchange **exactly** \(r\) selected vertices against \(r\) unselected vertices, with only the endpoints required to be minimum codes. Then \(\mathcal R_1\) consists of fourteen isolated quadrangle codes and one connected \(84\)-vertex \(4\)-regular component, with \(168\) edges. Its connected component has radius and diameter \(5\), and every vertex there has distance shells \((1,4,10,22,39,8)\). On the same \(98\) vertices, \(\mathcal R_2\) is connected with \(1134\) edges, radius and diameter \(2\), and degree \(30\) at each quadrangle code and \(22\) at each induced-matching code. Its corresponding distance shells are \((1,30,67)\) and \((1,22,75)\). Two simultaneous replacements are therefore necessary and sufficient to connect the entire optimum space.

## Assumptions and scope

Vertices of the chosen labelled graph are points \(p_i\) and lines \(\ell_j\), indexed modulo \(7\). Incidence is \(p_i\ell_j\in E(H)\) if and only if \(j-i\in\{0,1,3\}\pmod 7\). This describes all \(21\) edges of the simple cubic bipartite Heawood graph. For any subset \(C\), one-erasure robustness is equivalent to the two exact inequalities

\[
|N[v]\cap C|\ge2\quad(v\in V(H)),\qquad |(N[u]\triangle N[v])\cap C|\ge2\quad(u\ne v),
\]

where \(N[v]\) denotes the **closed** neighborhood. The first inequality ensures that a single detector deletion cannot empty a vertex signature; the second ensures that a deletion cannot make two distinct signatures equal. This is the redundant identifying-code (RED:IC) model of Jean and Seo, and **not** the stronger model that permits deletion of a graph vertex itself and its subsequent alteration of the neighborhoods. The result counts labelled vertex subsets, without quotienting by graph automorphisms.

A *quadrangle on a shore* means four points with no collinear triple, or dually four lines with no concurrent triple. An *induced two-edge matching* consists of two graph edges whose four endpoints induce precisely those two edges; this is not a maximum induced matching in \(H\), where three edges can be used.

## Proof

**Signature criterion.** For any distinct \(u,v\), the symmetric difference of their identifying signatures is \((N[u]\triangle N[v])\cap C\). Requiring the code after the deletion of each \(c\in C\) to have nonempty pairwise distinct signatures is equivalent to requiring both displayed quantities to have at least two elements. This equivalence is exact; no independent assumption of detectability is missing.

**Finite completeness of the minimum and polynomial.** Fix the \(14\)-bit encoding in `code/check_fano.py`: bit positions \(0\) through \(6\) are the points, and positions \(7\) through \(13\) are the lines. For each of the \(2^{14}=16384\) bitmasks, the checker constructs all \(14\) closed-neighborhood masks and all \(\binom{14}{2}=91\) symmetric-difference masks. It accepts precisely the masks having at least two selected bits in every one of these \(105\) masks. The exhaustive counts by cardinality are \((10,98),(11,224),(12,91),(13,14),(14,1)\), and no smaller cardinality occurs. A separate explicit scan of all \(\binom{14}{5}=2002\) five-element omissions finds no feasible complement. Since adding detectors preserves both inequalities, the latter excludes omitted sets of cardinality at least five. Thus the claimed minimum and full polynomial follow by a finite exhaustive proof over all possible labelled codes, not by interpolation or sampling.

**Geometric classification of all minima.** The same checker builds a catalogue of the \(14\) one-shore quadrangles and a separate catalogue of all induced two-edge matchings. The quadrangle count is \(7+7\): each four-point quadrangle is the complement of a unique line, with a dual statement for four-line quadrangles. For every fixed incidence edge \(p\ell\), the partner edge must have its point outside \(\ell\) (four choices) and its line through that point but not through \(p\) (two choices), producing \(21\cdot8/2=84\) two-edge induced matchings. The program compares the **complete sets of 14-bit masks**, not only their cardinalities, with every accepted ten-detector mask. It verifies equality of the union and the complete optimum set and verifies that the catalogue types are disjoint; this is a fully reproducible certificate for the finite implication from the signature inequalities to the classification.

**Exact mobility.** For each unordered pair of the \(98\) optimal masks \(x,y\), place an edge in \(\mathcal R_r\) precisely when the Hamming weight of \(x\oplus y\) is \(2r\). Construct all adjacency lists, exhaust all connected components, and run breadth-first search from **every** vertex to obtain all eccentricities and distance shells. The checker establishes for \(r=1\) the degree histogram \(14\) zeros and \(84\) fours, component multiset \(14\cdot1+1\cdot84\), and all \(84\) nontrivial shell vectors \((1,4,10,22,39,8)\). For \(r=2\), it establishes a single component of size \(98\), degree histogram \(14\) thirties and \(84\) twenty-twos, and all \(98\) shell vectors specified in the theorem. The result is an exact finite graph computation, not an assertion about larger projective planes.

## Verification

Two independently implemented standalone exhaustive programs are supplied. `code/check_fano.py` implements the mask-inequality characterization and constructs the graph using modular-seven incidence. `code/check_hamiltonian.cpp` instead constructs a fourteen-cycle plus seven non-cycle chords and **deletes each chosen detector explicitly**, retesting identifying signatures after every deletion. Both enumerate all \(2^{14}\) subsets, independently establish all cardinality counts and distinguish the geometric classes; both compute the two full exchange graphs and breadth-first metrics. The first checks full shell histograms; the second reproduces the same component, edge, degree and shell information in an independent graph labelling. Their expected outputs are included in `certificates/`.

Reproduce from a directory containing the supplied paths with `python3 code/check_fano.py`, and with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic code/check_hamiltonian.cpp -o heawood_check && ./heawood_check`. Both programs use only standard language libraries and terminate after finite exhaustive enumeration. Assertions constitute executable checks of the claimed values. The programs also use distinct graph representations, so a graph-labelling-specific enumeration error is less likely.

## Relationship to prior work

Jean and Seo (2021) define one-offline-detector redundant identifying codes and prove general bounds for special graph families, including cubic graphs; their general inequality does not determine this Heawood exact optimum, catalogue, or reconfiguration metrics. Earlier robust-identifying-code terminology of Honkala, Karpovsky and Levitin (2006) includes distinct failure conventions, sometimes imposing a stronger signature-distance constraint; it must not silently be identified with the model proved here. Balbuena, Foucaud and Hansberg (2014 preprint, 2015 journal) treat identifying and locating-dominating sets of graphs of girth at least five and prove that the Heawood graph's ordinary locating-domination number is six; that statement does not give the one-erasure identifying-code polynomial. The ordinary minimum identifying codes and their token-slide graph have also been examined separately; requiring the survival of a detector failure is a strictly stronger constraint and yields different feasible configurations and exchanges. The previously studied \(84\) **maximum three-edge** induced matchings of the Heawood graph must also not be confused with the \(84\) **two-edge** induced matchings that appear here as omitted vertex quartets.

## Limitations

The theorem concerns the one-erased-selected-detector model on this one finite labelled graph. It does not cover two detector failures, removal of graph vertices from the host network, or general projective planes. The proof and full metric are finite exhaustions with complete loops and independently checked representations; no symbolic infinite-family assertion is made. Historical priority may be affected by unindexed or inaccessible exact Heawood sensor-code tabulations. Independent scholarly audit has not been performed.

## References

- C. Balbuena, F. Foucaud, A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263v1 (first public July 27, 2014), and *Electronic Journal of Combinatorics* 22(2), P2.15 (2015), https://arxiv.org/abs/1407.7263.
- D. C. Jean and S. J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685 (2021), https://arxiv.org/abs/2112.01685.
- I. Honkala, M. Karpovsky, L. Levitin, *On Robust and Dynamic Identifying Codes*, 2006, https://sites.bu.edu/mark/files/2018/02/169.pdf.
- F. Foucaud et al., studies of minimum identifying codes in triangle-free graphs, arXiv:1010.5975 (2010), https://arxiv.org/abs/1010.5975.
