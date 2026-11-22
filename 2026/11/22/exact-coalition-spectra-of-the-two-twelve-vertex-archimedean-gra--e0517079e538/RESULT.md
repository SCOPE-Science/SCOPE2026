# Exact coalition spectra of the two twelve-vertex Archimedean graphs

## Finding

Let \(P_G(z)=\sum_{k=1}^{12}c_k(G)z^k\), where \(c_k(G)\) counts **unordered partitions of the fixed, labelled vertex set** into exactly \(k\) nonempty blocks, each block non-dominating and partnered with a distinct block whose union is dominating. For the cuboctahedral graph \(C=L(Q_3)\) and the truncated tetrahedral graph \(T\), both of order twelve,

\[
\begin{aligned}
P_C(z)&=24z^2+10128z^3+194733z^4+582874z^5\\
&\quad+378855z^6+47900z^7+762z^8,\\
P_T(z)&=171z^2+24846z^3+258625z^4+441384z^5\\
&\quad+153715z^6+7422z^7+93z^8.
\end{aligned}
\]

Consequently the ordinary coalition numbers are \(C(C)=C(T)=8\), but their numbers of maximum-block coalition partitions are respectively \(762\) and \(93\). The complete totals are \(1,215,276\) and \(886,256\). The cuboctahedral optimum partitions have block-size profiles \((1,1,1,1,1,1,3,3)\), \((1,1,1,1,1,2,2,3)\), and \((1,1,1,1,2,2,2,2)\), in multiplicities \(420,180,162\). The truncated tetrahedral optima have profiles \((1,1,1,1,1,1,3,3)\) and \((1,1,1,1,2,2,2,2)\), in multiplicities \(12,81\). Under their full automorphism groups, the optimum partitions comprise \(23\) and \(7\) orbits, respectively.

## Assumptions and scope

Graphs are finite, simple, undirected and vertex-labelled before partitioning. The vertex set of \(C\) is the twelve edges \(\{a,b\}\) of the three-dimensional binary cube on \(a,b\in\{0,\ldots,7\}\), where \(a\) and \(b\) differ in one bit; two vertices of \(C\) are adjacent precisely when the underlying cube edges have a common endpoint. The twelve vertices of \(T\) are ordered pairs \((a,b)\) of distinct elements of \(\{0,1,2,3\}\); two such vertices are adjacent when their first coordinates coincide or when they are reversals of each other. These definitions are, respectively, the cuboctahedral and truncated tetrahedral graphs, not their geometric faces or edge graphs. Their degrees are four and three. Neither graph has universal vertices, so the general exceptional single dominating vertex-block permitted by the coalition-partition definition cannot occur.

A block \(B\subseteq V(G)\) dominates when \(\bigcup_{v\in B}N[v]=V(G)\). Two disjoint **non-dominating** blocks form a coalition when their union dominates. A valid partition requires each block to have at least one coalition partner; blocks are *unlabelled*, even though graph vertices remain labelled. All polynomial coefficients are exact integers, not probabilities or estimates.

## Proof

**Dominance obstruction.** For \(B\subseteq V(G)\), define its undominated set
\[
M_G(B)=V(G)\setminus\bigcup_{v\in B}N[v].
\]
Then \(B\) is non-dominating exactly when \(M_G(B)\ne\varnothing\). Moreover, \(B_i\cup B_j\) dominates exactly when \(M_G(B_i)\cap M_G(B_j)=\varnothing\). Therefore a set partition \(\{B_1,\dots,B_k\}\) is valid exactly when all the \(M_G(B_i)\) are nonempty and each \(i\) has some distinct \(j\) with disjoint missed sets. These are necessary and sufficient conditions, not just necessary tests.

**Exhaustive exact certificate.** Every partition of a twelve-element vertex set has a unique restricted-growth sequence: vertex zero has block label zero, and each later vertex receives an existing label or the next unused label. The included `checker_rgs.cpp` visits each such sequence exactly once, computes all closed neighborhoods directly from the above graph definitions, and applies the preceding criterion. It visits exactly the twelfth Bell number \(4,213,597\) complete partitions for each graph, computing every coefficient and each block-size profile. Thus zero counts outside the displayed supports prove the upper bound \(C(G)\le8\), while the positive degree-eight coefficients prove attainment. The coefficients sum to the stated totals.

**Independent enumeration route.** The included `checker_subsets.cpp` instead takes the least unassigned vertex and recursively chooses every subset of the remaining vertices containing that vertex as its next block. It updates missed-set bitmasks by the recurrence \(M(B\cup\{v\})=M(B)\setminus N[v]\), and tests coalition partnerships through disjoint missed sets. The least-unassigned choice again creates each unordered partition exactly once, but with a different enumeration and domination implementation. It reproduces every coefficient and the optimum profiles and writes all optima as collections of twelve-bit block masks. Full certificates are in `opt_cubo.txt` and `opt_trunc.txt`.

**Symmetry classification.** For the cube, coordinate permutations and bit-flips give the full group of \(48\) automorphisms, acting on its edges and thence on cuboctahedral vertices. For the truncated tetrahedron, the \(24\) root-label permutations act on its ordered-pair vertices and give its full automorphism group. `orbits.py` applies these explicitly defined permutations to every enumerated optimum. It checks that each orbit is contained in the complete enumerated set and removes disjoint orbits until no optima remain. The resulting \(23\) and \(7\) orbits, including representatives and stabilizer-implied orbit sizes, are reproduced in `orbit_cubo.json` and `orbit_trunc.json`. The orbit sizes add to \(762\) and \(93\), respectively. This proves the stated orbit counts for these groups.

## Verification

Run `sh verify.sh` in the extracted artifact directory with a C++17 compiler and Python 3. The script compiles the two enumeration implementations, regenerates the two count tables and the complete optimum lists, reruns the symmetry analysis, and checks the stated counts, profiles and group orders. Its success marker is `COALITION_PAIR_VERIFY_OK`. The output files `rgs_cubo.txt`, `rgs_trunc.txt`, `opt_cubo.txt`, `opt_trunc.txt`, `orbit_cubo.json`, `orbit_trunc.json`, and `orbit_summary.txt` accompany the code. The two exact enumerators agree on all counting coefficients. All enumeration loops terminate over explicitly finite sets. The code is a reproducible exhaustive certificate of this finite statement; a claimed all-orders theorem is not inferred from tests.

## Relationship to prior work

Haynes, Hedetniemi, Hedetniemi, McRae and Mohan introduced ordinary graph coalitions and coalition partitions, with first public online publication October 26, 2020. Alikhani, Golmohammadi and Konstantinova determined coalition numbers of cubic graphs **of order at most ten**; their classification does not include the twelve-vertex cubic truncated tetrahedral graph and supplies no complete partition polynomials. Besharati, Emadi and Masoumi studied edge coalition partitions; the identity between an edge coalition partition of the cube \(Q_3\) and a vertex coalition partition of its line graph \(C=L(Q_3)\) is relevant, but their inspected 2026 text presents results for paths, cycles, complete graphs, trees and other stated classes rather than a cube census. General maximum-degree upper bounds do not determine either polynomial or optimum orbit structure. Related exact computations of other invariants on these two graphs, such as second-independence homotopy, do not imply a coalition-partition census. These comparisons do not constitute exhaustive proof of historical priority.

## Limitations

This is a self-contained, finite, computer-assisted classification for two specified twelve-vertex graphs only. It does not give a formula for all Archimedean graphs or arbitrary line graphs, nor does it establish novelty independently of the checked literature. The automorphism orbit counts use the explicit full graph automorphism groups and are not counts of unlabelled graph isomorphism classes. The algorithms and outputs are reproducible; independent scholarly audit has not been performed.

## References

1. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae and R. Mohan, *Introduction to coalitions in graphs*, published online October 26, 2020. https://doi.org/10.1080/09728600.2020.1832874
2. S. Alikhani, H. R. Golmohammadi and E. V. Konstantinova, *Coalition of cubic graphs of order at most 10*, arXiv:2212.10004 (first version December 20, 2022). https://arxiv.org/abs/2212.10004
3. N. Besharati, A. S. Emadi and I. Masoumi, *Edge Coalitions in Graphs*, arXiv:2302.10926 (inspected version 2, July 2026). https://arxiv.org/abs/2302.10926
4. E. W. Weisstein, *Cuboctahedral Graph* and *Truncated Tetrahedral Graph*, MathWorld. https://mathworld.wolfram.com/CuboctahedralGraph.html ; https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html
